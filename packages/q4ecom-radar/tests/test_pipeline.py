from q4radar.pipeline import Scanner
from q4radar.sources.demo import DemoSource


def test_demo_pipeline(tmp_path):
    s=Scanner("config", str(tmp_path/"x.sqlite3"), [DemoSource()])
    r=s.run(["GB","NO","DK"],["compression-packing-cubes","boot-dryer"])
    assert len(r.scores)==6
    assert all(0 <= x.total_score <= 100 for x in r.scores)
