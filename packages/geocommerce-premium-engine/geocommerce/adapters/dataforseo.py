from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings

class DataForSEOAdapter:
    URL = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    def search_volume(self, *, keywords: list[str], location_code: int, language_code: str) -> list[dict]:
        if not settings.dataforseo_login or not settings.dataforseo_password:
            raise NotConfigured("DATAFORSEO_LOGIN/PASSWORD required")
        body = [{"keywords": keywords[:1000], "location_code": location_code, "language_code": language_code, "search_partners": False}]
        with httpx.Client(timeout=45, auth=(settings.dataforseo_login, settings.dataforseo_password)) as client:
            r = client.post(self.URL, json=body)
        if r.status_code >= 400: raise AdapterError(f"DataForSEO {r.status_code}: {r.text[:800]}")
        tasks = r.json().get("tasks", [])
        if not tasks or tasks[0].get("status_code") != 20000:
            raise AdapterError(f"DataForSEO task error: {r.text[:800]}")
        return tasks[0].get("result", []) or []
