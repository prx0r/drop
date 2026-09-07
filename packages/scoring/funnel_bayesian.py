"""
Funnel Bayesian Models — Beta-Binomial for each funnel stage.
P(CTR > viable | impressions, clicks)
P(ATC_RATE > viable | clicks, atcs)
P(CHECKOUT_RATE > viable | atcs, checkouts)
P(PURCHASE_RATE > viable | checkouts, orders)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
import math


@dataclass
class StagePosterior:
    stage_name: str
    prior_alpha: float = 1.0
    prior_beta: float = 1.0
    successes: int = 0
    trials: int = 0
    posterior_alpha: float = 1.0
    posterior_beta: float = 1.0
    posterior_mean: float = 0.0
    credible_interval_low: float = 0.0
    credible_interval_high: float = 0.0
    probability_above_threshold: float = 0.0
    threshold: float = 0.0
    decision: str = ""

    def _update(self):
        self.posterior_alpha = self.prior_alpha + self.successes
        self.posterior_beta = self.prior_beta + (self.trials - self.successes)
        total = self.posterior_alpha + self.posterior_beta
        self.posterior_mean = self.posterior_alpha / total if total > 0 else 0.0
        if total > 20:
            std = math.sqrt(
                (self.posterior_alpha * self.posterior_beta) /
                (total ** 2 * (total + 1))
            )
            self.credible_interval_low = max(0.0, self.posterior_mean - 1.645 * std)
            self.credible_interval_high = min(1.0, self.posterior_mean + 1.645 * std)
        else:
            self.credible_interval_low = 0.0
            self.credible_interval_high = min(1.0, self.posterior_mean * 3)

    def compute_probability_above(self, threshold: float):
        self.threshold = threshold
        self._update()
        total = self.posterior_alpha + self.posterior_beta
        mean = self.posterior_alpha / total
        std = math.sqrt(
            (self.posterior_alpha * self.posterior_beta) /
            (total ** 2 * (total + 1))
        ) if total > 0 else 0.0
        if std == 0:
            self.probability_above_threshold = 1.0 if mean > threshold else 0.0
        else:
            z = (threshold - mean) / std
            p_below = 0.5 * (1 + math.erf(z / math.sqrt(2)))
            self.probability_above_threshold = 1.0 - p_below
        return self.probability_above_threshold

    def decide(self, threshold: float) -> str:
        p = self.compute_probability_above(threshold)
        if p >= 0.90:
            self.decision = "STRONG_SIGNAL"
        elif p >= 0.70:
            self.decision = "SIGNAL"
        elif p >= 0.30:
            self.decision = "UNCERTAIN"
        elif p >= 0.05:
            self.decision = "WEAK"
        else:
            self.decision = "EVIDENCE_AGAINST"
        return self.decision


@dataclass
class FunnelBayesianResult:
    ctr: StagePosterior = field(default_factory=lambda: StagePosterior("CTR"))
    atc_rate: StagePosterior = field(default_factory=lambda: StagePosterior("ATC_RATE"))
    checkout_rate: StagePosterior = field(default_factory=lambda: StagePosterior("CHECKOUT_RATE"))
    purchase_rate: StagePosterior = field(default_factory=lambda: StagePosterior("PURCHASE_RATE"))
    overall_viable: bool = False
    bottleneck_stage: str = ""
    summary: str = ""


def analyze_funnel_bayesian(
    impressions: int = 0,
    clicks: int = 0,
    atcs: int = 0,
    checkouts: int = 0,
    orders: int = 0,
    viable_ctr: float = 0.02,
    viable_atc_rate: float = 0.05,
    viable_checkout_rate: float = 0.50,
    viable_purchase_rate: float = 0.90,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
) -> FunnelBayesianResult:
    """
    Analyze full funnel with Bayesian models for each stage.

    viable_* thresholds define what "good enough" looks like for each stage:
    - CTR > 2% is healthy
    - ATC rate > 5% of clicks is healthy
    - Checkout rate > 50% of ATCs is healthy
    - Purchase rate > 90% of checkouts is healthy
    """
    result = FunnelBayesianResult()

    # Stage 1: CTR
    if impressions > 0:
        result.ctr = StagePosterior(
            stage_name="CTR",
            prior_alpha=prior_alpha,
            prior_beta=prior_beta,
            successes=clicks,
            trials=impressions,
        )
        result.ctr.decide(viable_ctr)
    else:
        result.ctr.stage_name = "CTR"
        result.ctr.decision = "NO_DATA"
        result.ctr.threshold = viable_ctr

    # Stage 2: ATC rate
    if clicks > 0:
        result.atc_rate = StagePosterior(
            stage_name="ATC_RATE",
            prior_alpha=prior_alpha,
            prior_beta=prior_beta,
            successes=atcs,
            trials=clicks,
        )
        result.atc_rate.decide(viable_atc_rate)
    else:
        result.atc_rate.stage_name = "ATC_RATE"
        result.atc_rate.decision = "NO_DATA"
        result.atc_rate.threshold = viable_atc_rate

    # Stage 3: Checkout rate
    if atcs > 0:
        result.checkout_rate = StagePosterior(
            stage_name="CHECKOUT_RATE",
            prior_alpha=prior_alpha,
            prior_beta=prior_beta,
            successes=checkouts,
            trials=atcs,
        )
        result.checkout_rate.decide(viable_checkout_rate)
    else:
        result.checkout_rate.stage_name = "CHECKOUT_RATE"
        result.checkout_rate.decision = "NO_DATA"
        result.checkout_rate.threshold = viable_checkout_rate

    # Stage 4: Purchase rate
    if checkouts > 0:
        result.purchase_rate = StagePosterior(
            stage_name="PURCHASE_RATE",
            prior_alpha=prior_alpha,
            prior_beta=prior_beta,
            successes=orders,
            trials=checkouts,
        )
        result.purchase_rate.decide(viable_purchase_rate)
    else:
        result.purchase_rate.stage_name = "PURCHASE_RATE"
        result.purchase_rate.decision = "NO_DATA"
        result.purchase_rate.threshold = viable_purchase_rate

    # Determine bottleneck
    stages = [
        ("CTR", result.ctr),
        ("ATC_RATE", result.atc_rate),
        ("CHECKOUT_RATE", result.checkout_rate),
        ("PURCHASE_RATE", result.purchase_rate),
    ]

    bottleneck = None
    worst_prob = 1.0
    for name, stage in stages:
        if stage.decision in ("WEAK", "EVIDENCE_AGAINST", "NO_DATA"):
            if stage.probability_above_threshold < worst_prob:
                worst_prob = stage.probability_above_threshold
                bottleneck = name

    result.bottleneck_stage = bottleneck or "NONE"
    result.overall_viable = all(
        s.decision in ("STRONG_SIGNAL", "SIGNAL", "UNCERTAIN")
        for _, s in stages
        if s.decision != "NO_DATA"
    )

    # Summary
    parts = []
    for name, stage in stages:
        if stage.decision == "NO_DATA":
            parts.append(f"{name}: no data")
        else:
            parts.append(f"{name}: {stage.probability_above_threshold:.1%} p>{stage.threshold:.1%} → {stage.decision}")
    result.summary = " | ".join(parts)

    return result
