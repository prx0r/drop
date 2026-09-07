from __future__ import annotations
from ..db import connect

def create(product_slug:str,market_code:str,budget:float):
    with connect() as c:
        cur=c.execute('INSERT INTO experiments(product_slug,market_code,budget) VALUES(?,?,?)',(product_slug,market_code,budget)); return cur.lastrowid

def update(exp_id:int,spend:float,clicks:int,conversions:int,revenue:float):
    with connect() as c:
        row=c.execute('SELECT budget FROM experiments WHERE id=?',(exp_id,)).fetchone()
        if not row: raise KeyError(exp_id)
        status='complete' if spend>=row['budget'] else 'running'
        c.execute('UPDATE experiments SET spend=?,clicks=?,conversions=?,revenue=?,status=? WHERE id=?',(spend,clicks,conversions,revenue,status,exp_id))
    return metrics(exp_id)

def metrics(exp_id:int):
    with connect() as c: row=c.execute('SELECT * FROM experiments WHERE id=?',(exp_id,)).fetchone()
    if not row: raise KeyError(exp_id)
    d=dict(row); d['cpc']=round(d['spend']/d['clicks'],2) if d['clicks'] else None; d['cvr']=round(d['conversions']/d['clicks'],4) if d['clicks'] else None; d['roas']=round(d['revenue']/d['spend'],2) if d['spend'] else None; return d
