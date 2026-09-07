from __future__ import annotations

import math
from q4radar.models import ProductSeed, Market, ProductObservation, ScoreBreakdown


def clamp(v: float, lo: float = 0, hi: float = 100) -> float:
    return max(lo, min(hi, v))


def log_score(v: float | None, low: float = 100, high: float = 10000) -> float:
    if v is None or v <= 0:
        return 35.0
    x = (math.log10(max(v, low)) - math.log10(low)) / (math.log10(high)-math.log10(low))
    return clamp(x*100)


def momentum_score(v: float | None) -> float:
    if v is None:
        return 50
    return clamp((v + 50) / 150 * 100)


def competition_gap_score(obs: ProductObservation) -> float:
    vals = []
    if obs.keyword_competition is not None:
        vals.append((1-clamp(obs.keyword_competition,0,1))*100)
    if obs.competitor_count is not None:
        vals.append(clamp(100 - obs.competitor_count*1.7))
    if obs.ad_count is not None:
        a = obs.ad_count
        vals.append(clamp(100 - abs(a-15)*2.2))
    if obs.ad_longevity_days is not None:
        vals.append(clamp(obs.ad_longevity_days/90*100))
    return sum(vals)/len(vals) if vals else 50


def economics(product: ProductSeed, market: Market, obs: ProductObservation) -> dict[str, float | None]:
    """Conservative screening economics.

    Consumer competitor prices are treated as VAT/GST-inclusive where a market VAT/GST rate is
    configured. VAT is stripped from revenue before margin calculation. A configurable estimate
    of 2026 low-value import duty is added to landed cost. Payment and return reserves are then
    deducted to calculate a more realistic breakeven CAC.
    """
    retail_gross = obs.competitor_price_median_usd or sum(product.typical_retail_usd)/2
    net_revenue = retail_gross/(1+market.vat_rate) if market.vat_rate else retail_gross
    supplier = obs.supplier_price_median_usd or obs.supplier_price_low_usd or sum(product.target_supplier_usd)/2
    shipping = obs.shipping_usd or 0
    import_fee = market.low_value_import_fee_usd_estimate
    landed = supplier + shipping + import_fee
    gross = net_revenue - landed
    gross_margin = gross/net_revenue if net_revenue else None
    markup = retail_gross/landed if landed else None
    payment_fee = retail_gross*0.03
    # Heuristic reserve, not a predicted return rate: risk 0..100 -> 1%..13% return reserve rate,
    # assuming 60% of returned order value is economically lost after shipping/handling/recovery.
    assumed_return_rate = 0.01 + (product.base_return_risk/100)*0.12
    return_reserve = retail_gross*assumed_return_rate*0.60
    contribution = gross - payment_fee - return_reserve
    return {
        "retail_price_gross_usd": round(retail_gross,2),
        "net_revenue_ex_tax_usd": round(net_revenue,2),
        "supplier_usd": round(supplier,2),
        "shipping_usd": round(shipping,2),
        "import_fee_usd_estimate": round(import_fee,2),
        "landed_cost_usd": round(landed,2),
        "gross_profit_pre_fees_usd": round(gross,2),
        "gross_margin_pct": round(gross_margin*100,1) if gross_margin is not None else None,
        "retail_to_landed_markup_x": round(markup,2) if markup is not None else None,
        "payment_fee_reserve_usd": round(payment_fee,2),
        "return_reserve_usd": round(return_reserve,2),
        "assumed_return_rate_pct": round(assumed_return_rate*100,1),
        "contribution_pre_ads_usd": round(contribution,2),
        "breakeven_cac_usd": round(max(0,contribution),2),
    }


def margin_score(econ: dict) -> float:
    margin = econ.get("gross_margin_pct")
    markup = econ.get("retail_to_landed_markup_x")
    contribution = econ.get("contribution_pre_ads_usd")
    if margin is None:
        return 45
    s = clamp((margin-25)/45*100)
    if markup is not None and markup >= 3:
        s = min(100, s+8)
    elif markup is not None and markup < 2:
        s = max(0, s-25)
    if contribution is not None and contribution < 20:
        s = max(0, s-20)
    return s


def shipping_score(obs: ProductObservation, market: Market) -> float:
    score = 100 - market.shipping_difficulty*0.35
    if obs.shipping_days is not None:
        score -= max(0, obs.shipping_days-5)*4.5
    if obs.shipping_usd is not None:
        score -= max(0, obs.shipping_usd-8)*1.2
    return clamp(score)


