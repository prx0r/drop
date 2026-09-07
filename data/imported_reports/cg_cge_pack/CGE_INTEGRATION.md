# CGE Integration Spec — Untrusted Proposer / Space Expander

## Current CGE capabilities worth using

CGE currently adds:
- peer-reviewed evolution;
- trust-weighted consensus;
- feedback signals;
- rejection-pattern adversarial cases;
- adaptive mutation;
- MAP-Elites style diversity;
- a first-class space-expansion charter in its spec.

For Drop, use these for **proposal quality**, not final factual scoring.

## Deployment

Because CG and CGE share the same package name, run CGE separately.

CGE gets:
- campaign parent JSON;
- PUBLIC CG gate result;
- public failure reasons;
- BigQuery-derived typed search-space manifest;
- prior mutation outcomes;
- kill ledger;
- public country/OEM/supplier intelligence.

CGE does NOT get:
- CG secret cases;
- hidden benchmark answers;
- mutable access to verified evidence;
- authority to mark gates PASS.

## Genome

Mutatable genes:

```text
country
track
oem_ecosystem
asset
generation_scope
component_scope
trigger
buyer_segment
supplier_candidate_set
monetization_route
distribution_route
launch_sku_scope
resolver_input_set
```

Non-mutatable:
```text
rubric thresholds
observed installed base
observed buyer-role statistics
observed supplier terms
observed prices
compatibility truth
incumbent benchmark results
source tier
```

## Mutation families

### 1. NARROW
- narrower generation;
- narrower component;
- owner-replaceable subset;
- exact obsolescence cohort.

### 2. REROUTE
- D2C → service;
- D2C → B2B;
- product margin → referral;
- direct checkout → RFQ/PO.

### 3. SUPPLY
- swap supplier candidate;
- multi-source supplier set;
- choose supplier with feed/direct ship;
- partner-first aftersales model.

### 4. GEOGRAPHIC TRANSFER
- move same installed asset to another country where incumbent gap is weaker;
- preserve OEM/component but alter local supplier graph.

### 5. GRAPH DEEPENING
- change from commodity component to supersession-heavy component;
- add required adapter/bundle relation;
- target negative-compatibility ambiguity.

### 6. SPLIT
Broad:
`Finland heat-pump electronics`

Children:
- Mitsubishi indoor PCB cohort X;
- Panasonic receiver modules cohort Y;
- NIBE F-series fan/sensor lifecycle.

### 7. COMPOSE
Combine:
- replacement part +
- installation provider +
- repair exchange +
- successor bundle

only when buyer route supports it.

### 8. RESEARCH ACTION
Instead of campaign mutation, propose:
- supplier call;
- buyer-role sample;
- incumbent benchmark;
- compatibility edge extraction;
- keyword/demand test.

## Feedback mapping

Translate CG public failure into CGE mutation guidance.

| CG result | CGE response |
|---|---|
| G4 buyer autonomy FAIL | reroute or mutate to owner-selected component |
| G6 incumbent gap FAIL | narrow atom or transfer country |
| G7 reseller UNKNOWN | evidence action, not campaign rewrite |
| G8 economics FAIL | supplier/monetization mutation |
| G9 demand FAIL | kill or broaden event pool without breaking atom integrity |
| G10 operations FAIL | service/B2B route or simpler component |
| G3 compatibility UNKNOWN | extract graph evidence |
| stagnation | invoke space expansion |

## MAP-Elites descriptors

Avoid convergence to 100 Allaway clones.

Recommended descriptors:
- track: D2C / migration / service / B2B;
- trigger: consumable / failure / obsolescence / maintenance;
- asset class: building / leisure / marine / industrial / aquaculture;
- country cluster;
- buyer selector: consumer / engineer / technician;
- operational burden bucket.

Quality within each cell is judged by CG.

## Proposer peer roles

CGE peer review can use specialized critics:

1. **Buyer-role prosecutor**
2. **Incumbent hunter**
3. **Supplier-path critic**
4. **Compatibility graph critic**
5. **Demand statistician**
6. **Economics critic**
7. **Platform/retrieval critic**
8. **Cross-country transfer proposer**

Their consensus may guide mutation priority.

It cannot flip hard gates.
