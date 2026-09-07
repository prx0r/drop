from q4radar.config import load_markets, load_products, load_scoring
from q4radar.models import ProductObservation
from q4radar.scoring import score, economics


def test_good_unit_economics_score_better():
    markets=load_markets("config"); products=load_products("config"); cfg=load_scoring("config")
    p=products["compression-packing-cubes"]; m=markets["GB"]
    good=ProductObservation(product_slug=p.slug,market="GB",search_volume=5000,search_momentum=30,keyword_competition=.35,competitor_count=18,competitor_price_median_usd=110,supplier_price_median_usd=20,shipping_usd=6,shipping_days=6,supplier_count=12,ad_count=12,ad_longevity_days=60)
    bad=good.model_copy(update={"supplier_price_median_usd":70,"shipping_usd":20})
    assert score(p,m,good,cfg).total_score > score(p,m,bad,cfg).total_score


def test_economics():
    p=load_products("config")["dog-car-hammock"]
    o=ProductObservation(product_slug=p.slug,market="NO",competitor_price_median_usd=100,supplier_price_median_usd=20,shipping_usd=10)
    m=load_markets("config")["NO"]
    e=economics(p,m,o)
    assert e["landed_cost_usd"] == 30
    assert e["gross_profit_pre_fees_usd"] < 70
    assert e["retail_to_landed_markup_x"] == 3.33
