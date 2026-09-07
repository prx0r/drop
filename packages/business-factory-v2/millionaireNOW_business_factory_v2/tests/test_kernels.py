from __future__ import annotations
import importlib, os, sys
from pathlib import Path
from fastapi.testclient import TestClient

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
os.environ["ADMIN_TOKEN"]="test-secret"


def load(name,tmp_path):
    os.environ["DB_PATH"]=str(tmp_path/f"{name}.db")
    sys.modules.pop(f"{name}.app",None)
    return importlib.import_module(f"{name}.app")


def admin(): return {"X-Admin-Token":"test-secret"}


def test_saas_savings_end_to_end(tmp_path):
    m=load("01_saas_savings_desk",tmp_path); c=TestClient(m.app)
    assert c.get("/health").status_code==200
    p={"subscriptions":[{"vendor":"ToolA","category":"crm","annual_cost":12000,"seats":10,"active_seats":8,"quoted_increase_pct":10}]}
    r=c.post("/api/analyze",json=p); assert r.status_code==200
    data=r.json(); assert data["conservative_opportunity"]==3600.0
    case=c.post("/api/cases",json={**p,"email":"buyer@example.com","consent":True}); assert case.status_code==200 and case.json()["case_id"]
    bad=c.post("/api/admin/benchmarks",json={"vendor":"ToolA","annual_unit_price":800,"source_url":"https://example.com/source","observed_at":"2026-09-01T00:00:00Z"}); assert bad.status_code==401
    good=c.post("/api/admin/benchmarks",headers=admin(),json={"vendor":"ToolA","annual_unit_price":800,"source_url":"https://example.com/source","observed_at":"2026-09-01T00:00:00Z"}); assert good.status_code==200


def test_signal_radar_ingest_score_action(tmp_path):
    m=load("02_signal_lead_radar",tmp_path); c=TestClient(m.app)
    sig=[{"id":"p1","source":"test","source_url":"https://example.com/p1","title":"Rear extension and loft conversion","description":"Residential extension","location":"Leicester","published_at":"2026-09-03T00:00:00Z"}]
    assert c.post("/api/admin/signals",headers=admin(),json=sig).status_code==200
    r=c.get("/api/signals/builders?min_score=1"); assert r.status_code==200 and r.json()[0]["id"]=="p1" and r.json()[0]["score"]>30
    assert c.post("/api/actions",json={"signal_id":"p1","vertical":"builders","status":"contacted","note":"manual letter"}).status_code==200


def test_tender_qualifier_hard_gates(tmp_path):
    m=load("03_tender_bid_desk",tmp_path); c=TestClient(m.app)
    tender=[{"id":"t1","source":"test","source_url":"https://example.com/t1","title":"Managed cyber security service","description":"SOC monitoring and incident response","buyer":"Council","value":100000,"currency":"GBP","deadline":"2026-10-01T12:00:00Z","region":"London","cpv":"72000000"}]
    assert c.post("/api/admin/tenders",headers=admin(),json=tender).status_code==200
    pr={"id":"p1","name":"SecCo","capabilities":["cyber security","SOC monitoring","incident response"],"regions":["London"],"min_value":20000,"max_value":200000,"cpv_prefixes":["72"],"must_have_terms":["security"],"exclusion_terms":["construction"]}
    assert c.post("/api/profiles",json=pr).status_code==200
    r=c.get("/api/matches/p1"); assert r.status_code==200 and r.json()[0]["decision"] in {"BID","REVIEW"} and not r.json()[0]["hard_failures"]
    q=c.post("/api/decisions/p1/t1"); assert q.status_code==200


def test_reactivator_compliance_and_export(tmp_path):
    m=load("04_database_reactivator",tmp_path); c=TestClient(m.app)
    payload={"business_name":"RoofCo","offer":"We have two survey slots this week","booking_url":"https://example.com/book","contacts":[
      {"name":"Allowed","email":"a@example.com","subscriber_type":"individual","consent_basis":"explicit_consent","optout_offered_at_collection":True},
      {"name":"Blocked","email":"b@example.com","subscriber_type":"individual","consent_basis":"unknown","optout_offered_at_collection":False}
    ]}
    r=c.post("/api/campaigns",json=payload); assert r.status_code==200 and r.json()["eligible"]==1 and r.json()["blocked"]==1
    cid=r.json()["campaign_id"]; review=c.get(f"/api/campaigns/{cid}/review").json(); allowed=next(x for x in review if x["name"]=="Allowed"); blocked=next(x for x in review if x["name"]=="Blocked")
    assert allowed["draft"] and blocked["draft"] is None
    assert c.post(f"/api/admin/contacts/{allowed['id']}/approve",headers=admin()).status_code==200
    exp=c.get(f"/api/admin/campaigns/{cid}/export",headers=admin()); assert exp.status_code==200 and len(exp.json())==1
    assert c.post(f"/api/contacts/{allowed['id']}/outcome",json={"outcome":"unsubscribed"}).status_code==200
    exp2=c.get(f"/api/admin/campaigns/{cid}/export",headers=admin()); assert exp2.json()==[]


