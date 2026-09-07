# [GoldProbe B04] Singapore Residential AC — schema hardening + full evidence report

# GoldProbe B04 — Singapore Residential Air-Conditioning
**Date:** 2026-09-07  
**Method:** research-native GoldProbe 2.1  
**Score:** deliberately disabled — no naked scores  
**Core verdict:** HOLD generic diagnostic/servicing middleman; INVESTIGATE NARROW tenancy/property-management orchestration.

## 1. Schema peer review: what changes now

The downstream schema is directionally excellent: it forces time-series, competition, search, regulation, supplier availability, problem types, hypotheses and falsifiers. The danger is that its neat numeric fields encourage false precision.

The rules for all future probes are now:

- A numeric score is `null` unless a versioned formula can reconstruct it from cited metrics.
- A confidence number is not accepted unless its formula is explicit. Source class/directness/comparability/recency are stored instead.
- `households using`, `current device stock`, `cumulative installs`, `registered systems`, `annual sales`, and `installed units` are different datatypes.
- A legal/contractual service requirement is **not** an observed maintenance probability of 1.0.
- Prices are atomic observations with provider, service, units, tax/transport conditions and timestamp. Premiums/discounts are derived from exact observation IDs.
- Competitive seller counts are query snapshots, never market censuses.
- Search volume/CPC remains null without an authenticated source.
- Failure rates remain null without a cohort/repair dataset.
- Revenue/lead and conversion are experiment assumptions, not market facts.
- One probe creates mechanism **candidates**; independent replication is required before promotion to a recurring pattern.

The human report is intentionally broad and readable. BigQuery should contain deterministic extractions from the evidence, not compressed analyst guesses.

## 2. Why Singapore AC was selected

B03 France pellet heating showed a measurable seasonal capacity premium and a diagnostic-vs-dispatch wedge. Singapore is the clean counterfactual: year-round hot/humid cooling demand, enormous equipment penetration, but no winter heating season and very compact geography.

**Hypothesis:** recurring maintenance can exist without seasonal scarcity, but dense geography will commoditize ordinary dispatch. Value should migrate toward trust, service records, contractual compliance, and exceptional-time availability.

## 3. Hard installed-base / demand-side evidence

Singapore Department of Statistics' HES 2023 reports household air-conditioner ownership rising:

| HES period | Households with AC |
|---|---:|
| 2012/13 | 76.1% |
| 2017/18 | 79.7% |
| 2023 | **81.9%** |

The same report says the lowest-income 20% reached **64.4%** AC ownership in 2023, while HDB 1–2 room households reached **32.6%**. This is not merely a luxury-owner ecosystem.

Official resident-household count for 2023: **1,425,100**. Multiplying by 81.9% gives a transparent proxy of approximately **1,167,157 resident households with AC**. This is a household proxy, not an indoor-unit count.

Sources:
- Singapore HES 2023: https://www.singstat.gov.sg/-/media/files/publications/households/hes2023.ashx
- Resident households: https://www.singstat.gov.sg/publications/reference/ebook/households/households

## 4. Climate removes the winter-season variable

Meteorological Service Singapore describes high and relatively uniform temperature and humidity throughout the year. The 1991–2020 normals show about **82% mean annual relative humidity**; 24-hour monthly mean temperature ranges only from roughly **26.8°C to 28.6°C**.

Source: https://www.weather.gov.sg/climate-climate-of-singapore/

This matters experimentally: if recurring AC economics are strong here, they cannot be attributed to a short heating season.

## 5. Official maintenance guidance vs vendor claims

Current NEA guidance says:
- check the filter about monthly;
- service AC regularly;
- have it inspected annually.

It does **not**, on the current page, itself impose quarterly servicing.

Source: https://www.nea.gov.sg/our-services/climate-change-energy-efficiency/energy-efficiency/household-sector/energy-saving-tips

That produces an important data-quality lesson: vendor pages claiming “NEA recommends every 3 months” should not be promoted to official guidance without checking the primary source.

## 6. The surprise forcing function: tenancy contracts

The Council for Estate Agencies' private-residential tenancy template contains a much stronger quarterly mechanism: it says the tenant should take up a service contract with a qualified AC contractor and service the units **at least once every three months**, keep the system maintained, and provide service records/receipts when requested.

CEA also explicitly says its tenancy templates are guides and parties are free to negotiate terms. Therefore this is **contractual**, not universal statutory, demand.

