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

__all__ = [
    "Observation",
    "EvidenceGrade",
    "EvidenceSource",
    "UnknownField",
    "Hypothesis",
    "HypothesisState",
    "EvidenceUpdate",
    "FalsificationResult",
    "Kernel",
    "KernelType",
    "BeliefDelta",
    "Candidate",
    "CandidateState",
    "ScoreComponent",
    "GateResult",
    "GateStatus",
    "ProbeResult",
    "ProbeOutcome",
    "ResearchEVI",
]
