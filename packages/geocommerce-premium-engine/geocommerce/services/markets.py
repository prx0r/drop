from __future__ import annotations
import json
from pathlib import Path
from ..models import MarketConfig
ROOT=Path(__file__).resolve().parents[2]
MARKET_FILE=ROOT/'config'/'markets.json'

def load_markets() -> dict[str, MarketConfig]:
    data=json.loads(MARKET_FILE.read_text())
    return {row['code']:MarketConfig(**row) for row in data}

def get_market(code:str)->MarketConfig:
    markets=load_markets()
    code=code.upper()
    if code not in markets: raise KeyError(f'unknown market {code}')
    return markets[code]
