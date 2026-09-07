"""Country Model v1 schemas.

Machine-readable economic operating model of a country.
Finland is the canonical implementation.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class CountryProfile(BaseModel):
    """Slow-changing country truths."""

    country_code: str  # "FI"
    country_name: str  # "Finland"
    currency: str  # "EUR"
    languages: list[str]  # ["fi", "sv", "en"]
    population: int  # 5,500,000
    gdp_per_capita: float  # 50,000 EUR
    ecommerce_penetration: float  # 0.84
    cross_border_rate: float  # 0.80
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CommercePolicy(BaseModel):
    """Regulatory and policy rules."""

    country_code: str
    vat_rate: float  # 0.255
    vat_name: str  # "ALV"
    consumer_return_days: int  # 14
    online_withdrawal_required: bool  # True (since 2026-06-19)
    required_checkout_fields: list[str]  # ["price_incl_vat", "merchant_info", "withdrawal_right"]
    required_disclosures: list[str]  # ["priset sisältää ALV:n", "vakuutus", "toimitusehdot"]
    consent_regime: str  # "eea_gdpr"
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConsumerBehavior(BaseModel):
    """Consumer preferences and behavior."""

    country_code: str
    payment_preferences: list[str]  # ["online_banking", "debit_card", "mobilepay"]
    delivery_preferences: list[str]  # ["parcel_locker", "home_delivery", "service_point"]
    trust_signals: list[str]  # ["local_brand", "reviews", "trust_seal"]
    checkout_friction: list[str]  # ["complex_form", "account_required"]
    mobile_behavior: str  # "high_mobile_share"
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Logistics(BaseModel):
    """Shipping and delivery infrastructure."""

    country_code: str
    primary_carriers: list[str]  # ["Posti", "Matkahuolto", "DB Schenker"]
    parcel_locker_density: float  # lockers per 1000 people
    average_delivery_days: float  # 2.5
    shipping_cost_curve: dict  # {"0-5kg": 5.90, "5-10kg": 8.90, ...}
    remote_area_surcharge: float  # 15.00 EUR
    free_shipping_threshold: Optional[float] = None  # 50.00 EUR
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class InstalledBase(BaseModel):
    """A large physical system installed in the country."""

    system_id: str = Field(default_factory=lambda: f"IB-{uuid.uuid4().hex[:12]}")
    country_code: str
    system_type: str  # "heat_pump", "cottage", "ev", "sauna", etc.
    installed_base: int  # Number of units
    annual_sales: int  # New units per year
    avg_age_years: Optional[float] = None
    replacement_cycle_years: Optional[float] = None
    warranty_years: Optional[float] = None
    
    # Lifecycle events
    failure_modes: list[str] = Field(default_factory=list)
    accessories: list[str] = Field(default_factory=list)
    compatibility_requirements: list[str] = Field(default_factory=list)
    service_network: str = "limited"  # "extensive", "limited", "none"
    
    # Economic potential
    annual_replacement_value: Optional[float] = None  # EUR
    annual_accessory_value: Optional[float] = None  # EUR
    annual_service_value: Optional[float] = None  # EUR
    
    # Source
    source_url: Optional[str] = None
    source_year: Optional[int] = None
    confidence: float = 0.5
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LifecycleEvent(BaseModel):
    """A recurring economic event triggered by installed base."""

    event_id: str = Field(default_factory=lambda: f"LE-{uuid.uuid4().hex[:12]}")
    installed_base_id: str
    event_type: str  # "replacement", "maintenance", "upgrade", "failure"
    trigger: str  # "age", "warranty_expiry", "season", "regulation"
    frequency: str  # "annual", "every_5_years", "one_time"
    commercial_needs: list[str]  # What the customer needs to buy
    average_spend: Optional[float] = None  # EUR
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class MerchantCensus(BaseModel):
    """Point-in-time snapshot of merchant landscape for a product."""

    snapshot_id: str = Field(default_factory=lambda: f"MC-{uuid.uuid4().hex[:12]}")
    country_code: str
    gtin: Optional[str] = None
    category: str
    brand: Optional[str] = None
    model: Optional[str] = None
    
    # Merchant counts
    seller_count: int
    seller_count_change_30d: Optional[int] = None
    stocked_sellers: Optional[int] = None
    
    # Pricing
    median_price: Optional[float] = None
    minimum_price: Optional[float] = None
    price_dispersion: Optional[float] = None  # CV
    shipping_inclusive_minimum: Optional[float] = None
    
    # Delivery
    delivery_days: Optional[float] = None
    
    # Popularity
    popularity_rank: Optional[int] = None
    popularity_rank_change: Optional[int] = None
    
    # Quality
    merchant_quality_top_5: list[dict] = Field(default_factory=list)
    
    # Source
    source: str = "hinta.fi"
    snapshot_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SupplyNode(BaseModel):
    """A node in the supply graph."""

    node_id: str = Field(default_factory=lambda: f"SN-{uuid.uuid4().hex[:12]}")
    node_type: str  # "manufacturer", "distributor", "wholesaler", "retailer"
    name: str
    country: str
    
    # Capabilities
    wholesale_price: Optional[float] = None
    currency: str = "EUR"
    warehouse_country: Optional[str] = None
    lead_time_days: Optional[int] = None
    moq: Optional[int] = None
    dropship_capable: bool = False
    reseller_authorized: bool = False
    
    # Restrictions
    map_restrictions: bool = False
    territory_restrictions: list[str] = Field(default_factory=list)
    warranty_handling: Optional[str] = None  # "manufacturer", "distributor", "seller"
    returns_destination: Optional[str] = None
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DemandSignal(BaseModel):
    """A demand signal from search/comparison engines."""

    signal_id: str = Field(default_factory=lambda: f"DS-{uuid.uuid4().hex[:12]}")
    country_code: str
    query: str
    category: Optional[str] = None
    
    # Metrics
    search_volume: Optional[int] = None
    cpc: Optional[float] = None
    competition: Optional[str] = None  # "low", "medium", "high"
    trend: Optional[str] = None  # "rising", "stable", "falling"
    
    # Intent
    intent_classification: str  # "transactional", "decision", "support", "informational"
    purchase_probability: Optional[float] = None
    
    # Source
    source: str = "google"
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CountrySnapshot(BaseModel):
    """Point-in-time snapshot for campaign compiler."""

    snapshot_id: str = Field(default_factory=lambda: f"CS-{uuid.uuid4().hex[:12]}")
    country_code: str
    snapshot_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # All components
    profile: Optional[CountryProfile] = None
    commerce_policy: Optional[CommercePolicy] = None
    consumer_behavior: Optional[ConsumerBehavior] = None
    logistics: Optional[Logistics] = None
    installed_bases: list[InstalledBase] = Field(default_factory=list)
    lifecycle_events: list[LifecycleEvent] = Field(default_factory=list)
    merchant_censuses: list[MerchantCensus] = Field(default_factory=list)
    supply_nodes: list[SupplyNode] = Field(default_factory=list)
    demand_signals: list[DemandSignal] = Field(default_factory=list)
    
    # Metadata
    completeness_score: float = 0.0  # 0-1, how complete is this snapshot
    freshness_score: float = 0.0  # 0-1, how fresh is the data
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
