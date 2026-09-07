# Case Study Schema

*Standardized format for organizing case study data.*
*Every case study must have these fields for pattern analysis.*

---

## Schema

```json
{
  "case_id": "C001",
  
  // Source
  "source_type": "case_study|blog|reddit|ama",
  "source_url": "https://...",
  "source_date": "2026-04-30",
  "evidence_grade": "A|B|C|D",
  "credibility_notes": "Verified agency case; unusually granular spend curve",
  
  // Operator
  "operator": "ZenoX",
  "channel": "Google PMax + Search",
  "market": "1 market / home gadgets",
  "stage": "cold launch|launch/scale|operating|mature",
  
  // Economics
  "period": "60 days",
  "days": 60,
  "start_daily_budget": 80,
  "ad_spend": 50480,
  "revenue": 103200,
  "roas": 3.6,
  "aov": 58,
  "gross_margin_pct": 48,
  "profit": 2413.62,
  "net_margin_pct": null,
  "first_sale_day": 28,
  
  // Funnel
  "orders": null,
  "impressions": null,
  "clicks": null,
  "ctr": null,
  "cvr": null,
  "cpc": null,
  
  // What worked
  "success_factors": [
    "Day 8 launch",
    "Day 15 margin-tier restructure",
    "Day 30 scaling/value-bidding shift"
  ],
  
  // What didn't work
  "failure_modes": [],
  
  // Lessons
  "lessons": "Anonymized agency case; unusually granular spend curve",
  
  // GeoDrop relevance
  "geo_drop_relevant": true,
  "geo_drop_lesson": "Google PMax can work with structured product feed"
}
```

---

## Why This Matters

With standardized case studies, we can:

1. **Find patterns** — What channel/market/stage combinations work?
2. **Calculate benchmarks** — What ROAS/margin is realistic?
3. **Identify failure modes** — What kills stores?
4. **Validate hypotheses** — Does our thesis match real outcomes?
5. **Train models** — Feed into Bayesian inference

---

## Current Inventory

| Source Type | Count | Confidence |
|-------------|-------|------------|
| Case study | 7 | High |
| Blog | 2 | Medium |
| Reddit | 3 | Low-Medium |
| **Total** | **12** | |

| Channel | Count |
|---------|-------|
| Google Shopping | 5 |
| Google PMax + Search | 1 |
| Google Ads only | 1 |
| Google + Meta | 1 |
| Multi-channel | 1 |
| Organic SEO | 1 |
| Paid traffic (unspecified) | 2 |
