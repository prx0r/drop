from nordic_arbitrage.config import COUNTRIES
from nordic_arbitrage.economics import calculate_economics
from nordic_arbitrage.models import Candidate
from nordic_arbitrage.scoring import score_candidate


def candidate(delivery=5, regulated=0.05):
    return Candidate(None,"DK","hardware","Handle",100,1,3,10,"near","x","y",3000,2,0.03,5,0.15,0.8,0.8,0.8,0.9,regulated,0.05,0,0.04,delivery,True,True,20,95)


def test_fast_low_risk_scores_higher():
    a = candidate(3,0.05); b = candidate(10,0.7)
    ea = calculate_economics(a, COUNTRIES["DK"]); eb = calculate_economics(b, COUNTRIES["DK"])
    assert score_candidate(a,ea,COUNTRIES["DK"]).total > score_candidate(b,eb,COUNTRIES["DK"]).total


def test_lamp_requires_compliance_review():
    c = candidate(3,0.05)
    c.product_name = "Rechargeable restaurant lamp"
    e = calculate_economics(c, COUNTRIES["DK"])
    assert score_candidate(c,e,COUNTRIES["DK"]).gate == "COMPLIANCE_REVIEW"


def test_unverified_supplier_match_cannot_test():
    c = candidate(3,0.05)
    c.match_quality = "category/near-match only"
    e = calculate_economics(c, COUNTRIES["DK"])
    assert score_candidate(c,e,COUNTRIES["DK"]).gate == "RESEARCH"


def test_verified_low_risk_candidate_can_test():
    c = candidate(3,0.05)
    c.match_quality = "verified exact SKU"
    c.expected_units_per_order = 8
    e = calculate_economics(c, COUNTRIES["DK"])
    assert score_candidate(c,e,COUNTRIES["DK"]).gate == "TEST"
