# GeoDrop Installed-Base Ownership — Finland — 2026-09-07 21:05 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 10:10:17 -0400

# GeoDrop Installed-Base Ownership — Finland

## RUN DECISION

**NO NEW OWNABLE FINLAND NICHE cleared all hard gates in this run.**

This is a productive null result. The strongest new research cell is **Ouman legacy building/HVAC controller successor migration (EH-105 → S105; EH-203 → S203)**, but it remains **HUMAN_ACTION_REQUIRED / WATCH**, not launchable. Several apparently attractive Finnish installed-base niches were killed because OEMs or specialist merchants already solve compatibility unusually well.

The prior-state search found **no earlier sent Gmail reports** with the exact Finland subject prefix, so this is the novelty bootstrap run. The canonical prompt explicitly names Allaway as prior state; therefore Allaway was not rediscovered or counted as novel.

---

## 1. EXECUTIVE ALPHA

### Strongest new near-miss — Ouman legacy controllers

**Atom:** Finland × Ouman × legacy EH-series building/HVAC controllers × obsolescence/successor migration × controller × generation/configuration compatibility.

Ouman maintains an official discontinued-products archive stating that **EH-105 is replaced by S105** and **EH-203 is replaced by S203**, while also retaining documentation and configuration software for legacy controllers. This is exactly the kind of supersession graph GeoDrop wants. The commercial gap is less clear: the products are building-control equipment, likely purchased/commissioned through professional HVAC/building-automation channels, and reseller economics plus installation/configuration responsibility are unresolved.

Primary evidence:
- Ouman discontinued-products archive: https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/
- Ouman applications / EH-105 configuration software: https://ouman.fi/ouman-sovellukset/
- Ouman S105 pilot announcement explicitly describing S105 as EH-105’s replacement: https://kauppa.ouman.fi/haemme-s105-ilmastoinninsaatimelle-pilot-kohteita/

**Decision:** HUMAN_ACTION_REQUIRED / WATCH.

Highest-EVI unresolved questions:
1. Can an unaffiliated ecommerce reseller buy S105/S203 at dealer pricing?
2. Is field replacement sufficiently standardized to sell controller + migration bundle without taking on engineering liability?
3. Which EH-105/EH-203 configurations require rewiring, sensor replacement, I/O remapping, or professional recommissioning?
4. Is the customer actually the building owner, an HVAC contractor, or an automation integrator?

Until those are answered, margin and lightweight ecommerce feasibility are UNKNOWN.

### Most important hard kill — legacy Vallox / ILTO / Swegon fan motors

This initially looked excellent: old ventilation units, expensive replacement fans, left/right variants, connector changes, old motor-code matching and genuine wrong-part risk. But Finnish specialist merchants already solve much of the decision.

Examples:
- BistroTec Vallox 95 fan motor: asks the buyer for the old motor number, exposes rotation, dimensions, motor type and detailed fitment guidance: https://www.bistrotec.fi/product/33109/vallox-95-puhallinmoottori-185w
- BistroTec Swegon/ILTO/Meptek VG400 fan motor: explicit handedness and transfer-part caveats: https://www.bistrotec.fi/product/33359/swegon-casameptekilto-vg400-r-puhallinmoottori-185w
- Suodatinkeskus ILTO/Swegon 800/850 fan: exact compatible models and 5-pin → 4-pin connector migration note: https://www.suodatinkeskus.com/fi/product/ilto-swegon-puhallin-800-850-r-malli/5840
- JL-TT fan packages: explicit model lists and handedness: https://www.jltt.fi/tuote/swegon-f200r-puhallinpakkaus-l-malli-tulo-poisto/

**Decision:** KILL as a standalone GeoDrop ownership niche. The compatibility problem exists, but competent local specialists already own much of it.

---

## 2. MASS-SCAN FRONTIER

