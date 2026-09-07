"""BigQuery storage layer.

Handles all BigQuery I/O. Pipelines don't call BigQuery directly.
This layer provides typed read/write for all schema objects.

BigQuery project: from agent-vault (GOOGLE_CLOUD_PROJECT)
BigQuery dataset: drop

Credentials: OAuth2 from agent-vault (GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)
"""

from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel


# BigQuery config — use agent-vault credentials
DATASET = "drop"

# Table names — must match actual BigQuery table names
TABLES = {
    "observations": "fact_market_observation",
    "hypotheses": "fact_decision_event",  # Using decision events as proxy
    "kernels": "fact_market_observation",  # Kernels stored as observations
    "candidates": "products",  # Using products table as proxy
    "probe_results": "probe_reports",
    "graph_nodes": "graph_nodes",
    "graph_edges": "graph_edges",
    "graph_observations": "graph_observations",
}


class BigQueryStorage:
    """BigQuery read/write for all schema objects.

    Usage:
        storage = BigQueryStorage()
        storage.write_observation(observation)
        observations = storage.read_observations(candidate_id="NO-TESTO-550S-001")
    """

    def __init__(self, project_id: Optional[str] = None, dataset: str = DATASET):
        self.project_id = project_id or os.environ.get("GCP_PROJECT_ID", "")
        self.dataset = dataset
        self._client = None

    @property
    def client(self):
        """Lazy-load BigQuery client."""
        if self._client is None:
            try:
                from google.cloud import bigquery

                self._client = bigquery.Client(project=self.project_id)
            except ImportError:
                raise ImportError(
                    "google-cloud-bigquery not installed. "
                    "Run: pip install google-cloud-bigquery"
                )
        return self._client

    def _table_ref(self, table_name: str) -> str:
        """Get full table reference."""
        return f"{self.project_id}.{self.dataset}.{table_name}"

    def _to_bq_row(self, model: BaseModel) -> dict:
        """Convert Pydantic model to BigQuery-compatible dict."""
        data = model.model_dump()
        # Convert datetime to ISO string for BigQuery
        for key, value in list(data.items()):
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            elif isinstance(value, dict):
                data[key] = json.dumps(value)
            elif isinstance(value, list):
                # Keep lists as-is for ArrayQueryParameter handling
                pass
            # Convert enums to strings
            elif hasattr(value, 'value'):
                data[key] = value.value
        
        # Map schema field names to BigQuery column names
        if hasattr(model, 'observation_id'):  # Observation
            data['field_name'] = data.pop('field', None)
            value = data.pop('value', None)
            data['field_value'] = str(value) if value is not None else None
            # Ensure field_value_numeric is actually numeric or None
            if isinstance(value, (int, float)):
                data['field_value_numeric'] = float(value)
            else:
                data['field_value_numeric'] = None
            data['source_type'] = data.pop('source', None)
            # Remove fields not in BigQuery table
            for key in ['unit', 'raw_snapshot', 'event_time', 'published_at', 'available_at']:
                data.pop(key, None)
        
        return data

    def _insert_row(self, table_name: str, row: dict) -> None:
        """Insert a single row using parameterized query (avoids insert_rows_json permission issues)."""
        table_ref = self._table_ref(table_name)
        columns = ", ".join(row.keys())
        param_names = ", ".join([f"@{k}" for k in row.keys()])
        
        # Build parameterized query
        query = f"INSERT INTO `{table_ref}` ({columns}) VALUES ({param_names})"
        
        # Build parameters with correct types
        from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter, ArrayQueryParameter
        params = []
        for k, v in row.items():
            if isinstance(v, bool):
                params.append(ScalarQueryParameter(k, "BOOL", v))
            elif isinstance(v, int):
                params.append(ScalarQueryParameter(k, "INT64", v))
            elif isinstance(v, float):
                params.append(ScalarQueryParameter(k, "FLOAT64", v))
            elif isinstance(v, list):
                # Arrays need ArrayQueryParameter
                params.append(ArrayQueryParameter(k, "STRING", v if v else []))
            elif isinstance(v, str):
                # Try to parse as timestamp
                if "T" in v and ("Z" in v or "+" in v):
                    params.append(ScalarQueryParameter(k, "TIMESTAMP", v))
                else:
                    params.append(ScalarQueryParameter(k, "STRING", v))
            elif v is None:
                params.append(ScalarQueryParameter(k, "STRING", None))
            else:
                params.append(ScalarQueryParameter(k, "STRING", str(v)))
        
        job_config = QueryJobConfig(query_parameters=params)
        self.client.query(query, job_config=job_config).result()

    # --- Observations ---

    def write_observation(self, observation) -> None:
        """Write a single observation to BigQuery."""
        table_ref = self._table_ref(TABLES["observations"])
        row = self._to_bq_row(observation)
        # Use query-based insert (insert_rows_json has permission issues)
        self._insert_row(TABLES["observations"], row)

    def write_observations(self, observations: list) -> int:
        """Write multiple observations to BigQuery. Returns count written."""
        if not observations:
            return 0
        for obs in observations:
            self.write_observation(obs)
        return len(observations)

    def read_observations(
        self,
        candidate_id: Optional[str] = None,
        hypothesis_id: Optional[str] = None,
        entity_type: Optional[str] = None,
        limit: int = 100,
    ) -> list[dict]:
        """Read observations from BigQuery with optional filters."""
        conditions = []
        params = {}

        if candidate_id:
            conditions.append("candidate_id = @candidate_id")
            params["candidate_id"] = candidate_id
        if hypothesis_id:
            conditions.append("hypothesis_id = @hypothesis_id")
            params["hypothesis_id"] = hypothesis_id
        if entity_type:
            conditions.append("entity_type = @entity_type")
            params["entity_type"] = entity_type

        where = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
            SELECT * FROM `{self._table_ref(TABLES['observations'])}`
            {where}
            ORDER BY observed_at DESC
            LIMIT {limit}
        """

        # Build QueryJobConfig with parameters
        job_config = None
        if params:
            from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
            job_config = QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(name, "STRING", value)
                    for name, value in params.items()
                ]
            )

        job = self.client.query(query, job_config=job_config)
        return [dict(row) for row in job.result()]

    # --- Hypotheses ---

    def write_hypothesis(self, hypothesis) -> None:
        """Write a single hypothesis to BigQuery."""
        self._insert_row(TABLES["hypotheses"], self._to_bq_row(hypothesis))

    def read_hypotheses(
        self,
        state: Optional[str] = None,
        candidate_id: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Read hypotheses from BigQuery."""
        conditions = []
        params = {}

        if state:
            conditions.append("state = @state")
            params["state"] = state
        if candidate_id:
            conditions.append("candidate_id = @candidate_id")
            params["candidate_id"] = candidate_id

        where = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
            SELECT * FROM `{self._table_ref(TABLES['hypotheses'])}`
            {where}
            ORDER BY created_at DESC
            LIMIT {limit}
        """

        job_config = None
        if params:
            from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
            job_config = QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(name, "STRING", value)
                    for name, value in params.items()
                ]
            )

        job = self.client.query(query, job_config=job_config)
        return [dict(row) for row in job.result()]

    # --- Kernels ---

    def write_kernel(self, kernel) -> None:
        """Write a single kernel to BigQuery."""
        self._insert_row(TABLES["kernels"], self._to_bq_row(kernel))

    def read_kernels(
        self,
        candidate_id: Optional[str] = None,
        kernel_type: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Read kernels from BigQuery."""
        conditions = []
        params = {}

        if candidate_id:
            conditions.append("candidate_id = @candidate_id")
            params["candidate_id"] = candidate_id
        if kernel_type:
            conditions.append("kernel_type = @kernel_type")
            params["kernel_type"] = kernel_type

        where = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
            SELECT * FROM `{self._table_ref(TABLES['kernels'])}`
            {where}
            ORDER BY created_at DESC
            LIMIT {limit}
        """

        job_config = None
        if params:
            from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
            job_config = QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(name, "STRING", value)
                    for name, value in params.items()
                ]
            )

        job = self.client.query(query, job_config=job_config)
        return [dict(row) for row in job.result()]

    # --- Candidates ---

    def write_candidate(self, candidate) -> None:
        """Write a single candidate to BigQuery."""
        self._insert_row(TABLES["candidates"], self._to_bq_row(candidate))

    def read_candidates(
        self,
        state: Optional[str] = None,
        country_code: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Read candidates from BigQuery."""
        conditions = []
        params = {}

        if state:
            conditions.append("state = @state")
            params["state"] = state
        if country_code:
            conditions.append("country_code = @country_code")
            params["country_code"] = country_code

        where = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
            SELECT * FROM `{self._table_ref(TABLES['candidates'])}`
            {where}
            ORDER BY updated_at DESC
            LIMIT {limit}
        """

        job_config = None
        if params:
            from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
            job_config = QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(name, "STRING", value)
                    for name, value in params.items()
                ]
            )

        job = self.client.query(query, job_config=job_config)
        return [dict(row) for row in job.result()]

    # --- Probe Results ---

    def write_probe_result(self, probe_result) -> None:
        """Write a single probe result to BigQuery."""
        self._insert_row(TABLES["probe_results"], self._to_bq_row(probe_result))

    # --- Graph ---

    def write_graph_node(self, node_id: str, node_type: str, properties: dict, confidence: float = 1.0) -> None:
        """Write a node to the knowledge graph."""
        row = {
            "node_id": node_id,
            "node_type": node_type,
            "properties_json": json.dumps(properties),
            "confidence": confidence,
        }
        self._insert_row(TABLES["graph_nodes"], row)

    def write_graph_edge(self, source: str, target: str, edge_type: str, weight: float = 1.0) -> None:
        """Write an edge to the knowledge graph."""
        row = {
            "source_node": source,
            "target_node": target,
            "edge_type": edge_type,
            "weight": weight,
        }
        self._insert_row(TABLES["graph_edges"], row)

    def write_graph_observation(self, node_id: str, metric_name: str, metric_value: float, evidence_type: str = "OBSERVED", source: str = "") -> None:
        """Write an observation to the knowledge graph."""
        row = {
            "node_id": node_id,
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "metric_name": metric_name,
            "metric_value": metric_value,
            "evidence_type": evidence_type,
            "source": source,
        }
        self._insert_row(TABLES["graph_observations"], row)

    # --- Generic query ---

    def query(self, sql: str, params: Optional[dict] = None) -> list[dict]:
        """Run an arbitrary SQL query. Returns list of dicts."""
        job_config = None
        if params:
            from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
            job_config = QueryJobConfig(
                query_parameters=[
                    ScalarQueryParameter(name, "STRING", value)
                    for name, value in params.items()
                ]
            )
        job = self.client.query(sql, job_config=job_config)
        return [dict(row) for row in job.result()]
