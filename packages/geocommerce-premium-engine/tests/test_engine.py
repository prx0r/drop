import json
from pathlib import Path
from fastapi.testclient import TestClient
from geocommerce.models import ProductCreate,ProductFacts,MarketSignal,SupplierOffer,EconomicsInput,SupportRequest
from geocommerce.services.economics import compute_economics,score_opportunity
from geocommerce.services.markets import get_market
from geocommerce.services.catalog import upsert_product
from geocommerce.services.signals import save_signal,save_offer
from geocommerce.services.opportunities import evaluate
from geocommerce.services.feed import build_title
from geocommerce.services.support import answer_guarded
from geocommerce.app import app

ROOT=Path(__file__).resolve().parents[1]

def seed_one(slug='test-premium'):
    p=ProductCreate(slug=slug,name='Premium Test Machine',category='test',supplier_cost=300,supplier_currency='EUR',facts=ProductFacts(materials=['steel'],features={'dual_motor':True},warranty_months=24,advisor_fit=.9,visual_demo_fit=.9,supplier_quality=.9))
    upsert_product(p)
    s=MarketSignal(product_slug=slug,market_code='FI',query='premium test machine',currency='EUR',avg_monthly_searches=1800,competition_index=25,cpc_low=.3,cpc_high=.9,avg_cpc=.55,benchmark_price_gross=999,source='test',observed_at='2026-09-04T00:00:00Z')
    o=SupplierOffer(product_slug=slug,supplier='test-supplier',unit_cost=300,currency='EUR',shipping_cost=30,shipping_days=5,stock=10,ship_from_country='DE',observed_at='2026-09-04T00:00:00Z',reliability=.9)
    save_signal(s); save_offer(o); return p,s,o

def test_economics_positive_and_headroom():
    e=compute_economics(EconomicsInput(price_gross=1000,supplier_cost=300,shipping_cost=30,vat_rate=.25,duty_rate=.03,avg_cpc=.5,conservative_cvr=.015))
    assert e['contribution']>300
    assert e['break_even_cpc']>5
    assert e['cpc_headroom']>5

def test_currency_mismatch_is_hard_gate():
    facts=ProductFacts(advisor_fit=.9,supplier_quality=.9)
    m=get_market('FI')
    s=MarketSignal(product_slug='x',market_code='FI',query='x',currency='USD',avg_monthly_searches=1000,competition_index=20,cpc_low=.2,cpc_high=.8,avg_cpc=.5,benchmark_price_gross=1000,source='x',observed_at='x')
    o=SupplierOffer(product_slug='x',supplier='x',unit_cost=300,currency='EUR',shipping_cost=10,shipping_days=3,observed_at='x')
    r=score_opportunity('x',facts,m,s,o)
    assert r.verdict=='REJECT' and 'currency_not_normalized' in r.gates

def test_regulated_product_rejected():
    m=get_market('FI'); facts=ProductFacts(regulated=True,advisor_fit=.9,supplier_quality=.9)
    s=MarketSignal(product_slug='x2',market_code='FI',query='x',currency='EUR',avg_monthly_searches=5000,competition_index=5,cpc_low=.1,cpc_high=.2,avg_cpc=.1,benchmark_price_gross=2000,source='x',observed_at='x')
    o=SupplierOffer(product_slug='x2',supplier='x',unit_cost=200,currency='EUR',shipping_cost=10,shipping_days=2,observed_at='x')
    r=score_opportunity('x2',facts,m,s,o)
    assert r.verdict=='REJECT' and 'regulated_or_high_liability' in r.gates

def test_end_to_end_opportunity():
    seed_one('test-e2e')
    r=evaluate('test-e2e','FI')
    assert r.score>60 and r.verdict in {'FREE_LISTING_TEST','PAID_TEST'}

def test_feed_title_uses_only_verified_features():
    _,s,_=seed_one('test-title')
    title=build_title('Premium Test Machine',{'materials':['steel'],'features':{'dual_motor':True}},s)
    assert 'dual motor' in title and 'waterproof' not in title

def test_support_refuses_unknown_spec():
    seed_one('test-support')
    r=answer_guarded(SupportRequest(market_code='FI',product_slug='test-support',name='A',email='a@example.com',question='Does it have a feature that is not recorded?'))
    assert 'instead of inventing' in r['answer']

def test_admin_auth_required():
    client=TestClient(app)
    r=client.post('/v1/evaluate',json={'product_slug':'nope','market_code':'FI'})
    assert r.status_code==401

def test_public_advisor_and_storefront():
    seed_one('test-store')
    client=TestClient(app)
    a=client.post('/v1/advisor',json={'market_code':'FI','budget':1200,'priorities':['steel'],'constraints':{}})
    assert a.status_code==200 and any(x['slug']=='test-store' for x in a.json()['recommendations'])
    p=client.get('/fi/products/test-store')
    assert p.status_code==200
    assert 'Find my best fit' in p.text
    assert 'Ask for a human callback' in p.text
    assert 'Verified facts' in p.text

def test_market_config_has_local_checkout():
    assert 'Vipps' in get_market('NO').checkout_methods
    assert any('bank' in x.lower() for x in get_market('FI').checkout_methods)

def test_demo_json_valid():
    for name in ['demo_catalog.json','demo_signals.json','demo_offers.json']:
        assert json.loads((ROOT/'data'/name).read_text())

