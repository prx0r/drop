from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class SupplierAuditInput:
    authorized_reseller_path: bool = False
    eu_or_local_warehouse: bool = False
    tracked_shipping: bool = False
    shipping_days: int = 30
    warranty_months: int = 0
    local_return_address: bool = False
    live_stock_signal: bool = False
    gtin_or_mpn_present: bool = False
    complete_spec_sheet: bool = False
    sample_order_passed: bool = False
    replacement_parts: bool = False
    support_contact: bool = False


def audit_supplier(inp: SupplierAuditInput) -> dict:
    """Score whether a supplier is suitable for a premium consultant storefront.

    This is intentionally stricter than a typical dropshipping supplier check. A premium
    promise requires traceable identity, warranty, returns, product truth, and sample QA.
    """
    components = {
        "authorization": 15 if inp.authorized_reseller_path else 0,
        "warehouse": 12 if inp.eu_or_local_warehouse else 0,
        "tracked_shipping": 6 if inp.tracked_shipping else 0,
        "delivery": 12 if inp.shipping_days <= 7 else 8 if inp.shipping_days <= 12 else 3 if inp.shipping_days <= 21 else 0,
        "warranty": 10 if inp.warranty_months >= 24 else 6 if inp.warranty_months >= 12 else 0,
        "returns": 8 if inp.local_return_address else 0,
        "inventory": 6 if inp.live_stock_signal else 0,
        "identity": 6 if inp.gtin_or_mpn_present else 0,
        "spec_truth": 8 if inp.complete_spec_sheet else 0,
        "sample": 8 if inp.sample_order_passed else 0,
        "parts": 5 if inp.replacement_parts else 0,
        "support": 4 if inp.support_contact else 0,
    }
    score = sum(components.values())
    gates = []
    if not inp.complete_spec_sheet:
        gates.append("missing_product_truth")
    if inp.shipping_days > 21:
        gates.append("delivery_too_slow")
    if inp.warranty_months < 12:
        gates.append("weak_warranty")
    if not inp.sample_order_passed:
        gates.append("sample_not_verified")
    if not inp.gtin_or_mpn_present:
        gates.append("weak_product_identity")

    stage = "REJECT" if any(x in gates for x in ("missing_product_truth", "delivery_too_slow", "weak_warranty")) else "SAMPLE" if "sample_not_verified" in gates else "APPROVE" if score >= 72 else "WATCH"
    return {"score": score, "stage": stage, "gates": gates, "components": components, "input": asdict(inp)}
