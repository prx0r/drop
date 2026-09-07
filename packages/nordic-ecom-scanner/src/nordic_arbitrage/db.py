from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT NOT NULL,
    niche TEXT NOT NULL,
    product_name TEXT NOT NULL,
    competitor_price_local REAL NOT NULL,
    supplier_price_usd_low REAL NOT NULL,
    supplier_price_usd_high REAL NOT NULL,
    supplier_moq INTEGER NOT NULL,
    match_quality TEXT NOT NULL,
    competitor_source TEXT NOT NULL,
    supplier_source TEXT NOT NULL,
    monthly_searches REAL DEFAULT 0,
    cpc_local REAL DEFAULT 0,
    assumed_cvr REAL DEFAULT 0.02,
    merchant_count INTEGER DEFAULT 8,
    dominant_merchant_share REAL DEFAULT 0.25,
    creative_gap REAL DEFAULT 0.5,
    title_gap REAL DEFAULT 0.5,
    b2b_multiplier REAL DEFAULT 0,
    bundle_multiplier REAL DEFAULT 0,
    regulated_risk REAL DEFAULT 0,
    fragility_risk REAL DEFAULT 0,
    bulky_risk REAL DEFAULT 0,
    expected_return_rate REAL DEFAULT 0.06,
    estimated_delivery_days INTEGER DEFAULT 7,
    has_local_payment INTEGER DEFAULT 1,
    has_local_return_address INTEGER DEFAULT 0,
    landed_cost_local REAL,
    target_price_local REAL,
    expected_units_per_order REAL DEFAULT 1,
    notes TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS scores (
    candidate_id INTEGER PRIMARY KEY,
    score_total REAL NOT NULL,
    gate TEXT NOT NULL,
    reason TEXT NOT NULL,
    economics_json TEXT NOT NULL,
    breakdown_json TEXT NOT NULL,
    scored_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT NOT NULL,
    country TEXT NOT NULL,
    query TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    observed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def db_path() -> str:
    return os.getenv("ECSCAN_DB", "scanner.sqlite")


def connect(path: str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(path or db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(path: str | None = None) -> None:
    with connect(path) as conn:
        conn.executescript(SCHEMA)


def save_observation(provider: str, country: str, query: str, payload: dict, path: str | None = None) -> None:
    with connect(path) as conn:
        conn.execute(
            "INSERT INTO observations(provider,country,query,payload_json) VALUES (?,?,?,?)",
            (provider, country, query, json.dumps(payload, ensure_ascii=False)),
        )
