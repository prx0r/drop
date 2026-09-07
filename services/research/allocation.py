"""
Capital Allocation — Rank eligible experiments by expected value of information.
Budget: $10/day total, not split evenly.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from packages.schemas.candidate import Candidate, RecommendedAction, TestType, CandidateState


@dataclass
class ExperimentCandidate:
    """Candidate eligible for budget allocation."""
    candidate: Candidate
    expected_information_gain: float = 0.0  # How much uncertainty does this test remove?
    expected_economic_upside: float = 0.0  # If positive, how much money can we make?
    cost_of_test: float = 0.0  # How much does this test cost?
    priority_score: float = 0.0  # EIG * upside / cost
    max_daily_budget: float = 10.0


@dataclass
class AllocationResult:
    """Budget allocation decision."""
    total_budget: float = 10.0
    allocations: List[dict] = field(default_factory=list)
    unallocated: float = 0.0
    rationale: str = ""


# Test cost estimates
TEST_COSTS = {
    TestType.CHECK_SERP: 0.0,
    TestType.CHECK_SUPPLIER: 0.0,
    TestType.GET_SHIPPING_QUOTE: 0.0,
    TestType.FETCH_KEYWORD_DATA: 0.0,
    TestType.FETCH_GTIN_SELLERS: 0.0,
    TestType.ENABLE_FREE_LISTING: 0.0,
    TestType.RUN_FREE_TRAFFIC_TEST: 0.0,
    TestType.RUN_5_PAID_TEST: 5.0,
    TestType.RUN_10_PAID_TEST: 10.0,
}


def calculate_information_gain(candidate: Candidate, test_type: TestType) -> float:
    """
    Estimate how much uncertainty a test removes.
    Higher = more valuable to run.
    """
    gain = 0.0

    # Free tests always have high information gain relative to cost
    if test_type in [TestType.CHECK_SERP, TestType.CHECK_SUPPLIER,
                     TestType.GET_SHIPPING_QUOTE, TestType.FETCH_KEYWORD_DATA,
                     TestType.FETCH_GTIN_SELLERS]:
        gain = 0.8  # High information, zero cost

    elif test_type == TestType.ENABLE_FREE_LISTING:
        # Free listings give real demand signal
        gain = 0.7

    elif test_type == TestType.RUN_FREE_TRAFFIC_TEST:
        # Free traffic test gives CVR signal
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            gain = 0.9  # Very valuable if CVR is unknown
        else:
            gain = 0.3  # Less valuable if CVR already estimated

    elif test_type == TestType.RUN_5_PAID_TEST:
        # $5 paid test gives strong CVR signal
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            gain = 0.85
        else:
            gain = 0.4

    elif test_type == TestType.RUN_10_PAID_TEST:
        # $10 paid test
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            gain = 0.9
        else:
            gain = 0.5

    # Reduce gain if economics are already well-understood
    if candidate.economics_confidence.value == "HIGH":
        gain *= 0.7

    return gain


def calculate_economic_upside(candidate: Candidate) -> float:
    """
    Estimate economic upside if this candidate works.
    Based on headroom and estimated monthly volume.
    """
    if candidate.headroom_base <= 0:
        return 0.0

    # Monthly upside = headroom * monthly_clicks * profit_per_click
    monthly_clicks = candidate.monthly_search_volume * candidate.exact_query_share * 0.02  # 2% CTR
    profit_per_click = (candidate.cvr_base * candidate.pre_ad_contribution) - candidate.expected_cpc

    if profit_per_click <= 0:
        return 0.0

    monthly_upside = monthly_clicks * profit_per_click
    return max(0.0, monthly_upside)


def allocate_budget(
    candidates: List[Candidate],
    total_budget: float = 10.0,
    min_allocation: float = 3.0,
) -> AllocationResult:
    """
    Rank eligible experiments by: EIG × UPSIDE ÷ COST
    One $10/day budget, not split evenly.
    """
    result = AllocationResult(total_budget=total_budget)

    # Filter to eligible candidates
    eligible = []
    for c in candidates:
        if c.state in [CandidateState.FREE_LISTINGS_LIVE, CandidateState.FREE_SIGNAL_POSITIVE,
                        CandidateState.PAID_TEST_READY, CandidateState.PAID_TESTING,
                        CandidateState.PROFITABLE_SPARSE]:
            if c.hard_gate_status.value != "REJECT":
                eligible.append(c)

    if not eligible:
        result.rationale = "No eligible candidates for budget allocation."
        return result

    # Score each candidate
    experiments = []
    for c in eligible:
        # Determine test type
        if c.state == CandidateState.FREE_LISTINGS_LIVE:
            test_type = TestType.RUN_FREE_TRAFFIC_TEST
            cost = 0.0
        elif c.state == CandidateState.FREE_SIGNAL_POSITIVE:
            test_type = TestType.RUN_5_PAID_TEST
            cost = 5.0
        elif c.state == CandidateState.PAID_TEST_READY:
            test_type = TestType.RUN_10_PAID_TEST
            cost = 10.0
        elif c.state == CandidateState.PAID_TESTING:
            test_type = TestType.RUN_10_PAID_TEST
            cost = 10.0
        elif c.state == CandidateState.PROFITABLE_SPARSE:
            test_type = TestType.RUN_10_PAID_TEST
            cost = 10.0
        else:
            continue

        eig = calculate_information_gain(c, test_type)
        upside = calculate_economic_upside(c)

        # Priority = EIG * upside / cost (handle zero cost)
        if cost > 0:
            priority = (eig * upside) / cost
        else:
            priority = eig * upside * 10  # Free tests get huge priority boost

        experiments.append(ExperimentCandidate(
            candidate=c,
            expected_information_gain=eig,
            expected_economic_upside=upside,
            cost_of_test=cost,
            priority_score=priority,
            max_daily_budget=total_budget,
        ))

    if not experiments:
        result.rationale = "No testable experiments found."
        return result

    # Sort by priority (descending)
    experiments.sort(key=lambda x: x.priority_score, reverse=True)

    # Allocate budget
    remaining = total_budget
    for exp in experiments:
        if remaining <= 0:
            break

        allocation = min(exp.cost_of_test, remaining, exp.max_daily_budget)
        if allocation >= min_allocation or exp.cost_of_test == 0:
            result.allocations.append({
                "candidate_id": exp.candidate.candidate_id,
                "product": exp.candidate.product_family,
                "test_type": exp.candidate.recommended_next_test.value,
                "budget": allocation,
                "expected_information_gain": exp.expected_information_gain,
                "expected_upside": exp.expected_economic_upside,
                "priority_score": exp.priority_score,
            })
            remaining -= allocation

    result.unallocated = remaining
    if result.allocations:
        top = result.allocations[0]
        result.rationale = (
            f"Top allocation: {top['product']} (${top['budget']:.2f}/day). "
            f"Priority score: {top['priority_score']:.2f}. "
            f"Information gain: {top['expected_information_gain']:.2f}. "
            f"Expected upside: ${top['expected_upside']:.2f}/mo."
        )
    else:
        result.rationale = "Could not allocate budget to any candidate."

    return result
