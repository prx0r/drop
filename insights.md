# Insights: Foreign-Product Scanner Pipeline

*How to find product-country arbitrage systematically using Google APIs and local comparison engines.*

---

## The Target

> **A product already proven to sell + meaningful local demand + surprisingly few competent sellers + weak merchant experience + supplier we can actually use + advertising cost cheap relative to contribution margin.**

Not "low listings." Not "trending on TikTok." Not "nobody is selling this."

The distinction matters.

---

## The Killer Discovery Pattern

```text
PRODUCT: proven / popular elsewhere
COUNTRY: affluent + ecommerce-native

Local demand:        HIGH
Exact SKU sellers:   3–8
Good specialists:    0–2
Amazon dominance:    LOW/MEDIUM
Manufacturer DTC:    weak/absent
Price dispersion:    meaningful
Stock availability:  inconsistent
Local content:       weak
PDP quality:         mediocre
Images:              generic/poor
Comparison content:  poor
Shipping clarity:    poor
Supplier path:       easy
Delivery:            competitive
Contribution:        large
CPC:                 low relative to contribution
```

That is much more interesting than some obscure product with one seller and no searches.

---

## The Big Discovery: Google Already Gives Us a Foreign-Product Scanner

Merchant Center's **Popular Products** report can show products and brands people are buying/searching for, popularity rank, price ranges and suggestions for products you don't currently sell. Crucially, Google says you can change the **country filter to countries you do not sell in yet**, and the data can go back up to two years. Norway, Finland, Denmark, Sweden, Netherlands, Austria, Switzerland and most of the other countries we're interested in are supported.

That gives us an extremely clean first-stage scanner:

> **What products does Google already know are popular in Norway/Finland/etc.?**

Then we measure how well those products are actually served.

This is much stronger than starting with random "winning product" tools.

---

## The 10-Stage Pipeline

### Stage 1 — Produce the Universe of Proven Products

Start with **proof of demand**, not supplier catalogs.

For each target country collect the top 500–5,000 candidate products/brands from:

**A. Google Merchant Center Popular Products**

Country = Norway / Finland / Denmark / Sweden / etc.

Capture:
- product
- brand
- category
- popularity rank
- rank change
- price range
- historical popularity

**B. Local Comparison Engines**

Norway: Prisjakt. Finland: Hintaopas. Sweden: PriceRunner.

Prisjakt says its category popularity ordering is based on products receiving clicks, and it tries to list every shop and price it knows about. It surfaces stock status, delivery, shop reviews and prices.

```text
Google popularity
+
Prisjakt popularity
+
local retailer evidence
=
real demand signal
```

Much better than "this is trending on TikTok."

---

### Stage 2 — Calculate Local Seller Density

For every high-demand product, search the exact SKU on Prisjakt / Hintaopas / local equivalent.

Capture:
```text
seller_count
seller_names
price_min
price_median
price_max
stock_count
shipping estimates
shop review counts
price history
```

Calculate:

**Demand-to-seller ratio:**

$$
OpportunityDensity = \frac{Demand}{GoodSellerCount}
$$

| Scenario | Demand | Total Sellers | Good Specialists | Action |
|----------|--------|---------------|------------------|--------|
| A | Enormous | 42 | 15 | Forget it |
| B | Enormous | 5 | 1 | **Investigate immediately** |
| C | Zero | 0 | 0 | Probably nonexistent demand |

---

### Stage 3 — Count GOOD Sellers, Not Sellers

"6 sellers" is weak. "6 sellers, but only one is remotely good" is interesting.

For the first 5–10 merchants, score:

**Merchant quality:**

| Dimension | What to Check |
|-----------|---------------|
| Product presentation | Multiple good images, consistent high-res, video, dimensions, manuals, diagrams |
| Decision support | Specs, model comparisons, compatibility, accessories, FAQs, alternatives, expert guidance |
| Trust | Reviews, contact details, company legitimacy, warranty, returns, clear shipping |
| Localization | Fluent native language, local currency, appropriate payments, proper local delivery |
| UX | Fast mobile site, modern checkout, sensible navigation, good filtering, no broken pages |