| Candidate atom | Structural signal | Strongest counterevidence | State |
|---|---|---|---|
| Ouman EH-105/EH-203 → S105/S203 controller migration | Explicit OEM supersession; legacy docs/configuration; meaningful configuration complexity | Likely professional commissioning; reseller economics unknown | HUMAN_ACTION_REQUIRED / WATCH |
| Vallox legacy ventilation fan motors | Old model generations; motor-code/handedness ambiguity; €150–€900+ parts | BistroTec/Suodatinkeskus/JL-TT already expose detailed fitment | KILL |
| ILTO/Swegon CASA legacy fan assemblies | Old models; left/right variants; connector migration | Strong specialist ecommerce with exact compatibility | KILL |
| Enervent Pingvin/LTR legacy filters | Installed legacy ecosystem; recurring consumable | Multiple strong specialist filter stores; compatibility simple | KILL |
| Vallox legacy filters | Recurring consumables; old model families | Bauhaus/Dahl/Dreamhome and specialists already map models accurately | KILL |
| Uponor/Wirsbo 24V floor-heating thermostat replacement | Genuine legacy installed base; old Wirsbo branding; compatibility caveats | Uponor itself publishes exact replacement guidance and wiring; retail stock abundant | KILL |
| Oras discontinued faucet cartridges | Large Finnish installed base; old faucet models; cartridge compatibility | Oras product pages expose discontinued models + compatible spare parts directly | KILL |
| Harvia C80/C90/C150 control boards | Long-lived sauna equipment; PCB failure; superseded electrical part numbers | Harvia + Saunavaraosat + Finnish electrical registry expose parts/supersession well | KILL / WATCH only for obscure generations |
| Oilon old LJ burner → BF1 replacement | Explicit successor; high ticket (~€950 public retail) | Selection reportedly mainly by kW; professional burner installation/service burden | KILL for lightweight ecommerce |
| Savo legacy cooker-hood filters | Replacement consumable; legacy model mapping | Low ticket; compatibility frequently simple; specialist merchant already maps exact models | KILL |
| Ensto floor-heating thermostat replacement | Huge likely installed category; sensor/resistance compatibility can matter | Current products broadly distributed; fixed electrical installation requires professional work; exact legacy gap not yet demonstrated | WATCH, low priority |
| NIBE Fighter-era heat-pump sensors/parts | Long asset life and replacement tail | Strong Nordic spare-part channels; technical service/install burden; Finland-specific merchant gap unproven | WATCH, low priority |

No candidate was promoted merely for being technically interesting.

---

## 3. DEEP AUDIT — OUMAN LEGACY CONTROLLER MIGRATION

### Executive thesis

Finland has a long-running installed base of Ouman building/HVAC controllers. Ouman’s own discontinued-product archive preserves legacy documentation and explicitly maps at least EH-105 → S105 and EH-203 → S203. A possible GeoDrop object is not “sell Ouman controllers,” but a bounded **legacy controller migration graph** that resolves old controller identity, current successor, I/O/sensor/configuration implications, required accessories and locally available transaction paths.

### Why this exists

Lifecycle trigger: **OBSOLESCENCE / FAILURE / SUCCESSOR_MIGRATION.**

The useful decision surface is potentially:

old controller model
→ application / number of circuits
→ connected sensors/actuators
→ legacy configuration
→ current successor
→ required wiring/I/O changes
→ commissioning requirement
→ purchasable controller/accessories.

### Verified compatibility/supersession edges

- EH-105 **REPLACED_BY** S105 — official Ouman archive.
- EH-203 **REPLACED_BY** S203 — official Ouman archive.
- EH-105 has legacy configuration software still published by Ouman.

Sources:
- https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/
- https://ouman.fi/ouman-sovellukset/
- https://kauppa.ouman.fi/haemme-s105-ilmastoinninsaatimelle-pilot-kohteita/

### What is still UNKNOWN

- Installed-base count by model/generation.
- Surviving installed cohort.
- Failure/replacement incidence.
- Dealer/net cost.
- Reseller authorization.
- Dropship/blind-ship capability.
- S105/S203 current public/wholesale price and reliable stock across independent supplier clusters.
- Whether replacement is plug-compatible or typically requires engineering/configuration work.
- Return/RMA burden.
- Consumer vs contractor purchase share.
- Native-language exact-model search volume/CPC/CVR.

### Ownership-gap audit

Ouman itself is technically strong and publishes legacy documentation, which weakens a pure information-gap thesis. However, the OEM archive is not necessarily a consumer-facing migration/checkout decision engine. The gap, if real, would be in **transactional migration packaging**, not in discovering that a successor exists.

The main threat is that the economically relevant buyer is an HVAC/building-automation professional who already knows Ouman and sources via established trade accounts. If true, GeoDrop’s consumer-specialist wedge largely disappears.

### Economics

**UNKNOWN.** Public Ouman EH-800 pricing observed at €906 excluding VAT demonstrates that Ouman controllers can be high-ticket, but this is NOT evidence of S105/S203 margin or economics and is not used as a proxy.

