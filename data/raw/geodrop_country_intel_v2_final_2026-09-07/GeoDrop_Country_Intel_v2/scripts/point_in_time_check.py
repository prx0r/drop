#!/usr/bin/env python3
import json,sys,datetime
from pathlib import Path
country=Path(sys.argv[1]); as_of=sys.argv[2]
def dateval(x):
 if not x:return None
 return x[:10]
errs=[]
for file,idkey in [('observations.jsonl','observation_id'),('raw_snapshot_manifest.jsonl','snapshot_id')]:
 for line in (country/file).read_text().splitlines():
  if not line.strip():continue
  r=json.loads(line); av=dateval(r.get('available_at'))
  if av is None: errs.append({'id':r.get(idkey),'reason':'unknown_available_at'})
  elif av>as_of[:10]: errs.append({'id':r.get(idkey),'reason':'future_evidence','available_at':av})
print(json.dumps({'as_of':as_of,'point_in_time_safe':not errs,'violations':errs},indent=2))
sys.exit(1 if errs else 0)
