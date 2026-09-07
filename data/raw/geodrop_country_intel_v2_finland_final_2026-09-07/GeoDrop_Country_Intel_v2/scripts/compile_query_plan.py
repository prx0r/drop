#!/usr/bin/env python3
import json,sys
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'countries/no'
rows=[json.loads(x) for x in (p/'queries.jsonl').read_text().splitlines() if x.strip()]
plan={}
for r in rows: plan.setdefault((r['language'],r['ecosystem_id']),[]).append(r['native_phrase'])
print(json.dumps([{'language':k[0],'ecosystem_id':k[1],'queries':v} for k,v in plan.items()],ensure_ascii=False,indent=2))
