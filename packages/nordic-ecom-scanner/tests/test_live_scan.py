from pathlib import Path
import sqlite3

from nordic_arbitrage.db import init_db
from nordic_arbitrage.live_scan import observe_query
from nordic_arbitrage.providers.csv_provider import CSVKeywordProvider, CSVShoppingProvider


def test_csv_provider_to_observation(tmp_path):
    root = Path(__file__).resolve().parents[1]
    db = str(tmp_path / "obs.sqlite")
    init_db(db)
    payload = observe_query(
        query="oppladbar bordlampe",
        country="NO",
        shopping=CSVShoppingProvider(str(root / "examples" / "shopping_results.csv")),
        keywords=CSVKeywordProvider(str(root / "examples" / "keyword_metrics.csv")),
        db_path=db,
    )
    assert payload["serp"]["result_count"] == 1
    assert payload["serp"]["median_price"] == 599
    assert payload["keyword"]["keyword"] == "oppladbar bordlampe"
    with sqlite3.connect(db) as conn:
        assert conn.execute("select count(*) from observations").fetchone()[0] == 1
