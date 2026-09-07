from giftradar.pipeline import Radar

def test_ranking_is_bounded_and_has_builds():
    r=Radar('config','data/evidence.yml')
    scores=r.rank()
    assert len(scores) >= 35
    assert all(0 <= s.total <= 100 for s in scores)
    assert any(s.verdict == 'BUILD' for s in scores)
    assert scores[0].total >= scores[-1].total

def test_ai_labor_candidates_rank_well():
    r=Radar('config','data/evidence.yml')
    scores={s.slug:s for s in r.rank()}
    assert scores['family-annual-newspaper'].total > 75
    assert scores['recipient-one-click-photobook'].total > 75
