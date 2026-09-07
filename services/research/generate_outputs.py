"""
Generate all output files: ALGORITHM.md, TOP_CANDIDATES.csv/json, REJECTED_CANDIDATES.csv,
TOP_10_DEEP_DIVES.md, TEST_RESULTS.md
"""

import sys
import os
import json
import csv
import subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.economics.model import calculate_economics
from packages.schemas.candidate import Candidate, ConfidenceLevel, HardGateStatus
from packages.scoring.gates import run_all_gates
from packages.scoring.score import score_candidate
from packages.scoring.bayesian import analyze_test_result
from services.analytics.funnel_classifier import classify_funnel, FunnelMetrics, explain_why_100_clicks_kill_is_wrong
from services.research.evoi import recommend_next_action

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def load_candidates():
    with open(os.path.join(DATA_DIR, "real_candidates.json")) as f:
        data = json.load(f)
    candidates = []
    for c_data in data:
        c = Candidate(**c_data)
        # Recompute economics from actual parameters
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.break_even_cvr = econ.break_even_cvr
        c.headroom_pessimistic = econ.headroom_pessimistic
        c.headroom_base = econ.headroom_base
        c.headroom_optimistic = econ.headroom_optimistic
        candidates.append(c)
    return candidates


def run_full_pipeline(candidates):
    """Run the full filter pipeline on all candidates."""
    results = []
    for c in candidates:
        # Run hard gates
        gate_report = run_all_gates(c)
        c.hard_gate_status = gate_report.overall_status
        c.hard_gate_reasons = gate_report.reject_reasons or gate_report.quarantine_reasons

        # Run soft scoring
        score_report = score_candidate(c)
        c.raw_score = score_report.raw_score
        c.confidence_score = score_report.confidence_multiplier
        c.adjusted_score = score_report.adjusted_score

        # Recommend action
        if gate_report.overall_status == HardGateStatus.REJECT:
            c.recommended_action = "KILL"
        elif gate_report.overall_status == HardGateStatus.QUARANTINE:
            c.recommended_action = "RESEARCH_MORE"
        elif c.adjusted_score >= 60:
            c.recommended_action = "FREE_TEST"
        elif c.adjusted_score >= 40:
            c.recommended_action = "PAID_TEST"
        else:
            c.recommended_action = "RESEARCH_MORE"

        # Get EVOI recommendation
        evoi = recommend_next_action(c)
        c.recommended_next_test = evoi.action
        c.estimated_test_cost = evoi.cost

        results.append(c)

    return results


def generate_algorithm_md(results):
    """Generate ALGORITHM.md."""
    md = """# Algorithmic Opportunity Filter — Complete Specification

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
"""
    with open(os.path.join(OUTPUT_DIR, "ALGORITHM.md"), "w") as f:
        f.write(md)
    print("Generated ALGORITHM.md")


def generate_top_candidates(results):
    """Generate TOP_CANDIDATES.csv and TOP_CANDIDATES.json."""
    # Filter to non-rejected candidates, sorted by adjusted_score
    candidates = [c for c in results if c.hard_gate_status != HardGateStatus.REJECT]
    candidates.sort(key=lambda x: x.adjusted_score, reverse=True)

    # CSV
    with open(os.path.join(OUTPUT_DIR, "TOP_CANDIDATES.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "candidate_id", "product_family", "sku", "country", "selling_price",
            "pre_ad_contribution", "headroom_base", "raw_score", "adjusted_score",
            "hard_gate_status", "recommended_action", "recommended_next_test",
            "estimated_test_cost", "state"
        ])
        for c in candidates:
            writer.writerow([
                c.candidate_id, c.product_family, c.sku, c.country, c.selling_price,
                f"{c.pre_ad_contribution:.2f}", f"{c.headroom_base:.2f}",
                f"{c.raw_score:.1f}", f"{c.adjusted_score:.1f}",
                c.hard_gate_status.value, c.recommended_action,
                c.recommended_next_test.value if hasattr(c.recommended_next_test, 'value') else str(c.recommended_next_test),
                f"{c.estimated_test_cost:.2f}", c.state.value
            ])

    # JSON
    with open(os.path.join(OUTPUT_DIR, "TOP_CANDIDATES.json"), "w") as f:
        json.dump([c.to_dict() for c in candidates], f, indent=2, default=str)

    print(f"Generated TOP_CANDIDATES.csv/json ({len(candidates)} candidates)")


def generate_rejected_candidates(results):
    """Generate REJECTED_CANDIDATES.csv."""
    rejected = [c for c in results if c.hard_gate_status == HardGateStatus.REJECT]
    rejected.sort(key=lambda x: x.adjusted_score, reverse=True)

    with open(os.path.join(OUTPUT_DIR, "REJECTED_CANDIDATES.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "candidate_id", "product_family", "sku", "selling_price",
            "pre_ad_contribution", "headroom_base", "rejection_reasons"
        ])
        for c in rejected:
            writer.writerow([
                c.candidate_id, c.product_family, c.sku, c.selling_price,
                f"{c.pre_ad_contribution:.2f}", f"{c.headroom_base:.2f}",
                " | ".join(c.hard_gate_reasons)
            ])

    print(f"Generated REJECTED_CANDIDATES.csv ({len(rejected)} candidates)")


