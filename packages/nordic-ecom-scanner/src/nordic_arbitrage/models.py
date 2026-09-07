from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Candidate:
    id: int | None
    country: str
    niche: str
    product_name: str
    competitor_price_local: float
    supplier_price_usd_low: float
    supplier_price_usd_high: float
    supplier_moq: int
    match_quality: str
    competitor_source: str
    supplier_source: str
    monthly_searches: float = 0.0
    cpc_local: float = 0.0
    assumed_cvr: float = 0.02
    merchant_count: int = 8
    dominant_merchant_share: float = 0.25
    creative_gap: float = 0.5
    title_gap: float = 0.5
    b2b_multiplier: float = 0.0
    bundle_multiplier: float = 0.0
    regulated_risk: float = 0.0
    fragility_risk: float = 0.0
    bulky_risk: float = 0.0
    expected_return_rate: float = 0.06
    estimated_delivery_days: int = 7
    has_local_payment: bool = True
    has_local_return_address: bool = False
    landed_cost_local: float | None = None
    target_price_local: float | None = None
    expected_units_per_order: float = 1.0
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
