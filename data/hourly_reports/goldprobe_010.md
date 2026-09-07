# Gold Probe — Agent-Native Commerce — 2026-09-07 18:00 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 13:07:49 +0200

# Gold Probe — Agent-Native Commerce

Run: 2026-09-07 18:00 Asia/Phnom_Penh

## 1. EXECUTIVE ALPHA

This run deliberately avoided the previous report’s Australia rooftop-solar, German Fronius, and UK EV-charger cells. Four new product×country mechanisms survived the novelty filter long enough for adversarial research. One remains materially interesting; three are useful hard falsifications.

### Strongest new cell: Australia × residential pools × salt-chlorinator failure / replacement

Australia has roughly 1.1–1.4 million residential pools depending on source/methodology. An Australian energy-demand study estimated about 1.2 million households with a pool or spa and 150,000–200,000 pool-pump sales annually, while Jim’s Pool Care’s 2026 head-of-pool-care estimate puts backyard pools above 1.4 million and new installations around 20,000–25,000/year.

The interesting commerce object is NOT “a chlorinator shop.” There are already strong Australian pool-parts merchants. The opportunity is a structured replacement decision engine:

OLD CHLORINATOR / CELL / CONTROL BOX + POOL SIZE + EXISTING PLUMBING + AUTOMATION BRAND + FAILURE SYMPTOMS
→ CELL-ONLY vs CONTROL-BOX vs FULL RETROFIT
→ OEM vs COMPATIBLE OPTIONS
→ EXACT FIT / UNION / OUTPUT / AUTOMATION CONSTRAINTS
→ PRICE / WARRANTY / STOCK
→ BUY

The field evidence is unusually clean. Australian owners explicitly ask whether to replace just a cell or the full chlorinator, whether a generic replacement is safe, whether existing plumbing can be retained, and whether different automation brands interoperate. A self-identified experienced Australian pool technician says the cell is generally the failure point but diagnosis must distinguish cell failure from control-box polarity failure. Another 2025 discussion warns that automation ecosystems matter: a Jandy cell does not simply work with Hayward automation.

Current commerce proves the ticket and compatibility complexity. Examples:
- Allstar Pool Parts: generic Saltigem SG30 cell AUD $795.
- Allstar: genuine Astral/Hurlcon VX7 cell + housing AUD $999; fits all VX7 versions and also Jacuzzi J-SC40.
- Zodiac Ezi Salt 24 retrofit AUD $1,150; marketed as replacing several Zodiac/Aquasphere families.
- Tropical Pool Store retrofit systems AUD $999–$1,299 for older Zodiac LM2/LM3 families.
- Pool Shop Australia lists ~170 chlorinator-cell products and explicitly asks uncertain buyers to send a photo/model for identification.

That last point is important: the market itself is telling us the current compatibility interface is often still “send us a photo and we’ll tell you.” That is exactly the sort of decision state an agent can structure.

H1-AU-POOL-CHLOR-001
Australian pool owners with failed/weak salt chlorinators will use a structured model/symptom/automation compatibility service to determine whether to replace the cell, control box, or whole chlorinator and select a direct-fit replacement, because the existing market has high SKU fragmentation and non-obvious compatibility despite abundant supply.

H0
Existing specialist merchants already resolve this adequately through product filters, model lists, phone/email/photo support, and local pool shops; software diagnosis adds little incremental conversion value.

Falsifier
Across ≥3 major Australian pool-parts merchants, a buyer with an old Astral/Zodiac/Pool Controls unit can already enter exact model + pool size + failure symptom + automation stack and receive a confident cell/control-box/full-system recommendation with direct-fit alternatives and no human contact.

Status: OPEN / strongest this run.

Highest-EVI next test
Take 10 legacy chlorinator models across Astral/Hurlcon, Zodiac, Pool Controls, AutoChlor and older discontinued families. For each, test five real failure states: low-output, low-salt false reading, dead display, eroded cell, obsolete/discontinued cell. Measure whether current merchants can produce a correct recommendation without phone/email/photo escalation. The opportunity only survives if the product graph exists but the decision graph does not.

### Hard falsification 1: UK × Klargester BioDisc sewage-treatment spares

This looked ideal on paper: installed durable infrastructure, model/era-specific motors/gearboxes/capacitors/rotors, regulatory servicing, and parts from ~£30 to £3,000.

