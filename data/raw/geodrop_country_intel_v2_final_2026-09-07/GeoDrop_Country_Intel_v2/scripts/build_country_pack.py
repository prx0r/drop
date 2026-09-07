#!/usr/bin/env python3
import sys,zipfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
country=(ROOT/sys.argv[1]) if len(sys.argv)>1 else ROOT/'countries/no'
out=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT.parent/f'geodrop_country_{country.name.upper()}_v2.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(country.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(country.parent))
h=hashlib.sha256(out.read_bytes()).hexdigest(); out.with_suffix(out.suffix+'.sha256').write_text(f'{h}  {out.name}\n')
print(out); print(h)
