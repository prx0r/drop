from __future__ import annotations

from .models import Candidate


HIGH_RISK_TERMS = {
    "mains lamp", "ceiling lamp", "power supply", "heater", "baby", "cosmetic",
    "supplement", "medical", "charger", "battery pack", "food contact",
}


def compliance_flags(candidate: Candidate) -> list[str]:
    text = f"{candidate.niche} {candidate.product_name} {candidate.notes}".lower()
    flags: list[str] = []
    for term in sorted(HIGH_RISK_TERMS):
        if term in text:
            flags.append(f"manual compliance review: {term}")
    if candidate.regulated_risk >= 0.75:
        flags.append("high regulated_risk score")
    if "lamp" in text or "led" in text:
        flags.append("verify electrical/battery conformity, declarations, labelling and importer obligations")
    if candidate.country == "NO":
        flags.append("verify VOEC eligibility/treatment and disclose seller/shipping origin clearly")
    if candidate.country == "DK":
        flags.append("verify EU VAT/OSS/IOSS treatment and current third-country customs charge")
    return flags
