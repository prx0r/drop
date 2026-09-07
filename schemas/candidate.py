"""Candidate schema.

A Candidate is a PRODUCT × COUNTRY cell that we're evaluating.
It has a state machine, economics, competition, and scoring.

The state machine is the canonical lifecycle:
    DISCOVERED -> DEMAND_VERIFIED -> MERCHANT_GAP_VERIFIED -> SUPPLY_PATH_VERIFIED
    -> MARGIN_VERIFIED -> SEARCH_ECONOMICS_VERIFIED -> LAUNCHABLE
    -> FREE_TRAFFIC_TEST -> PAID_TEST -> PROFITABLE / KILLED

Key principle: every field must have a source (OBSERVED, ESTIMATED, UNKNOWN).
No field is null — unknowns are first-class objects.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class CandidateState(str, Enum):
    """Canonical candidate lifecycle.

    Transitions must be explicit and logged.
    """

    DISCOVERED = "DISCOVERED"
    DEMAND_VERIFIED = "DEMAND_VERIFIED"
    MERCHANT_GAP_VERIFIED = "MERCHANT_GAP_VERIFIED"
    SUPPLY_PATH_VERIFIED = "SUPPLY_PATH_VERIFIED"
    MARGIN_VERIFIED = "MARGIN_VERIFIED"
    SEARCH_ECONOMICS_VERIFIED = "SEARCH_ECONOMICS_VERIFIED"
    LAUNCHABLE = "LAUNCHABLE"
    FREE_TRAFFIC_TEST = "FREE_TRAFFIC_TEST"
    PAID_TEST = "PAID_TEST"
    PROFITABLE = "PROFITABLE"
    KILLED = "KILLED"
    HUMAN_ACTION_REQUIRED = "HUMAN_ACTION_REQUIRED"
    FROZEN = "FROZEN"

    # Additional states for nuance
    RESEARCHING = "RESEARCHING"
    BUILD_READY = "BUILD_READY"


# Valid transitions: from_state -> set of allowed to_states
VALID_TRANSITIONS: dict[CandidateState, set[CandidateState]] = {
    CandidateState.DISCOVERED: {
        CandidateState.DEMAND_VERIFIED,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.DEMAND_VERIFIED: {
        CandidateState.MERCHANT_GAP_VERIFIED,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.MERCHANT_GAP_VERIFIED: {
        CandidateState.SUPPLY_PATH_VERIFIED,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.SUPPLY_PATH_VERIFIED: {
        CandidateState.MARGIN_VERIFIED,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.MARGIN_VERIFIED: {
        CandidateState.SEARCH_ECONOMICS_VERIFIED,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.SEARCH_ECONOMICS_VERIFIED: {
        CandidateState.LAUNCHABLE,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.LAUNCHABLE: {
        CandidateState.FREE_TRAFFIC_TEST,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.FREE_TRAFFIC_TEST: {
        CandidateState.PAID_TEST,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.PAID_TEST: {
        CandidateState.PROFITABLE,
        CandidateState.KILLED,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.PROFITABLE: {
        CandidateState.KILLED,
    },
    CandidateState.KILLED: set(),  # Terminal state
    CandidateState.HUMAN_ACTION_REQUIRED: {
        CandidateState.DISCOVERED,
        CandidateState.DEMAND_VERIFIED,
        CandidateState.MERCHANT_GAP_VERIFIED,
        CandidateState.SUPPLY_PATH_VERIFIED,
        CandidateState.MARGIN_VERIFIED,
        CandidateState.SEARCH_ECONOMICS_VERIFIED,
        CandidateState.LAUNCHABLE,
        CandidateState.FROZEN,
    },
    CandidateState.FROZEN: {
        CandidateState.DISCOVERED,
        CandidateState.DEMAND_VERIFIED,
        CandidateState.MERCHANT_GAP_VERIFIED,
        CandidateState.SUPPLY_PATH_VERIFIED,
        CandidateState.MARGIN_VERIFIED,
        CandidateState.SEARCH_ECONOMICS_VERIFIED,
        CandidateState.LAUNCHABLE,
        CandidateState.HUMAN_ACTION_REQUIRED,
    },
    CandidateState.RESEARCHING: {
        CandidateState.DEMAND_VERIFIED,
        CandidateState.KILLED,
    },
    CandidateState.BUILD_READY: {
        CandidateState.FREE_TRAFFIC_TEST,
        CandidateState.KILLED,
    },
}


class FieldSource(str, Enum):
    """Where did this field value come from?"""

    OBSERVED = "OBSERVED"  # We measured it ourselves
    ESTIMATED = "ESTIMATED"  # We inferred it from evidence
    UNKNOWN = "UNKNOWN"  # We don't know
    ASSUMED = "ASSUMED"  # We assumed a default
    DERIVED = "DERIVED"  # Calculated from other fields


class ScoreComponent(BaseModel):
    """A single dimension of the scoring rubric.

    Total score = sum(component * weight) * confidence_multiplier
    """

    name: str  # e.g. "demand", "economics", "merchant_gap"
    raw_score: float  # 0-100
    weight: float  # 0-1, sum of weights = 1.0
    weighted_score: float  # raw_score * weight
    reason: str  # Why this score?
    source: FieldSource = FieldSource.ESTIMATED


class GateResult(BaseModel):
    """Result of a hard gate check.

    Gates are binary: PASS, QUARANTINE, or REJECT.
    Any REJECT kills the candidate.
    """

    gate_name: str
    status: str  # "PASS", "QUARANTINE", "REJECT"
    reason: str
    details: Optional[dict] = None


class GateStatus(str, Enum):
    PASS = "PASS"
    QUARANTINE = "QUARANTINE"
    REJECT = "REJECT"


class Candidate(BaseModel):
    """A PRODUCT × COUNTRY cell being evaluated.

    This is the backbone entity. Every pipeline reads or writes candidates.
    Every field has a source (OBSERVED, ESTIMATED, UNKNOWN).
    """

    candidate_id: str = Field(default_factory=lambda: f"C-{uuid.uuid4().hex[:12]}")

    # Identity
    product_family: str  # e.g. "Testo 550s"
    country_code: str  # e.g. "NO"
    category: Optional[str] = None  # e.g. "HVAC/R"
    subcategory: Optional[str] = None

    # State machine
    state: CandidateState = CandidateState.DISCOVERED
    state_history: list[dict] = Field(default_factory=list)  # [{state, timestamp, reason}]

    # Economics (all with source tracking)
    selling_price: Optional[float] = None
    selling_price_currency: Optional[str] = None
    selling_price_source: FieldSource = FieldSource.UNKNOWN

    supplier_price: Optional[float] = None
    supplier_price_source: FieldSource = FieldSource.UNKNOWN

    shipping_cost: Optional[float] = None
    shipping_cost_source: FieldSource = FieldSource.UNKNOWN

    vat_rate: Optional[float] = None  # 0-1
    duty_rate: Optional[float] = None  # 0-1

    contribution_margin: Optional[float] = None  # Pre-ad margin
    contribution_margin_source: FieldSource = FieldSource.UNKNOWN

    # Traffic
    estimated_daily_clicks: Optional[int] = None
    estimated_cpc: Optional[float] = None
    cpc_source: FieldSource = FieldSource.UNKNOWN

    # CVR scenarios
    cvr_pessimistic: Optional[float] = None  # 0-1
    cvr_base: Optional[float] = None  # 0-1
    cvr_optimistic: Optional[float] = None  # 0-1

    # Break-even
    break_even_cvr: Optional[float] = None  # 0-1
    break_even_cpc: Optional[float] = None

    # Demand
    search_volume_monthly: Optional[int] = None
    demand_growth_rate: Optional[float] = None  # -1 to 1

    # Competition
    total_sellers: Optional[int] = None
    good_sellers: Optional[int] = None  # Sellers meeting quality threshold
    merchant_gap_score: Optional[float] = None  # 0-1, higher = more gap
    price_dispersion: Optional[float] = None  # coefficient of variation

    # Supplier
    supplier_name: Optional[str] = None
    supplier_contact: Optional[str] = None
    supplier_status: Optional[str] = None  # "contacted", "quoted", "authorized"
    single_supplier_risk: Optional[float] = None  # 0-1

    # Scoring
    score_components: list[ScoreComponent] = Field(default_factory=list)
    total_score: Optional[float] = None  # 0-100
    confidence_multiplier: float = 1.0

    # Gates
    gate_results: list[GateResult] = Field(default_factory=list)
    all_gates_pass: bool = False

    # Decision
    recommended_action: Optional[str] = None  # "ADVANCE", "HOLD", "KILL", "LAUNCH"
    action_rationale: Optional[str] = None

    # Bayesian evidence
    clicks_observed: int = 0
    orders_observed: int = 0
    revenue_observed: float = 0.0

    # Unknowns (first-class objects)
    unknown_fields: list[str] = Field(default_factory=list)  # field names that are unknown

    # Metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    probe_id: Optional[str] = None  # Which probe generated this?

    def transition(self, new_state: CandidateState, reason: str) -> bool:
        """Attempt a state transition.

        Returns True if transition was valid, False otherwise.
        """
        if new_state not in VALID_TRANSITIONS.get(self.state, set()):
            return False

        self.state_history.append(
            {
                "from": self.state.value,
                "to": new_state.value,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "reason": reason,
            }
        )
        self.state = new_state
        self.updated_at = datetime.now(timezone.utc)
        return True

    @property
    def is_terminal(self) -> bool:
        """Is this candidate in a terminal state?"""
        return self.state in {CandidateState.PROFITABLE, CandidateState.KILLED}

    @property
    def progress(self) -> float:
        """How far through the state machine is this candidate? 0-1."""
        # Define linear progression states (excluding terminal and special states)
        linear_states = [
            CandidateState.DISCOVERED,
            CandidateState.DEMAND_VERIFIED,
            CandidateState.MERCHANT_GAP_VERIFIED,
            CandidateState.SUPPLY_PATH_VERIFIED,
            CandidateState.MARGIN_VERIFIED,
            CandidateState.SEARCH_ECONOMICS_VERIFIED,
            CandidateState.LAUNCHABLE,
            CandidateState.FREE_TRAFFIC_TEST,
            CandidateState.PAID_TEST,
            CandidateState.PROFITABLE,
        ]

        if self.state == CandidateState.KILLED:
            return 0.0  # Killed candidates have no progress
        if self.state == CandidateState.PROFITABLE:
            return 1.0  # Fully complete

        try:
            idx = linear_states.index(self.state)
            return idx / (len(linear_states) - 1)  # 0.0 to 1.0
        except ValueError:
            # For non-linear states (FROZEN, HUMAN_ACTION_REQUIRED, etc.)
            return 0.5  # Assume middle progress
            return 0.0
