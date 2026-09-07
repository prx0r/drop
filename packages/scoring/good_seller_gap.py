#!/usr/bin/env python3
"""
Good Seller Gap Model
=====================
Frozen feature model for prospective validation.
The central meta-thesis: merchant quality gap predicts profit per qualified click.

From the critique:
> "Before seeing store outcomes, score every competing merchant using a frozen rubric
> measuring things such as local payment support, delivery-choice quality, checkout
> transparency, pricing, stock, product expertise, comparisons, compatibility assistance,
> returns, warranty, merchant trust and customer support."

This is a FROZEN model — changes require explicit version bumps and re-validation.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import json
from pathlib import Path


class MerchantQualityDimension(Enum):
    """16 dimensions for scoring merchant quality."""
    IMAGE_QUALITY = "image_quality"
    PRODUCT_INFO = "product_info"
    DECISION_SUPPORT = "decision_support"
    SHIPPING_CLARITY = "shipping_clarity"
    STOCK_AVAILABILITY = "stock_availability"
    LOCALIZATION = "localization"
    REVIEWS = "reviews"
    TRUST = "trust"
    ACCESSORIES = "accessories"
    MOBILE_SPEED = "mobile_speed"
    LOCAL_PAYMENT = "local_payment"
    DELIVERY_CHOICES = "delivery_choices"
    RETURNS_CLARITY = "returns_clarity"
    WARRANTY_INFO = "warranty_info"
    EXPERT_GUIDANCE = "expert_guidance"
    COMPARISON_CONTENT = "comparison_content"


@dataclass
class MerchantScore:
    """Score for a single merchant."""
    merchant_name: str
    merchant_url: str
    scores: Dict[str, int] = field(default_factory=dict)  # dimension -> 0-10
    total_score: float = 0.0
    is_good: bool = False  # total_score >= 70
    
    def calculate_total(self):
        """Calculate weighted total score."""
        weights = {
            MerchantQualityDimension.IMAGE_QUALITY: 0.08,
            MerchantQualityDimension.PRODUCT_INFO: 0.10,
            MerchantQualityDimension.DECISION_SUPPORT: 0.12,
            MerchantQualityDimension.SHIPPING_CLARITY: 0.08,
            MerchantQualityDimension.STOCK_AVAILABILITY: 0.08,
            MerchantQualityDimension.LOCALIZATION: 0.10,
            MerchantQualityDimension.REVIEWS: 0.08,
            MerchantQualityDimension.TRUST: 0.10,
            MerchantQualityDimension.ACCESSORIES: 0.05,
            MerchantQualityDimension.MOBILE_SPEED: 0.05,
            MerchantQualityDimension.LOCAL_PAYMENT: 0.08,
            MerchantQualityDimension.DELIVERY_CHOICES: 0.05,
            MerchantQualityDimension.RETURNS_CLARITY: 0.05,
            MerchantQualityDimension.WARRANTY_INFO: 0.05,
            MerchantQualityDimension.EXPERT_GUIDANCE: 0.07,
            MerchantQualityDimension.COMPARISON_CONTENT: 0.04,
        }
        
        total = 0
        for dim, weight in weights.items():
            total += self.scores.get(dim.value, 0) * weight * 10
        
        self.total_score = total
        self.is_good = total >= 70
        return total


@dataclass
class GoodSellerGap:
    """The core metric: how much better could we do than existing sellers?"""
    
    # Demand signals
    demand_score: float  # 0-100, from keyword volume, trends, etc.
    
    # Existing seller landscape
    total_sellers: int
    good_sellers: int  # Merchors scoring >= 70/100
    excellent_sellers: int  # Merchors scoring >= 85/100
    poor_sellers: int  # Merchors scoring < 40/100
    
    # Our planned merchant quality (what we aim to build)
    planned_merchant_score: float  # 0-100
    
    # Gap calculation
    gap_score: float = 0.0
    
    def calculate_gap(self):
        """
        Calculate the Good Seller Gap.
        
        Core insight: demand × (1 / good_sellers) × merchant_weakness
        
        High demand + few good sellers + weak existing merchants = large gap
        """
        # Demand factor (normalized 0-1)
        demand_factor = self.demand_score / 100
        
        # Seller gap factor (inverse of good seller density)
        if self.good_sellers == 0:
            seller_gap = 2.0  # No good sellers = maximum gap
        elif self.good_sellers <= 2:
            seller_gap = 1.5
        elif self.good_sellers <= 5:
            seller_gap = 1.0
        else:
            seller_gap = max(0.2, 5.0 / self.good_sellers)
        
        # Merchant weakness factor (how much room for improvement)
        avg_existing = (self.good_sellers * 75 + self.poor_sellers * 25) / max(1, self.total_sellers)
        weakness = max(0, (100 - avg_existing) / 100)
        
        # Our advantage (how much better we plan to be)
        advantage = max(0, (self.planned_merchant_score - avg_existing) / 100)
        
        # Composite score
        self.gap_score = demand_factor * seller_gap * weakness * advantage * 100
        
        return self.gap_score
    
    def to_dict(self) -> dict:
        return {
            "demand_score": self.demand_score,
            "total_sellers": self.total_sellers,
            "good_sellers": self.good_sellers,
            "excellent_sellers": self.excellent_sellers,
            "poor_sellers": self.poor_sellers,
            "planned_merchant_score": self.planned_merchant_score,
            "gap_score": self.gap_score,
        }


def score_merchant_quality(
    merchant_url: str,
    merchant_name: str,
    scores: Dict[str, int]
) -> MerchantScore:
    """Score a single merchant on 16 dimensions."""
    ms = MerchantScore(
        merchant_name=merchant_name,
        merchant_url=merchant_url,
        scores=scores
    )
    ms.calculate_total()
    return ms


def calculate_good_seller_gap(
    product_category: str,
    country: str,
    total_sellers: int,
    merchant_scores: List[MerchantScore],
    planned_merchant_score: float = 80,
    demand_score: float = 50
) -> GoodSellerGap:
    """
    Calculate the Good Seller Gap for a product × country.
    
    Args:
        product_category: e.g., "heat_pump_aftermarket"
        country: e.g., "FI"
        total_sellers: Total number of sellers found
        merchant_scores: List of MerchantScore objects for each seller
        planned_merchant_score: What we aim to build (default 80)
        demand_score: Demand signal (0-100)
    """
    good = sum(1 for m in merchant_scores if m.is_good)
    excellent = sum(1 for m in merchant_scores if m.total_score >= 85)
    poor = sum(1 for m in merchant_scores if m.total_score < 40)
    
    gap = GoodSellerGap(
        demand_score=demand_score,
        total_sellers=total_sellers,
        good_sellers=good,
        excellent_sellers=excellent,
        poor_sellers=poor,
        planned_merchant_score=planned_merchant_score,
    )
    gap.calculate_gap()
    
    return gap


# --- Example usage ---
if __name__ == "__main__":
    print("=== Good Seller Gap Model v1.0 ===\n")
    
    # Example: Finnish heat pump aftermarket
    merchants = [
        score_merchant_quality("kataikko.fi", "Kataikko Oy", {
            "image_quality": 7, "product_info": 8, "decision_support": 6,
            "shipping_clarity": 7, "stock_availability": 8, "localization": 9,
            "reviews": 5, "trust": 8, "accessories": 6, "mobile_speed": 7,
            "local_payment": 8, "delivery_choices": 7, "returns_clarity": 6,
            "warranty_info": 7, "expert_guidance": 8, "comparison_content": 4,
        }),
        score_merchant_quality("gigantti.fi", "Gigantti", {
            "image_quality": 8, "product_info": 7, "decision_support": 5,
            "shipping_clarity": 8, "stock_availability": 9, "localization": 9,
            "reviews": 7, "trust": 9, "accessories": 5, "mobile_speed": 8,
            "local_payment": 9, "delivery_choices": 8, "returns_clarity": 7,
            "warranty_info": 7, "expert_guidance": 4, "comparison_content": 5,
        }),
        score_merchant_quality("csmegastore.fi", "CS Megastore", {
            "image_quality": 6, "product_info": 6, "decision_support": 4,
            "shipping_clarity": 6, "stock_availability": 7, "localization": 8,
            "reviews": 5, "trust": 7, "accessories": 4, "mobile_speed": 6,
            "local_payment": 7, "delivery_choices": 6, "returns_clarity": 5,
            "warning_info": 5, "expert_guidance": 3, "comparison_content": 3,
        }),
    ]
    
    print("Merchant Scores:")
    for m in merchants:
        print(f"  {m.merchant_name:20} → {m.total_score:.1f}/100 {'GOOD' if m.is_good else 'WEAK'}")
    
    gap = calculate_good_seller_gap(
        product_category="heat_pump_aftermarket",
        country="FI",
        total_sellers=12,
        merchant_scores=merchants,
        planned_merchant_score=85,
        demand_score=80
    )
    
    print(f"\nGood Seller Gap:")
    print(f"  Total sellers: {gap.total_sellers}")
    print(f"  Good sellers: {gap.good_sellers}")
    print(f"  Excellent sellers: {gap.excellent_sellers}")
    print(f"  Poor sellers: {gap.poor_sellers}")
    print(f"  Demand score: {gap.demand_score}")
    print(f"  Planned score: {gap.planned_merchant_score}")
    print(f"  GAP SCORE: {gap.gap_score:.1f}")
    
    # Verdict
    if gap.gap_score >= 50:
        print(f"\n→ STRONG OPPORTUNITY (gap >= 50)")
    elif gap.gap_score >= 25:
        print(f"\n→ MODERATE OPPORTUNITY (gap 25-50)")
    else:
        print(f"\n→ WEAK OPPORTUNITY (gap < 25)")
