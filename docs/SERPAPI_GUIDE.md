# SerpApi Usage Guide — Maximize 1,047 Credits

*Budget: 1,047 searches. Every search counts.*

---

## Account Status

- **Plan:** Free (250/mo) + 1,000 extra credits
- **Total remaining:** 1,047
- **Renewal:** Sep 24
- **Rate limit:** 200,000/hr (not a concern)

---

## Endpoints We Use

| Endpoint | Engine | Cost | Use For |
|----------|--------|------|---------|
| Google Shopping | `google_shopping` | 1 search | Seller count, prices, shipping, ratings per GTIN per country |
| Google Trends | `google_trends` | 1 search | Seasonality, demand trajectory (**NOT on free plan**) |
| Google SERP | `google` | 1 search | Organic competition, manufacturer DTC presence |

---

## Credit Allocation Strategy

### Phase 1: Candidate Scanning (150 searches)

30 serious candidates × 5 queries each = 150

For each candidate, run:

| # | Query | Engine | What It Reveals |
|---|-------|--------|-----------------|
| 1 | `"exact product name"` | google_shopping | Exact SKU sellers + prices |
| 2 | `"exact product name" + brand` | google_shopping | Brand-level competition |
| 3 | `"product category"` | google_shopping | Category competition |
| 4 | `"product" site:amazon.com` | google | Amazon presence |
| 5 | `"product" + "buy"` | google_shopping | Purchase intent results |

### Phase 2: Country Comparison (100 searches)

10 top candidates × 4 countries × 2-3 queries = 80-120

For each candidate, compare:

```
Product × UK Shopping
Product × Norway Shopping  
Product × Denmark Shopping
Product × Sweden Shopping
```

This catches geographic arbitrage opportunities.

### Phase 3: Ad-Hoc Investigation (remaining)

Reserve ~800 searches for:
- Investigating new candidates as they emerge
- Checking competitor stores
- Verifying supplier economics
- Post-launch monitoring

---

## Shopping API — Exact Usage

### Request

```
GET https://serpapi.com/search.json
  ?engine=google_shopping
  ?q=QUERY
  ?location=COUNTRY
  ?api_key=KEY
```

### Parameters

| Param | Required | Notes |
|-------|----------|-------|
| `engine` | Yes | `google_shopping` |
| `q` | Yes | Product name, GTIN, or search query |
| `location` | No | Country name (e.g., "United Kingdom", "Norway") |
| `api_key` | Yes | Your key |
| `gl` | No | Country code (us, uk, no, dk, se) — alternative to location |
| `hl` | No | Language (en, no, da, sv) |
| `currency` | No | Currency code (GBP, NOK, USD) |
| `page` | No | Pagination (0, 1, 2...) — each page = 1 search |

### Response Fields

```json
{
  "shopping_results": [
    {
      "position": 1,
      "title": "Product Name",
      "price": "$398.00",
      "extracted_price": 398.0,
      "link": "https://...",
      "source": "Store Name",
      "rating": 4.7,
      "reviews": 312,
      "thumbnail": "https://...",
      "delivery": "Free delivery",
      "tag": "Sponsored"
    }
  ]
}
```

### What to Extract Per Query

| Field | Use For |
|-------|---------|
| `source` | Seller count (Gate 4) |
| `extracted_price` | Price distribution, median, percentile |
| `rating` + `reviews` | Merchant quality signal |
| `delivery` | Shipping competitiveness |
| `tag` | Sponsored vs organic (sponsored = paid competition) |

---

## Strategic Role: Selective Enrichment Layer

**Don't use SerpApi to discover opportunities. Use it to validate them.**

The flow is:

```
Research surfaces something interesting
(Reddit, case study, YouTube, forum)
         ↓
Did they reveal enough product detail?
         ↓
If yes → ONE SerpApi Shopping call
         ↓
Snapshot current auction reality:
  - sellers
  - prices
  - delivery
  - ratings
  - Amazon presence
         ↓
Bridge: historical success → current auction room
```

### Why This Matters

A strategy that worked 6 months ago can now be saturated.

Example:
- Operator posts: "$400 baby product, great margins, Google Shopping"
- We query: `product name × country`
- Result: 34 sellers, Amazon dominant, price compressed
- Decision: REJECT — the auction has no room

vs.

