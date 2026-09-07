from __future__ import annotations
from ..db import connect,jdump,jload
from ..models import ProductCreate
from .provenance import record

def upsert_product(p:ProductCreate):
    with connect() as c:
        c.execute('''INSERT INTO products(slug,name,category,supplier_cost,supplier_currency,supplier_id,supplier_url,images_json,facts_json)
        VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(slug) DO UPDATE SET name=excluded.name,category=excluded.category,supplier_cost=excluded.supplier_cost,supplier_currency=excluded.supplier_currency,supplier_id=excluded.supplier_id,supplier_url=excluded.supplier_url,images_json=excluded.images_json,facts_json=excluded.facts_json''',
        (p.slug,p.name,p.category,p.supplier_cost,p.supplier_currency,p.supplier_id,p.supplier_url,jdump(p.images),jdump(p.facts.model_dump())))
    record('product',p.slug,p.supplier_id,p.model_dump(),p.supplier_url)
    return p

def get_product(slug:str)->dict:
    with connect() as c:
        row=c.execute('SELECT * FROM products WHERE slug=?',(slug,)).fetchone()
    if not row: raise KeyError(slug)
    d=dict(row); d['images']=jload(d.pop('images_json')); d['facts']=jload(d.pop('facts_json')); return d

def list_products()->list[dict]:
    with connect() as c: rows=c.execute('SELECT * FROM products ORDER BY id').fetchall()
    out=[]
    for row in rows:
        d=dict(row); d['images']=jload(d.pop('images_json')); d['facts']=jload(d.pop('facts_json')); out.append(d)
    return out
