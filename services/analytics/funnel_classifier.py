"""
Funnel State Classifier — Evidence-based (not calendar-based) funnel diagnosis.
Uses Bayesian model for decisions, not 'wait 14 days' or '100 clicks then kill'.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from packages.scoring.bayesian import create_posterior, analyze_test_result


class FunnelState(str, Enum):
    NO_DELIVERY = "NO_DELIVERY"
    IMPRESSIONS_NO_CLICKS = "IMPRESSIONS_NO_CLICKS"
    CLICKS_NO_ATC = "CLICKS_NO_ATC"
    ATC_NO_CHECKOUT = "ATC_NO_CHECKOUT"
    CHECKOUT_NO_PURCHASE = "CHECKOUT_NO_PURCHASE"
    PURCHASE_UNPROFITABLE = "PURCHASE_UNPROFITABLE"
    PROFITABLE_SPARSE = "PROFITABLE_SPARSE"
    PROFITABLE_SCALABLE = "PROFITABLE_SCALABLE"
    TRACKING_ANOMALY = "TRACKING_ANOMALY"
    SUPPLIER_ANOMALY = "SUPPLIER_ANOMALY"


@dataclass
class FunnelMetrics:
    """Raw funnel metrics."""
    impressions: int = 0
    clicks: int = 0
    atc: int = 0  # add to cart
    checkout: int = 0
    purchases: int = 0
    revenue: float = 0.0
    ad_spend: float = 0.0
    contribution_profit: float = 0.0

    # Reference economics
    break_even_cvr: float = 0.05
    pre_ad_contribution: float = 0.0
    expected_cpc: float = 1.0


@dataclass
class FunnelDiagnosis:
    """Complete diagnosis with evidence-based reasoning."""
    state: FunnelState
    confidence: str  # HIGH, MEDIUM, LOW
    evidence_count: int = 0
    evidence_summary: str = ""

    # Bayesian analysis
    probability_viable: float = 0.0
    expected_orders_if_viable: float = 0.0
    surprising_zero_orders: bool = False

    # Diagnosis details
    likely_problem_class: str = ""
    recommended_action: str = ""
    explanation: str = ""

    # Comparison with known cases
    similar_cases: List[str] = field(default_factory=list)


def classify_funnel(metrics: FunnelMetrics) -> FunnelDiagnosis:
    """
    Classify funnel state based on evidence, not calendar time.
    Uses Bayesian reasoning for decisions.
    """
    diag = FunnelDiagnosis(state=FunnelState.NO_DELIVERY, confidence="LOW")

    # Count evidence points
    evidence = 0
    if metrics.impressions > 0: evidence += 1
    if metrics.clicks > 0: evidence += 1
    if metrics.atc > 0: evidence += 1
    if metrics.checkout > 0: evidence += 1
    if metrics.purchases > 0: evidence += 1
    diag.evidence_count = evidence

    # --- NO DELIVERY ---
    if metrics.impressions == 0:
        diag.state = FunnelState.NO_DELIVERY
        diag.confidence = "HIGH" if metrics.clicks == 0 else "MEDIUM"
        diag.likely_problem_class = "eligibility/feed/bids/demand"
        diag.recommended_action = "CHECK_FEED_STATUS, CHECK_MERCHANT_CENTER, CHECK_BIDS"
        diag.explanation = (
            "No impressions means Google isn't showing the product. "
            "This is a feed/eligibility/bid issue, not a product-market fit issue."
        )
        diag.similar_cases = ["May 2026 campaign: 1,0,3,2,0 impressions over 5 days"]
        return diag

    # --- IMPRESSIONS, NO CLICKS ---
    if metrics.clicks == 0 and metrics.impressions > 100:
        diag.state = FunnelState.IMPRESSIONS_NO_CLICKS
        diag.confidence = "HIGH" if metrics.impressions > 1000 else "MEDIUM"
        diag.likely_problem_class = "title/image/price/query-mismatch"
        ctr = 0
        diag.recommended_action = "FIX_TITLE, FIX_IMAGE, CHECK_PRICE_vs_COMPETITION, CHECK_QUERY_MATCH"
        diag.explanation = (
            f"Got {metrics.impressions:,} impressions but zero clicks. "
            f"CTR is 0%. Problem is in the ad presentation, not the landing page."
        )
        return diag

    # --- CLICKS, NO ATC ---
    if metrics.clicks > 0 and metrics.atc == 0:
        # How many clicks is enough evidence?
        # Use Bayesian: if break-even CVR is X, what's P(0 ATC)?
        if metrics.break_even_cvr > 0:
            p_zero = (1 - metrics.break_even_cvr) ** metrics.clicks
        else:
            p_zero = 1.0

        diag.state = FunnelState.CLICKS_NO_ATC
        diag.probability_viable = 1 - p_zero
        diag.surprising_zero_orders = p_zero < 0.05

        if metrics.clicks >= 148:
            # The $289 mask case: 148 clicks, 0 ATC
            diag.confidence = "HIGH"
            diag.likely_problem_class = "product-market-fit/trust/pricing/landing-page"
            diag.explanation = (
                f"{metrics.clicks} clicks, 0 ATC. "
                f"P(0 ATC | viable CVR={metrics.break_even_cvr:.1%}) = {p_zero:.1%}. "
                f"This is {'surprising — something is wrong' if p_zero < 0.1 else 'within normal variance'}. "
                f"Not a delivery problem. Not a Google problem. The product/offer/trust isn't working."
            )
            diag.recommended_action = "KILL or major landing page rewrite"
            diag.similar_cases = [
                "$289 mask: 86% impression share, 148 clicks, 0 ATC → economics impossible",
                "335 clicks zero sales at 0.5% viable CVR: 18.7% probability (within normal)",
            ]
        elif metrics.clicks >= 50:
            diag.confidence = "MEDIUM"
            diag.likely_problem_class = "product/offer/trust/landing-page"
            diag.explanation = (
                f"{metrics.clicks} clicks, 0 ATC. "
                f"P(0 ATC | viable CVR) = {p_zero:.1%}. "
                f"{'Suspicious' if p_zero < 0.1 else 'Too early to diagnose'}."
            )
            diag.recommended_action = "Continue collecting data OR inspect landing page"
        else:
            diag.confidence = "LOW"
            diag.explanation = (
                f"Only {metrics.clicks} clicks — insufficient evidence. "
                f"At {metrics.break_even_cvr:.1%} CVR, need ~{int(3/metrics.break_even_cvr)} clicks for 95% confidence."
            )
            diag.recommended_action = "CONTINUE — collect more data"

        return diag

    # --- ATC, NO CHECKOUT ---
    if metrics.atc > 0 and metrics.checkout == 0:
        diag.state = FunnelState.ATC_NO_CHECKOUT
        diag.confidence = "MEDIUM"
        diag.likely_problem_class = "offer/friction"
        diag.recommended_action = "CHECK_CHECKOUT_FLOW, CHECK_SHIPPING_COST, CHECK_TRUST_SIGNALS"
        diag.explanation = (
            f"{metrics.atc} add-to-carts but 0 checkouts. "
            f"Interest exists but friction prevents purchase progression."
        )
        diag.similar_cases = [
            "Lumbar pillow: 4 ATC, 1 checkout, 0 purchase → 12-15 day shipping on pain product"
        ]
        return diag

    # --- CHECKOUT, NO PURCHASE ---
    if metrics.checkout > 0 and metrics.purchases == 0:
        diag.state = FunnelState.CHECKOUT_NO_PURCHASE
        diag.confidence = "HIGH"
        diag.likely_problem_class = "shipping/payment/trust/price"
        diag.recommended_action = "CHECK_SHIPPING_TIME, CHECK_PAYMENT_OPTIONS, CHECK_CHECKOUT_FRICION"
        diag.explanation = (
            f"{metrics.checkout} checkouts but 0 purchases. "
            f"Customer was ready to buy but something stopped them at the final step."
        )
        diag.similar_cases = [
            "Lumbar pillow: 1 checkout, 0 purchase → 12-15 day stated shipping"
        ]
        return diag

    # --- PURCHASES ---
    if metrics.purchases > 0:
        # Is it profitable?
        if metrics.contribution_profit > 0:
            # Is it scalable or sparse?
            if metrics.purchases >= 3 and metrics.contribution_profit / max(1, metrics.ad_spend) > 0.5:
                diag.state = FunnelState.PROFITABLE_SCALABLE
                diag.confidence = "HIGH"
                diag.recommended_action = "SCALE — 20% budget increments"
                diag.explanation = (
                    f"{metrics.purchases} purchases, profitable. "
                    f"Contribution margin: ${metrics.contribution_profit:.2f}. "
                    f"Ready to scale gradually."
                )
            else:
                diag.state = FunnelState.PROFITABLE_SPARSE
                diag.confidence = "MEDIUM"
                diag.recommended_action = "CONTINUE — collect more data before scaling"
                diag.explanation = (
                    f"{metrics.purchases} purchases, profitable but sparse. "
                    f"Need more data to confirm this isn't variance."
                )
                diag.similar_cases = [
                    "Pitiful_Gene: days 1-4 dead, days 5-6 movement → not enough data to judge early"
                ]
        else:
            diag.state = FunnelState.PURCHASE_UNPROFITABLE
            diag.confidence = "HIGH"
            diag.recommended_action = "FIX_ECONOMICS or KILL"
            diag.explanation = (
                f"{metrics.purchases} purchases but contribution is negative (${metrics.contribution_profit:.2f}). "
                f"Unit economics don't work."
            )
        return diag

    # Fallback
    diag.state = FunnelState.NO_DELIVERY
    diag.explanation = "Insufficient data to classify"
    return diag


def explain_why_100_clicks_kill_is_wrong(
    clicks: int,
    viable_cvr: float,
) -> str:
    """
    Demonstrate why '100 clicks then kill' is often wrong.
    P(0 sales | viable CVR) at various click counts.
    """
    results = []
    for n in [50, 100, 150, 200, 300, 500]:
        p_zero = (1 - viable_cvr) ** n
        results.append(f"  {n} clicks: P(0 sales) = {p_zero:.1%}")

    return (
        f"At {viable_cvr:.1%} CVR, probability of zero sales:\n"
        + "\n".join(results)
        + f"\n\nSo at 100 clicks, there's a {(1-viable_cvr)**100:.0%} chance of zero sales "
        f"even if the product IS viable at {viable_cvr:.1%} CVR. "
        f"Killing at 100 clicks would discard {((1-viable_cvr)**100)*100:.0f}% of viable products."
    )
