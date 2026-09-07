"""
Auction Room Explanation Generator — Generates the "WHY DOES THIS AUCTION
HAVE ROOM FOR US?" paragraph with specific numbers.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from packages.schemas.candidate import Candidate
from packages.economics.model import calculate_economics


@dataclass
class AuctionExplanation:
    candidate_id: str
    product_family: str
    contribution_margin: float = 0.0
    break_even_cvr: float = 0.0
    expected_cpc: float = 0.0
    headroom: float = 0.0
    query_specificity: float = 0.0
    seller_count: int = 0
    price_positioning: str = ""
    shipping_advantage: str = ""
    supplier_selectivity: str = ""
    main_uncertainty: str = ""
    cheapest_next_test: str = ""
    explanation_paragraph: str = ""
    reasoning: List[str] = field(default_factory=list)


def generate_auction_explanation(
    c: Candidate,
    cheapest_test: str = "ENABLE_FREE_LISTING ($0)",
    market_avg_price: float = 0.0,
) -> AuctionExplanation:
    """
    Generate a detailed auction explanation with specific numbers.
    Answers: WHY DOES THIS AUCTION HAVE ROOM FOR US?
    """
    expl = AuctionExplanation(
        candidate_id=c.candidate_id,
        product_family=c.product_family,
    )

    # Contribution margin
    expl.contribution_margin = c.pre_ad_contribution
    expl.break_even_cvr = c.break_even_cvr
    expl.expected_cpc = c.expected_cpc
    expl.headroom = c.headroom_base
    expl.query_specificity = c.exact_query_share
    expl.seller_count = c.shopping_seller_count
    expl.cheapest_next_test = cheapest_test

    # Price positioning
    if market_avg_price > 0 and c.selling_price > 0:
        price_ratio = c.selling_price / market_avg_price
        if price_ratio < 0.85:
            expl.price_positioning = f"We're {((1 - price_ratio) * 100):.0f}% below market average"
        elif price_ratio > 1.15:
            expl.price_positioning = f"We're {((price_ratio - 1) * 100):.0f}% above market average (premium positioning)"
        else:
            expl.price_positioning = f"Price within {abs(price_ratio - 1) * 100:.0f}% of market average"
    else:
        expl.price_positioning = "No market price data"

    # Shipping advantage
    if c.shipping_days <= 7:
        expl.shipping_advantage = f"Fast shipping ({c.shipping_days} days) vs market avg ~14 days"
    elif c.shipping_days <= 14:
        expl.shipping_advantage = f"Standard shipping ({c.shipping_days} days)"
    else:
        expl.shipping_advantage = f"Slow shipping ({c.shipping_days} days) — competitive disadvantage"

    if c.shipping_gap_vs_market > 0:
        expl.shipping_advantage += f", {c.shipping_gap_vs_market} days slower than competitors"
    elif c.shipping_gap_vs_market == 0:
        expl.shipping_advantage += ", on par with competitors"

    # Supplier selectivity
    if c.supplier_selectivity == "selective":
        expl.supplier_selectivity = "Selective supplier — limits competition"
    elif c.supplier_selectivity == "open":
        expl.supplier_selectivity = "Open supplier — others can source same product"
    else:
        expl.supplier_selectivity = f"Supplier selectivity: {c.supplier_selectivity or 'unknown'}"

    # Main uncertainty
    uncertainties = []
    if c.cvr_confidence.value in ["VERY_LOW", "LOW"]:
        uncertainties.append(f"CVR is the key unknown (confidence: {c.cvr_confidence.value})")
    if c.cpc_confidence_domain.value in ["VERY_LOW", "LOW"]:
        uncertainties.append(f"CPC estimate is uncertain ({c.cpc_confidence_domain.value} confidence)")
    if c.observed_clicks == 0:
        uncertainties.append("Zero observed traffic — no empirical data yet")
    elif c.observed_clicks < 100:
        uncertainties.append(f"Only {c.observed_clicks} clicks — insufficient data")
    expl.main_uncertainty = "; ".join(uncertainties) if uncertainties else "Economics well-understood"

    # Build the explanation paragraph
    paragraph_parts = []

    paragraph_parts.append(
        f"{c.product_family} has a ${c.pre_ad_contribution:.2f} contribution margin "
        f"after all costs (landed, shipping, payment fees, expected returns)."
    )

    if c.headroom_base >= 1.0:
        paragraph_parts.append(
            f"At base CVR ({c.cvr_base:.2%}), headroom is {c.headroom_base:.2f}x — "
            f"meaning we generate ${c.headroom_base:.2f} for every ${1.00} spent on ads."
        )
    else:
        paragraph_parts.append(
            f"At base CVR ({c.cvr_base:.2%}), headroom is only {c.headroom_base:.2f}x — "
            f"marginally viable, needs optimistic CVR scenario to work."
        )

    paragraph_parts.append(
        f"Break-even CVR is {c.break_even_cvr:.2%} at ${c.expected_cpc:.2f} CPC — "
        f"{'achievable' if c.break_even_cvr < 0.02 else 'challenging' if c.break_even_cvr < 0.05 else 'very difficult'} "
        f"for cold traffic."
    )

    if c.shopping_seller_count <= 5:
        paragraph_parts.append(
            f"Only {c.shopping_seller_count} Shopping sellers for this GTIN — "
            f"{'blue ocean' if c.shopping_seller_count == 0 else 'low competition'}."
        )
    elif c.shopping_seller_count <= 15:
        paragraph_parts.append(
            f"{c.shopping_seller_count} Shopping sellers — moderate competition."
        )
    else:
        paragraph_parts.append(
            f"{c.shopping_seller_count} Shopping sellers — heavily saturated."
        )

    if c.exact_query_share > 0.3:
        paragraph_parts.append(
            f"Query specificity is strong: {c.exact_query_share:.0%} exact query share "
            f"means buyers know what they want."
        )
    elif c.exact_query_share > 0.1:
        paragraph_parts.append(
            f"Query specificity is moderate: {c.exact_query_share:.0%} exact query share."
        )
    else:
        paragraph_parts.append(
            f"Query specificity is low: {c.exact_query_share:.0%} exact query share — "
            f"generic traffic dominates."
        )

    paragraph_parts.append(f"{expl.shipping_advantage}.")
    paragraph_parts.append(f"{expl.supplier_selectivity}.")

    paragraph_parts.append(
        f"Main uncertainty: {expl.main_uncertainty}."
    )

    paragraph_parts.append(
        f"Cheapest next test: {expl.cheapest_next_test}."
    )

    expl.explanation_paragraph = " ".join(paragraph_parts)
    expl.reasoning = paragraph_parts

    return expl
