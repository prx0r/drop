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
from schemas.campaign import (
    CampaignHypothesis,
    LaunchSpec,
    Deployment,
    ActivationGate,
    CampaignState,
)
from schemas.decision import (
    BuildDecision,
    DecisionType,
    BuildDecisionRequest,
    BuildDecisionResponse,
)
from schemas.mechanism import (
    Mechanism,
    MechanismType,
    MechanismLibrary,
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
    # Campaign
    "CampaignHypothesis",
    "LaunchSpec",
    "Deployment",
    "ActivationGate",
    "CampaignState",
    # Decision
    "BuildDecision",
    "DecisionType",
    "BuildDecisionRequest",
    "BuildDecisionResponse",
    # Mechanism
    "Mechanism",
    "MechanismType",
    "MechanismLibrary",
]
