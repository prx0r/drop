from __future__ import annotations
import os, sys, uuid
from datetime import date, datetime, timezone
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi import Depends, HTTPException

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from shared.app import make_app
from shared.db import DB
from shared.security import require_admin
from shared.provenance import record_observation
from shared.text import clamp

APP = "saas_savings"
DB_PATH = os.getenv("DB_PATH", str(Path(__file__).with_name("app.db")))
db = DB(DB_PATH)
with db.connect() as con:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS benchmarks(vendor TEXT NOT NULL, annual_unit_price REAL NOT NULL, seats INTEGER, source_url TEXT NOT NULL, observed_at TEXT NOT NULL, PRIMARY KEY(vendor,observed_at));
    CREATE TABLE IF NOT EXISTS cases(id TEXT PRIMARY KEY, email TEXT NOT NULL, consent INTEGER NOT NULL, analysis_json TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
    """)
app = make_app("SaaS Renewal Savings Desk")

class Subscription(BaseModel):
    vendor: str
    category: str
    annual_cost: float = Field(gt=0)
    seats: int = Field(ge=1)
    active_seats: int = Field(ge=0)
    renewal_date: date | None = None
    quoted_increase_pct: float = Field(default=0, ge=0, le=200)

class Portfolio(BaseModel):
    subscriptions: list[Subscription] = Field(min_length=1, max_length=500)

class CaseIn(Portfolio):
    email: str
    consent: bool

class BenchmarkIn(BaseModel):
    vendor: str
    annual_unit_price: float = Field(gt=0)
    seats: int | None = Field(default=None, ge=1)
    source_url: str
    observed_at: datetime


def latest_benchmark(vendor: str) -> dict | None:
    rows = db.query("SELECT * FROM benchmarks WHERE lower(vendor)=lower(?) ORDER BY observed_at DESC LIMIT 1", (vendor,))
    return rows[0] if rows else None


def analyze_portfolio(p: Portfolio) -> dict:
    today = date.today()
    category_counts: dict[str,int] = {}
    for s in p.subscriptions: category_counts[s.category.lower()] = category_counts.get(s.category.lower(),0)+1
    rows=[]; total=0.0
    for s in p.subscriptions:
        active=min(s.active_seats,s.seats)
        unit=s.annual_cost/s.seats
        unused=max(0,s.seats-active)
        unused_waste=unused*unit
        renewal_increase=s.annual_cost*(s.quoted_increase_pct/100)
        bench=latest_benchmark(s.vendor)
        benchmark_gap=0.0; benchmark_note=None
        if bench:
            observed=datetime.fromisoformat(str(bench["observed_at"]).replace("Z","+00:00"))
            age=(datetime.now(timezone.utc)-observed.astimezone(timezone.utc)).days
            if age <= 180:
                benchmark_gap=max(0.0, unit-float(bench["annual_unit_price"]))*active
                benchmark_note={"annual_unit_price":bench["annual_unit_price"],"age_days":age,"source_url":bench["source_url"]}
        days=(s.renewal_date-today).days if s.renewal_date else None
        urgency=1.0 if days is not None and 0 <= days <= 45 else 0.6 if days is not None and days <= 90 else 0.2
        duplicate=category_counts[s.category.lower()] > 1
        # avoid double counting renewal increase and benchmark gap: use the larger renewal lever.
        opportunity=unused_waste+max(renewal_increase,benchmark_gap)
        confidence=0.9 if bench else 0.65
        score=round(100*clamp((opportunity/max(s.annual_cost,1))*0.6+urgency*0.25+(0.15 if duplicate else 0))*confidence)
        total += opportunity
        rows.append({"vendor":s.vendor,"annual_cost":round(s.annual_cost,2),"unused_seat_waste":round(unused_waste,2),"renewal_or_benchmark_opportunity":round(max(renewal_increase,benchmark_gap),2),"duplicate_category_review":duplicate,"days_to_renewal":days,"benchmark":benchmark_note,"priority_score":score})
    rows.sort(key=lambda x:x["priority_score"],reverse=True)
    return {"annual_spend":round(sum(s.annual_cost for s in p.subscriptions),2),"conservative_opportunity":round(total,2),"success_fee_example_20pct":round(total*0.2,2),"opportunities":rows,"methodology":"Seat waste is arithmetic. Renewal increase is quoted increase. Benchmark gaps are used only when a sourced observation <=180 days exists. Duplicate categories are review flags, not assumed savings."}

@app.post("/api/analyze")
def analyze(p: Portfolio):
    result=analyze_portfolio(p); db.event(APP,"analysis",None,result); return result

@app.post("/api/cases")
def create_case(c: CaseIn):
    if not c.consent: raise HTTPException(400,"consent required")
    result=analyze_portfolio(c); cid=str(uuid.uuid4())
    import json
    db.execute("INSERT INTO cases(id,email,consent,analysis_json) VALUES(?,?,?,?)",(cid,c.email,1,json.dumps(result)))
    db.event(APP,"case_created",cid,{"email":c.email,"opportunity":result["conservative_opportunity"]})
    return {"case_id":cid,"analysis":result,"next_step":"Offer a no-upfront renewal review with an explicitly agreed success fee on verified savings."}

@app.post("/api/admin/benchmarks", dependencies=[Depends(require_admin)])
def add_benchmark(b: BenchmarkIn):
    db.execute("INSERT INTO benchmarks(vendor,annual_unit_price,seats,source_url,observed_at) VALUES(?,?,?,?,?)",(b.vendor,b.annual_unit_price,b.seats,b.source_url,b.observed_at.isoformat()))
    record_observation(db,APP,"benchmark",b.vendor,b.model_dump(mode="json"),b.source_url,b.observed_at.isoformat())
    return {"ok":True}
