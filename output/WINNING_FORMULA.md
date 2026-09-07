# The Winning Formula

*Synthesized from 52 sources, 12 case studies, 15 strategy rules, 21 operator events, and 5 probe reports. This is what the data says.*

---

## The One Sentence

> **Find a product people already search for, in a country where the existing sellers are mediocre, with a supplier who lets you sell online at a margin that survives the CPC.**

---

## The 7 Laws (from the data, not theory)

### Law 1: Contribution Profit Per Click, Not ROAS

The data is unambiguous on this. ROAS is a vanity metric.

**Formula:**
```
contribution_per_click = (selling_price - all_costs) × CVR - CPC
```

**What the cases show:**
- C001 (ZenoX): ROAS 3.6x looks good, but real story is $80/day → $2,400/day over 60 days with 48% gross margin
- C008 (D2C skincare): Platform ROAS 4.2x but Shopify-attributed only 0.99x. Attribution lies.
- C010 (Pitiful_Gene): 3.9x ROAS on $389 AOV with 0.48% CVR. That's 36 orders from 7,500 sessions. The CVR is the real number.

**Rule:** A £500 product with £250 contribution survives much higher CPC than a £25 product with £10 contribution.

### Law 2: High Ticket Solves Small Budgets

The most successful case studies all share one trait: high enough AOV that one conversion funds weeks of testing.

| Case | AOV | Revenue | Days | First Sale |
|------|-----|---------|------|------------|
| C001 ZenoX | $58 | $103K | 60 | Day 28 |
| C006 Holly | $2,000 | $500K | 180 | Day 7 |
| C010 Pitiful_Gene | $389 | $14K | 7 | Day 11 |
| C012 SEO operator | — | $250K | 365 | Day 14 |

**Why it works:** At $10/day, you need 50 clicks per conversion at 2% CVR. If AOV is $50, one sale pays for 50 clicks. If AOV is $500, one sale pays for 500 clicks. The math is brutally simple.

**The $10k/day case (millions2.md):** 0.48% CVR, $389 AOV, 7,500 sessions for 36 orders. Not 4-5% CVR. Most operators overestimate CVR by 10x.

### Law 3: Free First, Then Paid

Every successful case in the corpus started with free or near-free validation before scaling paid.

**The free surfaces (in order of priority):**
1. Google Merchant free listings (zero cost, real impressions)
2. SEO / comparison pages (2-4 week ramp)
3. Bing Product Listings (lower competition)
4. Pinterest Product Pins (visual discovery)

**From the probe reports:** Hunter Hydrawise has content gaps (compatibility confusion, cloud outage concerns) that can be filled with comparison pages before spending a cent on ads.

**Rule:** If you can't get free impressions, paid won't fix it.

### Law 4: One Country, Lean Catalog, Focused Budget

The data is clear: spreading kills learning.

**Failed patterns:**
- Multiple countries with $10/day total = no interpretable data
- 5,000 SKU catalog with $10/day = diluted waste
- PMax + broad + high budget on day 1 =不可预测

**Successful patterns:**
- C001: 1 market, home gadgets, 60 days
- C003: 1 store, $10/day, 22 days
- C006: 1 category (outdoor ponds), 6 months
- C010: 1 niche (baby/toddler), $389 AOV

**Rule:** Launch one country. 15-50 SKUs. One campaign structure. Observe for 14-30 days before changing anything.

### Law 5: Product × Query × Economics Is The Strategy

From the millions docs: "Campaign structure barely changed. The product was baby/toddler $300-500. The lesson: product × query × economics IS the strategy."

**The three variables that matter:**

1. **Product:** People already search for it. Not "trending" — searched.
2. **Query:** Exact-model, high-intent queries with CPC you can afford.
3. **Economics:** Contribution margin > CPC × (1/CVR)

Everything else (campaign structure, bidding strategy, ad copy) is secondary.

### Law 6: Kill Bad Ideas Fast, Advance Good Ideas Slowly

From the probe reports, the system's best behavior was **falsification:**

- Finnish robot mowers → found sophisticated merchants → KILLED
- Bosch wall scanners → found established retailers → KILLED  
- RIDGID SeeSnake → found deep B2B channels → KILLED
- Hunter Hydrawise → found competent specialists → DOWNGRADED

**The operator traces (commerce trace) reinforce this:**
- CTR-004: Removing brand terms from PMax → worse performance
- CTR-010: Splitting 37 winners into new campaign → zero sales
- CTR-009: NZ store switched to PMax+broad → ROAS collapsed

**Rule:** Every run must ADVANCE, KILL, or RESOLVE a field. If it does none, the run was wasted.

### Law 7: Operations Are The Bottleneck After Validation

From the millions docs and case studies:

- C011 (Pitiful_Gene): "Payment gateways, fulfillment, support become constraints after product validates"
- C005 (Johnny FD): COGS $10,256 + shipping $1,620 + CC fees $456 + Shopify $59 + phone support $150 — that's the real P&L
- Commerce trace CTR-020: Shopify Payments switch → 46% sales drop

**Rule:** Once you have a winner, operations (supplier reliability, fulfillment, payment processing, customer support) determine whether it survives.

---

## The Decision Matrix (from data)

