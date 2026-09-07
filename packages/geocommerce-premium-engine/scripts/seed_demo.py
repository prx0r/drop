from __future__ import annotations
import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
import json
from pathlib import Path
from geocommerce.db import init_db
from geocommerce.models import ProductCreate,MarketSignal,SupplierOffer
from geocommerce.services.catalog import upsert_product
from geocommerce.services.signals import save_signal,save_offer
ROOT=Path(__file__).resolve().parents[1]
init_db()
for row in json.loads((ROOT/'data/demo_catalog.json').read_text()): upsert_product(ProductCreate(**row))
for row in json.loads((ROOT/'data/demo_signals.json').read_text()): save_signal(MarketSignal(**row))
for row in json.loads((ROOT/'data/demo_offers.json').read_text()): save_offer(SupplierOffer(**row))
print('demo seeded')
