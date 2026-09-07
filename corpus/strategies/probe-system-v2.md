# Drop Probe System v2 — Restructured

*Based on operator review 2026-09-07. Pivots from "continually discover novel intelligence" to "scan proven demand → identify gaps → resolve blockers → produce one launchable store."*

---

## Architecture: 6 Layers

```
Layer 1: MASS MARKET SCANNER (30%)
  → Screen 1000s of Product × Country cells
  → Cheap data only
  → Output: Top 25

Layer 2: MARKET GAP AUDITOR (25%)
  → Deep audit top 25
  → Merchant websites, images, decision support, shipping, localization
  → Output: Top 5

Layer 3: SUPPLIER + MARGIN RESOLUTION (25%)
  → Can we actually sell this?
  → Supplier, warehouse, net price, delivery, returns, warranty
  → Output: 1-3 candidates

Layer 4: SEARCH / CPC / FREE-TRAFFIC ECONOMICS (10%)
  → Real demand × real cost
  → Keyword volume, CPC, break-even CVR
  → Output: Economics verified

Layer 5: BLOCKER RESOLVER (NEW)
  → If candidate has UNKNOWN fields, pursue ONLY those
  → Do not invent new niches
  → If web can't answer: HUMAN ACTION REQUIRED
  → Output: Fields resolved or candidate killed

Layer 6: BLUEPRINT (conditional)
  → ONLY after passing all gates
  → Full store plan
  → Output: Launchable candidate
```

---

## Candidate State Machine

Every candidate MUST progress through states. Each hourly run must either ADVANCE, KILL, or RESOLVE a field.

```
DISCOVERED
    ↓
DEMAND_VERIFIED          (Layer 1: popularity + search volume confirmed)
    ↓
MERCHANT_GAP_VERIFIED    (Layer 2: few good sellers, weak experience)
    ↓
SUPPLY_PATH_VERIFIED     (Layer 3: supplier found, terms known)
    ↓
MARGIN_VERIFIED          (Layer 3: real economics calculated)
    ↓
SEARCH_ECONOMICS_VERIFIED (Layer 4: CPC, break-even CVR confirmed)
    ↓
LAUNCHABLE               (All gates passed)
    ↓
FREE_TRAFFIC_TEST        (Live with 0 ad spend)
    ↓
PAID_TEST                ($5-10/day controlled experiment)
    ↓
PROFITABLE / KILLED
```

---

## New Probe Allocation

| Probe | Weight | Focus |
|-------|--------|-------|
| **Mass Market Scanner** | 30% | Product × Country screening at scale |
| **Market Gap Auditor** | 25% | Deep merchant quality analysis |
| **Supplier + Margin** | 25% | Supplier resolution, real economics |
| **Search/CPC/Free-Traffic** | 10% | Demand × cost verification |
| **Commerce Trace** | 5% | Operator failure/success corpus |
| **Synthesis** | 5% | Only when candidate passes gates |

---

## What Changed From v1

### KILLED
- Novelty forcing (20 new queries every hour)
- Category rotation (jumping to new niches)
- Repeated synthesis when blocker unresolved
- Generic operator traces without outcome data

### ADDED
- **State machine** for every candidate
- **Blocker Resolver** layer (explicit role)
- **CONTENT_GAP vs MERCHANT_GAP** separation
- **B2B penalty** in scoring (enterprise sales complexity)
- **Conditional synthesis** (only after gates pass)
- **GOOD_SELLER_COUNT** as standardized metric

### IMPROVED
- Supplier Radar: keep (best probe, 9.5/10)
- Product-Market Radar: keep but stop rotating categories
- Free-Traffic Radar: reduce from 20 queries to 3 high-value clusters
- Commerce Trace: keep but only A/B graded records
- Blueprint: conditional (not generated every hour)

---

## Scoring Updates

### B2B Capital Equipment Penalty

Products requiring enterprise sales get penalized:

