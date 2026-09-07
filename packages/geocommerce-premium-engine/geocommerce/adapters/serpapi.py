from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings
class SerpApiShoppingAdapter:
    URL="https://serpapi.com/search.json"
    def search(self, *, query: str, location: str, gl: str, hl: str) -> dict:
        if not settings.serpapi_key: raise NotConfigured("SERPAPI_KEY required")
        params={"engine":"google_shopping","q":query,"location":location,"gl":gl.lower(),"hl":hl,"api_key":settings.serpapi_key}
        with httpx.Client(timeout=45) as client: r=client.get(self.URL,params=params)
        if r.status_code>=400: raise AdapterError(f"SerpApi {r.status_code}: {r.text[:800]}")
        return r.json()
