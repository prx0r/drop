"""
Expected Value of Information (EVOI) — For every uncertain candidate,
find the cheapest next action that removes the largest uncertainty.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from packages.schemas.candidate import Candidate, TestType, ConfidenceLevel


@dataclass
class ActionCandidate:
    """A possible next action for a candidate."""
    action: TestType
    cost: float
    expected_uncertainty_reduction: float  # 0-1, how much uncertainty this removes
    information_value: float  # How valuable is this information?
    evoi: float  # Expected Value of Information = value * reduction / cost
    rationale: str = ""


# Cost estimates for each action
ACTION_COSTS = {
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


def estimate_uncertainty_reduction(candidate: Candidate, action: TestType) -> float:
    """Estimate how much uncertainty a given action removes."""
    reduction = 0.0

    if action == TestType.CHECK_SERP:
        # SERP check reveals: competition, pricing, market structure
        if candidate.competition_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.7
        else:
            reduction = 0.2

    elif action == TestType.CHECK_SUPPLIER:
        # Supplier check reveals: reliability, stock, authorization
        if candidate.supplier_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.8
        else:
            reduction = 0.2

    elif action == TestType.GET_SHIPPING_QUOTE:
        # Shipping quote reveals: actual shipping cost and time
        if candidate.supplier_shipping == 0:
            reduction = 0.6
        else:
            reduction = 0.1

    elif action == TestType.FETCH_KEYWORD_DATA:
        # Keyword data reveals: search volume, CPC, competition
        if candidate.demand_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.8
        else:
            reduction = 0.3

    elif action == TestType.FETCH_GTIN_SELLERS:
        # GTIN seller data reveals: SKU saturation
        if candidate.shopping_seller_count == 0:
            reduction = 0.9
        else:
            reduction = 0.2

    elif action == TestType.ENABLE_FREE_LISTING:
        # Free listing reveals: real demand, CTR, some conversion signal
        if candidate.demand_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.6
        else:
            reduction = 0.3

    elif action == TestType.RUN_FREE_TRAFFIC_TEST:
        # Free traffic test reveals: CVR signal at zero cost
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.8
        else:
            reduction = 0.3

    elif action == TestType.RUN_5_PAID_TEST:
        # $5 test reveals: CVR signal with cost
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.7
        else:
            reduction = 0.4

    elif action == TestType.RUN_10_PAID_TEST:
        # $10 test reveals: stronger CVR signal
        if candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]:
            reduction = 0.85
        else:
            reduction = 0.5

    return reduction


def estimate_information_value(candidate: Candidate, action: TestType) -> float:
    """Estimate how valuable the information from this action is."""
    value = 0.0

    # High value if this action resolves a hard gate blocker
    if action == TestType.CHECK_SUPPLIER:
        if candidate.supplier_reliability < 0.5:
            value = 0.9  # Could unblock a quarantined candidate
        else:
            value = 0.3

    elif action == TestType.FETCH_GTIN_SELLERS:
        if candidate.shopping_seller_count == 0:
            value = 0.8  # Could reveal saturation
        else:
            value = 0.3

    elif action == TestType.FETCH_KEYWORD_DATA:
        if candidate.monthly_search_volume == 0:
            value = 0.9  # Could reveal demand
        else:
            value = 0.4

    elif action in [TestType.RUN_FREE_TRAFFIC_TEST, TestType.RUN_5_PAID_TEST, TestType.RUN_10_PAID_TEST]:
        # CVR tests are most valuable when economics are good but CVR is unknown
        if (candidate.headroom_base >= 1.2 and
            candidate.cvr_confidence.value in ["VERY_LOW", "LOW"]):
            value = 0.95  # This is the make-or-break question
        elif candidate.headroom_base >= 1.0:
            value = 0.7
        else:
            value = 0.3  # Don't waste money testing bad economics

    elif action == TestType.ENABLE_FREE_LISTING:
        if candidate.state.value in ["BUILD_READY", "FREE_LISTINGS_LIVE"]:
            value = 0.8  # Free data is always valuable
        else:
            value = 0.4

    return value


def calculate_evoi(candidate: Candidate) -> List[ActionCandidate]:
    """
    Calculate Expected Value of Information for all possible actions.
    Returns actions ranked by EV/OI (value * reduction / cost).
    """
    actions = []

    for action in TestType:
        cost = ACTION_COSTS[action]
        reduction = estimate_uncertainty_reduction(candidate, action)
        value = estimate_information_value(candidate, action)

        # EV/OI = value * reduction / cost (handle zero cost)
        if cost > 0:
            evoi = (value * reduction) / cost
        else:
            evoi = value * reduction * 100  # Free tests get huge multiplier

        # Generate rationale
        rationale = _generate_rationale(candidate, action, reduction, value, cost)

        actions.append(ActionCandidate(
            action=action,
            cost=cost,
            expected_uncertainty_reduction=reduction,
            information_value=value,
            evoi=evoi,
            rationale=rationale,
        ))

    # Sort by EV/OI (descending)
    actions.sort(key=lambda x: x.evoi, reverse=True)

    return actions


def recommend_next_action(candidate: Candidate) -> ActionCandidate:
    """Recommend the single best next action for a candidate."""
    actions = calculate_evoi(candidate)
    if actions:
        return actions[0]
    return ActionCandidate(
        action=TestType.CHECK_SERP,
        cost=0.0,
        expected_uncertainty_reduction=0.5,
        information_value=0.5,
        evoi=50.0,
        rationale="Default: check SERP for market structure"
    )


def _generate_rationale(
    candidate: Candidate,
    action: TestType,
    reduction: float,
    value: float,
    cost: float,
) -> str:
    """Generate human-readable rationale for an action."""
    if action == TestType.CHECK_SERP:
        return (
            f"Check SERP for '{candidate.query}' in {candidate.country}. "
            f"Reveals: competition structure, pricing landscape, organic difficulty. "
            f"Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.CHECK_SUPPLIER:
        return (
            f"Validate supplier {candidate.supplier_id}. "
            f"Reveals: reliability, stock, authorization, shipping speed. "
            f"Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.GET_SHIPPING_QUOTE:
        return (
            f"Get actual shipping quote from {candidate.supplier_id} to {candidate.country}. "
            f"Reveals: true landed cost. Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.FETCH_KEYWORD_DATA:
        return (
            f"Fetch keyword data for '{candidate.query}'. "
            f"Reveals: search volume, CPC, competition index. "
            f"Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.FETCH_GTIN_SELLERS:
        return (
            f"Fetch GTIN seller count for {candidate.gtin or 'unknown'}. "
            f"Reveals: SKU saturation level. Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.ENABLE_FREE_LISTING:
        return (
            f"Enable Google free listing for {candidate.sku}. "
            f"Reveals: real demand, CTR, conversion signal at zero cost. "
            f"Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.RUN_FREE_TRAFFIC_TEST:
        return (
            f"Run free traffic test for {candidate.sku}. "
            f"Reveals: CVR signal without ad spend. "
            f"Cost: $0. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.RUN_5_PAID_TEST:
        return (
            f"Run $5/day paid test for {candidate.sku}. "
            f"Reveals: CVR signal with moderate spend. "
            f"Cost: $5/day. Uncertainty reduction: {reduction:.0%}."
        )
    elif action == TestType.RUN_10_PAID_TEST:
        return (
            f"Run $10/day paid test for {candidate.sku}. "
            f"Reveals: strong CVR signal. "
            f"Cost: $10/day. Uncertainty reduction: {reduction:.0%}."
        )
    return ""
