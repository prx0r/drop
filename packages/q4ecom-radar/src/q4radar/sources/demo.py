from __future__ import annotations

import hashlib
import random
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence, SupplierOffer
from .base import Source


class DemoSource(Source):
    """Deterministic synthetic data for testing the complete pipeline without API keys.

    Every evidence record is marked synthetic so demo output cannot be mistaken for market research.
    """
    name = "demo-synthetic"

    @staticmethod
    def _rng(product: ProductSeed, market: Market) -> random.Random:
        raw = f"{product.slug}:{market.code}:q4-2026".encode()
        seed = int(hashlib.sha256(raw).hexdigest()[:16], 16)
        return random.Random(seed)

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        r = self._rng(product, market)
        winter_boost = (product.winter_affinity / 100) * (market.q4_winter_intensity / 100)
        base_search = r.randint(300, 8500)
        search = base_search * (1 + 1.5 * winter_boost)
        momentum = max(-30, min(140, r.gauss(18 + 45 * winter_boost + product.giftability * 0.15, 22)))
        competition = max(0.05, min(1.0, r.uniform(0.25, 0.9)))
        low = r.uniform(product.target_supplier_usd[0], product.target_supplier_usd[1] * 0.75)
        med = low * r.uniform(1.05, 1.45)
        ship = r.uniform(4, 18) + market.shipping_difficulty / 14
        ship_cost = r.uniform(4, 18) + market.shipping_difficulty / 10
        retail = r.uniform(product.typical_retail_usd[0], product.typical_retail_usd[1])
        comp_count = int(r.uniform(6, 65) * (0.7 + market.ecommerce_maturity / 100))
        supplier_count = r.randint(3, 30)
        ad_count = r.randint(0, 70)
        longevity = r.uniform(4, 130)

        obs.search_volume = round(search)
        obs.search_momentum = round(momentum, 1)
        obs.keyword_competition = round(competition, 3)
        obs.avg_cpc_usd = round(r.uniform(0.35, 2.8) * (0.65 + market.affluent_score / 100), 2)
        obs.competitor_count = comp_count
        obs.competitor_price_median_usd = round(retail, 2)
        obs.supplier_price_low_usd = round(low, 2)
        obs.supplier_price_median_usd = round(med, 2)
        obs.shipping_usd = round(ship_cost, 2)
        obs.shipping_days = round(ship, 1)
        obs.supplier_count = supplier_count
        obs.ad_count = ad_count
        obs.ad_longevity_days = round(longevity, 1)
        obs.supplier_offers.append(SupplierOffer(
            source=self.name, product_id=f"demo-{product.slug}", title=product.name,
            price_usd=round(low, 2), shipping_usd=round(ship_cost, 2), shipping_days=round(ship, 1),
            stock=r.randint(100, 5000), ships_from="synthetic", weight_kg=round(r.uniform(0.2, 3.2), 2),
            metadata={"synthetic": True},
        ))
        for metric, value in {
            "search_volume": obs.search_volume,
            "search_momentum": obs.search_momentum,
            "keyword_competition": obs.keyword_competition,
            "competitor_count": obs.competitor_count,
            "supplier_price_low_usd": obs.supplier_price_low_usd,
        }.items():
            obs.evidence.append(Evidence(source=self.name, metric=metric, value=value, confidence=0.15, metadata={"synthetic": True}))
        return obs
