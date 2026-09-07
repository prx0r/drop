"""
Master Pipeline — Wires everything together:
1. Load candidates
2. Calculate economics
3. Run hard gates
4. Score passing candidates
5. Run Bayesian analysis
6. Classify products
7. Generate auction explanation
8. Recommend next actions via EVOI
9. Allocate capital
10. Output everything
"""

from __future__ import annotations
import os
import json
from dataclasses import dataclass, field
from typing import List, Optional

from packages.economics.model import calculate_economics
from packages.schemas.candidate import Candidate, HardGateStatus, CandidateState
from packages.scoring.gates import run_all_gates
from packages.scoring.score import score_candidate
from packages.scoring.bayesian import create_posterior
from services.analytics.product_classifier import classify_product, ProductClass, ClassificationResult
from services.analytics.free_signals import FreeListingData, calculate_free_signal_score, FreeSignalResult
from packages.scoring.funnel_bayesian import analyze_funnel_bayesian, FunnelBayesianResult
from services.research.evoi import recommend_next_action
from services.research.allocation import allocate_budget
from services.research.auction_explainer import generate_auction_explanation, AuctionExplanation
from services.research.country_selection import get_best_country, CountryScore
from services.research.scaling import ScalingEngine
from services.catalog.product_expert import ProductExpert

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


@dataclass
class PipelineCandidateResult:
    candidate: Candidate
    gate_report: object = None
    score_report: object = None
    classification: Optional[ClassificationResult] = None
    bayesian: Optional[object] = None
    funnel_bayesian: Optional[FunnelBayesianResult] = None
    free_signal: Optional[FreeSignalResult] = None
    auction_explanation: Optional[AuctionExplanation] = None
    evoi_action: object = None
    country_score: Optional[CountryScore] = None


@dataclass
class PipelineResult:
    candidates: List[PipelineCandidateResult] = field(default_factory=list)
    total_loaded: int = 0
    passed_gates: int = 0
    rejected: int = 0
    quarantined: int = 0
    classification_counts: dict = field(default_factory=dict)
    budget_allocation: object = None
    top_candidate: Optional[PipelineCandidateResult] = None


def load_candidates() -> List[Candidate]:
    path = os.path.join(DATA_DIR, "real_candidates.json")
    with open(path) as f:
        data = json.load(f)
    candidates = []
    for c_data in data:
        c = Candidate(**c_data)
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


def run_pipeline(candidates: Optional[List[Candidate]] = None) -> PipelineResult:
    """Execute the full pipeline."""
    if candidates is None:
        candidates = load_candidates()

    result = PipelineResult(total_loaded=len(candidates))
    product_expert = ProductExpert()
    scaling_engine = ScalingEngine()

    all_pipeline_results: List[PipelineCandidateResult] = []

    for c in candidates:
        pcr = PipelineCandidateResult(candidate=c)

        # 2. Economics already calculated during load

        # 3. Run hard gates
        gate_report = run_all_gates(c)
        pcr.gate_report = gate_report
        c.hard_gate_status = gate_report.overall_status
        c.hard_gate_reasons = gate_report.reject_reasons or gate_report.quarantine_reasons

        if gate_report.overall_status == HardGateStatus.REJECT:
            result.rejected += 1
        elif gate_report.overall_status == HardGateStatus.QUARANTINE:
            result.quarantined += 1
        else:
            result.passed_gates += 1

        # 4. Score
        score_report = score_candidate(c)
        pcr.score_report = score_report
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

        # 5. Bayesian analysis
        posterior = create_posterior(
            clicks=c.observed_clicks,
            orders=c.observed_orders,
        )
        pcr.bayesian = posterior
        c.posterior_alpha = posterior.posterior_alpha
        c.posterior_beta = posterior.posterior_beta
        c.posterior_mean_cvr = posterior.posterior_mean_cvr
        c.probability_cvr_above_break_even = posterior.probability_above(c.break_even_cvr)

        # 5b. Funnel Bayesian
        funnel_result = analyze_funnel_bayesian(
            impressions=c.observed_clicks * 50 if c.observed_clicks > 0 else 0,
            clicks=c.observed_clicks,
            atcs=int(c.observed_clicks * 0.05) if c.observed_clicks > 0 else 0,
            checkouts=int(c.observed_clicks * 0.02) if c.observed_clicks > 0 else 0,
            orders=c.observed_orders,
        )
        pcr.funnel_bayesian = funnel_result

        # 6. Classify product
        classification = classify_product(c)
        pcr.classification = classification
        product_class = classification.product_class.value
        result.classification_counts[product_class] = result.classification_counts.get(product_class, 0) + 1

        # 7. Auction explanation (for non-rejected)
        if gate_report.overall_status != HardGateStatus.REJECT:
            auction_expl = generate_auction_explanation(c)
            pcr.auction_explanation = auction_expl

        # 8. EVOI
        evoi_action = recommend_next_action(c)
        pcr.evoi_action = evoi_action
        c.recommended_next_test = evoi_action.action
        c.estimated_test_cost = evoi_action.cost

        # Register in product expert
        product_expert.register_product(c)

        # Country score
        country = get_best_country(product_price=c.selling_price)
        pcr.country_score = country

        all_pipeline_results.append(pcr)

    result.candidates = all_pipeline_results

    # 9. Budget allocation
    all_candidates = [pcr.candidate for pcr in all_pipeline_results]
    allocation = allocate_budget(all_candidates)
    result.budget_allocation = allocation

    # Find top candidate
    non_rejected = [pcr for pcr in all_pipeline_results
                    if pcr.candidate.hard_gate_status != HardGateStatus.REJECT]
    if non_rejected:
        non_rejected.sort(key=lambda x: x.candidate.adjusted_score, reverse=True)
        result.top_candidate = non_rejected[0]

    return result