| Factor | Penalty |
|--------|---------|
| Requires in-person demo | -15 |
| Requires site visit | -15 |
| Requires training | -10 |
| Repair/service network needed | -10 |
| Long purchasing cycle (>30 days) | -10 |
| Business customer only | -20 |
| Requires rental alternative | -10 |

**Target range:** £150-£2,000 standardized consumer/prosumer equipment

### GOOD_SELLER_COUNT Metric

For each top candidate, inspect top 10 sellers and score:

```python
seller_quality_dimensions = [
    "image_quality",        # Multiple good images, consistent, video
    "product_info",         # Specs, dimensions, manuals
    "decision_support",     # Comparisons, compatibility, FAQs
    "shipping_clarity",     # Clear delivery times, costs
    "stock_availability",   # In stock, lead times shown
    "localization",         # Native language, local currency, local payments
    "reviews",              # Quantity, quality, response
    "trust",                # Company info, contact, returns policy
    "accessories",          # Cross-sell, bundles, ecosystem
    "mobile_speed",         # Fast, modern checkout
]
```

GOOD_SELLER = seller with 8+ dimensions scoring well

---

## Content Gap vs Commerce Gap

Explicitly separate these:

```
CONTENT_GAP_SCORE = buyers have unanswered questions
MERCHANT_GAP_SCORE = few good sellers, weak retail execution
```

A product can have:
- CONTENT_GAP = 95 (lots of unanswered questions)
- MERCHANT_GAP = 18 (strong sellers exist)

→ Content opportunity (affiliate/SEO)
→ NOT store opportunity

Only proceed with MERCHANT_GAP >= 70

---

## Blocker Resolution Protocol

When a candidate has UNKNOWN fields:

1. **First pass:** Automated research (web scraping, API calls)
2. **Second pass:** Targeted deep research (specific queries, comparison sites)
3. **Third pass:** HUMAN ACTION REQUIRED

```text
BLOCKER: dealer_price = UNKNOWN
PRODUCT: Davis 6242EU
ACTION: Contact Flak (flak.no) or Hovdan (hovdan.no)
QUESTIONS:
  1. What is dealer net for 6242EU?
  2. What is minimum order quantity?
  3. Do you offer dropship/direct fulfillment?
  4. What is the lead time?
  5. What is the return policy?
  6. Is there a dealer territory restriction?
  7. Can we list products online?
FREEZE CANDIDATE UNTIL ANSWERED
```

If blocker cannot be resolved in 3 runs → KILL candidate.

---

## Blueprint Generation Rules

Blueprint ONLY generated when:

1. State = LAUNCHABLE (all prior states passed)
2. All UNKNOWN fields resolved
3. All 7 hard gates pass
4. Headroom >= 1.3
5. GOOD_SELLER_COUNT <= 3
6. No B2B penalty > -20 total

Blueprint includes:
- Executive verdict
- Country + market
- Customer profile
- Supplier chain
- Full catalog (SKUs, prices, margins)
- Competitor analysis
- Economics (real numbers)
- PDP specification
- AI expert system spec
- Imagery requirements
- Traffic strategy (free first)
- Paid test plan ($5-10/day)
- Decision gates

Blueprint NOT generated when:
- Any field is UNKNOWN
- Candidate is still in DISCOVERY/RESEARCH states
- Synthesis would repeat unchanged information

---

## Hourly Run Standard

Every run must produce one of:

```text
ADVANCE candidate (move to next state)
KILL candidate (with reason)
RESOLVE a field (change UNKNOWN → value)
```

If none of these happen:

> **The run didn't create useful information.**

---

## What stays the same

- NO LAUNCH is allowed until gates pass
- Unknown values remain UNKNOWN
- Exact-SKU local retailer checks
- Local comparison engines (Prisjakt, Hintaopas)
- Native-language research
- Hidden supplier/channel discovery
- Failure-state/operator corpus
- First-party sources > generic blogs
- Falsify rather than advocate
