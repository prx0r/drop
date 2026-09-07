"""Campaign compiler schemas.

The bridge from research to deployment.
CampaignHypothesis, LaunchSpec, Deployment.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Country Schemas ---


class CountryProfile(BaseModel):
    """Slow-changing country truths.

    Language, currency, tax regime, payment conventions, logistics.
    These rarely change and are shared across all campaigns in a country.
    """

    country_code: str  # "NO"
    country_name: str  # "Norway"
    currency: str  # "NOK"
    languages: list[str]  # ["no", "en"]
    vat_rate: float  # 0.25
    consumer_protection_days: int  # 14 days return
    payment_methods: list[str]  # ["vipps", "card", "klarna"]
    cross_border_rules: str  # "EEA free trade, VOEC for non-EEA"
    major_marketplaces: list[str]  # ["finn.no", "komplett.no"]
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CountryObservation(BaseModel):
    """Temporal country measurements.

    Every observation gets: value, unit, source, timestamps, confidence.
    These change over time and are the input to probes.
    """

    observation_id: str = Field(default_factory=lambda: f"CO-{uuid.uuid4().hex[:12]}")
    country_code: str
    category: str  # "weather_station", "ev_charger", etc.
    metric: str  # "installed_base", "cpc", "seller_count"
    value: float
    unit: str  # "count", "NOK", "percentage"
    
    # Source provenance
    source_url: Optional[str] = None
    source_name: Optional[str] = None
    evidence_grade: str = "C"  # A, B, C, D
    
    # Temporal
    event_time: Optional[datetime] = None  # When the event happened
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    available_at: Optional[datetime] = None  # When it became available
    fresh_until: Optional[datetime] = None  # When this expires
    
    # Confidence
    confidence: float = 0.5  # 0-1


class CountryExecutionPolicy(BaseModel):
    """Derived deterministic behavior for a country.

    This is what the campaign compiler consumes.
    Generated from CountryProfile + CountryObservations.
    """

    country_code: str
    currency: str
    required_language: str  # "no"
    required_payment_methods: list[str]
    required_disclosures: list[str]  # "priser inkl. mva", "angrefrist"
    tax_calculation: str  # "include_vat"
    shipping_constraints: list[str]  # ["max_14_days", "track_and_trace"]
    consent_regime: str  # "eea_gdpr"
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# --- Campaign Schemas ---


class CampaignState(str, Enum):
    """Campaign lifecycle states."""
    
    DRAFT = "DRAFT"  # Hypothesis exists, no spec
    COMPILED = "COMPILED"  # LaunchSpec generated
    PLANNED = "PLANNED"  # Plan reviewed, ready to apply
    APPLYING = "APPLYING"  # Deploying resources
    DEPLOYED = "DEPLOYED"  # Resources exist, paused
    PREFLIGHT = "PREFLIGHT"  # Running verification checks
    READY = "READY"  # All gates pass
    ACTIVE = "ACTIVE"  # Campaign running
    PAUSED = "PAUSED"  # Campaign paused
    OBSERVING = "OBSERVING"  # Collecting outcome data
    GRADED = "GRADED"  # Hypothesis evaluated
    KILLED = "KILLED"  # Hypothesis falsified


class CampaignHypothesis(BaseModel):
    """Scientific proposition with explicit falsifiers.

    This is what we're testing. Not "will this store make money?"
    But "does this causal mechanism produce positive CM2?"
    """

    hypothesis_id: str = Field(default_factory=lambda: f"CH-{uuid.uuid4().hex[:12]}")
    
    # Context
    candidate_id: str
    country_code: str
    ecosystem: str  # "weather_station", "ev_charger", etc.
    
    # The claim
    statement: str
    causal_mechanism: list[str]  # e.g. ["installed_base", "replacement_event", "compatibility_complexity"]
    
    # What we're measuring
    primary_outcome: str = "realized_cm2"
    intermediate_outcomes: list[str] = Field(default_factory=lambda: [
        "qualified_session_rate",
        "decision_tool_completion_rate",
        "product_clickthrough_rate",
        "add_to_cart_rate",
        "checkout_rate",
        "purchase_cvr",
        "cac",
    ])
    
    # What would kill this
    falsifiers: list[str]
    
    # Reference snapshots
    country_snapshot_id: Optional[str] = None
    candidate_snapshot_id: Optional[str] = None
    
    # Activation
    activation_status: str = "BLOCKED"  # BLOCKED, READY, ACTIVE, PAUSED, KILLED
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LaunchSpec(BaseModel):
    """Complete desired external configuration.

    This is what the compiler produces.
    The deployers consume this to create real resources.
    """

    spec_id: str = Field(default_factory=lambda: f"LS-{uuid.uuid4().hex[:12]}")
    campaign_hypothesis_id: str
    
    # Store configuration
    store: dict = Field(default_factory=dict)
    # Expected keys: market, language, currency, domain, brand, catalog,
    # pages, navigation, offer, shipping, payments, returns, legal
    
    # Decision engine (the AI advantage)
    decision_engine: dict = Field(default_factory=dict)
    # Expected keys: questions, compatibility_rules, recommendations
    
    # Merchant/Products
    merchant: dict = Field(default_factory=dict)
    # Expected keys: products, gtins, prices, stock, shipping, returns
    
    # Ads configuration
    ads: dict = Field(default_factory=dict)
    # Expected keys: channel, geo, language, keywords, negatives, ads,
    # landing_pages, bidding, budget
    
    # Measurement
    measurement: dict = Field(default_factory=dict)
    # Expected keys: events, conversions, attribution, consent
    
    # Economics
    economics: dict = Field(default_factory=dict)
    # Expected keys: cm0, cm1, cm2, break_even_cac, break_even_cpc
    
    # Activation gates
    activation_gates: list[dict] = Field(default_factory=list)
    # Each gate: {name: str, required: bool, status: str, evidence: str}
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Deployment(BaseModel):
    """What actually exists externally.

    This is the ground truth.
    Diff this against LaunchSpec to find gaps.
    """

    deployment_id: str = Field(default_factory=lambda: f"DE-{uuid.uuid4().hex[:12]}")
    campaign_hypothesis_id: str
    launch_spec_id: str
    
    # What was deployed
    store_id: Optional[str] = None
    product_ids: list[str] = Field(default_factory=list)
    merchant_account_id: Optional[str] = None
    merchant_product_ids: list[str] = Field(default_factory=list)
    google_ads_customer_id: Optional[str] = None
    campaign_id: Optional[str] = None
    ad_group_ids: list[str] = Field(default_factory=list)
    conversion_action_ids: list[str] = Field(default_factory=list)
    
    # Metadata
    deployment_version: int = 1
    deployed_at: Optional[datetime] = None
    status: str = "PENDING"  # PENDING, DEPLOYED, ACTIVE, PAUSED, FAILED
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActivationGate(BaseModel):
    """A deterministic gate that must pass before activation.

    The agent CANNOT override these.
    They are computed from facts, not opinions.
    """

    gate_id: str
    name: str  # e.g. "supplier_authorized"
    description: str
    required: bool = True
    
    # Evidence
    evidence_source: str  # e.g. "supplier_email", "bigquery_query"
    evidence_query: Optional[str] = None  # SQL or API call to verify
    evidence_value: Optional[str] = None  # Actual value found
    
    # Status
    status: str = "UNKNOWN"  # UNKNOWN, PASS, FAIL, BLOCKED
    verified_at: Optional[datetime] = None
    
    # If blocked
    blocked_reason: Optional[str] = None
    human_action_required: Optional[str] = None
