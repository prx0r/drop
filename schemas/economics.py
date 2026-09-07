"""Economic Ledger schemas.

The atomic learning object is the decision_event:
    STATE + AVAILABLE_ACTIONS + CHOSEN_ACTION + POLICY + COST + OUTCOME

Contribution levels CM0-CM3 prevent the system from optimizing
for headline revenue while consuming more in costs than it generates.

CM0 = Product contribution (pre-acquisition)
CM1 = Acquisition contribution (post-ads)
CM2 = Automated operating contribution (post-AI/API costs)
CM3 = Fully loaded experimental contribution (post-everything)

Primary machine optimization reward = CM2.
Information gain decides whether an experiment is worth purchasing.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Contribution Levels ---


class ContributionLevel(str, Enum):
    """The four contribution levels.

    CM0: Product contribution (pre-acquisition)
    CM1: Acquisition contribution (post-ads)
    CM2: Automated operating contribution (post-AI/API costs)
    CM3: Fully loaded experimental contribution (post-everything)
    """

    CM0 = "CM0"
    CM1 = "CM1"
    CM2 = "CM2"
    CM3 = "CM3"


class CostLedger(BaseModel):
    """Complete cost breakdown for a transaction or period.

    Every cost is categorized by type and attributed to a specific level.
    This prevents the system from optimizing for headline revenue while
    consuming more in costs than it generates.
    """

    ledger_id: str = Field(default_factory=lambda: f"CL-{uuid.uuid4().hex[:12]}")

    # Revenue
    gross_revenue: float = 0.0  # Before any deductions
    tax_collected: float = 0.0  # VAT/GST collected
    net_revenue: float = 0.0  # After tax

    # CM0: Product contribution costs
    cogs: float = 0.0  # Cost of goods sold
    supplier_freight: float = 0.0  # Shipping from supplier
    fulfilment: float = 0.0  # Pick, pack, ship to customer
    duty: float = 0.0  # Import duty / customs
    payment_processing: float = 0.0  # Stripe/PayPal fees
    refunds: float = 0.0  # Refund costs
    return_shipping: float = 0.0  # Cost of returns
    warranty_reserve: float = 0.0  # Estimated warranty claims
    chargeback_reserve: float = 0.0  # Estimated chargebacks

    # CM1: Acquisition costs
    paid_acquisition: float = 0.0  # Google Ads, Facebook, etc.
    affiliate_commissions: float = 0.0

    # CM2: Automated operating costs
    ai_tokens: float = 0.0  # LLM API costs
    scraping_api: float = 0.0  # Data collection costs
    image_generation: float = 0.0  # AI image/video generation
    agent_compute: float = 0.0  # Agent runtime costs
    per_order_software: float = 0.0  # Per-order API costs

    # CM3: Fully loaded costs
    domain_costs: float = 0.0  # Domain registration, DNS
    software_costs: float = 0.0  # Shopify, hosting, etc.
    human_intervention: float = 0.0  # Human time at loaded cost
    samples: float = 0.0  # Product samples
    setup_expenses: float = 0.0  # One-time setup costs

    # Calculated contribution margins
    cm0: float = Field(default=0.0, description="Product contribution")
    cm1: float = Field(default=0.0, description="Acquisition contribution")
    cm2: float = Field(default=0.0, description="Automated operating contribution")
    cm3: float = Field(default=0.0, description="Fully loaded contribution")

    # Metadata
    currency: str = "USD"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    period_start: Optional[datetime] = None
    period_end: Optional[datetime] = None

    def calculate(self) -> None:
        """Calculate all contribution levels."""
        self.net_revenue = self.gross_revenue - self.tax_collected

        # CM0: Product contribution
        self.cm0 = (
            self.net_revenue
            - self.cogs
            - self.supplier_freight
            - self.fulfilment
            - self.duty
            - self.payment_processing
            - self.refunds
            - self.return_shipping
            - self.warranty_reserve
            - self.chargeback_reserve
        )

        # CM1: Acquisition contribution
        self.cm1 = self.cm0 - self.paid_acquisition - self.affiliate_commissions

        # CM2: Automated operating contribution
        self.cm2 = (
            self.cm1
            - self.ai_tokens
            - self.scraping_api
            - self.image_generation
            - self.agent_compute
            - self.per_order_software
        )

        # CM3: Fully loaded contribution
        self.cm3 = (
            self.cm2
            - self.domain_costs
            - self.software_costs
            - self.human_intervention
            - self.samples
            - self.setup_expenses
        )

    @property
    def cm0_margin(self) -> float:
        """CM0 as percentage of net revenue."""
        if self.net_revenue == 0:
            return 0.0
        return self.cm0 / self.net_revenue

    @property
    def cm2_margin(self) -> float:
        """CM2 as percentage of net revenue."""
        if self.net_revenue == 0:
            return 0.0
        return self.cm2 / self.net_revenue

    @property
    def cac(self) -> float:
        """Customer acquisition cost."""
        return self.paid_acquisition

    @property
    def ltv_to_cac(self) -> Optional[float]:
        """LTV/CAC ratio (requires external LTV estimate)."""
        return None  # Requires external calculation


# --- Decision Events ---


class DecisionAction(str, Enum):
    """Available actions the agent can take."""

    # Research
    RESEARCH_SUPPLIER = "RESEARCH_SUPPLIER"
    RESEARCH_SEARCH_DEMAND = "RESEARCH_SEARCH_DEMAND"
    RESEARCH_COMPETITION = "RESEARCH_COMPETITION"
    RESEARCH_ECONOMICS = "RESEARCH_ECONOMICS"

    # Kill
    KILL = "KILL"

    # Build
    BUILD_FREE_PAGE = "BUILD_FREE_PAGE"
    BUILD_STORE = "BUILD_STORE"
    BUILD_COMPARISON = "BUILD_COMPARISON"

    # Test
    FREE_LISTING_TEST = "FREE_LISTING_TEST"
    PAID_PROBE_5 = "PAID_PROBE_5EUR"
    PAID_PROBE_10 = "PAID_PROBE_10EUR"
    PAID_PROBE_50 = "PAID_PROBE_50EUR"

    # Optimize
    CHANGE_PRICE = "CHANGE_PRICE"
    CHANGE_CREATIVE = "CHANGE_CREATIVE"
    CHANGE_SUPPLIER = "CHANGE_SUPPLIER"
    EXPAND_COUNTRY = "EXPAND_COUNTRY"

    # Scale
    SCALE_BUDGET = "SCALE_BUDGET"
    STOCK_INVENTORY = "STOCK_INVENTORY"
    SWITCH_FULFILMENT = "SWITCH_FULFILMENT"


class DecisionEvent(BaseModel):
    """Immutable record of an agent decision.

    This is the atomic learning object:
        STATE + AVAILABLE_ACTIONS + CHOSEN_ACTION + POLICY + COST + OUTCOME

    Every decision event is append-only. Never modify after creation.
    """

    event_id: str = Field(default_factory=lambda: f"DE-{uuid.uuid4().hex[:12]}")

    # Context
    agent_id: str  # Which agent made this decision?
    policy_id: Optional[str] = None  # Which policy version?
    policy_version: Optional[str] = None

    # State at decision time
    country_code: str
    ecosystem: Optional[str] = None  # e.g. "heat_pump", "ev_charger"
    product_family: Optional[str] = None
    candidate_id: Optional[str] = None

    # Feature snapshot reference
    feature_snapshot_id: Optional[str] = None  # Point-in-time features

    # Available actions
    available_actions: list[str] = Field(default_factory=list)

    # Chosen action
    chosen_action: str
    action_probability: Optional[float] = None  # Propensity score

    # Expected values
    expected_information_value: Optional[float] = None
    expected_cash_cost: Optional[float] = None
    expected_cm2: Optional[float] = None

    # Actual costs (filled after execution)
    actual_cash_cost: float = 0.0
    actual_token_cost: float = 0.0
    actual_api_cost: float = 0.0
    actual_human_minutes: float = 0.0
    actual_wall_clock_seconds: float = 0.0

    # Research metadata
    web_queries: int = 0
    search_cost: float = 0.0
    api_calls: int = 0

    # Outcome (filled later)
    decision_changed: Optional[bool] = None  # Did this change a decision?
    hypothesis_affected: Optional[str] = None
    downstream_experiment_ids: list[str] = Field(default_factory=list)

    # Quality
    result_quality: Optional[str] = None  # "HIGH", "MEDIUM", "LOW"

    # Temporal
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    executed_at: Optional[datetime] = None
    outcome_observed_at: Optional[datetime] = None

    model_config = {"frozen": True}  # Immutable after creation


# --- Feature Snapshots ---


class FeatureSnapshot(BaseModel):
    """Point-in-time feature vector for a candidate.

    CRITICAL: A model is only allowed to train on the feature snapshot
    that existed BEFORE its decision. This prevents data leakage.

    Every feature is frozen at decision time. No future data sneaks in.
    """

    snapshot_id: str = Field(default_factory=lambda: f"FS-{uuid.uuid4().hex[:12]}")
    as_of: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Entity
    candidate_id: str
    country_code: str
    ecosystem: Optional[str] = None

    # Country features
    country_gdp_per_capita: Optional[float] = None
    country_cross_border_rate: Optional[float] = None
    country_mobile_payment_rate: Optional[float] = None
    country_purchasing_power: Optional[float] = None

    # Installed base features
    installed_base: Optional[int] = None
    installed_base_growth: Optional[float] = None  # -1 to 1
    replacement_share: Optional[float] = None  # 0-1
    avg_asset_age: Optional[float] = None  # Years
    warranty_expiry_wave: Optional[float] = None  # Units expiring this year

    # Search/demand features
    search_volume: Optional[int] = None
    search_growth: Optional[float] = None  # -1 to 1
    cpc: Optional[float] = None
    cpc_growth: Optional[float] = None
    query_intent_score: Optional[float] = None  # 0-1

    # Competition features
    seller_count: Optional[int] = None
    good_seller_count: Optional[int] = None
    merchant_quality_gap: Optional[float] = None  # 0-1
    price_dispersion: Optional[float] = None  # CV
    marketplace_dominance: Optional[float] = None  # 0-1

    # Supply features
    supplier_margin: Optional[float] = None  # 0-1
    delivery_days: Optional[float] = None
    single_supplier_risk: Optional[float] = None  # 0-1
    return_risk_class: Optional[str] = None  # "LOW", "MEDIUM", "HIGH"

    # Economics features
    aov: Optional[float] = None  # Average order value
    gross_margin_pct: Optional[float] = None  # 0-1
    source_target_gap: Optional[float] = None  # Price/availability gap

    # Localization features
    localization_score: Optional[float] = None  # 0-1
    local_payment_available: bool = False
    local_shipping_available: bool = False

    # Historical performance (if any)
    previous_probes: int = 0
    previous_falsifications: int = 0
    historical_cm2: Optional[float] = None

    model_config = {"frozen": True}  # Immutable after creation


# --- Economic Outcomes ---


class OutcomeMaturity(str, Enum):
    """Economic outcome maturity levels.

    A sale today isn't economically mature today.
    Returns arrive at day 17, warranty claims at day 41.
    Use estimated reserves initially and true-up later.
    """

    D1 = "1d"
    D7 = "7d"
    D30 = "30d"
    D60 = "60d"
    D90 = "90d"


class EconomicOutcome(BaseModel):
    """Economic outcome for an experiment, with maturity windows.

    Outcomes are updated as time passes. Initial values use estimated
    reserves. Later maturities use actual data.
    """

    outcome_id: str = Field(default_factory=lambda: f"EO-{uuid.uuid4().hex[:12]}")
    experiment_id: str
    candidate_id: str
    country_code: str

    # Maturity tracking
    maturity: OutcomeMaturity

    # Traffic
    impressions: int = 0
    clicks: int = 0
    ctr: float = 0.0
    cpc: float = 0.0

    # Funnel
    atc: int = 0  # Add to cart
    checkout: int = 0
    orders: int = 0
    cvr: float = 0.0  # orders / clicks

    # Economics
    revenue: float = 0.0
    cost_ledger: Optional[CostLedger] = None
    cm0: float = 0.0
    cm1: float = 0.0
    cm2: float = 0.0
    cm3: float = 0.0

    # Returns/reserves
    returns: int = 0
    refunds: float = 0.0
    chargebacks: int = 0
    warranty_claims: int = 0

    # Reserve estimates (updated at each maturity)
    return_reserve: float = 0.0
    warranty_reserve: float = 0.0
    chargeback_reserve: float = 0.0

    # Metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def update_maturity(self, new_data: dict) -> None:
        """Update with new maturity data."""
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)


# --- Policy Action Logging ---


class PolicyAction(BaseModel):
    """Logged policy action with propensity.

    CRITICAL: Once the policy becomes adaptive, historical data is
    no longer i.i.d. The agent preferentially tests things it thinks
    will win. Logging the action probability enables offline policy
    evaluation / inverse propensity methods / doubly robust estimators.
    """

    action_id: str = Field(default_factory=lambda: f"PA-{uuid.uuid4().hex[:12]}")

    # Policy
    policy_id: str
    policy_version: str

    # Context
    candidate_id: str
    country_code: str
    feature_snapshot_id: str

    # Action set and choice
    available_actions: list[str] = Field(default_factory=list)
    chosen_action: str
    chosen_action_probability: float  # Propensity score

    # Expected values
    expected_value: Optional[float] = None
    uncertainty: Optional[float] = None

    # Actual outcome (filled later)
    actual_value: Optional[float] = None

    # Temporal
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"frozen": True}  # Immutable after creation


# --- Treatment Assignment ---


class TreatmentAssignment(BaseModel):
    """Randomized treatment assignment for experiments.

    For every real experiment store, we need to know:
    - What was randomized
    - What was control vs treatment
    - What was the assignment probability
    - When did it start/end

    If creative A gets cheap high-intent Norwegian traffic and
    creative B gets broader expensive traffic, raw CVR cannot
    answer which creative is better.
    """

    assignment_id: str = Field(default_factory=lambda: f"TA-{uuid.uuid4().hex[:12]}")

    # Experiment
    experiment_id: str
    candidate_id: str

    # Randomization
    randomization_unit: str  # "user", "session", "geo", "time"
    control: str  # What is the control?
    treatment: str  # What is the treatment?

    # Assignment probabilities
    assignment_probability: float  # P(assigned to treatment)
    actual_assignment: str  # "control" or "treatment"

    # Timing
    pre_period_start: Optional[datetime] = None
    pre_period_end: Optional[datetime] = None
    start: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end: Optional[datetime] = None

    # Measurement
    metric: str  # What metric are we measuring?
    measurement_horizon_days: int = 30

    # Metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"frozen": True}  # Immutable after creation
