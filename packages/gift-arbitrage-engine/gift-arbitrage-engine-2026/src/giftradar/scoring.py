from __future__ import annotations
from .models import Opportunity, Score, Evidence

def clamp(x: float, lo: float = 0, hi: float = 100) -> float:
    return max(lo, min(hi, x))

def score_opportunity(o: Opportunity, evidence: dict[str, Evidence], cfg: dict) -> Score:
    weights = cfg["weights"]
    components = {k: clamp(float(o.metrics.get(k, 50))) for k in weights}
    weighted = sum(components[k] * float(weights[k]) for k in weights)

    risk_cfg = cfg["risk_penalties"]
    penalties = {
        key: clamp(float(o.metrics.get(key, 0))) * float(mult)
        for key, mult in risk_cfg.items()
    }
    # Evidence bonus is deliberately small: it prevents high-review saturation from dominating.
    evs = [evidence[k] for k in o.evidence_keys if k in evidence]
    evidence_quality = sum(e.confidence for e in evs) / max(1, len(evs))
    evidence_bonus = min(float(cfg.get("max_evidence_bonus", 4)), len(evs) * evidence_quality * 0.65)
    total = clamp(weighted - sum(penalties.values()) + evidence_bonus)

    t = cfg["thresholds"]
    verdict = "BUILD" if total >= t["build"] else "TEST" if total >= t["test"] else "WATCH" if total >= t["watch"] else "PASS"
    price_mid = sum(o.target_price_usd)/2
    cogs_mid = sum(o.target_cogs_usd)/2
    gm = ((price_mid-cogs_mid)/price_mid*100) if price_mid else 0
    top = sorted(components.items(), key=lambda kv: kv[1], reverse=True)[:5]
    reasons = [f"{k.replace('_',' ')} {v:.0f}/100" for k,v in top]
    if components.get("ai_effort_removed",0) >= 85:
        reasons.append("AI removes substantial customer/design labour")
    if components.get("q4_multiplier",0) >= 85:
        reasons.append("strong holiday/occasion multiplier")
    if components.get("recurring_graph",0) >= 75:
        reasons.append("can seed reminders, recipient profiles or annual repeats")
    if gm >= 60:
        reasons.append(f"illustrative gross margin {gm:.0f}% before fees/ads")
    return Score(
        slug=o.slug, name=o.name, total=round(total,2), verdict=verdict,
        components={k:round(v,2) for k,v in components.items()},
        penalties={k:round(v,2) for k,v in penalties.items()},
        price_mid=round(price_mid,2), cogs_mid=round(cogs_mid,2),
        gross_margin_pct=round(gm,1), evidence_count=len(evs),
        reasons=reasons, risks=o.risks,
    )
