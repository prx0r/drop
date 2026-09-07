from __future__ import annotations
from ..db import connect,jdump
from ..models import SupportRequest
from .catalog import get_product
from .markets import get_market

def answer_guarded(req:SupportRequest)->dict:
    market=get_market(req.market_code); facts={}
    if req.product_slug:
        try: facts=get_product(req.product_slug)['facts']
        except KeyError: facts={}
    q=req.question.lower(); answer=None
    if 'warranty' in q and facts:
        answer=f"The recorded warranty is {facts.get('warranty_months',0)} months. I can relay any warranty-detail question to a human before you buy."
    elif 'delivery' in q or 'shipping' in q:
        answer=f"Delivery is market- and supplier-specific. For {market.name}, we show the confirmed delivery window at checkout and avoid promising a date that is not in supplier data."
    elif 'return' in q:
        answer="Returns depend on the product and destination. I can show the exact policy attached to this SKU or hand this to a human rather than guess."
    else:
        answer="I can help compare products using verified catalog facts. For anything not in the product record, I will create a support ticket instead of inventing an answer."
    with connect() as c:
        cur=c.execute('INSERT INTO support_tickets(payload_json,status) VALUES(?,?)',(jdump(req.model_dump()),'callback_requested' if req.wants_callback else 'open'))
        ticket_id=cur.lastrowid
    return {'ticket_id':ticket_id,'answer':answer,'callback_requested':req.wants_callback,'human_handoff':True if req.wants_callback or not facts else False}
