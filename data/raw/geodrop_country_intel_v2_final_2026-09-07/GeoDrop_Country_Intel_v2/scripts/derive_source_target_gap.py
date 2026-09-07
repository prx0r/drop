#!/usr/bin/env python3
import json,sys
def ratio(a,b): return None if a is None or b in (None,0) else a/b
x=json.load(open(sys.argv[1]))
s=x.get('source',{});t=x.get('target',{})
out={'assortment_gap_ratio':ratio(s.get('relevant_skus'),t.get('relevant_skus')),'merchant_gap_ratio':ratio(s.get('good_merchants'),t.get('good_merchants')),'decision_asset_gap':None if s.get('decision_assets') is None or t.get('decision_assets') is None else s['decision_assets']-t['decision_assets']}
print(json.dumps(out,indent=2))
