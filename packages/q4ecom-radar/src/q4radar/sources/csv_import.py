from __future__ import annotations

import csv
from pathlib import Path
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence
from .base import Source


class CSVObservationSource(Source):
    """Imports human/exported research without scraping restricted sites.

    CSV columns: product_slug,market,search_volume,search_momentum,keyword_competition,
    avg_cpc_usd,competitor_count,competitor_price_median_usd,supplier_price_low_usd,
    supplier_price_median_usd,shipping_usd,shipping_days,supplier_count,ad_count,ad_longevity_days,source,url
    """
    name = "csv-import"

    def __init__(self, path: str):
        self.rows = {}
        p = Path(path)
        if not p.exists():
            return
        with p.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                self.rows[(row.get("product_slug"), row.get("market"))] = row

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        row = self.rows.get((product.slug, market.code))
        if not row:
            return obs
        numeric = [
            "search_volume","search_momentum","keyword_competition","avg_cpc_usd","competitor_count",
            "competitor_price_median_usd","supplier_price_low_usd","supplier_price_median_usd",
            "shipping_usd","shipping_days","supplier_count","ad_count","ad_longevity_days",
        ]
        for field in numeric:
            v = row.get(field)
            if v not in (None, ""):
                setattr(obs, field, float(v) if field not in {"competitor_count","supplier_count","ad_count"} else int(float(v)))
        obs.evidence.append(Evidence(source=row.get("source") or self.name, metric="csv_observation", value=True, confidence=0.8, url=row.get("url") or None))
        return obs
