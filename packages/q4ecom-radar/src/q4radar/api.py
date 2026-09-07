from __future__ import annotations

import os
from fastapi import FastAPI, Query
from pydantic import BaseModel
from .database import Database
from .pipeline import Scanner
from .sources import DemoSource, GoogleAdsKeywordSource, GoogleTrendsAlphaSource, SerpApiShoppingSource, SerpApiTrendsSource, CJSource, MetaAdLibrarySource

app = FastAPI(title="Q4 Ecom Radar", version="0.1.0")


def _db():
    return Database(os.getenv("Q4RADAR_DB", "data/q4radar.sqlite3"))


def _live_sources():
    src = [GoogleAdsKeywordSource(), GoogleTrendsAlphaSource(), SerpApiTrendsSource(), SerpApiShoppingSource(), CJSource(), MetaAdLibrarySource()]
    return [x for x in src if getattr(x, "enabled", True)]


class ScanRequest(BaseModel):
    markets: list[str] = ["GB","NO","DK"]
    products: list[str] | None = None
    demo: bool = False


@app.get("/health")
def health():
    return {"ok": True, "service": "q4ecom-radar"}


@app.get("/opportunities")
def opportunities(market: str | None = None, limit: int = Query(50, ge=1, le=500)):
    return _db().latest_scores(market=market, limit=limit)


@app.get("/runs")
def runs(limit: int = Query(20, ge=1, le=100)):
    return _db().list_runs(limit)


@app.post("/scan")
def scan(req: ScanRequest):
    sources = [DemoSource()] if req.demo else _live_sources()
    if not sources:
        return {"error":"No live sources configured. Add API credentials or call with demo=true."}
    scanner = Scanner(os.getenv("Q4RADAR_CONFIG_DIR","config"), os.getenv("Q4RADAR_DB","data/q4radar.sqlite3"), sources)
    return scanner.run(req.markets, req.products)
