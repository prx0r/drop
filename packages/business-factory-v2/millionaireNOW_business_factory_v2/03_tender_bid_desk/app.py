from __future__ import annotations
import os, sys, uuid, json
from datetime import datetime, timezone
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi import Depends, HTTPException
import httpx, yaml

ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from shared.app import make_app
from shared.db import DB
from shared.security import require_admin
from shared.provenance import record_observation
from shared.text import tokens, clamp

APP="tender_desk"; db=DB(os.getenv("DB_PATH",str(Path(__file__).with_name("app.db"))))
with db.connect() as con:
    con.executescript("""CREATE TABLE IF NOT EXISTS tenders(id TEXT PRIMARY KEY, source TEXT NOT NULL, source_url TEXT, title TEXT NOT NULL, description TEXT NOT NULL, buyer TEXT, value REAL, currency TEXT, deadline TEXT, region TEXT, cpv TEXT, raw_json TEXT NOT NULL); CREATE TABLE IF NOT EXISTS profiles(id TEXT PRIMARY KEY, name TEXT NOT NULL, payload_json TEXT NOT NULL); CREATE TABLE IF NOT EXISTS decisions(id INTEGER PRIMARY KEY AUTOINCREMENT, tender_id TEXT NOT NULL, profile_id TEXT NOT NULL, decision TEXT NOT NULL, score REAL NOT NULL, rationale_json TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
app=make_app("Tender Qualifier + Bid Desk")

class TenderIn(BaseModel):
    id:str|None=None; source:str="manual"; source_url:str|None=None; title:str; description:str=""; buyer:str|None=None; value:float|None=Field(default=None,ge=0); currency:str="GBP"; deadline:datetime|None=None; region:str|None=None; cpv:str|None=None
class ProfileIn(BaseModel):
    id:str|None=None; name:str; capabilities:list[str]=Field(min_length=1); regions:list[str]=[]; min_value:float|None=Field(default=None,ge=0); max_value:float|None=Field(default=None,ge=0); cpv_prefixes:list[str]=[]; must_have_terms:list[str]=[]; exclusion_terms:list[str]=[]


def qualify(t:dict,p:ProfileIn)->dict:
    text=f"{t.get('title','')} {t.get('description','')} {t.get('cpv','')}".lower(); tt=tokens(text)
    reasons=[]; hard_fail=[]
    val=t.get("value")
    if val is not None and p.min_value is not None and val<p.min_value: hard_fail.append("below minimum contract value")
    if val is not None and p.max_value is not None and val>p.max_value: hard_fail.append("above maximum contract value")
    if p.regions and t.get("region") and not any(r.lower() in str(t.get("region")).lower() for r in p.regions): hard_fail.append("outside configured regions")
    if p.cpv_prefixes and t.get("cpv") and not any(str(t.get("cpv")).startswith(x) for x in p.cpv_prefixes): hard_fail.append("CPV outside configured prefixes")
    for term in p.must_have_terms:
        if not (tokens(term)&tt): hard_fail.append(f"missing required term: {term}")
    for term in p.exclusion_terms:
        if tokens(term)&tt: hard_fail.append(f"excluded term present: {term}")
    cap_hits=[c for c in p.capabilities if tokens(c)&tt]; capability=len(cap_hits)/max(len(p.capabilities),1)
    deadline_score=.5; days=None
    if t.get("deadline"):
        try:
            d=datetime.fromisoformat(str(t["deadline"]).replace("Z","+00:00")); days=(d.astimezone(timezone.utc)-datetime.now(timezone.utc)).days; deadline_score=1.0 if days>=21 else .7 if days>=10 else .35 if days>=3 else 0
        except Exception: pass
    score=0 if hard_fail else round(100*clamp(capability*.65+deadline_score*.2+(.15 if val else .07)))
    decision="NO_BID" if hard_fail or score<40 else "REVIEW" if score<70 else "BID"
    reasons.extend([f"capability hits: {', '.join(cap_hits) or 'none'}",f"deadline days: {days if days is not None else 'unknown'}"])
    return {"tender_id":t["id"],"decision":decision,"score":score,"hard_failures":hard_fail,"evidence":reasons,"checklist":["Verify mandatory selection criteria in original notice/documents","Confirm insurance/accreditations and evidence","Confirm delivery capacity and pricing","Check clarification deadline and submission mechanism"],"warning":"This is triage from structured notice fields, not a legal or procurement compliance determination."}

@app.post("/api/admin/tenders",dependencies=[Depends(require_admin)])
def ingest(items:list[TenderIn]):
    count=0
    for x in items:
        tid=x.id or str(uuid.uuid4()); raw=x.model_dump(mode="json")
        db.execute("INSERT OR REPLACE INTO tenders(id,source,source_url,title,description,buyer,value,currency,deadline,region,cpv,raw_json) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(tid,x.source,x.source_url,x.title,x.description,x.buyer,x.value,x.currency,x.deadline.isoformat() if x.deadline else None,x.region,x.cpv,json.dumps(raw)))
        record_observation(db,APP,"tender",tid,raw,x.source_url,x.deadline.isoformat() if x.deadline else None); count+=1
    return {"ingested":count}

@app.post("/api/admin/fetch/contracts-finder",dependencies=[Depends(require_admin)])
def fetch_contracts_finder(published_from:str,published_to:str,limit:int=100):
    url="https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search"
    params={"publishedFrom":published_from,"publishedTo":published_to,"limit":min(max(limit,1),100)}
    with httpx.Client(timeout=25,follow_redirects=True) as client:
        r=client.get(url,params=params,headers={"Accept":"application/json"}); r.raise_for_status(); payload=r.json()
    releases=payload.get("releases") or []
    mapped=[]
    for rel in releases:
        tender=rel.get("tender") or {}; parties=rel.get("parties") or []
        buyer=(rel.get("buyer") or {}).get("name") or next((p.get("name") for p in parties if "buyer" in p.get("roles",[])),None)
        val=(tender.get("value") or {}).get("amount"); deadline=(tender.get("tenderPeriod") or {}).get("endDate")
        items=tender.get("items") or []; cpv=next(((i.get("classification") or {}).get("id") for i in items if i.get("classification")),None)
        tid=str(rel.get("ocid") or rel.get("id") or uuid.uuid4())
        mapped.append(TenderIn(id=tid,source="Contracts Finder OCDS",source_url=str(r.url),title=tender.get("title") or "Public contract",description=tender.get("description") or "",buyer=buyer,value=val,currency=(tender.get("value") or {}).get("currency") or "GBP",deadline=deadline,region=None,cpv=cpv))
    return ingest(mapped)

@app.post("/api/profiles")
def create_profile(p:ProfileIn):
    pid=p.id or str(uuid.uuid4()); db.execute("INSERT OR REPLACE INTO profiles(id,name,payload_json) VALUES(?,?,?)",(pid,p.name,json.dumps(p.model_dump(mode="json")))); return {"profile_id":pid}

@app.get("/api/matches/{profile_id}")
def matches(profile_id:str,limit:int=100):
    rows=db.query("SELECT payload_json FROM profiles WHERE id=?",(profile_id,))
    if not rows: raise HTTPException(404,"profile not found")
    p=ProfileIn(**json.loads(rows[0]["payload_json"])); tenders=db.query("SELECT id,source,source_url,title,description,buyer,value,currency,deadline,region,cpv FROM tenders LIMIT ?",(min(max(limit,1),500),))
    out=[qualify(t,p) | {"title":t["title"],"buyer":t.get("buyer"),"value":t.get("value"),"deadline":t.get("deadline"),"source_url":t.get("source_url")} for t in tenders]; out.sort(key=lambda x:x["score"],reverse=True); return out

@app.post("/api/decisions/{profile_id}/{tender_id}")
def save_decision(profile_id:str,tender_id:str):
    pr=db.query("SELECT payload_json FROM profiles WHERE id=?",(profile_id,)); tr=db.query("SELECT id,source,source_url,title,description,buyer,value,currency,deadline,region,cpv FROM tenders WHERE id=?",(tender_id,))
    if not pr or not tr: raise HTTPException(404,"profile or tender not found")
    q=qualify(tr[0],ProfileIn(**json.loads(pr[0]["payload_json"]))); db.execute("INSERT INTO decisions(tender_id,profile_id,decision,score,rationale_json) VALUES(?,?,?,?,?)",(tender_id,profile_id,q["decision"],q["score"],json.dumps(q))); db.event(APP,"bid_decision",tender_id,q); return q
