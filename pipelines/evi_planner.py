"""Pipeline 4: EVI Research Planner

Unknowns → Research priority queue

Input: List[UnknownField], Candidate
Output: List[ResearchEVI] (ranked by Expected Value of Information)

This pipeline:
1. Takes unknown fields for a candidate
2. Calculates EVI for each unknown
3. Returns ranked research priorities

Side effects: NONE. Pure transform.
"""

from __future__ import annotations

from typing import Optional

from schemas.observation import UnknownField
from schemas.candidate import Candidate
from schemas.probe import ResearchEVI


class EVIPlannerPipeline:
    """Unknowns → Research priority queue.

    Pure transform. No I/O.
    """

    # Research cost estimates by resolution method
    RESEARCH_COSTS = {
        "serp_check": 0.1,  # Quick Google search
        "retailer_scrape": 0.2,  # Check a retailer site
        "comparison_site": 0.15,  # Check Prisjakt/Hinta.fi
        "forum_search": 0.2,  # Search forums
        "email_supplier": 0.5,  # Email a supplier (human time)
        "phone_supplier": 0.7,  # Call a supplier (human time)
        "create_account": 0.4,  # Create a dealer account
        "trade_association": 0.3,  # Check trade association
        "regulatory_check": 0.3,  # Check regulations
        "unknown": 0.5,  # Default
    }

    def estimate_resolve_probability(
        self,
        unknown: UnknownField,
        candidate: Candidate,
    ) -> float:
        """Estimate probability that this unknown can be resolved.

        Returns 0-1.
        """
        # Higher probability if resolution path is clear
        if unknown.resolution_path and "email" in unknown.resolution_path.lower():
            return 0.7  # Email has ~70% response rate
        if unknown.resolution_path and "serp" in unknown.resolution_path.lower():
            return 0.9  # SERP is usually available
        if unknown.resolution_path and "retailer" in unknown.resolution_path.lower():
            return 0.8  # Retailer sites are usually available

        # Lower probability if blocked
        if unknown.is_blocked:
            return 0.2

        # Default
        return 0.5

    def estimate_decision_impact(
        self,
        unknown: UnknownField,
        candidate: Candidate,
    ) -> float:
        """Estimate how much resolving this unknown would change the decision.

        Returns 0-1.
        """
        # High impact fields
        high_impact_fields = {
            "dealer_price",
            "contribution_margin",
            "reseller_eligibility",
            "territorial_restriction",
            "rma_responsibility",
            "stock_feed",
            "warranty_obligation",
        }

        if unknown.field in high_impact_fields:
            return 0.9

        # Medium impact fields
        medium_impact_fields = {
            "supplier_name",
            "shipping_cost",
            "lead_time",
            "moq",
            "payment_terms",
        }

        if unknown.field in medium_impact_fields:
            return 0.6

        # Low impact fields
        return 0.3

    def estimate_candidate_value(
        self,
        candidate: Candidate,
    ) -> float:
        """Estimate how valuable this candidate is.

        Returns 0-1.
        """
        # Higher value if candidate has progress
        progress = candidate.progress
        if progress > 0.7:
            return 0.9
        if progress > 0.4:
            return 0.6
        return 0.3

    def estimate_research_cost(
        self,
        unknown: UnknownField,
    ) -> float:
        """Estimate the cost of researching this unknown.

        Returns 0-1.
        """
        if unknown.research_cost is not None:
            return unknown.research_cost

        # Try to infer from resolution path
        if unknown.resolution_path:
            path_lower = unknown.resolution_path.lower()
            for method, cost in self.RESEARCH_COSTS.items():
                if method.replace("_", " ") in path_lower:
                    return cost

        return self.RESEARCH_COSTS["unknown"]

    def calculate_evi(
        self,
        unknown: UnknownField,
        candidate: Candidate,
    ) -> ResearchEVI:
        """Calculate Expected Value of Information for an unknown.

        EVI = P(resolve) * decision_impact * candidate_value / research_cost
        """
        p_resolve = self.estimate_resolve_probability(unknown, candidate)
        impact = self.estimate_decision_impact(unknown, candidate)
        value = self.estimate_candidate_value(candidate)
        cost = self.estimate_research_cost(unknown)

        # Generate recommended action
        action = self._recommend_action(unknown)
        rationale = self._generate_rationale(unknown, p_resolve, impact, value, cost)

        return ResearchEVI(
            field=unknown.field,
            candidate_id=unknown.candidate_id,
            hypothesis_id=None,
            probability_of_resolve=p_resolve,
            decision_impact=impact,
            candidate_value=value,
            research_cost=cost,
            recommended_action=action,
            rationale=rationale,
        )

    def _recommend_action(self, unknown: UnknownField) -> str:
        """Recommend a specific research action."""
        if unknown.resolution_path:
            return unknown.resolution_path

        # Default actions based on field type
        field_actions = {
            "dealer_price": "Email supplier with 1/5/10-unit quote request",
            "reseller_eligibility": "Check supplier website for dealer application",
            "territorial_restriction": "Email supplier asking about territory restrictions",
            "rma_responsibility": "Email supplier asking about RMA process",
            "stock_feed": "Check if supplier offers API or CSV stock feed",
            "shipping_cost": "Check shipping calculator on supplier site",
            "lead_time": "Check supplier website or email for lead times",
            "moq": "Email supplier asking about minimum order quantities",
        }

        return field_actions.get(unknown.field, "Research this unknown")

    def _generate_rationale(
        self,
        unknown: UnknownField,
        p_resolve: float,
        impact: float,
        value: float,
        cost: float,
    ) -> str:
        """Generate human-readable rationale."""
        evi = (p_resolve * impact * value / cost) if cost > 0 else float("inf")

        parts = [
            f"Resolving '{unknown.field}' has EVI={evi:.2f}",
            f"P(resolve)={p_resolve:.1%}",
            f"decision_impact={impact:.1%}",
            f"candidate_value={value:.1%}",
            f"research_cost={cost:.1%}",
        ]

        if unknown.decision_dependency:
            parts.append(f"Blocks: {unknown.decision_dependency}")

        return " | ".join(parts)

    def rank_unknowns(
        self,
        unknowns: list[UnknownField],
        candidate: Candidate,
    ) -> list[ResearchEVI]:
        """Rank unknowns by EVI.

        Returns sorted list (highest EVI first).
        """
        evi_list = []
        for unknown in unknowns:
            evi = self.calculate_evi(unknown, candidate)
            evi_list.append(evi)

        # Sort by EVI (highest first)
        evi_list.sort(key=lambda x: x.evi, reverse=True)
        return evi_list

    def run(
        self,
        unknowns: list[UnknownField],
        candidate: Candidate,
    ) -> list[ResearchEVI]:
        """Run the EVI planner pipeline.

        Input: Unknowns + Candidate
        Output: Ranked ResearchEVI list
        """
        return self.rank_unknowns(unknowns, candidate)
