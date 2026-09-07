from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
from .models import ProductObservation, ScoreBreakdown

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS runs (
  id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL,
  completed_at TEXT,
  markets_json TEXT NOT NULL,
  sources_json TEXT NOT NULL,
  status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS observations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  product_slug TEXT NOT NULL,
  market TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  UNIQUE(run_id, product_slug, market)
);
CREATE TABLE IF NOT EXISTS scores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  product_slug TEXT NOT NULL,
  market TEXT NOT NULL,
  total_score REAL NOT NULL,
  verdict TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  UNIQUE(run_id, product_slug, market)
);
CREATE INDEX IF NOT EXISTS idx_scores_market_score ON scores(market, total_score DESC);
CREATE INDEX IF NOT EXISTS idx_scores_run ON scores(run_id);
"""


class Database:
    def __init__(self, path: str):
        self.path = path
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def start_run(self, run_id: str, markets: list[str], sources: list[str]) -> None:
        self.conn.execute(
            "INSERT INTO runs(id, started_at, markets_json, sources_json, status) VALUES(?,?,?,?,?)",
            (run_id, datetime.now(timezone.utc).isoformat(), json.dumps(markets), json.dumps(sources), "running"),
        )
        self.conn.commit()

    def finish_run(self, run_id: str, status: str = "complete") -> None:
        self.conn.execute(
            "UPDATE runs SET completed_at=?, status=? WHERE id=?",
            (datetime.now(timezone.utc).isoformat(), status, run_id),
        )
        self.conn.commit()

    def save_observation(self, run_id: str, obs: ProductObservation) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO observations(run_id,product_slug,market,payload_json) VALUES(?,?,?,?)",
            (run_id, obs.product_slug, obs.market, obs.model_dump_json()),
        )
        self.conn.commit()

    def save_score(self, run_id: str, score: ScoreBreakdown) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO scores(run_id,product_slug,market,total_score,verdict,payload_json) VALUES(?,?,?,?,?,?)",
            (run_id, score.product_slug, score.market, score.total_score, score.verdict, score.model_dump_json()),
        )
        self.conn.commit()

    def latest_scores(self, market: str | None = None, limit: int = 100) -> list[dict]:
        if market:
            rows = self.conn.execute(
                "SELECT payload_json FROM scores WHERE run_id=(SELECT id FROM runs WHERE status='complete' ORDER BY completed_at DESC LIMIT 1) AND market=? ORDER BY total_score DESC LIMIT ?",
                (market, limit),
            ).fetchall()
        else:
            rows = self.conn.execute(
                "SELECT payload_json FROM scores WHERE run_id=(SELECT id FROM runs WHERE status='complete' ORDER BY completed_at DESC LIMIT 1) ORDER BY total_score DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [json.loads(r["payload_json"]) for r in rows]

    def list_runs(self, limit: int = 20) -> list[dict]:
        rows = self.conn.execute("SELECT * FROM runs ORDER BY started_at DESC LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]
