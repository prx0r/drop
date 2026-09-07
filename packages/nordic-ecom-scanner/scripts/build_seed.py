import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/live_screening_candidates.csv'

DK_LAMPS=[
('Sirius Tim rechargeable table lamp, black nickel 22 cm',479),
('Nordlux Mirano rechargeable table lamp, green',459),
('IP54 rechargeable LED table lamp, white, touch dimmable',279),
('Kave Home Arenys rechargeable table lamp, turquoise',799),
('3W rechargeable LED table lamp, brown, 4000mAh',454),
('Veli Line Shine rechargeable table lamp, green',109),
('House Nordic Wigan rechargeable table lamp',319),
('Sirius Tim rechargeable table lamp, white 22 cm',459),
('Nordlux Ellen rechargeable table lamp, green',319),
('Nielsen Light Move Me rechargeable lamp, light grey',299),
('Nielsen Light Bistro rechargeable table lamp, purple',254),
('Nielsen Light Nyhavn rechargeable table lamp, red',169),
('1W rechargeable LED table lamp, French Gold',235),
('Haipot rechargeable LED table lamp, dark red',599),
('Duni Zelda rechargeable table lamp, brass',1299),
]
DK_HANDLES=[
('Siena kitchen handle',55),('Conti cup handle',67),('Positano kitchen handle',72),
('Barga kitchen handle, matte brass',49),('Sala kitchen handle, matte brass',65),('Venosa handle, matte brass',69),
]
DK_MENU=[
('Securit Y-shaped A6 clear acrylic menu holder',95.20),
('Nobo A4 sign frame on stand',735.20),
('Securit MICHELLE black table lamp with board',495.20),
('A7 wooden menu/info holder',59.00),
]
NO_LAMPS=[
('Timo rechargeable outdoor table lamp',150),('Northlight rechargeable LED desk lamp',480),
('Frida rechargeable table lamp, beige',600),('LUTEC NOMA rechargeable table lamp 2-pack',549),
('Hygge rechargeable table lamp, antique',1099),('Modi rechargeable table lamp, red',1335),
('Joe rechargeable table lamp, 3W LED',2049),('Joy rechargeable table lamp, turquoise',1062),
('Halo Design Question rechargeable table lamp, black/brass',1315),('Nielsen Light Bistro rechargeable table lamp, green',571),
]
NO_HANDLES=[
('Beslag Design 0143-192 brushed brass handle',146),('Beslag Design Bella 160 brushed brass handle',118),
('Beslag Design Bror 160 brushed brass handle',66),('Beslag Design Profile 40mm brushed brass handle',53),
('Beslag Design Lounge 160 brushed brass handle',209),('Beslag Design Profile 160mm brushed brass handle',104),
('Beslagsboden B54 antique brass drawer handle 96mm',37),('Tapwell Bean 037 brass knob',295),
]
NO_ACOUSTIC=[
('Spilepanel Ro acoustic panel 21x600x2400 oak veneer',1179),('Lind acoustic panel 2390x600x19 oak',1999),
('Opus acoustic panel 600x2400 light',1299),('Fibrotech Quanti light oak acoustic panel',599),
('Fibrotech Square black oak acoustic panel 2-pack',400),('Fibrotech Square light oak acoustic panel 2-pack',399),
('Fibrotech acoustic panel 244 light oak',974),
]

fields=[
'country','niche','product_name','competitor_price_local','supplier_price_usd_low','supplier_price_usd_high','supplier_moq','match_quality','competitor_source','supplier_source','monthly_searches','cpc_local','assumed_cvr','merchant_count','dominant_merchant_share','creative_gap','title_gap','b2b_multiplier','bundle_multiplier','regulated_risk','fragility_risk','bulky_risk','expected_return_rate','estimated_delivery_days','has_local_payment','has_local_return_address','landed_cost_local','target_price_local','expected_units_per_order','notes']
rows=[]

def add(country,niche,name,price,slo,shi,moq,comp,supp,**kw):
    rows.append({
        'country':country,'niche':niche,'product_name':name,'competitor_price_local':price,
        'supplier_price_usd_low':slo,'supplier_price_usd_high':shi,'supplier_moq':moq,
        'match_quality':kw.pop('match_quality','category/near-match only'),'competitor_source':comp,'supplier_source':supp,
        'monthly_searches':kw.pop('monthly_searches',0),'cpc_local':kw.pop('cpc_local',0),'assumed_cvr':kw.pop('assumed_cvr',0.025),
        'merchant_count':kw.pop('merchant_count',8),'dominant_merchant_share':kw.pop('dominant_merchant_share',0.25),
        'creative_gap':kw.pop('creative_gap',0.55),'title_gap':kw.pop('title_gap',0.55),'b2b_multiplier':kw.pop('b2b_multiplier',0.6),
        'bundle_multiplier':kw.pop('bundle_multiplier',0.5),'regulated_risk':kw.pop('regulated_risk',0.35),'fragility_risk':kw.pop('fragility_risk',0.2),
        'bulky_risk':kw.pop('bulky_risk',0.05),'expected_return_rate':kw.pop('expected_return_rate',0.06),'estimated_delivery_days':kw.pop('estimated_delivery_days',6),
        'has_local_payment':kw.pop('has_local_payment',1),'has_local_return_address':kw.pop('has_local_return_address',0),
        'landed_cost_local':kw.pop('landed_cost_local'),'target_price_local':kw.pop('target_price_local',round(price*0.92,2)),
        'expected_units_per_order':kw.pop('expected_units_per_order',1.0),
        'notes':kw.pop('notes','Live competitor price + live supplier-category quote; landed cost/CPC/search volume are conservative scenario inputs, NOT verified quotes for an identical SKU.')
    })

