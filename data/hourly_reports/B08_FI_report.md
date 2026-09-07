# [GoldProbe B08] Finland Heat-Pump Replacement — Multi-Clock Aftermarket Replicated

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Sun, 6 Sep 2026 23:31:17 -0400
**Gmail ID:** 1a079eb99eb536e2

---

# GoldProbe B08 — Finland Residential Heat-Pump Replacement

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Does the B07 `MULTI_CLOCK_AFTERMARKET_TRIGGER` survive in a physically installed, climate-critical asset?

## Executive result

**Yes, directionally — and Finland makes the mechanism more precise.**

SULPU reports **74,000 heat-pump deliveries in H1 2026, +63% year-on-year**, with air-to-air units +71%. Its explanation explicitly includes both the **start of the air-to-air replacement market** and the **cold winter**, alongside low prior sales and improving economic conditions.

Source:
https://www.sulpu.fi/5132-2/

That gives us a better aftermarket model:

> **cohort readiness creates latent replacement demand; an external performance shock helps determine when it converts.**

This is stronger than simply saying “old machines get replaced.”

---

## 1. The installed-base scale is enormous, but the source itself has a definition problem

SULPU reports:
- 2025 sales: **112,000**
- 2025 market growth: **10.7%**
- 2025 system sales value: **>€600m**
- historical investment: **~€10bn**
- historical heat pumps sold: **>1.8m**
- replacement: **roughly one third of heat-pump sales**

Source:
https://www.sulpu.fi/heat-pump-sales-returned-to-a-growth-path-a-rise-of-10-pump-sales-in-finland-already-worth-10-billion/

The same page later says **1.9m installed**. The August 2026 release says **almost 2m installed**.

GoldProbe does not resolve that silently. B08 stores the contradiction explicitly and uses **~1.8–2.0m market scale**, not a fake exact stock value.

This is exactly why evidence atoms need stock definitions.

---

## 2. Replacement is already material while the primary market is still growing

SULPU's Jan 2025 release said roughly **one third of air-to-air heat-pump sales** were replacements.

2024 AAHP sales: **85,000**.  
Approximate replacement proxy:

**~28,333 AAHP replacements**

The Jan 2026 release broadens the wording to roughly **one third of heat-pump sales**. Applying that approximate share to 112,000 total sales gives only a contextual proxy:

**~37,333 replacement transactions**

This is not audited transaction classification. It is still powerful market evidence.

At the same time, H1 2026 deliveries grew **63%**.

So B08 creates:

### `AFTERMARKET_OVERLAPS_PRIMARY_GROWTH`

> Replacement can become a major share of a category **before** headline unit sales stop growing.

That's important for GoldProbe. Waiting until a category “looks mature” means arriving too late.

---

## 3. Historic cohorts line up with the replacement wave

Observed SULPU air-to-air sales:

| Year | AAHP sales |
|---|---:|
| 2012 | 45,000 |
| 2013 | 45,718 |
| 2014 | 52,822 |
| **2012–14 total** | **143,540** |

Sources:
https://www.sulpu.fi/wp-content/uploads/2021/05/Lehdisto%CC%88tiedote-SULPU-1.2013.pdf  
https://www.sulpu.fi/wp-content/uploads/2021/05/Statistics-Finland-Heat-Pump-Sales-per-HP-capacity-2014f.pdf

Those machines are now approximately **12–14 years old**.

Tukes gives heat pumps a broad **10–25 year** lifecycle range and explicitly tells consumers to ensure future parts/service availability.

Source:
https://tukes.fi/koti-ja-vapaa-aika/kodin-tekniikka-ja-sahko/ilmalampopumput-ja-jaahdytyslaitteet

Toshiba Finland gives a typical high-quality AAHP life of about **15 years**.

Source:
https://www.toshibasuomi.fi/ilmalampopumpun-kayttoika/

We therefore have **143,540 directly observed 2012–2014 AAHP sales entering a 12–14-year age band in 2026**.

This is a cohort exposure measure, **not surviving stock** and not a predicted failure count.

The alignment with SULPU's independently reported replacement-market emergence is nonetheless strong.

---

## 4. The next replacement waves are already visible in historic sales

SULPU annual data:

- 2018: **75,616 total / 59,395 AAHP**
- 2019: **98,205 / 79,033 AAHP**
- 2020: **102,293 / 82,188 AAHP**
- 2021: **129,375 / 103,136 AAHP**
- 2022: **196,000 / 160,000 AAHP**

Sources:
https://www.sulpu.fi/wp-content/uploads/2021/05/Heat-Pump-market-in-Finland-2019-slides-f.pdf  
https://www.sulpu.fi/wp-content/uploads/2022/01/Heat-Pump-market-in-Finland-2021-slidesf-1.pdf  
https://www.sulpu.fi/almost-200000-heat-pumps-were-sold-last-year-an-increase-of-50/

If service-life distributions remain broadly similar, the **late-2020s/2030s replacement pool will be substantially larger** than the cohort now reaching replacement age.

