#!/usr/bin/env python3
import json,sys
W={'installed_base_magnitude':20,'growth_replacement_pressure':15,'problem_incidence_urgency':15,'native_search_demand':15,'target_merchant_service_lag':15,'source_market_proof':10,'localization_geographic_edge':10}
obj=json.loads(open(sys.argv[1]).read()) if len(sys.argv)>1 else json.load(sys.stdin)
c=obj.get('discovery_components',obj)
for k,v in c.items():
 if k in W and v is not None and not(0<=v<=W[k]): raise SystemExit(f'{k} out of range 0..{W[k]}')
avail=sum(W[k] for k,v in c.items() if k in W and v is not None); score=sum(v for k,v in c.items() if k in W and v is not None)
print(json.dumps({'measured_points':score,'max_measured_points':avail,'evidence_coverage':avail/100,'normalized_measured_score':score/avail*100 if avail else None,'promotion_eligible':avail>=75 and all(c.get(k) is not None for k in ['native_search_demand','target_merchant_service_lag','source_market_proof'])},indent=2))
