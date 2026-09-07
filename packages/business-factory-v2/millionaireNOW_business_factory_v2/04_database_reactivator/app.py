from __future__ import annotations
import os, sys, uuid, json
from datetime import datetime, timezone
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi import Depends, HTTPException

ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from shared.app import make_app
from shared.db import DB
from shared.security import require_admin

APP="reactivator"; db=DB(os.getenv("DB_PATH",str(Path(__file__).with_name("app.db"))))
with db.connect() as con:
    con.executescript("""CREATE TABLE IF NOT EXISTS campaigns(id TEXT PRIMARY KEY, business_name TEXT NOT NULL, offer TEXT NOT NULL, booking_url TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS contacts(id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, name TEXT, email TEXT, phone TEXT, status TEXT, subscriber_type TEXT NOT NULL, consent_basis TEXT NOT NULL, optout_offered INTEGER NOT NULL, opted_out INTEGER NOT NULL DEFAULT 0, last_interaction TEXT, draft TEXT, approved INTEGER NOT NULL DEFAULT 0); CREATE TABLE IF NOT EXISTS outcomes(id INTEGER PRIMARY KEY AUTOINCREMENT, contact_id TEXT NOT NULL, outcome TEXT NOT NULL, revenue REAL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
app=make_app("Dormant Database Reactivator")

class ContactIn(BaseModel):
    name:str|None=None; email:str|None=None; phone:str|None=None; status:str="dormant"; subscriber_type:str=Field(pattern="^(individual|sole_trader|partnership|corporate)$"); consent_basis:str=Field(pattern="^(explicit_consent|soft_opt_in|corporate_subscriber|unknown)$"); optout_offered_at_collection:bool=False; opted_out:bool=False; last_interaction:datetime|None=None
class CampaignIn(BaseModel):
    business_name:str; offer:str; booking_url:str|None=None; contacts:list[ContactIn]=Field(min_length=1,max_length=10000)
class OutcomeIn(BaseModel):
    outcome:str=Field(pattern="^(replied_positive|replied_negative|not_now|unsubscribed|booked|held|won|lost)$"); revenue:float|None=Field(default=None,ge=0)

def eligible(c:ContactIn)->tuple[bool,str]:
    if c.opted_out: return False,"already opted out"
    if c.subscriber_type=="corporate" and c.consent_basis=="corporate_subscriber": return True,"corporate subscriber; still provide opt-out and assess data-protection lawful basis"
    if c.consent_basis=="explicit_consent": return True,"explicit consent recorded"
    if c.consent_basis=="soft_opt_in" and c.optout_offered_at_collection: return True,"soft opt-in asserted with collection-time opt-out recorded; verify similar-service and current eligibility"
    return False,"no recorded eligible basis for electronic reactivation"

def draft_message(business:str,offer:str,name:str|None,booking_url:str|None)->str:
    who=f" {name}" if name else ""
    book=f" {booking_url}" if booking_url else ""
    return f"Hi{who}, it’s {business}. You contacted us previously, so I wanted to check whether this is still relevant. {offer}.{book} If you’d rather not hear from us, reply STOP."

@app.post("/api/campaigns")
def create_campaign(c:CampaignIn):
    cid=str(uuid.uuid4()); db.execute("INSERT INTO campaigns(id,business_name,offer,booking_url) VALUES(?,?,?,?)",(cid,c.business_name,c.offer,c.booking_url)); eligible_count=0
    for item in c.contacts:
        ok,reason=eligible(item); contact_id=str(uuid.uuid4()); draft=draft_message(c.business_name,c.offer,item.name,c.booking_url) if ok else None
        db.execute("INSERT INTO contacts(id,campaign_id,name,email,phone,status,subscriber_type,consent_basis,optout_offered,opted_out,last_interaction,draft,approved) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,0)",(contact_id,cid,item.name,item.email,item.phone,item.status,item.subscriber_type,item.consent_basis,1 if item.optout_offered_at_collection else 0,1 if item.opted_out else 0,item.last_interaction.isoformat() if item.last_interaction else None,draft)); eligible_count+=1 if ok else 0
    db.event(APP,"campaign_created",cid,{"contacts":len(c.contacts),"eligible":eligible_count}); return {"campaign_id":cid,"contacts":len(c.contacts),"eligible":eligible_count,"blocked":len(c.contacts)-eligible_count,"note":"No messages are sent automatically. Review legality, approve eligible drafts, then export to the client's authorized sending system."}

@app.get("/api/campaigns/{cid}/review")
def review(cid:str):
    rows=db.query("SELECT id,name,email,phone,subscriber_type,consent_basis,optout_offered,opted_out,draft,approved FROM contacts WHERE campaign_id=?",(cid,)); return rows

@app.post("/api/admin/contacts/{contact_id}/approve",dependencies=[Depends(require_admin)])
def approve(contact_id:str):
    rows=db.query("SELECT * FROM contacts WHERE id=?",(contact_id,));
    if not rows: raise HTTPException(404,"contact not found")
    r=rows[0]
    if r["opted_out"] or not r["draft"]: raise HTTPException(400,"contact is not eligible for export")
    db.execute("UPDATE contacts SET approved=1 WHERE id=?",(contact_id,)); return {"ok":True}

@app.get("/api/admin/campaigns/{cid}/export",dependencies=[Depends(require_admin)])
def export(cid:str):
    return db.query("SELECT id,name,email,phone,draft FROM contacts WHERE campaign_id=? AND approved=1 AND opted_out=0 AND draft IS NOT NULL",(cid,))

@app.post("/api/contacts/{contact_id}/outcome")
def outcome(contact_id:str,o:OutcomeIn):
    if o.outcome=="unsubscribed": db.execute("UPDATE contacts SET opted_out=1,approved=0 WHERE id=?",(contact_id,))
    db.execute("INSERT INTO outcomes(contact_id,outcome,revenue) VALUES(?,?,?)",(contact_id,o.outcome,o.revenue)); db.event(APP,"reactivation_outcome",contact_id,o.model_dump()); return {"ok":True}

@app.get("/api/campaigns/{cid}/metrics")
def metrics(cid:str):
    total=db.query("SELECT COUNT(*) n FROM contacts WHERE campaign_id=?",(cid,))[0]["n"]
    approved=db.query("SELECT COUNT(*) n FROM contacts WHERE campaign_id=? AND approved=1",(cid,))[0]["n"]
    outcomes=db.query("SELECT o.outcome,COUNT(*) n,COALESCE(SUM(o.revenue),0) revenue FROM outcomes o JOIN contacts c ON c.id=o.contact_id WHERE c.campaign_id=? GROUP BY o.outcome",(cid,))
    return {"contacts":total,"approved_for_export":approved,"outcomes":outcomes}
