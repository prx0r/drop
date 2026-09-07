# GoldProbe B12 — UK Post-Flood Property Resilience / Build Back Better

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Does a major insured loss unlock a temporary prevention budget and create a distinct high-intent retrofit market?

## Executive result

**Yes — strongly.**

UK Build Back Better (BBB) creates exactly that market.

After an eligible flood claim, participating insurers can fund **up to £10,000 above ordinary reinstatement** for property flood resilience.

More than **70% of the UK home-insurance market** is currently committed to offering BBB.

Yet Flood Re reports take-up at only **around one third of households offered it**.

So this is not a demand-without-money problem.

It is:

> **funded intent + weak conversion + claim gatekeeper + small specialist supply chain**

That is an unusually interesting middleman structure.

---

## 1. The risk denominator

The Environment Agency's latest National Flood Risk Assessment says around **6.3 million homes and businesses in England** are in areas at risk from flooding.

As of 31 March 2025:

River/sea:
- high risk: **367,900**
- medium: **323,300**
- low: **966,500**

Surface water:
- high: **1,071,800**
- medium: **884,800**
- low: **2,644,000**

Source:
https://www.gov.uk/government/publications/flood-and-coastal-risk-management-national-report/flood-and-coastal-erosion-risk-management-report-1-april-2024-to-31-march-2025

Do not sum those rows: properties can face multiple flood sources.

The EA says climate change could push total properties at risk toward **8 million by mid-century**.

Source:
https://environmentagency.blog.gov.uk/2025/01/28/enhancing-flood-and-coastal-erosion-risk-digital-services-with-the-latest-data-and-mapping/

---

## 2. The claim creates a new budget

GOV.UK explicitly tells flooded homeowners:

> if their insurer participates in Build Back Better, they may receive **up to £10,000** for future flood-protection measures as part of flood repairs.

Source:
https://www.gov.uk/prepare-for-flooding/get-insurance

Flood Re clarifies:
- it is above ordinary repair/reinstatement cost;
- the insurer and customer decide suitable measures;
- a property survey can be funded;
- customers do **not necessarily receive the full £10k**;
- each insurer has its own limits/criteria.

Source:
https://www.floodre.co.uk/faq/who-decides-what-to-spend-the-additional-up-to-10000-on/

That is exactly B11's `LOSS_EVENT_UNLOCKS_PREVENTION_BUDGET` mechanism in a second distinct context.

---

## 3. The budget is economically meaningful

Flood Re reports recent average household flood claims around **£60,000–£90,000**, depending on the event, with alternative accommodation a major component.

Source:
https://www.floodre.co.uk/ara-2025/transition/

The maximum £10,000 BBB budget is therefore roughly:

- **11.1%** of a £90k average claim
- **16.7%** of a £60k average claim.

This isn't customer WTP and isn't the cost-effectiveness ratio.

It shows the order of magnitude of the insurer-funded incremental resilience budget.

---

## 4. Insurer coverage is broad

Flood Re's 2026 annual-report statistics say **over 70% of the UK market** has committed to offer BBB.

Source:
https://www.floodre.co.uk/ara-2026/key-stats/

The prior 2024-25 report gave **77% of the market**, with **346,200 Flood Re policies** that year.

Source:
https://www.floodre.co.uk/ara-2025/key-stats/

The 2025 FloodReady review says **12 major insurers** accounted for around 77% of the residential home-insurance market.

Source:
https://www.gov.uk/government/publications/floodproof-an-action-plan-to-build-resilience/floodready-an-action-plan-to-build-the-resilience-of-people-and-properties

So availability itself is no longer the main problem.

---

## 5. And yet take-up is only around one third

Flood Re reports BBB household take-up at **around one third of those offered**.

Source:
https://www.floodre.co.uk/ara-2025/transition/

That means, approximately, **two out of three people who are already at the point of an insured flood claim and are offered resilience still don't take it up.**

