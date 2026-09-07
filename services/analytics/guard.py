"""
Overintervention Guard — Every change must contain:
observation, hypothesis, action, expected_effect, minimum_evidence, evaluation_date.
If insufficient evidence: RECOMMENDATION = DO_NOTHING.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta
from enum import Enum


class InterventionType(str, Enum):
    DO_NOTHING = "DO_NOTHING"
    CHANGE_BIDS = "CHANGE_BIDS"
    CHANGE_BUDGET = "CHANGE_BUDGET"
    CHANGE_BIDDING_STRATEGY = "CHANGE_BIDDING_STRATEGY"
    CHANGE_FEED = "CHANGE_FEED"
    ADD_NEGATIVE_KEYWORD = "ADD_NEGATIVE_KEYWORD"
    PAUSE_CAMPAIGN = "PAUSE_CAMPAIGN"
    RESUME_CAMPAIGN = "RESUME_CAMPAIGN"
    CHANGE_LANDING_PAGE = "CHANGE_LANDING_PAGE"
    CHANGE_PRODUCT = "CHANGE_PRODUCT"
    SCALE_UP = "SCALE_UP"
    SCALE_DOWN = "SCALE_DOWN"


@dataclass
class Intervention:
    """A single intervention record with full context."""
    intervention_id: str
    candidate_id: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    # Required fields — every intervention must have these
    observation: str = ""  # What did we observe?
    hypothesis: str = ""  # What do we think is happening?
    action: InterventionType = InterventionType.DO_NOTHING
    action_description: str = ""  # Specific details of the action
    expected_effect: str = ""  # What change do we expect?
    minimum_evidence: str = ""  # How much evidence before we evaluate?
    evaluation_date_or_condition: str = ""  # When/how do we evaluate?

    # State tracking
    before_state: dict = field(default_factory=dict)
    after_state: dict = field(default_factory=dict)
    evaluated: bool = False
    evaluation_result: str = ""  # POSITIVE, NEGATIVE, INCONCLUSIVE


@dataclass
class GuardDecision:
    """Decision from the overintervention guard."""
    should_intervene: bool
    intervention: Optional[Intervention] = None
    reason: str = ""
    recommendation: str = ""  # DO_NOTHING or the recommended intervention


class OverinterventionGuard:
    """Prevents unnecessary changes by requiring evidence-based reasoning."""

    def __init__(self):
        self.interventions: List[Intervention] = []
        self.min_evidence_threshold = 20  # Minimum clicks before any intervention
        self.min_time_between_interventions_hours = 24

    def should_intervene(
        self,
        candidate_id: str,
        current_clicks: int,
        current_orders: int,
        current_state: dict,
        proposed_action: InterventionType = InterventionType.DO_NOTHING,
        observation: str = "",
        hypothesis: str = "",
    ) -> GuardDecision:
        """
        Determine if an intervention is warranted based on evidence.
        """
        # Check if we have enough evidence
        if current_clicks < self.min_evidence_threshold:
            return GuardDecision(
                should_intervene=False,
                reason=(
                    f"Insufficient evidence: {current_clicks} clicks "
                    f"(need {self.min_evidence_threshold}). DO NOT intervene."
                ),
                recommendation="DO_NOTHING",
            )

        # Check time since last intervention
        if self.interventions:
            last = self.interventions[-1]
            last_time = datetime.fromisoformat(last.timestamp)
            hours_since = (datetime.utcnow() - last_time).total_seconds() / 3600
            if hours_since < self.min_time_between_interventions_hours:
                return GuardDecision(
                    should_intervene=False,
                    reason=(
                        f"Too soon: {hours_since:.1f}h since last intervention "
                        f"(need {self.min_time_between_interventions_hours}h). DO NOT intervene."
                    ),
                    recommendation="DO_NOTHING",
                )

        # If no observation/hypothesis provided, cannot justify intervention
        if not observation or not hypothesis:
            return GuardDecision(
                should_intervene=False,
                reason="No observation or hypothesis provided. Cannot justify intervention.",
                recommendation="DO_NOTHING",
            )

        # If action is DO_NOTHING, that's the correct recommendation
        if proposed_action == InterventionType.DO_NOTHING:
            return GuardDecision(
                should_intervene=False,
                reason="DO_NOTHING is the correct recommendation.",
                recommendation="DO_NOTHING",
            )

        # Validate intervention has all required fields
        intervention = Intervention(
            intervention_id=f"INT-{candidate_id}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            candidate_id=candidate_id,
            observation=observation,
            hypothesis=hypothesis,
            action=proposed_action,
            expected_effect=f"Expected: {observation} → {proposed_action.value}",
            minimum_evidence=f"Need {self.min_evidence_threshold}+ clicks for evaluation",
            evaluation_date_or_condition=(
                datetime.utcnow() + timedelta(hours=48)
            ).isoformat(),
            before_state=current_state,
        )

        # Record the intervention
        self.interventions.append(intervention)

        return GuardDecision(
            should_intervene=True,
            intervention=intervention,
            reason=(
                f"Intervention justified: {observation} → {hypothesis}. "
                f"Action: {proposed_action.value}. "
                f"Evaluate after: {intervention.evaluation_date_or_condition}"
            ),
            recommendation=proposed_action.value,
        )

    def evaluate_intervention(
        self,
        intervention_id: str,
        after_state: dict,
        result: str,  # POSITIVE, NEGATIVE, INCONCLUSIVE
    ) -> Optional[Intervention]:
        """Evaluate an intervention after evidence has been collected."""
        for intervention in self.interventions:
            if intervention.intervention_id == intervention_id:
                intervention.evaluated = True
                intervention.after_state = after_state
                intervention.evaluation_result = result
                return intervention
        return None

    def get_pending_evaluations(self) -> List[Intervention]:
        """Get all interventions that haven't been evaluated yet."""
        return [i for i in self.interventions if not i.evaluated]

    def summarize(self) -> dict:
        """Summarize all interventions."""
        total = len(self.interventions)
        evaluated = sum(1 for i in self.interventions if i.evaluated)
        positive = sum(1 for i in self.interventions if i.evaluation_result == "POSITIVE")
        negative = sum(1 for i in self.interventions if i.evaluation_result == "NEGATIVE")

        return {
            "total_interventions": total,
            "evaluated": evaluated,
            "pending": total - evaluated,
            "positive_results": positive,
            "negative_results": negative,
            "intervention_rate": f"{total / max(1, evaluated):.1f} per evaluation",
        }


# The classic overintervention case from the research:
# May 2026 campaign with 1,0,3,2,0 impressions over 5 days,
# operator changed: bids, bidding strategy (twice), feed structure
# All within 5 days with essentially no data.
OVERINTERVENTION_EXAMPLE = {
    "case": "May 2026 new Shopping campaign",
    "evidence_count": 6,  # Total data points across 5 days
    "actions_taken": [
        InterventionType.CHANGE_BIDS,
        InterventionType.CHANGE_BIDDING_STRATEGY,
        InterventionType.CHANGE_BIDDING_STRATEGY,
        InterventionType.CHANGE_FEED,
    ],
    "diagnosis": "INSUFFICIENT_EVIDENCE_AND_EXCESS_INTERVENTION",
    "lesson": (
        "The operator changed everything with almost no data. "
        "Correct action: OBSERVE, don't ACT. "
        "Wait for statistically meaningful data before intervening."
    ),
}
