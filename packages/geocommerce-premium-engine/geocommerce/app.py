from __future__ import annotations
from fastapi import FastAPI, Depends, Header, HTTPException
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from pydantic import BaseModel, Field
from .settings import settings
from .db import init_db
from .models import ProductCreate, MarketSignal, SupplierOffer, AdvisorRequest, SupportRequest, ExperimentUpdate
from .services.catalog import upsert_product, list_products
from .services.signals import save_signal, save_offer, latest_signal
from .services.opportunities import evaluate, leaderboard
from .services.markets import load_markets, get_market
from .services.storefront import render_product
from .services.advisor import recommend
from .services.support import answer_guarded
from .services.media import build_media_brief
from .services.feed import merchant_tsv
from .services.experiments import create as create_experiment, update as update_experiment, metrics as experiment_metrics
from .adapters.google_ads import GoogleAdsKeywordAdapter
from .adapters.merchant import MerchantReportsAdapter
from .adapters.cj import CJAdapter
from .adapters.kopy import KopyHandoffAdapter
from .adapters.serpapi import SerpApiShoppingAdapter
from .adapters.ecb_fx import ECBFXAdapter
from .adapters.llm import OpenAICompatibleLLMAdapter
from .adapters.photoroom import PhotoroomAdapter
from .adapters.runway import RunwayAdapter
from .adapters.veo import VeoAdapter
from .adapters.twilio import TwilioVoiceAdapter
from .adapters.shopify import ShopifyAdminAdapter
from .services.scanner import LiveMarketScanner
from .services.localization import compile_localized_manifest, llm_translator
from .services.offer_normalization import normalize_offer_currency
from .services.supplier_audit import SupplierAuditInput, audit_supplier
from .services.discovery import normalize_best_seller_rows

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app=FastAPI(title='GeoCommerce Premium Engine',version='0.1.0',lifespan=lifespan)

def admin(x_admin_token: str = Header(default='')):
    if x_admin_token != settings.admin_token: raise HTTPException(401,'invalid admin token')
    return True

class EvaluateBody(BaseModel):
    product_slug:str
    market_code:str
class ExperimentCreate(BaseModel):
    product_slug:str
    market_code:str
    budget:float=Field(gt=0)
class KeywordRequest(BaseModel):
    keywords:list[str]
    market_code:str
class CJSearchRequest(BaseModel):
    keyword:str
    country_code:str|None=None
class KopyRequest(BaseModel):
    urls:list[str]
    target_language:str
class LiveScanRequest(BaseModel):
    product_slug:str
    market_code:str
    query:str
    ads_currency:str
    benchmark_price_gross:float|None=None
    shopping_location:str|None=None
    use_shopping_snapshot:bool=False
class LocalizationRequest(BaseModel):
    product_slug:str
    market_code:str
    use_llm:bool=False
class NormalizeOfferRequest(BaseModel):
    offer:SupplierOffer
    market_code:str
class PackshotRequest(BaseModel):
    image_url:str
    background:str='FFFFFF'
class CallbackRequest(BaseModel):
    customer_number:str
    twiml_url:str
    status_callback:str
class ShopifyShellRequest(BaseModel):
    title:str
    product_type:str
    vendor:str='GeoCommerce'
class SupplierAuditBody(BaseModel):
    authorized_reseller_path:bool=False
    eu_or_local_warehouse:bool=False
    tracked_shipping:bool=False
    shipping_days:int=30
    warranty_months:int=0
    local_return_address:bool=False
    live_stock_signal:bool=False
    gtin_or_mpn_present:bool=False
    complete_spec_sheet:bool=False
    sample_order_passed:bool=False
    replacement_parts:bool=False
    support_contact:bool=False

