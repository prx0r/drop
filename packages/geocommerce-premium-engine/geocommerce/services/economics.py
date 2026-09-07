from __future__ import annotations
from math import log10
from ..models import EconomicsInput, ProductFacts, MarketConfig, MarketSignal, SupplierOffer, OpportunityScore
from .trade import estimated_duty_rate, requires_import_clearance

def compute_economics(inp: EconomicsInput) -> dict[str, float]:
    net_revenue = inp.price_gross / (1 + inp.vat_rate)
    duty = inp.supplier_cost * inp.duty_rate
    payment_fee = inp.price_gross * inp.payment_fee_rate
    return_reserve = inp.price_gross * inp.return_reserve_rate
    warranty_reserve = inp.price_gross * inp.warranty_reserve_rate
    variable_cost = inp.supplier_cost + inp.shipping_cost + duty + payment_fee + return_reserve + warranty_reserve
    contribution = net_revenue - variable_cost
    contribution_margin_net = contribution / net_revenue if net_revenue > 0 else -1
    break_even_cpc = max(0.0, contribution * inp.conservative_cvr)
    cpc_headroom = break_even_cpc / inp.avg_cpc if inp.avg_cpc > 0 else 0
    break_even_roas_gross = inp.price_gross / contribution if contribution > 0 else 999
    return {
        "net_revenue": round(net_revenue, 2),
        "duty": round(duty, 2),
        "payment_fee": round(payment_fee, 2),
        "return_reserve": round(return_reserve, 2),
        "warranty_reserve": round(warranty_reserve, 2),
        "variable_cost": round(variable_cost, 2),
        "contribution": round(contribution, 2),
        "contribution_margin_net": round(contribution_margin_net, 4),
        "break_even_cpc": round(break_even_cpc, 2),
        "cpc_headroom": round(cpc_headroom, 2),
        "break_even_roas_gross": round(break_even_roas_gross, 2),
    }

def _clamp(x: float, lo=0.0, hi=100.0) -> float:
    return max(lo, min(hi, x))

def _checkout_mode(price: float, market: MarketConfig) -> str:
    if price <= market.direct_checkout_ceiling:
        return "direct"
    if price <= market.assisted_checkout_ceiling:
        return "assisted"
    return "quote"

def score_opportunity(product_slug: str, facts: ProductFacts, market: MarketConfig, signal: MarketSignal, offer: SupplierOffer) -> OpportunityScore:
    price = signal.benchmark_price_gross * 0.97
    conservative_cvr = 0.012
    if facts.advisor_fit >= 0.75:
        conservative_cvr += 0.003
    if market.checkout_sensitivity > 0.7:
        conservative_cvr -= 0.001
    return_reserve_rate = 0.03 + facts.return_risk * 0.09 + facts.sizing_complexity * 0.04
    warranty_rate = 0.01 + (0.03 if facts.electrical else 0.01)
    econ_in = EconomicsInput(
        price_gross=price,
        supplier_cost=offer.unit_cost,
        shipping_cost=offer.shipping_cost,
        vat_rate=market.vat_rate,
        duty_rate=estimated_duty_rate(offer.ship_from_country, market.code, market.duty_rate_default, offer.landed_cost_includes_duties),
        return_reserve_rate=min(return_reserve_rate, 0.25),
        warranty_reserve_rate=warranty_rate,
        conservative_cvr=max(0.006, conservative_cvr),
        avg_cpc=max(signal.avg_cpc, 0.01),
    )
    econ = compute_economics(econ_in)
    gates: list[str] = []
    reasons: list[str] = []
    if signal.currency != market.currency or offer.currency != market.currency:
        gates.append("currency_not_normalized")
    if facts.regulated or facts.medical_claims or facts.child_safety_critical:
        gates.append("regulated_or_high_liability")
    if facts.electrical and not facts.electrical_certified:
        gates.append("electrical_certification_missing")
    if not facts.brand_authorized:
        gates.append("brand_authorization_missing")
    if offer.shipping_days > 21:
        gates.append("shipping_too_slow")
    if requires_import_clearance(offer.ship_from_country, market.code) and not offer.taxes_prepaid:
        gates.append("premium_import_not_prepaid")
    if econ["contribution"] <= 0:
        gates.append("negative_contribution")
    if econ["contribution_margin_net"] < 0.28:
        gates.append("thin_contribution_margin")

    demand = _clamp(log10(signal.avg_monthly_searches + 1) / 4.2 * 100)
    auction = _clamp((econ["cpc_headroom"] - 0.7) / 2.3 * 100)
    competition = _clamp(100 - signal.competition_index)
    supplier = _clamp((facts.supplier_quality * 0.55 + offer.reliability * 0.45) * 100)
    logistics = _clamp(100 - max(0, offer.shipping_days - 3) * 5 - (15 if facts.fragile else 0) + (5 if offer.local_return_address else 0))
    consultative = facts.advisor_fit * 100
    visual = facts.visual_demo_fit * 100
    market_fit = (market.cross_border_acceptance * 0.55 + market.localization_friction * 0.45) * 100
    returns = (1 - facts.return_risk) * 100

    aov_bonus = 100 if 250 <= price <= 2500 else 75 if 100 <= price < 250 else 80 if 2500 < price <= 5000 else 55
    score = (
        0.28 * auction + 0.14 * demand + 0.08 * competition + 0.10 * supplier +
        0.08 * logistics + 0.10 * consultative + 0.05 * visual + 0.05 * market_fit +
        0.04 * returns + 0.08 * aov_bonus
    )
    if econ["cpc_headroom"] >= 2.0:
        reasons.append("strong_cpc_headroom")
    if facts.advisor_fit >= 0.75:
        reasons.append("advice_can_add_conversion_value")
    if facts.visual_demo_fit >= 0.75:
        reasons.append("strong_ai_media_fit")
    if market.localization_friction >= 0.7:
        reasons.append("localization_may_create_defensible_surface_area")
    if offer.shipping_days <= 7:
        reasons.append("acceptable_cross_border_delivery")
    if gates:
        verdict = "REJECT"
        score = min(score, 35)
    elif econ["cpc_headroom"] >= 2.3 and score >= 78:
        verdict = "PAID_TEST"
    elif econ["cpc_headroom"] >= 1.5 and score >= 65:
        verdict = "FREE_LISTING_TEST"
    elif score >= 55:
        verdict = "WATCH"
    else:
        verdict = "REJECT"
    return OpportunityScore(
        product_slug=product_slug, market_code=market.code, score=round(score, 1), verdict=verdict,
        checkout_mode=_checkout_mode(price, market), economics=econ,
        components={
            "demand": round(demand,1), "auction": round(auction,1), "competition": round(competition,1),
            "supplier": round(supplier,1), "logistics": round(logistics,1), "consultative": round(consultative,1),
            "visual": round(visual,1), "market_fit": round(market_fit,1), "returns": round(returns,1), "aov": aov_bonus,
        }, gates=gates, reasons=reasons
    )
