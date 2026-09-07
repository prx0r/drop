from __future__ import annotations
import os
from fastapi import FastAPI, HTTPException
from .pipeline import Radar
from .gift_specs import build_spec
from .models import GiftSpecRequest

ROOT = os.getenv("GIFT_RADAR_ROOT", ".")
radar = Radar(f"{ROOT}/config", f"{ROOT}/data/evidence.yml")
app = FastAPI(title="Gift Arbitrage Engine", version="0.1.0")

@app.get("/health")
def health(): return {"ok": True, "opportunities": len(radar.opportunities), "evidence": len(radar.evidence)}

@app.get("/opportunities")
def opportunities(limit: int = 50):
    return [s.model_dump() for s in radar.rank()[:limit]]

@app.get("/opportunities/{slug}")
def opportunity(slug: str):
    if slug not in radar.opportunities: raise HTTPException(404, "unknown opportunity")
    o = radar.opportunities[slug]
    s = next(x for x in radar.rank([slug]))
    return {"opportunity": o.model_dump(), "score": s.model_dump()}

@app.post("/gift-spec")
def gift_spec(req: GiftSpecRequest):
    if req.opportunity_slug not in radar.opportunities: raise HTTPException(404, "unknown opportunity")
    return build_spec(radar.opportunities[req.opportunity_slug], req).model_dump()
