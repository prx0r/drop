from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Iterable
from .config import load_markets, load_products, load_scoring
from .models import ProductObservation, ScanResult
from .scoring import score
from .database import Database


class Scanner:
    def __init__(self, config_dir: str, db_path: str, sources: Iterable):
        self.config_dir = config_dir
        self.markets = load_markets(config_dir)
        self.products = load_products(config_dir)
        self.scoring = load_scoring(config_dir)
        self.db = Database(db_path)
        self.sources = list(sources)

    def run(self, market_codes: list[str], product_slugs: list[str] | None = None) -> ScanResult:
        bad = [m for m in market_codes if m not in self.markets]
        if bad:
            raise ValueError(f"Unknown markets: {bad}. Available: {sorted(self.markets)}")
        products = self.products.values() if not product_slugs else [self.products[x] for x in product_slugs]
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
        source_names = [s.name for s in self.sources]
        self.db.start_run(run_id, market_codes, source_names)
        scores = []
        try:
            for market_code in market_codes:
                market = self.markets[market_code]
                for product in products:
                    obs = ProductObservation(product_slug=product.slug, market=market_code)
                    for source in self.sources:
                        try:
                            obs = source.enrich(product, market, obs)
                        except Exception as e:
                            from .models import Evidence
                            obs.evidence.append(Evidence(source=source.name, metric="source_error", value=str(e), confidence=1.0))
                    self.db.save_observation(run_id, obs)
                    s = score(product, market, obs, self.scoring)
                    self.db.save_score(run_id, s)
                    scores.append(s)
            self.db.finish_run(run_id, "complete")
        except Exception:
            self.db.finish_run(run_id, "failed")
            raise
        return ScanResult(
            run_id=run_id,
            generated_at=datetime.now(timezone.utc),
            markets=market_codes,
            sources=source_names,
            scores=sorted(scores, key=lambda x: x.total_score, reverse=True),
        )
