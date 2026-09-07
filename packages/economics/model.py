"""
Economic Model for Dropshipping Opportunity Assessment
Core calculations: landed_cost, pre_ad_contribution, break_even_cvr, headroom
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class CostStructure:
    """All cost inputs with provenance."""
    supplier_price: float
    supplier_shipping: float
    duties: float = 0.0
    payment_fee_rate: float = 0.029
    payment_fee_fixed: float = 0.20
    expected_returns_rate: float = 0.05
    selling_price: float = 0.0
    currency: str = "USD"

    # Confidence tracking for each input
    supplier_price_confidence: str = "MEDIUM"
    supplier_price_source: str = ""
    supplier_price_timestamp: str = ""
    supplier_price_sample_size: int = 0


@dataclass
class TrafficEstimate:
    """CPC and CVR estimates with confidence."""
    expected_cpc: float = 0.0
    cpc_source: str = ""
    cpc_confidence: str = "LOW"
    cpc_timestamp: str = ""
    cpc_sample_size: int = 0

    cvr_pessimistic: float = 0.002
    cvr_base: float = 0.005
    cvr_optimistic: float = 0.01
    cvr_confidence: str = "LOW"
    cvr_source: str = ""
    cvr_timestamp: str = ""


@dataclass
class EconomicResult:
    """Complete economic model output."""
    # Cost components
    landed_cost: float = 0.0
    payment_fees: float = 0.0
    expected_refunds: float = 0.0
    pre_ad_contribution: float = 0.0

    # Break-even
    break_even_cvr: float = 0.0
    break_even_cpc: float = 0.0

    # Per-scenario outcomes
    profit_per_click_pessimistic: float = 0.0
    profit_per_click_base: float = 0.0
    profit_per_click_optimistic: float = 0.0

    # Economic headroom (the key metric)
    headroom_pessimistic: float = 0.0
    headroom_base: float = 0.0
    headroom_optimistic: float = 0.0

    # Overall assessment
    economic_quality: str = ""  # STRUCTURALLY LOSING, FRAGILE, MARGINAL, INTERESTING, VERY INTERESTING, EXCEPTIONAL
    max_allowed_cpc: float = 0.0  # At base CVR, what's the highest CPC that still works?

    # Provenance
    computed_at: str = ""
    assumptions: dict = field(default_factory=dict)


def calculate_economics(
    selling_price: float,
    supplier_price: float,
    supplier_shipping: float,
    duties: float = 0.0,
    payment_fee_rate: float = 0.029,
    payment_fee_fixed: float = 0.20,
    expected_returns_rate: float = 0.05,
    expected_cpc: float = 1.0,
    cvr_pessimistic: float = 0.002,
    cvr_base: float = 0.005,
    cvr_optimistic: float = 0.01,
    currency: str = "USD",
) -> EconomicResult:
    """
    Calculate complete economic model for a candidate.
    All inputs are PRODUCT x COUNTRY x SUPPLIER level.
    """
    result = EconomicResult()

    # --- Landed cost ---
    result.landed_cost = supplier_price + supplier_shipping + duties

    # --- Payment fees ---
    result.payment_fees = (selling_price * payment_fee_rate) + payment_fee_fixed

    # --- Expected refunds ---
    result.expected_refunds = selling_price * expected_returns_rate

    # --- Pre-ad contribution ---
    result.pre_ad_contribution = (
        selling_price - result.landed_cost - result.payment_fees - result.expected_refunds
    )

    # --- Break-even CVR ---
    # At what CVR does profit_per_click = 0?
    # (cvr * contribution) - cpc = 0  =>  cvr = cpc / contribution
    if result.pre_ad_contribution > 0 and expected_cpc > 0:
        result.break_even_cvr = expected_cpc / result.pre_ad_contribution
    elif expected_cpc == 0:
        result.break_even_cvr = 0.0
    else:
        result.break_even_cvr = float('inf')

    # --- Break-even CPC ---
    # At what CPC does profit_per_click = 0?
    # (cvr * contribution) - cpc = 0  =>  cpc = cvr * contribution
    if result.pre_ad_contribution > 0:
        result.break_even_cpc = cvr_base * result.pre_ad_contribution
    else:
        result.break_even_cpc = 0.0

    # --- Per-scenario profit per click ---
    # profit_per_click = (cvr * pre_ad_contribution) - cpc
    result.profit_per_click_pessimistic = (cvr_pessimistic * result.pre_ad_contribution) - expected_cpc
    result.profit_per_click_base = (cvr_base * result.pre_ad_contribution) - expected_cpc
    result.profit_per_click_optimistic = (cvr_optimistic * result.pre_ad_contribution) - expected_cpc

    # --- Economic headroom ---
    # headroom = (cvr * contribution) / cpc
    # < 1.0: structurally losing, 1.0-1.20: extremely fragile, 1.20-1.50: marginal,
    # 1.50-2.00: interesting, 2.00+: very interesting, 3.00+: exceptional
    if expected_cpc > 0:
        result.headroom_pessimistic = (cvr_pessimistic * result.pre_ad_contribution) / expected_cpc
        result.headroom_base = (cvr_base * result.pre_ad_contribution) / expected_cpc
        result.headroom_optimistic = (cvr_optimistic * result.pre_ad_contribution) / expected_cpc
    else:
        result.headroom_pessimistic = float('inf')
        result.headroom_base = float('inf')
        result.headroom_optimistic = float('inf')

    # --- Economic quality band ---
    # Use base scenario for classification
    h = result.headroom_base
    if result.pre_ad_contribution <= 0:
        result.economic_quality = "STRUCTURALLY LOSING"
    elif h < 1.0:
        result.economic_quality = "STRUCTURALLY LOSING"
    elif h < 1.20:
        result.economic_quality = "EXTREMELY FRAGILE"
    elif h < 1.50:
        result.economic_quality = "MARGINAL"
    elif h < 2.00:
        result.economic_quality = "INTERESTING"
    elif h < 3.00:
        result.economic_quality = "VERY INTERESTING"
    else:
        result.economic_quality = "EXCEPTIONAL"

    # --- Max allowed CPC ---
    # At base CVR, what CPC keeps us at break-even?
    result.max_allowed_cpc = cvr_base * result.pre_ad_contribution if result.pre_ad_contribution > 0 else 0.0

    # --- Assumptions record ---
    result.computed_at = datetime.utcnow().isoformat()
    result.assumptions = {
        "selling_price": selling_price,
        "supplier_price": supplier_price,
        "supplier_shipping": supplier_shipping,
        "duties": duties,
        "payment_fee_rate": payment_fee_rate,
        "payment_fee_fixed": payment_fee_fixed,
        "expected_returns_rate": expected_returns_rate,
        "expected_cpc": expected_cpc,
        "cvr_pessimistic": cvr_pessimistic,
        "cvr_base": cvr_base,
        "cvr_optimistic": cvr_optimistic,
        "currency": currency,
    }

    return result
