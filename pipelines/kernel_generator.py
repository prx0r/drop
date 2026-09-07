"""Pipeline 5: Kernel Generator

Probe results → Market-intelligence kernels

Input: ProbeResult, List[Observation], List[Hypothesis]
Output: List[Kernel]

This pipeline:
1. Takes probe results and observations
2. Maps observations to kernel types
3. Generates market-intelligence kernels

Side effects: NONE. Pure transform.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from schemas.observation import Observation, EvidenceGrade
from schemas.hypothesis import Hypothesis, HypothesisState
from schemas.kernel import Kernel, KernelType, BeliefDelta
from schemas.probe import ProbeResult


class KernelGeneratorPipeline:
    """Probe results → Market-intelligence kernels.

    Pure transform. No I/O.
    """

    # What observation fields map to what kernel types?
    KERNEL_TYPE_MAP = {
        # Demand
        "demand_level": KernelType.DEMAND_DISCOVERY,
        "search_volume": KernelType.DEMAND_DISCOVERY,
        "demand_growth": KernelType.DEMAND_DISCOVERY,
        "no_demand": KernelType.DEMAND_FALSIFICATION,
        # Merchant
        "merchant_gap_score": KernelType.MERCHANT_GAP_DISCOVERY,
        "good_sellers": KernelType.MERCHANT_GAP_DISCOVERY,
        "total_sellers": KernelType.MERCHANT_GAP_DISCOVERY,
        "too_competitive": KernelType.MERCHANT_GAP_FALSIFICATION,
        # Hidden channels
        "hidden_distributor": KernelType.HIDDEN_CHANNEL_DISCOVERY,
        "trade_portal": KernelType.HIDDEN_CHANNEL_DISCOVERY,
        "professional_channel": KernelType.HIDDEN_CHANNEL_DISCOVERY,
        # Supply
        "supplier_name": KernelType.SUPPLIER_PATH_DISCOVERY,
        "supplier_status": KernelType.SUPPLIER_PATH_DISCOVERY,
        "no_supply": KernelType.SUPPLIER_PATH_FAILURE,
        # Economics
        "dealer_price": KernelType.MARGIN_THRESHOLD,
        "contribution_margin": KernelType.MARGIN_THRESHOLD,
        "price_observed": KernelType.PRICE_COMPRESSION,
        "negative_margin": KernelType.MARGIN_THRESHOLD,
        # Content
        "content_gap": KernelType.CONTENT_NOT_COMMERCE,
        "merchant_gap_only_content": KernelType.CONTENT_NOT_COMMERCE,
        # Risk
        "support_burden": KernelType.SUPPORT_BURDEN,
        "return_risk": KernelType.RETURN_RISK,
        "warranty_risk": KernelType.WARRANTY_RISK,
        # Cross-market
        "source_market_proof": KernelType.SOURCE_MARKET_PROOF,
        "target_market_asymmetry": KernelType.TARGET_MARKET_ASYMMETRY,
        # Regulatory
        "regulatory_blocker": KernelType.REGULATORY_BLOCKER,
        # Decision
        "KILLED": KernelType.DEMAND_FALSIFICATION,
        "HUMAN_ACTION_REQUIRED": KernelType.HUMAN_ACTION_REQUIRED,
    }

    def classify_kernel_type(self, observation: Observation) -> KernelType:
        """Classify what type of kernel this observation generates."""
        return self.KERNEL_TYPE_MAP.get(
            observation.field, KernelType.DEMAND_DISCOVERY
        )

    def classify_belief_delta(
        self,
        observation: Observation,
        hypothesis: Optional[Hypothesis] = None,
    ) -> BeliefDelta:
        """Classify how this observation changes belief."""
        # Positive observations
        positive_fields = {
            "demand_level",
            "search_volume",
            "demand_growth",
            "merchant_gap_score",
            "supplier_name",
            "supplier_status",
            "dealer_price",
            "contribution_margin",
        }

        # Negative observations
        negative_fields = {
            "no_demand",
            "no_supply",
            "negative_margin",
            "too_competitive",
            "KILLED",
            "falsified",
        }

        if observation.field in positive_fields:
            return BeliefDelta.MODERATELY_FOR
        if observation.field in negative_fields:
            return BeliefDelta.MODERATELY_AGAINST

        return BeliefDelta.NEUTRAL

    def classify_information_gain(self, observation: Observation) -> str:
        """Classify information gain (HIGH, MEDIUM, LOW)."""
        grade_to_gain = {
            EvidenceGrade.A: "HIGH",
            EvidenceGrade.B: "HIGH",
            EvidenceGrade.C: "MEDIUM",
            EvidenceGrade.D: "LOW",
        }
        return grade_to_gain.get(observation.source_grade, "LOW")

    def generate_kernel(
        self,
        observation: Observation,
        hypothesis: Optional[Hypothesis] = None,
        probe_result: Optional[ProbeResult] = None,
    ) -> Kernel:
        """Generate a kernel from an observation."""
        kernel_type = self.classify_kernel_type(observation)
        belief_delta = self.classify_belief_delta(observation, hypothesis)
        information_gain = self.classify_information_gain(observation)

        # Generate hypothesis text
        hypothesis_text = "Unknown hypothesis"
        if hypothesis:
            hypothesis_text = hypothesis.claim

        # Generate new observation dict
        new_observation = {
            "fact": f"{observation.field} = {observation.value}",
            "source_grade": observation.source_grade.value,
            "source_name": observation.source_name,
            "source_url": observation.source_url,
        }

        # Generate mechanism
        mechanism = None
        if kernel_type == KernelType.HIDDEN_CHANNEL_DISCOVERY:
            mechanism = "Public SERP scarcity caused by hidden professional distribution"
        elif kernel_type == KernelType.CONTENT_NOT_COMMERCE:
            mechanism = "Content gap exists but commerce is already served"
        elif kernel_type == KernelType.DEMAND_FALSIFICATION:
            mechanism = "Demand signal was weaker than initially estimated"

        # Generate generalisable rule
        generalisable_rule = None
        if kernel_type == KernelType.HIDDEN_CHANNEL_DISCOVERY:
            generalisable_rule = "Professional-product public SERP scarcity must be checked against trade/distributor networks"
        elif kernel_type == KernelType.CONTENT_NOT_COMMERCE:
            generalisable_rule = "Content opportunity ≠ store opportunity"

        # Generate next best test
        next_best_test = None
        if hypothesis and hypothesis.next_best_test:
            next_best_test = hypothesis.next_best_test

        return Kernel(
            hypothesis_id=hypothesis.hypothesis_id if hypothesis else None,
            hypothesis=hypothesis_text,
            candidate_id=observation.candidate_id,
            new_observation=new_observation,
            belief_delta=belief_delta,
            mechanism=mechanism,
            state_before=hypothesis.state.value if hypothesis else None,
            state_after=None,  # State transitions happen in state_machine pipeline
            resolved_fields=[observation.field] if observation.field else [],
            remaining_decisive_unknown=None,
            falsification_effect=None,
            next_best_test=next_best_test,
            decision_threshold=None,
            generalisable_rule=generalisable_rule,
            kernel_type=kernel_type,
            novelty_type="MECHANISM_DISCOVERY" if mechanism else "OBSERVATION",
            information_gain=information_gain,
            probe_id=probe_result.probe_id if probe_result else None,
            source_urls=[observation.source_url] if observation.source_url else [],
            source_grades=[observation.source_grade.value],
        )

    def generate_kernels(
        self,
        observations: list[Observation],
        hypotheses: list[Hypothesis] = None,
        probe_result: Optional[ProbeResult] = None,
    ) -> list[Kernel]:
        """Generate kernels from observations.

        Input: Observations + optional Hypotheses + optional ProbeResult
        Output: List of Kernels
        """
        if hypotheses is None:
            hypotheses = []

        # Build hypothesis lookup
        hypothesis_map = {h.hypothesis_id: h for h in hypotheses}

        kernels = []
        for obs in observations:
            # Find relevant hypothesis
            hypothesis = None
            if obs.hypothesis_id and obs.hypothesis_id in hypothesis_map:
                hypothesis = hypothesis_map[obs.hypothesis_id]

            # Generate kernel
            kernel = self.generate_kernel(obs, hypothesis, probe_result)
            kernels.append(kernel)

        return kernels

    def run(
        self,
        observations: list[Observation],
        hypotheses: list[Hypothesis] = None,
        probe_result: Optional[ProbeResult] = None,
    ) -> list[Kernel]:
        """Run the kernel generator pipeline.

        Input: Observations + Hypotheses + ProbeResult
        Output: List of Kernels
        """
        return self.generate_kernels(observations, hypotheses, probe_result)