The source doesn't publish a precise raw denominator, so this remains an approximate conversion statistic.

This is extraordinary.

The customer:
- has just flooded
- is rebuilding anyway
- has insurer money available
- knows the risk is real.

And conversion is still low.

That is not ordinary marketing friction.

---

# 6. FloodReady effectively tells us where the funnel breaks

The 2025 government/EA FloodReady review explicitly calls for:

- clearer communication **at the point of claim**
- better signposting
- claims-handler/loss-adjuster training
- improved procurement
- improved tracking/reporting
- clearer registers of trusted products/professionals
- stronger quality assurance.

It also says early BBB feedback identified **procurement delays** and concerns about aesthetics.

Source:
https://www.gov.uk/government/publications/floodproof-an-action-plan-to-build-resilience/floodready-an-action-plan-to-build-the-resilience-of-people-and-properties

This is close to a government-authored product requirements document.

---

## 7. The market itself is tiny relative to the risk pool

Flood Re's 2023 Property Flood Resilience Market Study estimated:

- total manufacturer/installer turnover: **£20–25m/year**
- residential: **£13–16m**
- commercial/institutional: **£7–9m**
- just over **40 manufacturers**
- roughly **10–20 specialist installers**
- more than **two-thirds** of those firms had fewer than 20 employees.

The study was based primarily on **44 industry interviews**.

Source:
https://www.floodre.co.uk/wp-content/uploads/20759_Flood_Re_PFR-Report_2023.pdf

This is a 2023 structural estimate, not a 2026 census.

But the 2025 FloodReady review independently still describes the PFR market as small and needing mainstream adoption.

---

## 8. Supply has explicit event-spike constraints

That same market study found:

- more than **500 homes/year** had PFR installed in recent years, mostly via public schemes;
- large residential demand was primarily **post-event**;
- installers reported ability to scale by roughly **20–40% within 2–4 months**;
- manufacturers reported around **20% additional capacity**, generally with a hard cap beyond that;
- firms had little incentive to scale without guaranteed contracts/demand.

This produces:

### `EVENT_GATED_SUPPLY_MARKET`

```text
normal year
→ weak demand
→ small specialist industry

major flood
→ sudden funded demand
→ local procurement surge
→ limited certified supply
→ bottleneck / quality risk
```

That market shape is extremely different from Singapore AC.

---

## 9. Historical grant waves attracted low-quality entrants

The Flood Re market study is unusually candid.

Earlier post-flood grant programmes sometimes attracted under-specialized “cowboy” providers because money appeared quickly in stressed communities before robust standards existed.

The consequence was poor installation and damaged consumer trust.

Modern frameworks respond with:
- PFR Code of Practice
- BSI/KIWA certification
- supplier competence requirements.

Source:
https://www.floodre.co.uk/wp-content/uploads/20759_Flood_Re_PFR-Report_2023.pdf

This suggests that **trust becomes most valuable exactly when event-driven demand spikes**.

---

## 10. Certification itself constrains supply

FloodReady says the current EA supplier framework requires:
- supplier competence/training against the CIRIA PFR Code of Practice;
- products with BSI Kitemark or equivalent certification.

It says relatively few products have successfully passed the certification regime and notes that testing/certification can be costly for small firms.

Source:
https://www.gov.uk/government/publications/floodproof-an-action-plan-to-build-resilience/floodready-an-action-plan-to-build-the-resilience-of-people-and-properties

So “show me the cheapest flood door” is the wrong product.

The correct data layer is:

```text
property flood path
→ professional survey
→ appropriate resistance/recoverability measures
→ certified product
→ competent installer
→ insurer acceptance
→ evidence record
```

---

## 11. Mechanism: CLAIM_GATEKEEPER_CONTROLS_FUNDED_DEMAND

This is distinct from the Australian pool finding.

Australia:
> installer/pool shop influences which replacement product is selected.

B12:
> the **claims handler/loss adjuster controls whether the customer meaningfully enters a funded market at all.**

