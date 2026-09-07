from __future__ import annotations
from pathlib import Path
import yaml
from .models import Opportunity, Evidence

def load_yaml(path: str | Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_opportunities(config_dir: str | Path) -> dict[str, Opportunity]:
    raw = load_yaml(Path(config_dir)/"opportunities.yml")
    items = [Opportunity(**x) for x in raw["opportunities"]]
    return {x.slug: x for x in items}

def load_scoring(config_dir: str | Path) -> dict:
    return load_yaml(Path(config_dir)/"scoring.yml")

def load_evidence(path: str | Path) -> dict[str, Evidence]:
    raw = load_yaml(path)
    return {k: Evidence(**v) for k,v in raw["evidence"].items()}
