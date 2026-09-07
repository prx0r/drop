"""Mechanism schema.

A mechanism is a causal pattern that produces commercial demand.
Every experiment updates a mechanism belief, not merely a product score.

Mechanisms are discovered from probes, not hard-coded.
They compound over time as evidence accumulates.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MechanismType(str, Enum):
    """Known mechanism families."""
    INSTALLED_BASE_LIFECYCLE = "installed_base_lifecycle"
    COMPATIBILITY_COMPLEXITY = "compatibility_complexity"
    REMOTE_PROPERTY_PROBLEM = "remote_property_problem"
    CLIMATIC_STRESS = "climatic_stress"
    REGULATORY_TRANSITION = "regulatory_transition"
    CONSUMABLE_REPLENISHMENT = "consumable_replenishment"
    SOFTWARE_PLATFORM_EOL = "software_platform_eol"
    MERCHANT_FRAGMENTATION = "merchant_fragmentation"
    CROSS_BORDER_SUPPLY_GAP = "cross_border_supply_gap"
    DIAGNOSTIC_GAP = "diagnostic_gap"
    DECISION_SUPPORT_DEFICIT = "decision_support_deficit"
    UNKNOWN = "unknown"


class Mechanism(BaseModel):
    """A causal pattern that produces commercial demand.

    Every experiment updates a mechanism belief, not merely a product score.
    After 20-50 campaigns, mechanism beliefs compound into real intelligence.
    """

    mechanism_id: str = Field(default_factory=lambda: f"MECH-{uuid.uuid4().hex[:12]}")
    mechanism_type: MechanismType

    # Description
    name: str  # e.g. "installed_base_lifecycle"
    description: str  # What this mechanism does
    canonical_form: str  # Abstract representation

    # Example (from real probe)
    example_product: Optional[str] = None
    example_country: Optional[str] = None
    example_evidence: list[str] = Field(default_factory=list)
    # Evidence IDs that support this mechanism

    # Belief state
    belief_strength: float = 0.5  # 0-1, how strong is this mechanism?
    evidence_count: int = 0
    last_updated: Optional[datetime] = None

    # Cross-country transfer
    countries_observed: list[str] = Field(default_factory=list)
    # Which countries have we seen this mechanism in?

    transfer_confidence: float = 0.5  # 0-1, how well does this transfer?

    # Metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"frozen": True}  # Immutable after creation


class MechanismLibrary(BaseModel):
    """Collection of all discovered mechanisms.

    This is the growing intelligence that compounds over time.
    """

    library_id: str = Field(default_factory=lambda: f"ML-{uuid.uuid4().hex[:12]}")
    mechanisms: list[Mechanism] = Field(default_factory=list)

    # Statistics
    total_mechanisms: int = 0
    total_evidence: int = 0
    countries_covered: list[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def add_mechanism(self, mechanism: Mechanism) -> None:
        """Add a mechanism to the library."""
        self.mechanisms.append(mechanism)
        self.total_mechanisms = len(self.mechanisms)
        self.updated_at = datetime.now(timezone.utc)

    def get_by_type(self, mechanism_type: MechanismType) -> list[Mechanism]:
        """Get all mechanisms of a given type."""
        return [m for m in self.mechanisms if m.mechanism_type == mechanism_type]

    def get_by_country(self, country_code: str) -> list[Mechanism]:
        """Get all mechanisms observed in a country."""
        return [m for m in self.mechanisms if country_code in m.countries_observed]

    def get_strongest(self, n: int = 10) -> list[Mechanism]:
        """Get the N strongest mechanisms."""
        return sorted(self.mechanisms, key=lambda m: m.belief_strength, reverse=True)[:n]