Then:
```text
raw sellers: 7
competent generalists: 3
good specialists: 1
excellent specialists: 0
```

**That is the number I care about.**

---

### Stage 4 — Measure Search Demand and Ad Cost by Country

Google Keyword Planner supports country/location and language filtering and gives:
- average monthly searches
- advertiser competition
- low-range top-of-page bid
- high-range top-of-page bid

Run queries in the local language:

```text
[exact model]
[brand model]
[model price]
[model review]
[model vs model]
[buy model]
[category]
[best category for use case]
```

Example Norway:
```text
Roborock Qrevo Curv
Roborock Qrevo Curv pris
kjøp Roborock Qrevo Curv
beste robotstøvsuger hundehår
Roborock Qrevo Curv vs S8 MaxV
```

This produces a **demand × auction matrix**.

---

### Stage 5 — Don't Rank by CPC Alone

**€0.20 CPC is not necessarily cheap.**

If we make €8/order: `0.20 / 8 = bad`

€2 CPC could be wonderful if contribution is €250.

What matters:

$$
BreakEvenCVR = \frac{CPC}{PreAdContribution}
$$

Example:
- Contribution: €150
- Expected CPC: €0.90
- BreakEvenCVR: `0.90/150 = 0.6%` — potentially attractive

But:
- Contribution: €20
- CPC: €0.80
- BreakEvenCVR: `4%` — nasty

Rank: **cheap advertising relative to gross contribution**, not cheap CPC.

---

### Stage 6 — Find the Supplier Before Building

Take only the top ~20 cells. For each `product × country`, search:

```text
manufacturer distributor
authorized dealer
wholesale
B2B
dropship
Nordic distributor
EU distributor
local stockist
```

We want:

| Factor | Requirement |
|--------|-------------|
| Validation level | One-order fulfillment, no/low MOQ |
| Warehouse | Local/EU warehouse |
| Integration | API/CSV stock feed |
| Delivery | Acceptable delivery time |
| Returns | Decent return process |

If supplier price is unknown: **don't invent it.** Candidate remains unresolved.

---

### Stage 7 — Construct the "Foreign Gap Score"

Transparent components, not mystical AI score.

| Factor | Weight |
|--------|-------:|
| Proven product demand | 20 |
| Demand / good-seller ratio | 15 |
| Contribution economics | 20 |
| Supplier + delivery quality | 15 |
| Local merchant weakness | 10 |
| Search/ad headroom | 10 |
| Localization opportunity | 5 |
| Accessory/bundle upside | 5 |

Apply a confidence multiplier.

Example:
```text
Roborock X — Finland

Demand                 18/20
Demand / good sellers  12/15
Economics              14/20
Supply                 14/15
Merchant weakness       8/10
Ad headroom              8/10
Localization             4/5
Accessory upside         4/5

RAW = 82
Evidence confidence = .87
ADJUSTED = 71.3
```

---

### Stage 8 — Market Asymmetry Pattern

The strongest signal.

| Metric | Germany | Norway |
|--------|--------:|-------:|
| Product popularity | High | High |
| Sellers | 34 | 5 |
| Excellent specialists | 9 | 0 |
| Exact-model content | Excellent | Weak |
| Typical retailer imagery | Good | Generic |
| Local buying guides | Many | Almost none |
| Supplier | EU/Nordic | EU/Nordic |
| Delivery | 2–3d | 3–5d |
| Ad bid | €1.40 | €0.55 |

**Germany proves the business. Norway provides the gap. Supplier bridges the two.**

---

### Stage 9 — Manually Investigate Why the Gap Exists

For each finalist ask: **WHY hasn't a competent merchant already filled this?**

| Answer | Implication |
|--------|-------------|
| Supplier won't authorize more retailers | Great if we can get authorization |
| Product isn't certified locally | Kill |
| Manufacturer itself dominates sales | Kill |
| Everyone buys it from Sweden | Maybe interesting, maybe not |
| Norway has weird import economics | Potentially bad |
| Demand is mostly product research, nobody buys locally | Kill |

---

### Stage 10 — Don't Even Pay for Ads Initially

Google free listings allow eligible products to appear across Search, Shopping, Images, Lens, YouTube, Gemini and other Google surfaces. Norway and Finland are supported.

