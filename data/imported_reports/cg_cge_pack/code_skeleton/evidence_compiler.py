"""Evidence compiler skeleton.

The production implementation should use the BigQuery client, but the key
contract is: only VERIFIED observations are allowed into the bundle.
"""
from __future__ import annotations
import hashlib, json

def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode()

def content_id(prefix: str, obj: object) -> str:
    return f"{prefix}_{hashlib.sha256(canonical_bytes(obj)).hexdigest()}"

def compile_manifest(campaign_version_id: str, rubric_version_id: str,
                     evidence_rows: list[dict], as_of: str,
                     compiler_version: str = "1") -> dict:
    bad = [r for r in evidence_rows if r.get("verification_state") != "VERIFIED"]
    if bad:
        raise ValueError("unverified evidence cannot enter CG bundle")

    ids = sorted(r["evidence_id"] for r in evidence_rows)
    core = {
        "campaign_version_id": campaign_version_id,
        "rubric_version_id": rubric_version_id,
        "as_of": as_of,
        "compiler_version": compiler_version,
        "evidence_ids": ids,
    }
    core["evidence_snapshot_id"] = content_id("es", core)
    return core