GoldProbe should therefore store historic annual installations even when today's business is replacement.

---

## 5. Cold weather appears to activate the latent cohort

This is the highest-information B08 finding.

SULPU's August 2026 explanation for +63% growth names several causes simultaneously:

1. start of air-to-air replacement market
2. cold winter
3. unusually low prior-year sales
4. improved economic outlook
5. category maturity/reputation

This is not our interpretation imposed on the data; it is the industry's stated explanation.

### New candidate: `COHORT_READY_SHOCK_ACTIVATION`

> An old installed base creates latent demand. A climate/performance shock can move households from “old but functioning” into actual purchase.

That explains a real marketplace example found in Helsinki: a homeowner with a **14-year-old functioning Mitsubishi MSZ-GE35VAH** sought a pre-season turnkey replacement with a modern Daikin or Mitsubishi model, specifying strong performance at -20°C to -25°C.

Source:
https://www.urakkamaailma.fi/remontti/ilmalampopumpun-vaihto-daikin-perfera-30-nepura-tai-mitsubishi-ft35-sis-vanhan-purun/helsinki/251137

The marketplace job is anecdotal; the SULPU market-level statement is the stronger evidence.

---

## 6. Replacement economics are high enough for diagnosis/specification to matter

AaltoAir's current 2026 replacement guidance advertises approximate installed prices:

- basic heating/cooling replacement: **€2,000–€2,500**
- premium: **€2,500–€3,500**
- multisplit: **€3,500–€5,500**
- removal/recycling: **€690**
- fault diagnosis: **€210**
- maintenance wash: **€280**

Source:
https://aaltoair.fi/artikkelit/ilmalampopumpun-vaihto-vanhan-tilalle

A €210 diagnostic is only about:

- **10.5%** of a €2,000 replacement
- **6.0%** of a €3,500 replacement

That does not prove willingness-to-pay, but it creates sensible economics for a high-quality **repair-vs-replace + successor-specification** step.

---

## 7. The real compatibility problem is granular, not simply “will it fit?”

AaltoAir documents a useful replacement topology.

Potentially reusable:
- wall penetration
- outdoor-unit bracket/feet
- electrical supply

Often reworked:
- refrigerant piping
- evacuation/pressure testing
- connections
- commissioning

The provider specifically notes that moving from older R410A-era systems to newer refrigerants may require pipe replacement or specialist cleaning because oil/contamination can damage the successor.

This independently replicates the earlier ventilation finding.

### `LEGACY_INTERFACE_LOCK_IN` → **REPLICATED_STRONGLY**

Refined version:

> **Every embedded legacy interface has its own reuse probability. Replacement intelligence is the job of mapping which interfaces survive and which force rework.**

Ventilation:
old duct geometry → successor choice.

Heat pump:
wall opening + electrical + brackets + refrigerant line → successor/install complexity.

This is much more specific than generic “compatibility is hard.”

---

## 8. Warranty is again heterogeneous

Current Finnish examples:

### Daikin
- normal consumer heat-pump warranty: **3 years**
- selected registered Stand By Me units: **5 years**
- digital device/service history and maintenance reminders.

Source:
https://www.daikin.fi/fi_fi/takuu.html

### Toshiba
- AAHP factory: generally **2 years**, some models 3
- air-to-water: **4 years**
- optional protection can extend AAHP risk cover to **9 years**, AWHP to **10**.

Source:
https://www.toshibasuomi.fi/tuotteen-valinta/turva/

### Panasonic
- compressor material warranty: **5 years**
- eligible Pro Partner installation: **5-year full warranty**
- optional insurance can continue from year 6 through age **14 years**.

Source:
https://www.aircon.panasonic.eu/FI_fi/happening/takuu-ja-vakuutus/

### Mitsubishi / Scanoffice
Current 2026 warranty terms vary by exact product/model, with selected products at three or five years and some compressor material coverage in later years.

Source:
https://scanoffice.fi/wp-content/uploads/2026/03/scanoffice_takuuehdot_010226_taytettava.pdf

Conclusion:

> **There is no useful “Finnish heat-pump warranty = N years” field.**

It must remain model/cohort/channel specific.

---

## 9. Independent service is open — generic maintenance is not the goldmine

Observed current offers:

| Provider | Advertised service price |
|---|---:|
| Fin Lämpötekniikka | from €199 |
| Hesatek basic maintenance/repair | €220 |
| Scanoffice guidance | from €250 |
| AaltoAir full maintenance | €280 |
| Hesatek deep service | €329 |

Sources:
https://www.finlt.fi/ilmalampopumppu/ilmalampopumpun-huolto/  
https://hesatek.fi/pages/ilmalampopumpun-perushuolto-korjaus  
https://scanoffice.fi/ilmalampopumput/huolto/  
https://aaltoair.fi/ilmalampopumpun-huolto

Several explicitly service all common brands, including equipment they did not originally sell.

Meanwhile brand/importer networks such as Scanoffice also provide postcode/address-based authorised-service discovery.

So Finland is not OEM-closed.