def test_rfq_full_flow_and_commission_not_ranked(tmp_path):
    m=load("05_rfq_sourcing_desk",tmp_path); c=TestClient(m.app)
    s1=c.post("/api/admin/suppliers",headers=admin(),json={"id":"s1","name":"Cheap High Commission","capabilities":["custom cardboard packaging"],"certifications":["FSC"],"regions":["UK"],"min_qty":100,"commission_pct":20}); assert s1.status_code==200
    s2=c.post("/api/admin/suppliers",headers=admin(),json={"id":"s2","name":"Fast Low Commission","capabilities":["custom cardboard packaging"],"certifications":["FSC"],"regions":["UK"],"min_qty":100,"commission_pct":1}); assert s2.status_code==200
    rfq=c.post("/api/rfqs",json={"title":"Boxes","description":"Custom boxes","quantity":1000,"budget":1800,"currency":"GBP","required_capabilities":["custom cardboard packaging"],"required_certifications":["FSC"],"delivery_region":"UK"}); rid=rfq.json()["rfq_id"]
    matches=c.get(f"/api/rfqs/{rid}/suppliers"); assert matches.status_code==200 and len(matches.json())==2
    q1=c.post(f"/api/rfqs/{rid}/quotes",headers=admin(),json={"supplier_id":"s1","unit_price":1.5,"shipping":200,"fees":0,"lead_days":30}); q2=c.post(f"/api/rfqs/{rid}/quotes",headers=admin(),json={"supplier_id":"s2","unit_price":1.6,"shipping":100,"fees":0,"lead_days":5}); assert q1.status_code==q2.status_code==200
    comp=c.get(f"/api/rfqs/{rid}/comparison"); assert comp.status_code==200 and all(x["commission_excluded_from_rank"] for x in comp.json())
    top=comp.json()[0]; assert top["supplier_id"]=="s2"  # faster and same landed total despite 20x lower commission
    assert c.post(f"/api/rfqs/{rid}/award/{top['quote_id']}?actual_revenue=1700").status_code==200

def test_saas_requires_consent_for_case(tmp_path):
    m=load("01_saas_savings_desk",tmp_path); c=TestClient(m.app)
    p={"subscriptions":[{"vendor":"X","category":"crm","annual_cost":1000,"seats":5,"active_seats":5}],"email":"x@example.com","consent":False}
    assert c.post("/api/cases",json=p).status_code==400


def test_tender_no_bid_on_exclusion(tmp_path):
    m=load("03_tender_bid_desk",tmp_path); c=TestClient(m.app)
    c.post("/api/admin/tenders",headers=admin(),json=[{"id":"t2","title":"Construction security fencing","description":"construction works","value":50000}])
    c.post("/api/profiles",json={"id":"p2","name":"Cyber","capabilities":["security"],"exclusion_terms":["construction"]})
    result=c.get("/api/matches/p2").json()[0]
    assert result["decision"]=="NO_BID" and result["score"]==0


def test_reactivator_opted_out_always_blocked(tmp_path):
    m=load("04_database_reactivator",tmp_path); c=TestClient(m.app)
    r=c.post("/api/campaigns",json={"business_name":"X","offer":"Return","contacts":[{"email":"x@example.com","subscriber_type":"corporate","consent_basis":"corporate_subscriber","opted_out":True}]}).json()
    assert r["eligible"]==0 and r["blocked"]==1


def test_rfq_certification_is_hard_gate(tmp_path):
    m=load("05_rfq_sourcing_desk",tmp_path); c=TestClient(m.app)
    c.post("/api/admin/suppliers",headers=admin(),json={"id":"sbad","name":"No Cert","capabilities":["metal fabrication"],"certifications":[],"regions":["UK"],"min_qty":1})
    rid=c.post("/api/rfqs",json={"title":"Part","description":"metal","quantity":10,"required_capabilities":["metal fabrication"],"required_certifications":["ISO9001"],"delivery_region":"UK"}).json()["rfq_id"]
    x=c.get(f"/api/rfqs/{rid}/suppliers").json()[0]
    assert x["eligible"] is False and x["fit_score"]==0


def test_all_sensitive_admin_endpoints_reject_bad_token(tmp_path):
    for name,path,payload in [
      ("02_signal_lead_radar","/api/admin/signals",[]),
      ("03_tender_bid_desk","/api/admin/tenders",[]),
      ("05_rfq_sourcing_desk","/api/admin/suppliers",{"name":"X","capabilities":["x"]}),
    ]:
        m=load(name,tmp_path); c=TestClient(m.app)
        assert c.post(path,headers={"X-Admin-Token":"wrong"},json=payload).status_code==401
