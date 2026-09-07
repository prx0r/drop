"""Optional Prodigi quote adapter. Does not place orders."""
from __future__ import annotations
import os, httpx

class ProdigiQuoteClient:
    def __init__(self, api_key: str | None = None, sandbox: bool = True):
        self.api_key = api_key or os.getenv("PRODIGI_API_KEY")
        self.base = "https://api.sandbox.prodigi.com/v4.0" if sandbox else "https://api.prodigi.com/v4.0"
    def quote(self, destination: str, currency: str, sku: str, copies: int = 1, page_count: int | None = None):
        if not self.api_key: raise RuntimeError("Set PRODIGI_API_KEY")
        asset = {"printArea":"default"}
        if page_count is not None: asset["pageCount"] = page_count
        payload = {"destinationCountryCode":destination,"currencyCode":currency,"items":[{"sku":sku,"copies":copies,"attributes":{},"assets":[asset]}]}
        r = httpx.post(f"{self.base}/quotes", headers={"X-API-Key":self.api_key}, json=payload, timeout=30)
        r.raise_for_status(); return r.json()