@app.get('/health')
def health(): return {'ok':True,'service':'geocommerce','version':'0.1.0'}
@app.get('/v1/markets')
def markets(): return [m.model_dump() for m in load_markets().values()]
@app.get('/v1/products')
def products(): return list_products()
@app.post('/v1/products',dependencies=[Depends(admin)])
def product_create(p:ProductCreate): return upsert_product(p)
@app.post('/v1/signals',dependencies=[Depends(admin)])
def signal_create(s:MarketSignal): return save_signal(s)
@app.post('/v1/supplier-offers',dependencies=[Depends(admin)])
def offer_create(o:SupplierOffer): return save_offer(o)
@app.post('/v1/evaluate',dependencies=[Depends(admin)])
def evaluate_one(b:EvaluateBody):
    try:return evaluate(b.product_slug,b.market_code)
    except KeyError as e: raise HTTPException(404,str(e))
@app.get('/v1/opportunities')
def opportunities(limit:int=50): return leaderboard(max(1,min(limit,200)))
@app.get('/{market_code}/products/{product_slug}',response_class=HTMLResponse)
def storefront(market_code:str,product_slug:str):
    try:return HTMLResponse(render_product(product_slug,market_code.upper()))
    except KeyError as e: raise HTTPException(404,str(e))
@app.get('/v1/merchant-feed/{market_code}.tsv',response_class=PlainTextResponse)
def feed(market_code:str):
    market=get_market(market_code); ps=list_products(); signals={}
    for p in ps:
        try:signals[p['slug']]=latest_signal(p['slug'],market.code)
        except KeyError:pass
    return PlainTextResponse(merchant_tsv(ps,market,signals,settings.public_base_url),media_type='text/tab-separated-values')
@app.post('/v1/advisor')
def advisor(req:AdvisorRequest): return {'recommendations':recommend(req.market_code,req.budget,req.priorities,req.constraints)}
@app.post('/v1/support')
def support(req:SupportRequest): return answer_guarded(req)
@app.get('/v1/media-brief/{market_code}/{product_slug}')
def media_brief(market_code:str,product_slug:str): return build_media_brief(product_slug,market_code.upper())
@app.post('/v1/experiments',dependencies=[Depends(admin)])
def experiment_create(req:ExperimentCreate): return {'id':create_experiment(req.product_slug,req.market_code.upper(),req.budget)}
@app.put('/v1/experiments/{experiment_id}',dependencies=[Depends(admin)])
def experiment_update(experiment_id:int,req:ExperimentUpdate): return update_experiment(experiment_id,**req.model_dump())
@app.get('/v1/experiments/{experiment_id}',dependencies=[Depends(admin)])
def experiment_get(experiment_id:int): return experiment_metrics(experiment_id)

@app.post('/v1/integrations/google-ads/historical',dependencies=[Depends(admin)])
def google_historical(req:KeywordRequest):
    m=get_market(req.market_code)
    customer=settings.google_ads_customer_id
    if not customer: raise HTTPException(400,'GOOGLE_ADS_CUSTOMER_ID missing')
    try:return GoogleAdsKeywordAdapter().historical_metrics(customer_id=customer,keywords=req.keywords,geo_id=m.google_geo_id,language_id=m.google_language_id)
    except Exception as e: raise HTTPException(502,str(e))
@app.get('/v1/integrations/merchant/best-sellers/{market_code}',dependencies=[Depends(admin)])
def merchant_best_sellers(market_code:str,category_id:str|None=None):
    try:return MerchantReportsAdapter().best_sellers(market_code.upper(),category_id)
    except Exception as e: raise HTTPException(502,str(e))
@app.post('/v1/integrations/cj/search',dependencies=[Depends(admin)])
def cj_search(req:CJSearchRequest):
    try:return CJAdapter().search_products(req.keyword,req.country_code)
    except Exception as e: raise HTTPException(502,str(e))
@app.post('/v1/integrations/kopy/handoff',dependencies=[Depends(admin)])
def kopy_handoff(req:KopyRequest): return KopyHandoffAdapter().manifest(req.urls,req.target_language)

