#!/usr/bin/env python3
"""Minimal evaluator for frozen prediction/outcome JSONL. Production analysis can extend this without changing country evidence."""
import json,sys,statistics
pred=[json.loads(x) for x in open(sys.argv[1]) if x.strip()]; out={x['candidate_id']:x for x in (json.loads(y) for y in open(sys.argv[2]) if y.strip())}
rows=[(p,out.get(p['candidate_id'])) for p in pred if p['candidate_id'] in out]; rows.sort(key=lambda x:x[0].get('score',0),reverse=True)
for k in [1,3,5,10]:
 top=rows[:min(k,len(rows))]; hit=sum(bool(o.get('validated')) for _,o in top); print(f'precision@{k}={hit/len(top):.3f}' if top else f'precision@{k}=NA')
contrib=[o.get('realized_contribution') for _,o in rows if isinstance(o.get('realized_contribution'),(int,float))]
print('median_realized_contribution=',statistics.median(contrib) if contrib else 'NA')
