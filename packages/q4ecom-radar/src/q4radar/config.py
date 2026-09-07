from __future__ import annotations

from pathlib import Path
import yaml
from .models import Market, ProductSeed


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_markets(config_dir: str | Path = "config") -> dict[str, Market]:
    raw = _load_yaml(Path(config_dir) / "markets.yml").get("markets", {})
    return {code: Market(code=code, **data) for code, data in raw.items()}


def load_products(config_dir: str | Path = "config") -> dict[str, ProductSeed]:
    raw = _load_yaml(Path(config_dir) / "products.yml").get("products", [])
    return {item["slug"]: ProductSeed(**item) for item in raw}


def load_scoring(config_dir: str | Path = "config") -> dict:
    return _load_yaml(Path(config_dir) / "scoring.yml")
