from __future__ import annotations

import base64
import os
import requests

from .base import KeywordMetric


LOCATION_CODES = {
    "NO": 2578,
    "DK": 2208,
    "GB": 2826,
    "SE": 2752,
    "FI": 2246,
    "IE": 2372,
    "CH": 2756,
    "AU": 2036,
    "NZ": 2554,
    "AE": 2784,
    "SA": 2682,
}
LANGUAGE_CODES = {
    "NO": "no", "DK": "da", "GB": "en", "SE": "sv", "FI": "fi", "IE": "en",
    "CH": "de", "AU": "en", "NZ": "en", "AE": "ar", "SA": "ar",
}


class DataForSEOKeywordProvider:
    """Keyword metrics adapter. Verify account endpoint/plan before production use."""

    endpoint = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

    def __init__(self, login: str | None = None, password: str | None = None, timeout: float = 30.0):
        self.login = login or os.getenv("DATAFORSEO_LOGIN")
        self.password = password or os.getenv("DATAFORSEO_PASSWORD")
        self.timeout = timeout
        if not self.login or not self.password:
            raise RuntimeError("DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD are required")

    @staticmethod
    def _unsupported_country(country: str):
        raise ValueError(f"No DataForSEO location code configured for {country}; add it in providers/dataforseo.py")

    def metrics(self, *, keywords: list[str], country: str, language: str) -> list[KeywordMetric]:
        auth = base64.b64encode(f"{self.login}:{self.password}".encode()).decode()
        payload = [{
            "keywords": keywords,
            "location_code": LOCATION_CODES.get(country) or self._unsupported_country(country),
            "language_code": LANGUAGE_CODES.get(country, language.split("-")[0]),
            "include_adult_keywords": False,
        }]
        r = requests.post(self.endpoint, headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"}, json=payload, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        rows = (((data.get("tasks") or [{}])[0].get("result")) or [])
        return [KeywordMetric(
            keyword=row.get("keyword", ""),
            monthly_searches=float(row.get("search_volume") or 0),
            cpc=float(row.get("cpc") or 0),
            competition=float(row.get("competition") or 0) if row.get("competition") is not None else None,
        ) for row in rows]
