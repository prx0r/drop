# Compatibility Commerce Compiler — Refined Thesis

*Generated: 2026-09-07*
*Status: REFINED — Core thesis with corrections*

---

## The One Sentence (Refined)

> **Find physical systems with millions of installed units where a meaningful fraction of failures reduce to "identify this weird replaceable object correctly and get it to me."**

---

## The Correct Equation

```text
ECOMMERCE OPPORTUNITY =

installed_base
× annual_failure_events
× CUSTOMER_PURCHASABLE_SHARE
× online_purchase_share
× information_gap
× probability_we_get_selected
× contribution_profit
```

`CUSTOMER_PURCHASABLE_SHARE` is critical.

For a heat pump:
```
WHOLE UNIT             very low
compressor             very low
refrigerant components very low
main PCB               low/medium
sensor                  medium
Wi-Fi module            high
remote                  very high
filters                 very high
covers/accessories      high
```

---

## New Metrics

### Self-Service Resolution Ratio

Of 100 problems involving this installed asset, how many can realistically go:
photo → identify → buy item → user installs/swaps → solved

WITHOUT professional diagnosis or regulated work?

| Subgraph | Self-service ratio |
|----------|-------------------|
| Remote controls | Very high |
| Filters | Very high |
| Marine adapters | High |
| Cabin pump switches | High |
| Garage remotes | High |
| Robot-mower chargers | High |
| Heat-pump Wi-Fi interfaces | Medium-high |
| Appliance pumps | Medium |
| Heat-pump PCB | Low |
| Compressor | Near zero |
| Whole heat pump | Near zero |

### Pre-SKU Uncertainty

How difficult is it for a nonexpert to translate their physical problem into an exact purchasable SKU?

We want **high uncertainty but high resolvability**.

```
Product A: User searches "Bosch 00631200"
→ They already know the SKU
→ We're just another merchant

Product B: User says "This came out of the water system in my 2008 Norwegian cabin"
→ That's where we add enormous value
```

---

## The Winning Function

```text
GEODROP_AGENT_SCORE =

installed_base
× replacement_event_rate
× SELF_SERVICE_RESOLUTION
× PRE_SKU_UNCERTAINTY
× visual_identifiability
× compatibility_complexity
× digital_supplier_gap
× supplier_accessibility
× gross_profit_per_resolution
× local_language_fragmentation

÷
wrong_fit_risk
÷ marketplace_quality
÷ regulatory_friction
```

---

## What Changes

### Much Stronger
- Norwegian cabin water components (pressure switches, pump heads, filters, membranes, connectors)
- Marine retrofit adapters
- Garage/gate control ecosystem
- Commercial equipment consumable/easy parts

### Weaker Than Previously Thought
- Whole heat-pump lifecycle (installer revenue, not consumer ecommerce)
- EV charger replacement (often technician procurement)
- Heat-pump PCBs/compressors (wrong buyer)

---

## The Heat-Pump Lesson

"1.8M heat pumps and 33% replacements" does NOT justify a dropshipping store.

What it tells us: Finland contains an enormous aging installed base worth mining for **specific consumer-purchasable failure surfaces**.

---

## The Moat (Refined)

Not:
- language alone (LLM translation is excellent)
- visual identification alone (becoming commodity)
- machine-readable feeds alone (not a ranking guarantee)

But:
- **installed-base knowledge**
- **legacy model aliases**
- **local suppliers**
- **local inventory**
- **historical generations**
- **actual compatibility evidence**

Language is the wedge. **The graph is the moat.**

---

## The Information Moat

The information moat is **upstream of fulfillment**.

Once the exact commodity SKU is known, price/logistics start dominating again.

We need to own the **uncertain step before the SKU is known**:

```
USER: "I have this old remote."
OURS: identify generation → resolve SKU → explain compatibility → provide current successor
```

---

## Sources

1. AaltoAir — heat pump replacement journey
2. Innoair — Mitsubishi remotes €99-€141
