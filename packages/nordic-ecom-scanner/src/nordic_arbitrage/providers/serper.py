from __future__ import annotations

import os
import re
import requests

from .base import ShoppingResult


_CURRENCY = {"NO": "NOK", "DK": "DKK", "GB": "GBP", "SE": "SEK", "FI": "EUR", "IE": "EUR"}
_GL = {"NO": "no", "DK": "dk", "GB": "gb", "SE": "se", "FI": "fi", "IE": "ie"}


def _price_number(text: str | None) -> float | None:
    if not text:
        return None
    cleaned = re.sub(r"[^0-9,.-]", "", text).replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


class SerperShoppingProvider:
    """Google Shopping via Serper. Keeps scraping concerns outside the core engine."""

    endpoint = "https://google.serper.dev/shopping"

    def __init__(self, api_key: str | None = None, timeout: float = 25.0):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError("SERPER_API_KEY is required")

    def search(self, *, query: str, country: str, language: str) -> list[ShoppingResult]:
        payload = {"q": query, "gl": _GL.get(country, country.lower()), "hl": language.split("-")[0], "num": 20}
        r = requests.post(self.endpoint, headers={"X-API-KEY": self.api_key, "Content-Type": "application/json"}, json=payload, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        out: list[ShoppingResult] = []
        for i, item in enumerate(data.get("shopping", []), start=1):
            out.append(ShoppingResult(
                title=item.get("title", ""),
                price=_price_number(item.get("price")),
                currency=_CURRENCY.get(country),
                merchant=item.get("source"),
                link=item.get("link"),
                image_url=item.get("imageUrl"),
                position=item.get("position", i),
            ))
        return out
