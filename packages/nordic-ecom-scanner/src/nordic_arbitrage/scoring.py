from __future__ import annotations

import math
from dataclasses import dataclass

from .config import CountryProfile
from .economics import Economics
from .models import Candidate
from .compliance import compliance_flags


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


@dataclass(frozen=True)
class ScoreBreakdown:
    total: float
    economics: float
    demand: float
    competition: float
    merchandising: float
    basket: float
    localization: float
    operations: float
    gate: str
    reason: str


def score_candidate(c: Candidate, e: Economics, country: CountryProfile) -> ScoreBreakdown:
    # Economics: 0..35. Reward contribution margin and a CVR safety buffer.
    margin_component = clamp((e.contribution_margin_after_ads + 0.05) / 0.35)
    if e.break_even_cvr > 0:
        cvr_buffer = clamp((c.assumed_cvr / e.break_even_cvr - 0.75) / 1.5)
    else:
        cvr_buffer = 0.5
    economics = 35.0 * (0.7 * margin_component + 0.3 * cvr_buffer)

    # Demand: 0..15. A log curve prevents huge keywords dominating.
    demand = 15.0 * clamp(math.log10(max(c.monthly_searches, 1)) / 5.0)

    # Competition: 0..15. Lower merchant count and lower dominance are better.
    merchant_component = 1.0 - clamp(c.merchant_count / 40.0)
    dominance_component = 1.0 - clamp(c.dominant_merchant_share)
    competition = 15.0 * (0.65 * merchant_component + 0.35 * dominance_component)

    merchandising = 10.0 * clamp((c.creative_gap + c.title_gap) / 2.0)
    basket = 10.0 * clamp((c.b2b_multiplier + c.bundle_multiplier) / 2.0)

    payment_score = 1.0 if c.has_local_payment else 0.2
    return_score = 1.0 if c.has_local_return_address else 0.45
    localization = 10.0 * clamp(
        0.5 * country.localization_moat + 0.3 * payment_score + 0.2 * return_score
    )

    delivery_penalty = clamp(
        (c.estimated_delivery_days - country.target_delivery_days)
        / max(country.max_acceptable_delivery_days - country.target_delivery_days, 1)
    )
    product_risk = clamp((c.regulated_risk + c.fragility_risk + c.bulky_risk) / 3.0)
    operations = 5.0 * (1.0 - clamp(0.55 * delivery_penalty + 0.45 * product_risk))

    total = economics + demand + competition + merchandising + basket + localization + operations

    gate = "TEST"
    reasons: list[str] = []
    if e.pre_ad_contribution_local <= 0:
        gate = "REJECT"
        reasons.append("negative pre-ad contribution")
    if e.contribution_after_ads_local < 0:
        gate = "RESEARCH" if gate != "REJECT" else gate
        reasons.append("negative contribution at current CPC/CVR assumptions")
    if e.break_even_cvr > 0.04:
        gate = "RESEARCH" if gate != "REJECT" else gate
        reasons.append("requires >4% break-even CVR")
    flags = compliance_flags(c)
    product_compliance = [f for f in flags if f.startswith("manual compliance review:") or f.startswith("verify electrical/battery")]
    if c.regulated_risk >= 0.75 or product_compliance:
        if gate != "REJECT":
            gate = "COMPLIANCE_REVIEW"
        if c.regulated_risk >= 0.75:
            reasons.append("high regulatory/product-safety risk")
        if product_compliance:
            reasons.append("product category requires manual compliance evidence")
    match = (c.match_quality or "").lower()
    supplier_match_verified = ("verified" in match or "exact" in match) and "near" not in match
    if not supplier_match_verified:
        gate = "RESEARCH" if gate == "TEST" else gate
        reasons.append("supplier match/delivered quote not yet verified")
    if c.estimated_delivery_days > country.max_acceptable_delivery_days:
        gate = "RESEARCH" if gate == "TEST" else gate
        reasons.append("delivery too slow for market profile")
    if not c.has_local_payment and country.code in {"NO", "DK", "SE"}:
        gate = "RESEARCH" if gate == "TEST" else gate
        reasons.append("missing preferred local payment method")

    return ScoreBreakdown(
        total=round(total, 2), economics=round(economics, 2), demand=round(demand, 2),
        competition=round(competition, 2), merchandising=round(merchandising, 2),
        basket=round(basket, 2), localization=round(localization, 2), operations=round(operations, 2),
        gate=gate, reason="; ".join(reasons) if reasons else "passes current screening gates",
    )
