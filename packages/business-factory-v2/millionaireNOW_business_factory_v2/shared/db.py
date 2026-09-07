from __future__ import annotations
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  app TEXT NOT NULL,
  event_type TEXT NOT NULL,
  entity_id TEXT,
  payload_json TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_events_app_type ON events(app, event_type);

CREATE TABLE IF NOT EXISTS provenance (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  app TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  source_url TEXT,
  observed_at TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_provenance_lookup ON provenance(app, entity_type, entity_id, observed_at);
"""

class DB:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as con:
            con.executescript(SCHEMA)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row
        try:
            yield con
            con.commit()
        finally:
            con.close()

    def execute(self, sql: str, params: tuple[Any, ...] = ()) -> int:
        with self.connect() as con:
            cur = con.execute(sql, params)
            return int(cur.lastrowid or 0)

    def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict]:
        with self.connect() as con:
            return [dict(r) for r in con.execute(sql, params).fetchall()]

    def event(self, app: str, event_type: str, entity_id: str | None, payload: dict) -> int:
        return self.execute(
            "INSERT INTO events(app,event_type,entity_id,payload_json) VALUES(?,?,?,?)",
            (app, event_type, entity_id, json.dumps(payload, sort_keys=True, default=str)),
        )
