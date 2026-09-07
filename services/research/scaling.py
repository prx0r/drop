"""
Scaling Rule Module — When and how to scale budget.
Initial increment: 10-20%. Only scale when ALL conditions are met.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum
from packages.schemas.candidate import Candidate


class ScalingAction(str, Enum):
    SCALE_UP = "SCALE_UP"
    SCALE_DOWN = "SCALE_DOWN"
    HOLD = "HOLD"
    STOP = "STOP"


@dataclass
class ScalingDecision:
    action: ScalingAction
    current_budget: float = 0.0
    new_budget: float = 0.0
    increment_pct: float = 0.15
    conditions_met: dict = field(default_factory=dict)
    conditions_failed: dict = field(default_factory=dict)
    reasoning: List[str] = field(default_factory=list)


@dataclass
class ScalingRecord:
    candidate_id: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    action: ScalingAction = ScalingAction.HOLD
    old_budget: float = 0.0
    new_budget: float = 0.0
    roas: float = 0.0
    contribution: float = 0.0
    posterior_p_above: float = 0.0
    conditions_snapshot: dict = field(default_factory=dict)


class ScalingEngine:
    def __init__(self, increment_pct: float = 0.15):
        self.increment_pct = increment_pct
        self.records: List[ScalingRecord] = []
        self.min_clicks_before_scale: int = 100
        self.min_orders_before_scale: int = 3
        self.roas_collapse_threshold: float = 0.5
        self.min_posterior_for_scale: float = 0.7

    def evaluate_scaling(
        self,
        candidate: Candidate,
        current_budget: float,
        roas: float = 0.0,
        recent_contribution: float = 0.0,
        recent_cvr: float = 0.0,
        baseline_cvr: float = 0.0,
        returns_rate: float = 0.05,
        supplier_health: float = 1.0,
    ) -> ScalingDecision:
        """
        Evaluate whether to scale, hold, or stop.
        ALL conditions must be met for SCALE_UP.
        """
        decision = ScalingDecision(
            action=ScalingAction.HOLD,
            current_budget=current_budget,
            new_budget=current_budget,
        )
        conditions_met = {}
        conditions_failed = {}

        # Condition 1: Positive contribution
        if recent_contribution > 0:
            conditions_met["positive_contribution"] = f"${recent_contribution:.2f}"
        else:
            conditions_failed["positive_contribution"] = f"${recent_contribution:.2f} (negative)"

        # Condition 2: Posterior viability strong
        p_above = candidate.probability_cvr_above_break_even
        if p_above >= self.min_posterior_for_scale:
            conditions_met["posterior_viability"] = f"{p_above:.1%}"
        elif candidate.observed_clicks == 0:
            conditions_met["posterior_viability"] = "no data yet (allow initial test)"
        else:
            conditions_failed["posterior_viability"] = f"{p_above:.1%} < {self.min_posterior_for_scale:.0%}"

        # Condition 3: Supplier healthy
        if supplier_health >= 0.5:
            conditions_met["supplier_health"] = f"{supplier_health:.2f}"
        else:
            conditions_failed["supplier_health"] = f"{supplier_health:.2f} < 0.5"

        # Condition 4: CVR not collapsing
        if baseline_cvr > 0 and recent_cvr > 0:
            cvr_ratio = recent_cvr / baseline_cvr
            if cvr_ratio >= 0.7:
                conditions_met["cvr_stable"] = f"ratio {cvr_ratio:.2f}"
            else:
                conditions_failed["cvr_stable"] = f"CVR collapsed: {cvr_ratio:.2f}x baseline"
        elif candidate.observed_clicks == 0:
            conditions_met["cvr_stable"] = "no data yet"
        else:
            conditions_met["cvr_stable"] = "insufficient data to judge"

        # Condition 5: Returns stable
        if returns_rate <= 0.10:
            conditions_met["returns_stable"] = f"{returns_rate:.1%}"
        else:
            conditions_failed["returns_stable"] = f"{returns_rate:.1%} > 10%"

        # Condition 6: Enough data
        if candidate.observed_clicks >= self.min_clicks_before_scale:
            conditions_met["sufficient_data"] = f"{candidate.observed_clicks} clicks"
        else:
            conditions_met["sufficient_data"] = f"{candidate.observed_clicks} clicks (initial phase)"

        # Decision logic
        if conditions_failed:
            # Check for stop conditions
            stop_conditions = [
                "positive_contribution" in conditions_failed,
                "cvr_stable" in conditions_failed and "CVR collapsed" in conditions_failed.get("cvr_stable", ""),
            ]
            if any(stop_conditions):
                decision.action = ScalingAction.STOP
                decision.reasoning.append("STOP: critical conditions failed")
                for k, v in conditions_failed.items():
                    decision.reasoning.append(f"  FAILED: {k} = {v}")
            else:
                decision.action = ScalingAction.HOLD
                decision.reasoning.append("HOLD: some conditions not met")
                for k, v in conditions_failed.items():
                    decision.reasoning.append(f"  FAILED: {k} = {v}")
        else:
            # All conditions met — scale up
            new_budget = current_budget * (1 + self.increment_pct)
            decision.action = ScalingAction.SCALE_UP
            decision.new_budget = round(new_budget, 2)
            decision.increment_pct = self.increment_pct
            decision.reasoning.append(
                f"SCALE UP: ${current_budget:.2f} → ${decision.new_budget:.2f} "
                f"(+{self.increment_pct:.0%})"
            )
            for k, v in conditions_met.items():
                decision.reasoning.append(f"  OK: {k} = {v}")

        decision.conditions_met = conditions_met
        decision.conditions_failed = conditions_failed

        # Record
        self.records.append(ScalingRecord(
            candidate_id=candidate.candidate_id,
            action=decision.action,
            old_budget=current_budget,
            new_budget=decision.new_budget,
            roas=roas,
            contribution=recent_contribution,
            posterior_p_above=p_above,
            conditions_snapshot={**conditions_met, **conditions_failed},
        ))

        return decision

    def should_stop_scaling(
        self,
        roas: float = 0.0,
        contribution: float = 0.0,
        supplier_health: float = 1.0,
    ) -> bool:
        """Quick check: should we stop scaling entirely?"""
        if roas > 0 and roas < self.roas_collapse_threshold:
            return True
        if contribution < 0:
            return True
        if supplier_health < 0.3:
            return True
        return False

    def get_history(self, candidate_id: Optional[str] = None) -> List[ScalingRecord]:
        if candidate_id:
            return [r for r in self.records if r.candidate_id == candidate_id]
        return self.records
