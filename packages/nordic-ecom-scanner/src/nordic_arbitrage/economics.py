from __future__ import annotations

from dataclasses import dataclass

from .config import CountryProfile
from .models import Candidate


@dataclass(frozen=True)
class Economics:
    target_price_local: float
    expected_units_per_order: float
    order_revenue_local: float
    net_revenue_ex_vat: float
    landed_cost_local: float
    landed_cost_order_local: float
    payment_fee_local: float
    expected_returns_loss_local: float
    support_allowance_local: float
    pre_ad_contribution_local: float
    expected_cpa_local: float
    contribution_after_ads_local: float
    break_even_cvr: float
    break_even_roas: float
    expected_roas: float
    contribution_margin_after_ads: float


def calculate_economics(
    c: Candidate,
    country: CountryProfile,
    *,
    support_allowance_rate: float = 0.015,
    returns_recovery_rate: float = 0.65,
) -> Economics:
    unit_price = c.target_price_local or c.competitor_price_local * 0.92
    if not c.landed_cost_local or c.landed_cost_local <= 0:
        raise ValueError("landed_cost_local must be populated before economics can be calculated")

    units = max(float(c.expected_units_per_order or 1.0), 1.0)
    order_revenue = unit_price * units
    landed_order = c.landed_cost_local * units
    net_revenue = order_revenue / (1.0 + country.standard_vat_rate)
    payment_fee = order_revenue * country.default_payment_fee_rate
    # Only the unrecovered portion of a return is treated as economic loss here.
    returns_loss = order_revenue * c.expected_return_rate * (1.0 - returns_recovery_rate)
    support = order_revenue * support_allowance_rate
    pre_ad = net_revenue - landed_order - payment_fee - returns_loss - support

    if c.cpc_local > 0 and c.assumed_cvr > 0:
        expected_cpa = c.cpc_local / c.assumed_cvr
    else:
        expected_cpa = 0.0

    after_ads = pre_ad - expected_cpa
    break_even_cvr = (c.cpc_local / pre_ad) if c.cpc_local > 0 and pre_ad > 0 else 0.0
    break_even_roas = (order_revenue / pre_ad) if pre_ad > 0 else float("inf")
    expected_roas = (order_revenue / expected_cpa) if expected_cpa > 0 else float("inf")
    margin_after_ads = after_ads / order_revenue if order_revenue > 0 else -1.0

    return Economics(
        target_price_local=round(unit_price, 2),
        expected_units_per_order=round(units, 2),
        order_revenue_local=round(order_revenue, 2),
        net_revenue_ex_vat=round(net_revenue, 2),
        landed_cost_local=round(c.landed_cost_local, 2),
        landed_cost_order_local=round(landed_order, 2),
        payment_fee_local=round(payment_fee, 2),
        expected_returns_loss_local=round(returns_loss, 2),
        support_allowance_local=round(support, 2),
        pre_ad_contribution_local=round(pre_ad, 2),
        expected_cpa_local=round(expected_cpa, 2),
        contribution_after_ads_local=round(after_ads, 2),
        break_even_cvr=round(break_even_cvr, 5),
        break_even_roas=round(break_even_roas, 3) if break_even_roas != float("inf") else break_even_roas,
        expected_roas=round(expected_roas, 3) if expected_roas != float("inf") else expected_roas,
        contribution_margin_after_ads=round(margin_after_ads, 4),
    )