def generate_final_selection(pipeline_result: PipelineResult) -> str:
    """Generate FINAL_SELECTION.md content."""
    top = pipeline_result.top_candidate
    if not top:
        return "# Final Selection\n\nNo viable candidates found.\n"

    c = top.candidate
    expl = top.auction_explanation
    classification = top.classification
    evoi = top.evoi_action

    md = f"""# Final Selection — Top Candidate

## {c.product_family} ({c.candidate_id})

**SKU:** {c.sku} | **Country:** {c.country} | **Price:** ${c.selling_price:.2f}
**Classification:** {classification.product_class.value if classification else 'N/A'}
**Adjusted Score:** {c.adjusted_score:.1f}/100 | **Hard Gate:** {c.hard_gate_status.value}

---

## Why This Candidate?

{expl.explanation_paragraph if expl else 'No explanation generated.'}

---

## Economics

| Metric | Value |
|--------|-------|
| Selling Price | ${c.selling_price:.2f} |
| Landed Cost | ${c.supplier_price + c.supplier_shipping + c.duties:.2f} |
| Pre-ad Contribution | ${c.pre_ad_contribution:.2f} |
| Break-even CVR | {c.break_even_cvr:.3%} |
| Headroom (base) | {c.headroom_base:.2f}x |
| Headroom (optimistic) | {c.headroom_optimistic:.2f}x |
| Expected CPC | ${c.expected_cpc:.2f} |

## Bayesian Evidence

| Metric | Value |
|--------|-------|
| Observed Clicks | {c.observed_clicks} |
| Observed Orders | {c.observed_orders} |
| P(CVR > break_even) | {c.probability_cvr_above_break_even:.1%} |
| Posterior Mean CVR | {c.posterior_mean_cvr:.4%} |

## Classification: {classification.product_class.value if classification else 'N/A'}

{chr(10).join(f'- {r}' for r in (classification.reasoning if classification else []))}

## Next Action (EVOI)

**Action:** {evoi.action.value if evoi else 'N/A'}
**Cost:** ${evoi.cost:.2f}
**Rationale:** {evoi.rationale}

## Country Recommendation

**Best Country:** {top.country_score.country if top.country_score else 'N/A'}
**Composite Score:** {f'{top.country_score.composite_score:.3f}' if top.country_score else '0'}

---

*Generated by the Dropshipping Opportunity Filter pipeline.*
"""
    return md