No margin, CAC, CPC or CVR is inferred.

### Minimum useful graph

Before any store build, resolve at least:
- EH-105 variants/configurations → S105 conditions;
- EH-203 variants/configurations → S203 conditions;
- sensors/actuators retained vs replaced;
- wiring terminal mapping;
- accessories/modules required;
- commissioning steps that legally/operationally require a professional;
- negative edges where a nominal successor is not a simple swap.

### Distribution projection if commercial gates clear

**GMC:** brand, MPN/GTIN, truthful stock/price/shipping, product_detail for controller I/O and electrical characteristics. Historical installed assets should remain in GeoDrop’s own compatibility graph rather than being forced into inventory-only relationship fields.

**Shopify:** controller SKUs as products; legacy model, application, compatibility conditions, successor relation, installation class and evidence URL as structured metafields/metaobjects.

**Web/API:** `/ouman/eh-105/replacement`, `/ouman/eh-203/replacement`, migration matrices, “identify your controller” flow, structured compatibility API with explicit UNKNOWN/REQUIRES_PRO states.

### Ads probe if supply/economics clear

Native Finnish exact-model Search only:
- `ouman eh-105 korvaava`
- `ouman eh-105 uusi säädin`
- `ouman eh-203 korvaava`
- `ouman eh-203 varaosa`
- `ouman s105`
- `ouman s203`

Negatives should exclude manuals/software/support-only queries once real search-term data appears. No paid probe is justified before reseller and installation-path gates are resolved.

### Hypothesis ledger

**H1:** A meaningful Finland market exists for Ouman legacy controller migration where buyers need a reliable old-model → successor → required-parts → purchase path that no merchant currently owns.

**H0:** The meaningful buyers are professional HVAC/building-automation firms already served by Ouman/trade channels; migration requires project-specific commissioning, leaving little lightweight ecommerce ownership gap.

**Strongest evidence for H1:** official explicit legacy → successor mappings and retained legacy configuration infrastructure show a real aging installed-product graph.

**Strongest evidence for H0:** product class is professional building control; public evidence does not yet show consumer transaction friction or reseller whitespace.

**Falsifier:** evidence that Ouman/major Finnish trade distributors already provide a complete old-model migration/selection/ordering workflow to the actual buyer, or that replacement typically requires bespoke engineering rather than a bounded compatibility decision.

**Highest-EVI next test:** supplier/Ouman channel contact asking exact S105/S203 dealer availability, reseller eligibility, migration kit contents, commissioning requirements and whether old EH installations can be converted from a finite documented ruleset.

**Decision:** HUMAN_ACTION_REQUIRED / WATCH.

---

## 4. HARD KILL DETAILS

### Uponor / Wirsbo 24V thermostat migration — KILL

This looked attractive because old Wirsbo systems remain installed and a replacement thermostat must match voltage/wiring. But Uponor itself has an unusually strong support page that answers the exact question: a 24V wired Wirsbo room thermostat can be replaced by Uponor spare thermostat LVI 2026916, and it publishes terminal mapping. Retail availability is also straightforward.

OEM: https://www.uponor.com/fi-fi/lattialammityksen-saatojarjestelmien-tukisivusto/wirsbo
Retail: https://lvitarvikkeet.fi/collections/sahko/products/uponor-2026916
Trade: https://www.ahlsell.fi/products/lampo-ja-vesi/lammitys/lattialammitys/ohjausjarjestelmat/termostaatit/2026916

The compatibility graph is valuable but already substantially owned by the OEM. A GeoDrop store would mostly compete on merchandising.

### Oras legacy faucet cartridges — KILL

Oras product pages expose spare-part identifiers and the discontinued faucet models they fit. Example cartridge 158888 lists compatible discontinued Oras Saga faucet codes and official spare-part documentation.

https://www.oras.com/fi/tuoteperheet/oras/saatoosa/158888

This is a good example of what an OEM-owned compatibility graph looks like. GeoDrop should seek the opposite.

### Harvia C-series electronics — KILL / narrow WATCH

There is real supersession structure: the Finnish electrical product registry shows old Harvia WX200 / C80-C90-C150 upper board archived and a replacement electrical product number. But Harvia itself exposes product families/spare parts, and specialist Saunavaraosat sells exact C-series boards.