But the merchant gap is weak.

Direct Drainage carries a deep BioDisc parts catalog with model-specific parts, same-day shipping for stock, technical documentation and explicit model compatibility. ECS Pumps explains replacement-generation details such as when an external capacitor box is required for older Vipa/Panasonic motor configurations. Tanks Direct exposes exact BioDisc model compatibility, lead times and technical documents. Examples:
- BA/BA-X/BB motor/gearbox ~£275–£324.
- BC/BD/BE Bauer motor/gearbox ~£570–£595+.
- complete BB rotor pack ~£3,031 inc VAT.
- BA rotor assembly ~£1,395.

A Tanks Direct customer review even describes routinely buying and fitting BioDisc peripheral-drive components themselves. The category is technical, but competent merchants already encode much of the compatibility logic.

H1-GB-BIODISC-001
UK BioDisc owners/service firms lack adequate model/era compatibility support for replacement parts.

H0
Established drainage specialists already provide model-specific catalogs, technical guidance and fulfillment.

Falsifier result
Strong specialist sellers found with exact compatibility and high catalog depth.

Status: FALSIFIED as a broad merchant-gap opportunity.

Residual insight
This is good training data for what excellent agent-readable lifecycle commerce should look like: model family, production era, predecessor component, required companion parts, stock, lead time and service option.

### Hard falsification 2: UK × caravan/motorhome fridge replacement

A 2026 VW Transporter owner reported that a failed Dometic fridge pump allegedly could not be replaced independently and was quoted £575 for the whole fridge. That is real replacement friction.

However, specialist merchants already solve the successor mapping surprisingly well. Jacksons Leisure and The Outpost publish detailed Dometic RCS10.5T replacement charts mapping dozens of legacy Dometic and Thetford fridge models to a current successor, plus exact dimensions, voltage and installation caveats. Leisureshopdirect and CamperNation carry broad current fridge catalogs in roughly the £1,200–£2,500 range, while Leisure Warehouse stocks substantial exact-model Dometic control boards and spare parts.

H1-GB-CARAVAN-FRIDGE-001
Legacy Dometic/Thetford owners face enough successor/fitment ambiguity to support a specialist compatibility-first merchant.

H0
Existing caravan specialists already provide model replacement charts, dimensions and replacement parts.

Status: FALSIFIED / content and product graph already strong.

Residual insight
The seller pages are strong examples of predecessor→successor mapping and should be harvested as training structure, not competed with blindly.

### Hard falsification 3: Norway × outboard propellers

Propeller selection is highly specification-driven: engine make/model/HP, gearcase size, splines, diameter, pitch, blade count, hub and desired RPM/performance. This initially looked almost tailor-made for an AI chooser.

Norwegian/Nordic specialists already do much of it:
- Seven Seas Marine organizes propellers by Yamaha/Mercury/Suzuki/Honda/Tohatsu/Volvo Penta and engine-size families and offers expert selection help.
- Watski exposes ~913 propeller products plus a motor-parts search and detailed guidance.
- Winrace lets buyers filter by motor, motor size and splines.
- Propulse has a model guide covering ~90% of outboards and an expert-selection path.
- Norsk Båtservice says it stocks 20,000+ boat parts and provides specialist advice based on 35+ years of experience.

H1-NO-PROPELLER-001
Norwegian boat owners lack adequate specification-driven online propeller selection.

H0
Marine specialists already provide structured filters, model guides and expert support.

Status: FALSIFIED.

## 2. NEW PRODUCT × COUNTRY CELLS

| Country | Ecosystem | Product/lifecycle event | Ticket evidence | Merchant-gap read | Status |
|---|---|---|---|---|---|
| AU | residential pools | salt chlorinator cell/control-box/full retrofit | ~AUD $795–$1,495 common observed replacement range; larger systems higher | Supply abundant; decision/diagnostic compatibility may remain weak | OPEN |
| GB | sewage treatment | Klargester BioDisc motors/gearboxes/rotors/control parts | ~£30 to £3,031 observed | Strong specialist merchants | FALSIFIED |
| GB | caravan/motorhome | legacy fridge replacement / successor mapping | ~£575 quoted failure case; new units ~£1,200–£2,500 | Strong successor charts + spares | FALSIFIED |
| NO | marine outboards | replacement/optimization propellers | ~NOK 869–5,640+ observed | Strong filtering + specialist advice | FALSIFIED |