def generate_launch_plan(pipeline_result: PipelineResult) -> str:
    """Generate LAUNCH_PLAN.md content."""
    top = pipeline_result.top_candidate
    if not top:
        return "# Launch Plan\n\nNo viable candidates to launch.\n"

    c = top.candidate
    classification = top.classification
    evoi = top.evoi_action

    md = f"""# Launch Plan — {c.product_family}

## Candidate: {c.candidate_id} | SKU: {c.sku}

---

## Phase 1: Validation (Days 1-7)

### Day 1-2: Free Listing Setup
- [ ] Enable Google Free Listings for {c.sku}
- [ ] Verify product feed is eligible
- [ ] Check Merchant Center for disapprovals
- **Cost:** $0
- **Expected outcome:** Organic impressions data within 48-72 hours

### Day 3-5: Free Traffic Collection
- [ ] Monitor organic impressions, clicks, CTR
- [ ] Track add-to-cart rate from organic traffic
- [ ] Collect Search Console query data
- **Cost:** $0
- **Minimum evidence:** 100+ impressions, 20+ clicks

### Day 6-7: Free Signal Evaluation
- [ ] Calculate free_signal_score
- [ ] Classify: ZERO_IMPRESSIONS / IMPRESSIONS_NO_CLICKS / CLICKS_NO_ATC / CLICKS_WITH_ATC
- [ ] Decision gate: proceed to paid test or kill/fix
- **Cost:** $0
- **Decision:** If CLICKS_WITH_ATC or free_signal_score >= 0.4 → proceed

---

## Phase 2: Initial Paid Test (Days 8-14)

### Day 8: Launch $5/day Test
- [ ] Create Shopping campaign, $5/day budget
- [ ] Set target ROAS bid strategy
- [ ] Enable all query types initially
- **Budget:** $5/day ($35 total for 7 days)
- **Expected clicks:** ~{35 / c.expected_cpc:.0f} clicks at ${c.expected_cpc:.2f} CPC

### Day 10-12: First Data Check
- [ ] 50+ clicks collected
- [ ] Check ATC rate, conversion rate
- [ ] Apply Overintervention Guard: DO NOT change bids/budget yet
- **Decision:** Continue or kill

### Day 14: Paid Test Evaluation
- [ ] 100+ clicks collected
- [ ] Calculate P(CVR > break_even) = {c.probability_cvr_above_break_even:.1%}
- [ ] If P >= 70% → scale to $10/day
- [ ] If P 30-70% → extend test 7 more days
- [ ] If P < 30% → kill or major fix
- **Budget:** $35 total

---

## Phase 3: Scaling (Days 15-30)

### Scaling Rules
- **Only scale when ALL conditions met:**
  - [ ] Positive contribution (profit > $0)
  - [ ] P(CVR > break_even) >= 70%
  - [ ] Supplier reliability >= 0.5
  - [ ] CVR not collapsing (ratio >= 0.7x baseline)
  - [ ] Returns rate <= 10%
- **Increment:** 15% per scale event
- **Max budget:** $10/day

### Day 15-21: $10/day
- [ ] Scale to $10/day if conditions met
- [ ] Monitor daily contribution
- [ ] Track ROAS
- **Budget:** $70 total (14 days × $5)

### Day 22-30: Scale Decision
- [ ] If profitable and stable → maintain $10/day
- [ ] If contribution positive but volatile → hold at $10/day
- [ ] If contribution negative → stop, evaluate
- **Budget:** $90 total (9 days × $10)

---

## Budget Summary

| Phase | Duration | Daily Budget | Total |
|-------|----------|-------------|-------|
| Validation | 7 days | $0 | $0 |
| Initial Test | 7 days | $5 | $35 |
| Scaling | 15 days | $10 | $90 |
| **Total** | **29 days** | — | **$125** |

---

## Milestones

| Day | Milestone | Decision |
|-----|-----------|----------|
| 3 | First organic data | If no impressions → check feed |
| 7 | Free signal score | If score < 0.4 → kill |
| 14 | Paid test complete | If P(CVR) < 30% → kill |
| 21 | Scaling check | If negative contribution → stop |
| 30 | Full evaluation | Profitable? Scale or stop |

---

## Risk Factors

1. **CVR is the key unknown** — base estimate {c.cvr_base:.2%} is unvalidated
2. **{c.shopping_seller_count} sellers** — {'low competition' if c.shopping_seller_count <= 5 else 'moderate competition' if c.shopping_seller_count <= 15 else 'high competition'}
3. **Shipping {c.shipping_days} days** — {'fast' if c.shipping_days <= 7 else 'standard' if c.shipping_days <= 14 else 'slow, may hurt conversion'}
4. **Supplier reliability {c.supplier_reliability:.2f}** — {'healthy' if c.supplier_reliability >= 0.7 else 'needs monitoring' if c.supplier_reliability >= 0.5 else 'risky'}

---

*Generated by the Dropshipping Opportunity Filter pipeline.*
"""
    return md


