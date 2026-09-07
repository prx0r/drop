import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from pathlib import Path
from geocommerce.services.storefront import render_product
import argparse

ap=argparse.ArgumentParser(description='Compile one localized premium product storefront to static HTML.')
ap.add_argument('market', help='Market code, e.g. FI')
ap.add_argument('product', help='Canonical product slug')
ap.add_argument('--out',default='output/product.html',help='Output HTML file or directory')
a=ap.parse_args()

out=Path(a.out)
# Ergonomic behavior: a directory (existing or suffix-less) gets a deterministic filename.
if out.is_dir() or not out.suffix:
    out = out / f'{a.product}-{a.market.lower()}.html'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(render_product(a.product,a.market.upper()), encoding='utf-8')
print(out)