DK_LAMP_COMP='https://bord-lampe.dk/genopladelig/'
NO_LAMP_COMP='https://www.prisjakt.no/s/oppladbar-bordlampe/'
LAMP_SUPP='https://www.alibaba.com/wholesale/cordless-table-lamps-rechargeable.html'
DK_HANDLE_COMP='https://www.kungreb.dk/da/kokkengreb/handtag-messing/'
NO_HANDLE_COMP='https://www.prisjakt.no/s/kjokken-handtak-borstet-messing/'
HANDLE_SUPP='https://www.alibaba.com/countrysearch/CN/brass-handles-kitchen.html'
DK_MENU_COMP1='https://www.grafical.dk/menuholder/'
DK_MENU_COMP2='https://displayshop.dk/shop/menu-info-holder-a6-53c1.html'
MENU_SUPP='https://www.alibaba.com/wholesale/acrylic-menu-stand.html'
NO_ACOUSTIC_COMP='https://www.prisjakt.no/s/akustikkpanel/'
ACOUSTIC_SUPP='https://www.alibaba.com/showroom/wood-slat-acoustic-wall-panels.html'

# Scenario keyword inputs are deliberately conservative placeholders so the software can be exercised offline.
for i,(n,p) in enumerate(DK_LAMPS):
    add('DK','rechargeable hospitality/table lighting',n,p,1.89,12.90,2,DK_LAMP_COMP,LAMP_SUPP,
        monthly_searches=500+100*i,cpc_local=3.2+0.08*i,assumed_cvr=0.026,b2b_multiplier=0.9,bundle_multiplier=0.85,
        regulated_risk=0.65,fragility_risk=0.2,landed_cost_local=55+4*i,estimated_delivery_days=6,expected_units_per_order=1.5,
        notes='Live DK retail observation and live Alibaba category quotes. Electrical/battery product: compliance pack is a hard gate. Search/CPC/landed cost are DEMO assumptions until imported from ad/supplier data.')
for i,(n,p) in enumerate(DK_HANDLES):
    add('DK','architectural/kitchen hardware',n,p,0.45,6.75,2,DK_HANDLE_COMP,HANDLE_SUPP,
        monthly_searches=350+80*i,cpc_local=2.1+0.1*i,assumed_cvr=0.03,b2b_multiplier=0.8,bundle_multiplier=1.0,
        regulated_risk=0.05,fragility_risk=0.02,landed_cost_local=12+3*i,estimated_delivery_days=5,expected_units_per_order=8,
        notes='Live DK handle price and live Alibaba brass-hardware category quotes. Exact material/finish must be matched manually. Search/CPC/landed cost are DEMO assumptions.')
for i,(n,p) in enumerate(DK_MENU):
    add('DK','restaurant/hospitality display hardware',n,p,0.36,7.0,1,DK_MENU_COMP1 if i<3 else DK_MENU_COMP2,MENU_SUPP,
        monthly_searches=120+50*i,cpc_local=1.8+0.15*i,assumed_cvr=0.028,b2b_multiplier=1.0,bundle_multiplier=0.95,
        regulated_risk=0.02,fragility_risk=0.1,landed_cost_local=10+10*i,estimated_delivery_days=5,expected_units_per_order=4,
        notes='Live Danish hospitality display price and live Alibaba menu-holder quotes. High multi-unit potential. Search/CPC/landed cost are DEMO assumptions.')

for i,(n,p) in enumerate(NO_LAMPS):
    add('NO','rechargeable hospitality/table lighting',n,p,1.89,12.90,2,NO_LAMP_COMP,LAMP_SUPP,
        monthly_searches=450+100*i,cpc_local=5.2+0.12*i,assumed_cvr=0.026,b2b_multiplier=0.9,bundle_multiplier=0.85,
        regulated_risk=0.65,fragility_risk=0.2,landed_cost_local=85+6*i,estimated_delivery_days=7,expected_units_per_order=1.5,
        notes='Live NO retail observation and live Alibaba category quotes. Electrical/battery product: compliance + VOEC/import treatment are hard gates. Search/CPC/landed cost are DEMO assumptions.')
for i,(n,p) in enumerate(NO_HANDLES):
    add('NO','architectural/kitchen hardware',n,p,0.45,6.75,2,NO_HANDLE_COMP,HANDLE_SUPP,
        monthly_searches=300+70*i,cpc_local=3.5+0.12*i,assumed_cvr=0.03,b2b_multiplier=0.8,bundle_multiplier=1.0,
        regulated_risk=0.05,fragility_risk=0.02,landed_cost_local=22+4*i,estimated_delivery_days=6,expected_units_per_order=8,
        notes='Live NO retail price and live Alibaba hardware category quotes. Exact material/finish/CC spacing must be matched manually. Search/CPC/landed cost are DEMO assumptions.')
for i,(n,p) in enumerate(NO_ACOUSTIC):
    add('NO','acoustic/slat wall panels',n,p,5.01,15.0,2,NO_ACOUSTIC_COMP,ACOUSTIC_SUPP,
        monthly_searches=700+150*i,cpc_local=6.0+0.2*i,assumed_cvr=0.024,b2b_multiplier=0.9,bundle_multiplier=0.9,
        regulated_risk=0.15,fragility_risk=0.15,bulky_risk=0.85,landed_cost_local=210+18*i,estimated_delivery_days=8,expected_units_per_order=3,
        notes='Live NO panel price and live Alibaba wood-slat acoustic-panel category quotes. Bulky freight is the core risk; EU/Nordic warehouse sourcing is preferable. Search/CPC/landed cost are DEMO assumptions.')

assert len(rows)==50, len(rows)
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
print(OUT, len(rows))
