"""Market-intelligence kernel schema.

A Kernel is the atomic output of a probe.
It is a structured fact that changes our belief about a candidate.

One kernel is worth more than 2,000 words of market commentary.

Example:
{
  "kernel_id": "K-20260907-TESTO-NO-003",
  "candidate_id": "NO-TESTO-550S-001",
  "hypothesis": "Norway has sparse specialist Testo 550s retail",
  "new_observation": {
    "fact": "Testo Norway routes through Max Sievert A-S",
    "source_grade": "A"
  },
  "belief_delta": "STRONGLY_AGAINST",
  "mechanism": "weak public exact-SKU indexing caused by hidden professional distribution",
  "generalisable_rule": "professional-product public SERP scarcity must be checked against trade/distributor networks",
  "novelty_type": "MECHANISM_DISCOVERY",
  "information_gain": "HIGH"
}
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class KernelType(str, Enum):
    """What kind of intelligence does this kernel contain?

    This is the ontology of market-intelligence kernels.
    We can query: "Show me every GENERALISABLE_MECHANISM learned across 500 probes."
    """

    # Demand
    DEMAND_DISCOVERY = "DEMAND_DISCOVERY"
    DEMAND_FALSIFICATION = "DEMAND_FALSIFICATION"

    # Merchant
    MERCHANT_GAP_DISCOVERY = "MERCHANT_GAP_DISCOVERY"
    MERCHANT_GAP_FALSIFICATION = "MERCHANT_GAP_FALSIFICATION"

    # Hidden channels
    HIDDEN_CHANNEL_DISCOVERY = "HIDDEN_CHANNEL_DISCOVERY"

    # Supply
    SUPPLIER_PATH_DISCOVERY = "SUPPLIER_PATH_DISCOVERY"
    SUPPLIER_PATH_FAILURE = "SUPPLIER_PATH_FAILURE"

    # Economics
    MARGIN_THRESHOLD = "MARGIN_THRESHOLD"
    PRICE_COMPRESSION = "PRICE_COMPRESSION"
    SATURATION_ACCELERATION = "SATURATION_ACCELERATION"

    # Content vs Commerce
    CONTENT_NOT_COMMERCE = "CONTENT_NOT_COMMERCE"

    # Risk
    SUPPORT_BURDEN = "SUPPORT_BURDEN"
    RETURN_RISK = "RETURN_RISK"
    WARRANTY_RISK = "WARRANTY_RISK"

    # Cross-market
    SOURCE_MARKET_PROOF = "SOURCE_MARKET_PROOF"
    TARGET_MARKET_ASYMMETRY = "TARGET_MARKET_ASYMMETRY"

    # Regulatory
    REGULATORY_BLOCKER = "REGULATORY_BLOCKER"

    # Action required
    HUMAN_ACTION_REQUIRED = "HUMAN_ACTION_REQUIRED"

    # Store probe
    STORE_PROBE_RESULT = "STORE_PROBE_RESULT"

    # Learning
    GENERALISABLE_MECHANISM = "GENERALISABLE_MECHANISM"


class BeliefDelta(str, Enum):
    """How did this kernel change our belief?

    Strongly supporting = STRONGLY_FOR
    Strongly weakening = STRONGLY_AGAINST
    """

    STRONGLY_FOR = "STRONGLY_FOR"
    MODERATELY_FOR = "MODERATELY_FOR"
    NEUTRAL = "NEUTRAL"
    MODERATELY_AGAINST = "MODERATELY_AGAINST"
    STRONGLY_AGAINST = "STRONGLY_AGAINST"


class Kernel(BaseModel):
    """A market-intelligence kernel.

    The atomic output of a probe. One kernel is one structured fact
    that changes our belief about a candidate.

    Every kernel answers:
    1. What exact hypothesis was tested?
    2. What new fact was observed?
    3. Did it support or weaken the hypothesis?
    4. What decision changed?
    5. What is the single most valuable unknown now?
    6. What general rule did this teach us?
    """

    kernel_id: str = Field(default_factory=lambda: f"K-{uuid.uuid4().hex[:12]}")

    # What was tested?
    hypothesis_id: Optional[str] = None
    hypothesis: str  # The hypothesis in plain language
    candidate_id: Optional[str] = None

    # What was observed?
    new_observation: dict = Field(default_factory=dict)
    # Expected keys: "fact", "source_grade", "source_url", "source_name"

    # How did it change our belief?
    belief_delta: BeliefDelta
    belief_delta_magnitude: Optional[float] = None  # 0-1, how much did belief change?

    # What mechanism explains this?
    mechanism: Optional[str] = None  # Why did this happen?

    # State transition
    state_before: Optional[str] = None
    state_after: Optional[str] = None

    # What was resolved?
    resolved_fields: list[str] = Field(default_factory=list)

    # What's still unknown?
    remaining_decisive_unknown: Optional[str] = None

    # What would falsify the opposite?
    falsification_effect: Optional[str] = None

    # What should we do next?
    next_best_test: Optional[str] = None

    # Decision thresholds
    decision_threshold: Optional[dict] = None
    # Expected keys: "field", "threshold_value", "unit", "comparison"

    # Learning
    generalisable_rule: Optional[str] = None  # What did this teach us?

    # Classification
    kernel_type: KernelType = KernelType.DEMAND_DISCOVERY
    novelty_type: Optional[str] = None  # e.g. "MECHANISM_DISCOVERY"
    information_gain: Optional[str] = None  # "HIGH", "MEDIUM", "LOW"

    # Source provenance
    probe_id: Optional[str] = None
    source_urls: list[str] = Field(default_factory=list)
    source_grades: list[str] = Field(default_factory=list)

    # Temporal
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"frozen": True}  # Kernels are immutable
