#!/usr/bin/env python3
"""
Unified Scoring Pipeline
========================
ONE canonical scoring system. All other scoring is deprecated.

Uses:
- Hierarchical empirical priors (bayesian_v2.py)
- Evidence-preserving data model
- Exact Beta calculations
- Monte Carlo profit simulation

Input: Candidate dict with evidence fields
Output: Decision with posterior statistics
"""

import sys
import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from pathlib import Path

# Add scoring package to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "packages" / "scoring"))
from bayesian_v2 import (
    EvidenceObservation, EvidenceType, CandidateBeliefs,
    hierarchical_cvr_prior, update_cvr_posterior, cvr_posterior_stats,
    profit_per_click_distribution, clicks_needed_for_observations,
    decision_from_posteriors
)


@dataclass
class ScoredCandidate:
    """Result of scoring a candidate."""
    cand_id: str
    name: str
    country: str
    
    # Input evidence (all should be EvidenceObservation, not raw numbers)
    cvr_observations: list = field(default_factory=list)
    cpc_observations: list = field(default_factory=list)
    margin_observations: list = field(default_factory=list)
    
    # Posterior beliefs
    beliefs: CandidateBeliefs = field(default_factory=CandidateBeliefs)
    
    # Economic simulation
    ppc_stats: dict = field(default_factory=dict)
    
    # Decision
    action: str = "UNKNOWN"
    reason: str = ""
    next_experiment: str = ""
    
    # Metadata
    scored_at: str = ""
    scoring_version: str = "2.0"
    

def score_candidate(cand: dict) -> ScoredCandidate:
    """
    Score a candidate using proper Bayesian inference.
    
    Input cand must have:
    - cand_id, name, country
    - OR evidence observations in cvr_observations, cpc_observations, margin_observations
    
    Never invent values. Unknown = EvidenceType.UNKNOWN.
    """
    # Create beliefs from evidence
    beliefs = CandidateBeliefs()
    
    # Process CVR evidence
    prior_alpha, prior_beta = hierarchical_cvr_prior(
        category=cand.get("category", "default"),
        country=cand.get("country", "default")
    )
    
    clicks = 0
    orders = 0
    for obs in cand.get("cvr_observations", []):
        if obs.evidence_type == EvidenceType.MEASURED:
            clicks += int(obs.value)  # clicks observed
        elif obs.evidence_type == EvidenceType.OBSERVED_ZERO:
            orders += 0  # explicitly zero orders
    
    # Update posterior
    beliefs.cvr_alpha, beliefs.cvr_beta = update_cvr_posterior(
        prior_alpha, prior_beta, clicks, orders
    )
    
    # Process CPC evidence
    cpc_values = [obs.value for obs in cand.get("cpc_observations", []) 
                  if obs.evidence_type in (EvidenceType.MEASURED, EvidenceType.ESTIMATED)]
    if cpc_values:
        beliefs.cpc_mean = sum(cpc_values) / len(cpc_values)
        beliefs.cpc_std = max(0.1, beliefs.cpc_mean * 0.3)  # 30% uncertainty
    
    # Process margin evidence
    margin_values = [obs.value for obs in cand.get("margin_observations", []) 
                     if obs.evidence_type in (EvidenceType.MEASURED, EvidenceType.ESTIMATED)]
    if margin_values:
        beliefs.margin_mean = sum(margin_values) / len(margin_values)
        beliefs.margin_std = max(1.0, beliefs.margin_mean * 0.2)  # 20% uncertainty
    
    # Run economic simulation
    ppc_stats = profit_per_click_distribution(
        beliefs.cvr_alpha, beliefs.cvr_beta,
        beliefs.margin_mean, beliefs.margin_std,
        beliefs.cpc_mean, beliefs.cpc_std
    )
    
    # Make decision
    decision = decision_from_posteriors(beliefs)
    
    return ScoredCandidate(
        cand_id=cand.get("cand_id", "unknown"),
        name=cand.get("name", "unknown"),
        country=cand.get("country", "unknown"),
        beliefs=beliefs,
        ppc_stats=ppc_stats,
        action=decision["action"],
        reason=decision["reason"],
        next_experiment=decision.get("next_experiment", ""),
        scored_at=datetime.now().isoformat()
    )


def score_all(candidates_file: str) -> list:
    """Score all candidates from a JSON file."""
    from datetime import datetime
    
    with open(candidates_file) as f:
        candidates = json.load(f)
    
    scored = []
    for cand in candidates:
        try:
            s = score_candidate(cand)
            scored.append(s)
        except Exception as e:
            print(f"Error scoring {cand.get('name', '?')}: {e}")
    
    # Sort by expected profit
    scored.sort(key=lambda x: x.ppc_stats.get("mean", 0), reverse=True)
    
    return scored


if __name__ == "__main__":
    from datetime import datetime
    
    print("=== Unified Scoring Pipeline v2 ===\n")
    
    # Example: Davis weather station with real data
    candidate = {
        "cand_id": "DAVIS-NO",
        "name": "Davis Weather Stations Norway",
        "country": "NO",
        "category": "high_ticket_technical",
        "cvr_observations": [
            EvidenceObservation(100, EvidenceType.MEASURED, "prisjakt", "2026-09-07", 0.8, "organic"),
        ],
        "cpc_observations": [
            EvidenceObservation(5.0, EvidenceType.ESTIMATED, "keyword_planner_proxy", "2026-09-07", 0.5, "estimated"),
        ],
        "margin_observations": [
            EvidenceObservation(2000, EvidenceType.ESTIMATED, "price_gap_analysis", "2026-09-07", 0.6, "estimated"),
        ],
    }
    
    result = score_candidate(candidate)
    
    print(f"Candidate: {result.name}")
    print(f"Country: {result.country}")
    print(f"\nPosterior CVR: Beta({result.beliefs.cvr_alpha:.1f}, {result.beliefs.cvr_beta:.1f})")
    print(f"  Mean: {result.beliefs.cvr_alpha/(result.beliefs.cvr_alpha+result.beliefs.cvr_beta):.4f}")
    print(f"\nProfit/Click Distribution:")
    for k, v in result.ppc_stats.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.4f}")
        else:
            print(f"  {k}: {v}")
    print(f"\nDecision: {result.action}")
    print(f"Reason: {result.reason}")
    print(f"Next experiment: {result.next_experiment}")
