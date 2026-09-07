"""
Bayesian Evidence Model — Beta-Binomial posterior for CVR.
Answers: P(actual_CVR > break_even_CVR | observed_data)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple
import math


@dataclass
class BayesianPosterior:
    """Beta-Binomial posterior for conversion rate estimation."""
    # Prior parameters (weak prior: Beta(1, 1) = uniform)
    prior_alpha: float = 1.0
    prior_beta: float = 1.0

    # Observed data
    clicks: int = 0
    orders: int = 0

    # Posterior parameters
    posterior_alpha: float = 1.0
    posterior_beta: float = 1.0

    # Derived quantities
    posterior_mean_cvr: float = 0.0
    credible_interval_low: float = 0.0  # 5th percentile
    credible_interval_high: float = 0.0  # 95th percentile

    # Decision quantities
    probability_above_break_even: float = 0.0
    probability_zero_sales_if_viable: float = 0.0

    # Decision bands
    decision: str = ""  # STRONGLY_PROMISING, PROMISING, UNCERTAIN, WEAK, STRONG_EVIDENCE_AGAINST

    def __post_init__(self):
        self._update_posterior()

    def _update_posterior(self):
        """Recalculate posterior from data."""
        self.posterior_alpha = self.prior_alpha + self.orders
        self.posterior_beta = self.prior_beta + (self.clicks - self.orders)

        # Posterior mean
        self.posterior_mean_cvr = (
            self.posterior_alpha / (self.posterior_alpha + self.posterior_beta)
        )

        # Credible interval using Beta distribution approximation
        # For large enough alpha/beta, use normal approximation
        total = self.posterior_alpha + self.posterior_beta
        if total > 20:
            mean = self.posterior_alpha / total
            std = math.sqrt(
                (self.posterior_alpha * self.posterior_beta) /
                (total ** 2 * (total + 1))
            )
            # 90% credible interval (5th to 95th percentile)
            self.credible_interval_low = max(0.0, mean - 1.645 * std)
            self.credible_interval_high = min(1.0, mean + 1.645 * std)
        else:
            # For small samples, use wider interval
            self.credible_interval_low = 0.0
            self.credible_interval_high = min(1.0, self.posterior_mean_cvr * 3)

    def probability_above(self, threshold: float) -> float:
        """
        P(CVR > threshold | data) using regularized incomplete beta function.
        For practical purposes, use normal approximation when possible.
        """
        if self.clicks == 0:
            # No data: prior only
            total = self.prior_alpha + self.prior_beta
            mean = self.prior_alpha / total
            std = math.sqrt(
                (self.prior_alpha * self.prior_beta) /
                (total ** 2 * (total + 1))
            )
        else:
            total = self.posterior_alpha + self.posterior_beta
            mean = self.posterior_alpha / total
            std = math.sqrt(
                (self.posterior_alpha * self.posterior_beta) /
                (total ** 2 * (total + 1))
            )

        if std == 0:
            return 1.0 if mean > threshold else 0.0

        # P(X > threshold) using normal approximation
        z = (threshold - mean) / std
        # Standard normal CDF approximation
        p_below = 0.5 * (1 + math.erf(z / math.sqrt(2)))
        return 1.0 - p_below

    def probability_zero_sales(self, viable_cvr: float) -> float:
        """
        P(0 sales | viable_cvr) = (1 - viable_cvr)^clicks
        This is the key formula that shows why '100 clicks then kill' is often wrong.
        """
        if self.clicks == 0:
            return 1.0
        return (1 - viable_cvr) ** self.clicks

    def decide(self, break_even_cvr: float) -> str:
        """Make a decision based on P(CVR > break_even)."""
        p = self.probability_above(break_even_cvr)
        self.probability_above_break_even = p

        if p >= 0.90:
            return "STRONGLY_PROMISING"
        elif p >= 0.70:
            return "PROMISING"
        elif p >= 0.30:
            return "UNCERTAIN"
        elif p >= 0.05:
            return "WEAK"
        else:
            return "STRONG_EVIDENCE_AGAINST"

    def update(self, additional_clicks: int, additional_orders: int) -> BayesianPosterior:
        """Create updated posterior with new data."""
        new = BayesianPosterior(
            prior_alpha=self.prior_alpha,
            prior_beta=self.prior_beta,
            clicks=self.clicks + additional_clicks,
            orders=self.orders + additional_orders,
        )
        return new


def create_posterior(
    clicks: int = 0,
    orders: int = 0,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
) -> BayesianPosterior:
    """Create a Bayesian posterior with observed data."""
    return BayesianPosterior(
        prior_alpha=prior_alpha,
        prior_beta=prior_beta,
        clicks=clicks,
        orders=orders,
    )


def analyze_test_result(
    clicks: int,
    orders: int,
    break_even_cvr: float,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
) -> dict:
    """
    Complete analysis of a test result.
    Returns probability, decision, and whether to continue/kill/scale.
    """
    posterior = create_posterior(clicks, orders, prior_alpha, prior_beta)
    decision = posterior.decide(break_even_cvr)

    # Also compute P(0 sales | viable CVR)
    p_zero = posterior.probability_zero_sales(break_even_cvr)

    return {
        "clicks": clicks,
        "orders": orders,
        "break_even_cvr": break_even_cvr,
        "posterior_mean_cvr": posterior.posterior_mean_cvr,
        "credible_interval": (posterior.credible_interval_low, posterior.credible_interval_high),
        "probability_above_break_even": posterior.probability_above_break_even,
        "probability_zero_sales_if_viable": p_zero,
        "decision": decision,
        "recommendation": _recommend(decision, clicks, p_zero),
    }


def _recommend(decision: str, clicks: int, p_zero: float) -> str:
    """Generate recommendation from decision and evidence."""
    if decision == "STRONGLY_PROMISING":
        return "SCALE — strong evidence of viable economics"
    elif decision == "PROMISING":
        if clicks < 200:
            return "CONTINUE — promising but need more data"
        else:
            return "SCALE — sufficient evidence"
    elif decision == "UNCERTAIN":
        if clicks < 300:
            return "CONTINUE — insufficient data to decide"
        else:
            return "KILL/FIX — after 300+ clicks still uncertain"
    elif decision == "WEAK":
        return "KILL/FIX — weak evidence against viability"
    else:
        return "KILL — strong evidence this doesn't work"