## 3. FIELD EVIDENCE TABLE

### ANC-AU-POOL-001 — Australian pool technician diagnosis
Palace proximity: 82
Evidence grade: B
Source: Reddit, self-identified experienced pool technician
URL: https://www.reddit.com/r/swimmingpools/comments/10mc6sd
Exact words: “Generally it’s the cell which fails — but such quick build up could also be the box.”
Detailed claim: In real chlorinator troubleshooting, apparent chlorine-production failure is not a single SKU lookup; the technician distinguishes cell wear/scaling from control-box reverse-polarity or electronics failure. That means a useful commerce interface must diagnose replacement scope before recommending a product.
Mechanism: symptom→component diagnosis→replacement scope.
Moat implication: a cross-brand failure/compatibility graph is potentially more valuable than a catalog.
Novelty: entirely new ecosystem vs previous run.

### ANC-AU-POOL-002 — current installed-base/operator estimate
Palace proximity: 68
Evidence grade: B
Person/company: Brett Blair / Jim’s Pool Care
Role: Head of pool care division
Source: operator statement carried in April 15 2026 release
URL: https://prwire.com.au/pr/127953/pool-expert-warns-households-to-understand-maintenance-costs-and-benefits-when-choosing-pool-sanitation-systems
Exact words: “approximately more than 1.4 million pools”
Quantitative claims: 20,000–25,000 new Australian pools/year; >1.4m backyard pools. Treat as operator estimate, not government census.
Mechanism: very large installed durable equipment base produces ongoing replacement demand.

### ANC-AU-POOL-003 — Australian energy-market installed-base benchmark
Palace proximity: 60
Evidence grade: A-
Source: Australian Energy Regulator supporting modelling document
URL: https://www.aer.gov.au/system/files/Endeavour%20Energy%20-%20NIEIR%20-%207.02%20Post%20Modelling%20Adjustments%20for%20Demand%20Forecasts%20-%20June%202021%20-%20Public.pdf
Detailed claim: modelling uses approximately 1.2m Australian households with a swimming pool or spa and estimates 150k–200k annual pool-pump sales based partly on replacement cycles.
Caveat: older 2021 modelling and pump-specific, not chlorinator-specific.
Mechanism: validates scale and replacement cadence in adjacent pool equipment.

### ANC-AU-POOL-004 — Pool Shop Australia catalog structure
Palace proximity: 88
Evidence grade: A
Role: direct specialist merchant / inventory operator
URL: https://poolshop.com.au/collections/chlorinator-cells
Exact words: “Not sure which cell you need? Send us a photo or model details.”
Quantitative claims: collection currently displays roughly 170 chlorinator-cell products.
Mechanism: catalog complexity is high enough that the merchant still uses human/photo-assisted identification.
Moat implication: convert the photo/model escalation into a structured compatibility/diagnosis API.

### ANC-GB-BIODISC-001 — Direct Drainage deep lifecycle catalog
Palace proximity: 90
Evidence grade: A
Role: specialist merchant/operator
URL: https://direct-drainage.co.uk/collections/klargester-biodisc-spare-parts
Detailed claim: large model-specific BioDisc spare catalog across motors, gearboxes, belts, bearings, control panels, pulleys and accessories with fast dispatch and human support.
Outcome: falsifies a broad merchant-scarcity thesis.

### ANC-GB-CARAVAN-001 — 2026 owner failure case
Palace proximity: 65
Evidence grade: B
Source: VW T6 forum
URL: https://www.t6forum.com/threads/pump-for-dometic-fridge.64161/
Exact words: “The pump in our Dometic fridge is kaput… The whole fridge needs replacing. The quote is £575.”
Mechanism: small component failure can trigger whole-appliance replacement and successor selection.
Counterevidence: current specialist replacement charts are already excellent.

### ANC-NO-PROP-001 — Norwegian specialist selection interface
Palace proximity: 88
Evidence grade: A
Person/company: Seven Seas Marine
Role: specialist propeller merchant
URL: https://sevenseasmarine.no/
Detailed claim: merchant already organizes selection by outboard/inboard/sailboat, engine manufacturer and power families and explicitly offers expert matching.
Outcome: falsifies broad propeller-selection whitespace.