| Factor | Weight | What The Data Says |
|--------|--------|-------------------|
| **Existing search demand** | 20% | Products people already search for convert 5-10x better than products you must create demand for |
| **Demand / good-seller ratio** | 15% | 8 sellers with 1 good specialist > 2 sellers with 2 good specialists |
| **Contribution economics** | 20% | Break-even CVR must be achievable. Headroom >= 1.3x |
| **Supplier quality** | 15% | EU/Nordic warehouse, dropship, no MOQ, stock feed |
| **Merchant weakness** | 10% | Bad images + weak content + poor localization = your gap |
| **CPC relative to contribution** | 10% | Not cheap CPC — cheap CPC relative to what you make per order |
| **Localization opportunity** | 5% | Native language, local payment (Vipps), local trust |
| **Accessory/bundle upside** | 5% | Attach revenue through ecosystem products |

---

## The Failure Patterns (from data)

### Pattern 1: The CVR Illusion
**What operators believe:** "I'll get 4-5% CVR"
**What data shows:** 0.48% is realistic for high-ticket (C010). 1-2% is optimistic for most categories.
**Kill rule:** If break-even CVR > 3%, the product probably doesn't work at small scale.

### Pattern 2: The ROAS Trap
**What operators believe:** "3x ROAS = profitable"
**What data shows:** Platform ROAS 4.2x can mean Shopify-attributed 0.99x (C008). Branded search inflates PMax ROAS. Attribution lies.
**Kill rule:** Reconcile to store-side P&L. Track COGS, shipping, fees, returns daily.

### Pattern 3: The Category Rotation
**What operators do:** Find something interesting → research → hit blocker → find new interesting thing
**What data says:** The $10k/day case barely changed campaign structure. The product did the work. Stop rotating. Attack blockers.
**Kill rule:** If a candidate reaches 65%+ confidence, spend all research time resolving its specific blockers.

### Pattern 4: The B2B Drift
**What the scoring accidentally does:** Gravitates toward high AOV industrial equipment
**What the data says:** RIDGID SeeSnake ($7k) = demo, service, training, rental alternative, long cycle. Not lightweight ecommerce.
**Kill rule:** Penalize: requires demo (-15), requires site visit (-15), business customer only (-20). Target: £150-£2,000 consumer/prosumer.

### Pattern 5: The Content-Commerce Confusion
**What operators do:** Find unanswered buyer questions → assume it's a store opportunity
**What data says:** Bosch had content gaps (compatibility confusion) but strong merchants. Content opportunity ≠ store opportunity.
**Kill rule:** Separate CONTENT_GAP from MERCHANT_GAP. Only proceed if MERCHANT_GAP >= 70.

---

## The Winning Pattern (from all successful cases)

```
PRODUCT: Already searched for. Not trending — searched.
AOV: £150-£2,000 (high enough to survive CPC, low enough for impulse)
COUNTRY: One affluent market with weak merchants
SUPPLIER: EU/Nordic warehouse, dropship, no MOQ, stock feed
MERCHANT GAP: Few good sellers, mediocre images/content/localization
CPC: Cheap relative to contribution (not absolute cheap)
LAUNCH: Free listings first → observe → $5-10/day paid test → scale or kill
CATALOG: 15-50 SKUs, lean, well-fed
TIMELINE: 14-30 days observation before changing anything
```

---

## The One-Page Checklist

Before launching any store, answer YES to all:

- [ ] Do people already search for this exact product?
- [ ] Is the AOV high enough that one sale funds 100+ clicks?
- [ ] Are there fewer than 3 GOOD sellers in the target country?
- [ ] Do the existing sellers have weak images/content/localization?
- [ ] Can we get EU/Nordic supplier with dropship and no MOQ?
- [ ] Is the contribution margin > 3× expected CPC?
- [ ] Can we launch with free listings before spending on ads?
- [ ] Is this ONE country with a lean catalog?
- [ ] Can we explain why existing sellers haven't filled this gap?
- [ ] Does the product pass the "would I buy this?" test?

If any answer is NO → don't launch. Resolve the blocker or kill.

---

## What We Have Now vs What We Need

### Have
- 52 research sources
- 12 quantitative case studies
- 15 strategy rules with confidence levels
- 21 operator traces (13 Grade A)
- 5 probe reports (Supplier, Product-Market, Free-Traffic, Commerce, Blueprint)
- Economic model with Bayesian scoring
- Hard gates system (7 gates)
- State machine for candidates
- BigQuery data warehouse (7 tables, 111 rows)

### Need
- Real dealer prices (emails sent, waiting)
- Real CPC data (waiting for Google Ads access)
- Real search volume (waiting for Keyword Planner)
- First free listings test (waiting for Merchant Center product feed)

### Blocker
**Everything is blocked on supplier economics.** The scoring engine, the state machine, the gates — they all work. But they need REAL numbers, not UNKNOWN.

The 4 emails I just sent are the single highest-ROI action in this entire project. When Flak responds with Davis dealer prices, we either have a launchable candidate or we don't. Everything else is preparation for that moment.

---

*This document is the distillation of everything in the corpus. It should be read before any product decision. If a new product can't pass the 7 Laws, it doesn't matter how interesting it looks.*
