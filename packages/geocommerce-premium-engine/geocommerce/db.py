from __future__ import annotations
import json, sqlite3, threading
from contextlib import contextmanager
from pathlib import Path
from .settings import settings

_SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS schema_meta(version INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS products(
 id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
 category TEXT NOT NULL, supplier_cost REAL NOT NULL, supplier_currency TEXT NOT NULL,
 supplier_id TEXT NOT NULL, supplier_url TEXT, images_json TEXT NOT NULL, facts_json TEXT NOT NULL,
 created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS market_signals(
 id INTEGER PRIMARY KEY AUTOINCREMENT, product_slug TEXT NOT NULL, market_code TEXT NOT NULL,
 query TEXT NOT NULL, payload_json TEXT NOT NULL, observed_at TEXT NOT NULL,
 UNIQUE(product_slug, market_code, query, observed_at)
);
CREATE TABLE IF NOT EXISTS supplier_offers(
 id INTEGER PRIMARY KEY AUTOINCREMENT, product_slug TEXT NOT NULL, supplier TEXT NOT NULL,
 payload_json TEXT NOT NULL, observed_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS opportunities(
 id INTEGER PRIMARY KEY AUTOINCREMENT, product_slug TEXT NOT NULL, market_code TEXT NOT NULL,
 payload_json TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS experiments(
 id INTEGER PRIMARY KEY AUTOINCREMENT, product_slug TEXT NOT NULL, market_code TEXT NOT NULL,
 budget REAL NOT NULL, spend REAL DEFAULT 0, clicks INTEGER DEFAULT 0, conversions INTEGER DEFAULT 0,
 revenue REAL DEFAULT 0, status TEXT DEFAULT 'planned', created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS support_tickets(
 id INTEGER PRIMARY KEY AUTOINCREMENT, payload_json TEXT NOT NULL, status TEXT DEFAULT 'open',
 created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS provenance_events(
 id INTEGER PRIMARY KEY AUTOINCREMENT, entity_type TEXT NOT NULL, entity_key TEXT NOT NULL,
 source TEXT NOT NULL, source_url TEXT, observed_at TEXT NOT NULL, payload_hash TEXT NOT NULL,
 payload_json TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""
_lock = threading.Lock()

def init_db(path: str | None = None) -> str:
    db_path = path or settings.db_path
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.executescript(_SCHEMA)
        row = conn.execute("SELECT COUNT(*) FROM schema_meta").fetchone()[0]
        if row == 0:
            conn.execute("INSERT INTO schema_meta(version) VALUES(1)")
    return db_path

@contextmanager
def connect(path: str | None = None):
    db_path = init_db(path)
    with _lock:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

def jdump(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def jload(value: str):
    return json.loads(value)
