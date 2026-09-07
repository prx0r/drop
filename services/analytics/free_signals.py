"""
Free Listing Signal Score — Calculate free_signal_score from Google free listings
and Search Console data BEFORE paid ads.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from enum import Enum


class FreeSignalState(str, Enum):
    ZERO_IMPRESSIONS = "ZERO_IMPRESSIONS"
    IMPRESSIONS_NO_CLICKS = "IMPRESSIONS_NO_CLICKS"
    CLICKS_NO_ATC = "CLICKS_NO_ATC"
    CLICKS_WITH_ATC = "CLICKS_WITH_ATC"


@dataclass
class FreeListingData:
    free_impressions: int = 0
    free_clicks: int = 0
    product_views: int = 0
    atcs: int = 0
    orders: int = 0
    revenue: float = 0.0

    console_impressions: int = 0
    console_clicks: int = 0
    console_queries: int = 0
    console_avg_position: float = 0.0
    console_ctr: float = 0.0


@dataclass
class FreeSignalResult:
    free_signal_score: float = 0.0
    state: FreeSignalState = FreeSignalState.ZERO_IMPRESSIONS
    free_ctr: float = 0.0
    console_ctr: float = 0.0
    atc_rate: float = 0.0
    order_rate: float = 0.0
    query_quality_score: float = 0.0
    reasoning: List[str] = field(default_factory=list)
    details: dict = field(default_factory=dict)


def calculate_free_signal_score(data: FreeListingData) -> FreeSignalResult:
    """
    Calculate free_signal_score (0-1) from organic data.

    Scoring components:
    - free_impressions → feed quality / demand signal (20%)
    - free_ctr → title/image/price appeal (25%)
    - atc_rate → product/offer fit (30%)
    - query_quality → search console signals (15%)
    - conversion → actual purchase signal (10%)
    """
    result = FreeSignalResult()
    reasoning: List[str] = []

    # Calculate base metrics
    free_ctr = (data.free_clicks / data.free_impressions) if data.free_impressions > 0 else 0.0
    atc_rate = (data.atcs / data.free_clicks) if data.free_clicks > 0 else 0.0
    order_rate = (data.orders / data.free_clicks) if data.free_clicks > 0 else 0.0
    console_ctr = data.console_ctr if data.console_ctr > 0 else (
        (data.console_clicks / data.console_impressions) if data.console_impressions > 0 else 0.0
    )

    result.free_ctr = free_ctr
    result.console_ctr = console_ctr
    result.atc_rate = atc_rate
    result.order_rate = order_rate

    # Determine free signal state
    if data.free_impressions == 0 and data.console_impressions == 0:
        result.state = FreeSignalState.ZERO_IMPRESSIONS
        reasoning.append("No organic impressions — feed/eligibility/demand issue")
    elif data.free_clicks == 0 and data.free_impressions > 100:
        result.state = FreeSignalState.IMPRESSIONS_NO_CLICKS
        reasoning.append(f"{data.free_impressions:,} impressions but 0 clicks — title/image/price problem")
    elif data.free_clicks > 0 and data.atcs == 0:
        result.state = FreeSignalState.CLICKS_NO_ATC
        reasoning.append(f"{data.free_clicks} clicks, 0 ATC — offer/product/trust problem")
    else:
        result.state = FreeSignalState.CLICKS_WITH_ATC
        if data.atcs > 0:
            reasoning.append(f"{data.free_clicks} clicks, {data.atcs} ATC — promising signal")

    # Component 1: Impression volume (0-1, 20% weight)
    if data.free_impressions >= 10000:
        impression_score = 1.0
        reasoning.append(f"High organic impressions ({data.free_impressions:,})")
    elif data.free_impressions >= 1000:
        impression_score = 0.7
        reasoning.append(f"Moderate organic impressions ({data.free_impressions:,})")
    elif data.free_impressions >= 100:
        impression_score = 0.3
        reasoning.append(f"Low organic impressions ({data.free_impressions:,})")
    else:
        impression_score = 0.0

    # Component 2: Free CTR (0-1, 25% weight)
    if free_ctr >= 0.05:
        ctr_score = 1.0
        reasoning.append(f"Strong free CTR ({free_ctr:.1%})")
    elif free_ctr >= 0.02:
        ctr_score = 0.7
        reasoning.append(f"Decent free CTR ({free_ctr:.1%})")
    elif free_ctr >= 0.005:
        ctr_score = 0.4
        reasoning.append(f"Weak free CTR ({free_ctr:.1%})")
    else:
        ctr_score = 0.0

    # Component 3: ATC rate (0-1, 30% weight)
    if data.free_clicks > 0:
        if atc_rate >= 0.10:
            atc_score = 1.0
            reasoning.append(f"Strong ATC rate ({atc_rate:.1%})")
        elif atc_rate >= 0.05:
            atc_score = 0.7
            reasoning.append(f"Decent ATC rate ({atc_rate:.1%})")
        elif atc_rate >= 0.02:
            atc_score = 0.4
            reasoning.append(f"Weak ATC rate ({atc_rate:.1%})")
        else:
            atc_score = 0.0
            if data.free_clicks >= 20:
                reasoning.append(f"Very low ATC rate ({atc_rate:.1%}) after {data.free_clicks} clicks")
    else:
        atc_score = 0.0

    # Component 4: Query quality from Search Console (0-1, 15% weight)
    if data.console_queries > 0:
        avg_clicks_per_query = data.console_clicks / data.console_queries
        if data.console_avg_position > 0 and data.console_avg_position <= 10:
            position_bonus = 0.3
        elif data.console_avg_position > 0 and data.console_avg_position <= 20:
            position_bonus = 0.15
        else:
            position_bonus = 0.0

        if console_ctr >= 0.05:
            query_quality = min(1.0, 0.7 + position_bonus)
        elif console_ctr >= 0.02:
            query_quality = min(1.0, 0.4 + position_bonus)
        else:
            query_quality = 0.2 + position_bonus

        result.query_quality_score = query_quality
        reasoning.append(f"Search Console: {data.console_queries} queries, avg position {data.console_avg_position:.1f}")
    else:
        query_quality = 0.0

    # Component 5: Conversion signal (0-1, 10% weight)
    if data.orders > 0:
        conversion_score = min(1.0, order_rate / 0.05)  # 5% order rate = perfect
        reasoning.append(f"Organic orders detected: {data.orders} (order rate {order_rate:.1%})")
    elif data.atcs > 0:
        conversion_score = 0.3  # ATC but no purchase
    else:
        conversion_score = 0.0

    # Weighted combination
    result.free_signal_score = (
        impression_score * 0.20 +
        ctr_score * 0.25 +
        atc_score * 0.30 +
        query_quality * 0.15 +
        conversion_score * 0.10
    )

    result.details = {
        "impression_score": impression_score,
        "ctr_score": ctr_score,
        "atc_score": atc_score,
        "query_quality_score": query_quality,
        "conversion_score": conversion_score,
    }

    result.reasoning = reasoning
    return result


def should_start_paid_test(result: FreeSignalResult) -> bool:
    """Determine if free signal data supports starting a paid test."""
    if result.state == FreeSignalState.CLICKS_WITH_ATC:
        return True
    if result.state == FreeSignalState.IMPRESSIONS_NO_CLICKS:
        return False
    if result.free_signal_score >= 0.4:
        return True
    return False


def summarize_free_signals(results: List[FreeSignalResult]) -> dict:
    """Summarize free signal results across multiple products."""
    if not results:
        return {"total": 0, "avg_score": 0.0, "states": {}}

    total_score = sum(r.free_signal_score for r in results)
    states = {}
    for r in results:
        state = r.state.value
        states[state] = states.get(state, 0) + 1

    return {
        "total": len(results),
        "avg_score": total_score / len(results),
        "states": states,
        "ready_for_paid": sum(1 for r in results if should_start_paid_test(r)),
    }
