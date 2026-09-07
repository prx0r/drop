from giftradar.pipeline import Radar
from giftradar.models import GiftSpecRequest
from giftradar.gift_specs import build_spec

def test_astrology_spec_requires_deterministic_data_step():
    r=Radar('config','data/evidence.yml')
    o=r.opportunities['year-ahead-astrology-book']
    spec=build_spec(o, GiftSpecRequest(opportunity_slug=o.slug))
    assert any('deterministic' in s.lower() for s in spec.generation_steps)

def test_spec_has_review_and_privacy():
    r=Radar('config','data/evidence.yml')
    o=r.opportunities['family-game-night']
    spec=build_spec(o, GiftSpecRequest(opportunity_slug=o.slug))
    assert spec.human_review_checks
    assert spec.privacy_notes