## 4. EXACT WORDS — BEST FIELD EXCERPTS

Australian pool technician:
“Generally it’s the cell which fails — but such quick build up could also be the box.”
https://www.reddit.com/r/swimmingpools/comments/10mc6sd

Australian pool-market operator Brett Blair:
“approximately more than 1.4 million pools”
https://prwire.com.au/pr/127953/pool-expert-warns-households-to-understand-maintenance-costs-and-benefits-when-choosing-pool-sanitation-systems

Pool Shop Australia:
“Not sure which cell you need? Send us a photo or model details.”
https://poolshop.com.au/collections/chlorinator-cells

UK VW T6 owner, January 2026:
“The pump in our Dometic fridge is kaput… The whole fridge needs replacing. The quote is £575.”
https://www.t6forum.com/threads/pump-for-dometic-fridge.64161/

## 5. INSTALLED-BASE / LIFECYCLE MECHANISMS

### Mechanism M-AU-POOL-REPLACE
Large Australian pool installed base → salt chlorinator/cell ages or loses output → owner observes low chlorine / false low-salt / dead display / eroded plates → must distinguish chemistry/scaling vs cell failure vs control-box failure → choose replacement scope → choose OEM/generic/retrofit → ensure plumbing and automation compatibility.

The strongest feature is that failure diagnosis and compatibility are inseparable from the product decision.

### Mechanism M-GB-BIODISC
Long-lived sewage-treatment plant → wear component or motor/gearbox fails → model/production era determines part and companion capacitor/wiring requirements → specialist merchants already encode this well. Useful negative control.

### Mechanism M-GB-CARAVAN-FRIDGE
Legacy fridge/component failure → whole-fridge successor may be required → cutout dimensions + wheel arch + voltage + ventilation + predecessor model constrain replacement → existing merchants already publish replacement charts. Useful negative control.

### Mechanism M-NO-PROPELLER
Boat/motor combination + existing RPM/performance → hub/splines/gearcase + pitch/diameter determine propeller → strong existing model guides and specialists. Useful negative control.

## 6. MERCHANT-GAP / COMPATIBILITY FINDINGS

### Australia pool chlorinators: CONTENT GAP = MEDIUM; MERCHANT GAP = UNKNOWN / potentially decision-layer specific

Supply is definitely not scarce. There are hundreds of compatible and OEM cells and multiple retrofit systems. The gap, if real, is that compatibility and failure-state diagnosis are distributed across model names, legacy part numbers, photos, pool size, plumbing unions, chlorination output, control boxes and automation ecosystems.

Evidence against the thesis is strong:
- Allstar Pool Parts publishes exact legacy/current compatibility.
- Tropical Pool Store publishes direct retrofit families.
- Pool Shop Australia has a huge replacement catalog.

Evidence for the narrower thesis:
- the merchant explicitly requests photo/model escalation;
- users repeatedly ask cell vs whole-system questions;
- technician advice shows symptom interpretation is required;
- automation-brand incompatibility can invalidate apparently compatible hardware.

This is therefore an AGENT DECISION GAP hypothesis, not a seller-count gap.

### BioDisc / caravan fridges / Norwegian propellers
All three have GOOD merchants that already encode compatibility. Do not build another specialist catalog unless a specific unsupported legacy sub-family is found later.

## 7. HARD FALSIFICATIONS / KILLS

KILL: broad UK Klargester/BioDisc spare-parts store.
Reason: mature specialists already carry deep model-specific catalogs, documentation and fulfillment.

KILL: broad UK Dometic/Thetford replacement-fridge chooser/store.
Reason: merchants already publish excellent predecessor→successor charts and exact installation dimensions.

KILL: Norwegian outboard-propeller AI shop as a generic category.
Reason: several Norwegian/Nordic specialists already offer motor-based filtering, model guides, huge inventory and human expertise.

## 8. HYPOTHESIS LEDGER

### H1-AU-POOL-CHLOR-001 — OPEN
H1: A model/symptom/automation-aware decision engine materially improves Australian salt-chlorinator replacement selection and can route high-ticket product purchases.
H0: merchant filters/photo support already solve the job cheaply enough.
Evidence for: 1.1–1.4m pool installed-base estimates; high-ticket replacement products; 170-product chlorinator-cell catalog; users asking cell-vs-system questions; expert troubleshooting indicates diagnostic ambiguity; automation compatibility constraints.
Evidence against: multiple mature pool-parts merchants; good model compatibility on many pages; local pool shops offer human diagnosis.
Falsifier: ≥3 leading merchants already perform fully structured no-human diagnosis and recommendation across legacy brands.
Belief delta: FOR.
Next best test: 10-model × 5-failure-state benchmark against leading merchants.

