#!/usr/bin/env python3
"""
Proper Bayesian Inference for Ecommerce CVR
===========================================
Replaces Beta(1,1) with hierarchical empirical priors.
Uses exact Beta calculations, not Gaussian approximations.

This is the canonical inference engine. All scoring must route through here.
"""

import numpy as np
from scipy import stats
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class EvidenceType(Enum):
    """Provenance-preserving evidence classification."""
    UNKNOWN = "unknown"
    OBSERVED_ZERO = "observed_zero"
    ESTIMATED = "estimated"
    MEASURED = "measured"
    DERIVED = "derived"


@dataclass
class EvidenceObservation:
    """Single evidence point with provenance."""
    value: float
    evidence_type: EvidenceType
    source: str
    timestamp: str
    confidence: float  # 0-1, how much we trust this evidence
    independence_group: str  # For accounting correlated evidence


@dataclass
class CandidateBeliefs:
    """Posterior beliefs about a candidate's economics."""
    # CVR posterior (Beta distribution parameters)
    cvr_alpha: float = 1.0
    cvr_beta: float = 1.0
    
    # CPC posterior (normal distribution)
    cpc_mean: float = 0.0
    cpc_std: float = 1.0
    
    # Contribution margin posterior
    margin_mean: float = 0.0
    margin_std: float = 1.0
    
    # Evidence tracking
    observations: List[EvidenceObservation] = None
    
    def __post_init__(self):
        if self.observations is None:
            self.observations = []


def hierarchical_cvr_prior(category: str = "default", country: str = "default") -> tuple:
    """
    Return (alpha, beta) for hierarchical CVR prior.
    
    Based on empirical ecommerce data:
    - High-ticket technical: ~0.3-0.5% CVR
    - Mid-range consumer: ~1-2% CVR
    - Low-ticket impulse: ~2-4% CVR
    
    Prior is weakly informative, centered around realistic values.
    """
    priors = {
        "high_ticket_technical": (0.5, 150),    # mean ~0.33%, very uncertain
        "mid_range_consumer": (2, 200),          # mean ~1%, uncertain
        "low_ticket_impulse": (5, 150),          # mean ~3.3%, uncertain
        "default": (1, 200),                     # mean ~0.5%, very uncertain
    }
    return priors.get(category, priors["default"])


def update_cvr_posterior(prior_alpha: float, prior_beta: float, 
                         clicks: int, orders: int) -> tuple:
    """
    Update CVR posterior with observed data.
    
    Returns (posterior_alpha, posterior_beta).
    """
    return prior_alpha + orders, prior_beta + (clicks - orders)


def cvr_posterior_stats(alpha: float, beta: float) -> dict:
    """Calculate posterior statistics from Beta distribution."""
    dist = stats.beta(alpha, beta)
    
    return {
        "mean": dist.mean(),
        "std": dist.std(),
        "ci_95": (dist.ppf(0.025), dist.ppf(0.975)),
        "p_above_0_001": 1 - dist.cdf(0.001),
        "p_above_0_003": 1 - dist.cdf(0.003),
        "p_above_0_005": 1 - dist.cdf(0.005),
        "p_above_0_01": 1 - dist.cdf(0.01),
    }


def profit_per_click_distribution(
    cvr_alpha: float, cvr_beta: float,
    margin_mean: float, margin_std: float,
    cpc_mean: float, cpc_std: float,
    n_simulations: int = 10000
) -> dict:
    """
    Monte Carlo simulation of profit per click.
    
    Returns distribution of:
    - profit_per_click
    - probability_positive
    - expected_profit
    - value_at_risk (5th percentile)
    """
    # Sample from posteriors
    cvr_samples = np.random.beta(cvr_alpha, cvr_beta, n_simulations)
    margin_samples = np.random.normal(margin_mean, margin_std, n_simulations)
    cpc_samples = np.random.normal(cpc_mean, cpc_std, n_simulations)
    
    # Calculate profit per click for each sample
    profit = cvr_samples * margin_samples - cpc_samples
    
    return {
        "mean": float(np.mean(profit)),
        "std": float(np.std(profit)),
        "p_positive": float(np.mean(profit > 0)),
        "p_negative": float(np.mean(profit < 0)),
        "var_5pct": float(np.percentile(profit, 5)),
        "var_50pct": float(np.percentile(profit, 50)),
        "var_95pct": float(np.percentile(profit, 95)),
        "expected_profit_per_1000_clicks": float(np.mean(profit) * 1000),
    }


