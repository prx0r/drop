"""Hypothesis ledger schema.

A Hypothesis is a testable claim about the world.
It has a falsifier. It has evidence for and against.
It has a state (OPEN, SUPPORTED, FALSIFIED, etc.).

Key principle: every hypothesis must have an explicit null hypothesis.

Example:
    H1: Norway has sparse specialist Testo 550s retail
    H0: Apparent scarcity is caused by hidden B2B distribution

The probe must search for evidence of H0, not just H1.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class HypothesisState(str, Enum):
    """Lifecycle of a hypothesis."""

    OPEN = "OPEN"  # Actively being tested
    SUPPORTED = "SUPPORTED"  # Evidence supports, but not yet confirmed
    STRONGLY_SUPPORTED = "STRONGLY_SUPPORTED"  # Strong evidence, ready for experiment
    FALSIFIED = "FALSIFIED"  # Evidence contradicts
    INCONCLUSIVE = "INCONCLUSIVE"  # Evidence is mixed
    EXTERNALLY_BLOCKED = "EXTERNALLY_BLOCKED"  # Cannot resolve without external action
    SUPERSEDED = "SUPERSEDED"  # Replaced by a better hypothesis


class EvidenceDirection(str, Enum):
    """Does this evidence support or weaken the hypothesis?"""

    FOR = "FOR"
    AGAINST = "AGAINST"
    NEUTRAL = "NEUTRAL"


class EvidenceStrength(str, Enum):
    """How strong is this evidence?"""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class EvidenceUpdate(BaseModel):
    """A piece of evidence mapped to a hypothesis.

    This is how observations become hypothesis updates.
    """

    update_id: str = Field(default_factory=lambda: f"EU-{uuid.uuid4().hex[:12]}")
    hypothesis_id: str
    observation_id: str

    direction: EvidenceDirection
    strength: EvidenceStrength
    reason: str  # Why does this evidence support/weaken the hypothesis?

    # Independence tracking
    independence_cluster: Optional[str] = None
    independent_source_count: int = 1

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FalsificationResult(BaseModel):
    """Result of a falsification attempt.

    Did the probe find evidence that kills this hypothesis?
    """

    hypothesis_id: str
    is_falsified: bool
    confidence: float  # 0-1, how confident are we in the falsification?
    evidence_summary: str  # What evidence killed it?
    alternative_explanation: Optional[str] = None  # What else could explain the data?
    generalisable_rule: Optional[str] = None  # What did this teach us?


class Hypothesis(BaseModel):
    """A testable claim about the world.

    Every hypothesis has:
    - A claim (what we think is true)
    - A null hypothesis (what would explain the data without our claim)
    - A falsifier (what would prove us wrong)
    - Evidence for and against
    - A state (open, supported, falsified)
    """

    hypothesis_id: str = Field(default_factory=lambda: f"H-{uuid.uuid4().hex[:12]}")

    # The claim
    claim: str
    null_hypothesis: str  # What would explain the data WITHOUT our claim?
    falsifier: str  # What evidence would kill this hypothesis?

    # Context
    candidate_id: Optional[str] = None
    product_family: Optional[str] = None
    country_code: Optional[str] = None
    probe_id: Optional[str] = None

    # Source
    generated_from: list[str] = Field(default_factory=list)  # What anomalies generated this?

    # Evidence tracking
    evidence_for: list[str] = Field(default_factory=list)  # observation_ids
    evidence_against: list[str] = Field(default_factory=list)  # observation_ids
    independent_source_count: int = 0  # How many independent sources?

    # State
    state: HypothesisState = HypothesisState.OPEN
    confidence: float = 0.5  # 0-1, prior probability

    # Resolution
    resolved_fields: list[str] = Field(default_factory=list)  # Fields this hypothesis resolved
    remaining_unknowns: list[str] = Field(default_factory=list)  # Fields still unknown

    # Next action
    next_best_test: Optional[str] = None
    evi: Optional[float] = None  # Expected Value of Information

    # Temporal
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    resolved_at: Optional[datetime] = None

    # Learning
    generalisable_rule: Optional[str] = None  # What did this teach us?

    def add_evidence_for(self, observation_id: str) -> None:
        """Add supporting evidence."""
        if observation_id not in self.evidence_for:
            self.evidence_for.append(observation_id)
            self.updated_at = datetime.now(timezone.utc)

    def add_evidence_against(self, observation_id: str) -> None:
        """Add contradicting evidence."""
        if observation_id not in self.evidence_against:
            self.evidence_against.append(observation_id)
            self.updated_at = datetime.now(timezone.utc)

    def falsify(self, reason: str, confidence: float = 1.0) -> FalsificationResult:
        """Falsify this hypothesis."""
        self.state = HypothesisState.FALSIFIED
        self.resolved_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

        return FalsificationResult(
            hypothesis_id=self.hypothesis_id,
            is_falsified=True,
            confidence=confidence,
            evidence_summary=reason,
        )

    def support(self, confidence: float = 0.7) -> None:
        """Support this hypothesis."""
        if confidence >= 0.9:
            self.state = HypothesisState.STRONGLY_SUPPORTED
        elif confidence >= 0.6:
            self.state = HypothesisState.SUPPORTED
        self.updated_at = datetime.now(timezone.utc)

    @property
    def support_ratio(self) -> float:
        """Ratio of supporting to total evidence. 0.5 = neutral."""
        total = len(self.evidence_for) + len(self.evidence_against)
        if total == 0:
            return 0.5
        return len(self.evidence_for) / total

    @property
    def is_resolved(self) -> bool:
        """Is this hypothesis in a terminal state?"""
        return self.state in {
            HypothesisState.FALSIFIED,
            HypothesisState.SUPERSEDED,
        }