First test:
```text
20 products
→ local-language store
→ correct Merchant feed
→ free listings
→ exact-model pages
→ comparison pages
→ Search Console + Merchant observations
```

Watch:
```text
Are we getting impressions?
Which SKUs?
Which queries?
Which pages?
Which country?
Which product clusters?
```

Market feedback for essentially pennies.

---

## The 3-Pass Scanner

### PASS A — Machine Scan, Thousands of Cells

Cheap. For each of 500 products × 12 countries = 6,000 cells, collect:
- Google popularity rank
- Trend direction
- Comparison-site seller count
- Price range
- Stock count
- Keyword Planner volume
- Keyword Planner competition
- Bid low/high

Reject ~90%.

### PASS B — Intelligence Scan, Top 100

For each inspect:
- Top merchants
- Merchant quality
- Local-language content
- Amazon/manufacturer presence
- Reviews
- Shipping
- Payment
- Product imagery
- Comparison support
- Accessories

Reject ~80%.

### PASS C — Commercial Verification, Top 10–20

Find suppliers. Calculate:
- Landed cost
- Contribution
- Break-even CVR
- Delivery
- Returns
- Warranty

Pick perhaps **1–3 experiments**.

---

## Key Metrics

### GOOD_SELLER_GAP

$$
GoodSellerGap = Popularity \times \frac{1 + TotalSellers}{1 + GoodSellers}
$$

What we're hunting:
```text
POPULARITY: 91/100
TOTAL SELLERS: 8
GOOD SELLERS: 1
```

Not:
```text
POPULARITY: 17/100
TOTAL SELLERS: 1
GOOD SELLERS: 0
```

### ECONOMIC_HEADROOM

$$
Headroom = \frac{RealisticCVR \times PreAdContribution}{ExpectedCPC}
$$

| Headroom | Interpretation |
|----------|----------------|
| <1 | Inherently losing |
| 1–1.3 | Fragile |
| 1.3–2 | Interesting |
| 2+ | Investigate aggressively |

---

## Google API Integration Plan

### What We Have

| API | Status | Use |
|-----|--------|-----|
| Merchant Center | Live | Popular Products per country |
| Google Ads | Test mode | Keyword Planner, Auction Insights |
| GCP Credits | $20/week | BigQuery, Vertex AI, Storage |

### Weekly API Budget ($20)

| Service | Cost | Purpose |
|---------|------|---------|
| BigQuery | $5 | Analyze Merchant Center data at scale |
| Vertex AI | $10 | Product classification, content generation |
| Cloud Storage | $2 | Feed storage, data backups |
| Compute Engine | $3 | Scheduled data pulls |
| Reserve | $0 | Buffer |

### Data Flow

```
Merchant Center Popular Products (per country)
        ↓
Keyword Planner (demand × CPC per product per country)
        ↓
Prisjakt/PriceRunner (seller density, price history, stock)
        ↓
Scoring Engine (economic model + gates + Bayesian)
        ↓
Top Candidates → Supplier Verification → Free Listings Test
        ↓
Record Results → Update Scoring Model → Repeat
```

---

## Operator Wisdom Worth Remembering

1. **Score contribution profit per click, not ROAS.** ROAS is a vanity metric.

2. **0.48% CVR is realistic.** Most operators overestimate CVR by 10x. The $10k/day case had 36 orders from 7,500 sessions.

3. **Product × query × economics IS the strategy.** Campaign structure barely matters compared to picking the right product in the right market.

4. **One country first.** Don't spread thin. Learn one market deeply before expanding.

5. **Free listings first.** Zero-cost market validation before spending a cent on ads.

6. **EU stock, not China.** Start with local/EU warehouse suppliers. Delivery speed matters.

7. **Localization is not translation.** Copying a working domestic setup into Germany/France/Netherlands does NOT automatically reproduce economics.

8. **The content moat.** "Tell me what you're trying to do, and I'll tell you exactly which model you should buy and why" beats generic product pages.

9. **$10/day is a feature.** Forces disciplined experimentation and prevents throwing money at bad ideas.

10. **The data flywheel.** Each experiment feeds back into the model. The system gets smarter with every test.
