import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from geocommerce.services.opportunities import evaluate,leaderboard
pairs=[('barista-dual-boiler-espresso','FI'),('barista-dual-boiler-espresso','NO'),('premium-pet-ramp-oak','FI'),('ergonomic-standing-desk-frame','BE')]
for p,m in pairs:
    print(evaluate(p,m).model_dump_json(indent=2))
print('\nLEADERBOARD')
for r in leaderboard(): print(r['score'],r['verdict'],r['product_slug'],r['market_code'])
