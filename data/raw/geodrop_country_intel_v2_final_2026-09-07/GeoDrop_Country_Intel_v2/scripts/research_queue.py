#!/usr/bin/env python3
import json,sys
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'countries/no'
q=[]
for line in (p/'ecosystems.jsonl').read_text().splitlines():
 if not line.strip():continue
 e=json.loads(line); c=e.get('discovery_components',{})
 for k,v in c.items():
  if v is None:q.append({'priority':'DISCOVERY_REQUIRED','ecosystem_id':e['ecosystem_id'],'missing_component':k,'next_action':e.get('next_action')})
for line in (p/'product_markets.jsonl').read_text().splitlines():
 if not line.strip():continue
 x=json.loads(line)
 for g,v in x.get('hard_gates',{}).items():
  if v is not True:q.append({'priority':'LAUNCH_GATE','product_market_id':x['product_market_id'],'gate':g,'state':x.get('state')})
print(json.dumps(q,indent=2))
