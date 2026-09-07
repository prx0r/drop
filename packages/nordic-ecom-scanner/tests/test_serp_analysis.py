from nordic_arbitrage.providers.base import ShoppingResult
from nordic_arbitrage.serp_analysis import summarize_shopping


def test_serp_summary():
    rows = [
        ShoppingResult("Rechargeable restaurant lamp brass", 499, "DKK", "A", "x", "i1", 1),
        ShoppingResult("Restaurant table lamp black", 299, "DKK", "A", "y", "i2", 2),
        ShoppingResult("Cordless table light", 399, "DKK", "B", "z", "i3", 3),
    ]
    s = summarize_shopping(rows, "restaurant table lamp")
    assert s["merchant_count"] == 2
    assert s["median_price"] == 399
    assert 0 < s["dominant_merchant_share"] < 1
