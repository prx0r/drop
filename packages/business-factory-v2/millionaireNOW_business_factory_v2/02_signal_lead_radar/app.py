from __future__ import annotations
import os, sys, uuid
from datetime import datetime, timezone, date
from pathlib import Path
from pydantic import BaseModel, Field, HttpUrl
from fastapi import Depends, HTTPException, Query
import httpx, yaml

ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from shared.app import make_app
from shared.db import DB
from shared.security import require_admin
from shared.provenance import record_observation
from shared.text import tokens, clamp

APP="signal_radar"; DB_PATH=os.getenv("DB_PATH",str(Path(__file__).with_name("app.db"))); db=DB(DB_PATH)
with db.connect() as con:
    con.executescript("""CREATE TABLE IF NOT EXISTS signals(id TEXT PRIMARY KEY, source TEXT NOT NULL, source_url TEXT, title TEXT NOT NULL, description TEXT NOT NULL, location TEXT, published_at TEXT, raw_json TEXT NOT NULL); CREATE TABLE IF NOT EXISTS actions(id INTEGER PRIMARY KEY AUTOINCREMENT, signal_id TEXT NOT NULL, vertical TEXT NOT NULL, status TEXT NOT NULL, note TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
app=make_app("Public Signal Lead Radar")
CONFIG=yaml.safe_load(Path(__file__).with_name("config.yaml").read_text())

class SignalIn(BaseModel):
    id: str | None=None; source: str; source_url: str | None=None; title: str; description: str=""; location: str | None=None; published_at: datetime | None=None
class ActionIn(BaseModel):
    signal_id: str; vertical: str; status: str; note: str | None=None


def score(sig: dict, vertical: str) -> dict:
    v=CONFIG["verticals"].get(vertical)
    if not v: raise HTTPException(404,"unknown vertical")
    text=(sig.get("title","")+" "+sig.get("description","")).lower(); tt=tokens(text)
    pos=sum(float(w) for k,w in v["keywords"].items() if set(tokens(k)) & tt)
    neg=sum(float(w) for k,w in v.get("negative_keywords",{}).items() if set(tokens(k)) & tt)
    loc=0.5
    wanted=[x.lower() for x in v.get("locations",[])]
    if wanted and sig.get("location"): loc=1.0 if any(x in sig["location"].lower() for x in wanted) else 0.15
    recency=0.5
    if sig.get("published_at"):
        try:
            d=datetime.fromisoformat(str(sig["published_at"]).replace("Z","+00:00")); age=max(0,(datetime.now(timezone.utc)-d.astimezone(timezone.utc)).days); recency=max(0,1-age/30)
        except Exception: pass
    raw=clamp((pos-neg)/max(float(v.get("keyword_scale",5)),1))*0.55+loc*0.2+recency*0.25
    return {**sig,"vertical":vertical,"score":round(raw*100),"matched_keywords":[k for k in v["keywords"] if set(tokens(k)) & tt]}

@app.post("/api/admin/signals",dependencies=[Depends(require_admin)])
def ingest(items:list[SignalIn]):
    import json
    count=0
    for s in items:
        sid=s.id or str(uuid.uuid4()); raw=s.model_dump(mode="json")
        db.execute("INSERT OR REPLACE INTO signals(id,source,source_url,title,description,location,published_at,raw_json) VALUES(?,?,?,?,?,?,?,?)",(sid,s.source,s.source_url,s.title,s.description,s.location,s.published_at.isoformat() if s.published_at else None,json.dumps(raw)))
        record_observation(db,APP,"signal",sid,raw,s.source_url,s.published_at.isoformat() if s.published_at else None); count+=1
    return {"ingested":count}

@app.post("/api/admin/fetch/planning",dependencies=[Depends(require_admin)])
def fetch_planning(since: date, limit:int=Query(default=100,ge=1,le=500)):
    # Official Planning Data API is public and beta. Parser is intentionally tolerant of schema wrappers.
    url="https://www.planning.data.gov.uk/entity.json"
    params={"dataset":"planning-application","start_date_year":since.year,"start_date_month":since.month,"start_date_day":since.day,"start_date_match":"since","limit":limit}
    with httpx.Client(timeout=20,follow_redirects=True) as client:
        r=client.get(url,params=params); r.raise_for_status(); payload=r.json()
    entities=payload.get("entities") or payload.get("entity") or []
    if isinstance(entities,dict): entities=[entities]
    mapped=[]
    for e in entities:
        sid=str(e.get("entity") or e.get("reference") or uuid.uuid4())
        mapped.append(SignalIn(id=sid,source="planning.data.gov.uk",source_url=str(r.url),title=str(e.get("name") or e.get("reference") or "Planning application"),description=str(e.get("description") or e.get("notes") or ""),location=str(e.get("address") or e.get("organisation-entity") or ""),published_at=None))
    return ingest(mapped)

@app.get("/api/signals/{vertical}")
def list_signals(vertical:str, min_score:int=35, limit:int=100):
    rows=db.query("SELECT id,source,source_url,title,description,location,published_at FROM signals ORDER BY COALESCE(published_at,'') DESC LIMIT ?",(min(max(limit,1),500),))
    ranked=[score(r,vertical) for r in rows]; ranked=[r for r in ranked if r["score"]>=min_score]; ranked.sort(key=lambda x:x["score"],reverse=True); return ranked

@app.post("/api/actions")
def action(a:ActionIn):
    if a.status not in {"new","reviewed","contacted","won","lost","ignored"}: raise HTTPException(400,"invalid status")
    db.execute("INSERT INTO actions(signal_id,vertical,status,note) VALUES(?,?,?,?)",(a.signal_id,a.vertical,a.status,a.note)); db.event(APP,"signal_action",a.signal_id,a.model_dump()); return {"ok":True}
