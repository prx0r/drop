# Nordic Market Matrix v0 — Guide

*From the user's guide sent to tradesprior@gmail.com*

---

## The Thesis (Corrected)

> **Some Nordic country × product × intent cells may have unusually high CM2 headroom because native-language competition, merchant density, price umbrellas and local buyer quality interact favorably. We measure that against GB rather than assume it.**

NOT: "Nordic ads are cheap"

---

## The Architecture

```text
                SAME HYPOTHESES
                       │
       ┌────────┬──────┼──────┬────────┐
       NO       FI     SE     DK       GB
       │        │      │      │        │
       ▼        ▼      ▼      ▼        ▼

native keyword universe
Google search volume
competition index
20th/80th percentile bids
forecast CPC/clicks
paid advertisers
organic competitors
Shopping products
Shopping sellers
local prices
price dispersion
local comparison engines
competitor catalogs
GTINs
shipping
payments
returns
supplier cost
landed cost
       │
       ▼
CM1
break-even CPC
break-even CVR
CPC headroom
merchant density
P(CM2 > 0)
p10 downside
EVI
       │
       ▼
BUILD / PROBE / BLOCK / KILL
```

---

## Data Sources

| Source | What it provides | Cost |
|--------|------------------|------|
| Google Keyword Planner | Historical demand, competition, bid ranges, forecast | Free (with Ads account) |
| DataForSEO | Localized Shopping products/sellers | ~$0.001/product |
| Hinta.fi | 1.5M Finnish products, ~4M prices | Free (public) |
| Prisjakt | NO/SE product/merchant coverage | Partner API |
| PriceRunner/Klarna | Product catalog API | Approved access |
| Merchant Center | Best sellers, benchmark prices, competitive visibility | Free (with account) |

---

## Google Cloud Credits Usage

- **Cloud Run Jobs** — Scheduled collectors/crawlers
- **BigQuery** — Canonical evidence warehouse
- **Cloud Storage** — Immutable raw responses
- **Vertex/Gemini** — Entity resolution, native-language normalization
- **Translation Advanced** — Query translation
- **Google Trends** — Already in BigQuery

---

## The Process

1. **Freeze 20-50 existing Drop hypotheses**
2. **Run every one across NO/FI/SE/DK/GB**
3. **Collect real Google/Shopping/merchant/pricing data**
4. **Run economics**
5. **Let BuildDecision select the winner**
6. **Compile exactly one localized real campaign**

---

## The Recurring Probe

Make Nordic matrix a recurring probe that:
- Refreshes auction, price, advertiser and merchant-density changes
- Alerts when a previously blocked cell becomes launchable

---

## Key Insight

> That first matrix will tell us whether the geographic-arbitrage thesis is actually real—and, much more usefully, **where and for what mechanism it is real**.
