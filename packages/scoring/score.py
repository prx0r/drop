"""
Soft Scoring — 0-100 transparent score with weights.
Hard gates and soft scoring are SEPARATE.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from packages.schemas.candidate import Candidate, ConfidenceLevel


@dataclass
class ScoreComponent:
    """A single scoring component with reasons."""
    name: str
    weight: int
    raw_value: float  # 0-1 before weight
    weighted_value: float  # raw * weight
    reasons: List[str] = field(default_factory=list)


@dataclass
class ScoreReport:
    """Complete scoring breakdown."""
    components: List[ScoreComponent] = field(default_factory=list)
    raw_score: float = 0.0
    confidence_multiplier: float = 1.0
    adjusted_score: float = 0.0
    overall_confidence: str = "LOW"
    overall_reasons: List[str] = field(default_factory=list)


# Default weights — transparent and configurable
WEIGHTS = {
    "ECONOMICS": 35,
    "QUERY_PURCHASE_INTENT": 15,
    "EXACT_SKU_COMPETITION": 15,
    "SUPPLIER_FULFILLMENT": 15,
    "DEMAND_TREND": 10,
    "MERCHANT_DIFFERENTIATION": 10,
}

CONFIDENCE_MULTIPLIERS = {
    "HIGH": 1.00,
    "MEDIUM": 0.85,
    "LOW": 0.65,
    "VERY_LOW": 0.40,
}


def _score_economics(c: Candidate) -> ScoreComponent:
    """Score economic viability (35 points)."""
    reasons = []
    h = c.headroom_base

    # Map headroom to 0-1 score
    if c.pre_ad_contribution <= 0:
        raw = 0.0
        reasons.append("Negative contribution")
    elif h < 1.0:
        raw = 0.0
        reasons.append(f"Headroom {h:.2f} < 1.0 (structurally losing)")
    elif h < 1.20:
        raw = 0.2
        reasons.append(f"Headroom {h:.2f} (extremely fragile)")
    elif h < 1.50:
        raw = 0.5
        reasons.append(f"Headroom {h:.2f} (marginal)")
    elif h < 2.00:
        raw = 0.7
        reasons.append(f"Headroom {h:.2f} (interesting)")
    elif h < 3.00:
        raw = 0.85
        reasons.append(f"Headroom {h:.2f} (very interesting)")
    else:
        raw = 1.0
        reasons.append(f"Headroom {h:.2f} (exceptional)")

    # Bonus for high contribution absolute value
    if c.pre_ad_contribution > 200:
        raw = min(1.0, raw + 0.1)
        reasons.append(f"High contribution ${c.pre_ad_contribution:.0f}")

    # Penalty for negative profit per click
    if c.profit_per_click_base if hasattr(c, 'profit_per_click_base') else (c.cvr_base * c.pre_ad_contribution - c.expected_cpc) < 0:
        raw = max(0.0, raw - 0.15)
        reasons.append("Negative expected profit per click (base)")

    weight = WEIGHTS["ECONOMICS"]
    return ScoreComponent("ECONOMICS", weight, raw, raw * weight, reasons)


def _score_query_intent(c: Candidate) -> ScoreComponent:
    """Score query purchase intent (15 points)."""
    reasons = []
    raw = c.intent_score  # Already 0-1

    if raw >= 0.8:
        reasons.append(f"High intent ({raw:.2f}) — likely exact model/brand search")
    elif raw >= 0.6:
        reasons.append(f"Moderate-high intent ({raw:.2f})")
    elif raw >= 0.4:
        reasons.append(f"Moderate intent ({raw:.2f})")
    else:
        reasons.append(f"Low intent ({raw:.2f}) — may be informational")

    if c.exact_query_share > 0.5:
        raw = min(1.0, raw + 0.15)
        reasons.append(f"High exact query share ({c.exact_query_share:.0%})")

    weight = WEIGHTS["QUERY_PURCHASE_INTENT"]
    return ScoreComponent("QUERY_PURCHASE_INTENT", weight, raw, raw * weight, reasons)


def _score_sku_competition(c: Candidate) -> ScoreComponent:
    """Score exact SKU competition (15 points)."""
    reasons = []

    # Fewer sellers is better
    if c.shopping_seller_count == 0:
        raw = 0.9
        reasons.append("No known Shopping sellers (blue ocean)")
    elif c.shopping_seller_count <= 3:
        raw = 0.8
        reasons.append(f"Low seller count ({c.shopping_seller_count})")
    elif c.shopping_seller_count <= 8:
        raw = 0.6
        reasons.append(f"Moderate seller count ({c.shopping_seller_count})")
    elif c.shopping_seller_count <= 15:
        raw = 0.3
        reasons.append(f"High seller count ({c.shopping_seller_count})")
    else:
        raw = 0.1
        reasons.append(f"Very high seller count ({c.shopping_seller_count})")

    # Amazon presence penalty
    if c.amazon_presence:
        raw = max(0.0, raw - 0.2)
        reasons.append("Amazon presence — price ceiling pressure")

    # Manufacturer DTC penalty
    if c.manufacturer_dtc:
        raw = max(0.0, raw - 0.1)
        reasons.append("Manufacturer sells DTC — harder to compete")

    # Price percentile (higher = more expensive relative to market = harder)
    if c.price_percentile > 0.8:
        raw = max(0.0, raw - 0.1)
        reasons.append(f"Price at {c.price_percentile:.0%} of market (expensive)")

    weight = WEIGHTS["EXACT_SKU_COMPETITION"]
    return ScoreComponent("EXACT_SKU_COMPETITION", weight, raw, raw * weight, reasons)


def _score_supplier(c: Candidate) -> ScoreComponent:
    """Score supplier/fulfillment (15 points)."""
    reasons = []
    raw = c.supplier_reliability  # 0-1

    if raw >= 0.8:
        reasons.append(f"High supplier reliability ({raw:.2f})")
    elif raw >= 0.5:
        reasons.append(f"Moderate supplier reliability ({raw:.2f})")
    else:
        reasons.append(f"Low supplier reliability ({raw:.2f})")

    # Shipping speed bonus
    if c.shipping_days <= 7:
        raw = min(1.0, raw + 0.15)
        reasons.append(f"Fast shipping ({c.shipping_days} days)")
    elif c.shipping_days <= 14:
        reasons.append(f"Acceptable shipping ({c.shipping_days} days)")
    else:
        raw = max(0.0, raw - 0.15)
        reasons.append(f"Slow shipping ({c.shipping_days} days)")

    # Selectivity bonus
    if c.supplier_selectivity == "selective":
        raw = min(1.0, raw + 0.1)
        reasons.append("Selective supplier (less competition)")
    elif c.supplier_selectivity == "open":
        raw = max(0.0, raw - 0.05)
        reasons.append("Open supplier (more competition)")

    weight = WEIGHTS["SUPPLIER_FULFILLMENT"]
    return ScoreComponent("SUPPLIER_FULFILLMENT", weight, raw, raw * weight, reasons)


def _score_demand(c: Candidate) -> ScoreComponent:
    """Score demand/trend (10 points)."""
    reasons = []

    # Search volume score
    vol = c.monthly_search_volume
    if vol >= 10000:
        vol_score = 1.0
        reasons.append(f"High search volume ({vol:,}/mo)")
    elif vol >= 5000:
        vol_score = 0.8
        reasons.append(f"Good search volume ({vol:,}/mo)")
    elif vol >= 1000:
        vol_score = 0.6
        reasons.append(f"Moderate search volume ({vol:,}/mo)")
    elif vol >= 100:
        vol_score = 0.3
        reasons.append(f"Low search volume ({vol:,}/mo)")
    else:
        vol_score = 0.1
        reasons.append(f"Very low search volume ({vol:,}/mo)")

    # Trend adjustment
    trend_bonus = 0.0
    if c.trend_3m > 0.3:
        trend_bonus = 0.15
        reasons.append(f"Strong upward trend (+{c.trend_3m:.0%} 3m)")
    elif c.trend_3m > 0.1:
        trend_bonus = 0.05
        reasons.append(f"Slight upward trend (+{c.trend_3m:.0%} 3m)")
    elif c.trend_3m < -0.3:
        trend_bonus = -0.15
        reasons.append(f"Declining trend ({c.trend_3m:.0%} 3m)")
    elif c.trend_3m < -0.1:
        trend_bonus = -0.05
        reasons.append(f"Slight decline ({c.trend_3m:.0%} 3m)")

    raw = max(0.0, min(1.0, vol_score + trend_bonus))
    weight = WEIGHTS["DEMAND_TREND"]
    return ScoreComponent("DEMAND_TREND", weight, raw, raw * weight, reasons)


def _score_merchant_differentiation(c: Candidate) -> ScoreComponent:
    """Score merchant differentiation (10 points)."""
    reasons = []
    raw = c.merchant_differentiation_score  # 0-1

    if raw >= 0.7:
        reasons.append(f"Strong differentiation ({raw:.2f})")
    elif raw >= 0.4:
        reasons.append(f"Moderate differentiation ({raw:.2f})")
    else:
        reasons.append(f"Low differentiation ({raw:.2f}) — commodity product")

    weight = WEIGHTS["MERCHANT_DIFFERENTIATION"]
    return ScoreComponent("MERCHANT_DIFFERENTIATION", weight, raw, raw * weight, reasons)


def score_candidate(c: Candidate) -> ScoreReport:
    """Score a candidate 0-100 with transparent breakdown."""
    report = ScoreReport()

    # Calculate each component
    report.components = [
        _score_economics(c),
        _score_query_intent(c),
        _score_sku_competition(c),
        _score_supplier(c),
        _score_demand(c),
        _score_merchant_differentiation(c),
    ]

    # Raw score = sum of weighted values
    report.raw_score = sum(comp.weighted_value for comp in report.components)

    # Confidence multiplier
    confidences = [
        c.economics_confidence,
        c.cpc_confidence_domain,
        c.cvr_confidence,
        c.supplier_confidence,
        c.competition_confidence,
        c.demand_confidence,
    ]

    # Use worst confidence as overall
    conf_order = ["VERY_LOW", "LOW", "MEDIUM", "HIGH"]
    worst = "HIGH"
    for conf in confidences:
        conf_val = conf.value if hasattr(conf, 'value') else conf
        if conf_order.index(conf_val) < conf_order.index(worst):
            worst = conf_val

    report.overall_confidence = worst
    report.confidence_multiplier = CONFIDENCE_MULTIPLIERS.get(worst, 0.5)

    # Adjusted score
    report.adjusted_score = report.raw_score * report.confidence_multiplier

    # Overall reasons
    report.overall_reasons = []
    for comp in report.components:
        if comp.reasons:
            report.overall_reasons.append(f"{comp.name}: {comp.reasons[0]}")

    return report