- https://www.sahkonumerot.fi/8261460
- https://www.saunavaraosat.com/product/223/harvia-c90-alakortti-sp211--wx211
- https://www.harvia.com/fi/tuotteet/C150400/c150-170-kw-valkoinen

Potential obscure generations can be revisited later, but the obvious C-series cell is not whitespace.

### Oilon old LJ burners — KILL

Finnish retailers state that current Oilon BF1 FUV HC replaces old LJ burners and selection is by kW. Public retail is around €949–€984, so ticket size is attractive, but the decision appears less compatibility-rich than expected and the burner is professional heating equipment with substantial installation/service burden.

- https://jukira.fi/tuote/oljypoltin-oilon-oljypoltin-bf-1-fuv-hc-15-55kw/
- https://talotuote.fi/p51239/oilon-%C3%B6ljypoltin-bf1-fuv-hc-15-55kw

### Vallox / Swegon / ILTO fan motors — KILL

The underlying mechanism is excellent—old equipment, motor-code ambiguity, handedness, connector migrations—but the strongest Finnish specialist merchants already perform the job GeoDrop proposes to own. This is a hard kill rather than a score downgrade.

---

## 5. NOVELTY AUDIT

Prior Finland email corpus under the required subject prefix: **0 messages found**.

Known prior object from canonical GeoDrop state: **Allaway Finland**, deliberately excluded from novelty discovery.

New substantive cells investigated this run:
1. Ouman EH-series migration
2. Vallox legacy fan motors
3. ILTO/Swegon CASA fan assemblies
4. Enervent legacy filters
5. Vallox legacy filters
6. Uponor/Wirsbo thermostat migration
7. Oras legacy cartridges
8. Harvia C-series controller electronics
9. Oilon LJ → BF1 burner migration
10. Savo legacy hood filters
11. Ensto legacy/current floor-heating thermostats
12. NIBE Fighter-era parts

Semantic duplicates rejected: multiple retailer pages for the same Uponor thermostat; multiple Vallox/ILTO fan SKUs that did not create a new market mechanism; multiple filter-store pages demonstrating the same solved-merchant pattern.

Reusable negative pattern learned this run:

> **Finland’s HVAC/LVI ecosystem frequently has exceptionally strong model-specific specialist ecommerce and OEM support. Compatibility complexity alone is not enough; we must explicitly test whether the Finnish incumbent already exposes the graph.**

This is useful because it should make later Finland runs kill mainstream ventilation/filter/sauna/plumbing cells earlier and shift exploration toward less digitally mature installed bases.

---

## 6. SOURCE-YIELD SUMMARY

High-yield source families this run:
- OEM discontinued-product archives: very high
- OEM support/FAQ pages: very high for hard kills
- Finnish specialist spare-parts stores: very high for incumbent audit
- Finnish trade distributors/registries: high for identifiers/supersession
- Generic retail product pages: medium; useful mostly for stock/public pricing

Low-yield / deprioritized:
- generic filter categories where fitment is already standardized
- broad searches for “old spare part” without OEM/model binding

---

## 7. HARD-GATE STATUS — BEST NEW CELL

| Gate | Ouman legacy migration |
|---|---|
| G1 Installed base exists | SUPPORTED qualitatively; size UNKNOWN |
| G2 Real lifecycle purchase trigger | SUPPORTED — obsolete controllers have named successors |
| G3 Nontrivial compatibility/identity problem | SUPPORTED but depth not yet fully mapped |
| G4 Real local supply | PARTIAL; OEM exists, exact S105/S203 stock graph unresolved |
| G5 Genuine ownership/merchant gap | UNKNOWN |
| G6 Legitimate reseller/transaction path | UNKNOWN |
| G7 Viable/testable economics | UNKNOWN |
| G8 Manageable RMA/regulatory burden | UNKNOWN / likely professional commissioning |

Because G5–G8 remain unresolved, **no Ownability Score /130 is issued**. The prompt forbids using weighted scoring to hide failed or UNKNOWN hard gates.

---

## 8. MACHINE-READABLE CAMPAIGN JSON — BEST NEW CELL

