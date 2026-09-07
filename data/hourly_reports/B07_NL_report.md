# [GoldProbe B07] Netherlands Solar Inverter Aftermarket — full report + JSON

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Sun, 6 Sep 2026 20:22:17 -0700
**Gmail ID:** 1a079e35998a1954

---

GoldProbe B07 complete.

Core result: the simple B06 warranty-expiry model was falsified as too coarse. Dutch residential PV is enormous and mature, and national inverter repair/revision is real, but aftermarket timing depends on multiple clocks: brand/model warranty, technical age, installer survival, policy change and compatibility obsolescence.

Key hard findings:
- Residential PV capacity rose from 2.329 GW in 2018 to 11.672 GW in 2024 (+401.2%).
- Netbeheer Nederland reports ~2.0m solar homes end-2022, ~2.6m end-2023, just under 3m end-2024; growth slowed from ~30% to ~10%.
- SolarEdge standard inverter warranty: 12 years, extendable to 20/25.
- SMA base warranty: 5 years; many newer registered residential units can reach 10 years free.
- National mail-in inverter repair is already mature: fixed model-specific prices, no-cure-no-pay, 3-year repair warranty.
- Selected live repair-price sample median: €430.76 (range €279–€773.19 across different models/powers; not directly comparable to one replacement SKU).
- SolarEdge Power Care in NL: €100/year Lite, €150/year Premium, including OEM monitoring/support even when the original installer is gone.
- Dutch net metering ends 1 Jan 2027, creating a policy/compatibility clock that can trigger inverter/EMS/battery decisions before physical failure.

New mechanism candidates:
1. MULTI_CLOCK_AFTERMARKET_TRIGGER
2. ORPHANED_INSTALLED_BASE
3. POLICY_OBSOLESCENCE_BEFORE_PHYSICAL_FAILURE

Cross-probe update: REMOVABLE_CONTROL_BOARD_DELOCALIZES_REPAIR is now strongly replicated across UK EV chargers and Dutch solar inverters.

Autonomous next probe: B08 Finland heat-pump replacement, run natively under GoldProbe 2.1 to test the multi-clock aftermarket model with hard installed-base/replacement/regulation/model-compatibility evidence.

Full Markdown report and structured JSON are attached.

