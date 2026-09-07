from __future__ import annotations
from .catalog import get_product

def build_media_brief(product_slug:str,market_code:str)->dict:
    p=get_product(product_slug); facts=p['facts']
    truthful=', '.join([p['name'],*facts.get('materials',[]),*facts.get('features',{}).keys()])
    return {
      'product_slug':product_slug,'market_code':market_code,'reference_images':p['images'][:3],
      'shots':[
        {'name':'hero_orbit','purpose':'premium PDP hero','prompt':f"Slow cinematic orbit around {truthful}; preserve exact product geometry, materials and controls; clean premium studio; no invented logos or features."},
        {'name':'use_case','purpose':'show scale and use','prompt':f"Show {p['name']} naturally in a high-end home environment; preserve exact product design; demonstrate only verified features."},
        {'name':'detail_macro','purpose':'trust and craftsmanship','prompt':f"Macro product-detail video emphasizing verified materials and controls of {p['name']}; no text hallucinations."}
      ],
      'qa_rules':['Product geometry must match references','No invented certifications','No altered controls/connectors','No fake customer testimonials','Human approve before paid media']
    }
