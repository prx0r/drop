from __future__ import annotations
from ..db import connect,jdump,jload
from ..models import MarketSignal,SupplierOffer
from .provenance import record

def save_signal(s:MarketSignal):
    with connect() as c:
        c.execute('INSERT OR IGNORE INTO market_signals(product_slug,market_code,query,payload_json,observed_at) VALUES(?,?,?,?,?)',(s.product_slug,s.market_code,s.query,jdump(s.model_dump()),s.observed_at))
    record('market_signal',f'{s.product_slug}:{s.market_code}:{s.query}',s.source,s.model_dump(),s.source_url,s.observed_at)
    return s

def latest_signal(product_slug:str,market_code:str)->MarketSignal:
    with connect() as c: row=c.execute('SELECT payload_json FROM market_signals WHERE product_slug=? AND market_code=? ORDER BY observed_at DESC,id DESC LIMIT 1',(product_slug,market_code)).fetchone()
    if not row: raise KeyError(f'no signal for {product_slug}/{market_code}')
    return MarketSignal(**jload(row['payload_json']))

def save_offer(o:SupplierOffer):
    with connect() as c: c.execute('INSERT INTO supplier_offers(product_slug,supplier,payload_json,observed_at) VALUES(?,?,?,?)',(o.product_slug,o.supplier,jdump(o.model_dump()),o.observed_at))
    record('supplier_offer',f'{o.product_slug}:{o.supplier}',o.supplier,o.model_dump(),o.source_url,o.observed_at)
    return o

def latest_offer(product_slug:str,currency:str|None=None)->SupplierOffer:
    q='SELECT payload_json FROM supplier_offers WHERE product_slug=?'; args=[product_slug]
    with connect() as c: rows=c.execute(q+' ORDER BY observed_at DESC,id DESC',(product_slug,)).fetchall()
    for row in rows:
        o=SupplierOffer(**jload(row['payload_json']))
        if currency is None or o.currency==currency: return o
    raise KeyError(f'no supplier offer for {product_slug} in {currency or "any currency"}')