### H1-GB-BIODISC-001 — FALSIFIED
H1: UK BioDisc owners lack adequate compatibility-led part commerce.
H0: mature specialists already encode model/era parts and service.
Evidence: Direct Drainage, ECS Pumps, Tanks Direct.
Belief delta: STRONGLY_AGAINST.

### H1-GB-CARAVAN-FRIDGE-001 — FALSIFIED
H1: legacy caravan fridge replacement lacks successor mapping.
H0: specialist merchants already map predecessor models and dimensions.
Belief delta: STRONGLY_AGAINST.

### H1-NO-PROPELLER-001 — FALSIFIED
H1: Norwegian propeller selection is poorly served online.
H0: structured selection and expert specialists already exist.
Belief delta: STRONGLY_AGAINST.

## 9. WHO TO WATCH NEXT

1. Pool Shop Australia — direct merchant with unusually large replacement-cell catalog. The human/photo-identification workflow is a possible product requirement hiding in plain sight.
https://poolshop.com.au/collections/chlorinator-cells

2. Allstar Pool Parts — high-quality mapping of OEM/generic/legacy chlorinator compatibility and useful price/warranty observations.
https://allstarpoolparts.com.au/

3. Tropical Pool Store — unusually explicit retrofit catalog: which obsolete chlorinators can be replaced without re-plumbing and at what price.
https://tropicalpoolstore.com.au/

4. Jim’s Pool Care / Brett Blair — operator-level view of installed base, sanitation-system economics and replacement behavior.
https://www.jimspoolcare.com.au/

5. Direct Drainage / ECS Pumps — negative-control merchants whose BioDisc pages show what agent-native lifecycle merchandising looks like when it is already solved.
https://direct-drainage.co.uk/
https://ecspumps.co.uk/

## 10. NOVELTY AUDIT VS PRIOR REPORT

Prior report cells explicitly excluded from this run:
- AU rooftop solar inverter repowering
- AU Fronius Datamanager
- DE Fronius smart meters
- GB EV-charger commodity spares

New substantive cells this run:
- AU residential pool salt-chlorinator replacement
- GB Klargester BioDisc lifecycle spares
- GB caravan/motorhome refrigerator replacement
- NO outboard propeller replacement/selection

New mechanism discovered:
- DIAGNOSTIC COMMERCE GAP: the market can have abundant inventory and decent individual compatibility pages yet still lack a structured state machine that determines WHAT failed before choosing WHAT to buy.

Semantic duplicates rejected:
- individual salt-cell SKUs were grouped into the same chlorinator-replacement mechanism;
- multiple BioDisc merchants were treated as competitive evidence rather than separate opportunities;
- individual Dometic fridge models were grouped into successor-mapping;
- individual Norwegian propellers were grouped into the selection mechanism.

Novel substantive evidence share: >70% relative to the previous report.

## 11. SOURCE-YIELD LEDGER

| Source family | Reads/searches | Accepted material | Belief changes | Next treatment |
|---|---:|---:|---:|---|
| first-hand forums/Reddit | ~10 | 4 | 2 | EXPLOIT for failure-state discovery |
| specialist ecommerce | ~25 | 12+ | 4 incl. 3 kills | EXPLOIT heavily for merchant-gap falsification |
| government/energy modelling | 3 | 1 strong installed-base benchmark | 1 | EXPLOIT selectively |
| manufacturer / operator pages | ~8 | 4 | 2 | EXPLOIT for compatibility truth |
| marine merchants | ~8 | 5 | 1 kill | DEPRIORITIZE Norway propellers |

## 12. MACHINE-READABLE JSONL

