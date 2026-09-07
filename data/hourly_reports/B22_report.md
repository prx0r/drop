# GoldProbe B22 — France DPE / Audit / RGE Open Retrofit Graph

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**B22 strongly validates the value of open regulatory asset data — but falsifies the naive idea that an open asset ledger automatically creates an open lead database.**

France currently exposes an unusually complete public retrofit-intelligence stack:

1. **15,512,658 existing-home DPE records**, updated weekly, Open Licence 2.0.
2. **3,237,797 audit-data records**, updated weekly, with a standardized audit model, >250 tabular fields, API and full anonymized database dump.
3. **161,603 current RGE qualification records**, updated daily, plus a **5.69m-record qualification history since 2014**.
4. Known legal rental/sale deadlines.
5. A €3.6bn 2026 MaPrimeRénov budget and real completed-work flow.

Sources:
https://data.ademe.fr/datasets/dpe03existant
https://data.ademe.fr/datasets/audit-opendata
https://data.ademe.fr/datasets/liste-des-entreprises-rge-2
https://data.ademe.fr/datasets/historique-rge

This is close to a public graph of:

```text
PROPERTY
  ↓
CONDITION / EQUIPMENT / ENERGY LABEL
  ↓
REGULATORY CLOCK
  ↓
AUDIT / RECOMMENDED SCENARIO
  ↓
QUALIFIED LOCAL SUPPLY
```

But two major corrections matter:

**A. A label can change without the building changing.**

**B. Open data does not imply permission or ability to cold-contact the owner.**

Those are the most valuable B22 findings.

---

# 1. The raw DPE data asset is genuinely enormous

ADEME's existing-home DPE dataset currently contains **15,512,658 records**, updated **2 September 2026**, France-wide, under **Open Licence 2.0**, with API and database access.

The records contain building/property characteristics including:
- surface
- orientation
- walls/windows/materials
- heating
- hot water
- ventilation
- energy consumption
- GHG.

Source:
https://data.ademe.fr/datasets/dpe03existant

The live API exposes far more than a label. A current sample includes:
- normalized BAN address
- BAN identifier
- coordinates
- construction period
- building type
- heating energy
- exact heating-generator descriptions
- DPE/GES class
- consumption
- energy-cost fields
- visit/establishment/expiry dates.

API:
https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines?size=1

So this is a legitimate installed-property intelligence layer.

---

# 2. Do not call 15.5m records “half of French homes covered”

ADEME explicitly warns that raw DPE data is **not representative of the housing stock**.

A DPE is primarily triggered by:
- sale
- rental
- new construction.

Properties without those events may be absent.

There may also be multiple DPE records over time.

ADEME says national prevalence requires reweighting using other housing datasets such as Fidéli and heating distributions.

Source:
https://data.ademe.fr/datasets/dpe03existant

This distinction is critical:

```text
DPE RECORD COUNT
≠
UNIQUE CURRENT PROPERTIES
≠
REPRESENTATIVE NATIONAL STOCK
```

GoldProbe must preserve all three meanings separately.

---

# 3. The observatory itself shows the throughput

As of **23 August 2026**, ADEME's observatory reported:

- **17,485,060 total DPE**
- **16,924,578 housing DPE**
- **246,855 DPE in July 2026**.

Source:
https://observatoire-dpe-audit.ademe.fr/statistiques

The 15.512m existing-home dataset is a different scope and later update.

They are stored separately.

---

# 4. France also publishes the prescriptive layer: energy audits

This is where B22 becomes especially interesting.

ADEME's audit dataset currently reports **3,237,797 records** and is updated weekly.

The audit's explicit purpose is to propose **renovation scenarios**.

The open system offers:
- >250 tabular fields
- filters/exports
- API
- full anonymized PostgreSQL dump
- full audit detail through XML/XLS lookup.

Source:
https://data.ademe.fr/datasets/audit-opendata

Since October 2023, regulatory and incentive audits have converged on a standardized model.

That means the public system has both:

```text
CURRENT ASSET STATE
```

and

```text
PROPOSED BETTER STATE
```

at enormous scale.

---

# 5. But this is recommendation data, NOT realized transaction data

This becomes an explicit GoldProbe rule.

The audit tells us what a qualified professional proposed.

It does **not** prove:
- quote accepted
- finance obtained
- contractor selected
- work begun
- work completed.

So:

## `DIAGNOSIS_RECOMMENDATION_OUTCOME_MUST_BE_SEPARATE`

