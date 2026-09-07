# The Canonical Strategy

*The single playbook for winning at dropshipping/ecommerce. Derived from 52 sources, 12 case studies, 370 opportunities, 159 intelligence reports, finalbuilds2, and z2m. This is the law.*

---

## The Core Thesis

> **Sell saturated products in unsaturated markets.**

The product already exists. The demand already exists. The edge is: execute better than the existing sellers in a market where they are weak.

---

## The Three Laws

### Law 1: Proven Demand × Weak Execution

Don't invent products. Find products people already search for, in countries where the existing sellers are mediocre.

```
DEMAND: People search for it (Google Keyword Planner proves it)
EXECUTION: Few good sellers (Prisjakt/Hinta.fi proves it)
EDGE: Better images, better content, better localization, better decision support
```

### Law 2: Free Before Paid

Never spend money on ads until free surfaces prove demand.

```
Step 1: Google Free Listings ($0)
Step 2: SEO/Comparison pages ($0)
Step 3: Bing/Pinterest free ($0)
Step 4: $5-10/day paid test (only after free proves signal)
Step 5: Scale only after contribution profit is real
```

### Law 3: The Campaign Is A Hypothesis

Every store is an experiment. Sales data proves or disproves the hypothesis. If proven, replicate the edge.

```
HYPOTHESIS: "Product X in Country Y with Z% margin will be profitable at CPC $C"
EXPERIMENT: Launch store, list products, observe
DATA: Impressions, clicks, ATC, sales, contribution per click
VERDICT: Promote (scale) or Kill (stop)
REPLICATION: If proven, build 5 more stores exploiting the same edge
```

---

## The Budget

| Category | Daily | Monthly | Source |
|----------|-------|---------|--------|
| GCP Credits | $20 | $600 | Free trial |
| Ad Spend | $10 | $300 | Revenue-funded |
| Domain | — | $10 | One-time per store |
| Hosting | $0 | $0 | Cloudflare free tier |
| **Total Capex** | **$10** | **$300** | **Before first sale** |

**Rules:**
- Never spend more than $10/day on ads until contribution profit is proven
- Use GCP credits for intelligence (BigQuery, Vertex AI, scraping)
- Domains only after hypothesis is validated
- Hosting always free (Cloudflare)

---

## The Scoring Rubric

Every product × country scores on 10 dimensions (0-10 each, max 100):

| Dimension | Weight | What It Measures | How To Get Data |
|-----------|--------|------------------|-----------------|
| **Demand** | 20 | People search for it | Keyword Planner, Google Trends |
| **Economics** | 20 | Contribution margin > 3× CPC | Supplier price vs retail price |
| **Merchant Gap** | 15 | Few good sellers, weak experience | Prisjakt/Hinta.fi seller count + quality |
| **Supplier** | 15 | EU/Nordic warehouse, dropship, no MOQ | Contact suppliers directly |
| **CPC Headroom** | 10 | Cheap relative to contribution | Keyword Planner (when available) |
| **Localization** | 5 | Norwegian/Finnish language, local payment | Competitor analysis |
| **Seasonality** | 5 | Evergreen or timed for Q4 | Google Trends |
| **Accessory Upsell** | 5 | Bundle, accessories, repeat purchase | Product ecosystem research |
| **Barrier to Entry** | 5 | Foreign language, specialist knowledge | Competitor quality audit |

### Score Interpretation

| Score | Decision |
|-------|----------|
| 80-100 | LAUNCH — build store immediately |
| 60-79 | INVESTIGATE — resolve blockers |
| 40-59 | MONITOR — watch for changes |
| 0-39 | KILL — don't pursue |

---

## The Pipeline

### Stage 1: Mass Scanner (30% of compute)

Screen 1000s of Product × Country cells. Cheap data only.

**Data sources:**
- Prisjakt.no (Norway) — 8000+ winter tires, 724 sleeping bags, 560 fireplaces
- Hinta.fi (Finland) — 341 robot vacuums, 625 air purifiers, 435 EV chargers
- Google Merchant Center Popular Products — per country
- Google Trends — seasonal patterns

**Output:** Top 25 candidates

### Stage 2: Market Gap Auditor (25% of compute)

Deep audit top 25. Score merchant quality.

**For each candidate, inspect top 10 sellers:**
- Image quality (1-10)
- Product info (specs, dimensions, manuals)
- Decision support (comparisons, compatibility, FAQs)
- Shipping clarity
- Stock availability
- Localization (language, currency, payments)
- Reviews
- Trust (company info, returns)
- Accessories
- Mobile speed

**Output:** Top 5 with MERCHANT_GAP >= 70

### Stage 3: Supplier Resolution (25% of compute)

Can we actually sell this thing?

**For each top 5:**
- Find manufacturer/distributor
- Contact for dealer terms
- Calculate: landed cost, contribution, break-even CVR
- Verify: MOQ, dropship, stock feed, returns

**Output:** 1-3 candidates with REAL economics

### Stage 4: Search Economics (10% of compute)

Verify demand × cost.

