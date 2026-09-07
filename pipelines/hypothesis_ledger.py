"""Pipeline 3: Hypothesis Ledger

Observations → Hypotheses → Falsification tracking

Input: List[Observation], List[Hypothesis]
Output: List[Hypothesis] (with updated states)

This pipeline:
1. Takes observations about hypotheses
2. Updates hypothesis evidence (for/against)
3. Evaluates falsification conditions
4. Updates hypothesis states

Side effects: NONE. Pure transform.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from schemas.observation import Observation, EvidenceGrade
from schemas.hypothesis import (
    Hypothesis,
    HypothesisState,
    EvidenceUpdate,
    EvidenceDirection,
    EvidenceStrength,
    FalsificationResult,
)


class HypothesisUpdate:
    """Result of evaluating a hypothesis against observations."""

    def __init__(
        self,
        hypothesis: Hypothesis,
        evidence_updates: list[EvidenceUpdate],
        state_changed: bool,
        old_state: Optional[HypothesisState] = None,
        new_state: Optional[HypothesisState] = None,
        falsification_result: Optional[FalsificationResult] = None,
    ):
        self.hypothesis = hypothesis
        self.evidence_updates = evidence_updates
        self.state_changed = state_changed
        self.old_state = old_state
        self.new_state = new_state
        self.falsification_result = falsification_result

    @property
    def summary(self) -> str:
        if self.state_changed:
            return f"{self.old_state.value} → {self.new_state.value}"
        if self.evidence_updates:
            return f"+{len(self.evidence_updates)} evidence updates"
        return "No change"


class HypothesisLedgerPipeline:
    """Observations → Hypotheses → Falsification tracking.

    Pure transform. No I/O.
    """

    # How does each observation field map to hypothesis evidence?
    # NOTE: This is a default mapping. The actual direction depends on the hypothesis claim.
    # For example, "good_sellers" AGAINST "underserved market" but FOR "market has demand".
    EVIDENCE_MAPPING = {
        # Observations that SUPPORT most hypotheses
        "demand_level": EvidenceDirection.FOR,
        "search_volume": EvidenceDirection.FOR,
        "demand_growth": EvidenceDirection.FOR,
        "merchant_gap_score": EvidenceDirection.FOR,
        "supplier_name": EvidenceDirection.FOR,  # Found a supplier
        "dealer_price": EvidenceDirection.FOR,  # Got economics
        "contribution_margin": EvidenceDirection.FOR,  # Positive margin
        "price_observed": EvidenceDirection.FOR,  # Price data
        # Observations that WEAKEN most hypotheses
        "KILLED": EvidenceDirection.AGAINST,
        "falsified": EvidenceDirection.AGAINST,
        "no_demand": EvidenceDirection.AGAINST,
        "no_supply": EvidenceDirection.AGAINST,
        "negative_margin": EvidenceDirection.AGAINST,
        "too_competitive": EvidenceDirection.AGAINST,
    }

    def classify_evidence_strength(
        self, observation: Observation
    ) -> EvidenceStrength:
        """Classify evidence strength based on source grade."""
        grade_to_strength = {
            EvidenceGrade.A: EvidenceStrength.HIGH,
            EvidenceGrade.B: EvidenceStrength.HIGH,
            EvidenceGrade.C: EvidenceStrength.MEDIUM,
            EvidenceGrade.D: EvidenceStrength.LOW,
        }
        return grade_to_strength.get(observation.source_grade, EvidenceStrength.LOW)

    def evaluate_hypothesis(
        self,
        hypothesis: Hypothesis,
        observations: list[Observation],
    ) -> HypothesisUpdate:
        """Evaluate a single hypothesis against observations.

        Pure transform: deep-copies hypothesis before mutation.
        """
        # Deep copy to avoid mutating the original
        hypothesis = hypothesis.model_copy(deep=True)

        evidence_updates = []
        old_state = hypothesis.state

        # Map observations to evidence updates
        for obs in observations:
            # Check if this observation is relevant to this hypothesis
            if not self._is_relevant(obs, hypothesis):
                continue

            # Determine direction
            direction = self.EVIDENCE_MAPPING.get(obs.field, EvidenceDirection.NEUTRAL)
            if direction == EvidenceDirection.NEUTRAL:
                continue

            # Determine strength
            strength = self.classify_evidence_strength(obs)

            # Create evidence update
            update = EvidenceUpdate(
                hypothesis_id=hypothesis.hypothesis_id,
                observation_id=obs.observation_id,
                direction=direction,
                strength=strength,
                reason=f"Observation {obs.field} = {obs.value} ({obs.source_grade.value})",
                independence_cluster=obs.independence_cluster,
                independent_source_count=obs.independent_source_count,
            )
            evidence_updates.append(update)

            # Apply to hypothesis
            if direction == EvidenceDirection.FOR:
                hypothesis.add_evidence_for(obs.observation_id)
            elif direction == EvidenceDirection.AGAINST:
                hypothesis.add_evidence_against(obs.observation_id)

        # Update independent source count
        unique_sources = set()
        for obs in observations:
            if obs.source_name:
                unique_sources.add(obs.source_name)
        hypothesis.independent_source_count = len(unique_sources)

        # Evaluate falsification
        falsification_result = None
        if self._should_falsify(hypothesis):
            falsification_result = self._falsify(hypothesis, observations)
            hypothesis.state = HypothesisState.FALSIFIED
            hypothesis.resolved_at = datetime.now(timezone.utc)
        elif self._should_support(hypothesis):
            hypothesis.support(confidence=hypothesis.confidence)

        # Check for external block
        if self._is_externally_blocked(hypothesis, observations):
            hypothesis.state = HypothesisState.EXTERNALLY_BLOCKED

        state_changed = hypothesis.state != old_state

        return HypothesisUpdate(
            hypothesis=hypothesis,
            evidence_updates=evidence_updates,
            state_changed=state_changed,
            old_state=old_state,
            new_state=hypothesis.state,
            falsification_result=falsification_result,
        )

    def _is_relevant(self, observation: Observation, hypothesis: Hypothesis) -> bool:
        """Is this observation relevant to this hypothesis?"""
        # Check by candidate_id (if both have it)
        if hypothesis.candidate_id and observation.candidate_id:
            if hypothesis.candidate_id != observation.candidate_id:
                return False

        # Don't filter by country_code in entity_id - too strict
        # Instead, rely on candidate_id for relevance

        return True

    def _should_falsify(self, hypothesis: Hypothesis) -> bool:
        """Should this hypothesis be falsified?"""
        if hypothesis.state in {
            HypothesisState.FALSIFIED,
            HypothesisState.SUPERSEDED,
        }:
            return False

        # Falsify if evidence_against outweighs evidence_for
        total = len(hypothesis.evidence_for) + len(hypothesis.evidence_against)
        if total < 2:
            return False

        against_ratio = len(hypothesis.evidence_against) / total
        return against_ratio > 0.7  # 70%+ evidence against

    def _should_support(self, hypothesis: Hypothesis) -> bool:
        """Should this hypothesis be supported?"""
        if hypothesis.state in {
            HypothesisState.FALSIFIED,
            HypothesisState.SUPERSEDED,
        }:
            return False

        # Support if evidence_for outweighs evidence_against
        total = len(hypothesis.evidence_for) + len(hypothesis.evidence_against)
        if total < 3:
            return False

        for_ratio = len(hypothesis.evidence_for) / total
        return for_ratio > 0.7  # 70%+ evidence for

    def _is_externally_blocked(
        self, hypothesis: Hypothesis, observations: list[Observation]
    ) -> bool:
        """Is this hypothesis blocked by external factors?"""
        for obs in observations:
            if obs.field == "decision" and obs.value == "HUMAN_ACTION_REQUIRED":
                return True
            if obs.field == "decision" and obs.value == "FROZEN":
                return True
        return False

    def _falsify(
        self, hypothesis: Hypothesis, observations: list[Observation]
    ) -> dict:
        """Falsify a hypothesis and return the result."""
        # Find the most damaging evidence
        damaging_evidence = []
        for obs in observations:
            if obs.field in {"KILLED", "falsified", "no_demand", "no_supply", "negative_margin", "too_competitive"}:
                damaging_evidence.append(obs)

        reason = "Evidence against outweighs evidence for"
        if damaging_evidence:
            reason = f"Key evidence: {damaging_evidence[0].field} = {damaging_evidence[0].value}"

        return FalsificationResult(
            hypothesis_id=hypothesis.hypothesis_id,
            is_falsified=True,
            confidence=0.8,
            evidence_summary=reason,
        )

    def run(
        self,
        hypotheses: list[Hypothesis],
        observations: list[Observation],
    ) -> list[HypothesisUpdate]:
        """Run the hypothesis ledger pipeline.

        Input: Hypotheses + Observations
        Output: List of HypothesisUpdate
        """
        updates = []
        for hypothesis in hypotheses:
            update = self.evaluate_hypothesis(hypothesis, observations)
            updates.append(update)
        return updates
