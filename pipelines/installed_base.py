"""Installed-base lifecycle subsystem.

Tracks large physical systems and their recurring economic events.
The structural data generates the hypothesis.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class InstalledBaseSubsystem(BaseModel):
    """A subsystem tracking installed base lifecycle."""

    system_id: str = Field(default_factory=lambda: f"IB-{uuid.uuid4().hex[:12]}")
    country_code: str
    system_type: str  # "heat_pump", "cottage", "ev", "sauna"
    
    # Core metrics
    installed_base: int  # Number of units
    annual_sales: int  # New units per year
    avg_age_years: Optional[float] = None
    replacement_cycle_years: Optional[float] = None
    warranty_years: Optional[float] = None
    
    # Lifecycle events
    failure_modes: list[str] = Field(default_factory=list)
    accessories: list[str] = Field(default_factory=list)
    compatibility_requirements: list[str] = Field(default_factory=list)
    service_network: str = "limited"
    
    # Economic potential
    annual_replacement_value: Optional[float] = None
    annual_accessory_value: Optional[float] = None
    annual_service_value: Optional[float] = None
    
    # Source
    source_url: Optional[str] = None
    source_year: Optional[int] = None
    confidence: float = 0.5
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LifecycleEvent(BaseModel):
    """A recurring economic event triggered by installed base."""

    event_id: str = Field(default_factory=lambda: f"LE-{uuid.uuid4().hex[:12]}")
    installed_base_id: str
    event_type: str  # "replacement", "maintenance", "upgrade", "failure"
    trigger: str  # "age", "warranty_expiry", "season", "regulation"
    frequency: str  # "annual", "every_5_years", "one_time"
    commercial_needs: list[str]  # What the customer needs to buy
    average_spend: Optional[float] = None
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class InstalledBasePipeline:
    """Generates hypotheses from installed base data."""

    def generate_hypotheses(
        self,
        installed_bases: list[InstalledBaseSubsystem],
    ) -> list[dict]:
        """Generate hypotheses from installed base intersections."""
        hypotheses = []
        
        for base in installed_bases:
            # Generate lifecycle hypotheses
            for event_type in ["replacement", "maintenance", "upgrade", "failure"]:
                for need in base.accessories:
                    hypothesis = {
                        "country": base.country_code,
                        "system_type": base.system_type,
                        "event_type": event_type,
                        "need": need,
                        "installed_base": base.installed_base,
                        "annual_sales": base.annual_sales,
                        "commercial_need": f"{base.system_type}_{event_type}_{need}",
                        "mechanism": f"{event_type}_of_{need}_in_{base.system_type}",
                    }
                    hypotheses.append(hypothesis)
        
        return hypotheses

    def generate_cross_system_hypotheses(
        self,
        installed_bases: list[InstalledBaseSubsystem],
    ) -> list[dict]:
        """Generate hypotheses from intersections of multiple installed bases."""
        hypotheses = []
        
        # Find systems that share compatibility requirements
        for i, base1 in enumerate(installed_bases):
            for base2 in installed_bases[i+1:]:
                shared = set(base1.compatibility_requirements) & set(base2.compatibility_requirements)
                if shared:
                    hypothesis = {
                        "country": base1.country_code,
                        "systems": [base1.system_type, base2.system_type],
                        "shared_requirements": list(shared),
                        "mechanism": f"compatibility_{base1.system_type}_{base2.system_type}",
                        "installed_base_product": base1.installed_base * base2.installed_base,
                    }
                    hypotheses.append(hypothesis)
        
        return hypotheses
