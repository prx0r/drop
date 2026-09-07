from pathlib import Path
from nordic_arbitrage.db import init_db
from nordic_arbitrage.seed import seed_from_csv
from nordic_arbitrage.pipeline import score_all, ranked


def test_end_to_end(tmp_path):
    db = str(tmp_path / "x.sqlite")
    seed = Path(__file__).resolve().parents[1] / "data" / "live_screening_candidates.csv"
    init_db(db)
    assert seed_from_csv(str(seed), db) == 50
    assert score_all(db) == 50
    assert len(ranked(db,5)) == 5
