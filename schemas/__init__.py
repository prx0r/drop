"""Canonical schemas for the Drop intelligence system.

These are the single source of truth for all data structures.
Pipelines consume and produce these types. Storage layer handles persistence.

Design principles:
- Every field is typed (no raw dicts)
- Every entity has a stable ID
- Every entity has created_at / updated_at
- Unknowns are first-class objects, not nulls
- State machines are explicit with valid transitions
"""

from schemas.observation import (
    Observation,
    EvidenceGrade,
    EvidenceSource,
    UnknownField,
)
from schemas.hypothesis import (
    Hypothesis,
    HypothesisState,
    EvidenceUpdate,
    FalsificationResult,
)
from schemas.kernel import (
    Kernel,
    KernelType,
    BeliefDelta,
)
from schemas.candidate import (
    Candidate,
    CandidateState,
    ScoreComponent,
    GateResult,
    GateStatus,
)
from schemas.probe import (
    ProbeResult,
    ProbeOutcome,
    ResearchEVI,
)
from schemas.economics import (
    CostLedger,
    ContributionLevel,
    DecisionEvent,
    DecisionAction,
    FeatureSnapshot,
    EconomicOutcome,
    OutcomeMaturity,
    PolicyAction,
    TreatmentAssignment,
)

__all__ = [
    # Observations
    "Observation",
    "EvidenceGrade",
    "EvidenceSource",
    "UnknownField",
    # Hypotheses
    "Hypothesis",
    "HypothesisState",
    "EvidenceUpdate",
    "FalsificationResult",
    # Kernels
    "Kernel",
    "KernelType",
    "BeliefDelta",
    # Candidates
    "Candidate",
    "CandidateState",
    "ScoreComponent",
    "GateResult",
    "GateStatus",
    # Probes
    "ProbeResult",
    "ProbeOutcome",
    "ResearchEVI",
    # Economics
    "CostLedger",
    "ContributionLevel",
    "DecisionEvent",
    "DecisionAction",
    "FeatureSnapshot",
    "EconomicOutcome",
    "OutcomeMaturity",
    "PolicyAction",
    "TreatmentAssignment",
]