Source: https://www.cea.gov.sg/docs/default-source/default-document-library/tenancy-agreement-template-for-private-residential-property-2021.pdf

This is not just boilerplate. A 2026 Small Claims Tribunals decision reproduced a real lease requiring servicing at least every three months and examined whether the tenant had complied.

Source: https://www.elitigation.sg/gdviewer/s/2026_SGSCT_21

That gives us a new mechanism candidate: **PRIVATE_CONTRACT_SERVICE_CLOCK**.

## 7. Recurring customers receive discounts, not convenience premiums

I held provider and fan-coil count constant and compared one-time routine service with four-visit annual contracts.

| Provider | Units | One-time | Quarterly annual | Per visit | Contract discount |
|---|---:|---:|---:|---:|---:|
| LK Brothers | 3 | S$76.30 | S$234.35 | S$58.59 | 23.2% |
| Cool Aircon | 4 | S$90.00 | S$345.00 | S$86.25 | 4.2% |
| Tech-V Air Conditioning | 3 | S$90.00 | S$264.00 | S$66.00 | 26.7% |
| SunMec Engineering | 3 | S$60.00 | S$210.00 | S$52.50 | 12.5% |
| Hey Aircon | 3 | S$75.00 | S$260.00 | S$65.00 | 13.3% |
| StringsSG | 3 | S$73.46 | S$279.16 | S$69.79 | 5.0% |

Across these six same-provider pairs:

- median per-visit discount: **12.9%**
- mean discount: **14.2%**
- range: **4.2%–26.7%**

These are advertised prices, not transaction/conversion data. But they falsify a simplistic “recurring convenience = consumer pays a premium” assumption.

The supplier is often paying for recurrence through a discount because recurrence creates:
- scheduled demand,
- lower reacquisition cost,
- customer lock-in,
- repair upsell opportunity,
- predictable technician utilization.

This creates mechanism candidate **RECURRENCE_BOUGHT_WITH_DISCOUNT**.

Source pages are preserved in the JSON for every pair.

## 8. Dense geography appears to crush ordinary dispatch friction

Several independent providers price routine travel very lightly:

- aircons.sg: standard transport included, same standard-hour prices on weekends, only S$10–20 restricted parking; after-hours 10pm–7am adds S$50.
- Cool Aircon: no call-out or out-of-area surcharge, no weekend/public-holiday surcharge; troubleshooting S$50–80 and waived if repair proceeds.
- LK Brothers: troubleshooting S$43.60 including GST and transportation.
- Newway: S$10 surcharge for CBD/Sentosa/Jurong Island; otherwise package pricing dominates.

This does **not prove geography causes the low travel price**. It does show that in this market ordinary dispatch is commonly bundled while exceptional **time/access** carries explicit pricing.

That is the opposite of the France pellet probe, where scarce seasonal field capacity was a meaningful part of the economic wedge.

## 9. OEM service vs independent service

Mitsubishi Electric Asia currently lists room-AC evaluation from **S$140**, excludes spare parts and adds **S$45 transport**, so the minimum displayed evaluation+transport is S$185 before parts. Independent troubleshooting offers observed in this run cluster around roughly S$40–80 and are often waived on repair.

Offered-price gap:

- S$185 / S$80 = **2.31×**
- S$185 / S$40 = **4.63×**

This comparison has scope/brand-specialization differences, so it is not a controlled test. But it is strong evidence that the independent service channel is economically open.

Source: https://www.mitsubishielectric.com.sg/service-charges/

## 10. Competition is already ferocious

A structured local-business search snapshot returned 20 relevant Singapore AC servicing/repair businesses.

Snapshot summary:
- sample size: **20**
- median review count: **1,230**
- mean review count: **2,192.7**
- **13/20** have at least 1,000 reviews
- **6/20** have at least 2,000
- **2/20** exceed 10,000
- median rating: **4.9/5**

This is not “20 sellers in the market”. It is a timestamped top-result sample. But it is excellent evidence that customer acquisition is not an empty local-search field.

## 11. Incumbents already digitize the obvious recurring wedge

StringsSG offers annual packages with rescheduling, account tracking, downloadable PDF service records and support. Newway offers recurring plans, automated follow-up/reminders and a customer portal with service records.

Sources:
- https://www.stringssg.com/sg/aircon-servicing-singapore/annual-package
- https://newway.sg/aircon-servicing-package/

