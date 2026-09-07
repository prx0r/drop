from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from statistics import median
from typing import Callable

from ..models import MarketSignal
from .markets import get_market
from .signals import save_signal


def aggregate_keyword_metrics(rows: list[dict]) -> dict[str, float | int]:
    """Conservative aggregate for a query cluster.

    Similar keyword ideas overlap heavily. We therefore use MAX search volume rather
    than SUM to avoid pretending synonyms are independent demand. CPC/competition are
    search-volume-weighted across returned rows.
    """
    usable = [r for r in rows if int(r.get("avg_monthly_searches", 0) or 0) >= 0]
    if not usable:
        return {"avg_monthly_searches": 0, "competition_index": 0.0, "cpc_low": 0.0, "cpc_high": 0.0, "avg_cpc": 0.0}
    max_searches = max(int(r.get("avg_monthly_searches", 0) or 0) for r in usable)
    weights = [max(1, int(r.get("avg_monthly_searches", 0) or 0)) for r in usable]
    total = sum(weights)

    def weighted(key: str) -> float:
        return sum(float(r.get(key, 0) or 0) * w for r, w in zip(usable, weights)) / total

    return {
        "avg_monthly_searches": max_searches,
        "competition_index": weighted("competition_index"),
        "cpc_low": weighted("low_top_page_bid"),
        "cpc_high": weighted("high_top_page_bid"),
        "avg_cpc": weighted("average_cpc") or weighted("low_top_page_bid"),
    }


def shopping_snapshot(payload: dict) -> dict:
    """Extract a robust local price benchmark from a Google Shopping snapshot."""
    rows = payload.get("shopping_results", []) or []
    prices: list[float] = []
    domains: set[str] = set()
    for row in rows:
        value = row.get("extracted_price")
        try:
            if value is not None and float(value) > 0:
                prices.append(float(value))
        except (TypeError, ValueError):
            pass
        source = row.get("source") or row.get("merchant_name")
        if source:
            domains.add(str(source).strip().lower())
    return {
        "benchmark_price_gross": median(prices) if prices else None,
        "shopping_seller_count": len(domains) or len(rows),
        "observed_prices": prices,
    }


@dataclass
class LiveMarketScanner:
    google_ads: object
    fx_convert: Callable[[float, str, str], float]
    shopping: object | None = None

    def scan(
        self,
        *,
        product_slug: str,
        market_code: str,
        query: str,
        customer_id: str,
        ads_currency: str,
        benchmark_price_gross: float | None = None,
        shopping_location: str | None = None,
        source_url: str | None = None,
    ) -> MarketSignal:
        market = get_market(market_code)
        rows = self.google_ads.historical_metrics(
            customer_id=customer_id,
            keywords=[query],
            geo_id=market.google_geo_id,
            language_id=market.google_language_id,
        )
        agg = aggregate_keyword_metrics(rows)
        for key in ("cpc_low", "cpc_high", "avg_cpc"):
            agg[key] = self.fx_convert(float(agg[key]), ads_currency, market.currency)

        seller_count = None
        if benchmark_price_gross is None and self.shopping is not None:
            if not shopping_location:
                raise ValueError("shopping_location required when deriving benchmark from Shopping")
            payload = self.shopping.search(
                query=query,
                location=shopping_location,
                gl=market.code.lower(),
                hl=market.language_code.lower(),
            )
            snap = shopping_snapshot(payload)
            benchmark_price_gross = snap["benchmark_price_gross"]
            seller_count = snap["shopping_seller_count"]
        if benchmark_price_gross is None:
            raise ValueError("benchmark_price_gross required when Shopping snapshot is unavailable")

        observed = datetime.now(timezone.utc).isoformat()
        signal = MarketSignal(
            product_slug=product_slug,
            market_code=market.code,
            query=query,
            currency=market.currency,
            avg_monthly_searches=int(agg["avg_monthly_searches"]),
            competition_index=float(agg["competition_index"]),
            cpc_low=round(float(agg["cpc_low"]), 4),
            cpc_high=round(float(agg["cpc_high"]), 4),
            avg_cpc=round(float(agg["avg_cpc"]), 4),
            benchmark_price_gross=float(benchmark_price_gross),
            shopping_seller_count=seller_count,
            source="google_ads+shopping" if self.shopping else "google_ads",
            source_url=source_url,
            observed_at=observed,
        )
        save_signal(signal)
        return signal
