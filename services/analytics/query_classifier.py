"""
Query Classifier — Categorize search queries by purchase intent.
Tracks per-query metrics: impressions, clicks, cost, orders, revenue, contribution.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import re


class QueryCategory(str, Enum):
    EXACT_MODEL = "EXACT_MODEL"          # "Roomba j7+"
    BRAND_MODEL = "BRAND_MODEL"          # "iRobot Roomba j7+"
    PRODUCT_HIGH_INTENT = "PRODUCT_HIGH_INTENT"  # "robot vacuum for pet hair"
    FEATURE_HIGH_INTENT = "FEATURE_HIGH_INTENT"  # "cordless vacuum with HEPA filter"
    COMPARISON = "COMPARISON"            # "Roomba j7+ vs Neato D8"
    GENERIC_COMMERCIAL = "GENERIC_COMMERCIAL"  # "best vacuum cleaner"
    INFORMATIONAL = "INFORMATIONAL"      # "how do robot vacuums work"
    IRRELEVANT = "IRRELEVANT"           # "vacuum recipe" (wrong intent)


@dataclass
class QueryMetrics:
    """Performance metrics for a specific query."""
    query: str = ""
    category: QueryCategory = QueryCategory.IRRELEVANT
    impressions: int = 0
    clicks: int = 0
    cost: float = 0.0
    orders: int = 0
    revenue: float = 0.0
    contribution: float = 0.0
    ctr: float = 0.0
    cvr: float = 0.0
    cpc: float = 0.0
    cpa: float = 0.0


@dataclass
class ClassificationRule:
    """A rule for classifying queries."""
    category: QueryCategory
    patterns: List[str]  # Regex patterns
    weight: float = 1.0
    examples: List[str] = field(default_factory=list)


# Classification rules — ordered by specificity (most specific first)
CLASSIFICATION_RULES = [
    ClassificationRule(
        QueryCategory.EXACT_MODEL,
        [
            r'^[A-Z][a-z]+\s+[A-Z][a-z]+\s+\d+\b',  # "Roomba j7+" at start
            r'^[A-Z][a-z]+\s+[A-Z]\d+\b',  # "Model X1" at start
            r'\b\w+-\w+\b',  # Hyphenated model numbers
            r'\b(mk|mark|gen|version|v)\s*\d+\b',  # "mk 2", "gen 3"
        ],
        weight=1.0,
        examples=["Roomba j7+", "Dyson V15", "Shark Navigator ZU56"]
    ),
    ClassificationRule(
        QueryCategory.BRAND_MODEL,
        [
            r'\b(iRobot|Dyson|Shark|Bissell|Eureka|Miele|Hoover|Kenmore)\b',
        ],
        weight=0.9,
        examples=["iRobot Roomba", "Dyson Ball", "Shark Vertex"]
    ),
    ClassificationRule(
        QueryCategory.PRODUCT_HIGH_INTENT,
        [
            r'\b(buy|purchase|order|shop|deal|deals|price|pricing|cost|cheap|cheapest|affordable|best price)\b',
            r'\b\w+\s+(for sale|on sale|discount|coupon|free shipping)\b',
        ],
        weight=0.8,
        examples=["buy robot vacuum", "cheap Dyson", "vacuum deals"]
    ),
    ClassificationRule(
        QueryCategory.FEATURE_HIGH_INTENT,
        [
            r'\b(best|top|review|reviews|vs|versus|comparison|compare)\b.*\b(for|with|that|which)\b',
            r'\b\w+\s+(for pet hair|for hardwood|for carpet|with HEPA|cordless|corded|bagless)\b',
        ],
        weight=0.7,
        examples=["best vacuum for pet hair", "cordless vacuum with HEPA"]
    ),
    ClassificationRule(
        QueryCategory.COMPARISON,
        [
            r'\b\w+\s+(vs|versus|or)\s+\w+\b',
            r'\bcompare\s+\w+\b',
        ],
        weight=0.6,
        examples=["Roomba j7+ vs Neato D8", "Dyson or Shark"]
    ),
    ClassificationRule(
        QueryCategory.GENERIC_COMMERCIAL,
        [
            r'\b(best|top|good|great)\s+\w+\b',
            r'\w+\s+(guide|list|ranking|review)\b',
        ],
        weight=0.4,
        examples=["best vacuum cleaner", "top robot vacuums"]
    ),
    ClassificationRule(
        QueryCategory.INFORMATIONAL,
        [
            r'\b(how|what|why|when|where|can|do|does|is|are|should)\b',
            r'\b(wiki|wikipedia|definition|meaning|explain)\b',
        ],
        weight=0.2,
        examples=["how do robot vacuums work", "what is a HEPA filter"]
    ),
]


def classify_query(query: str) -> QueryCategory:
    """Classify a single query into a category."""
    query_lower = query.lower().strip()

    # Check each rule (most specific first)
    for rule in CLASSIFICATION_RULES:
        for pattern in rule.patterns:
            if re.search(pattern, query, re.IGNORECASE):
                return rule.category

    # Default to GENERIC if has commercial words, else INFORMATIONAL
    commercial_words = {'buy', 'price', 'cheap', 'deal', 'shop', 'order', 'sale'}
    if any(w in query_lower for w in commercial_words):
        return QueryCategory.GENERIC_COMMERCIAL

    return QueryCategory.INFORMATIONAL


def classify_queries(queries: List[str]) -> List[QueryMetrics]:
    """Classify a batch of queries."""
    results = []
    for q in queries:
        category = classify_query(q)
        results.append(QueryMetrics(query=q, category=category))
    return results


def should_add_negative(query_metrics: QueryMetrics, threshold: float = 0.40) -> bool:
    """
    Determine if a query should be added as a negative keyword.
    Uses Helena's finding: 40% of generic traffic didn't convert.
    
    Only add negatives when:
    1. Query is GENERIC_COMMERCIAL or INFORMATIONAL
    2. Has enough clicks to be statistically meaningful (>20)
    3. CVR is below threshold
    """
    if query_metrics.category not in [QueryCategory.GENERIC_COMMERCIAL, QueryCategory.INFORMATIONAL]:
        return False

    if query_metrics.clicks < 20:
        return False  # Not enough data

    if query_metrics.cvr < threshold:
        return True  # Not converting

    return False


def summarize_query_portfolio(metrics: List[QueryMetrics]) -> dict:
    """Summarize query portfolio performance."""
    total_impressions = sum(m.impressions for m in metrics)
    total_clicks = sum(m.clicks for m in metrics)
    total_cost = sum(m.cost for m in metrics)
    total_orders = sum(m.orders for m in metrics)
    total_revenue = sum(m.revenue for m in metrics)
    total_contribution = sum(m.contribution for m in metrics)

    by_category = {}
    for m in metrics:
        cat = m.category.value
        if cat not in by_category:
            by_category[cat] = {"clicks": 0, "orders": 0, "cost": 0.0, "contribution": 0.0}
        by_category[cat]["clicks"] += m.clicks
        by_category[cat]["orders"] += m.orders
        by_category[cat]["cost"] += m.cost
        by_category[cat]["contribution"] += m.contribution

    return {
        "total_queries": len(metrics),
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "total_cost": total_cost,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_contribution": total_contribution,
        "overall_cvr": total_orders / total_clicks if total_clicks > 0 else 0,
        "overall_cpc": total_cost / total_clicks if total_clicks > 0 else 0,
        "by_category": by_category,
        "negative_candidates": [
            m.query for m in metrics if should_add_negative(m)
        ],
    }
