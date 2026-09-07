from __future__ import annotations
import csv, io, re
from ..models import MarketSignal, MarketConfig

def build_title(name:str, facts:dict, signal:MarketSignal, max_len:int=150)->str:
    tokens=[name]
    feature_keys=[k.replace('_',' ') for k,v in facts.get('features',{}).items() if v is True][:3]
    materials=facts.get('materials',[])[:2]
    query=signal.query.strip()
    for part in feature_keys+materials+[query]:
        if part and part.lower() not in ' '.join(tokens).lower(): tokens.append(str(part))
    title=' – '.join(tokens)
    return re.sub(r'\s+',' ',title)[:max_len].rstrip(' –')

def merchant_tsv(products:list[dict], market:MarketConfig, signals:dict[str,MarketSignal], base_url:str)->str:
    fields=['id','title','description','link','image_link','availability','price','condition','brand','gtin','shipping_label']
    sio=io.StringIO(); w=csv.DictWriter(sio,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader()
    for p in products:
        if p['slug'] not in signals: continue
        sig=signals[p['slug']]; facts=p['facts']; title=build_title(p['name'],facts,sig)
        desc=f"{p['name']}. " + '; '.join(f"{k.replace('_',' ')}: {v}" for k,v in facts.get('features',{}).items())
        w.writerow({'id':f"{p['slug']}-{market.code.lower()}",'title':title,'description':desc[:5000],'link':f"{base_url.rstrip('/')}/{market.code.lower()}/products/{p['slug']}",'image_link':(p['images'][0] if p['images'] else ''),'availability':'in_stock','price':f"{sig.benchmark_price_gross*0.97:.2f} {market.currency}",'condition':'new','brand':'GeoCommerce Select','gtin':facts.get('gtin',''),'shipping_label':market.code})
    return sio.getvalue()