def market_fit(product: ProductSeed, market: Market) -> float:
    base = market.affluent_score*0.35 + market.ecommerce_maturity*0.30 + market.localization_advantage*0.20
    winter = (product.winter_affinity/100)*(market.q4_winter_intensity)*0.15
    if market.q4_winter_intensity == 0 and product.winter_affinity > 60:
        winter -= 35
    return clamp(base+winter)


def risk_penalties(product: ProductSeed, obs: ProductObservation, config: dict) -> dict[str,float]:
    rules = config["risk_penalties"]
    supplier_concentration = 70 if obs.supplier_count is None else clamp(100-obs.supplier_count*5)
    return {
        "compliance": product.compliance_risk * float(rules.get("compliance",0)),
        "ip": _ip_risk(product) * float(rules.get("ip",0)),
        "returns": product.base_return_risk * float(rules.get("returns",0)),
        "fragility": product.fragility_risk * float(rules.get("fragility",0)),
        "supplier_concentration": supplier_concentration * float(rules.get("supplier_concentration",0)),
    }


def _ip_risk(product: ProductSeed) -> float:
    hot = {"dupe","replica","compatible with patented","designer"}
    txt = (product.name+" "+" ".join(product.keywords)).lower()
    return 75 if any(x in txt for x in hot) else 12


def score(product: ProductSeed, market: Market, obs: ProductObservation, config: dict) -> ScoreBreakdown:
    econ = economics(product, market, obs)
    components = {
        "search_demand": log_score(obs.search_volume),
        "search_momentum": momentum_score(obs.search_momentum),
        "competition_gap": competition_gap_score(obs),
        "gross_margin": margin_score(econ),
        "shipping_fit": shipping_score(obs, market),
        "giftability": product.giftability,
        "evergreen": product.evergreen,
        "upsellability": product.upsellability,
        "ai_advisor_value": product.ai_advisor_value,
        "market_fit": market_fit(product, market),
    }
    weighted = sum(components[k]*float(config["weights"].get(k,0)) for k in components)
    penalties = risk_penalties(product, obs, config)
    total = clamp(weighted - sum(penalties.values()))
    t = config["thresholds"]
    verdict = "STRONG" if total >= t["strong"] else "TEST" if total >= t["test"] else "WATCH" if total >= t["watch"] else "REJECT"
    reasons, risks, missing = [], [], []
    top = sorted(components.items(), key=lambda kv: kv[1], reverse=True)[:4]
    reasons.extend([f"{k.replace('_',' ')} {v:.0f}/100" for k,v in top])
    if econ.get("retail_to_landed_markup_x") and econ["retail_to_landed_markup_x"] >= 3:
        reasons.append(f"retail/landed markup {econ['retail_to_landed_markup_x']:.1f}×")
    if product.ai_advisor_value >= 80:
        reasons.append("high-value specialist buying-advisor opportunity")
    if product.winter_affinity >= 70 and market.q4_winter_intensity >= 70:
        reasons.append("strong Q4 winter-market fit")
    if product.compliance_risk >= 40:
        risks.append("material product-safety/compliance diligence required")
    if product.base_return_risk >= 45:
        risks.append("return/refund risk could erase apparent margin")
    if econ.get("retail_to_landed_markup_x") and econ["retail_to_landed_markup_x"] < 2.5:
        risks.append("retail/landed markup below preferred 2.5×")
    if obs.shipping_days and obs.shipping_days > 10:
        risks.append("shipping slower than preferred Q4 window")
    if market.low_value_import_fee_usd_estimate:
        risks.append("2026 low-value import duty estimate included; verify current customs/handling rules before launch")
    for f in ["search_volume","search_momentum","keyword_competition","competitor_count","supplier_price_median_usd","shipping_days"]:
        if getattr(obs,f) is None:
            missing.append(f)
    return ScoreBreakdown(
        product_slug=product.slug, market=market.code, total_score=round(total,2), verdict=verdict,
        components={k:round(v,2) for k,v in components.items()},
        penalties={k:round(v,2) for k,v in penalties.items()}, economics=econ,
        reasons=reasons, risks=risks, missing_signals=missing,
    )