- Operator posts: "$400 baby product, great margins"
- We query: 5 sellers, no Amazon, wide price dispersion
- Decision: INVESTIGATE — auction may have room

**One SerpApi call bridges historical operator success with current auction reality.**

### Credit Efficiency

| Approach | Searches | Waste |
|----------|----------|-------|
| Blind scanning 100 products | 100 | High — most won't be viable |
| Research → validate top 10 | 10 | Low — every search has a hypothesis |
| Research → validate top 30 × 4 countries | 120 | Medium — but geographic signal is worth it |

**Rule: Every SerpApi search must start with "this product was flagged as interesting by [source]."**

---

## What NOT to Waste Credits On

| Don't | Why |
|-------|-----|
| Paginating beyond page 2 | First 40 results give 90%+ of the signal |
| Searching the same product twice in same country | Cache exists but don't rely on it |
| Using Trends on free plan | Returns zeros, wastes 1 search |
| Searching broad categories ("coffee grinder") for competition | Too noisy — search exact products |
| Searching your own products | You already know your prices |
| Running searches just to "see what's there" | Every search needs a hypothesis |

---

## Caching Strategy

SerpApi caches results for 1 hour. Same query + same params = free (doesn't count toward credits).

**Use this for:**
- Re-checking a competitor's price within the same hour
- Verifying your own submission appeared

**Don't rely on it for:**
- Daily monitoring (cache expires)
- Cross-session research

---

## Example: Full Candidate Scan

```python
import requests

SERPAPI_KEY = "0f9f1e04..."

def scan_candidate(product_name, countries=["United Kingdom", "Norway", "Denmark", "Sweden"]):
    """Scan one candidate across countries. Costs: len(countries) searches."""
    results = {}
    
    for country in countries:
        resp = requests.get("https://serpapi.com/search.json", params={
            "engine": "google_shopping",
            "q": product_name,
            "location": country,
            "api_key": SERPAPI_KEY,
        })
        data = resp.json()
        shopping = data.get("shopping_results", [])
        
        sellers = set(r.get("source", "") for r in shopping)
        prices = [r.get("extracted_price", 0) for r in shopping if r.get("extracted_price")]
        
        results[country] = {
            "sellers": len(sellers),
            "price_min": min(prices) if prices else 0,
            "price_max": max(prices) if prices else 0,
            "price_median": sorted(prices)[len(prices)//2] if prices else 0,
            "top_sellers": list(sellers)[:5],
        }
    
    return results

# Example: scan 30 candidates × 4 countries = 120 searches
candidates = [
    "Eureka Mignon Specialita",
    "Premium baby stroller",
    "Cordless vacuum cleaner",
    # ... 27 more
]

total_searches = 0
for candidate in candidates:
    results = scan_candidate(candidate)
    total_searches += 4  # 4 countries per candidate
    print(f"{candidate}: {total_searches} searches used")

print(f"Total: {total_searches} / 1047 remaining")
```

---

## Cost Per Insight

| Insight | Searches | Cost |
|---------|----------|------|
| Exact SKU seller count (1 country) | 1 | 1 credit |
| Price distribution (1 country) | 1 | 1 credit |
| Geographic competition matrix (4 countries) | 4 | 4 credits |
| Full candidate scan (4 countries) | 4 | 4 credits |
| 30 candidates × 4 countries | 120 | 120 credits |
| Reserve for ad-hoc | — | 927 credits |

**Total research cost: ~120 credits for 30 candidates across 4 countries.**
**Remaining: ~927 credits for ad-hoc investigation.**

---

## SERP API vs Google Ads API

| Data | SerpApi | Google Ads API |
|------|---------|----------------|
| Shopping sellers per GTIN | ✅ | ❌ |
| Shopping prices per seller | ✅ | ❌ |
| Shopping ratings/reviews | ✅ | ❌ |
| Monthly search volume | ❌ | ✅ |
| CPC estimates | ❌ | ✅ |
| Bid ranges | ❌ | ✅ |
| Competition index | ❌ | ✅ |
| Seasonality/trends | ❌ (free plan) | ❌ |
| Forecasts | ❌ | ✅ |

**Use SerpApi for competition research. Use Google Ads API for demand/CPC data.**
They complement, not duplicate.

---

*1,047 credits = enough to scan 30 candidates across 4 countries with 900+ reserves. Don't waste them.*
