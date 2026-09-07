#!/usr/bin/env python3
"""
Free Listings as Low-Fidelity Observations
==========================================
Models the relationship between free listing signals and actual paid profitability.

From the critique:
> "Free listings are F0/F1 fidelity observations. They provide evidence but are not gates.
> Google explicitly says eligibility doesn't guarantee exposure."

Multi-fidelity framework:
F0 = SERP / price-comparison / keyword observational evidence
F1 = organic/free-listing impressions + clicks
F2 = controlled paid exact-intent traffic
F3 = store transactions / contribution
F4 = fulfilled contribution after returns/support/RMA
F5 = replicated outcome in another market/store
"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum


class FidelityLevel(Enum):
    """Evidence fidelity levels."""
    F0_OBSERVATIONAL = "F0"  # SERP, price comparison, keyword data
    F1_FREE_LISTINGS = "F1"  # Free listing impressions/clicks
    F2_PAID_TRAFFIC = "F2"   # Controlled paid exact-intent traffic
    F3_TRANSACTION = "F3"    # Store transactions / contribution
    F4_FULFILLED = "F4"      # After returns/support/RMA
    F5_REPLICATED = "F5"     # Replicated in another market


@dataclass
class FreeListingObservation:
    """A free listing observation with fidelity level."""
    fidelity: FidelityLevel
    impressions: int = 0
    clicks: int = 0
    ctr: float = 0.0
    days_observed: int = 0
    source: str = "google_free_listings"
    
    def __post_init__(self):
        if self.impressions > 0 and self.clicks > 0:
            self.ctr = self.clicks / self.impressions


def estimate_paid_from_free(
    free_obs: FreeListingObservation,
    paid_cpc_multiplier: float = 2.0,
    paid_cvr_multiplier: float = 0.5
) -> dict:
    """
    Estimate what paid traffic would look like based on free listing observations.
    
    Free listings have lower intent than paid, so:
    - Paid CPC is typically 2-5x higher than free "CPC" (which is $0)
    - Paid CVR is typically 0.5-2x higher than free CTR
    
    This is a rough approximation, not a precise model.
    """
    if free_obs.clicks == 0:
        return {
            "estimated_paid_clicks": 0,
            "estimated_paid_cvr": 0,
            "estimated_paid_conversions": 0,
            "confidence": 0.0,
            "notes": "No free listing clicks — cannot estimate paid performance"
        }
    
    # Free listing CTR is not the same as paid CVR
    # But it provides a lower bound
    estimated_paid_cvr = free_obs.ctr * paid_cvr_multiplier
    
    return {
        "free_impressions": free_obs.impressions,
        "free_clicks": free_obs.clicks,
        "free_ctr": free_obs.ctr,
        "estimated_paid_cvr": estimated_paid_cvr,
        "estimated_paid_cvr_range": (estimated_paid_cvr * 0.3, estimated_paid_cvr * 3.0),
        "confidence": min(0.3, free_obs.days_observed / 30),  # Low confidence
        "notes": "Free listing evidence is F1 fidelity. Treat as directional, not precise."
    }


if __name__ == "__main__":
    print("=== Free Listings Model Demo ===\n")
    
    # Scenario 1: Good free listing signal
    obs1 = FreeListingObservation(
        fidelity=FidelityLevel.F1_FREE_LISTINGS,
        impressions=5000,
        clicks=150,
        days_observed=14
    )
    result1 = estimate_paid_from_free(obs1)
    print(f"Good signal (5000 imp, 150 clicks):")
    print(f"  Free CTR: {result1['free_ctr']:.2%}")
    print(f"  Estimated paid CVR: {result1['estimated_paid_cvr']:.2%}")
    print(f"  Range: {result1['estimated_paid_cvr_range'][0]:.2%} - {result1['estimated_paid_cvr_range'][1]:.2%}")
    print(f"  Confidence: {result1['confidence']:.0%}")
    
    # Scenario 2: Weak signal
    obs2 = FreeListingObservation(
        fidelity=FidelityLevel.F1_FREE_LISTINGS,
        impressions=500,
        clicks=5,
        days_observed=7
    )
    result2 = estimate_paid_from_free(obs2)
    print(f"\nWeak signal (500 imp, 5 clicks):")
    print(f"  Free CTR: {result2['free_ctr']:.2%}")
    print(f"  Estimated paid CVR: {result2['estimated_paid_cvr']:.2%}")
    print(f"  Confidence: {result2['confidence']:.0%}")
    
    # Scenario 3: No signal
    obs3 = FreeListingObservation(
        fidelity=FidelityLevel.F1_FREE_LISTINGS,
        impressions=0,
        clicks=0,
        days_observed=14
    )
    result3 = estimate_paid_from_free(obs3)
    print(f"\nNo signal (0 imp, 0 clicks):")
    print(f"  {result3['notes']}")