def generate_unknownknowns(pipeline_result: PipelineResult) -> str:
    """Generate CURRENT_UNKNOWNKNOWNS.md content."""
    top = pipeline_result.top_candidate
    if not top:
        return "# Current Unknowns\n\nNo candidates to analyze.\n"

    c = top.candidate
    classification = top.classification

    unknowns = []

    # CVR unknown
    if c.cvr_confidence.value in ["VERY_LOW", "LOW"]:
        unknowns.append({
            "what": "True CVR for this product at this price point",
            "why_it_matters": f"Break-even CVR is {c.break_even_cvr:.2%}. If actual CVR is below this, every paid click loses money.",
            "cheapest_test": "Free listing test ($0) — collect organic CTR and ATC data",
            "cost": "$0",
            "expected_timeline": "3-7 days",
        })

    # CPC unknown
    if c.cpc_confidence_domain.value in ["VERY_LOW", "LOW"]:
        unknowns.append({
            "what": "Actual CPC in this market",
            "why_it_matters": f"Estimated CPC is ${c.expected_cpc:.2f}. Actual CPC could be 30-50% different.",
            "cheapest_test": "Check Google Keyword Planner for CPC range",
            "cost": "$0",
            "expected_timeline": "1 day",
        })

    # Supplier unknown
    if c.supplier_confidence.value in ["VERY_LOW", "LOW"]:
        unknowns.append({
            "what": "Supplier reliability and fulfillment speed",
            "why_it_matters": f"Supplier reliability is {c.supplier_reliability:.2f}. Low reliability = high return rate and bad reviews.",
            "cheapest_test": "Place test order from supplier",
            "cost": f"${c.selling_price:.2f}" if c.selling_price > 0 else "$0",
            "expected_timeline": "7-14 days",
        })

    # Competition unknown
    if c.competition_confidence.value in ["VERY_LOW", "LOW"]:
        unknowns.append({
            "what": "Actual competitor pricing and positioning",
            "why_it_matters": f"{c.shopping_seller_count} known sellers, but actual landscape may differ.",
            "cheapest_test": "Manual SERP check + Shopping tab scan",
            "cost": "$0",
            "expected_timeline": "1 day",
        })

    # Demand validation
    if c.observed_clicks == 0:
        unknowns.append({
            "what": "Whether real buyers search for this product",
            "why_it_matters": f"Monthly search volume is {c.monthly_search_volume:,} but this is estimated, not validated.",
            "cheapest_test": "Enable free listings and measure organic traffic",
            "cost": "$0",
            "expected_timeline": "3-7 days",
        })

    # Always include these
    unknowns.append({
        "what": "Landing page conversion rate",
        "why_it_matters": "Even with perfect traffic, the landing page must convert. Unknown until tested.",
        "cheapest_test": "Run free traffic and measure ATC rate",
        "cost": "$0",
        "expected_timeline": "7-14 days",
    })

    unknowns.append({
        "what": "Return rate in practice",
        "why_it_matters": f"Assumed {c.expected_returns_cost / c.selling_price:.0%} returns, but actual rate depends on product quality and description accuracy.",
        "cheapest_test": "Track returns after first 10 orders",
        "cost": "$0 (only matters after sales start)",
        "expected_timeline": "14-30 days",
    })

    md = f"""# Current Unknowns — {c.product_family} ({c.candidate_id})

## Summary

| Category | Status |
|----------|--------|
| Economics | {'Known' if c.economics_confidence.value in ['HIGH', 'MEDIUM'] else 'Unknown'} — headroom {c.headroom_base:.2f}x |
| CVR | {'Unknown' if c.cvr_confidence.value in ['VERY_LOW', 'LOW'] else 'Estimated'} — break-even at {c.break_even_cvr:.2%} |
| CPC | {'Unknown' if c.cpc_confidence_domain.value in ['VERY_LOW', 'LOW'] else 'Estimated'} — ${c.expected_cpc:.2f} |
| Supplier | {'Unknown' if c.supplier_confidence.value in ['VERY_LOW', 'LOW'] else 'Estimated'} — {c.supplier_reliability:.2f} reliability |
| Competition | {'Unknown' if c.competition_confidence.value in ['VERY_LOW', 'LOW'] else 'Known'} — {c.shopping_seller_count} sellers |
| Demand | {'Unknown' if c.demand_confidence.value in ['VERY_LOW', 'LOW'] else 'Known'} — {c.monthly_search_volume:,}/mo |

---

## Unknowns Ranked by Impact

"""

    for i, u in enumerate(unknowns, 1):
        md += f"""### {i}. {u['what']}

**Why it matters:** {u['why_it_matters']}

**Cheapest test:** {u['cheapest_test']}

**Cost:** {u['cost']} | **Timeline:** {u['expected_timeline']}

---

"""

    md += """## Cheapest Path to Knowledge

| Priority | Unknown | Test | Cost | Days |
|----------|---------|------|------|------|
"""

    for i, u in enumerate(unknowns[:5], 1):
        md += f"| {i} | {u['what'][:40]}... | {u['cheapest_test'][:30]} | {u['cost']} | {u['expected_timeline']} |\n"

    md += """
## Total Cost to Resolve Top 5 Unknowns: $0

All critical unknowns can be resolved with free tests before spending any paid budget.

---

*Generated by the Dropshipping Opportunity Filter pipeline.*
"""
    return md
