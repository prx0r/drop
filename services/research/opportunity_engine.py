"""
MythicBee Drop — Opportunity Research Engine
Finds and scores product opportunities based on search demand + economics
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class Product:
    """A candidate product opportunity"""
    sku: str
    name: str
    category: str
    country: str
    supplier_price: float
    selling_price: float
    shipping_cost: float
    search_volume: int = 0
    competition_score: float = 0.0
    source: str = ""
    grade: str = "C"

@dataclass
class EconomicModel:
    """Economic calculations for a product"""
    landed_cost: float
    selling_price: float
    pre_ad_contribution: float
    payment_fees: float
    expected_refunds: float
    expected_cvr: float
    expected_cpc: float
    break_even_cvr: float
    break_even_cpc: float
    expected_profit_per_click: float
    economic_headroom: float
    confidence: str

@dataclass
class OpportunityScore:
    """Final scored opportunity"""
    product: Product
    economics: EconomicModel
    score: float
    confidence: str
    tags: List[str]
    why_it_might_work: str
    why_it_might_fail: str
    largest_unknown: str
    cheapest_way_to_test: str

class OpportunityEngine:
    def __init__(self):
        self.products = []
        self.scores = []
    
    def calculate_economics(self, product: Product) -> EconomicModel:
        """Calculate economic model for a product"""
        # Landed cost
        landed_cost = product.supplier_price + product.shipping_cost
        
        # Pre-ad contribution
        payment_fees = product.selling_price * 0.029 + 0.20  # Stripe/PayPal
        expected_refunds = product.selling_price * 0.05  # 5% refund rate
        pre_ad_contribution = product.selling_price - landed_cost - payment_fees - expected_refunds
        
        # CVR assumptions
        pessimistic_cvr = 0.002
        base_cvr = 0.005
        optimistic_cvr = 0.01
        
        # CPC assumptions
        pessimistic_cpc = 2.0
        base_cpc = 1.0
        optimistic_cpc = 0.5
        
        # Break-even calculations
        break_even_cvr = base_cpc / pre_ad_contribution if pre_ad_contribution > 0 else 999
        break_even_cpc = base_cvr * pre_ad_contribution if pre_ad_contribution > 0 else 0
        
        # Expected profit per click
        expected_profit = (base_cvr * pre_ad_contribution) - base_cpc
        
        # Economic headroom
        headroom = (base_cvr * pre_ad_contribution) / base_cpc if base_cpc > 0 else 0
        
        # Confidence
        if headroom >= 2.0: confidence = "STRONG"
        elif headroom >= 1.5: confidence = "INTERESTING"
        elif headroom >= 1.25: confidence = "MARGINAL"
        else: confidence = "WEAK"
        
        return EconomicModel(
            landed_cost=landed_cost,
            selling_price=product.selling_price,
            pre_ad_contribution=pre_ad_contribution,
            payment_fees=payment_fees,
            expected_refunds=expected_refunds,
            expected_cvr=base_cvr,
            expected_cpc=base_cpc,
            break_even_cvr=break_even_cvr,
            break_even_cpc=break_even_cpc,
            expected_profit_per_click=expected_profit,
            economic_headroom=headroom,
            confidence=confidence
        )
    
    def score_opportunity(self, product: Product) -> OpportunityScore:
        """Score a product opportunity"""
        economics = self.calculate_economics(product)
        
        # Score components
        economics_score = min(economics.economic_headroom / 2.0, 1.0) * 35
        demand_score = min(product.search_volume / 10000, 1.0) * 20
        competition_score = (1 - product.competition_score) * 15
        supplier_score = 0.8 * 15  # Default supplier quality
        differentiation_score = 0.7 * 10
        trend_score = 0.5 * 5
        
        total_score = economics_score + demand_score + competition_score + supplier_score + differentiation_score + trend_score
        
        # Tags
        tags = []
        if economics.economic_headroom >= 2.0: tags.append("STRONG_ECONOMICS")
        if economics.economic_headroom >= 1.5: tags.append("INTERESTING")
        if product.search_volume > 5000: tags.append("HIGH_DEMAND")
        if product.competition_score < 0.3: tags.append("LOW_COMPETITION")
        if product.selling_price > 200: tags.append("HIGH_TICKET")
        
        # Why it might work/fail
        why_work = f"Good economics (headroom {economics.economic_headroom:.1f}x)"
        if product.search_volume > 5000: why_work += ", strong search demand"
        
        why_fail = "Low CVR possible"
        if economics.economic_headroom < 1.5: why_fail = "Tight economics"
        
        return OpportunityScore(
            product=product,
            economics=economics,
            score=total_score,
            confidence=economics.confidence,
            tags=tags,
            why_it_might_work=why_work,
            why_it_might_fail=why_fail,
            largest_unknown="Real CVR with our landing page",
            cheapest_way_to_test="$10/day Google Shopping for 7 days"
        )
    
    def rank_opportunities(self) -> List[OpportunityScore]:
        """Rank all opportunities by score"""
        self.scores = [self.score_opportunity(p) for p in self.products]
        self.scores.sort(key=lambda x: x.score, reverse=True)
        return self.scores

# Test with sample data
engine = OpportunityEngine()

# Add sample products
engine.products = [
    Product("SKU001", "Red-light therapy mask", "Health", "US", 50, 289, 15, 8000, 0.4),
    Product("SKU002", "Lumbar support pillow", "Home", "US", 25, 64.99, 10, 5000, 0.3),
    Product("SKU003", "Baby stroller", "Baby", "US", 150, 450, 25, 12000, 0.5),
    Product("SKU004", "Coffee grinder", "Kitchen", "US", 80, 299, 12, 8000, 0.35),
    Product("SKU005", "Yoga mat premium", "Fitness", "US", 30, 89, 8, 15000, 0.6),
]

# Rank opportunities
scores = engine.rank_opportunities()

print("=== Top Opportunities ===")
for i, s in enumerate(scores[:5]):
    print(f"\n{i+1}. {s.product.name}")
    print(f"   Score: {s.score:.1f}")
    print(f"   Economics: {s.economics.confidence} (headroom {s.economics.economic_headroom:.1f}x)")
    print(f"   Price: ${s.product.selling_price} | Cost: ${s.economics.landed_cost:.2f} | Contribution: ${s.economics.pre_ad_contribution:.2f}")
    print(f"   Tags: {', '.join(s.tags)}")
    print(f"   Why work: {s.why_it_might_work}")