But ordinary maintenance is already mature and easy to purchase.

### HOLD:
generic heat-pump servicing marketplace.

### INVESTIGATE STRONGLY:
**legacy model → repair or replace → successor model → interface/refrigerant compatibility → installer quotes.**

---

## 10. Regulation is important, but not in the naive way

EU Regulation 2024/573 creates future bans on placing certain new F-gas heat-pump equipment on the market.

For small split systems:

- air-to-water ≤12 kW using F-gases with GWP ≥150: **1 Jan 2027**
- air-to-air ≤12 kW using F-gases with GWP ≥150: **1 Jan 2029**
- split systems ≤12 kW using fluorinated greenhouse gases: **1 Jan 2035**, subject to safety exceptions.

Source:
https://eur-lex.europa.eu/eli/reg/2024/573

R32 has GWP 675, so the 2029 successor-market transition is particularly relevant to common air-to-air equipment.

But GoldProbe explicitly **rejects**:

> “Your existing R32 heat pump becomes illegal in 2029.”

These are product-placement restrictions, not by themselves forced retirement dates for already-installed household systems.

### New candidate: `POLICY_CONSTRAINS_SUCCESSOR_NOT_LEGACY_USE`

Regulation changes **what you should replace the unit with**, not necessarily **when the old unit must die**.

That distinction is extremely valuable for any regulated installed base.

---

## 11. Licensed work is part of the moat

Tukes states that installation, maintenance, repair, decommissioning, leak testing and refrigerant recovery on relevant F-gas/hydrocarbon systems require appropriate refrigeration qualifications.

Source:
https://tukes.fi/fi/tuotteet-ja-palvelut/kylmaala/henkilopatevyydet-ja-patevyysvaatimukset

So the intermediary cannot just route to “a handyman.”

The supply graph can be filtered against qualified businesses.

That makes correct routing more valuable while keeping the commercial channel open.

---

## 12. B08 strongly strengthens the multi-clock model

B07 solar clocks:
- warranty
- technical age
- installer survival
- policy
- compatibility.

B08 adds:
- **weather/performance shock**
- physical interface
- refrigerant transition
- seasonal installer capacity
- household macro confidence.

The better structure is:

```text
latent installed cohort
        |
        v
   readiness state
        |
   +----+-----+----------+-----------+
   |          |          |           |
 failure    weather    policy     economics
   |          |          |           |
   +----------+----------+-----------+
                     |
                 transaction
                     |
         successor constraints
```

This is a much better market model than “installed base × age.”

---

## 13. Exact business cell

### Finnish Legacy Heat-Pump Replacement Passport

Input:
- photo/nameplate
- postcode
- install year if known
- old model
- symptoms
- current refrigerant
- house size/heating role
- existing pipe route / wall penetration / electrical supply
- desired cold-weather performance.

Output:

1. estimated warranty/service status
2. repair vs replace path
3. likely parts availability
4. exact current successor candidates
5. which old interfaces can probably be reused
6. refrigerant-transition implications
7. expected installation scope
8. three normalized licensed-installer quotes
9. future-regulation compatibility of the successor.

This is substantially more defensible than `heatpumpaccessories.fi`.

---

## 14. What B08 falsified

**Falsified:** warranty expiry alone predicts replacement.

**Falsified:** F-gas dates automatically force existing household pumps to be replaced.

**Falsified:** routine maintenance is obvious whitespace.

**Supported:** a large aged cohort is now producing a genuine replacement market.

**Supported:** physical/refrigerant compatibility creates non-trivial replacement work.

**Supported:** multiple independent clocks interact.

**Supported directionally:** an exogenous winter shock can activate cohort-ready replacement demand.

---

## 15. Cross-probe promotions

### `LEGACY_INTERFACE_LOCK_IN`
**REPLICATED_STRONGLY**

Now independently seen in:
- legacy ventilation replacement
- heat-pump replacement.

### `MULTI_CLOCK_AFTERMARKET_TRIGGER`
**REPLICATED_DIRECTIONALLY**

Now independently seen in:
- Dutch solar inverter aftermarket
- Finnish heat-pump replacement.

It still needs a third sector before I would treat the exact formulation as mature.

---

## 16. Search data

Authenticated Keyword Planner monthly volume: **null**  
CPC: **null**

No SEO-tool estimates substituted.

---

## 17. Autonomous next probe — B09 Australia residential pool equipment

B08 created a more specific hypothesis:

### `COHORT_READY_SHOCK_ACTIVATION`

Australia pools are selected because they provide a very different asset ecosystem with:
- mature installed base;
- affluent owners;
- high-load hot-weather periods;
- pumps/chlorinators/controllers with model-specific failures;
- deep parts/service market;
- routine maintenance likely already commoditized.

B09 will test:

> **Does an extreme-use/climate period activate latent failures/replacements in ageing pool equipment, while the higher-value whitespace sits in rapid model-specific diagnosis/replacement rather than routine cleaning?**

This directly attempts to falsify the B08 shock-activation mechanism outside heating.

