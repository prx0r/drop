from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from .db import DB


def record_observation(db: DB, app: str, entity_type: str, entity_id: str, payload: dict, source_url: str | None = None, observed_at: str | None = None) -> int:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    when = observed_at or datetime.now(timezone.utc).isoformat()
    return db.execute(
        "INSERT INTO provenance(app,entity_type,entity_id,source_url,observed_at,content_hash,payload_json) VALUES(?,?,?,?,?,?,?)",
        (app, entity_type, entity_id, source_url, when, digest, canonical),
    )
