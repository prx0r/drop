"""
Candidate Data Model — Pydantic model for PRODUCT × COUNTRY × SUPPLIER × QUERY × SKU
Every estimate stores: value, source, timestamp, confidence, sample_size
"""

from __future__ import annotations
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class ConfidenceLevel(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"


class HardGateStatus(str, Enum):
    PASS = "PASS"
    QUARANTINE = "QUARANTINE"
    REJECT = "REJECT"
    UNKNOWN = "UNKNOWN"


class RecommendedAction(str, Enum):
    LAUNCH = "LAUNCH"
    FREE_TEST = "FREE_TEST"
    PAID_TEST = "PAID_TEST"
    RESEARCH_MORE = "RESEARCH_MORE"
    WAIT = "WAIT"
    FIX = "FIX"
    KILL = "KILL"
    SCALE = "SCALE"


class TestType(str, Enum):
    CHECK_SERP = "CHECK_SERP"
    CHECK_SUPPLIER = "CHECK_SUPPLIER"
    GET_SHIPPING_QUOTE = "GET_SHIPPING_QUOTE"
    FETCH_KEYWORD_DATA = "FETCH_KEYWORD_DATA"
    FETCH_GTIN_SELLERS = "FETCH_GTIN_SELLERS"
    ENABLE_FREE_LISTING = "ENABLE_FREE_LISTING"
    RUN_FREE_TRAFFIC_TEST = "RUN_FREE_TRAFFIC_TEST"
    RUN_5_PAID_TEST = "RUN_$5_PAID_TEST"
    RUN_10_PAID_TEST = "RUN_$10_PAID_TEST"


class CandidateState(str, Enum):
    DISCOVERED = "DISCOVERED"
    RESEARCHING = "RESEARCHING"
    HARD_REJECTED = "HARD_REJECTED"
    SUPPLIER_VALIDATED = "SUPPLIER_VALIDATED"
    BUILD_READY = "BUILD_READY"
    FREE_LISTINGS_LIVE = "FREE_LISTINGS_LIVE"
    FREE_SIGNAL_WEAK = "FREE_SIGNAL_WEAK"
    FREE_SIGNAL_POSITIVE = "FREE_SIGNAL_POSITIVE"
    PAID_TEST_READY = "PAID_TEST_READY"
    PAID_TESTING = "PAID_TESTING"
    PAUSED = "PAUSED"
    FIXING = "FIXING"
    PROFITABLE_SPARSE = "PROFITABLE_SPARSE"
    PROFITABLE_SCALABLE = "PROFITABLE_SCALABLE"
    KILLED = "KILLED"


class EvidenceField(BaseModel):
    """A value with full provenance tracking."""
    value: float = 0.0
    source: str = ""
    timestamp: str = ""
    confidence: ConfidenceLevel = ConfidenceLevel.LOW
    sample_size: int = 0


class Candidate(BaseModel):
    """Full candidate model — the atomic unit of evaluation."""
    # Identity
    candidate_id: str = ""
    product_family: str = ""
    sku: str = ""
    gtin: str = ""
    mpn: str = ""
    brand: str = ""
    country: str = "US"
    currency: str = "USD"
    supplier_id: str = ""
    query: str = ""

    # Price / economics
    selling_price: float = 0.0
    supplier_price: float = 0.0
    supplier_shipping: float = 0.0
    duties: float = 0.0
    payment_fee_rate: float = 0.029
    expected_returns_cost: float = 0.0
    pre_ad_contribution: float = 0.0

    # Traffic
    expected_cpc: float = 0.0
    cpc_source: str = ""
    cpc_confidence: ConfidenceLevel = ConfidenceLevel.LOW

    # CVR scenarios
    cvr_pessimistic: float = 0.002
    cvr_base: float = 0.005
    cvr_optimistic: float = 0.01

    # Break-even
    break_even_cvr: float = 0.0
    headroom_pessimistic: float = 0.0
    headroom_base: float = 0.0
    headroom_optimistic: float = 0.0

    # Demand
    monthly_search_volume: int = 0
    trend_3m: float = 0.0  # -1.0 to +1.0
    trend_yoy: float = 0.0
    exact_query_share: float = 0.0
    intent_score: float = 0.0

    # Competition
    shopping_seller_count: int = 0
    amazon_presence: bool = False
    manufacturer_dtc: bool = False
    price_percentile: float = 0.5
    shipping_days: int = 0
    shipping_gap_vs_market: int = 0

    # Supplier
    supplier_selectivity: str = ""  # open, selective, restricted
    supplier_reliability: float = 0.0  # 0-1

    # Differentiation
    merchant_differentiation_score: float = 0.0

    # Scoring
    raw_score: float = 0.0
    confidence_score: float = 0.0
    adjusted_score: float = 0.0

    # Hard gates
    hard_gate_status: HardGateStatus = HardGateStatus.UNKNOWN
    hard_gate_reasons: List[str] = Field(default_factory=list)

    # Decision
    recommended_action: RecommendedAction = RecommendedAction.WAIT
    recommended_next_test: TestType = TestType.CHECK_SERP
    estimated_test_cost: float = 0.0

    # Bayesian evidence (updated as tests run)
    observed_clicks: int = 0
    observed_orders: int = 0
    posterior_alpha: float = 1.0
    posterior_beta: float = 1.0
    posterior_mean_cvr: float = 0.0
    credible_interval_low: float = 0.0
    credible_interval_high: float = 0.0
    probability_cvr_above_break_even: float = 0.0

    # Confidence fields for each domain
    economics_confidence: ConfidenceLevel = ConfidenceLevel.LOW
    cpc_confidence_domain: ConfidenceLevel = ConfidenceLevel.LOW
    cvr_confidence: ConfidenceLevel = ConfidenceLevel.LOW
    supplier_confidence: ConfidenceLevel = ConfidenceLevel.LOW
    competition_confidence: ConfidenceLevel = ConfidenceLevel.LOW
    demand_confidence: ConfidenceLevel = ConfidenceLevel.LOW

    # State machine
    state: CandidateState = CandidateState.DISCOVERED
    state_history: List[dict] = Field(default_factory=list)

    # Metadata
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> dict:
        return self.model_dump()