- Keyword Planner: exact-model search volume per country
- CPC estimates
- Break-even CVR calculation
- Headroom = (realistic_CVR × pre_ad_contribution) / CPC

**Output:** Economics verified or killed

### Stage 5: Blueprint (conditional)

Only after passing all gates.

Full store plan: catalog, content, feed, traffic, ads, operations.

---

## The State Machine

Every candidate MUST progress through states:

```
DISCOVERED → DEMAND_VERIFIED → MERCHANT_GAP_VERIFIED → SUPPLY_PATH_VERIFIED → MARGIN_VERIFIED → SEARCH_ECONOMICS_VERIFIED → LAUNCHABLE → FREE_TRAFFIC_TEST → PAID_TEST → PROFITABLE/KILLED
```

Each run must: ADVANCE, KILL, or RESOLVE a field.

---

## The 7 Kill Rules

1. **Break-even CVR > 3%** — structurally impossible at small scale
2. **Headroom < 1.0** — every scenario loses money
3. **GTIN sellers > 20** — too saturated
4. **Shipping > 21 days** — unacceptable for customer satisfaction
5. **No EU/Nordic supplier** — can't fulfill competitively
6. **B2B complexity** — requires demo, site visit, training (target consumer/prosumer)
7. **Content gap but not merchant gap** — affiliate opportunity, not store opportunity

---

## The Replication Model

If a store proves profitable:

1. **Document the edge** — what specifically worked (product × query × economics × localization)
2. **Find adjacent markets** — same product, different country
3. **Find adjacent products** — same country, different product in same ecosystem
4. **Build 5 stores** — each exploiting the same proven edge
5. **Systematize** — templatize the store build, feed optimization, content creation

**Example:**
- Store 1: Davis Weather Stations Norway — PROVEN
- Store 2: Davis Weather Stations Finland — same product, different country
- Store 3: VPCompass Finland — same country, different weather brand
- Store 4: Davis Accessories Norway — same country, accessory ecosystem
- Store 5: Helsport Sleeping Bags Norway — same country, different outdoor category

---

## The $20/day GCP Allocation

| Use | Daily | Purpose |
|-----|-------|---------|
| BigQuery | $5 | Store all research data, run analytics |
| Vertex AI | $10 | Product classification, content generation, scoring |
| Cloud Storage | $2 | Feed storage, data backups |
| Compute Engine | $3 | Scheduled scraping, data pulls |
| Reserve | $0 | Buffer |

**What this buys:**
- Automated daily product scanning across 7 markets
- AI-powered merchant quality scoring
- Automated content generation in Norwegian/Finnish
- Real-time competitor price monitoring
- Bayesian scoring updates

---

## The $10/day Ad Budget

| Phase | Budget | Duration | Goal |
|-------|--------|----------|------|
| Free listings | $0 | 14 days | Get impressions, measure CTR |
| SEO/Content | $0 | 21 days | Build organic traffic |
| $5/day test | $5 | 14 days | Validate paid economics |
| $10/day scale | $10 | 30 days | Scale if profitable |
| Revenue-funded | from profit | ongoing | Scale with contribution |

**Rules:**
- Never increase budget until contribution profit is positive
- Never change structure within 14 days of launch
- Kill if no sales after 100 clicks at break-even CVR

---

## The Hypothesis Format

Every store launch is a formal hypothesis:

```json
{
  "hypothesis_id": "H-NO-DAVIS-001",
  "statement": "Davis weather stations in Norway will be profitable at NOK 15,000+ AOV with <1% CVR",
  "mechanism": "Marine/general retailers have weak decision support. Specialist content + comparison tools will capture demand.",
  "prediction": {
    "metric": "contribution_per_click",
    "target": "> 0",
    "window": "30 days"
  },
  "falsifier": "If 100 clicks produce 0 sales at break-even CVR, hypothesis is false",
  "budget": "$0 free listings for 14 days, then $5/day for 14 days",
  "success_criteria": "Positive contribution profit per click after 30 days"
}
```

---

## What We Have Now

### Data
- 52 research sources
- 12 case studies with quantitative data
- 370 scored opportunities (z2m)
- 159 intelligence reports (z2m)
- 12 pain themes, 87 pain points (z2m)
- 7 Google Merchant XML feeds (z2m)
- 21 operator events
- 5 probe reports

### Infrastructure
- BigQuery data warehouse (7 tables, 123 rows)
- Cloudflare Workers for comparison pages
- Gmail API for supplier outreach
- Merchant Center account (5849184805)
- Google Ads (pending)

### Active Pipeline
- 1 leader candidate (Davis NO, 85/100)
- 5 new leads (robot vacuums, air purifiers, EV chargers, AC, sleeping bags)
- 4 emails sent to suppliers

---

## What's Next

1. **Wait for dealer responses** (48h)
2. **If economics work → launch Davis store**
3. **If not → pivot to EV chargers or robot vacuums**
4. **Build the scoring pipeline** to scan 1000s of products automatically
5. **Replicate the first win** across 5 stores

---

*This document is the canonical strategy. Every product decision should trace back to it. If something contradicts this document, this document wins.*