def clicks_needed_for_observations(
    prior_alpha: float, prior_beta: float,
    target_cvr: float,
    confidence: float = 0.8
) -> int:
    """
    How many clicks needed to have `confidence` probability of seeing ≥1 order
    if true CVR = target_cvr.
    """
    # P(0 orders | n clicks) = (1 - target_cvr)^n
    # We want P(≥1 order) >= confidence
    # So (1 - target_cvr)^n <= 1 - confidence
    # n >= log(1 - confidence) / log(1 - target_cvr)
    import math
    if target_cvr <= 0:
        return float('inf')
    n = math.log(1 - confidence) / math.log(1 - target_cvr)
    return int(math.ceil(n))


def decision_from_posteriors(
    beliefs: CandidateBeliefs,
    risk_tolerance: float = 0.1
) -> dict:
    """
    Make decision from posterior beliefs.
    
    Returns:
        - action: PROCEED / WAIT / KILL
        - reason: explanation
        - next_experiment: what to do next
        - evsi_next: expected value of next experiment
    """
    # Simulate profit distribution
    ppc = profit_per_click_distribution(
        beliefs.cvr_alpha, beliefs.cvr_beta,
        beliefs.margin_mean, beliefs.margin_std,
        beliefs.cpc_mean, beliefs.cpc_std
    )
    
    # Check minimum data
    total_clicks = beliefs.cvr_alpha + beliefs.cvr_beta - 2  # prior is (1,1) effectively
    if total_clicks < 30:
        return {
            "action": "WAIT",
            "reason": f"Only {total_clicks} clicks observed. Need 30+ for minimum inference.",
            "next_experiment": "Collect more traffic",
            "ppc_stats": ppc
        }
    
    # Check if contribution is plausibly positive
    if ppc["p_positive"] > 0.8:
        return {
            "action": "PROCEED",
            "reason": f"P(profit>0) = {ppc['p_positive']:.1%}. Expected profit/click = €{ppc['mean']:.2f}",
            "next_experiment": "Scale cautiously",
            "ppc_stats": ppc
        }
    elif ppc["p_positive"] > 0.5:
        return {
            "action": "WAIT",
            "reason": f"P(profit>0) = {ppc['p_positive']:.1%}. Uncertain. Need more data.",
            "next_experiment": "Collect 100+ more qualified clicks",
            "ppc_stats": ppc
        }
    else:
        return {
            "action": "KILL",
            "reason": f"P(profit>0) = {ppc['p_positive']:.1%}. Economics unlikely to work.",
            "next_experiment": "None — thesis falsified",
            "ppc_stats": ppc
        }


# --- Example usage ---
if __name__ == "__main__":
    print("=== Bayesian CVR Inference Demo ===\n")
    
    # Scenario: 100 clicks, 0 orders (the dangerous case)
    prior_alpha, prior_beta = hierarchical_cvr_prior("high_ticket_technical")
    print(f"Prior: Beta({prior_alpha}, {prior_beta}) — mean = {prior_alpha/(prior_alpha+prior_beta):.3f}")
    
    posterior_alpha, posterior_beta = update_cvr_posterior(prior_alpha, prior_beta, 100, 0)
    print(f"After 100 clicks, 0 orders: Beta({posterior_alpha}, {posterior_beta})")
    
    stats = cvr_posterior_stats(posterior_alpha, posterior_beta)
    print(f"Posterior mean: {stats['mean']:.4f}")
    print(f"95% CI: ({stats['ci_95'][0]:.4f}, {stats['ci_95'][1]:.4f})")
    print(f"P(CVR > 0.1%): {stats['p_above_0_001']:.1%}")
    print(f"P(CVR > 0.3%): {stats['p_above_0_003']:.1%}")
    print(f"P(CVR > 0.5%): {stats['p_above_0_005']:.1%}")
    
    # Compare with old Beta(1,1)
    print(f"\n--- Comparison with Beta(1,1) ---")
    old_alpha, old_beta = 1, 1
    old_stats = cvr_posterior_stats(old_alpha + 0, old_beta + 100)
    print(f"Old prior Beta(1,1): posterior mean = {old_stats['mean']:.4f}")
    print(f"P(CVR > 0.3%): {old_stats['p_above_0_003']:.1%} ← THIS IS THE BUG")
    
    # Clicks needed
    print(f"\n--- Clicks needed for 80% chance of 1 order at 0.3% CVR ---")
    n = clicks_needed_for_observations(prior_alpha, prior_beta, 0.003, 0.8)
    print(f"Need {n} clicks")
