from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from pydantic import BaseModel, Field


class Market(BaseModel):
    code: str
    name: str
    currency: str
    locale: str
    language: str
    google_ads_geo_id: int | None = None
    google_ads_language_id: int | None = None
    vat_rate: float = 0.0
    affluent_score: float = Field(ge=0, le=100)
    ecommerce_maturity: float = Field(ge=0, le=100)
    localization_advantage: float = Field(ge=0, le=100)
    q4_winter_intensity: float = Field(ge=0, le=100)
    shipping_difficulty: float = Field(ge=0, le=100)
    low_value_import_fee_usd_estimate: float = 0.0
    notes: str = ""


class ProductSeed(BaseModel):
    slug: str
    name: str
    cluster: str
    keywords: list[str]
    giftability: float = Field(ge=0, le=100)
    evergreen: float = Field(ge=0, le=100)
    upsellability: float = Field(ge=0, le=100)
    ai_advisor_value: float = Field(ge=0, le=100)
    base_return_risk: float = Field(ge=0, le=100)
    compliance_risk: float = Field(ge=0, le=100)
    fragility_risk: float = Field(ge=0, le=100)
    winter_affinity: float = Field(ge=0, le=100)
    typical_retail_usd: tuple[float, float]
    target_supplier_usd: tuple[float, float]
    notes: str = ""


class Evidence(BaseModel):
    source: str
    metric: str
    value: float | int | str | bool | None = None
    unit: str | None = None
    url: str | None = None
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    confidence: float = Field(default=0.7, ge=0, le=1)
    metadata: dict[str, Any] = Field(default_factory=dict)


class SupplierOffer(BaseModel):
    source: str
    product_id: str
    title: str
    price_usd: float | None = None
    shipping_usd: float | None = None
    shipping_days: float | None = None
    stock: int | None = None
    ships_from: str | None = None
    weight_kg: float | None = None
    url: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ProductObservation(BaseModel):
    product_slug: str
    market: str
    search_volume: float | None = None
    search_momentum: float | None = None
    keyword_competition: float | None = None
    avg_cpc_usd: float | None = None
    competitor_count: int | None = None
    competitor_price_median_usd: float | None = None
    supplier_price_low_usd: float | None = None
    supplier_price_median_usd: float | None = None
    shipping_usd: float | None = None
    shipping_days: float | None = None
    supplier_count: int | None = None
    ad_count: int | None = None
    ad_longevity_days: float | None = None
    evidence: list[Evidence] = Field(default_factory=list)
    supplier_offers: list[SupplierOffer] = Field(default_factory=list)


class ScoreBreakdown(BaseModel):
    product_slug: str
    market: str
    total_score: float
    verdict: Literal["STRONG", "TEST", "WATCH", "REJECT"]
    components: dict[str, float]
    penalties: dict[str, float]
    economics: dict[str, float | None]
    reasons: list[str]
    risks: list[str]
    missing_signals: list[str]


class ScanResult(BaseModel):
    run_id: str
    generated_at: datetime
    markets: list[str]
    sources: list[str]
    scores: list[ScoreBreakdown]