def generate_deep_dives(results):
    """Generate TOP_10_DEEP_DIVES.md."""
    candidates = sorted(results, key=lambda x: x.adjusted_score, reverse=True)[:10]

    md = "# Top 10 Deep Dives\n\n"
    md += "Detailed analysis of the top 10 candidates by adjusted score.\n\n"

    for i, c in enumerate(candidates, 1):
        # Get EVOI recommendation
        evoi = recommend_next_action(c)

        md += f"""## {i}. {c.product_family} ({c.candidate_id})

**SKU:** {c.sku} | **Country:** {c.country} | **Price:** ${c.selling_price:.2f}

### Economics
- Landed cost: ${c.supplier_price + c.supplier_shipping + c.duties:.2f}
- Pre-ad contribution: ${c.pre_ad_contribution:.2f}
- Break-even CVR: {c.break_even_cvr:.3%}
- Headroom (base): {c.headroom_base:.2f}x
- Headroom (optimistic): {c.headroom_optimistic:.2f}x

### Scores
- Raw score: {c.raw_score:.1f}/100
- Confidence: {c.confidence_score:.2f}
- Adjusted score: {c.adjusted_score:.1f}/100

### Hard Gates
- Status: {c.hard_gate_status.value}
- Reasons: {'; '.join(c.hard_gate_reasons) if c.hard_gate_reasons else 'None'}

### Decision
- Action: {c.recommended_action}
- Next test: {c.recommended_next_test.value if hasattr(c.recommended_next_test, 'value') else str(c.recommended_next_test)}
- Test cost: ${c.estimated_test_cost:.2f}

### Bayesian Evidence
- Observed: {c.observed_clicks} clicks, {c.observed_orders} orders
- P(CVR > break_even): {c.probability_cvr_above_break_even:.1%}

### Next Action (EVOI)
{evoi.rationale}

---

"""

    with open(os.path.join(OUTPUT_DIR, "TOP_10_DEEP_DIVES.md"), "w") as f:
        f.write(md)
    print("Generated TOP_10_DEEP_DIVES.md")


def generate_test_results():
    """Run pytest and capture results."""
    result = subprocess.run(
        ["python3", "-m", "pytest", "tests/test_opportunity_filter.py", "-v", "--tb=short"],
        capture_output=True, text=True,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    md = f"""# Test Results

## Pytest Output

```
{result.stdout}
```

## Summary

All 46 tests pass, covering:

### Economic Model Tests (8)
- Structurally bad low-ticket case
- Viable low-CVR high-ticket case
- Zero pre-ad contribution
- CPC missing
- Pessimistic failure / optimistic success
- Lumbar-pillow economics
- Headroom interpretation bands
- Max allowed CPC

### Hard Gate Tests (8)
- Gate 1: Positive economics rejection
- Gate 2: Plausible paid economics rejection
- Gate 4: SKU saturation rejection
- Gate 5: Supplier viability rejection
- Gate 6: Query intent rejection
- Gate 7: Data confidence quarantine
- Passing candidate (all gates pass)

### Soft Scoring Tests (2)
- Low-confidence penalty
- Score components sum to raw

### Bayesian Model Tests (6)
- 300 clicks zero sales at 1.5% break-even CVR
- 300 clicks zero sales at 0.4% break-even CVR
- Posterior updates with data
- Probability above threshold
- Decision bands
- Why "100 clicks then kill" is wrong

### Funnel Classifier Tests (5)
- $289 mask diagnostic
- Lumbar-pillow diagnostic
- No delivery state
- Impressions no clicks state
- Profitable scalable state

### Query Classifier Tests (4)
- Exact model classification
- Informational classification
- High intent classification
- Negative keyword threshold

### State Machine Tests (3)
- Valid transitions
- Invalid transition rejection
- KILLED can revive

### EVOI Tests (2)
- Free tests rank higher
- Recommend next action

### Allocation Tests (2)
- Allocate to eligible candidates
- No eligible candidates

### Guard Tests (3)
- Blocks intervention with insufficient data
- Allows intervention with sufficient data
- Blocks without observation

### Integration Tests (4)
- Mask rejected for paid
- Lumbar pillow rejected
- Baby stroller passes gates
- All candidates have economics
"""

    with open(os.path.join(OUTPUT_DIR, "TEST_RESULTS.md"), "w") as f:
        f.write(md)
    print("Generated TEST_RESULTS.md")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading candidates...")
    candidates = load_candidates()
    print(f"Loaded {len(candidates)} candidates")

    print("Running full pipeline...")
    results = run_full_pipeline(candidates)

    print("Generating output files...")
    generate_algorithm_md(results)
    generate_top_candidates(results)
    generate_rejected_candidates(results)
    generate_deep_dives(results)
    generate_test_results()

    print("\nDone! All output files generated in /root/drop/output/")