```jsonl
{"record_id":"ANC-AU-POOL-001","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"AU","market_or_entity":"residential salt-chlorinator replacement","person_or_company":"self-identified experienced Australian pool technician","role":"pool technician","source_type":"reddit","source_url":"https://www.reddit.com/r/swimmingpools/comments/10mc6sd","published_at":"2023-01-27","palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"Generally it’s the cell which fails — but such quick build up could also be the box.","detailed_claim":"Real chlorinator troubleshooting requires distinguishing ordinary cell wear/scaling from control-box/reverse-polarity failure before selecting a replacement product.","quantitative_claims":[],"state_before":"DISCOVERED","action_taken":"diagnostic troubleshooting","observed_agent_behavior":"UNKNOWN","outcome":"component-level replacement decision required","time_horizon":"same maintenance event","mechanism":"failure symptom -> diagnose cell vs control box -> replacement scope","moat_implication":"cross-brand diagnostic plus compatibility graph may be more defensible than catalog inventory","h1":"Australian pool owners will use model/symptom-aware chlorinator replacement guidance","h0":"existing merchants/pool shops already solve diagnosis cheaply","falsifier":"three leading merchants provide structured no-human failure diagnosis plus product selection across legacy brands","belief_delta":"FOR","next_best_test":"10 legacy models x 5 failure-state merchant benchmark","novelty_reason":"new installed-base ecosystem and diagnostic-commerce mechanism","independence_cluster":"AU_POOL_TECH_REDDIT_2023"}
{"record_id":"ANC-AU-POOL-002","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"AU","market_or_entity":"Australian residential pool installed base","person_or_company":"Brett Blair / Jim's Pool Care","role":"Head of pool care division","source_type":"blog","source_url":"https://prwire.com.au/pr/127953/pool-expert-warns-households-to-understand-maintenance-costs-and-benefits-when-choosing-pool-sanitation-systems","published_at":"2026-04-15","palace_proximity_score":68,"evidence_grade":"B","verbatim_excerpt":"approximately more than 1.4 million pools","detailed_claim":"A current Australian pool-service operator estimates >1.4m backyard pools and 20k-25k new installations annually; useful scale evidence but not an official census.","quantitative_claims":[{"metric":"backyard_pool_installed_base","value":">1.4m","denominator":"Australia","timeframe":"2026 operator estimate","caveat":"operator estimate"},{"metric":"new_pool_installations","value":"20,000-25,000/year","denominator":"Australia","timeframe":"2026","caveat":"operator estimate"}],"state_before":"DISCOVERED","action_taken":"UNKNOWN","observed_agent_behavior":"UNKNOWN","outcome":"large replacement-bearing installed base supported","time_horizon":"annual","mechanism":"large durable installed base -> recurring equipment replacement","moat_implication":"enough installed base for narrow lifecycle decision products","h1":"installed base can support recurring chlorinator replacement demand","h0":"chlorinator penetration/replacement frequency too low despite pool count","falsifier":"credible chlorinator-specific installed/replacement data shows small addressable base","belief_delta":"FOR","next_best_test":"obtain brand/model penetration and cell replacement data","novelty_reason":"new current operator estimate","independence_cluster":"JIMS_POOLCARE_2026"}
{"record_id":"ANC-AU-POOL-003","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"AU","market_or_entity":"chlorinator-cell catalog complexity","person_or_company":"Pool Shop Australia","role":"specialist pool-parts merchant","source_type":"blog","source_url":"https://poolshop.com.au/collections/chlorinator-cells","published_at":null,"palace_proximity_score":88,"evidence_grade":"A","verbatim_excerpt":"Not sure which cell you need? Send us a photo or model details.","detailed_claim":"The merchant exposes roughly 170 replacement chlorinator-cell items and still offers human/photo-assisted model identification, indicating substantial compatibility complexity despite abundant inventory.","quantitative_claims":[{"metric":"visible_chlorinator_cell_items","value":"~170","denominator":"merchant collection","timeframe":"observed 2026-09-07","caveat":"catalog count may change"}],"state_before":"DISCOVERED","action_taken":"merchant asks for photo/model escalation","observed_agent_behavior":"UNKNOWN","outcome":"compatibility uncertainty handled manually","time_horizon":"purchase session","mechanism":"large fragmented catalog -> human identification -> purchase","moat_implication":"photo/model-to-compatible-SKU graph could automate current human support","h1":"structured compatibility guidance can remove manual merchant escalation","h0":"manual escalation is cheap and conversion-effective enough","falsifier":"existing structured tools already match legacy units as reliably as staff","belief_delta":"FOR","next_best_test":"benchmark photo/model identification across merchants","novelty_reason":"direct merchant evidence of manual compatibility workflow","independence_cluster":"POOLSHOP_AU"}
{"record_id":"ANC-GB-BIODISC-001","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"GB","market_or_entity":"Klargester BioDisc replacement parts","person_or_company":"Direct Drainage","role":"specialist drainage merchant","source_type":"blog","source_url":"https://direct-drainage.co.uk/collections/klargester-biodisc-spare-parts","published_at":null,"palace_proximity_score":90,"evidence_grade":"A","verbatim_excerpt":null,"detailed_claim":"Deep genuine BioDisc parts range with model-specific motors, gearboxes, bearings, pulleys, control parts, technical support and fast fulfillment substantially solves the merchant/compatibility gap.","quantitative_claims":[],"state_before":"DISCOVERED","action_taken":"merchant structures model-specific lifecycle parts","observed_agent_behavior":"UNKNOWN","outcome":"broad opportunity falsified","time_horizon":"current","mechanism":"specialist merchant already encodes lifecycle compatibility","moat_implication":"use as negative-control/training example, not target","h1":"UK BioDisc owners lack compatibility-led spare-parts commerce","h0":"mature drainage specialists already solve it","falsifier":"multiple strong model-specific merchants","belief_delta":"STRONGLY_AGAINST","next_best_test":"none; re-open only for unsupported obsolete sub-family","novelty_reason":"new lifecycle category falsified","independence_cluster":"GB_BIODISC_MERCHANTS"}
{"record_id":"ANC-GB-CARAVAN-001","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"GB","market_or_entity":"legacy caravan/motorhome refrigerator replacement","person_or_company":"VW T6 Forum user dirkie","role":"owner","source_type":"forum","source_url":"https://www.t6forum.com/threads/pump-for-dometic-fridge.64161/","published_at":"2026-01-14","palace_proximity_score":65,"evidence_grade":"B","verbatim_excerpt":"The pump in our Dometic fridge is kaput… The whole fridge needs replacing. The quote is £575.","detailed_claim":"A component failure can force a whole-appliance replacement decision, but current UK merchants already publish detailed predecessor-to-successor charts and installation dimensions.","quantitative_claims":[{"metric":"quoted_whole_fridge_replacement","value":"£575","denominator":"one owner quote","timeframe":"2026-01","caveat":"single anecdote"}],"state_before":"DISCOVERED","action_taken":"searched current successor commerce","observed_agent_behavior":"UNKNOWN","outcome":"merchant-gap thesis falsified","time_horizon":"current","mechanism":"component failure -> whole-unit successor selection","moat_implication":"replacement mapping valuable but already well supplied","h1":"legacy caravan fridge owners lack successor mapping","h0":"specialist merchants already provide detailed replacement guides","falsifier":"multiple strong replacement charts and merchants","belief_delta":"STRONGLY_AGAINST","next_best_test":"none unless obsolete model class lacks mapping","novelty_reason":"new vehicle-equipment lifecycle cell","independence_cluster":"GB_CARAVAN_FRIDGE"}
{"record_id":"ANC-NO-PROP-001","probe":"agent_native_commerce","observed_at":"2026-09-07T18:02:36+07:00","country":"NO","market_or_entity":"outboard propeller selection","person_or_company":"Seven Seas Marine","role":"specialist propeller merchant","source_type":"blog","source_url":"https://sevenseasmarine.no/","published_at":null,"palace_proximity_score":88,"evidence_grade":"A","verbatim_excerpt":null,"detailed_claim":"Norwegian specialist already organizes propeller selection by engine type/manufacturer/power and provides expert selection support; other Nordic merchants expose motor, spline and size filters.","quantitative_claims":[],"state_before":"DISCOVERED","action_taken":"merchant structured compatibility navigation","observed_agent_behavior":"UNKNOWN","outcome":"broad selection-gap thesis falsified","time_horizon":"current","mechanism":"specification-heavy product -> mature specialist selector","moat_implication":"do not assume technical complexity implies merchant whitespace","h1":"Norwegian boat owners lack adequate propeller selection tooling","h0":"specialists already solve selection with structured filters and experts","falsifier":"multiple mature selectors and high-inventory specialists","belief_delta":"STRONGLY_AGAINST","next_best_test":"none","novelty_reason":"new marine category tested and killed","independence_cluster":"NO_PROP_MERCHANTS"}
```