BigQuery should distinguish:

```text
diagnosis
recommendation
application
funding commitment
work start
completion
post-work verification
```

If we collapse those into one “renovation event,” agents will hallucinate conversion rates.

---

# 6. The actual adjusted housing stock is already quantified separately

SDES's adjusted national estimate for **1 January 2025** gives:

**30.9m main residences**

DPE distribution:
- A 3.3%
- B 5.3%
- C 27.2%
- D 33.7%
- E **17.8%**
- F **7.9%**
- G **4.8%**.

Source:
https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-performance-energetique-au-1er-janvier-2025

That corresponds mechanically to roughly:

- E: **5,500,200**
- F: **2,441,100**
- G: **1,483,200**
- E/F/G: **9,424,500**

under that Jan-2025 model.

SDES directly reports F/G as around **3.9m**, 12.7%.

Private rental:
- **13.8% F/G**
- about **1.1m private-rental F/G homes**.

This is a much better prevalence denominator than counting raw open-data rows.

---

# 7. France has hard future transaction clocks

Rental energy-decency minimum:

- **2025:** at least F
- **2028:** at least E
- **2034:** at least D.

Source:
https://www.ecologie.gouv.fr/politiques-publiques/location-gel-loyers-passoires-energetiques

This means the same open asset record can be evaluated against known future dates.

Conceptually:

```text
address
× current DPE
× tenure/use if known lawfully
× future date
→ regulatory risk state
```

That is much more useful than generic keyword demand.

---

# 8. Sale events create an even richer audit trigger

For qualifying monoproperty sales:

- F/G audit obligation since **1 Apr 2023**
- E since **1 Jan 2025**
- D from **1 Jan 2034**.

Source:
https://www.ecologie.gouv.fr/politiques-publiques/audit-energetique-reglementaire

So a low-performing property placed for sale can produce:

```text
DPE
→ mandatory audit
→ proposed work scenarios
→ prospective buyer receives audit
```

This is a pre-transaction renovation-intelligence event.

---

# 9. Then B22 finds the dangerous trap: the label itself is mutable policy

This is probably the most important statistical finding in the probe.

SDES says F/G main residences fell by roughly **327,000** between Jan 2024 and Jan 2025.

But **nearly 40% of that decrease was attributable to the reform of DPE calculation for small surfaces**.

Source:
https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-performance-energetique-au-1er-janvier-2025

A large apparent improvement in the installed base happened because **the measuring rule changed**.

Not necessarily because walls were insulated or boilers replaced.

---

# 10. The 2026 electricity reform creates an even larger synthetic migration

France changed the electricity primary-energy conversion factor:

**2.3 → 1.9** from 1 January 2026.

The Ministry estimated this would remove about **850,000 homes**, mainly electrically heated, from F/G status using the **1 January 2023 stock baseline**.

No physical renovation was required.

Older post-July-2021 DPEs remain legally valid and owners can obtain an updated label attestation.

Source:
https://www.ecologie.gouv.fr/actualites/evolutions-du-calcul-du-dpe-reponses-vos-questions

SDES separately simulated the same 2026 reform against its **Jan-2025** stock and estimated F/G would fall from **3.9m to 3.2m**, roughly 700k fewer.

Different baselines.

Both are stored.

They are **not averaged together**.

---

# 11. And the formula changes AGAIN in four months

On **31 August 2026**, the government published the next change.

From **1 January 2027**:

**electricity factor 1.9 → 1.7**.

The government says:
- many electrically heated homes will improve
- none will worsen because of this change
- DPE/audits through 31 Dec 2026 remain valid
- a free immediate updated attestation can be generated without a new visit.

Source:
https://www.ecologie.gouv.fr/presse/dpe-audits-energetiques-publication-larrete-abaissant-facteur-conversion-lelectricite-17-1er

This generates:

# `RULE_CHANGE_MIGRATES_COHORT_WITHOUT_PHYSICAL_CHANGE`

This should become a canonical GoldProbe safeguard.

Never learn:

```text
G → F
```

as a “successful renovation transition” without asking:

```text
physical work?
new diagnostic?
method change?
threshold change?
coefficient change?
administrative correction?
```

This is exactly the sort of subtle graph contamination that would destroy forecasting.

---

# 12. We therefore need two separate states

For every compliance-labelled asset:

### PHYSICAL STATE
- insulation
- windows
- heating
- hot water
- ventilation
- age
- materials.

### REGULATORY CLASSIFICATION STATE
- methodology version
- coefficients
- thresholds
- effective date
- official label.

Then:

```text
same physical state
+
new rule
=
new label
```

is correctly represented as a policy event, not a renovation.

---

# 13. Supply is also open data

ADEME's current RGE register:

- **161,603 qualification records**
- daily updates
- work domains
- qualification/certification information
- map/search
- Open Licence.

Updated **6 September 2026**.

Source:
https://data.ademe.fr/datasets/liste-des-entreprises-rge-2

Do not call these 161,603 unique firms.

ADEME BâtiZoom says there were approximately **55,000 RGE work businesses in 2025**.

Source:
https://batizoom.ademe.fr/indicateurs/nombre-dentreprises-de-travaux-rge

And the historical RGE dataset contains **5,691,110 records since 2014**, including qualification periods and SIRET search.

Source:
https://data.ademe.fr/datasets/historique-rge

So France gives us both sides:

```text
property demand condition
↕
qualified supplier capacity
```

without Google Maps scraping.

---

# 14. This creates a genuinely interesting BigQuery graph

Possible cell:

```text
property/address
  ├── DPE class/current methodology
  ├── heating fuel
  ├── construction age
  ├── energy costs
  ├── audit exists?
  ├── audit scenario
  ├── current legal state
  ├── 2028 legal state
  ├── 2034 legal state
  └── classification-change sensitivity

postcode / commune
  ├── E/F/G density
  ├── audit density
  ├── fossil-heating density
  ├── RGE firms by work domain
  ├── qualification churn
  └── subsidized-renovation activity
```

That is vastly stronger than asking an LLM whether "French heat-pump demand looks good."

---

# 15. But open asset data does NOT mean open homeowner acquisition

The DPE dataset is Open Licence.

That permits reuse subject to the licence.

However, CNIL is explicit that publicly accessible personal data remains personal data and reuse still needs a lawful basis, information/rights handling and GDPR compliance.

Source:
https://www.cnil.fr/fr/recommandations-reutilisateurs-donnees-internet

And the outbound environment just tightened.

As of **11 August 2026**, B2C telephone prospecting generally requires prior consent except specified existing-contract situations.

Electronic B2C prospecting also generally requires prior consent.

Source:
https://cnil.fr/fr/demarchage-commercial

So:

```text
I know this address has DPE G
```

does **not** mean:

```text
I may identify the resident and cold-call them
```

or that this is the highest-ROI GTM.

---

# 16. This produces another precise mechanism

## `OPEN_LEDGER_DOES_NOT_OPEN_CUSTOMER_RELATIONSHIP`

Open data can collapse:

- asset discovery cost
- market sizing cost
- condition inference cost
- locality prioritization cost.

While leaving:

- owner resolution
- consent
- customer trust
- acquisition

expensive or constrained.

That distinction matters enormously for our opportunity formula.

---

# 17. France also increasingly owns the subsidized customer journey

From **17 August 2026**, France Rénov became the single entry point for all Anah aid journeys through a unified France Connect+ account.

Source:
https://www.anah.gouv.fr/presse/compter-du-17-aout-2026-france-renov-renforce-son-offre-de-services-avec-un-compte-personnel

For deep MaPrimeRénov renovation:
- E/F/G eligibility
- minimum 2-class improvement
- up to 80% of €40,000 under current published conditions
- personalized France Rénov adviser meeting required.

Source:
https://france-renov.gouv.fr/aides/maprimerenov-renovation-ampleur

So even though the intelligence graph is open, the publicly financed customer path is becoming more centralized.

Another reason not to equate **information openness** with **channel openness**.

---

# 18. The transaction economics are very large

Current 2026 MaPrimeRénov budget:

**€3.6bn**

with target:
- at least **120,000 deep renovations**
- **150,000 single-measure renovations**.

Source:
https://www.ecologie.gouv.fr/presse/maprimerenov-reouverture-du-guichet-promulgation-loi-finances

At 30 June 2026:
- **110,835 homes renovated**
- **41,409 deep renovations**
- >9,000 applications rejected
- average processing time **6 months**
- 100,240 households advised.

Source:
https://www.anah.gouv.fr/presse/bilan-des-aides-de-l-anah-au-1er-semestre-2026-cap-maintenu-pour-ameliorer-durablement-l

