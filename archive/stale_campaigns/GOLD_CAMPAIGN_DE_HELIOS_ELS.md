# STALE — GOLD_CAMPAIGN_DE_HELIOS_ELS.md

*This file is archived. See HCC_V2.md for current campaigns.*

# Campaign: Helios ELS Legacy Ventilation (Germany)

*Generated: 2026-09-07*
*Status: WATCH (B5/B6/B8/B10 UNKNOWN)*

---

## Binary Gate Result

| # | Statement | Verdict |
|---|-----------|---------|
| B1 | Installed base exists | YES |
| B2 | Lifecycle trigger exists | YES |
| B3 | Compatibility problem exists | YES |
| B4 | Local supply exists | YES |
| B5 | Consumer can self-identify | UNKNOWN |
| B6 | Shippable without technician | UNKNOWN |
| B7 | No single specialist owns decision | YES |
| B8 | Supplier will sell to us | UNKNOWN |
| B9 | Compatibility can be proven | YES |
| B10 | Legal responsibility explicit | UNKNOWN |

**Result: B5/B6/B8/B10 UNKNOWN → BLOCKED**

---

## Campaign JSON

```json
{
  "campaign_id": "DE-HELIOS-ELS-001",
  "track": "d2c_compatibility_commerce",

  "country": "DE",
  "language": "de",
  "oem": "Helios",
  "asset_family": "ventilation",
  "installed_asset": "ELS under-plaster ventilation housing",
  "generation": "1984-2008",
  "trigger": "fan_failure",
  "component_family": "fan_insert",

  "status": "WATCH",

  "hard_gates": {
    "supplier_exists": true,
    "stock_fresh": "UNKNOWN",
    "compatibility_proven": true,
    "legal_explicit": "UNKNOWN",
    "buyer_role_tested": false,
    "technician_required": "UNKNOWN"
  },

  "installed_base": {
    "description": "Helios ELS ventilation housings installed in German housing 1984-2008",
    "source": "https://www.heliosventilatoren.de/de/service/kundendienst/ersatzteilwesen",
    "confidence": "MEDIUM"
  },

  "identity": {
    "identification_method": "type plate: article number, product version, production code, serial number",
    "resolver_inputs": ["type plate photo", "housing photo"],
    "resolver_outputs": ["exact fan insert", "retrofit component if needed"]
  },

  "compatibility_graph": {
    "source": "Haustechnik Binder listing + Helios spare-parts page",
    "edges": [
      {"from": "ELS housing 1992-2008", "to": "ELS-VEZ 60 / 00426", "relation": "FITS", "condition": "no conversion, 4-pole plug"},
      {"from": "ELS housing 1989-1992", "to": "ELS-VEZ 60 / 00426", "relation": "FITS", "condition": "no conversion, 4-pole plug"},
      {"from": "ELS housing 1984-1989", "to": "ELS-VEZ 60 / 00426", "relation": "FITS_WITH_CONDITION", "condition": "requires Steckkontakt 20590"}
    ],
    "unresolved": ["all ELS insert families", "controller modules", "EC insert compatibility"]
  },

  "supplier": {
    "identified": true,
    "primary": "Haustechnik Binder",
    "retail_price": "EUR 249.90 incl. VAT",
    "delivery": "1-3 working days",
    "net_prices_verified": false,
    "direct_ship_verified": false
  },

  "economics": {
    "aov": 250,
    "aov_currency": "EUR",
    "supplier_cost": "UNKNOWN",
    "contribution_margin": "UNKNOWN"
  },

  "experiment": {
    "phase": "buyer_role_test",
    "action": "Establish whether German homeowners select these parts themselves or call an installer",
    "success_rule": ["Homeowner selects part in >50% of cases"],
    "kill_rule": ["Installer selects part in >80% of cases"]
  },

  "evidence": [
    {
      "type": "oem_spare_parts",
      "source": "https://www.heliosventilatoren.de/de/service/kundendienst/ersatzteilwesen",
      "date": "2026-09-07",
      "confidence": "HIGH"
    },
    {
      "type": "specialist_listing",
      "source": "https://haustechnik-binder.de/de/Lueftung/HELIOS-Ersatz-Ventilatoren-ELS-1984-bis-2008/",
      "date": "2026-09-07",
      "confidence": "HIGH"
    }
  ],

  "kill_reasons": [],
  "lessons": ["Germany has strong OEM + specialist infrastructure; many categories already well-served"],

  "state": "WATCH"
}
```

---

## Score (if all gates verified)

| # | Statement | Score |
|---|-----------|-------|
| S1 | Type plate photo required | +10 |
| S2 | Wrong part = doesn't fit housing | +10 |
| S3 | 1984-2008 legacy graph with conditions | +10 |
| S4 | Installed base exists (evidence medium) | +10 |
| S5 | Fan failure trigger | +10 |
| S6 | Helios + Haustechnik Binder | +10 |
| S7 | No stock feed | 0 |
| S8 | Direct ship unknown | -10 |
| S9 | Small parcel | +10 |
| S10 | Photo identifiable | +10 |
| S11 | EUR 250 AOV | +10 |
| S12 | Margin unknown | 0 |
| S13 | Wrong-part cost unknown | 0 |
| S14 | Helios has catalogue but not resolver | +10 |
| S15 | Helios is OEM, not competing | +10 |
| S16 | German market fragmented | +10 |
| S17 | German native language | +10 |
| S18 | Ventilation terminology non-trivial | +10 |
| S19 | Fits GMC | +10 |
| S20 | Fits Shopify | +10 |

**Total: 150/200 → VERIFY (needs B5/B6/B8/B10 verification)**

---

## Key Insight from Germany Report

**Germany is a difficult market for obvious installed-base ecommerce because many technical categories already have unusually strong specialist parts merchants and OEM replacement infrastructure.**

The discovery process must move farther into poorly digitised light-commercial/building-infrastructure niches rather than mainstream HVAC, fireplace, roof-window, door-entry, garage-door or plumbing ecosystems.
