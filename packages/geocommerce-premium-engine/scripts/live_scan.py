#!/usr/bin/env python
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from geocommerce.settings import settings
from geocommerce.adapters.google_ads import GoogleAdsKeywordAdapter
from geocommerce.adapters.serpapi import SerpApiShoppingAdapter
from geocommerce.adapters.ecb_fx import ECBFXAdapter
from geocommerce.services.scanner import LiveMarketScanner
from geocommerce.services.opportunities import evaluate


def main():
    ap=argparse.ArgumentParser(description='Collect a live country-specific market signal and evaluate it.')
    ap.add_argument('product_slug'); ap.add_argument('market_code'); ap.add_argument('query')
    ap.add_argument('--ads-currency',required=True,help='currency of the Google Ads customer metrics, e.g. EUR')
    ap.add_argument('--benchmark-price',type=float)
    ap.add_argument('--shopping-location',help='SerpApi geocodable location; used only if benchmark is omitted')
    args=ap.parse_args()
    if not settings.google_ads_customer_id:
        raise SystemExit('GOOGLE_ADS_CUSTOMER_ID missing')
    fx=ECBFXAdapter()
    def convert(amount,a,b): return amount if a.upper()==b.upper() else fx.convert(amount,a,b)
    shopping=None if args.benchmark_price is not None else SerpApiShoppingAdapter()
    scanner=LiveMarketScanner(GoogleAdsKeywordAdapter(),convert,shopping)
    signal=scanner.scan(product_slug=args.product_slug,market_code=args.market_code.upper(),query=args.query,customer_id=settings.google_ads_customer_id,ads_currency=args.ads_currency.upper(),benchmark_price_gross=args.benchmark_price,shopping_location=args.shopping_location)
    result=evaluate(args.product_slug,args.market_code.upper())
    print(json.dumps({'signal':signal.model_dump(),'opportunity':result.model_dump()},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
