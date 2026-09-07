from __future__ import annotations

import os
from statistics import median
import httpx
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence
from .base import Source


class SerpApiShoppingSource(Source):
    name = "serpapi-google-shopping"
    endpoint = "https://serpapi.com/search.json"

    @property
    def enabled(self) -> bool:
        return bool(os.getenv("SERPAPI_KEY"))

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled:
            return obs
        params = {
            "engine": "google_shopping",
            "q": product.keywords[0],
            "api_key": os.environ["SERPAPI_KEY"],
            "gl": market.code.lower(),
            "hl": market.language,
            "num": 40,
        }
        data = httpx.get(self.endpoint, params=params, timeout=30).json()
        items = data.get("shopping_results", [])
        prices = []
        for item in items:
            val = item.get("extracted_price")
            if isinstance(val, (int, float)):
                prices.append(float(val))
        obs.competitor_count = len(items)
        if prices:
            obs.competitor_price_median_usd = median(prices)
        obs.evidence.append(Evidence(
            source=self.name, metric="shopping_results", value=len(items), confidence=0.75,
            url="https://serpapi.com/google-shopping-api",
            metadata={"query": product.keywords[0], "market": market.code},
        ))
        return obs


class SerpApiTrendsSource(Source):
    name = "serpapi-google-trends"
    endpoint = "https://serpapi.com/search.json"

    @property
    def enabled(self) -> bool:
        return bool(os.getenv("SERPAPI_KEY"))

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled:
            return obs
        params = {
            "engine": "google_trends",
            "q": product.keywords[0],
            "api_key": os.environ["SERPAPI_KEY"],
            "geo": market.code,
            "data_type": "TIMESERIES",
            "date": "today 12-m",
        }
        data = httpx.get(self.endpoint, params=params, timeout=30).json()
        timeline = data.get("interest_over_time", {}).get("timeline_data", [])
        vals = []
        for row in timeline:
            values = row.get("values") or []
            if values:
                v = values[0].get("extracted_value")
                if isinstance(v, (int, float)):
                    vals.append(float(v))
        if len(vals) >= 4:
            recent_n = max(2, len(vals)//4)
            recent = sum(vals[-recent_n:]) / recent_n
            prior = sum(vals[:recent_n]) / recent_n or 1
            obs.search_momentum = ((recent / prior) - 1) * 100
            obs.evidence.append(Evidence(source=self.name, metric="search_momentum", value=round(obs.search_momentum, 2), unit="%", confidence=0.75, metadata={"points": len(vals)}))
        return obs