def test_ecb_fx_parse_and_cross_convert():
    from geocommerce.adapters.ecb_fx import parse_ecb_rates, convert_amount
    xml='''<Envelope><Cube><Cube time="2026-09-03"><Cube currency="USD" rate="1.2"/><Cube currency="NOK" rate="12"/></Cube></Cube></Envelope>'''
    rates=parse_ecb_rates(xml)
    assert rates['EUR']==1.0 and rates['USD']==1.2
    # 120 USD = 100 EUR = 1200 NOK
    assert convert_amount(120,'USD','NOK',rates)==1200


def test_keyword_cluster_aggregation_is_conservative():
    from geocommerce.services.scanner import aggregate_keyword_metrics
    rows=[
        {'avg_monthly_searches':1000,'competition_index':20,'low_top_page_bid':.4,'high_top_page_bid':1.0,'average_cpc':.6},
        {'avg_monthly_searches':800,'competition_index':30,'low_top_page_bid':.5,'high_top_page_bid':1.2,'average_cpc':.7},
    ]
    x=aggregate_keyword_metrics(rows)
    assert x['avg_monthly_searches']==1000  # not 1800: synonym demand must not be double-counted
    assert .6 < x['avg_cpc'] < .7


def test_shopping_snapshot_median_and_seller_count():
    from geocommerce.services.scanner import shopping_snapshot
    x=shopping_snapshot({'shopping_results':[{'extracted_price':100,'source':'A'},{'extracted_price':130,'source':'B'},{'extracted_price':999,'source':'A'}]})
    assert x['benchmark_price_gross']==130
    assert x['shopping_seller_count']==2


def test_localization_manifest_is_fact_bounded():
    from geocommerce.services.localization import compile_localized_manifest
    seed_one('test-localize')
    manifest=compile_localized_manifest('test-localize','FI')
    assert manifest['translation_status']=='source_only'
    assert manifest['verified_facts']['features']['dual_motor'] is True
    assert 'waterproof' not in json.dumps(manifest).lower()

def test_sirv_spin_requires_real_frame_sequence():
    from geocommerce.adapters.sirv import spin_manifest
    import pytest
    with pytest.raises(ValueError):
        spin_manifest(['x.jpg']*7)
    m=spin_manifest([f'{i}.jpg' for i in range(24)])
    assert m['frame_count']==24 and 'no generative geometry edits' in m['qa']

def test_supplier_audit_requires_truth_and_sample_for_premium():
    from geocommerce.services.supplier_audit import SupplierAuditInput,audit_supplier
    bad=audit_supplier(SupplierAuditInput(shipping_days=5,warranty_months=24,sample_order_passed=True))
    assert bad['stage']=='REJECT' and 'missing_product_truth' in bad['gates']
    good=audit_supplier(SupplierAuditInput(authorized_reseller_path=True,eu_or_local_warehouse=True,tracked_shipping=True,shipping_days=5,warranty_months=24,local_return_address=True,live_stock_signal=True,gtin_or_mpn_present=True,complete_spec_sheet=True,sample_order_passed=True,replacement_parts=True,support_contact=True))
    assert good['stage']=='APPROVE' and good['score']>=90


def test_best_seller_normalization_prioritizes_riser():
    from geocommerce.services.discovery import normalize_best_seller_rows
    rows=[{'bestSellersProductClusterView':{'title':'A','rank':'5','relativeDemand':'HIGH','relativeDemandChange':'RISER','variantGtins':['1']}},{'bestSellersProductClusterView':{'title':'B','rank':'1','relativeDemand':'HIGH','relativeDemandChange':'FLAT','variantGtins':['2']}}]
    out=normalize_best_seller_rows(rows)
    assert out[0]['title']=='A' or out[0]['research_priority']>=out[1]['research_priority']
    assert out[0]['next_actions']

def test_intra_eu_trade_has_no_customs_duty_reserve():
    from geocommerce.services.trade import estimated_duty_rate,requires_import_clearance
    assert estimated_duty_rate('DE','FI',.04)==0
    assert requires_import_clearance('DE','FI') is False
    assert requires_import_clearance('DE','NO') is True


def test_premium_cross_border_import_requires_prepaid_tax():
    from geocommerce.models import ProductFacts,MarketSignal,SupplierOffer
    from geocommerce.services.economics import score_opportunity
    from geocommerce.services.markets import get_market
    m=get_market('NO')
    s=MarketSignal(product_slug='import-x',market_code='NO',query='x',currency='NOK',avg_monthly_searches=5000,competition_index=10,cpc_low=2,cpc_high=5,avg_cpc=3,benchmark_price_gross=15000,source='test',observed_at='x')
    o=SupplierOffer(product_slug='import-x',supplier='eu',unit_cost=4000,currency='NOK',shipping_cost=500,shipping_days=5,ship_from_country='DE',observed_at='x',reliability=.9,taxes_prepaid=False)
    r=score_opportunity('import-x',ProductFacts(advisor_fit=.9,supplier_quality=.9),m,s,o)
    assert r.verdict=='REJECT' and 'premium_import_not_prepaid' in r.gates


def test_offer_currency_normalization_is_deterministic():
    from geocommerce.models import SupplierOffer
    from geocommerce.services.offer_normalization import normalize_offer_currency
    o=SupplierOffer(product_slug='fx-x',supplier='s',unit_cost=100,currency='USD',shipping_cost=10,shipping_days=3,observed_at='x')
    n=normalize_offer_currency(o,'FI',lambda amount,a,b: amount*.9)
    assert n.currency=='EUR' and n.unit_cost==90 and n.shipping_cost==9
