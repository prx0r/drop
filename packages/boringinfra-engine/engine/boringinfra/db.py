import sqlite3
from pathlib import Path
from .models import Opportunity

SCHEMA = """
CREATE TABLE IF NOT EXISTS opportunities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  pattern TEXT NOT NULL,
  niche TEXT NOT NULL,
  problem TEXT NOT NULL,
  economic_event TEXT NOT NULL,
  verified_revenue_signal REAL NOT NULL,
  wtp REAL NOT NULL,
  recurrence REAL NOT NULL,
  build_simplicity REAL NOT NULL,
  data_access REAL NOT NULL,
  distribution REAL NOT NULL,
  localization REAL NOT NULL,
  gross_margin REAL NOT NULL,
  competition_gap REAL NOT NULL,
  workflow_criticality REAL NOT NULL,
  platform_risk REAL NOT NULL,
  support_burden REAL NOT NULL,
  regulatory_burden REAL NOT NULL,
  notes TEXT DEFAULT ''
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_opportunity ON opportunities(name, niche);
"""

FIELDS = [
    "name","pattern","niche","problem","economic_event","verified_revenue_signal","wtp","recurrence",
    "build_simplicity","data_access","distribution","localization","gross_margin","competition_gap",
    "workflow_criticality","platform_risk","support_burden","regulatory_burden","notes"
]


def connect(path: str):
    p = Path(path)
    conn = sqlite3.connect(p)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def upsert(conn, op: Opportunity):
    cols = ",".join(FIELDS)
    placeholders = ",".join("?" for _ in FIELDS)
    updates = ",".join(f"{f}=excluded.{f}" for f in FIELDS[2:])
    vals = [getattr(op, f) for f in FIELDS]
    conn.execute(
        f"INSERT INTO opportunities ({cols}) VALUES ({placeholders}) "
        f"ON CONFLICT(name,niche) DO UPDATE SET {updates}", vals
    )
    conn.commit()


def all_ops(conn):
    rows = conn.execute("SELECT * FROM opportunities").fetchall()
    return [Opportunity(**dict(r)) for r in rows]
