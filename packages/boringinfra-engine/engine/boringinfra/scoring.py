from .models import Opportunity

POSITIVE_WEIGHTS = {
    "verified_revenue_signal": 0.18,
    "workflow_criticality": 0.12,
    "wtp": 0.10,
    "recurrence": 0.10,
    "build_simplicity": 0.10,
    "data_access": 0.08,
    "distribution": 0.10,
    "localization": 0.07,
    "gross_margin": 0.05,
    "competition_gap": 0.10,
}

PENALTY_WEIGHTS = {
    "platform_risk": 0.07,
    "support_burden": 0.05,
    "regulatory_burden": 0.08,
}

# Positive weights sum to 1.00. Penalties can subtract up to 20 points.

def clamp(v: float, lo: float = 0.0, hi: float = 10.0) -> float:
    return max(lo, min(hi, float(v)))


def score(op: Opportunity) -> float:
    base = sum(clamp(getattr(op, k)) * w for k, w in POSITIVE_WEIGHTS.items()) * 10.0
    penalty = sum(clamp(getattr(op, k)) * w for k, w in PENALTY_WEIGHTS.items()) * 10.0
    return round(max(0.0, min(100.0, base - penalty)), 1)


def score_breakdown(op: Opportunity) -> dict[str, float]:
    out = {k: round(clamp(getattr(op, k)) * w * 10.0, 2) for k, w in POSITIVE_WEIGHTS.items()}
    out.update({f"penalty_{k}": round(-clamp(getattr(op, k)) * w * 10.0, 2) for k, w in PENALTY_WEIGHTS.items()})
    out["total"] = score(op)
    return out