Since 2020:
- 2.9m MPR-renovated homes
- >500k deep renovations
- nearly **€47bn of work generated**.

That is real downstream money, not theoretical TAM.

---

# 19. Best observed transaction-size evidence

Q1 2025 deep-renovation programme:

- **17,178 deep renovations**
- **€1.4bn works**
- €700m public aid
- nearly 80% on F/G properties
- average project: **€59,197**
- average MaPrimeRénov aid: **€41,201**.

Source:
https://www.ecologie.gouv.fr/presse/maprimerenov-valerie-letard-salue-premier-trimestre-2025-dynamique-appelle-renforcer-qualite

That average MPR aid was about **69.6%** of average works.

Arithmetic residual:

**€17,996**

But that is **not homeowner WTP**:
- other aid may exist
- financing may exist
- 2025 programme rules differ.

Still, the observed transaction sizes are enormous.

---

# 20. What is actually worth building?

Not:

> CSV of DPE G addresses for cold callers.

Much stronger:

## France Property Retrofit Intelligence Graph

For a lawful B2B/customer-owned property universe:

1. resolve asset to BAN/RNB/address
2. retrieve DPE history
3. normalize all labels onto a chosen methodology version
4. separate physical vs policy-driven label changes
5. detect future rental/sale clocks
6. find audit
7. extract audit recommendations/scenarios
8. map qualified RGE supply by exact work domain
9. measure local supply churn/depth
10. connect to realized programme statistics
11. expose confidence/provenance on every field.

Potential buyers:
- property managers
- landlord portfolios
- estate agencies
- banks/lenders
- insurers
- RGE operators
- renovation networks
- municipalities.

This is a **data product first**, lead-gen second.

---

# 21. A powerful locality opportunity metric becomes possible

For:

`commune × property cohort × work type`

we can derive something like:

```text
physical_need_density
× legal_deadline_proximity
× audit_scenario_frequency
× funded_transaction_value
÷ qualified_RGE_supply_depth
```

with explicit corrections for:
- DPE representativeness
- methodology version
- subsidy gatekeeping
- qualification record deduplication.

This is the kind of market-cell graph we actually want.

---

# 22. B22 falsification review

### Strongly supported
- public compliance ledger can massively reduce research cost
- technical condition data is rich enough for asset segmentation
- audit layer adds standardized proposed interventions
- supply qualification layer is open
- future legal cohorts are machine-computable
- actual public-money transaction flows are huge.

### Falsified
- DPE records can be used as uncorrected national prevalence
- class migration equals renovation
- audit recommendation equals completed job
- open licence equals permission to cold-prospect any resident
- open asset data means the subsidized customer channel is open.

### Unresolved
- how often DPE/audit recommendation converts into actual work by scenario
- quote-price dispersion for matched audit work packages
- locality-level relationship between RGE density and job price/wait time
- how completely stable building IDs can be resolved across DPE histories
- predictive lift over Google search/CPC when forecasting actual booked work.

---

# 23. Batch-level quality review: B20–B22

This batch stayed high-information.

### B20
Produced a natural institutional A/B:
**mandatory diagnoser prohibited from repair → repair demand exported.**

### B21
Did not simply repeat B20.
It found:
**partial monopoly + commercial firewall + machine-readable private asset ledger.**

### B22
Did not simply repeat B21.
It tested ledger accessibility and found:
**open asset + audit + supplier graph**, plus two critical failure modes:
- policy formula can move cohorts without physical change
- open asset intelligence does not open the human/customer channel.

The three results form a causal progression rather than three anecdotes.

**Redundancy assessment: LOW.**

---

# 24. Autonomous next experiment — B23 NYC Local Law 97

B22 leaves one very precise unresolved variable:

> What if the compliance asset is openly identifiable **and** the owner is a business/legal entity **and** noncompliance maps to an explicit monetary penalty?

The next GoldProbe should therefore be:

## B23 — New York City Local Law 97

Large-building emissions compliance.

Why:
- public building/compliance/emissions data
- commercial/organizational owners
- explicit statutory emissions thresholds
- explicit penalty economics
- energy-retrofit supply market
- no private-household cold-call assumption.

Hypothesis:

> **`LEDGER_ACCESSIBILITY × ENTITY_ADDRESSABILITY × PENALTY_CERTAINTY` creates a more commercially actionable middleman/data market than open residential compliance data alone.**

That is a genuinely new test, not “another energy retrofit country.”