```json
{
  "campaign_id": "FI-OUMAN-EH-MIGRATION-20260907-01",
  "country": "FI",
  "state": "HUMAN_ACTION_REQUIRED",
  "atom": {
    "oem": "Ouman",
    "installed_asset": "EH-series HVAC/building controllers",
    "generation": ["EH-105", "EH-203"],
    "lifecycle_trigger": ["OBSOLESCENCE", "FAILURE", "SUCCESSOR_MIGRATION"],
    "component": "controller",
    "compatibility_decision": "legacy controller to current successor and migration requirements"
  },
  "installed_base": {
    "exists": "SUPPORTED",
    "count": "UNKNOWN",
    "surviving_cohort": "UNKNOWN"
  },
  "compatibility_graph": {
    "edges": [
      {
        "from": "EH-105",
        "relation": "REPLACED_BY",
        "to": "S105",
        "source": "https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/",
        "evidence_grade": "A"
      },
      {
        "from": "EH-203",
        "relation": "REPLACED_BY",
        "to": "S203",
        "source": "https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/",
        "evidence_grade": "A"
      }
    ],
    "negative_edges": [],
    "unresolved_edges": [
      "sensor compatibility",
      "actuator compatibility",
      "terminal/wiring migration",
      "I/O mapping",
      "configuration migration",
      "professional commissioning requirement"
    ]
  },
  "supplier_graph": {
    "oem": "Ouman",
    "reseller_eligibility": "UNKNOWN",
    "dealer_price": "UNKNOWN",
    "stock": "UNKNOWN",
    "dropship": "UNKNOWN",
    "feed_api_csv": "UNKNOWN"
  },
  "demand": {
    "search_volume": "UNKNOWN",
    "cpc": "UNKNOWN",
    "cvr": "UNKNOWN",
    "query_families": [
      "ouman eh-105 korvaava",
      "ouman eh-105 uusi säädin",
      "ouman eh-203 korvaava",
      "ouman eh-203 varaosa",
      "ouman s105",
      "ouman s203"
    ]
  },
  "economics": {
    "supplier_cost": "UNKNOWN",
    "pre_ad_contribution": "UNKNOWN",
    "break_even_cac": "UNKNOWN",
    "break_even_cpc": "UNKNOWN"
  },
  "competition": {
    "content_gap": "PARTIAL",
    "merchant_gap": "UNKNOWN",
    "strongest_counterparty": "Ouman OEM / Finnish HVAC trade channel"
  },
  "hypothesis": {
    "h1": "Legacy Ouman controller owners/installers need a bounded migration graph and transactional path not currently owned by one merchant.",
    "h0": "Professional HVAC buyers are already adequately served by OEM/trade channels and replacements require project-specific commissioning.",
    "falsifier": "OEM/trade channel already provides full old-model migration and ordering workflow, or migration is mostly bespoke engineering.",
    "highest_evi_next_test": "Resolve S105/S203 reseller eligibility, dealer pricing, migration-kit contents and commissioning requirements directly with Ouman/distributors."
  },
  "hard_gates": {
    "G1": "SUPPORTED_SIZE_UNKNOWN",
    "G2": "SUPPORTED",
    "G3": "SUPPORTED_PARTIAL",
    "G4": "PARTIAL",
    "G5": "UNKNOWN",
    "G6": "UNKNOWN",
    "G7": "UNKNOWN",
    "G8": "UNKNOWN"
  },
  "decision": "HUMAN_ACTION_REQUIRED"
}
```

---

## FINAL RUN OUTPUT

**BEST NEW OWNABLE NICHE:** NONE CLEARED HARD GATES.

**BEST NEAR-MISS:** Ouman EH-105/EH-203 legacy-controller → S105/S203 migration graph.

**MOST IMPORTANT KILL:** Vallox / ILTO / Swegon legacy fan motors — excellent structural fit, but Finnish specialist merchants already solve compatibility and checkout too well.

**NEW REUSABLE MARKET MECHANISM:** Explicit OEM discontinued-product archives can reveal successor graphs quickly, but in Finland they also frequently reveal that the OEM itself has already solved the informational side. Future scans should pair every supersession discovery immediately with a buyer-channel test: consumer vs professional, standardized swap vs commissioned project.

**HIGHEST-EVI NEXT RESEARCH ACTION:** Contact Ouman or an authorized Finnish distributor with a tightly bounded questionnaire for S105/S203: dealer eligibility, net pricing/MOQ, stock, direct shipping/feed availability, exact EH-105/EH-203 migration rules, accessory/sensor reuse, and whether commissioning must be performed by an authorized professional. This single action can either promote the cell toward SUPPLIER_READY or kill it cheaply.
