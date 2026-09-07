# Algorithmic Opportunity Filter — Complete Specification

## Overview

This system answers four questions for every PRODUCT × COUNTRY × SUPPLIER × QUERY × SKU:
1. Should we investigate this opportunity?
2. Should we launch it?
3. How much evidence should we buy?
4. Should we WAIT / FIX / KILL / SCALE once live?

**Max paid testing budget:** $10/day TOTAL. $0/day preferred. Free surfaces first.

---

## 1. Economic Model (`packages/economics/model.py`)

### Core Formulas

```
landed_cost = supplier_price + supplier_shipping + duties
payment_fees = (selling_price × 0.029) + $0.20
expected_refunds = selling_price × 0.05
pre_ad_contribution = selling_price - landed_cost - payment_fees - expected_refunds

break_even_CVR = expected_CPC / pre_ad_contribution
break_even_CPC = expected_CVR × pre_ad_contribution

profit_per_click = (expected_CVR × pre_ad_contribution) - expected_CPC

economic_headroom = (expected_CVR × pre_ad_contribution) / expected_CPC
```

### Headroom Interpretation Bands

| Headroom | Band | Meaning |
|----------|------|---------|
| < 1.0 | STRUCTURALLY LOSING | Every scenario loses money |
| 1.0 - 1.20 | EXTREMELY FRAGILE | Only works if everything goes right |
| 1.20 - 1.50 | MARGINAL | Some room for error |
| 1.50 - 2.00 | INTERESTING | Good economics, worth testing |
| 2.00 - 3.00 | VERY INTERESTING | Strong room for error |
| 3.00+ | EXCEPTIONAL | Rare, excellent economics |

### Three CVR Scenarios

- **Pessimistic:** 0.2% CVR (worst realistic case)
- **Base:** 0.5% CVR (expected)
- **Optimistic:** 1.0% CVR (best realistic case)

### Key Examples from Research

```
Low-ticket bad:
  $30 contribution, $1 CPC, 2% CVR → profit/click = -$0.40

High-ticket good:
  $250 contribution, $0.80 CPC, 0.8% CVR → headroom = 2.5

Lumbar pillow:
  $30 contribution, $2.13 CPC → needs 7.1% CVR → dead

$289 mask:
  $200 contribution, $2.10 CPC → needs 0.73% CVR → barely viable at base
```

---

## 2. Hard Gates (`packages/scoring/gates.py`)

Binary rejection BEFORE soft scoring. Each gate is independent.

| Gate | Rule | Threshold |
|------|------|-----------|
| 1: Positive Economics | pre_ad_contribution <= 0 | REJECT |
| 2: Plausible Paid Economics | headroom_optimistic < 1.0 | REJECT paid |
| | headroom_base < 1.2 | QUARANTINE |
| 3: Shipping Competitiveness | shipping_days > 21 | REJECT |
| | shipping_gap > 10 days | QUARANTINE |
| 4: SKU Saturation | GTIN sellers > 20 | REJECT |
| | Amazon + sellers > 10 | QUARANTINE |
| 5: Supplier Viability | reliability < 0.3 | REJECT |
| | reliability < 0.5 | QUARANTINE |
| 6: Query Purchase Intent | intent_score <= 0.1 | REJECT |
| | intent_score < 0.4 | QUARANTINE |
| 7: Data Confidence | >= 4 VERY_LOW fields | QUARANTINE |

**Critical rule:** A candidate with headroom_optimistic < 1.0 is rejected for paid regardless of popularity score.

---

## 3. Soft Scoring (`packages/scoring/score.py`)

0-100 transparent score with configurable weights:

| Component | Weight | What it measures |
|-----------|--------|------------------|
| ECONOMICS | 35 | Headroom, contribution, break-even |
| QUERY/PURCHASE INTENT | 15 | Search intent, exact query share |
| EXACT SKU COMPETITION | 15 | Seller count, Amazon, price percentile |
| SUPPLIER/FULFILLMENT | 15 | Reliability, shipping speed, selectivity |
| DEMAND/TREND | 10 | Search volume, trend direction |
| MERCHANT DIFFERENTIATION | 10 | How different is our offering |

### Uncertainty Penalty

```
adjusted_score = raw_score × confidence_multiplier

HIGH confidence:     × 1.00
MEDIUM confidence:   × 0.85
LOW confidence:      × 0.65
VERY_LOW confidence: × 0.40
```

**Every component exposes raw reasons for transparency.**

---

## 4. Bayesian Evidence Model (`packages/scoring/bayesian.py`)

### Why "100 clicks then kill" is wrong

