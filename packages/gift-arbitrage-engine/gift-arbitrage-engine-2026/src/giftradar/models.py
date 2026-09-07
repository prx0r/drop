from __future__ import annotations
from typing import Literal, Any
from pydantic import BaseModel, Field

class Evidence(BaseModel):
    source: str
    source_type: Literal["official", "marketplace", "trend", "provider", "community", "estimate"]
    metric: str
    value: str
    url: str | None = None
    confidence: float = Field(default=0.7, ge=0, le=1)
    observed_at: str | None = None

class Opportunity(BaseModel):
    slug: str
    name: str
    archetype: str
    description: str
    primary_marketplaces: list[str]
    q4_window: str
    target_price_usd: tuple[float, float]
    target_cogs_usd: tuple[float, float]
    personalization_inputs: list[str]
    output_formats: list[str]
    evidence_keys: list[str]
    metrics: dict[str, float]
    risks: list[str] = []
    moat: str = ""
    first_test: str = ""

class Score(BaseModel):
    slug: str
    name: str
    total: float
    verdict: str
    components: dict[str, float]
    penalties: dict[str, float]
    price_mid: float
    cogs_mid: float
    gross_margin_pct: float
    evidence_count: int
    reasons: list[str]
    risks: list[str]

class GiftSpecRequest(BaseModel):
    opportunity_slug: str
    recipient: str | None = None
    occasion: str | None = None
    inputs: dict[str, Any] = {}
    tone: str = "warm"
    locale: str = "en-GB"

class GiftSpec(BaseModel):
    opportunity_slug: str
    product_title: str
    required_inputs: list[str]
    optional_inputs: list[str]
    generation_steps: list[str]
    human_review_checks: list[str]
    fulfillment_assets: list[str]
    privacy_notes: list[str]
