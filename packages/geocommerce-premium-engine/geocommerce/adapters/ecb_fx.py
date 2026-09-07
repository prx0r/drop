from __future__ import annotations

from dataclasses import dataclass
from xml.etree import ElementTree as ET
import httpx

from .base import AdapterError

ECB_DAILY_XML = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


def parse_ecb_rates(xml_text: str) -> dict[str, float]:
    """Parse ECB daily reference rates into EUR-base units.

    Returned values mean `1 EUR = rate[currency]`.
    The ECB rates are research/reference inputs; do not use them as promised checkout FX.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise AdapterError(f"invalid ECB XML: {exc}") from exc
    rates: dict[str, float] = {"EUR": 1.0}
    for node in root.iter():
        currency = node.attrib.get("currency")
        rate = node.attrib.get("rate")
        if currency and rate:
            try:
                rates[currency.upper()] = float(rate)
            except ValueError:
                continue
    if len(rates) < 2:
        raise AdapterError("ECB response contained no usable rates")
    return rates


def convert_amount(amount: float, from_currency: str, to_currency: str, rates: dict[str, float]) -> float:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in rates or to_currency not in rates:
        missing = [c for c in (from_currency, to_currency) if c not in rates]
        raise AdapterError(f"ECB rate missing for: {', '.join(missing)}")
    # ECB publishes 1 EUR = X units. Convert source -> EUR -> target.
    eur = float(amount) / rates[from_currency]
    return eur * rates[to_currency]


@dataclass
class ECBFXAdapter:
    url: str = ECB_DAILY_XML

    def fetch_rates(self) -> dict[str, float]:
        with httpx.Client(timeout=20, follow_redirects=True) as client:
            r = client.get(self.url)
        if r.status_code >= 400:
            raise AdapterError(f"ECB FX {r.status_code}: {r.text[:500]}")
        return parse_ecb_rates(r.text)

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        return convert_amount(amount, from_currency, to_currency, self.fetch_rates())
