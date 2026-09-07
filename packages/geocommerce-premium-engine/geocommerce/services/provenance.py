from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from ..db import connect, jdump

def now_iso(): return datetime.now(timezone.utc).isoformat()

def record(entity_type:str, entity_key:str, source:str, payload:dict, source_url:str|None=None, observed_at:str|None=None):
    raw=jdump(payload); digest=hashlib.sha256(raw.encode()).hexdigest(); observed_at=observed_at or now_iso()
    with connect() as c:
        c.execute('INSERT INTO provenance_events(entity_type,entity_key,source,source_url,observed_at,payload_hash,payload_json) VALUES(?,?,?,?,?,?,?)',(entity_type,entity_key,source,source_url,observed_at,digest,raw))
    return digest
