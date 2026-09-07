from __future__ import annotations

from collections import Counter
from dataclasses import asdict
from statistics import median
from typing import Iterable

from .providers.base import ShoppingResult


def _tokens(text: str) -> set[str]:
    return {t.strip('.,:;!?()[]{}\"\'').lower() for t in text.split() if len(t.strip('.,:;!?()[]{}\"\'')) >= 3}


def summarize_shopping(results: Iterable[ShoppingResult], query: str = "") -> dict:
    rows = list(results)
    priced = [r.price for r in rows if r.price is not None and r.price > 0]
    merchants = [r.merchant.strip() for r in rows if r.merchant and r.merchant.strip()]
    merchant_counts = Counter(merchants)
    dominant_share = (max(merchant_counts.values()) / len(merchants)) if merchants else 0.0

    query_tokens = _tokens(query)
    if rows and query_tokens:
        coverage = []
        for row in rows:
            tt = _tokens(row.title)
            coverage.append(len(query_tokens & tt) / len(query_tokens))
        mean_query_coverage = sum(coverage) / len(coverage)
    else:
        mean_query_coverage = 0.0

    image_urls = [r.image_url for r in rows if r.image_url]
    unique_image_ratio = len(set(image_urls)) / len(image_urls) if image_urls else 0.0

    out = {
        "result_count": len(rows),
        "merchant_count": len(set(merchants)),
        "dominant_merchant_share": round(dominant_share, 4),
        "median_price": round(median(priced), 2) if priced else None,
        "min_price": round(min(priced), 2) if priced else None,
        "max_price": round(max(priced), 2) if priced else None,
        "price_spread_ratio": round((max(priced) - min(priced)) / median(priced), 4) if len(priced) >= 2 and median(priced) else None,
        "missing_image_share": round(1 - (len(image_urls) / len(rows)), 4) if rows else 0.0,
        "unique_image_ratio": round(unique_image_ratio, 4),
        # A title-relevance proxy only. It is not a human/LLM creative-quality judgment.
        "mean_query_token_coverage": round(mean_query_coverage, 4),
        "title_gap_proxy": round(1.0 - mean_query_coverage, 4) if query_tokens else None,
        "top_merchants": merchant_counts.most_common(10),
        "results": [asdict(r) for r in rows],
    }
    return out
