"""Probe result schema.

A ProbeResult is the output of a probe run.
It contains observations, kernels, and metadata about the probe.

Probes are hypothesis tests. Each probe run:
1. Takes a hypothesis
2. Searches for evidence
3. Produces observations
4. Maps observations to hypothesis updates
5. Generates kernels (market-intelligence facts)
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from schemas.observation import Observation
from schemas.kernel import Kernel, KernelType, BeliefDelta
from schemas.hypothesis import Hypothesis, HypothesisState


class ProbeOutcome(str, Enum):
    """What happened in this probe run?"""

    NO_MATERIAL_INFORMATION_GAIN = "NO_MATERIAL_INFORMATION_GAIN"
    HYPOTHESIS_SUPPORTED = "HYPOTHESIS_SUPPORTED"
    HYPOTHESIS_FALSIFIED = "HYPOTHESIS_FALSIFIED"
    HYPOTHESIS_STRENGTHENED = "HYPOTHESIS_STRENGTHENED"
    HYPOTHESIS_WEAKENED = "HYPOTHESIS_WEAKENED"
    NEW_HYPOTHESIS = "NEW_HYPOTHESIS"
    CANDIDATE_ADVANCED = "CANDIDATE_ADVANCED"
    CANDIDATE_KILLED = "CANDIDATE_KILLED"
    CANDIDATE_FROZEN = "CANDIDATE_FROZEN"
    BLOCKER_RESOLVED = "BLOCKER_RESOLVED"
    HUMAN_ACTION_REQUIRED = "HUMAN_ACTION_REQUIRED"


class ResearchEVI(BaseModel):
    """Expected Value of Information for a research action.

    EVI = P(resolve) * decision_impact * candidate_value / research_cost

    Higher EVI = more valuable to research next.
    """

    field: str  # What unknown would this resolve?
    candidate_id: Optional[str] = None
    hypothesis_id: Optional[str] = None

    probability_of_resolve: float  # 0-1
    decision_impact: float  # 0-1, how much does this change the decision?
    candidate_value: float  # 0-1, how valuable is this candidate?
    research_cost: float  # 0-1, how expensive is this research?

    @property
    def evi(self) -> float:
        """Calculate EVI."""
        if self.research_cost == 0:
            return float("inf")
        return (
            self.probability_of_resolve
            * self.decision_impact
            * self.candidate_value
            / self.research_cost
        )

    recommended_action: str  # e.g. "email supplier", "check SERP", "scrape retailer"
    rationale: str  # Why is this the best next action?


class ProbeResult(BaseModel):
    """The output of a single probe run.

    This is what a probe produces. It contains:
    - Observations (atomic facts)
    - Kernels (market-intelligence facts)
    - Hypothesis updates
    - Metadata about the probe run
    """

    probe_id: str
    probe_name: str
    run_id: str = Field(default_factory=lambda: f"RUN-{uuid.uuid4().hex[:12]}")

    # What was tested?
    hypothesis_id: Optional[str] = None
    candidate_id: Optional[str] = None

    # What did we find?
    observations: list[Observation] = Field(default_factory=list)
    kernels: list[Kernel] = Field(default_factory=list)

    # Hypothesis updates
    hypothesis_state_before: Optional[HypothesisState] = None
    hypothesis_state_after: Optional[HypothesisState] = None
    support_ratio_before: Optional[float] = None
    support_ratio_after: Optional[float] = None

    # Outcome
    outcome: ProbeOutcome = ProbeOutcome.NO_MATERIAL_INFORMATION_GAIN
    outcome_rationale: str = ""

    # What's still unknown?
    remaining_unknowns: list[str] = Field(default_factory=list)

    # What should we do next?
    next_best_test: Optional[str] = None
    evi_rankings: list[ResearchEVI] = Field(default_factory=list)

    # Research accounting
    queries_made: int = 0
    sources_checked: int = 0
    material_information_gains: int = 0  # How many observations actually changed belief?

    # Freshness
    novelty_score: Optional[float] = None  # 0-1

    # Temporal
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None

    # Source tracking
    source_classes_used: list[str] = Field(default_factory=list)
    # e.g. ["prisjakt", "retailer_site", "forum"]

    model_config = {"frozen": True}  # Probe results are immutable

    @property
    def duration_seconds(self) -> Optional[float]:
        """How long did this probe run?"""
        if self.completed_at is None:
            return None
        return (self.completed_at - self.started_at).total_seconds()

    @property
    def efficiency(self) -> float:
        """Material information gains per query made. Higher = more efficient."""
        if self.queries_made == 0:
            return 0.0
        return self.material_information_gains / self.queries_made
