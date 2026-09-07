#!/usr/bin/env python3
"""
SerpApi test — Shopping + Trends validation
Run: python3 test_serpapi.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SERPAPI_KEY = "0f9f1e0429767c6bad59a1de759f14173720397857eaab324acaba9813634ff6"

def test_shopping(query, location="United Kingdom"):
    """Test Google Shopping endpoint."""
    import urllib.request
    params = {
        "engine": "google_shopping",
        "q": query,
        "location": location,
        "api_key": SERPAPI_KEY,
    }
    from urllib.parse import urlencode
    url = "https://serpapi.com/search.json?" + urlencode(params)
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())

    results = data.get("shopping_results", [])
    print(f"\n{'='*60}")
    print(f"SHOPPING: {query} ({location})")
    print(f"{'='*60}")
    print(f"Results: {len(results)}")
    for r in results[:5]:
        title = r.get("title", "")[:50]
        price = r.get("price", "N/A")
        source = r.get("source", "")
        rating = r.get("rating", "")
        reviews = r.get("reviews", "")
        print(f"  {title} | {price} | {source} | {rating} ({reviews} reviews)")

    # Extract seller data
    sellers = {}
    for r in results:
        source = r.get("source", "unknown")
        if source not in sellers:
            sellers[source] = {"count": 0, "prices": []}
        sellers[source]["count"] += 1
        price_str = r.get("price", "")
        if price_str:
            try:
                price_num = float(price_str.replace("$", "").replace(",", "").replace("£", ""))
                sellers[source]["prices"].append(price_num)
            except:
                pass

    print(f"\nUnique sellers: {len(sellers)}")
    for s, d in sorted(sellers.items(), key=lambda x: -x[1]["count"])[:5]:
        avg = sum(d["prices"])/len(d["prices"]) if d["prices"] else 0
        print(f"  {s}: {d['count']} products, avg ${avg:.2f}")

    return results, sellers

def test_trends(query):
    """Test Google Trends endpoint."""
    import urllib.request
    params = {
        "engine": "google_trends",
        "q": query,
        "data_type": "TIMESERIES",
        "date": "today 12-m",
        "api_key": SERPAPI_KEY,
    }
    from urllib.parse import urlencode
    url = "https://serpapi.com/search.json?" + urlencode(params)
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())

    ts = data.get("interest_over_time", {}).get("timeline_data", [])
    values = [p.get("value", 0) for p in ts]

    print(f"\n{'='*60}")
    print(f"TRENDS: {query}")
    print(f"{'='*60}")
    print(f"Data points: {len(ts)}")
    if values:
        print(f"Range: {min(values)}-{max(values)}")
        print(f"Last 4: {values[-4:]}")
    else:
        print("No data")

    return values

def test_account():
    """Check SerpApi account status."""
    import urllib.request
    url = f"https://serpapi.com/account?api_key={SERPAPI_KEY}"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())
    print(f"\n{'='*60}")
    print(f"ACCOUNT STATUS")
    print(f"{'='*60}")
    print(json.dumps(data, indent=2))
    return data


if __name__ == "__main__":
    print("SerpApi Test Suite")
    print("=" * 60)

    # Account
    test_account()

    # Shopping tests
    test_shopping("eureka mignon specialita", "United Kingdom")
    test_shopping("eureka mignon specialita", "Norway")
    test_shopping("baby stroller", "United Kingdom")
    test_shopping("lumbar support pillow", "United States")

    # Trends tests
    test_trends("coffee grinder")
    test_trends("baby stroller")

    print(f"\n{'='*60}")
    print("DONE")
