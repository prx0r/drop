from __future__ import annotations

import os
from datetime import datetime, timezone
import httpx
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence
from .base import Source


class MetaAdLibrarySource(Source):
    """Optional Meta Ad Library adapter.

    Availability and permitted fields differ by ad category, geography, API version and account
    permissions. Failures are intentionally non-fatal; use CSV imports when your account cannot
    query general commercial ads programmatically.
    """
    name = "meta-ad-library"

    @property
    def enabled(self) -> bool:
        return bool(os.getenv("META_ACCESS_TOKEN"))

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled:
            return obs
        version = os.getenv("META_GRAPH_VERSION", "v25.0")
        url = f"https://graph.facebook.com/{version}/ads_archive"
        params = {
            "access_token": os.environ["META_ACCESS_TOKEN"],
            "search_terms": product.keywords[0],
            "ad_reached_countries": f'["{market.code}"]',
            "ad_active_status": "ACTIVE",
            "fields": "id,ad_creation_time,ad_delivery_start_time,page_name",
            "limit": 100,
        }
        try:
            r = httpx.get(url, params=params, timeout=30)
            if r.status_code >= 400:
                obs.evidence.append(Evidence(source=self.name, metric="api_unavailable", value=r.status_code, confidence=0.9, metadata={"message": r.text[:300]}))
                return obs
            items = r.json().get("data", [])
        except Exception as e:
            obs.evidence.append(Evidence(source=self.name, metric="api_error", value=str(e), confidence=0.9))
            return obs
        obs.ad_count = len(items)
        days = []
        now = datetime.now(timezone.utc)
        for x in items:
            raw = x.get("ad_delivery_start_time") or x.get("ad_creation_time")
            if raw:
                try:
                    dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
                    days.append((now-dt).total_seconds()/86400)
                except Exception:
                    pass
        if days:
            obs.ad_longevity_days = sum(days)/len(days)
        obs.evidence.append(Evidence(source=self.name, metric="active_ads", value=len(items), confidence=0.65, url="https://www.facebook.com/ads/library/"))
        return obs
