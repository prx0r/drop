"""
AI Product Expert (lightweight) — Data structures and logic for product
comparison, buyer need matching, and demand capture. No LLM calls.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from packages.schemas.candidate import Candidate


class BuyerNeedType(str, Enum):
    BUDGET_CONSTRAINED = "BUDGET_CONSTRAINED"
    FEATURE_SEEKING = "FEATURE_SEEKING"
    USE_CASE_SPECIFIC = "USE_CASE_SPECIFIC"
    COMPARISON_SHOPPER = "COMPARISON_SHOPPER"
    BRAND_LOYAL = "BRAND_LOYAL"
    IMPULSE_BUY = "IMPULSE_BUY"


class ConversionOutcome(str, Enum):
    PURCHASED = "PURCHASED"
    ABANDONED_CART = "ABANDONED_CART"
    BROWSED_ONLY = "BROWSED_ONLY"
    COMPETITOR_WON = "COMPETITOR_WON"
    TOO_EXPENSIVE = "TOO_EXPENSIVE"
    WRONG_PRODUCT = "WRONG_PRODUCT"
    UNKNOWN = "UNKNOWN"


@dataclass
class BuyerDemand:
    buyer_need_type: BuyerNeedType = BuyerNeedType.BUDGET_CONSTRAINED
    budget_range: tuple = (0.0, 0.0)
    feature_requirements: List[str] = field(default_factory=list)
    use_case: str = ""
    objections: List[str] = field(default_factory=list)
    products_compared: List[str] = field(default_factory=list)
    recommended_product: str = ""
    conversion_outcome: ConversionOutcome = ConversionOutcome.UNKNOWN
    captured_at: str = ""
    source: str = ""


@dataclass
class ProductProfile:
    candidate_id: str
    product_family: str
    sku: str
    price: float = 0.0
    features: List[str] = field(default_factory=list)
    target_use_cases: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    comparable_skus: List[str] = field(default_factory=list)


@dataclass
class ComparisonResult:
    product_a: str
    product_b: str
    price_difference: float = 0.0
    a_advantages: List[str] = field(default_factory=list)
    b_advantages: List[str] = field(default_factory=list)
    recommendation: str = ""
    reasoning: List[str] = field(default_factory=list)


@dataclass
class DemandCaptureResult:
    buyer_need_type: BuyerNeedType = BuyerNeedType.BUDGET_CONSTRAINED
    estimated_budget: float = 0.0
    key_features: List[str] = field(default_factory=list)
    best_match_candidate_id: str = ""
    match_score: float = 0.0
    reasoning: List[str] = field(default_factory=list)


class ProductExpert:
    """Lightweight product expert for comparison and demand matching."""

    def __init__(self):
        self.products: dict[str, ProductProfile] = {}
        self.demand_log: List[BuyerDemand] = []

    def register_product(self, candidate: Candidate) -> ProductProfile:
        """Register a candidate as a product profile."""
        profile = ProductProfile(
            candidate_id=candidate.candidate_id,
            product_family=candidate.product_family,
            sku=candidate.sku,
            price=candidate.selling_price,
            features=[],
            target_use_cases=[],
            strengths=[],
            weaknesses=[],
        )

        # Auto-detect strengths/weaknesses from economics
        if candidate.headroom_base >= 2.0:
            profile.strengths.append("Strong economics (headroom >= 2.0)")
        if candidate.headroom_base < 1.2:
            profile.weaknesses.append("Fragile economics (headroom < 1.2)")
        if candidate.supplier_reliability >= 0.7:
            profile.strengths.append(f"Reliable supplier ({candidate.supplier_reliability:.2f})")
        if candidate.supplier_reliability < 0.5:
            profile.weaknesses.append(f"Unreliable supplier ({candidate.supplier_reliability:.2f})")
        if candidate.shipping_days <= 7:
            profile.strengths.append(f"Fast shipping ({candidate.shipping_days} days)")
        if candidate.shipping_days > 14:
            profile.weaknesses.append(f"Slow shipping ({candidate.shipping_days} days)")
        if candidate.shopping_seller_count <= 5:
            profile.strengths.append(f"Low competition ({candidate.shopping_seller_count} sellers)")
        if candidate.shopping_seller_count > 15:
            profile.weaknesses.append(f"Saturated ({candidate.shopping_seller_count} sellers)")
        if candidate.merchant_differentiation_score >= 0.6:
            profile.strengths.append("Strong differentiation")
        if candidate.intent_score >= 0.7:
            profile.strengths.append(f"High buyer intent ({candidate.intent_score:.2f})")

        self.products[candidate.candidate_id] = profile
        return profile

    def compare_products(self, id_a: str, id_b: str) -> Optional[ComparisonResult]:
        """Compare two products side by side."""
        a = self.products.get(id_a)
        b = self.products.get(id_b)
        if not a or not b:
            return None

        result = ComparisonResult(product_a=a.product_family, product_b=b.product_family)
        result.price_difference = a.price - b.price

        if a.price < b.price:
            result.a_advantages.append(f"${abs(result.price_difference):.2f} cheaper")
            result.b_advantages.append("Higher price point (perceived quality)")
        elif b.price < a.price:
            result.b_advantages.append(f"${abs(result.price_difference):.2f} cheaper")
            result.a_advantages.append("Higher price point (perceived quality)")

        a_strengths = set(a.strengths)
        b_strengths = set(b.strengths)
        result.a_advantages.extend(list(a_strengths - b_strengths))
        result.b_advantages.extend(list(b_strengths - a_strengths))

        a_weak = set(a.weaknesses)
        b_weak = set(b.weaknesses)
        result.b_advantages.extend([f"Competitor weakness: {w}" for w in a_weak - b_weak])
        result.a_advantages.extend([f"Competitor weakness: {w}" for w in b_weak - a_weak])

        if len(result.a_advantages) > len(result.b_advantages):
            result.recommendation = a.product_family
            result.reasoning.append(f"{a.product_family} has {len(result.a_advantages)} advantages vs {len(result.b_advantages)}")
        elif len(result.b_advantages) > len(result.a_advantages):
            result.recommendation = b.product_family
            result.reasoning.append(f"{b.product_family} has {len(result.b_advantages)} advantages vs {len(result.a_advantages)}")
        else:
            result.recommendation = "TIE"
            result.reasoning.append("Both products have equal advantages")

        return result

    def answer_buyer_need(
        self,
        need_type: BuyerNeedType,
        budget: float = 0.0,
        features: Optional[List[str]] = None,
        use_case: str = "",
    ) -> DemandCaptureResult:
        """Recommend products based on buyer requirements."""
        result = DemandCaptureResult(
            buyer_need_type=need_type,
            estimated_budget=budget,
            key_features=features or [],
        )

        best_id = ""
        best_score = 0.0
        reasoning = []

        for pid, profile in self.products.items():
            score = 0.0

            # Budget match
            if need_type == BuyerNeedType.BUDGET_CONSTRAINED and budget > 0:
                if profile.price <= budget:
                    score += 0.4
                    reasoning.append(f"{profile.product_family}: within budget (${profile.price:.2f} <= ${budget:.2f})")
                else:
                    score -= 0.2
                    reasoning.append(f"{profile.product_family}: over budget")

            # Feature match
            if features:
                matched = sum(1 for f in features if any(f.lower() in s.lower() for s in profile.strengths))
                score += (matched / len(features)) * 0.3

            # Strength bonus
            score += len(profile.strengths) * 0.05
            score -= len(profile.weaknesses) * 0.05

            if score > best_score:
                best_score = score
                best_id = pid

        result.best_match_candidate_id = best_id
        result.match_score = best_score
        result.reasoning = reasoning
        return result

    def capture_demand(self, demand: BuyerDemand) -> None:
        """Capture structured customer demand as research data."""
        self.demand_log.append(demand)

    def get_demand_summary(self) -> dict:
        """Summarize captured demand data."""
        if not self.demand_log:
            return {"total_captures": 0}

        by_need = {}
        by_outcome = {}
        for d in self.demand_log:
            need = d.buyer_need_type.value
            outcome = d.conversion_outcome.value
            by_need[need] = by_need.get(need, 0) + 1
            by_outcome[outcome] = by_outcome.get(outcome, 0) + 1

        return {
            "total_captures": len(self.demand_log),
            "by_need_type": by_need,
            "by_outcome": by_outcome,
        }
