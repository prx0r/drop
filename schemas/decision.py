"""Build Decision schema.

The deterministic bridge between "we know things" and "build this."
Every BuildDecision must be reconstructable from frozen evidence.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DecisionType(str, Enum):
    """The possible outcomes of a build decision."""
    REJECT = "REJECT"
    RESEARCH = "RESEARCH"
    PROBE = "PROBE"
    BLOCKED = "BLOCKED"
    BUILD = "BUILD"
    LAUNCH = "LAUNCH"


class BuildDecision(BaseModel):
    """The deterministic bridge between knowledge and action.

    Of every possible thing we could spend money or engineering time on,
    this is the rational next action.

    Every reason must reference evidence IDs.
    Every decision must be reconstructable from frozen evidence.
    """

    decision_id: str = Field(default_factory=lambda: f"BD-{uuid.uuid4().hex[:12]}")
    evidence_cutoff: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Context snapshots
    country_snapshot_id: Optional[str] = None
    candidate_snapshot_id: Optional[str] = None
    hypothesis_id: Optional[str] = None

    # Mechanism
    mechanisms: list[str] = Field(default_factory=list)
    # e.g. ["installed_base_lifecycle", "compatibility_complexity"]

    # Hypothesis
    h1: str = ""  # What we think is true
    h0: str = ""  # What would explain the data without our claim
    falsifiers: list[str] = Field(default_factory=list)

    # Hard gate results
    hard_gate_results: list[dict] = Field(default_factory=list)
    # Each: {gate_name: str, status: str, reason: str, evidence_id: str}
    all_gates_pass: bool = False

    # Probabilistic forecast
    p_positive_cm2_30d: Optional[float] = None  # P(CM2 > 0, 30d)
    expected_cm2: Optional[float] = None
    p10_cm2: Optional[float] = None  # 10th percentile (worst realistic case)
    maximum_test_loss: Optional[float] = None

    # Uncertainty
    uncertainty_by_variable: dict = Field(default_factory=dict)
    # e.g. {"cpc": 0.4, "cvr": 0.3, "supplier_margin": 0.2}

    # Economics
    expected_information_value: Optional[float] = None
    test_cost: Optional[float] = None
    deployment_cost: Optional[float] = None

    # Evidence
    reasons_for: list[dict] = Field(default_factory=list)
    # Each: {evidence_id: str, reason: str, weight: float}
    reasons_against: list[dict] = Field(default_factory=list)

    # Next action
    next_best_test: Optional[str] = None
    next_best_test_evi: Optional[float] = None

    # Decision
    decision: DecisionType = DecisionType.RESEARCH
    decision_rationale: str = ""

    # Metadata
    agent_id: Optional[str] = None
    policy_id: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"frozen": True}  # Immutable after creation


class BuildDecisionRequest(BaseModel):
    """Request to evaluate a build decision.

    This is what the portfolio planner sends to the decision engine.
    """

    request_id: str = Field(default_factory=lambda: f"BDR-{uuid.uuid4().hex[:12]}")

    # Available candidates
    candidate_ids: list[str] = Field(default_factory=list)

    # Constraints
    capital_limit: float = 100.0  # EUR/GBP/NOK
    time_limit_days: int = 30
    risk_tolerance: str = "conservative"  # conservative, moderate, aggressive

    # Context
    country_codes: list[str] = Field(default_factory=list)
    ecosystem_filter: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class BuildDecisionResponse(BaseModel):
    """Response from the decision engine.

    Contains the decision and all supporting evidence.
    """

    response_id: str = Field(default_factory=lambda: f"BDR-{uuid.uuid4().hex[:12]}")
    request_id: str

    # The decision
    decision: BuildDecision

    # All candidates evaluated
    candidates_evaluated: list[str] = Field(default_factory=list)
    candidates_rejected: list[dict] = Field(default_factory=list)
    # Each: {candidate_id: str, reason: str, evidence_id: str}

    # Portfolio context
    active_experiments: int = 0
    remaining_budget: float = 0.0

    # Metadata
    evaluation_time_ms: Optional[float] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
