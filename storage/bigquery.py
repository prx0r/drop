"""BigQuery storage layer.

Handles all BigQuery I/O. Pipelines don't call BigQuery directly.
This layer provides typed read/write for all schema objects.

BigQuery project: project-ff2366d2-8fda-4fcb-9ba
BigQuery dataset: drop
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel


# BigQuery config — use environment variables or agent-vault
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "")
DATASET = os.environ.get("GCP_DATASET", "drop")

# Table names
TABLES = {
    "observations": "observations",
    "hypotheses": "hypotheses",
    "kernels": "kernels",
    "candidates": "candidates",
    "probe_results": "probe_results",
    "unknowns": "unknowns",
    "evidence_updates": "evidence_updates",
    "state_transitions": "state_transitions",
    "graph_nodes": "graph_nodes",
    "graph_edges": "graph_edges",
    "graph_observations": "graph_observations",
    "products": "products",
    "sources": "sources",
}


class BigQueryStorage:
    """BigQuery read/write for all schema objects.

    Usage:
        storage = BigQueryStorage()
        storage.write_observation(observation)
        observations = storage.read_observations(candidate_id="NO-TESTO-550S-001")
    """

    def __init__(self, project_id: str = PROJECT_ID, dataset: str = DATASET):
        self.project_id = project_id
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
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            elif isinstance(value, dict):
                data[key] = json.dumps(value)
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                data[key] = json.dumps(value)
        return data

    # --- Observations ---

    def write_observation(self, observation) -> None:
        """Write a single observation to BigQuery."""
        table_ref = self._table_ref(TABLES["observations"])
        row = self._to_bq_row(observation)
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

    def write_observations(self, observations: list) -> int:
        """Write multiple observations to BigQuery. Returns count written."""
        if not observations:
            return 0
        table_ref = self._table_ref(TABLES["observations"])
        rows = [self._to_bq_row(obs) for obs in observations]
        errors = self.client.insert_rows_json(table_ref, rows)
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")
        return len(rows)

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
        table_ref = self._table_ref(TABLES["hypotheses"])
        row = self._to_bq_row(hypothesis)
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

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
        table_ref = self._table_ref(TABLES["kernels"])
        row = self._to_bq_row(kernel)
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

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

        job = self.client.query(query)
        return [dict(row) for row in job.result()]

    # --- Candidates ---

    def write_candidate(self, candidate) -> None:
        """Write a single candidate to BigQuery."""
        table_ref = self._table_ref(TABLES["candidates"])
        row = self._to_bq_row(candidate)
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

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

        job = self.client.query(query)
        return [dict(row) for row in job.result()]

    # --- Probe Results ---

    def write_probe_result(self, probe_result) -> None:
        """Write a single probe result to BigQuery."""
        table_ref = self._table_ref(TABLES["probe_results"])
        row = self._to_bq_row(probe_result)
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

    # --- Graph ---

    def write_graph_node(self, node_id: str, node_type: str, properties: dict, confidence: float = 1.0) -> None:
        """Write a node to the knowledge graph."""
        table_ref = self._table_ref(TABLES["graph_nodes"])
        row = {
            "node_id": node_id,
            "node_type": node_type,
            "properties_json": json.dumps(properties),
            "confidence": confidence,
        }
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

    def write_graph_edge(self, source: str, target: str, edge_type: str, weight: float = 1.0) -> None:
        """Write an edge to the knowledge graph."""
        table_ref = self._table_ref(TABLES["graph_edges"])
        row = {
            "source_node": source,
            "target_node": target,
            "edge_type": edge_type,
            "weight": weight,
        }
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

    def write_graph_observation(self, node_id: str, metric_name: str, metric_value: float, evidence_type: str = "OBSERVED", source: str = "") -> None:
        """Write an observation to the knowledge graph."""
        table_ref = self._table_ref(TABLES["graph_observations"])
        row = {
            "node_id": node_id,
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "metric_name": metric_name,
            "metric_value": metric_value,
            "evidence_type": evidence_type,
            "source": source,
        }
        errors = self.client.insert_rows_json(table_ref, [row])
        if errors:
            raise RuntimeError(f"BigQuery insert failed: {errors}")

    # --- Generic query ---

    def query(self, sql: str, params: Optional[dict] = None) -> list[dict]:
        """Run an arbitrary SQL query. Returns list of dicts."""
        job = self.client.query(sql, job_config=None)
        return [dict(row) for row in job.result()]
