"""Pipeline 2: Candidate State Machine

Observations → State transitions

Input: List[Observation], Candidate
Output: Candidate (with updated state)

This pipeline:
1. Takes observations about a candidate
2. Determines what state transition is warranted
3. Returns the candidate with updated state and history

Side effects: NONE. Pure transform.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from schemas.observation import Observation
from schemas.candidate import Candidate, CandidateState, VALID_TRANSITIONS


class StateTransitionResult:
    """Result of a state machine evaluation."""

    def __init__(
        self,
        candidate: Candidate,
        transitioned: bool,
        from_state: Optional[CandidateState] = None,
        to_state: Optional[CandidateState] = None,
        reason: Optional[str] = None,
    ):
        self.candidate = candidate
        self.transitioned = transitioned
        self.from_state = from_state
        self.to_state = to_state
        self.reason = reason

    @property
    def summary(self) -> str:
        if not self.transitioned:
            return f"No transition from {self.candidate.state.value}"
        return f"{self.from_state.value} → {self.to_state.value}: {self.reason}"


class StateMachinePipeline:
    """Observations → State transitions.

    Pure transform. No I/O.
    """

    # What observations trigger what transitions?
    TRANSITION_TRIGGERS = {
        # From DISCOVERED
        CandidateState.DISCOVERED: {
            "demand_verified": CandidateState.DEMAND_VERIFIED,
            "search_volume": CandidateState.DEMAND_VERIFIED,
            "demand_level": CandidateState.DEMAND_VERIFIED,
            "demand_growth": CandidateState.DEMAND_VERIFIED,
        },
        # From DEMAND_VERIFIED
        CandidateState.DEMAND_VERIFIED: {
            "merchant_gap_score": CandidateState.MERCHANT_GAP_VERIFIED,
            "good_sellers": CandidateState.MERCHANT_GAP_VERIFIED,
            "total_sellers": CandidateState.MERCHANT_GAP_VERIFIED,
        },
        # From MERCHANT_GAP_VERIFIED
        CandidateState.MERCHANT_GAP_VERIFIED: {
            "supplier_name": CandidateState.SUPPLY_PATH_VERIFIED,
            "supplier_status": CandidateState.SUPPLY_PATH_VERIFIED,
            "dealer_price": CandidateState.SUPPLY_PATH_VERIFIED,
        },
        # From SUPPLY_PATH_VERIFIED
        CandidateState.SUPPLY_PATH_VERIFIED: {
            "contribution_margin": CandidateState.MARGIN_VERIFIED,
            "price_observed": CandidateState.MARGIN_VERIFIED,
            "margin": CandidateState.MARGIN_VERIFIED,
        },
        # From MARGIN_VERIFIED
        CandidateState.MARGIN_VERIFIED: {
            "search_volume": CandidateState.SEARCH_ECONOMICS_VERIFIED,
            "cpc": CandidateState.SEARCH_ECONOMICS_VERIFIED,
            "search_economics": CandidateState.SEARCH_ECONOMICS_VERIFIED,
        },
        # From SEARCH_ECONOMICS_VERIFIED
        CandidateState.SEARCH_ECONOMICS_VERIFIED: {
            "launch_ready": CandidateState.LAUNCHABLE,
            "all_gates_pass": CandidateState.LAUNCHABLE,
        },
        # From LAUNCHABLE
        CandidateState.LAUNCHABLE: {
            "free_traffic_test": CandidateState.FREE_TRAFFIC_TEST,
            "free_listing_active": CandidateState.FREE_TRAFFIC_TEST,
        },
        # From FREE_TRAFFIC_TEST
        CandidateState.FREE_TRAFFIC_TEST: {
            "paid_test": CandidateState.PAID_TEST,
            "free_signals_positive": CandidateState.PAID_TEST,
        },
        # From PAID_TEST
        CandidateState.PAID_TEST: {
            "profitable": CandidateState.PROFITABLE,
            "positive_contribution": CandidateState.PROFITABLE,
        },
        # From FROZEN (can be unfrozen by new evidence)
        CandidateState.FROZEN: {
            "demand_verified": CandidateState.DEMAND_VERIFIED,
            "merchant_gap_score": CandidateState.MERCHANT_GAP_VERIFIED,
            "supplier_name": CandidateState.SUPPLY_PATH_VERIFIED,
            "contribution_margin": CandidateState.MARGIN_VERIFIED,
            "launch_ready": CandidateState.LAUNCHABLE,
        },
    }

    # What observations trigger KILL from any state?
    # Uses (field, value) tuples for precise matching
    KILL_TRIGGERS = {
    ("decision", "KILLED"),
    ("decision", "FALSIFIED"),
    ("falsified", None),
    ("no_demand", None),
    ("no_supply", None),
    ("negative_margin", None),
    ("too_competitive", None),
}

    def evaluate_transition(
        self,
        candidate: Candidate,
        observations: list[Observation],
    ) -> StateTransitionResult:
        """Evaluate whether a state transition should occur.

        Pure transform: takes candidate + observations, returns transition result.
        """
        current_state = candidate.state

        # Check for KILL triggers first
        for obs in observations:
            is_kill = False
            for trigger_field, trigger_value in self.KILL_TRIGGERS:
                if trigger_value is None:
                    # Match any value for this field
                    if obs.field == trigger_field:
                        is_kill = True
                        break
                else:
                    # Match specific field + value
                    if obs.field == trigger_field and obs.value == trigger_value:
                        is_kill = True
                        break

            if is_kill and current_state != CandidateState.KILLED:
                    new_candidate = candidate.model_copy(deep=True)
                    new_candidate.transition(
                        CandidateState.KILLED,
                        reason=f"Kill trigger: {obs.field} = {obs.value}",
                    )
                    return StateTransitionResult(
                        candidate=new_candidate,
                        transitioned=True,
                        from_state=current_state,
                        to_state=CandidateState.KILLED,
                        reason=f"Kill trigger: {obs.field} = {obs.value}",
                    )

        # Check for HUMAN_ACTION_REQUIRED
        for obs in observations:
            if obs.field == "decision" and obs.value == "HUMAN_ACTION_REQUIRED":
                if current_state != CandidateState.HUMAN_ACTION_REQUIRED:
                    new_candidate = candidate.model_copy(deep=True)
                    new_candidate.transition(
                        CandidateState.HUMAN_ACTION_REQUIRED,
                        reason="External action required",
                    )
                    return StateTransitionResult(
                        candidate=new_candidate,
                        transitioned=True,
                        from_state=current_state,
                        to_state=CandidateState.HUMAN_ACTION_REQUIRED,
                        reason="External action required",
                    )

        # Check for normal transitions
        triggers = self.TRANSITION_TRIGGERS.get(current_state, {})
        for obs in observations:
            if obs.field in triggers:
                new_state = triggers[obs.field]
                if new_state in VALID_TRANSITIONS.get(current_state, set()):
                    new_candidate = candidate.model_copy(deep=True)
                    new_candidate.transition(
                        new_state,
                        reason=f"Observation: {obs.field} = {obs.value}",
                    )
                    return StateTransitionResult(
                        candidate=new_candidate,
                        transitioned=True,
                        from_state=current_state,
                        to_state=new_state,
                        reason=f"Observation: {obs.field} = {obs.value}",
                    )

        # No transition
        return StateTransitionResult(
            candidate=candidate,
            transitioned=False,
        )

    def run(
        self,
        candidate: Candidate,
        observations: list[Observation],
    ) -> StateTransitionResult:
        """Run the state machine pipeline.

        Input: Candidate + Observations
        Output: StateTransitionResult
        """
        return self.evaluate_transition(candidate, observations)
