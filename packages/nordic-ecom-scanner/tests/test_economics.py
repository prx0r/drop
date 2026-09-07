from nordic_arbitrage.config import COUNTRIES
from nordic_arbitrage.economics import calculate_economics
from nordic_arbitrage.models import Candidate


def base():
    return Candidate(None,"NO","hardware","Brass handle",150,2,4,10,"near","x","y",1000,4,0.025,6,0.2,0.7,0.7,0.8,0.9,0.05,0.1,0.0,0.04,5,True,True,35,140)


def test_break_even_cvr_identity():
    c = base()
    e = calculate_economics(c, COUNTRIES["NO"])
    assert e.pre_ad_contribution_local > 0
    assert abs(e.break_even_cvr - c.cpc_local / e.pre_ad_contribution_local) < 1e-4


def test_cpa_formula():
    c = base()
    e = calculate_economics(c, COUNTRIES["NO"])
    assert e.expected_cpa_local == round(c.cpc_local / c.assumed_cvr, 2)


def test_multi_unit_order_pays_cpa_once():
    c1 = base()
    c2 = base()
    c1.expected_units_per_order = 1
    c2.expected_units_per_order = 8
    e1 = calculate_economics(c1, COUNTRIES["NO"])
    e2 = calculate_economics(c2, COUNTRIES["NO"])
    assert e2.order_revenue_local == e1.order_revenue_local * 8
    assert e2.expected_cpa_local == e1.expected_cpa_local
    assert e2.break_even_cvr < e1.break_even_cvr
