from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .config import COUNTRIES
from .db import save_observation
from .providers.base import KeywordProvider, ShoppingProvider
from .serp_analysis import summarize_shopping


def observe_query(
    *,
    query: str,
    country: str,
    shopping: ShoppingProvider,
    keywords: KeywordProvider | None = None,
    db_path: str | None = None,
    persist: bool = True,
) -> dict[str, Any]:
    country = country.upper()
    profile = COUNTRIES[country]
    shop_results = shopping.search(query=query, country=country, language=profile.language)
    serp = summarize_shopping(shop_results, query)

    kw_payload = None
    if keywords is not None:
        metrics = keywords.metrics(keywords=[query], country=country, language=profile.language)
        kw_payload = asdict(metrics[0]) if metrics else None

    payload = {
        "query": query,
        "country": country,
        "currency": profile.currency,
        "locale": profile.language,
        "serp": serp,
        "keyword": kw_payload,
    }
    if persist:
        save_observation("live_query", country, query, payload, db_path)
    return payload
