from __future__ import annotations
import os, sys, uuid, json
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi import Depends, HTTPException

ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from shared.app import make_app
from shared.db import DB
from shared.security import require_admin
from shared.text import tokens, clamp

APP="rfq_desk"; db=DB(os.getenv("DB_PATH",str(Path(__file__).with_name("app.db"))))
with db.connect() as con:
    con.executescript("""CREATE TABLE IF NOT EXISTS suppliers(id TEXT PRIMARY KEY,name TEXT NOT NULL,capabilities_json TEXT NOT NULL,certifications_json TEXT NOT NULL,regions_json TEXT NOT NULL,min_qty INTEGER NOT NULL,commission_pct REAL NOT NULL DEFAULT 0); CREATE TABLE IF NOT EXISTS rfqs(id TEXT PRIMARY KEY,title TEXT NOT NULL,description TEXT NOT NULL,quantity INTEGER NOT NULL,budget REAL,currency TEXT NOT NULL,required_capabilities_json TEXT NOT NULL,required_certifications_json TEXT NOT NULL,delivery_region TEXT,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS quotes(id TEXT PRIMARY KEY,rfq_id TEXT NOT NULL,supplier_id TEXT NOT NULL,unit_price REAL NOT NULL,shipping REAL NOT NULL,fees REAL NOT NULL,lead_days INTEGER NOT NULL,valid_days INTEGER NOT NULL,notes TEXT,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS awards(id INTEGER PRIMARY KEY AUTOINCREMENT,rfq_id TEXT NOT NULL,quote_id TEXT NOT NULL,actual_revenue REAL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
app=make_app("B2B RFQ Sourcing Desk")

class SupplierIn(BaseModel):
    id:str|None=None; name:str; capabilities:list[str]=Field(min_length=1); certifications:list[str]=[]; regions:list[str]=[]; min_qty:int=Field(default=1,ge=1); commission_pct:float=Field(default=0,ge=0,le=100)
class RFQIn(BaseModel):
    title:str; description:str; quantity:int=Field(ge=1); budget:float|None=Field(default=None,gt=0); currency:str="GBP"; required_capabilities:list[str]=Field(min_length=1); required_certifications:list[str]=[]; delivery_region:str|None=None
class QuoteIn(BaseModel):
    supplier_id:str; unit_price:float=Field(gt=0); shipping:float=Field(default=0,ge=0); fees:float=Field(default=0,ge=0); lead_days:int=Field(ge=0); valid_days:int=Field(default=30,ge=1); notes:str|None=None

def supplier_match(s:dict,r:dict)->dict:
    caps=json.loads(s["capabilities_json"]); certs=set(json.loads(s["certifications_json"])); regions=[x.lower() for x in json.loads(s["regions_json"])]
    req_caps=json.loads(r["required_capabilities_json"]); req_certs=set(json.loads(r["required_certifications_json"]))
    hard=[]
    if r["quantity"]<s["min_qty"]: hard.append("quantity below supplier minimum")
    if not req_certs.issubset(certs): hard.append("missing required certification")
    if r.get("delivery_region") and regions and not any(x in r["delivery_region"].lower() for x in regions): hard.append("region mismatch")
    hay=tokens(" ".join(caps)); want=set().union(*(tokens(x) for x in req_caps)); cap=len(hay&want)/max(len(want),1)
    return {"supplier_id":s["id"],"supplier_name":s["name"],"eligible":not hard,"hard_failures":hard,"fit_score":0 if hard else round(100*clamp(cap)),"commission_pct":s["commission_pct"]}

@app.post("/api/admin/suppliers",dependencies=[Depends(require_admin)])
def add_supplier(s:SupplierIn):
    sid=s.id or str(uuid.uuid4()); db.execute("INSERT OR REPLACE INTO suppliers(id,name,capabilities_json,certifications_json,regions_json,min_qty,commission_pct) VALUES(?,?,?,?,?,?,?)",(sid,s.name,json.dumps(s.capabilities),json.dumps(s.certifications),json.dumps(s.regions),s.min_qty,s.commission_pct)); return {"supplier_id":sid}

@app.post("/api/rfqs")
def create_rfq(r:RFQIn):
    rid=str(uuid.uuid4()); db.execute("INSERT INTO rfqs(id,title,description,quantity,budget,currency,required_capabilities_json,required_certifications_json,delivery_region) VALUES(?,?,?,?,?,?,?,?,?)",(rid,r.title,r.description,r.quantity,r.budget,r.currency,json.dumps(r.required_capabilities),json.dumps(r.required_certifications),r.delivery_region)); db.event(APP,"rfq_created",rid,r.model_dump()); return {"rfq_id":rid}

@app.get("/api/rfqs/{rid}/suppliers")
def matches(rid:str):
    rr=db.query("SELECT * FROM rfqs WHERE id=?",(rid,));
    if not rr: raise HTTPException(404,"rfq not found")
    out=[supplier_match(s,rr[0]) for s in db.query("SELECT * FROM suppliers")]; out.sort(key=lambda x:x["fit_score"],reverse=True); return out

@app.post("/api/rfqs/{rid}/quotes",dependencies=[Depends(require_admin)])
def quote(rid:str,q:QuoteIn):
    if not db.query("SELECT id FROM rfqs WHERE id=?",(rid,)): raise HTTPException(404,"rfq not found")
    if not db.query("SELECT id FROM suppliers WHERE id=?",(q.supplier_id,)): raise HTTPException(404,"supplier not found")
    qid=str(uuid.uuid4()); db.execute("INSERT INTO quotes(id,rfq_id,supplier_id,unit_price,shipping,fees,lead_days,valid_days,notes) VALUES(?,?,?,?,?,?,?,?,?)",(qid,rid,q.supplier_id,q.unit_price,q.shipping,q.fees,q.lead_days,q.valid_days,q.notes)); return {"quote_id":qid}

@app.get("/api/rfqs/{rid}/comparison")
def comparison(rid:str):
    rr=db.query("SELECT * FROM rfqs WHERE id=?",(rid,));
    if not rr: raise HTTPException(404,"rfq not found")
    r=rr[0]; suppliers={s["id"]:s for s in db.query("SELECT * FROM suppliers")}; out=[]
    for q in db.query("SELECT * FROM quotes WHERE rfq_id=?",(rid,)):
        s=suppliers[q["supplier_id"]]; match=supplier_match(s,r); total=q["unit_price"]*r["quantity"]+q["shipping"]+q["fees"]
        budget_fit=1.0 if not r["budget"] else clamp(1-(max(0,total-r["budget"])/r["budget"]))
        speed=clamp(1-q["lead_days"]/120); rank=0 if not match["eligible"] else round(100*(match["fit_score"]/100*.45+budget_fit*.4+speed*.15))
        out.append({"quote_id":q["id"],"supplier_id":s["id"],"supplier_name":s["name"],"total_landed":round(total,2),"lead_days":q["lead_days"],"eligible":match["eligible"],"fit_score":match["fit_score"],"rank_score":rank,"commission_pct":s["commission_pct"],"commission_excluded_from_rank":True})
    out.sort(key=lambda x:(x["eligible"],x["rank_score"]),reverse=True); return out

@app.post("/api/rfqs/{rid}/award/{quote_id}")
def award(rid:str,quote_id:str,actual_revenue:float|None=None):
    rows=db.query("SELECT id FROM quotes WHERE id=? AND rfq_id=?",(quote_id,rid));
    if not rows: raise HTTPException(404,"quote not found")
    db.execute("INSERT INTO awards(rfq_id,quote_id,actual_revenue) VALUES(?,?,?)",(rid,quote_id,actual_revenue)); db.event(APP,"rfq_awarded",rid,{"quote_id":quote_id,"actual_revenue":actual_revenue}); return {"ok":True}
