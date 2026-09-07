"""
Product Allocation Classifier — Classifies candidates into categories
based on economics, uncertainty, and observed evidence.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from enum import Enum
from packages.schemas.candidate import Candidate, ConfidenceLevel


class ProductClass(str, Enum):
    CHAMPION = "CHAMPION"
    POTENTIAL = "POTENTIAL"
    SLEEPER = "SLEEPER"
    WASTER = "WASTER"
    ZOMBIE = "ZOMBIE"


@dataclass
class ClassificationResult:
    product_class: ProductClass
    reasoning: List[str] = field(default_factory=list)
    confidence: str = "LOW"
    signals: dict = field(default_factory=dict)


def classify_product(c: Candidate) -> ClassificationResult:
    """
    Classify a candidate into CHAMPION / POTENTIAL / SLEEPER / WASTER / ZOMBIE.

    Uses: headroom_base, pre_ad_contribution, supplier_reliability,
    posterior data (observed_clicks, observed_orders, probability_cvr_above_break_even),
    and observed data (state, shopping_seller_count, etc.)
    """
    reasoning: List[str] = []
    signals: dict = {}

    # Gather signals
    headroom = c.headroom_base
    contribution = c.pre_ad_contribution
    supplier_rel = c.supplier_reliability
    p_above = c.probability_cvr_above_break_even
    clicks = c.observed_clicks
    orders = c.observed_orders
    seller_count = c.shopping_seller_count
    intent = c.intent_score
    confidence_fields = [
        c.economics_confidence, c.cpc_confidence_domain, c.cvr_confidence,
        c.supplier_confidence, c.competition_confidence, c.demand_confidence,
    ]

    signals["headroom_base"] = headroom
    signals["pre_ad_contribution"] = contribution
    signals["supplier_reliability"] = supplier_rel
    signals["posterior_p_above"] = p_above
    signals["observed_clicks"] = clicks
    signals["observed_orders"] = orders

    # ZOMBIE: structurally bad or supplier/market failure
    if contribution <= 0:
        reasoning.append(f"Negative contribution (${contribution:.2f}) — structurally losing")
        signals["rejection_reason"] = "negative_contribution"
        return ClassificationResult(ProductClass.ZOMBIE, reasoning, "HIGH", signals)

    if headroom < 1.0 and headroom != float('inf'):
        reasoning.append(f"Headroom {headroom:.2f} < 1.0 — every paid scenario loses money")
        signals["rejection_reason"] = "headroom_below_1"
        return ClassificationResult(ProductClass.ZOMBIE, reasoning, "HIGH", signals)

    if supplier_rel < 0.3:
        reasoning.append(f"Supplier reliability {supplier_rel:.2f} < 0.3 — fulfillment failure risk")
        signals["rejection_reason"] = "unreliable_supplier"
        return ClassificationResult(ProductClass.ZOMBIE, reasoning, "HIGH", signals)

    if seller_count > 20:
        reasoning.append(f"{seller_count} sellers — SKU is saturated, no room")
        signals["rejection_reason"] = "saturated_sku"
        return ClassificationResult(ProductClass.ZOMBIE, reasoning, "HIGH", signals)

    # WASTER: sufficient evidence of poor paid economics
    if headroom >= 1.0 and headroom < 1.2 and clicks >= 100 and orders == 0:
        reasoning.append(f"Headroom {headroom:.2f} is fragile, {clicks} clicks, 0 orders — paid not viable")
        signals["rejection_reason"] = "fragile_no_evidence"
        return ClassificationResult(ProductClass.WASTER, reasoning, "MEDIUM", signals)

    if p_above < 0.1 and clicks >= 200:
        reasoning.append(f"P(CVR > break_even) = {p_above:.1%} after {clicks} clicks — strong evidence against")
        signals["rejection_reason"] = "low_posterior_probability"
        return ClassificationResult(ProductClass.WASTER, reasoning, "HIGH", signals)

    # SLEEPER: economics attractive, little traffic
    if headroom >= 1.5 and clicks == 0 and contribution > 50:
        reasoning.append(f"Headroom {headroom:.2f} and ${contribution:.0f} contribution but zero observed traffic")
        reasoning.append("Could be a sleeper — needs traffic validation")
        return ClassificationResult(ProductClass.SLEEPER, reasoning, "LOW", signals)

    if headroom >= 1.5 and clicks < 30 and orders == 0 and contribution > 50:
        reasoning.append(f"Good headroom ({headroom:.2f}), strong contribution (${contribution:.0f}), but only {clicks} clicks")
        reasoning.append("Insufficient traffic data — could be sleeper")
        return ClassificationResult(ProductClass.SLEEPER, reasoning, "LOW", signals)

    # CHAMPION: strong posterior viability, positive contribution, healthy fulfillment
    is_posterior_strong = (
        (clicks == 0 and headroom >= 2.0 and contribution > 100 and supplier_rel >= 0.6) or
        (clicks > 0 and p_above >= 0.7) or
        (orders > 0 and contribution > 0)
    )

    if is_posterior_strong and contribution > 0 and supplier_rel >= 0.5 and headroom >= 1.5:
        reasoning.append(f"Headroom {headroom:.2f}, contribution ${contribution:.0f}, supplier {supplier_rel:.2f}")
        if clicks > 0:
            reasoning.append(f"Posterior: P(CVR > break_even) = {p_above:.1%}")
        if orders > 0:
            reasoning.append(f"{orders} observed orders — positive signal")
        return ClassificationResult(ProductClass.CHAMPION, reasoning, "HIGH", signals)

    # POTENTIAL: good economics, some positive signal, insufficient evidence
    if contribution > 0 and headroom >= 1.2:
        reasoning.append(f"Headroom {headroom:.2f}, contribution ${contribution:.0f}")
        if clicks > 0 and orders > 0:
            reasoning.append(f"Some positive signal: {orders} orders from {clicks} clicks")
        elif clicks == 0:
            reasoning.append("No traffic data yet — need free listing test")
        else:
            reasoning.append(f"{clicks} clicks, {orders} orders — insufficient evidence")
        return ClassificationResult(ProductClass.POTENTIAL, reasoning, "MEDIUM", signals)

    # Fallback: if contribution positive but headroom borderline
    if contribution > 0:
        reasoning.append(f"Marginal economics: headroom {headroom:.2f}, contribution ${contribution:.0f}")
        return ClassificationResult(ProductClass.POTENTIAL, reasoning, "LOW", signals)

    reasoning.append("Could not classify — falling through to ZOMBIE")
    return ClassificationResult(ProductClass.ZOMBIE, reasoning, "LOW", signals)
