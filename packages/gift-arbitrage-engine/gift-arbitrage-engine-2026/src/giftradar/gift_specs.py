from __future__ import annotations
from .models import Opportunity, GiftSpecRequest, GiftSpec

ARCHETYPE_STEPS = {
    "memory_to_artifact": [
        "ingest customer-authorized photos/text/audio", "deduplicate and quality-rank inputs",
        "cluster by people/events/time", "generate a structured narrative/layout",
        "render a preview with editable captions", "run factual/name/date checks", "export print-ready assets"
    ],
    "profile_to_report": [
        "collect minimum structured profile inputs", "compute deterministic source data before using an LLM",
        "generate interpretation from the computed structure", "label entertainment/interpretive material clearly",
        "render premium digital and/or book layout", "run consistency and unsupported-claim checks"
    ],
    "people_to_game": [
        "collect names, facts, photos and inside jokes", "generate clue/question candidates",
        "remove sensitive or embarrassing content", "balance difficulty and duplicates",
        "render cards/board/puzzle", "preview and approve", "export production assets"
    ],
    "data_to_keepsake": [
        "collect date/place/name or handwriting/audio input", "validate/transcribe/normalize source data",
        "create visual transformation", "show buyer preview", "preserve original source as optional inset/QR",
        "export production assets"
    ],
    "occasion_bundle": [
        "collect guest/recipient list", "collect optional facts, photos and tone",
        "generate coordinated variable-data components", "flag unsafe/awkward jokes",
        "render whole-event preview", "batch-export print assets by guest/order"
    ],
}

def build_spec(o: Opportunity, req: GiftSpecRequest) -> GiftSpec:
    steps = ARCHETYPE_STEPS.get(o.archetype, ARCHETYPE_STEPS["memory_to_artifact"])
    required = o.personalization_inputs[:2] if len(o.personalization_inputs) >= 2 else o.personalization_inputs
    optional = [x for x in o.personalization_inputs if x not in required]
    return GiftSpec(
        opportunity_slug=o.slug,
        product_title=f"{o.name} — production blueprint",
        required_inputs=required,
        optional_inputs=optional,
        generation_steps=steps,
        human_review_checks=[
            "spelling of all names, dates and addresses", "copyright/IP ownership of uploaded media",
            "no invented biographical facts", "no unsafe medical/financial/legal claims",
            "no private/sensitive information exposed without consent", "print bleed, crop, resolution and QR scanability"
        ],
        fulfillment_assets=["customer preview PDF/JPG", "print-ready PDF(s)", "order manifest JSON", "thumbnail/mockup assets"],
        privacy_notes=[
            "collect the minimum data needed", "do not use customer uploads to train models without explicit permission",
            "use expiring/private object-storage URLs for production assets", "provide deletion/export controls",
            "treat child data, exact birth data, addresses and voice recordings as higher-sensitivity inputs"
        ]
    )
