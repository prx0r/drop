from __future__ import annotations

import os
import re
from statistics import median
import httpx
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence, SupplierOffer
from .base import Source


_PRICE_RE = re.compile(r"\d+(?:\.\d+)?")


def _price(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        xs = [float(x) for x in _PRICE_RE.findall(v)]
        if xs:
            return min(xs)
    return None


class CJSource(Source):
    name = "cjdropshipping-v2"
    endpoint = "https://developers.cjdropshipping.com/api2.0/v1/product/listV2"

    @property
    def enabled(self) -> bool:
        return bool(os.getenv("CJ_ACCESS_TOKEN"))

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled:
            return obs
        headers = {"CJ-Access-Token": os.environ["CJ_ACCESS_TOKEN"]}
        params = {"page": 1, "size": 50, "keyWord": product.keywords[0]}
        r = httpx.get(self.endpoint, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        payload = r.json()
        data = payload.get("data") or {}
        items = data.get("content") or data.get("list") or []
        prices = []
        for item in items:
            p = _price(item.get("sellPrice") or item.get("price") or item.get("nowPrice"))
            if p is not None:
                prices.append(p)
            pid = str(item.get("pid") or item.get("id") or item.get("productId") or "")
            if pid:
                obs.supplier_offers.append(SupplierOffer(
                    source=self.name,
                    product_id=pid,
                    title=str(item.get("productNameEn") or item.get("nameEn") or item.get("productName") or product.name),
                    price_usd=p,
                    url=item.get("productUrl") or item.get("url"),
                    metadata={"raw_category": item.get("categoryName")},
                ))
        if prices:
            obs.supplier_price_low_usd = min(prices)
            obs.supplier_price_median_usd = median(prices)
            obs.supplier_count = len(prices)
        obs.evidence.append(Evidence(source=self.name, metric="supplier_results", value=len(items), confidence=0.82, url="https://developers.cjdropshipping.com/en/api/api2/api/product.html"))
        return obs
