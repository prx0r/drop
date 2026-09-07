"""Local JSON storage layer.

For fast iteration and testing.
Data is stored as JSON files in /root/drop/data/.

This is NOT the source of truth — BigQuery is.
Local storage is for:
- Fast reads during development
- Caching probe results
- Storing ephemeral state
- Testing pipelines without BigQuery
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel


DATA_DIR = Path("/root/drop/data")
PROBES_DIR = Path("/root/drop/data/probes")


class LocalStorage:
    """Local JSON read/write for all schema objects.

    Usage:
        storage = LocalStorage()
        storage.write_observation(observation)
        observations = storage.read_observations(candidate_id="NO-TESTO-550S-001")
    """

    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = data_dir
        self.probes_dir = data_dir / "probes"
        self.probes_dir.mkdir(parents=True, exist_ok=True)

    def _entity_dir(self, entity_type: str) -> Path:
        """Get directory for an entity type."""
        d = self.data_dir / entity_type
        d.mkdir(parents=True, exist_ok=True)
        return d

    def _write_json(self, path: Path, data: Any) -> None:
        """Write data to JSON file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def _read_json(self, path: Path) -> Any:
        """Read data from JSON file."""
        if not path.exists():
            return None
        with open(path) as f:
            return json.load(f)

    # --- Observations ---

    def write_observation(self, observation) -> str:
        """Write a single observation. Returns the observation_id."""
        obs_dir = self._entity_dir("observations")
        obs_id = observation.observation_id
        path = obs_dir / f"{obs_id}.json"
        self._write_json(path, observation.model_dump())
        return obs_id

    def write_observations(self, observations: list) -> list[str]:
        """Write multiple observations. Returns list of observation_ids."""
        return [self.write_observation(obs) for obs in observations]

    def read_observations(
        self,
        candidate_id: Optional[str] = None,
        hypothesis_id: Optional[str] = None,
    ) -> list[dict]:
        """Read observations with optional filters."""
        obs_dir = self._entity_dir("observations")
        results = []
        for path in obs_dir.glob("*.json"):
            data = self._read_json(path)
            if data is None:
                continue
            if candidate_id and data.get("candidate_id") != candidate_id:
                continue
            if hypothesis_id and data.get("hypothesis_id") != hypothesis_id:
                continue
            results.append(data)
        return results

    # --- Hypotheses ---

    def write_hypothesis(self, hypothesis) -> str:
        """Write a single hypothesis. Returns the hypothesis_id."""
        hyp_dir = self._entity_dir("hypotheses")
        hyp_id = hypothesis.hypothesis_id
        path = hyp_dir / f"{hyp_id}.json"
        self._write_json(path, hypothesis.model_dump())
        return hyp_id

    def read_hypotheses(
        self,
        state: Optional[str] = None,
        candidate_id: Optional[str] = None,
    ) -> list[dict]:
        """Read hypotheses with optional filters."""
        hyp_dir = self._entity_dir("hypotheses")
        results = []
        for path in hyp_dir.glob("*.json"):
            data = self._read_json(path)
            if data is None:
                continue
            if state and data.get("state") != state:
                continue
            if candidate_id and data.get("candidate_id") != candidate_id:
                continue
            results.append(data)
        return results

    # --- Kernels ---

    def write_kernel(self, kernel) -> str:
        """Write a single kernel. Returns the kernel_id."""
        kern_dir = self._entity_dir("kernels")
        kern_id = kernel.kernel_id
        path = kern_dir / f"{kern_id}.json"
        self._write_json(path, kernel.model_dump())
        return kern_id

    def read_kernels(
        self,
        candidate_id: Optional[str] = None,
        kernel_type: Optional[str] = None,
    ) -> list[dict]:
        """Read kernels with optional filters."""
        kern_dir = self._entity_dir("kernels")
        results = []
        for path in kern_dir.glob("*.json"):
            data = self._read_json(path)
            if data is None:
                continue
            if candidate_id and data.get("candidate_id") != candidate_id:
                continue
            if kernel_type and data.get("kernel_type") != kernel_type:
                continue
            results.append(data)
        return results

    # --- Candidates ---

    def write_candidate(self, candidate) -> str:
        """Write a single candidate. Returns the candidate_id."""
        cand_dir = self._entity_dir("candidates")
        cand_id = candidate.candidate_id
        path = cand_dir / f"{cand_id}.json"
        self._write_json(path, candidate.model_dump())
        return cand_id

    def read_candidates(
        self,
        state: Optional[str] = None,
        country_code: Optional[str] = None,
    ) -> list[dict]:
        """Read candidates with optional filters."""
        cand_dir = self._entity_dir("candidates")
        results = []
        for path in cand_dir.glob("*.json"):
            data = self._read_json(path)
            if data is None:
                continue
            if state and data.get("state") != state:
                continue
            if country_code and data.get("country_code") != country_code:
                continue
            results.append(data)
        return results

    # --- Probe Results ---

    def write_probe_result(self, probe_result) -> str:
        """Write a single probe result. Returns the run_id."""
        probe_dir = self._entity_dir("probe_results")
        run_id = probe_result.run_id
        path = probe_dir / f"{run_id}.json"
        self._write_json(path, probe_result.model_dump())
        return run_id

    def read_probe_results(
        self,
        probe_id: Optional[str] = None,
        candidate_id: Optional[str] = None,
    ) -> list[dict]:
        """Read probe results with optional filters."""
        probe_dir = self._entity_dir("probe_results")
        results = []
        for path in probe_dir.glob("*.json"):
            data = self._read_json(path)
            if data is None:
                continue
            if probe_id and data.get("probe_id") != probe_id:
                continue
            if candidate_id and data.get("candidate_id") != candidate_id:
                continue
            results.append(data)
        return results

    # --- Generic ---

    def write_raw(self, entity_type: str, entity_id: str, data: dict) -> None:
        """Write raw data to an entity type."""
        entity_dir = self._entity_dir(entity_type)
        path = entity_dir / f"{entity_id}.json"
        self._write_json(path, data)

    def read_raw(self, entity_type: str, entity_id: str) -> Optional[dict]:
        """Read raw data from an entity type."""
        entity_dir = self.data_dir / entity_type
        path = entity_dir / f"{entity_id}.json"
        return self._read_json(path)

    def list_entities(self, entity_type: str) -> list[str]:
        """List all entity IDs for a type."""
        entity_dir = self.data_dir / entity_type
        if not entity_dir.exists():
            return []
        return [p.stem for p in entity_dir.glob("*.json")]
