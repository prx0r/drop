"""
Candidate State Machine — Lifecycle management for opportunities.
States: DISCOVERED → RESEARCHING → ... → PROFITABLE_SCALABLE or KILLED
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Callable
from datetime import datetime
from packages.schemas.candidate import Candidate, CandidateState, RecommendedAction


@dataclass
class StateTransition:
    """A single state transition record."""
    from_state: CandidateState
    to_state: CandidateState
    trigger: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    reason: str = ""
    evidence: dict = field(default_factory=dict)


# Valid transitions: from_state -> list of (to_state, trigger_pattern)
VALID_TRANSITIONS = {
    CandidateState.DISCOVERED: [
        (CandidateState.RESEARCHING, "start_research"),
        (CandidateState.HARD_REJECTED, "hard_gate_fail"),
    ],
    CandidateState.RESEARCHING: [
        (CandidateState.HARD_REJECTED, "hard_gate_fail"),
        (CandidateState.SUPPLIER_VALIDATED, "supplier_ok"),
        (CandidateState.BUILD_READY, "research_complete"),
    ],
    CandidateState.HARD_REJECTED: [
        (CandidateState.RESEARCHING, "new_evidence"),
    ],
    CandidateState.SUPPLIER_VALIDATED: [
        (CandidateState.BUILD_READY, "store_ready"),
        (CandidateState.HARD_REJECTED, "new_gate_fail"),
    ],
    CandidateState.BUILD_READY: [
        (CandidateState.FREE_LISTINGS_LIVE, "enable_free_listings"),
        (CandidateState.PAID_TEST_READY, "skip_free"),
        (CandidateState.HARD_REJECTED, "new_gate_fail"),
    ],
    CandidateState.FREE_LISTINGS_LIVE: [
        (CandidateState.FREE_SIGNAL_POSITIVE, "free_signal_positive"),
        (CandidateState.FREE_SIGNAL_WEAK, "free_signal_weak"),
        (CandidateState.PAID_TEST_READY, "free_signal_enough"),
    ],
    CandidateState.FREE_SIGNAL_WEAK: [
        (CandidateState.PAID_TEST_READY, "force_paid_test"),
        (CandidateState.KILLED, "no_signal"),
        (CandidateState.FIXING, "fix_offer"),
    ],
    CandidateState.FREE_SIGNAL_POSITIVE: [
        (CandidateState.PAID_TEST_READY, "ready_for_paid"),
        (CandidateState.FREE_LISTINGS_LIVE, "collect_more"),
    ],
    CandidateState.PAID_TEST_READY: [
        (CandidateState.PAID_TESTING, "start_paid_test"),
        (CandidateState.KILLED, "budget_unavailable"),
    ],
    CandidateState.PAID_TESTING: [
        (CandidateState.PROFITABLE_SPARSE, "sparse_profit"),
        (CandidateState.PROFITABLE_SCALABLE, "scalable_profit"),
        (CandidateState.PAUSED, "pause_test"),
        (CandidateState.FIXING, "needs_fix"),
        (CandidateState.KILLED, "kill_test"),
    ],
    CandidateState.PAUSED: [
        (CandidateState.PAID_TESTING, "resume"),
        (CandidateState.FIXING, "fix_after_pause"),
        (CandidateState.KILLED, "abandon"),
    ],
    CandidateState.FIXING: [
        (CandidateState.PAID_TESTING, "fix_applied"),
        (CandidateState.FREE_LISTINGS_LIVE, "fix_free_test"),
        (CandidateState.KILLED, "fix_failed"),
    ],
    CandidateState.PROFITABLE_SPARSE: [
        (CandidateState.PROFITABLE_SCALABLE, "scale_confirmed"),
        (CandidateState.PAUSED, "pause_to_optimize"),
        (CandidateState.KILLED, "profit_deteriorated"),
    ],
    CandidateState.PROFITABLE_SCALABLE: [
        (CandidateState.PAUSED, "pause_for_capacity"),
        (CandidateState.KILLED, "market_changed"),
    ],
    CandidateState.KILLED: [
        (CandidateState.DISCOVERED, "revive"),
    ],
}


class CandidateStateMachine:
    """Manages candidate lifecycle transitions."""

    def __init__(self):
        self.transitions_log: List[StateTransition] = []

    def get_valid_transitions(self, state: CandidateState) -> List[CandidateState]:
        """Get valid target states from current state."""
        return [t[0] for t in VALID_TRANSITIONS.get(state, [])]

    def can_transition(self, from_state: CandidateState, to_state: CandidateState) -> bool:
        """Check if a transition is valid."""
        return to_state in self.get_valid_transitions(from_state)

    def transition(
        self,
        candidate: Candidate,
        to_state: CandidateState,
        trigger: str,
        reason: str = "",
        evidence: dict = None,
    ) -> bool:
        """
        Attempt a state transition. Returns True if successful.
        Logs the transition regardless.
        """
        from_state = candidate.state
        valid = self.can_transition(from_state, to_state)

        if not valid:
            self.transitions_log.append(StateTransition(
                from_state=from_state,
                to_state=to_state,
                trigger=f"REJECTED:{trigger}",
                reason=f"Invalid transition: {from_state.value} → {to_state.value}",
            ))
            return False

        # Record transition
        transition = StateTransition(
            from_state=from_state,
            to_state=to_state,
            trigger=trigger,
            reason=reason,
            evidence=evidence or {},
        )
        self.transitions_log.append(transition)

        # Update candidate
        candidate.state = to_state
        candidate.state_history.append({
            "from": from_state.value,
            "to": to_state.value,
            "trigger": trigger,
            "reason": reason,
            "timestamp": transition.timestamp,
        })
        candidate.updated_at = transition.timestamp

        return True

    def get_history(self, candidate_id: str = None) -> List[StateTransition]:
        """Get transition history, optionally filtered by candidate."""
        if candidate_id:
            return [t for t in self.transitions_log
                    if hasattr(t, 'candidate_id') and t.candidate_id == candidate_id]
        return self.transitions_log

    def diagnose_stuck(self, candidate: Candidate) -> Optional[str]:
        """Check if candidate is stuck in a state too long."""
        if not candidate.state_history:
            return None

        last = candidate.state_history[-1]
        last_time = datetime.fromisoformat(last["timestamp"])
        now = datetime.utcnow()
        hours_stuck = (now - last_time).total_seconds() / 3600

        stuck_thresholds = {
            CandidateState.RESEARCHING: 48,  # 48 hours
            CandidateState.FREE_LISTINGS_LIVE: 168,  # 7 days
            CandidateState.PAID_TESTING: 336,  # 14 days
            CandidateState.FIXING: 168,  # 7 days
        }

        threshold = stuck_thresholds.get(candidate.state)
        if threshold and hours_stuck > threshold:
            return (
                f"Candidate stuck in {candidate.state.value} for {hours_stuck:.0f} hours "
                f"(threshold: {threshold}h). Consider intervention."
            )
        return None