So “aircon reminder + proof of service” by itself is **not whitespace**.

The narrower possible wedge is B2B:
- landlord with 20 units,
- property manager with hundreds,
- relocation provider,
- tenancy compliance across multiple contractors/properties.

That requires a different buyer and integration strategy.

## 12. Hong Kong comparator: dense cooling markets can also aggregate

Hong Kong EMSD reports air conditioning's share of residential electricity increasing from **33% in 2013 to 40% in 2023**.

Source: https://www.emsd.gov.hk/filemanager/en/content_762/HKEEUD2025.pdf

Toby's live AC-cleaning marketplace page displays:
- **38,189** window-AC cleaning sales,
- **6,056** split-system cleaning sales,
- **2,697** cassette cleaning sales.

These are platform-displayed counters with unknown period/methodology, so treat them as a commercial transaction proxy, not official market totals.

Source: https://www.hellotoby.com/en/ds/air-conditioning-cleaning

This supports the control result: dense, recurring cooling service does not remain fragmented forever. Platforms or strong service brands can capture it.

## 13. Hypothesis result

### Supported
1. Recurring maintenance economics exist with essentially no winter heating season.
2. Recurrence can be created by private tenancy contracts as well as regulation.
3. In a compact, heavily supplied market, routine dispatch is often bundled/cheap.
4. Time scarcity (after-hours) still commands a premium.
5. Recurring service is valuable enough that firms discount the individual visit to acquire the relationship.

### Falsified / weakened
1. **Huge installed base does not imply a good diagnostic-middleman opportunity.**
2. High channel openness is not monotonically good.
3. Generic digital scheduling/records are already incumbent features.
4. “People pay more for convenience” is too crude: here convenience is often bundled **with a discount**.

## 14. New mechanism candidates — not patterns yet

### MC-RECURRENCE-BOUGHT-WITH-DISCOUNT
Six matched providers show a median **12.9%** recurring-contract discount per visit.

### MC-PRIVATE-CONTRACT-SERVICE-CLOCK
A standard industry/government-supported tenancy template creates quarterly servicing + documentation demand, and a 2026 court case demonstrates the clause exists in real disputes.

### MC-ROUTINE-DISPATCH-COMMODITIZATION
Routine transport is commonly included; after-hours and access constraints carry the surcharge. Causality from urban density is not proven yet.

## 15. Cross-probe hypothesis generated

We now have three useful channel states:

- **Austria pellet:** relatively closed / OEM captured → weak independent whitespace.
- **France pellet:** fragmented enough for a narrow capacity/diagnostic wedge.
- **Singapore AC:** extremely open and competitive → routine routing commoditized.

This generates, but does **not prove**, the hypothesis:

> **Independent intermediary whitespace may follow an inverted-U with channel openness: too closed is OEM-owned; too open is commodity competition; intermediate fragmentation may be optimal.**

This is now the most valuable thing to test.

## 16. Search-demand fields deliberately left null

No authenticated Google Keyword Planner / Google Ads data was available in this run. Therefore:
- monthly search volume: `null`
- CPC: `null`

No SEO-blog estimate was substituted.

## 17. Next probe selected autonomously

### B05 — Ireland domestic wastewater / septic systems

Why: it has official installed-base, inspection-failure, grants and geographic data, and is predicted to have **intermediate provider fragmentation**. That makes it an unusually good test of the inverted-U channel-openness hypothesis.

B05 hypothesis:

> Independent intermediary value peaks where homeowners are forced to act, provider selection is fragmented enough to be confusing, but the service market is not so hypercompetitive and digitally mature that routing is already commoditized.

Kill conditions:
- remediation is already captured by a dominant aggregator/provider network;
- official inspection/grant mechanisms prescribe providers tightly;
- provider selection is not actually fragmented;
- inspection failures do not translate into economically reachable consumer demand.

## 18. Bottom line

Singapore AC is a valuable **negative/control**.

The market is enormous: official 2023 ownership is **81.9%**, yielding an approximate **1,167,157-household** AC ownership proxy. But incumbent service supply is so dense and digitally mature that basic routing, recurring scheduling, records and low-cost diagnosis are already heavily served.

The high-signal opportunity, if any, is not another consumer aircon marketplace. It is narrower B2B orchestration around tenancy/property portfolios.

And the more important orchard-level insight is that **channel openness may have an optimum rather than a monotonic relationship with opportunity**. B05 is selected specifically to test that.
