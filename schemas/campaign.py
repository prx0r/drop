"""Campaign compiler schemas.

The bridge from research to deployment.
CampaignHypothesis, LaunchSpec, Deployment.

NOTE: Country schemas are imported from schemas/country.py
to avoid duplication. Campaign-specific schemas are defined here.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

# Import canonical country schemas (no duplication)
from schemas.country import (
    CountryProfile,
    CommercePolicy,
    ConsumerBehavior,
    Logistics,
    InstalledBase,
    LifecycleEvent,
    MerchantCensus,
    SupplyNode,
    DemandSignal,
    CountrySnapshot,
)


class CampaignState(str, Enum):
    """Campaign lifecycle states."""
    DRAFT = "DRAFT"
    COMPILED = "COMPILED"
    PLANNED = "PLANNED"
    APPLYING = "APPLYING"
    DEPLOYED = "DEPLOYED"
    PREFLIGHT = "PREFLIGHT"
    READY = "READY"
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    OBSERVING = "OBSERVING"
    GRADED = "GRADED"
    KILLED = "KILLED"


class CampaignHypothesis(BaseModel):
    """Scientific proposition with explicit falsifiers."""

    hypothesis_id: str = Field(default_factory=lambda: f"CH-{uuid.uuid4().hex[:12]}")

    # Context
    candidate_id: str
    country_code: str
    ecosystem: str

    # The claim
    statement: str
    causal_mechanism: list[str]

    # What we're measuring
    primary_outcome: str = "realized_cm2"
    intermediate_outcomes: list[str] = Field(default_factory=list)

    # What would kill this
    falsifiers: list[str]

    # Reference snapshots
    country_snapshot_id: Optional[str] = None
    candidate_snapshot_id: Optional[str] = None

    # Activation
    activation_status: str = "BLOCKED"

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LaunchSpec(BaseModel):
    """Complete desired external configuration."""

    spec_id: str = Field(default_factory=lambda: f"LS-{uuid.uuid4().hex[:12]}")
    campaign_hypothesis_id: str

    # Store configuration
    store: dict = Field(default_factory=dict)

    # Decision engine
    decision_engine: dict = Field(default_factory=dict)

    # Merchant/Products
    merchant: dict = Field(default_factory=dict)

    # Ads configuration
    ads: dict = Field(default_factory=dict)

    # Measurement
    measurement: dict = Field(default_factory=dict)

    # Economics
    economics: dict = Field(default_factory=dict)

    # Activation gates
    activation_gates: list[dict] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Deployment(BaseModel):
    """What actually exists externally."""

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
    status: str = "PENDING"

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActivationGate(BaseModel):
    """A deterministic gate that must pass before activation."""

    gate_id: str
    name: str
    description: str
    required: bool = True

    # Evidence
    evidence_source: str
    evidence_query: Optional[str] = None
    evidence_value: Optional[str] = None

    # Status
    status: str = "UNKNOWN"  # UNKNOWN, PASS, FAIL, BLOCKED
    verified_at: Optional[datetime] = None

    # If blocked
    blocked_reason: Optional[str] = None
    human_action_required: Optional[str] = None
