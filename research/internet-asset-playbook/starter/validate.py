import json
from pathlib import Path
from datetime import date
from urllib.parse import urlparse

DATA = Path(__file__).parent / 'data' / 'listings.json'
REQUIRED = {'id','name','category','region','summary','source_url','last_verified','is_sponsored'}


def valid_url(url):
    p=urlparse(url)
    return p.scheme in {'http','https'} and bool(p.netloc)


def validate(records, publishing=False):
    errors=[]
    seen=set()
    for i,r in enumerate(records,1):
        missing=REQUIRED-r.keys()
        if missing:
            errors.append(f'row {i}: missing {sorted(missing)}')
        rid=r.get('id')
        if rid in seen:
            errors.append(f'row {i}: duplicate id {rid}')
        seen.add(rid)
        if not valid_url(r.get('source_url','')):
            errors.append(f'row {i}: invalid source_url')
        try:
            date.fromisoformat(r.get('last_verified',''))
        except Exception:
            errors.append(f'row {i}: last_verified must be YYYY-MM-DD')
        if len(r.get('summary','').strip()) < 30:
            errors.append(f'row {i}: summary too thin (<30 chars)')
        if publishing and r.get('sample_only'):
            errors.append(f'row {i}: sample_only record cannot be published')
    return errors

if __name__=='__main__':
    records=json.loads(DATA.read_text())
    errors=validate(records)
    if errors:
        print('\n'.join('ERROR: '+e for e in errors))
        raise SystemExit(1)
    print(f'OK: {len(records)} records passed validation (preview mode).')
