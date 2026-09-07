from __future__ import annotations
from ..db import connect,jdump,jload
from ..models import ProductFacts
from .catalog import get_product
from .signals import latest_signal,latest_offer
from .markets import get_market
from .economics import score_opportunity

def evaluate(product_slug:str,market_code:str):
    p=get_product(product_slug); market=get_market(market_code); signal=latest_signal(product_slug,market.code); offer=latest_offer(product_slug,market.currency)
    score=score_opportunity(product_slug,ProductFacts(**p['facts']),market,signal,offer)
    with connect() as c: c.execute('INSERT INTO opportunities(product_slug,market_code,payload_json) VALUES(?,?,?)',(product_slug,market.code,jdump(score.model_dump())))
    return score

def leaderboard(limit:int=100):
    with connect() as c: rows=c.execute('SELECT payload_json FROM opportunities ORDER BY id DESC LIMIT 1000').fetchall()
    latest={}
    for row in rows:
        d=jload(row['payload_json']); key=(d['product_slug'],d['market_code'])
        if key not in latest: latest[key]=d
    return sorted(latest.values(),key=lambda x:x['score'],reverse=True)[:limit]