At 0.48% CVR (the $10k baby product's actual rate):

| Clicks | P(0 sales) |
|--------|------------|
| 50 | 79% |
| 100 | **62%** |
| 150 | 49% |
| 200 | 38% |
| 300 | 24% |
| 500 | 9% |

**Killing at 100 clicks would discard 62% of viable products.**

### Beta-Binomial Posterior

```
prior: Beta(1, 1) — uniform, weak prior
posterior: Beta(1 + orders, 1 + clicks - orders)
posterior_mean_CVR = α / (α + β)
```

### Decision Bands

| P(CVR > break_even) | Decision |
|---------------------|----------|
| >= 0.90 | STRONGLY_PROMISING |
| 0.70 - 0.90 | PROMISING |
| 0.30 - 0.70 | UNCERTAIN |
| 0.05 - 0.30 | WEAK |
| < 0.05 | STRONG_EVIDENCE_AGAINST |

---

## 5. Funnel State Classifier (`services/analytics/funnel_classifier.py`)

Evidence-based (not calendar-based) funnel diagnosis:

| State | Evidence | Likely Problem |
|-------|----------|----------------|
| NO_DELIVERY | 0 impressions | Feed/eligibility/bids |
| IMPRESSIONS_NO_CLICKS | impressions, 0 clicks | Title/image/price/query |
| CLICKS_NO_ATC | clicks, 0 ATC | Product/offer/trust |
| ATC_NO_CHECKOUT | ATC, 0 checkout | Offer/friction |
| CHECKOUT_NO_PURCHASE | checkout, 0 purchase | Shipping/payment/trust |
| PURCHASE_UNPROFITABLE | purchases, negative profit | Economics/CPC |
| PROFITABLE_SPARSE | few purchases, profit | Variance/traffic volume |
| PROFITABLE_SCALABLE | many purchases, profit | Ready to scale |

### Real Cases

- **$289 mask:** 148 clicks, 0 ATC → CLICKS_NO_ATC (not delivery)
- **Lumbar pillow:** 81 clicks, 4 ATC, 1 checkout, 0 purchase → CHECKOUT_NO_PURCHASE (shipping friction)
- **Pitiful_Gene:** Days 1-4 dead, days 5-6 movement → PROFITABLE_SPARSE (was always viable)

---

## 6. Overintervention Guard (`services/analytics/guard.py`)

Every change must contain:
- **Observation:** What did we see?
- **Hypothesis:** What do we think is happening?
- **Action:** What specific change are we making?
- **Expected effect:** What change do we expect?
- **Minimum evidence:** How much data before we evaluate?
- **Evaluation date/condition:** When/how do we evaluate?

If insufficient evidence (< 20 clicks): **RECOMMENDATION = DO_NOTHING**

---

## 7. Expected Value of Information (`services/research/evoi.py`)

For every uncertain candidate, find the cheapest next action:

| Action | Cost | What it reveals |
|--------|------|-----------------|
| CHECK_SERP | $0 | Competition structure |
| CHECK_SUPPLIER | $0 | Reliability, stock |
| GET_SHIPPING_QUOTE | $0 | True landed cost |
| FETCH_KEYWORD_DATA | $0 | Search volume, CPC |
| FETCH_GTIN_SELLERS | $0 | SKU saturation |
| ENABLE_FREE_LISTING | $0 | Real demand signal |
| RUN_FREE_TRAFFIC_TEST | $0 | CVR signal |
| RUN_$5_PAID_TEST | $5 | CVR signal (moderate) |
| RUN_$10_PAID_TEST | $10 | CVR signal (strong) |

**EV/OI = Information Value × Uncertainty Reduction ÷ Cost**

Free tests always rank highest.

---

## 8. State Machine (`services/research/state_machine.py`)

```
DISCOVERED → RESEARCHING → HARD_REJECTED
                         → SUPPLIER_VALIDATED → BUILD_READY
                         → BUILD_READY → FREE_LISTINGS_LIVE
                                       → PAID_TEST_READY
            FREE_LISTINGS_LIVE → FREE_SIGNAL_POSITIVE → PAID_TEST_READY
                               → FREE_SIGNAL_WEAK → KILLED / FIXING
            PAID_TEST_READY → PAID_TESTING → PROFITABLE_SPARSE → PROFITABLE_SCALABLE
                                            → PAUSED → FIXING → KILLED
                                            → KILLED
```

---

## 9. Capital Allocation (`services/research/allocation.py`)

```
PRIORITY = EXPECTED_INFORMATION_GAIN × EXPECTED_ECONOMIC_UPSIDE ÷ COST_OF_TEST
```

One $10/day budget. Not split evenly. Free tests get 100× multiplier.

---

## Test Results

See TEST_RESULTS.md for complete pytest output.

---

*Generated by the Dropshipping Opportunity Filter pipeline.*
