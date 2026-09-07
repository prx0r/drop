"""
Country Selection Algorithm — Algorithmic country selection based on
CPC, demand, price, competition, shipping, tax, supplier, language.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CountryProfile:
    code: str
    name: str
    cpc_estimate: float = 0.0
    search_demand_monthly: int = 0
    avg_market_price: float = 0.0
    exact_sku_sellers: int = 0
    shipping_days_from_origin: int = 0
    shipping_cost: float = 0.0
    tax_burden: float = 0.0
    compliance_burden: str = "LOW"
    supplier_availability: float = 0.5
    language_advantage: float = 0.0
    currency: str = "USD"


@dataclass
class CountryScore:
    country: str
    composite_score: float = 0.0
    rank: int = 0
    component_scores: dict = field(default_factory=dict)
    reasoning: List[str] = field(default_factory=list)


DEFAULT_COUNTRIES = [
    CountryProfile(
        code="US", name="United States",
        cpc_estimate=1.20, search_demand_monthly=50000,
        avg_market_price=80.0, exact_sku_sellers=8,
        shipping_days_from_origin=12, shipping_cost=8.0,
        tax_burden=0.0, compliance_burden="LOW",
        supplier_availability=0.8, language_advantage=1.0,
        currency="USD",
    ),
    CountryProfile(
        code="UK", name="United Kingdom",
        cpc_estimate=0.95, search_demand_monthly=30000,
        avg_market_price=65.0, exact_sku_sellers=5,
        shipping_days_from_origin=14, shipping_cost=10.0,
        tax_burden=0.20, compliance_burden="MEDIUM",
        supplier_availability=0.7, language_advantage=1.0,
        currency="GBP",
    ),
    CountryProfile(
        code="DE", name="Germany",
        cpc_estimate=0.80, search_demand_monthly=25000,
        avg_market_price=70.0, exact_sku_sellers=6,
        shipping_days_from_origin=14, shipping_cost=10.0,
        tax_burden=0.19, compliance_burden="MEDIUM",
        supplier_availability=0.6, language_advantage=0.0,
        currency="EUR",
    ),
    CountryProfile(
        code="NO", name="Norway",
        cpc_estimate=1.50, search_demand_monthly=8000,
        avg_market_price=90.0, exact_sku_sellers=2,
        shipping_days_from_origin=16, shipping_cost=15.0,
        tax_burden=0.25, compliance_burden="HIGH",
        supplier_availability=0.4, language_advantage=0.0,
        currency="NOK",
    ),
    CountryProfile(
        code="SE", name="Sweden",
        cpc_estimate=1.10, search_demand_monthly=10000,
        avg_market_price=80.0, exact_sku_sellers=3,
        shipping_days_from_origin=15, shipping_cost=12.0,
        tax_burden=0.25, compliance_burden="MEDIUM",
        supplier_availability=0.5, language_advantage=0.0,
        currency="SEK",
    ),
    CountryProfile(
        code="DK", name="Denmark",
        cpc_estimate=1.20, search_demand_monthly=7000,
        avg_market_price=85.0, exact_sku_sellers=2,
        shipping_days_from_origin=15, shipping_cost=13.0,
        tax_burden=0.25, compliance_burden="MEDIUM",
        supplier_availability=0.5, language_advantage=0.0,
        currency="DKK",
    ),
    CountryProfile(
        code="NL", name="Netherlands",
        cpc_estimate=0.85, search_demand_monthly=15000,
        avg_market_price=70.0, exact_sku_sellers=4,
        shipping_days_from_origin=13, shipping_cost=9.0,
        tax_burden=0.21, compliance_burden="MEDIUM",
        supplier_availability=0.6, language_advantage=0.0,
        currency="EUR",
    ),
    CountryProfile(
        code="AU", name="Australia",
        cpc_estimate=1.00, search_demand_monthly=20000,
        avg_market_price=85.0, exact_sku_sellers=4,
        shipping_days_from_origin=18, shipping_cost=14.0,
        tax_burden=0.10, compliance_burden="LOW",
        supplier_availability=0.6, language_advantage=1.0,
        currency="AUD",
    ),
    CountryProfile(
        code="CA", name="Canada",
        cpc_estimate=0.90, search_demand_monthly=22000,
        avg_market_price=75.0, exact_sku_sellers=5,
        shipping_days_from_origin=12, shipping_cost=9.0,
        tax_burden=0.05, compliance_burden="LOW",
        supplier_availability=0.7, language_advantage=1.0,
        currency="CAD",
    ),
    CountryProfile(
        code="FR", name="France",
        cpc_estimate=0.75, search_demand_monthly=20000,
        avg_market_price=65.0, exact_sku_sellers=5,
        shipping_days_from_origin=14, shipping_cost=10.0,
        tax_burden=0.20, compliance_burden="MEDIUM",
        supplier_availability=0.6, language_advantage=0.0,
        currency="EUR",
    ),
]


def score_country(
    profile: CountryProfile,
    product_price: float = 0.0,
    target_sku_sellers: int = 0,
) -> CountryScore:
    """
    Score a country for product viability.

    Weights:
    - CPC (inverted): 25% — lower CPC is better
    - Search demand: 20% — higher demand is better
    - Price margin: 15% — market price vs our cost
    - Competition: 15% — fewer sellers is better
    - Shipping: 10% — faster and cheaper is better
    - Tax/compliance: 5% — lower burden is better
    - Supplier availability: 5% — more suppliers is better
    - Language: 5% — language advantage helps
    """
    cs = CountryScore(country=profile.code)
    reasons: List[str] = []

    # CPC score (inverted: lower CPC = higher score)
    if profile.cpc_estimate > 0:
        cpc_score = min(1.0, 2.0 / profile.cpc_estimate)  # $0.50 CPC = 1.0, $2.0 = 0.5
    else:
        cpc_score = 1.0
    cs.component_scores["cpc"] = cpc_score
    reasons.append(f"CPC ${profile.cpc_estimate:.2f} → score {cpc_score:.2f}")

    # Search demand score
    if profile.search_demand_monthly >= 50000:
        demand_score = 1.0
    elif profile.search_demand_monthly >= 20000:
        demand_score = 0.8
    elif profile.search_demand_monthly >= 10000:
        demand_score = 0.6
    elif profile.search_demand_monthly >= 5000:
        demand_score = 0.4
    else:
        demand_score = 0.2
    cs.component_scores["demand"] = demand_score
    reasons.append(f"Demand {profile.search_demand_monthly:,}/mo → score {demand_score:.2f}")

    # Price margin score (market price vs our expected selling price)
    if product_price > 0 and profile.avg_market_price > 0:
        price_ratio = profile.avg_market_price / product_price
        price_score = min(1.0, price_ratio)  # If market price >= our price, score 1.0
        reasons.append(f"Market price ratio {price_ratio:.2f} -> score {price_score:.2f}")
    else:
        price_score = 0.5
        reasons.append("No price data")
    cs.component_scores["price"] = price_score

    # Competition score (fewer sellers = better)
    if profile.exact_sku_sellers == 0:
        comp_score = 1.0
        reasons.append("No competitors (blue ocean)")
    elif profile.exact_sku_sellers <= 3:
        comp_score = 0.85
        reasons.append(f"{profile.exact_sku_sellers} sellers (low competition)")
    elif profile.exact_sku_sellers <= 8:
        comp_score = 0.6
        reasons.append(f"{profile.exact_sku_sellers} sellers (moderate)")
    elif profile.exact_sku_sellers <= 15:
        comp_score = 0.3
        reasons.append(f"{profile.exact_sku_sellers} sellers (high)")
    else:
        comp_score = 0.1
        reasons.append(f"{profile.exact_sku_sellers} sellers (saturated)")
    cs.component_scores["competition"] = comp_score

    # Shipping score
    if profile.shipping_days_from_origin <= 7:
        shipping_score = 1.0
    elif profile.shipping_days_from_origin <= 14:
        shipping_score = 0.7
    elif profile.shipping_days_from_origin <= 21:
        shipping_score = 0.4
    else:
        shipping_score = 0.2
    if profile.shipping_cost > 0:
        cost_factor = max(0.5, 1.0 - (profile.shipping_cost / 30.0))
        shipping_score *= cost_factor
    cs.component_scores["shipping"] = shipping_score
    reasons.append(f"Shipping {profile.shipping_days_from_origin}d/${profile.shipping_cost:.0f} → score {shipping_score:.2f}")

    # Tax/compliance score
    tax_score = max(0.2, 1.0 - profile.tax_burden)
    compliance_map = {"LOW": 1.0, "MEDIUM": 0.7, "HIGH": 0.4}
    tax_score *= compliance_map.get(profile.compliance_burden, 0.5)
    cs.component_scores["tax"] = tax_score
    reasons.append(f"Tax {profile.tax_burden:.0%}, compliance {profile.compliance_burden} → score {tax_score:.2f}")

    # Supplier availability score
    cs.component_scores["supplier"] = profile.supplier_availability
    reasons.append(f"Supplier availability {profile.supplier_availability:.2f}")

    # Language advantage score
    cs.component_scores["language"] = profile.language_advantage
    if profile.language_advantage >= 0.8:
        reasons.append("English-speaking market (full advantage)")
    elif profile.language_advantage > 0:
        reasons.append("Partial language advantage")
    else:
        reasons.append("Non-English market (translation needed)")

    # Weighted composite
    weights = {
        "cpc": 0.25,
        "demand": 0.20,
        "price": 0.15,
        "competition": 0.15,
        "shipping": 0.10,
        "tax": 0.05,
        "supplier": 0.05,
        "language": 0.05,
    }
    cs.composite_score = sum(
        cs.component_scores[k] * weights[k] for k in weights
    )
    cs.reasoning = reasons
    return cs


def select_country(
    product_price: float = 0.0,
    product_family: str = "",
    countries: Optional[List[CountryProfile]] = None,
    top_n: int = 3,
) -> List[CountryScore]:
    """
    Score all countries and return ranked list.
    Default candidate countries: US, UK, DE, NO, SE, DK, NL, AU, CA, FR
    """
    if countries is None:
        countries = DEFAULT_COUNTRIES

    scores = []
    for profile in countries:
        cs = score_country(profile, product_price)
        scores.append(cs)

    scores.sort(key=lambda x: x.composite_score, reverse=True)
    for i, s in enumerate(scores):
        s.rank = i + 1

    return scores[:top_n]


def get_best_country(
    product_price: float = 0.0,
    countries: Optional[List[CountryProfile]] = None,
) -> CountryScore:
    """Return the single best country with full reasoning."""
    ranked = select_country(product_price=product_price, countries=countries, top_n=1)
    return ranked[0] if ranked else CountryScore(country="US", composite_score=0.0)
