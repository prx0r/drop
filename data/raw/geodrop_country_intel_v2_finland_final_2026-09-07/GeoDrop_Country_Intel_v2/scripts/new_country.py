#!/usr/bin/env python3
import shutil,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)<3: raise SystemExit('usage: new_country.py CC "Country Name" [as_of]')
cc=sys.argv[1].upper(); name=sys.argv[2]; asof=sys.argv[3] if len(sys.argv)>3 else None
dst=ROOT/'countries'/cc.lower()
if dst.exists(): raise SystemExit(f'{dst} exists')
shutil.copytree(ROOT/'templates/country',dst)
for f in ['manifest.json','profile.json']:
 p=dst/f; o=json.loads(p.read_text()); o['country']=cc; o['country_name']=name
 if 'as_of' in o:o['as_of']=asof
 p.write_text(json.dumps(o,indent=2)+'\n')
for p in (dst/'reports').glob('*.json'):
 o=json.loads(p.read_text()); o['country']=cc; o['as_of']=asof; p.write_text(json.dumps(o,indent=2)+'\n')
print(dst)
