from __future__ import annotations

import json
from typing import Callable

from .catalog import get_product
from .markets import get_market
from .signals import latest_signal

Translator = Callable[[str, str], str]


def _humanize(key: str) -> str:
    return key.replace("_", " ").strip()


def source_copy(product: dict, market_code: str) -> dict:
    """Build a fact-bounded source manifest before any translation occurs."""
    market = get_market(market_code)
    facts = product["facts"]
    signal = None
    try:
        signal = latest_signal(product["slug"], market.code)
    except KeyError:
        pass

    verified_features = []
    for key, value in facts.get("features", {}).items():
        if isinstance(value, bool):
            if value:
                verified_features.append(_humanize(key))
        elif value not in (None, "", [], {}):
            verified_features.append(f"{_humanize(key)}: {value}")

    bullets = []
    bullets.extend([f"Material: {x}" for x in facts.get("materials", [])[:3]])
    bullets.extend(verified_features[:5])
    if facts.get("warranty_months"):
        bullets.append(f"Warranty: {facts['warranty_months']} months")

    return {
        "slug": product["slug"],
        "source_language": "English",
        "target_language": market.language_name,
        "market": market.code,
        "name": product["name"],
        "category": product["category"],
        "bullets": bullets,
        "verified_facts": {
            "materials": facts.get("materials", []),
            "dimensions": facts.get("dimensions", {}),
            "features": facts.get("features", {}),
            "certifications": facts.get("certifications", []),
            "warranty_months": facts.get("warranty_months"),
            "country_of_origin": facts.get("country_of_origin"),
            "gtin": facts.get("gtin"),
        },
        "local_context": {
            "currency": market.currency,
            "checkout_methods": market.checkout_methods,
            "preferred_delivery": market.preferred_delivery,
            "query": signal.query if signal else None,
        },
    }


def compile_localized_manifest(product_slug: str, market_code: str, translator: Translator | None = None) -> dict:
    product = get_product(product_slug)
    manifest = source_copy(product, market_code.upper())
    if translator is None:
        manifest["translation_status"] = "source_only"
        return manifest

    target = manifest["target_language"]
    # Translate only already-verified customer-facing strings, never the facts object itself.
    manifest["localized_name"] = translator(manifest["name"], target)
    manifest["localized_bullets"] = [translator(x, target) for x in manifest["bullets"]]
    manifest["translation_status"] = "translated_fact_bounded"
    return manifest


def llm_translator(adapter) -> Translator:
    def translate(text: str, target_language: str) -> str:
        system = (
            "You are a literal ecommerce localization translator. Translate only the supplied text. "
            "Do not add, infer, embellish, or change product claims, measurements, certifications, warranty, or use cases. "
            "Return only the translated text."
        )
        return adapter.complete(system=system, user=f"Target language: {target_language}\nText: {json.dumps(text, ensure_ascii=False)}")
    return translate
