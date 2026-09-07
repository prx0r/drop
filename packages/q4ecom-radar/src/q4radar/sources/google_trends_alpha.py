from __future__ import annotations

import os
import httpx
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence
from .base import Source


class GoogleTrendsAlphaSource(Source):
    """Adapter for the official Google Trends API alpha.

    Google publishes the existence/capabilities of the alpha, but endpoint/auth details are
    provided to accepted testers. To avoid hard-coding an undocumented contract, this adapter
    is driven by GOOGLE_TRENDS_API_URL. It expects a normalized proxy/endpoint returning:
      {"interest": [number,...]} OR {"momentum_pct": number}
    This keeps the engine ready for official access without brittle scraping.
    """
    name = "google-trends-alpha"

    @property
    def enabled(self) -> bool:
        return bool(os.getenv("GOOGLE_TRENDS_API_URL"))

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled:
            return obs
        headers = {}
        if os.getenv("GOOGLE_TRENDS_ACCESS_TOKEN"):
            headers["Authorization"] = f"Bearer {os.environ['GOOGLE_TRENDS_ACCESS_TOKEN']}"
        payload = {"terms": product.keywords[:8], "geo": market.code, "window": "P12M", "interval": "WEEK"}
        r = httpx.post(os.environ["GOOGLE_TRENDS_API_URL"], json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        momentum = data.get("momentum_pct")
        if momentum is None:
            values = [float(x) for x in data.get("interest", []) if isinstance(x, (int, float))]
            if len(values) >= 8:
                n = max(2, len(values)//4)
                a = sum(values[-n:]) / n
                b = sum(values[:n]) / n or 1
                momentum = ((a/b)-1)*100
        if momentum is not None:
            obs.search_momentum = float(momentum)
            obs.evidence.append(Evidence(source=self.name, metric="search_momentum", value=round(float(momentum),2), unit="%", confidence=0.95, url="https://developers.google.com/search/apis/trends"))
        return obs