@app.post('/v1/scan/live',dependencies=[Depends(admin)])
def live_scan(req:LiveScanRequest):
    customer=settings.google_ads_customer_id
    if not customer: raise HTTPException(400,'GOOGLE_ADS_CUSTOMER_ID missing')
    fx=ECBFXAdapter()
    def convert(amount:float,source:str,target:str)->float:
        if source.upper()==target.upper(): return amount
        return fx.convert(amount,source,target)
    shopping=SerpApiShoppingAdapter() if req.use_shopping_snapshot else None
    scanner=LiveMarketScanner(GoogleAdsKeywordAdapter(),convert,shopping)
    try:
        signal=scanner.scan(product_slug=req.product_slug,market_code=req.market_code.upper(),query=req.query,customer_id=customer,ads_currency=req.ads_currency.upper(),benchmark_price_gross=req.benchmark_price_gross,shopping_location=req.shopping_location)
        return signal.model_dump()
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/localization/manifest',dependencies=[Depends(admin)])
def localization_manifest(req:LocalizationRequest):
    try:
        translator=llm_translator(OpenAICompatibleLLMAdapter()) if req.use_llm else None
        return compile_localized_manifest(req.product_slug,req.market_code.upper(),translator)
    except KeyError as e: raise HTTPException(404,str(e))
    except Exception as e: raise HTTPException(502,str(e))

@app.get('/v1/fx/research/{from_currency}/{to_currency}',dependencies=[Depends(admin)])
def fx_research(from_currency:str,to_currency:str,amount:float=1.0):
    try:
        return {'amount':amount,'from':from_currency.upper(),'to':to_currency.upper(),'converted':ECBFXAdapter().convert(amount,from_currency,to_currency),'basis':'ECB reference rate; research only'}
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/supplier-offers/normalize',dependencies=[Depends(admin)])
def normalize_supplier_offer(req:NormalizeOfferRequest):
    fx=ECBFXAdapter()
    def convert(amount:float,source:str,target:str)->float:
        if source.upper()==target.upper(): return amount
        return fx.convert(amount,source,target)
    try:
        return normalize_offer_currency(req.offer,req.market_code.upper(),convert).model_dump()
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/suppliers/audit',dependencies=[Depends(admin)])
def supplier_audit(req:SupplierAuditBody):
    return audit_supplier(SupplierAuditInput(**req.model_dump()))

@app.get('/v1/discovery/best-sellers/{market_code}',dependencies=[Depends(admin)])
def discovery_best_sellers(market_code:str,category_id:str|None=None,report_date:str|None=None):
    market=get_market(market_code)
    try:
        rows=MerchantReportsAdapter().best_sellers(market.code,category_id,report_date=report_date)
        return {'market':market.code,'candidates':normalize_best_seller_rows(rows)}
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/media/packshot',dependencies=[Depends(admin)])
def create_packshot(req:PackshotRequest):
    try:
        content=PhotoroomAdapter().packshot_from_url(req.image_url,background=req.background)
        return Response(content=content,media_type='image/webp')
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/media/runway/{market_code}/{product_slug}',dependencies=[Depends(admin)])
def create_runway_video(market_code:str,product_slug:str):
    try:
        brief=build_media_brief(product_slug,market_code.upper())
        if not brief['reference_images']: raise HTTPException(400,'reference image required')
        shot=brief['shots'][0]
        return RunwayAdapter().image_to_video(brief['reference_images'][0],shot['prompt'])
    except HTTPException: raise
    except Exception as e: raise HTTPException(502,str(e))

@app.get('/v1/media/veo-spec/{market_code}/{product_slug}',dependencies=[Depends(admin)])
def veo_spec(market_code:str,product_slug:str):
    try:
        brief=build_media_brief(product_slug,market_code.upper())
        shot=brief['shots'][0]
        return VeoAdapter().build_job(prompt=shot['prompt'],reference_images=brief['reference_images'])
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/support/callback',dependencies=[Depends(admin)])
def callback(req:CallbackRequest):
    try:return TwilioVoiceAdapter().create_callback(customer_number=req.customer_number,twiml_url=req.twiml_url,status_callback=req.status_callback)
    except Exception as e: raise HTTPException(502,str(e))

@app.post('/v1/integrations/shopify/product-shell',dependencies=[Depends(admin)])
def shopify_product_shell(req:ShopifyShellRequest):
    try:return ShopifyAdminAdapter().create_product_shell(req.title,req.product_type,req.vendor)
    except Exception as e: raise HTTPException(502,str(e))
