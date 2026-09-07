from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class CountryProfile:
    code: str
    name: str
    currency: str
    language: str
    standard_vat_rate: float
    local_payments: tuple[str, ...]
    default_payment_fee_rate: float
    target_delivery_days: int
    max_acceptable_delivery_days: int
    local_return_address_bonus: float
    localization_moat: float
    import_scheme: str
    notes: str = ""


COUNTRIES: Mapping[str, CountryProfile] = {
    "NO": CountryProfile(
        "NO", "Norway", "NOK", "nb-NO", 0.25,
        ("Vipps", "cards"), 0.025, 4, 8, 1.0, 0.85,
        "VOEC for eligible low-value B2C goods; validate item/category eligibility and NOK 3,000-per-item limit",
        "High checkout sensitivity to shipping/return cost; transparent delivered pricing is critical.",
    ),
    "DK": CountryProfile(
        "DK", "Denmark", "DKK", "da-DK", 0.25,
        ("MobilePay", "cards"), 0.025, 3, 7, 1.0, 0.75,
        "EU VAT/OSS/IOSS rules; validate current customs treatment for third-country imports",
        "Smooth checkout and visible shipping price are major conversion factors.",
    ),
    "GB": CountryProfile("GB", "United Kingdom", "GBP", "en-GB", 0.20, ("cards", "PayPal", "Apple Pay"), 0.025, 3, 7, 1.0, 0.25, "UK VAT/import rules", "Control market."),
    "SE": CountryProfile("SE", "Sweden", "SEK", "sv-SE", 0.25, ("Swish", "cards", "Klarna"), 0.025, 3, 7, 1.0, 0.70, "EU VAT/OSS/IOSS rules"),
    "FI": CountryProfile("FI", "Finland", "EUR", "fi-FI", 0.255, ("cards", "online bank", "MobilePay"), 0.025, 4, 8, 1.0, 0.80, "EU VAT/OSS/IOSS rules"),
    "IE": CountryProfile("IE", "Ireland", "EUR", "en-IE", 0.23, ("cards", "PayPal", "Apple Pay"), 0.025, 3, 7, 1.0, 0.20, "EU VAT/OSS/IOSS rules"),
    "CH": CountryProfile("CH", "Switzerland", "CHF", "de-CH", 0.081, ("cards", "TWINT"), 0.025, 4, 8, 1.0, 0.85, "Swiss VAT/import rules"),
    "AU": CountryProfile("AU", "Australia", "AUD", "en-AU", 0.10, ("cards", "PayPal", "Afterpay"), 0.025, 4, 8, 1.0, 0.25, "Australian GST/import rules"),
    "NZ": CountryProfile("NZ", "New Zealand", "NZD", "en-NZ", 0.15, ("cards", "Afterpay"), 0.025, 4, 8, 1.0, 0.35, "New Zealand GST/import rules"),
    "AE": CountryProfile("AE", "United Arab Emirates", "AED", "ar-AE", 0.05, ("cards", "Apple Pay", "cash-on-delivery"), 0.03, 3, 7, 0.8, 0.90, "UAE VAT/import rules"),
    "SA": CountryProfile("SA", "Saudi Arabia", "SAR", "ar-SA", 0.15, ("Mada", "cards", "Apple Pay"), 0.03, 3, 7, 0.8, 0.95, "Saudi VAT/import rules"),
}
