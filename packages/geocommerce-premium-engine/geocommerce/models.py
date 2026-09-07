from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, Field, HttpUrl, field_validator

class ProductFacts(BaseModel):
    materials: list[str] = []
    dimensions: dict[str, float | str] = {}
    features: dict[str, Any] = {}
    certifications: list[str] = []
    warranty_months: int = 12
    country_of_origin: str = ""
    hs_code: str = ""
    gtin: str = ""
    brand_authorized: bool = True
    electrical: bool = False
    electrical_certified: bool = False
    regulated: bool = False
    medical_claims: bool = False
    child_safety_critical: bool = False
    fragile: bool = False
    installation_required: bool = False
    sizing_complexity: float = Field(0.1, ge=0, le=1)
    return_risk: float = Field(0.1, ge=0, le=1)
    advisor_fit: float = Field(0.7, ge=0, le=1)
    visual_demo_fit: float = Field(0.7, ge=0, le=1)
    supplier_quality: float = Field(0.7, ge=0, le=1)

class ProductCreate(BaseModel):
    slug: str
    name: str
    category: str
    supplier_cost: float = Field(gt=0)
    supplier_currency: str = "USD"
    supplier_id: str = "manual"
    supplier_url: str | None = None
    images: list[str] = []
    facts: ProductFacts = ProductFacts()

    @field_validator("slug")
    @classmethod
    def slug_safe(cls, value: str) -> str:
        allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-")
        if not value or any(ch not in allowed for ch in value):
            raise ValueError("slug must be lowercase letters, digits, hyphens")
        return value

class MarketConfig(BaseModel):
    code: str
    name: str
    language_code: str
    language_name: str
    google_language_id: str
    google_geo_id: str
    currency: str
    vat_rate: float = Field(ge=0, le=0.4)
    duty_rate_default: float = Field(0, ge=0, le=0.5)
    checkout_methods: list[str] = []
    preferred_delivery: list[str] = []
    localization_friction: float = Field(0.5, ge=0, le=1)
    cross_border_acceptance: float = Field(0.5, ge=0, le=1)
    checkout_sensitivity: float = Field(0.5, ge=0, le=1)
    direct_checkout_ceiling: float = 2500
    assisted_checkout_ceiling: float = 5000
    domain_hint: str = ""
    notes: list[str] = []

class MarketSignal(BaseModel):
    product_slug: str
    market_code: str
    query: str
    currency: str
    avg_monthly_searches: int = Field(ge=0)
    competition_index: float = Field(ge=0, le=100)
    cpc_low: float = Field(ge=0)
    cpc_high: float = Field(ge=0)
    avg_cpc: float = Field(ge=0)
    benchmark_price_gross: float = Field(gt=0)
    shopping_seller_count: int | None = Field(default=None, ge=0)
    source: str
    source_url: str | None = None
    observed_at: str

class SupplierOffer(BaseModel):
    product_slug: str
    supplier: str
    unit_cost: float = Field(gt=0)
    currency: str
    shipping_cost: float = Field(ge=0)
    shipping_days: int = Field(ge=0)
    stock: int | None = Field(default=None, ge=0)
    ship_from_country: str = ""
    source_url: str | None = None
    observed_at: str
    reliability: float = Field(0.7, ge=0, le=1)
    taxes_prepaid: bool = False
    landed_cost_includes_duties: bool = False
    local_return_address: bool = False

class EconomicsInput(BaseModel):
    price_gross: float = Field(gt=0)
    supplier_cost: float = Field(gt=0)
    shipping_cost: float = Field(ge=0)
    vat_rate: float = Field(ge=0, le=0.4)
    duty_rate: float = Field(ge=0, le=0.5)
    payment_fee_rate: float = Field(0.035, ge=0, le=0.15)
    return_reserve_rate: float = Field(0.05, ge=0, le=0.5)
    warranty_reserve_rate: float = Field(0.02, ge=0, le=0.3)
    conservative_cvr: float = Field(0.015, gt=0, le=0.2)
    avg_cpc: float = Field(gt=0)

class OpportunityScore(BaseModel):
    product_slug: str
    market_code: str
    score: float
    verdict: Literal["REJECT", "WATCH", "FREE_LISTING_TEST", "PAID_TEST", "SCALE"]
    checkout_mode: Literal["direct", "assisted", "quote"]
    economics: dict[str, float]
    components: dict[str, float]
    gates: list[str]
    reasons: list[str]

class AdvisorRequest(BaseModel):
    market_code: str
    budget: float = Field(gt=0)
    priorities: list[str] = []
    constraints: dict[str, Any] = {}

class SupportRequest(BaseModel):
    market_code: str
    product_slug: str | None = None
    name: str
    email: str
    phone: str | None = None
    question: str
    wants_callback: bool = False

class ExperimentUpdate(BaseModel):
    spend: float = Field(ge=0)
    clicks: int = Field(ge=0)
    conversions: int = Field(ge=0)
    revenue: float = Field(ge=0)
