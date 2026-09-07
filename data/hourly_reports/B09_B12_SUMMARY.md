# GeoDrop Probe Reports B09-B12 Summary

**Timestamp:** 2026-09-08T12:00:00Z

---

## B09 — Australia Pool Equipment

**Status:** Falsification + mechanism discovery

**Key findings:**
- 1.1 million Australian homes have swimming pools
- 150k–200k annual pump sales, 8-year asset-life assumption
- 50% of surveyed pool owners had replaced a pump
- 42% of replacements were 5–10 years old

**Falsified:** `COHORT_READY_SHOCK_ACTIVATION` — heatwave → hardware-failure spike did not survive evidence standard

**New mechanisms:**
- `OPERATING_COST_OBSOLESCENCE_BEFORE_FAILURE` — 5-star pump uses 55% less energy, pool pumps = 18% of home electricity bill
- `SERVICE_ADVISOR_REPLACEMENT_GATEKEEPER` — installer/pool-shop advice drives 62% of like-for-like replacements
- `STACKED_COMPONENT_CLOCKS` — different components have different warranty periods (1-25 years)

---

## B10 — Norway Cabins

**Status:** Strong evidence + original idea killed

**Key findings:**
- 483,631 holiday houses, 232,065 / 48% outside densely built-up areas
- Expected water-damage claims >10,000 in 2026, >50% higher than usual
- Many losses not discovered until summer, becoming much larger

**New mechanisms:**
- `ABSENCE_AMPLIFIES_DAMAGE_SEVERITY` — remote ownership changes failure economics
- `RISK_PRICER_SUBSIDIZES_PREVENTION` — insurers subsidize prevention (up to 15% off for water shutoff)
- `DETECTION_TO_INTERVENTION_VALUE_SHIFT` — as sensing commoditizes, value moves to response orchestration

**Killed:** Generic HytteGuard hardware idea — Norway already extremely sophisticated

---

## B11 — UK Escape-of-Water Prevention

**Status:** Strong replication

**Key finding:** `RISK_PRICER_SUBSIDIZES_PREVENTION` is now strongly supported across countries

**Evidence:**
- Hiscox gives eligible customers free £149 LeakBot + repair service
- Admiral committed 10,000 insurer-funded devices
- Ofwat funding customer-side leakage technology
- Aviva testing whether water-management standards influence insurance pricing

**The lesson:** The end user need not be the payer. If an insurer, utility, lender or landlord captures avoided loss, it can subsidize or fully fund adoption.

---

## B12 — UK Post-Flood Resilience

**Status:** Strong evidence + new mechanisms

**Key findings:**
- ~6.3 million English properties in flood-risk areas
- Build Back Better provides up to £10,000 above ordinary reinstatement costs
- Over 70% of UK home-insurance market committed to offering BBB
- Take-up at only ~1/3 of households offered BBB

**New mechanisms:**
- `EVENT_GATED_SUPPLY_MARKET` — normal-period demand sustains small specialist industry, disaster unlocks money/demand faster than supply can expand
- `CLAIM_GATEKEEPER_CONTROLS_FUNDED_DEMAND` — loss adjuster more important than Google

**Market shape:** funded customer + proven loss + rebuilding already underway + available resilience budget + low conversion

---

## Mechanism orchard (growing)

```
PHYSICAL          age / wear / failure
WARRANTY          OEM channel closes or opens
INTERFACE         old plumbing / ducts / wiring / refrigerant
ECONOMIC          energy use makes old asset uneconomic
REGULATORY        new equipment requirements / inspections
POLICY            tariff/subsidy changes
WEATHER           cold / flood / heat
OCCUPANCY         absence delays detection
CONTRACTUAL       lease/service requirements
RISK PAYER        insurer/government subsidizes action
```

Each entered the dataset because a probe generated hard supporting evidence.

---

## B13 — Next probe (autonomous selection)

**US hail/storm insurance-funded roofing**

Stress-test/negative control: insurance-funded event demand is enormous and mature. Tests whether `EVENT_GATED_SUPPLY_MARKET` has an optimum rather than "more funded demand = better opportunity."
