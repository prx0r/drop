from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings

class GoogleAdsKeywordAdapter:
    """Raw REST wrapper around KeywordPlanIdeaService.

    Uses an existing OAuth access token. Production should refresh OAuth tokens via your
    credential broker; this class intentionally does not persist refresh tokens.
    """
    def __init__(self, *, version: str | None = None):
        self.version = version or settings.google_ads_api_version

    def _headers(self) -> dict[str, str]:
        required = [settings.google_ads_developer_token, settings.google_ads_access_token]
        if not all(required):
            raise NotConfigured("GOOGLE_ADS_DEVELOPER_TOKEN and GOOGLE_ADS_ACCESS_TOKEN are required")
        h = {
            "Authorization": f"Bearer {settings.google_ads_access_token}",
            "developer-token": settings.google_ads_developer_token,
            "Content-Type": "application/json",
        }
        if settings.google_ads_manager_customer_id:
            h["login-customer-id"] = settings.google_ads_manager_customer_id.replace("-", "")
        return h

    def historical_metrics(self, *, customer_id: str, keywords: list[str], geo_id: str, language_id: str) -> list[dict]:
        customer_id = customer_id.replace("-", "")
        url = f"https://googleads.googleapis.com/{self.version}/customers/{customer_id}:generateKeywordHistoricalMetrics"
        body = {
            "keywords": keywords[:10000],
            "language": f"languageConstants/{language_id}",
            "geoTargetConstants": [f"geoTargetConstants/{geo_id}"],
            "keywordPlanNetwork": "GOOGLE_SEARCH",
            "historicalMetricsOptions": {"includeAverageCpc": True},
        }
        with httpx.Client(timeout=45) as client:
            r = client.post(url, headers=self._headers(), json=body)
        if r.status_code >= 400:
            raise AdapterError(f"Google Ads API {r.status_code}: {r.text[:800]}")
        payload = r.json()
        out = []
        for row in payload.get("results", []):
            m = row.get("keywordMetrics", {})
            out.append({
                "keyword": row.get("text", ""),
                "avg_monthly_searches": int(m.get("avgMonthlySearches", 0) or 0),
                "competition": m.get("competition"),
                "competition_index": float(m.get("competitionIndex", 0) or 0),
                "low_top_page_bid": (float(m.get("lowTopOfPageBidMicros", 0) or 0) / 1_000_000),
                "high_top_page_bid": (float(m.get("highTopOfPageBidMicros", 0) or 0) / 1_000_000),
                "average_cpc": (float(m.get("averageCpcMicros", 0) or 0) / 1_000_000),
                "monthly_search_volumes": m.get("monthlySearchVolumes", []),
            })
        return out

    def generate_ideas(self, *, customer_id: str, seeds: list[str], geo_id: str, language_id: str, page_url: str | None = None) -> list[dict]:
        customer_id = customer_id.replace("-", "")
        url = f"https://googleads.googleapis.com/{self.version}/customers/{customer_id}:generateKeywordIdeas"
        body = {
            "language": f"languageConstants/{language_id}",
            "geoTargetConstants": [f"geoTargetConstants/{geo_id}"],
            "includeAdultKeywords": False,
            "keywordPlanNetwork": "GOOGLE_SEARCH",
        }
        if page_url:
            body["keywordAndUrlSeed"] = {"keywords": seeds[:20], "url": page_url}
        else:
            body["keywordSeed"] = {"keywords": seeds[:20]}
        with httpx.Client(timeout=45) as client:
            r = client.post(url, headers=self._headers(), json=body)
        if r.status_code >= 400:
            raise AdapterError(f"Google Ads API {r.status_code}: {r.text[:800]}")
        return r.json().get("results", [])