### Product-opportunity JSON

```json
{
  "country":"AU",
  "ecosystem":"residential_pool_salt_chlorinator",
  "product_or_family":"replacement salt cells, control boxes, retrofit chlorinators",
  "installed_base":"~1.2m pool/spa households in 2021 energy modelling; >1.4m backyard pools in 2026 operator estimate; chlorinator-specific installed base UNKNOWN",
  "lifecycle_trigger":"low chlorine output, false low-salt state, cell erosion/scaling, dead control box, discontinued model, automation incompatibility",
  "total_sellers":"multiple national specialist merchants; exact count UNKNOWN",
  "good_sellers":"multiple; exact count UNKNOWN",
  "merchant_gap":"UNKNOWN; inventory gap low, diagnostic/compatibility decision gap potentially meaningful",
  "content_gap":"MEDIUM",
  "search_demand":"community recurrence + large live specialist catalog; exact search volume UNKNOWN",
  "retail_price":"observed ~AUD $795 generic cell, $999 genuine VX7 cell, $999-$1,495 retrofit/full chlorinator examples",
  "supplier_cost":"UNKNOWN",
  "break_even_cac":"UNKNOWN",
  "h1":"Australian pool owners will use model/symptom/automation-aware guidance to select cell vs control-box vs full retrofit and direct-fit replacements",
  "h0":"specialist merchants and local pool shops already resolve this cheaply via filters/photo/phone support",
  "falsifier":"3+ leading merchants already provide reliable structured no-human diagnosis and recommendation across legacy brands/failure states",
  "status":"OPEN"
}
```

