from __future__ import annotations
from jinja2 import Environment,FileSystemLoader,select_autoescape
from pathlib import Path
from .catalog import get_product
from .markets import get_market
from .signals import latest_signal
ROOT=Path(__file__).resolve().parents[1]
env=Environment(loader=FileSystemLoader(ROOT/'templates'),autoescape=select_autoescape())

def page_context(product_slug:str,market_code:str)->dict:
    p=get_product(product_slug); market=get_market(market_code); signal=latest_signal(product_slug,market.code)
    price=round(signal.benchmark_price_gross*0.97,2)
    mode='direct' if price<=market.direct_checkout_ceiling else 'assisted' if price<=market.assisted_checkout_ceiling else 'quote'
    return {'product':p,'market':market.model_dump(),'signal':signal.model_dump(),'price':price,'checkout_mode':mode}

def render_product(product_slug:str,market_code:str)->str:
    return env.get_template('product.html').render(**page_context(product_slug,market_code))
