"""
Hard Gates — Binary rejection before soft scoring.
Gate 1-7: Each gate is independent. Any REJECT kills the candidate for that path.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple
from packages.schemas.candidate import Candidate, HardGateStatus


@dataclass
class GateResult:
    """Result of a single gate evaluation."""
    gate_id: int
    gate_name: str
    passed: bool
    status: HardGateStatus  # PASS, QUARANTINE, REJECT
    reason: str = ""
    details: dict = field(default_factory=dict)


def gate_1_positive_economics(c: Candidate) -> GateResult:
    """Gate 1: Positive unit economics. pre_ad_contribution <= 0 → reject."""
    passed = c.pre_ad_contribution > 0
    status = HardGateStatus.PASS if passed else HardGateStatus.REJECT
    reason = "" if passed else f"Pre-ad contribution is ${c.pre_ad_contribution:.2f} (<=0). No scenario produces profit."
    return GateResult(1, "Positive Economics", passed, status, reason,
                      {"pre_ad_contribution": c.pre_ad_contribution})


def gate_2_plausible_paid_economics(c: Candidate) -> GateResult:
    """Gate 2: Plausible paid economics.
    headroom_optimistic < 1.0 → reject paid
    headroom_base < 1.2 → quarantine (needs free traffic first)
    """
    if c.headroom_optimistic < 1.0:
        return GateResult(2, "Plausible Paid Economics", False, HardGateStatus.REJECT,
                          f"Optimistic headroom {c.headroom_optimistic:.2f} < 1.0. "
                          f"Even best-case scenario loses money on paid traffic.",
                          {"headroom_optimistic": c.headroom_optimistic})
    if c.headroom_base < 1.2:
        return GateResult(2, "Plausible Paid Economics", False, HardGateStatus.QUARANTINE,
                          f"Base headroom {c.headroom_base:.2f} < 1.2. "
                          f"Can only test with free traffic. Not ready for paid.",
                          {"headroom_base": c.headroom_base})
    return GateResult(2, "Plausible Paid Economics", True, HardGateStatus.PASS, "",
                      {"headroom_base": c.headroom_base, "headroom_optimistic": c.headroom_optimistic})


def gate_3_shipping_offer(c: Candidate) -> GateResult:
    """Gate 3: Shipping/offer competitiveness.
    - Shipping > 14 days on pain/urgency products → quarantine
    - Shipping > 21 days → reject
    """
    if c.shipping_days > 21:
        return GateResult(3, "Shipping Competitiveness", False, HardGateStatus.REJECT,
                          f"Shipping {c.shipping_days} days exceeds 21-day threshold.",
                          {"shipping_days": c.shipping_days})
    if c.shipping_gap_vs_market > 10:
        return GateResult(3, "Shipping Competitiveness", False, HardGateStatus.QUARANTINE,
                          f"Shipping gap {c.shipping_gap_vs_market} days vs market average. "
                          f"Competitors ship faster.",
                          {"shipping_gap_vs_market": c.shipping_gap_vs_market})
    return GateResult(3, "Shipping Competitiveness", True, HardGateStatus.PASS, "",
                      {"shipping_days": c.shipping_days})


def gate_4_sku_saturation(c: Candidate) -> GateResult:
    """Gate 4: Exact SKU saturation.
    GTIN seller count > 20 → reject
    Amazon presence + many sellers → quarantine
    """
    if c.shopping_seller_count > 20:
        return GateResult(4, "SKU Saturation", False, HardGateStatus.REJECT,
                          f"{c.shopping_seller_count} sellers for this GTIN. SKU is saturated.",
                          {"shopping_seller_count": c.shopping_seller_count})
    if c.amazon_presence and c.shopping_seller_count > 10:
        return GateResult(4, "SKU Saturation", False, HardGateStatus.QUARANTINE,
                          f"Amazon present + {c.shopping_seller_count} sellers. "
                          f"Price compression likely.",
                          {"amazon_presence": c.amazon_presence,
                           "shopping_seller_count": c.shopping_seller_count})
    return GateResult(4, "SKU Saturation", True, HardGateStatus.PASS, "",
                      {"shopping_seller_count": c.shopping_seller_count,
                       "amazon_presence": c.amazon_presence})


def gate_5_supplier_viability(c: Candidate) -> GateResult:
    """Gate 5: Supplier viability.
    reliability < 0.3 → reject
    reliability < 0.5 → quarantine
    """
    if c.supplier_reliability < 0.3:
        return GateResult(5, "Supplier Viability", False, HardGateStatus.REJECT,
                          f"Supplier reliability {c.supplier_reliability:.2f} < 0.3. Too risky.",
                          {"supplier_reliability": c.supplier_reliability})
    if c.supplier_reliability < 0.5:
        return GateResult(5, "Supplier Viability", False, HardGateStatus.QUARANTINE,
                          f"Supplier reliability {c.supplier_reliability:.2f} < 0.5. Needs validation.",
                          {"supplier_reliability": c.supplier_reliability})
    return GateResult(5, "Supplier Viability", True, HardGateStatus.PASS, "",
                      {"supplier_reliability": c.supplier_reliability})


def gate_6_query_intent(c: Candidate) -> GateResult:
    """Gate 6: Query purchase intent.
    INFORMATIONAL queries → quarantine
    IRRELEVANT → reject
    """
    if c.intent_score <= 0.1:
        return GateResult(6, "Query Purchase Intent", False, HardGateStatus.REJECT,
                          f"Intent score {c.intent_score:.2f} ≤ 0.1. Query shows no purchase intent.",
                          {"intent_score": c.intent_score})
    if c.intent_score < 0.4:
        return GateResult(6, "Query Purchase Intent", False, HardGateStatus.QUARANTINE,
                          f"Intent score {c.intent_score:.2f} < 0.4. Low purchase intent.",
                          {"intent_score": c.intent_score})
    return GateResult(6, "Query Purchase Intent", True, HardGateStatus.PASS, "",
                      {"intent_score": c.intent_score})


def gate_7_data_confidence(c: Candidate) -> GateResult:
    """Gate 7: Data confidence.
    If all key inputs are guessed (VERY_LOW confidence), trigger RESEARCH_MORE not LAUNCH.
    """
    very_low_count = sum(1 for conf in [
        c.economics_confidence,
        c.cpc_confidence_domain,
        c.cvr_confidence,
        c.supplier_confidence,
        c.competition_confidence,
        c.demand_confidence,
    ] if conf.value == "VERY_LOW")

    if very_low_count >= 4:
        return GateResult(7, "Data Confidence", False, HardGateStatus.QUARANTINE,
                          f"{very_low_count}/6 confidence fields are VERY_LOW. Need more research.",
                          {"very_low_count": very_low_count})
    return GateResult(7, "Data Confidence", True, HardGateStatus.PASS, "",
                      {"very_low_fields": very_low_count})


ALL_GATES = [
    gate_1_positive_economics,
    gate_2_plausible_paid_economics,
    gate_3_shipping_offer,
    gate_4_sku_saturation,
    gate_5_supplier_viability,
    gate_6_query_intent,
    gate_7_data_confidence,
]


@dataclass
class GateReport:
    """Aggregate result of all gates."""
    results: List[GateResult] = field(default_factory=list)
    overall_status: HardGateStatus = HardGateStatus.PASS
    reject_reasons: List[str] = field(default_factory=list)
    quarantine_reasons: List[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return self.overall_status == HardGateStatus.PASS

    @property
    def quarantined(self) -> bool:
        return self.overall_status == HardGateStatus.QUARANTINE


def run_all_gates(c: Candidate) -> GateReport:
    """Run all 7 hard gates on a candidate. Returns aggregate report."""
    report = GateReport()

    for gate_fn in ALL_GATES:
        result = gate_fn(c)
        report.results.append(result)

        if result.status == HardGateStatus.REJECT:
            report.overall_status = HardGateStatus.REJECT
            report.reject_reasons.append(f"Gate {result.gate_id}: {result.reason}")
        elif result.status == HardGateStatus.QUARANTINE:
            if report.overall_status != HardGateStatus.REJECT:
                report.overall_status = HardGateStatus.QUARANTINE
            report.quarantine_reasons.append(f"Gate {result.gate_id}: {result.reason}")

    return report
