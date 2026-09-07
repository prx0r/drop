from __future__ import annotations
from .catalog import list_products
from .markets import get_market
from .signals import latest_signal

def recommend(market_code:str,budget:float,priorities:list[str],constraints:dict)->list[dict]:
    market=get_market(market_code); rows=[]
    for p in list_products():
        try: sig=latest_signal(p['slug'],market.code)
        except KeyError: continue
        price=sig.benchmark_price_gross*0.97
        if price>budget: continue
        facts=p['facts']; score=facts.get('advisor_fit',0.5)*30+facts.get('supplier_quality',0.5)*25+(1-facts.get('return_risk',0.2))*20
        text=' '.join([p['name'],p['category'],*facts.get('materials',[]),*facts.get('features',{}).keys()]).lower()
        score+=sum(5 for pr in priorities if pr.lower() in text)
        rows.append({'slug':p['slug'],'name':p['name'],'price':round(price,2),'currency':market.currency,'fit_score':round(score,1),'why':[f"advisor fit {facts.get('advisor_fit',0):.0%}",f"supplier quality {facts.get('supplier_quality',0):.0%}"]})
    return sorted(rows,key=lambda x:x['fit_score'],reverse=True)[:5]