Flood Re is now creating dedicated training for claims-management professionals.

Source:
https://www.floodre.co.uk/ara-2026/transition/

So the customer-acquisition channel is probably not:

`Google → flooded homeowner`

It is:

`insurer / loss adjuster / recovery contractor → homeowner`

That dramatically changes GTM.

---

## 12. Best business cell

### BBB Resilience Orchestration Layer

Triggered at claim acceptance.

Input:
- address
- flood source/depth
- insurer
- policy/BBB rules
- damaged parts already being replaced
- property construction
- previous floods.

Workflow:

1. determine BBB eligibility / insurer limit
2. book compliant survey
3. generate resilience specification
4. show only certified/appropriate products
5. locate available competent installers
6. normalize quotes
7. attach spend to insurer claim
8. record final installed measures
9. produce insurer/FPC-ready evidence.

This is much more defensible than a flood-door webshop.

---

## 13. The next data layer is already being created

Flood Re says Flood Performance Certificate pilots begin around the **end of 2026**, with further testing in 2027.

The proposed standardized data covers:
- flood risk
- property characteristics
- installed resilience measures
- supporting evidence.

Potential use cases include:
- Environment Agency schemes
- Build Back Better
- wider housing market
- potentially new builds.

Source:
https://www.floodre.co.uk/ara-2026/transition/

This creates candidate:

### `RESILIENCE_EVIDENCE_FINANCIALIZATION`

If verified resilience evidence eventually influences:
- insurance premium
- mortgage/lender decision
- property transaction
- eligibility

then the **record of installed mitigation becomes a financial asset**.

Too early to call it a pattern, but very high option value.

---

## 14. B12 strongly replicates B11

### `LOSS_EVENT_UNLOCKS_PREVENTION_BUDGET`
**REPLICATED STRONGLY**

B11:
covered water loss >£7.5k
→ Direct Line contributes up to £500 leak detection.

B12:
eligible insured flood
→ participating insurer contributes up to £10,000 PFR.

Refined statement:

> **A sufficiently costly insured loss can create a temporary third-party-funded retrofit window during recovery.**

The window itself is a market event.

---

## 15. Why B12 is commercially interesting despite low current turnover

Normally:

small £20–25m specialist market
→ probably ignore.

But the causal graph says:

- risk stock: millions
- insurer offer coverage: >70%
- claim budget: up to £10k
- adoption: only ~1/3 of offered
- supply: small/certification-constrained
- government/industry explicitly want to scale it.

That isn't “small demand.”

It looks more like a **conversion/supply-chain constrained market**.

Very different.

---

## 16. What B12 falsified

**Falsified:** no money exists for resilience.

**Falsified:** insurer adoption is the core bottleneck.

**Falsified:** product ecommerce is sufficient.

**Supported:** claims process controls acquisition.

**Supported:** specialist supply is constrained.

**Supported:** post-event demand creates capacity problems.

**Supported strongly:** the loss event can unlock funded betterment.

---

## 17. Autonomous next probe — B13 US hail/storm roofing

Why move there?

We now have:

### `EVENT_GATED_SUPPLY_MARKET`
and
### `CLAIM_GATEKEEPER_CONTROLS_FUNDED_DEMAND`

US hail/storm roofing is an excellent stress test because it is one of the world's most developed insurance-funded, event-driven repair markets.

Hypothesis:

> **Event-funded demand can become so mature and contractor-saturated that the exact mechanism which creates huge spend destroys neutral middleman whitespace.**

If true, it gives GoldProbe another inverted-U:

```text
too little event demand → no market
moderate funded demand → coordination opportunity
massive mature funded demand → storm-chasing / saturated contractor CAC
```

B13 will test:
- claims volumes
- roof replacement cost
- insurer/adjuster control
- contractor surge
- post-storm price/supply friction
- licensing/consumer-protection rules
- whether trusted verification/scope normalization still has whitespace.
