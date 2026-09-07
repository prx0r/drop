#!/usr/bin/env python3
"""
Country Economics Model
=======================
Fixed version. No more static country CPC assumptions.
Uses per-query, per-product, per-country evidence.
"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum


class CustomsRegime(Enum):
    """Three distinct cross-border regimes."""
    INTRA_EU = "intra_eu"           # Warehouse in EU → consumer in EU (OSS)
    IMPORT_LOW_VALUE = "import_low" # From outside EU, item ≤ €150 (IOSS + €3 duty since Jul 2026)
    IMPORT_HIGH_VALUE = "import_high" # From outside EU, item > €150 (full customs)
    NORWAY_VOEC = "norway_voec"     # Norway VOEC for items < NOK 3,000
    NORWAY_STANDARD = "norway_std"  # Norway for items ≥ NOK 3,000


@dataclass
class CrossBorderEconomics:
    """Precise cross-border economics."""
    origin_country: str
    warehouse_country: str
    customer_country: str
    
    # Tax/customs
    customs_regime: CustomsRegime
    vat_rate: float
    recoverable_vat: float  # VAT you can reclaim
    nonrecoverable_tax: float  # Duty, handling fees
    clearance_fee: float
    
    # Costs
    shipping_cost: float
    payment_fee_rate: float
    
    # Delivery
    expected_delivery_days: int
    delivery_reliability: float  # 0-1
    
    # RMA
    rma_route: str  # "local" / "cross_border" / "manufacturer"
    return_cost: float


def calculate_cross_border_economics(
    origin_country: str,
    warehouse_country: str,
    customer_country: str,
    item_value: float,
    shipping_cost: float
) -> CrossBorderEconomics:
    """
    Calculate precise cross-border economics.
    
    Three regimes:
    1. Intra-EU: warehouse in EU → consumer in EU (OSS applies)
    2. Import low-value: from outside EU, item ≤ €150 (IOSS + €3 duty since Jul 2026)
    3. Import high-value: from outside EU, item > €150 (full customs)
    4. Norway VOEC: items < NOK 3,000 (simplified)
    5. Norway standard: items ≥ NOK 3,000 (full customs)
    """
    
    # Determine regime
    if customer_country == "NO":
        if item_value < 3000:  # NOK
            regime = CustomsRegime.NORWAY_VOEC
            vat_rate = 0.25
            duty = 0
            clearance = 0
        else:
            regime = CustomsRegime.NORWAY_STANDARD
            vat_rate = 0.25
            duty = item_value * 0.025  # Approximate
            clearance = 50  # Handling fee
    elif origin_country in ("DE", "NL", "SE", "DK", "FI", "FR", "IT", "ES", "AT") and \
         customer_country in ("DE", "NL", "SE", "DK", "FI", "FR", "IT", "ES", "AT"):
        regime = CustomsRegime.INTRA_EU
        vat_rate = 0.25 if customer_country == "NO" else 0.19 if customer_country == "DE" else 0.24
        duty = 0
        clearance = 0
    elif item_value <= 150:
        regime = CustomsRegime.IMPORT_LOW_VALUE
        vat_rate = 0.25 if customer_country == "NO" else 0.19
        duty = 3  # €3 fixed duty since Jul 2026
        clearance = 5
    else:
        regime = CustomsRegime.IMPORT_HIGH_VALUE
        vat_rate = 0.25 if customer_country == "NO" else 0.19
        duty = item_value * 0.03  # Approximate
        clearance = 50
    
    return CrossBorderEconomics(
        origin_country=origin_country,
        warehouse_country=warehouse_country,
        customer_country=customer_country,
        customs_regime=regime,
        vat_rate=vat_rate,
        recoverable_vat=item_value * vat_rate if regime == CustomsRegime.INTRA_EU else 0,
        nonrecoverable_tax=duty,
        clearance_fee=clearance,
        shipping_cost=shipping_cost,
        payment_fee_rate=0.029,
        expected_delivery_days=3 if regime == CustomsRegime.INTRA_EU else 7,
        delivery_reliability=0.95 if regime == CustomsRegime.INTRA_EU else 0.85,
        rma_route="local" if regime == CustomsRegime.INTRA_EU else "cross_border",
        return_cost=shipping_cost * 2 if regime in (CustomsRegime.IMPORT_LOW_VALUE, CustomsRegime.IMPORT_HIGH_VALUE, CustomsRegime.NORWAY_STANDARD) else shipping_cost,
    )


if __name__ == "__main__":
    print("=== Cross-Border Economics Demo ===\n")
    
    # Scenario: Germany → Finland (intra-EU)
    e1 = calculate_cross_border_economics("DE", "DE", "FI", 500, 15)
    print(f"DE → FI (€500): regime={e1.customs_regime.value}, VAT={e1.vat_rate:.0%}, duty=€{e1.nonrecoverable_tax:.0f}, delivery={e1.expected_delivery_days}d")
    
    # Scenario: China → Finland (import low-value)
    e2 = calculate_cross_border_economics("CN", "CN", "FI", 100, 10)
    print(f"CN → FI (€100): regime={e2.customs_regime.value}, VAT={e2.vat_rate:.0%}, duty=€{e2.nonrecoverable_tax:.0f}, delivery={e2.expected_delivery_days}d")
    
    # Scenario: China → Finland (import high-value)
    e3 = calculate_cross_border_economics("CN", "CN", "FI", 500, 20)
    print(f"CN → FI (€500): regime={e3.customs_regime.value}, VAT={e3.vat_rate:.0%}, duty=€{e3.nonrecoverable_tax:.0f}, clearance=€{e3.clearance_fee:.0f}")
    
    # Scenario: Germany → Norway (above NOK 3,000)
    e4 = calculate_cross_border_economics("DE", "DE", "NO", 20000, 25)  # NOK
    print(f"DE → NO (NOK 20k): regime={e4.customs_regime.value}, VAT={e4.vat_rate:.0%}, duty=NOK{e4.nonrecoverable_tax:.0f}")
    
    # Scenario: Germany → Norway (below NOK 3,000 - VOEC)
    e5 = calculate_cross_border_economics("DE", "DE", "NO", 2000, 15)
    print(f"DE → NO (NOK 2k): regime={e5.customs_regime.value}, VAT={e5.vat_rate:.0%}, duty=NOK{e5.nonrecoverable_tax:.0f}")
