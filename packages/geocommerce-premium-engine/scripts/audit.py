from __future__ import annotations
import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
import ast,compileall,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
if not compileall.compile_dir(ROOT/'geocommerce',quiet=1): errors.append('compileall failed')
for p in (ROOT/'geocommerce').rglob('*.py'):
    txt=p.read_text()
    if 'api_key="' in txt.lower() or 'access_token="' in txt.lower(): errors.append(f'possible hardcoded secret {p}')
    try: ast.parse(txt)
    except SyntaxError as e: errors.append(f'syntax {p}:{e}')
# Ensure market config parses and currencies exist
markets=json.loads((ROOT/'config/markets.json').read_text())
for m in markets:
    for k in ['code','currency','google_geo_id','google_language_id','checkout_methods']:
        if not m.get(k): errors.append(f'market {m.get("code")} missing {k}')
print(json.dumps({'ok':not errors,'errors':errors,'market_count':len(markets)},indent=2))
sys.exit(1 if errors else 0)