## Principal source URLs

Australia pool installed base / economics:
https://www.aer.gov.au/system/files/Endeavour%20Energy%20-%20NIEIR%20-%207.02%20Post%20Modelling%20Adjustments%20for%20Demand%20Forecasts%20-%20June%202021%20-%20Public.pdf
https://prwire.com.au/pr/127953/pool-expert-warns-households-to-understand-maintenance-costs-and-benefits-when-choosing-pool-sanitation-systems

Australian operator/user evidence:
https://www.reddit.com/r/swimmingpools/comments/10mc6sd
https://www.reddit.com/r/swimmingpools/comments/1ja3ncr
https://www.reddit.com/r/pools/comments/1lvm1x5/got_this_email_from_a_pool_tech_after_a_visit/
https://www.reddit.com/r/sydney/comments/1szkrde/is_my_pool_guy_ripping_me_off/

Australian chlorinator commerce:
https://poolshop.com.au/collections/chlorinator-cells
https://allstarpoolparts.com.au/products/astralpool-hurlcon-vx7-cell-genuine
https://allstarpoolparts.com.au/products/zodiac-ezi-salt-24-chlorinator
https://tropicalpoolstore.com.au/products/copy-of-eco-chlor-lm2-15-20-24-retro-salt-water-chlorinator-7-year-warranty
https://tropicalpoolstore.com.au/collections/salt-chlorinators/products/eco-chlor-lm2-30-40-retro-salt-water-chlorinator-7-year-warranty-1

UK BioDisc negative control:
https://direct-drainage.co.uk/collections/klargester-biodisc-spare-parts
https://ecspumps.co.uk/product/ba-bb-panasonic-gearbox-motor/
https://www.tanks-direct.co.uk/bb-biodisc-rotor-pack/p30641

UK caravan fridge negative control:
https://www.t6forum.com/threads/pump-for-dometic-fridge.64161/
https://www.jacksonsleisure.com/dometic/rcs-10-5t/wheel/arch/fridge/
https://www.theoutpostuk.com/product/dometic-rcs-10-5t-wheel-arch-fridge-12v-73166/

Norway propeller negative control:
https://sevenseasmarine.no/
https://www.watski.no/propell-til-bat-11ThS
https://www.winrace.no/nettbutikk/staal
https://propulse.se/no/modellguide

## Next-hour research directive
Do NOT spend the next run adding more Australian chlorinator SKUs. The next useful information is binary: can the leading merchants already solve the five-state diagnostic/compatibility benchmark without human escalation? If yes, kill it. If no, map the minimum agent decision graph and then move to a new installed-base ecosystem.
