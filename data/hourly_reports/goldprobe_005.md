# Gold Probe — Agent-Native Commerce — 2026-09-07 19:04 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 08:08:17 -0400

Gold Probe — Agent-Native Commerce
Run: 2026-09-07 19:04 Asia/Phnom_Penh

1. EXECUTIVE ALPHA

This run semantically deduplicated the two prior Commerce reports and deliberately avoided their Australia rooftop-solar/inverter, German Fronius, UK EV-related, Australian salt-chlorinator, UK Klargester, UK caravan-fridge, and Norwegian outboard-propeller cells.

The strongest genuinely new mechanism is FINLAND — LEGACY SAUNA CONTROL / SMART-CONTROLLER MIGRATION, specifically Harvia Xenio/C-series/older controller states into Fenix-era control. This is not simply “sell a sauna controller.” Finland has an unusually large installed base (the widely cited order of magnitude is ~3 million saunas), Harvia has actively moved its control stack from Xenio toward Fenix, and compatibility depends on heater generation, controller/power-unit generation, serial/board state, remote-start safety hardware, and desired function. Harvia’s own support documentation now distinguishes FC/Fenix, XW/Xenio WiFi, and XE systems, with different upgrade requirements. Current field discussion shows owners struggling with both failure diagnosis and legacy-controller migration.

However, this is only OPEN, not SUPPORTED. The adversarial merchant audit found several competent sellers already explaining the upgrade, including Huolto Vuorio in Finland and stronger German merchants that publish explicit serial-number/power-card compatibility. The opportunity, if any, is therefore a cross-generation decision engine + exact parts bundle, not a generic webshop.

Two cleaner replacement ideas were weakened/killed:
- NORWAY — Mitsubishi heat-pump remote controls: official Mitsubishi and local parts merchants already expose model→remote mappings and direct purchase. Decision friction exists but is mostly solved.
- NORWAY/UK — marine sonar transducer replacement: real connector/network/adapter complexity exists, but strong retailers already publish detailed plotter→transducer→adapter compatibility. Potentially useful as a data product, but merchant whitespace is not yet proven.
- UK — Truma CP Plus control-panel replacement: compatibility involves PCB revision and connector count, but specialist caravan merchants already state these constraints clearly. Merchant gap currently looks weak.

The broader new rule from this run: replacement markets become interesting when the compatibility object is not MODEL→SKU but STATEFUL LEGACY SYSTEM→SAFE SUCCESSOR BUNDLE. That requires board revision, controller generation, firmware/network generation, safety accessory state, and desired functionality. Straightforward model→part lookups are increasingly commoditized by incumbent merchants.

2. NEW PRODUCT × COUNTRY CELLS

A. FINLAND — HARVIA LEGACY SAUNA CONTROLLER / FENIX MIGRATION
Status: OPEN
Installed base: Finland has an estimated ~3 million saunas; exact count is not registered. This is order-of-magnitude evidence, not a device-specific installed-base count.
Lifecycle trigger: failed Xenio/power unit; discontinued/transitioning controller; desire for WiFi/remote start; replacement of old analog/C-series controls; safety-system/door-sensor migration.
Observed current retail:
- Harvia Fenix FX001XW around €309–€368 at Finnish merchants.
- German specialist pricing found around €279 for FX001XW and €329 for FX002XW with door sensor.
Supplier cost: UNKNOWN.
Break-even CAC: UNKNOWN.
Merchant gap: MEDIUM/UNKNOWN.
Content gap: MEDIUM.
Why interesting: compatibility is serial/board/controller/safety-state dependent rather than one-dimensional.
H1: a decision layer that takes heater model + existing control unit + power-card/serial generation + remote-start requirement + safety hardware and returns an exact supported migration bundle can reduce purchase/support friction enough to win specialist commerce.
H0: Harvia plus existing specialist merchants already resolve the migration adequately, making the opportunity primarily content/support rather than commerce.
Falsifier: test 20 legacy Harvia configurations; if ≥90% can be resolved to a safe exact bundle from the first two Finnish specialist/official results without phone/email escalation, kill.
Highest-EVI next test: build a 20-case compatibility benchmark spanning C90/C150, Xenio non-WiFi, Xenio WiFi, XE, older power cards, and Fenix upgrade paths; measure answer completeness, serial/board requirements, safety accessory requirements, and merchant escalation.

B. NORWAY — MITSUBISHI HEAT-PUMP REMOTE / WIFI CONTROL REPLACEMENT
Status: FALSIFIED / weak
Observed retail:
- Mitsubishi Electric Norway directly sells model-specific remotes around NOK 473–683 for several families.
- Reservedel.no carries original replacement remotes with explicit compatible model/part numbers, roughly NOK 1,040–1,992 in examples observed.
- A Norwegian specialist publishes a broad compatibility list for the MELCloud MAC-567IF-E adapter.
Mechanism: lost/broken remote or smart-control retrofit.
Why killed: model→remote compatibility is already explicit and local fulfillment exists. The decision problem is too shallow for a defensible compatibility layer.

C. NORWAY — LEGACY MARINE SONAR TRANSDUCER / DISPLAY MIGRATION
Status: OPEN but weakened
Lifecycle trigger: old analogue/legacy sonar sensor retained while chartplotter/display is upgraded; connector-generation mismatch; network bridge requirement.
Observed retail:
- Garmin official documentation explicitly states an old 6-pin transducer may require an adapter for an 8-pin sounder and names the preferred successor part.
- Norwegian Raymarine merchants document exact Axiom/Element adapter requirements for CPT-S transducers.
- Raymarine iTC-5 is sold specifically to retain old analogue transducers while moving to SeaTalkng/NMEA2000-era displays; observed price ~€391 from one European specialist.
H1: cross-brand legacy sensor/display migration has enough multi-variable compatibility pain to support an agent-native selector and curated adapters/transducers.
H0: brand-specific retailers and manufacturer compatibility data already solve the purchase sufficiently.
Falsifier: benchmark 20 common old-display/transducer combinations across Garmin/Raymarine/Simrad; if exact keep-sensor vs adapter vs replace-sensor decisions are resolvable from top local sellers with no escalation, kill.
Highest-EVI next test: Norwegian-language benchmark on 10 legacy Raymarine/Garmin systems, because current evidence proves complexity but not merchant whitespace.

D. UK — TRUMA CP PLUS / LEGACY CARAVAN HEATING CONTROL MIGRATION
Status: FALSIFIED / weak merchant gap
Observed retail: specialist UK merchants sell CP Plus controls around £117–£148 and explicitly distinguish one-port/two-port variants, iNET dependency, GAR-era compatibility, and PCB version ≥5 requirements.
Why killed: this is exactly the kind of compatibility problem the probe seeks, but existing specialists already expose unusually good technical buying guidance.

3. FIELD EVIDENCE TABLE

ANC-20260907-1904-01 | Finland | Harvia control migration | Harvia official support | palace proximity 95 | A | Harvia documents distinct WiFi/remote-control paths for FC/Fenix, XW/Xenio WiFi and XE systems, with XE requiring an upgrade package. Mechanism: product-generation state changes the required bundle. Source: https://support.harvia.com/hc/fi/articles/22158926984732

ANC-20260907-1904-02 | Finland/global | Harvia Xenio/Fenix | owner/operator field evidence | palace proximity 68 | B | 2026 sauna owners report no-power/no-heat states after professional installs, faulty/ambiguous wiring, high-limit issues, and controller/power-box replacement. The useful signal is not that Harvia is unreliable; it is that heater/controller/safety/power-unit state is difficult for buyers and even electricians to resolve. Sources: https://www.reddit.com/r/Sauna/comments/1ra8l94/harvia_xenio_no_power/ ; https://www.reddit.com/r/Sauna/comments/1tv4sfy/troubleshooting_why_harvia_spirit_electric_heater/ ; https://www.reddit.com/r/Sauna/comments/1v645a7/xenio_harvia_heater_not_working/

ANC-20260907-1904-03 | Finland | Fenix FX001XW retail | Huolto Vuorio | palace proximity 82 | A/B | Finnish specialist states that Fenix FX001XW replaces the older Xenio control panel; observed price €367.90. This is evidence for live commerce, but also negative evidence against merchant whitespace. Source: https://www.huoltovuorio.fi/fi/tuote/harvia-fenix-wifi-ohjauspaneeli-fx001xw/

ANC-20260907-1904-04 | Germany/EU | Fenix compatibility | PEQU | palace proximity 82 | A/B | Specialist publishes unusually detailed compatibility: specific Fenix/Xenio controllers, XE heater models after a serial threshold, and a Xenio power-card/serial threshold. This directly demonstrates that migration is stateful, while also proving competent merchants exist. Source: https://pequ.eu/en/products/harvia-fenix-wifi-bedienteil-fx001wg

ANC-20260907-1904-05 | Norway | Mitsubishi remotes | Mitsubishi Electric Norway | palace proximity 95 | A | Official store maps exact remote part numbers to MSZ model families and sells directly. This falsifies a shallow remote-control selector thesis. Examples: https://mee.no/produkt/fjernkontroll-til-kaiteki-hvit/ ; https://mee.no/produkt/fjernkontroll-til-zen-hvit/ ; https://mee.no/produkt/fjernkontroll-til-kirigamine-hara/

ANC-20260907-1904-06 | Norway/global marine | Garmin transducer adapters | Garmin | palace proximity 95 | A | Garmin explicitly says a 6-pin legacy transducer used with an 8-pin sounder requires adapter 010-11613-00 and names a preferred transducer successor. This proves lifecycle compatibility complexity but not merchant gap. Source: https://www.garmin.com/en-GB/p/748/

ANC-20260907-1904-07 | Norway | Raymarine transducer migration | Maritim/Vrengen/merchant | palace proximity 78 | B | Norwegian merchant pages specify direct-connect and adapter-dependent combinations across Element/Axiom/Axiom Pro and publish stock. Strong negative evidence against easy geographic arbitrage. Source: https://www.maritim.no/raymarine-cpt-s-innvendig-giver-dybde-og-chirp-ekkolodd

ANC-20260907-1904-08 | UK | Truma CP Plus | Kustom Sport | palace proximity 82 | A/B | Merchant states CP Plus compatibility depends on system generation and PCB version, including “PCB board needs to be version 5 or later to be compatible.” Observed price £116.99 for one-port and £147.75 for two-port variants. Sources: https://www.kustomsport.co.uk/product/truma-control-panel-plus-inet-ready-36022-54/ ; https://www.kustomsport.co.uk/product/truma-control-panel-plus-inet-ready-ci-bus-2-port-36022-53/

4. EXACT WORDS

Harvia support, on XE systems: “Etäohjaus on mahdollista erikseen hankittavalla lisävarustepaketilla” — remote control is possible with a separately purchased accessory package. Source: Harvia support.

PEQU, on Fenix: “Plug-and-Play-Upgrade für Ihr vorhandenes Xenio-Saunasteuergerät.” The same merchant then narrows compatibility by controller and serial/power-card generation, illustrating why the headline is simpler than the actual decision graph.

Harvia owner, June 2026, asking about analog migration: “Do you know why it is so hard to have information on this matter?” This is anecdotal, but directly describes the documentation gap around legacy-control replacement. Source: https://www.reddit.com/r/Sauna/comments/1tv0rdv/analog_controller_for_harvia_club_125_kwh/

Kustom Sport on Truma CP Plus: “PCB board needs to be version 5 or later to be compatible.” This is exactly the kind of hidden state variable an agent-native compatibility graph would encode—but here the merchant already exposes it.

5. INSTALLED-BASE / LIFECYCLE MECHANISMS

Most important new mechanism:
LEGACY ASSET
→ control/electronics generation becomes obsolete, fails, or loses desired connectivity
→ buyer wants to preserve expensive physical asset
→ successor product exists
→ compatibility depends on invisible state (board revision / serial range / controller / network / safety hardware)
→ existing SKU pages only partially encode the migration
→ decision-support layer can potentially monetize the replacement bundle.

This is better than generic replacement parts because it creates a multi-variable decision boundary and higher cost of getting the recommendation wrong.

Finland is unusually interesting for testing this mechanism because the sauna installed base is enormous relative to population and Harvia is in an active controller-generation transition. But no precise installed count by Harvia controller generation was found this run; treat that field as UNKNOWN.

6. MERCHANT-GAP / COMPATIBILITY FINDINGS

FINLAND HARVIA: compatibility complexity = HIGH; merchant gap = MEDIUM/UNKNOWN; content gap = MEDIUM. Several Finnish merchants sell the new control panel, but the best explicit serial/board-level compatibility information found this run came from a German specialist. This asymmetry is worth testing, not yet proven.

NORWAY MITSUBISHI REMOTES: compatibility complexity = LOW/MEDIUM; merchant gap = LOW. Official direct commerce solves it.

NORWAY MARINE TRANSDUCERS: compatibility complexity = HIGH; merchant gap = LOW/MEDIUM. Local merchants already expose good adapter and plotter compatibility, though cross-brand migration remains fragmented.

UK TRUMA: compatibility complexity = MEDIUM/HIGH; merchant gap = LOW. Existing specialists understand and publish the important hidden variables.

7. HARD FALSIFICATIONS / KILLS

KILL: Norway Mitsubishi heat-pump remote controls as a specialist commerce wedge. Official manufacturer mapping and local parts merchants are sufficient.

KILL: UK Truma CP Plus as a standalone compatibility-commerce wedge. Specialist merchants already publish PCB/port/system constraints.

WEAKEN: Norwegian marine transducer migration. High technical complexity is real, but local retail competence is substantially better than expected.

DO NOT PROMOTE YET: Finland Harvia legacy-control migration. The opportunity survives because the decision graph is genuinely stateful, but merchant whitespace is not established.

8. HYPOTHESIS LEDGER

H-ANC-FI-HARVIA-01
H1: Finnish owners of legacy Harvia systems face a multi-variable successor/upgrade decision that current Finnish commerce does not consistently resolve without support escalation.
H0: Harvia documentation plus Finnish specialist merchants resolve almost all common cases adequately.
For H1: Harvia has multiple controller generations/upgrade paths; field users report confusion; serial/board state can matter; migration from analog/C-series is poorly surfaced.
Against H1: Finnish merchants sell Fenix upgrades directly; at least one states it replaces Xenio; EU specialists publish excellent exact compatibility.
Falsifier: 20-case benchmark ≥90% correctly resolvable from top two Finnish merchant/official paths without human escalation.
Belief delta: FOR, low-to-moderate confidence.
Next best test: 20-case legacy configuration benchmark.

H-ANC-NO-MARINE-01
H1: cross-generation marine-electronics upgrades still contain enough adapter/network/sensor ambiguity for a specialist decision layer.
H0: manufacturer and local specialist compatibility tables already solve the commercially relevant cases.
Belief delta: NEUTRAL.
Falsifier/next test: 20 legacy vessel configurations, measure exact decision success from existing local commerce.

9. WHO TO WATCH NEXT

Harvia technical support / product migration documentation — high source proximity for serial/board compatibility and transition rules.
Huolto Vuorio — Finnish sauna-parts specialist; useful for actual parts availability and replacement patterns.
PEQU / Saunarvia — unusually detailed Fenix compatibility publisher; useful adversarial benchmark for what a GOOD merchant looks like.
Norwegian marine electronics specialists such as Maritim/Vrengen — useful counterexample merchants when testing whether a compatibility market is actually underserved.

10. NOVELTY AUDIT

Previous reports reconstructed from sent email:
- 17:00: Australian rooftop-solar/inverter replacement mechanism; German Fronius; UK EV-related cells and related falsifications.
- 18:00: Australian salt-chlorinator compatibility winner; UK Klargester, UK caravan-fridge and Norwegian outboard-propeller falsifications.

Rejected as semantic repeats this run: solar inverter successors, chlorinator cells/control boxes, caravan refrigeration, outboard propellers.

New substantive cells: Finland sauna controller migration; Norway heat-pump remotes; Norway legacy marine sonar migration; UK Truma control-panel migration.
New mechanism: stateful electronics/control-generation migration as a higher-value compatibility class.
Estimated substantive novelty: >70% relative to prior two available reports.

11. SOURCE-YIELD LEDGER

Official manufacturer/support pages: highest yield. Harvia, Mitsubishi, Garmin each materially changed a decision.
Specialist merchant pages: very high falsification yield. PEQU, Huolto Vuorio, Kustom Sport, Maritim showed where merchant competence already exists.
Reddit/operator communities: useful mechanism/discovery yield, especially legacy-controller pain and installation failure states; weak for economics unless paired with commerce/official evidence.
Generic web/search results: low accepted yield.

12. JSONL — COMMON SCHEMA

{"record_id":"ANC-20260907-1904-01","probe":"agent_native_commerce","observed_at":"2026-09-07T19:04:00+07:00","country":"FI","market_or_entity":"Harvia Xenio/XE/Fenix controller migration","person_or_company":"Harvia","role":"manufacturer/support","source_type":"docs","source_url":"https://support.harvia.com/hc/fi/articles/22158926984732","published_at":"2026-02-23","palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"Etäohjaus on mahdollista erikseen hankittavalla lisävarustepaketilla","detailed_claim":"Harvia distinguishes remote-control and upgrade paths across Fenix FC, Xenio WiFi XW and Xenio XE systems; system generation changes required upgrade components.","quantitative_claims":[],"state_before":"legacy/current Harvia control state varies by generation","action_taken":"manufacturer transitioned product/control stack and documented upgrade paths","observed_agent_behavior":"UNKNOWN","outcome":"multi-variable replacement/upgrade decision exists","time_horizon":"current 2026 transition","mechanism":"controller generation and accessory/safety state determine successor bundle","moat_implication":"a compatibility graph is more valuable than a flat catalog if merchants do not encode serial/board state","h1":"Finnish legacy Harvia owners face unresolved successor decision friction","h0":"Harvia + specialists already resolve common configurations","falsifier":"20-case benchmark with >=90% exact resolution from existing Finnish sources","belief_delta":"FOR","next_best_test":"benchmark 20 legacy configurations","novelty_reason":"new ecosystem and stateful-control migration mechanism","independence_cluster":"harvia_primary"}

{"record_id":"ANC-20260907-1904-02","probe":"agent_native_commerce","observed_at":"2026-09-07T19:04:00+07:00","country":"FI","market_or_entity":"Harvia Fenix FX001XW upgrade retail","person_or_company":"Huolto Vuorio","role":"Finnish parts specialist","source_type":"other","source_url":"https://www.huoltovuorio.fi/fi/tuote/harvia-fenix-wifi-ohjauspaneeli-fx001xw/","published_at":null,"palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"Harvia Fenix ohjaimella korvaat vanhan Harvia Xenio ohjaimen vaivattomasti.","detailed_claim":"Finnish specialist directly markets Fenix FX001XW as a replacement for Xenio and lists live price and delivery estimate, proving local commerce already serves at least the simple migration path.","quantitative_claims":[{"metric":"retail_price","value":"€367.90","denominator":"one FX001XW panel","timeframe":"observed 2026-09-07","caveat":"retail price; supplier cost unknown"}],"state_before":"Xenio owner needs replacement/upgrade","action_taken":"merchant offers Fenix replacement","observed_agent_behavior":"UNKNOWN","outcome":"simple Xenio→Fenix path commercially served","time_horizon":"current","mechanism":"direct successor commerce","moat_implication":"weakens generic store thesis; pushes wedge toward difficult serial/board/legacy cases","h1":"merchant gap exists in complex legacy cases","h0":"merchant guidance covers nearly all cases","falsifier":"benchmark exact configurations","belief_delta":"AGAINST","next_best_test":"test cases beyond simple Xenio panel replacement","novelty_reason":"first Finnish merchant counterevidence","independence_cluster":"huolto_vuorio"}

{"record_id":"ANC-20260907-1904-03","probe":"agent_native_commerce","observed_at":"2026-09-07T19:04:00+07:00","country":"DE","market_or_entity":"Harvia Fenix serial/power-card compatibility","person_or_company":"PEQU","role":"sauna specialist merchant","source_type":"other","source_url":"https://pequ.eu/en/products/harvia-fenix-wifi-bedienteil-fx001wg","published_at":null,"palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"Plug-and-Play-Upgrade für Ihr vorhandenes Xenio-Saunasteuergerät.","detailed_claim":"Merchant publishes compatible controller families plus XE and Xenio serial/power-card thresholds, demonstrating both real compatibility complexity and a high-quality incumbent benchmark.","quantitative_claims":[{"metric":"retail_price","value":"€279","denominator":"FX001XW","timeframe":"observed 2026-09-07","caveat":"German/EU merchant"}],"state_before":"legacy Xenio/XE owner","action_taken":"merchant encodes serial/power-card eligibility","observed_agent_behavior":"UNKNOWN","outcome":"complex migration can be made machine-readable","time_horizon":"current","mechanism":"serial/board-aware compatibility","moat_implication":"the graph itself is useful but merchant differentiation depends on covering more systems/geographies than competent incumbents","h1":"Finnish commerce under-encodes these state variables","h0":"equally good Finnish sources exist","falsifier":"Finnish merchant audit finds equivalent coverage","belief_delta":"FOR","next_best_test":"compare Finnish top merchants against PEQU benchmark","novelty_reason":"new exact serial/board evidence","independence_cluster":"pequ"}

{"record_id":"ANC-20260907-1904-04","probe":"agent_native_commerce","observed_at":"2026-09-07T19:04:00+07:00","country":"NO","market_or_entity":"Mitsubishi heat-pump replacement remotes","person_or_company":"Mitsubishi Electric Norway","role":"manufacturer/direct merchant","source_type":"other","source_url":"https://mee.no/produkt/fjernkontroll-til-kirigamine-hara/","published_at":null,"palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"Passer til følgende modeller","detailed_claim":"Official manufacturer store maps exact remote to MSZ-FH25VE/FH35VE/FH50VE and sells directly, representative of several model-specific remote pages.","quantitative_claims":[{"metric":"retail_price","value":"NOK 575","denominator":"SG13A remote","timeframe":"observed 2026-09-07","caveat":"official retail"}],"state_before":"lost/failed remote","action_taken":"official model mapping + ecommerce","observed_agent_behavior":"UNKNOWN","outcome":"replacement decision substantially solved","time_horizon":"current","mechanism":"simple model-to-SKU mapping","moat_implication":"not defensible enough for agent-native specialist commerce","h1":"remote compatibility creates commerce wedge","h0":"official mapping commoditizes it","falsifier":"already falsified by direct mapping and multiple sellers","belief_delta":"STRONGLY_AGAINST","next_best_test":"none; reallocate","novelty_reason":"new killed category","independence_cluster":"mitsubishi_no"}

{"record_id":"ANC-20260907-1904-05","probe":"agent_native_commerce","observed_at":"2026-09-07T19:04:00+07:00","country":"NO","market_or_entity":"legacy marine transducer/display migration","person_or_company":"Garmin","role":"manufacturer","source_type":"docs","source_url":"https://www.garmin.com/en-GB/p/748/","published_at":null,"palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"When using with an 8-pin Garmin sounder, transducer adapter cable part number 010-11613-00 is required.","detailed_claim":"Garmin explicitly maps a legacy 6-pin transducer to an adapter requirement for 8-pin sounders and names a preferred successor transducer.","quantitative_claims":[{"metric":"retail_price","value":"£64.99","denominator":"010-10272-00 transducer","timeframe":"observed 2026-09-07","caveat":"UK Garmin price; not Norway"}],"state_before":"legacy sensor with newer display","action_taken":"manufacturer documents adapter/successor","observed_agent_behavior":"UNKNOWN","outcome":"migration complexity exists but is partially solved","time_horizon":"current","mechanism":"connector/network generation compatibility","moat_implication":"cross-brand graph may help, but manufacturer data weakens single-brand commerce moat","h1":"cross-brand Norwegian migration remains underserved","h0":"specialist merchants already solve it","falsifier":"20-case local merchant benchmark","belief_delta":"NEUTRAL","next_best_test":"benchmark Norwegian legacy configurations","novelty_reason":"new lifecycle category","independence_cluster":"garmin_primary"}

PRODUCT-OPPORTUNITY JSON

{"country":"FI","ecosystem":"sauna heating/control","product_or_family":"Harvia legacy controller/power-unit → Fenix/Xenio successor bundles","installed_base":"Finland approximately 3 million saunas at national order-of-magnitude; Harvia controller-generation installed base UNKNOWN","lifecycle_trigger":"controller failure, power-unit failure, smart-control upgrade, Xenio/Fenix transition, legacy analog-control replacement","total_sellers":"UNKNOWN","good_sellers":"at least 2 observed with useful guidance; full count UNKNOWN","merchant_gap":"MEDIUM/UNKNOWN","content_gap":"MEDIUM","search_demand":"community recurrence + active manufacturer transition; volume UNKNOWN","retail_price":"FX001XW observed ~€279–€368 across EU/FI merchants","supplier_cost":"UNKNOWN","break_even_cac":"UNKNOWN","h1":"stateful legacy-system migration is insufficiently resolved by Finnish commerce and can support a specialist decision engine plus parts bundles","h0":"Harvia and existing specialists already solve nearly all common configurations","falsifier":"20 representative legacy configurations are resolved correctly without human escalation by top existing Finnish sources in >=90% of cases","status":"OPEN"}

{"country":"NO","ecosystem":"marine electronics","product_or_family":"legacy sonar transducer/display adapters and successor sensors","installed_base":"UNKNOWN","lifecycle_trigger":"chartplotter/display upgrade while retaining or replacing old transducer","total_sellers":"UNKNOWN","good_sellers":"multiple competent local sellers observed","merchant_gap":"LOW/MEDIUM","content_gap":"MEDIUM","search_demand":"technical community recurrence; volume UNKNOWN","retail_price":"examples from ~NOK 1,509 for Garmin GT20-TM; converter modules much higher; exact category distribution UNKNOWN","supplier_cost":"UNKNOWN","break_even_cac":"UNKNOWN","h1":"cross-brand legacy migration remains sufficiently fragmented for a selector","h0":"manufacturer + specialist retailer compatibility data already solves purchase decisions","falsifier":"20 legacy configurations resolved from local commerce without escalation","status":"OPEN"}

{"country":"NO","ecosystem":"heat pumps","product_or_family":"Mitsubishi replacement remotes/controllers","installed_base":"UNKNOWN","lifecycle_trigger":"lost or failed remote","total_sellers":"multiple observed","good_sellers":"multiple","merchant_gap":"LOW","content_gap":"LOW","search_demand":"UNKNOWN","retail_price":"official remotes observed NOK 473–683; other original parts higher","supplier_cost":"UNKNOWN","break_even_cac":"UNKNOWN","h1":"compatibility friction supports specialist commerce","h0":"official model-to-part mapping commoditizes the decision","falsifier":"met — official manufacturer direct store provides exact mappings","status":"FALSIFIED"}

{"country":"GB","ecosystem":"caravan/motorhome heating controls","product_or_family":"Truma CP Plus replacement/retrofit panels","installed_base":"UNKNOWN","lifecycle_trigger":"failed control panel or legacy system upgrade","total_sellers":"multiple specialist sellers observed","good_sellers":"multiple","merchant_gap":"LOW","content_gap":"LOW/MEDIUM","search_demand":"UNKNOWN","retail_price":"~£116.99–£147.75 in observed specialist listings","supplier_cost":"UNKNOWN","break_even_cac":"UNKNOWN","h1":"PCB/connector/version complexity creates specialist commerce whitespace","h0":"existing caravan specialists already encode the decisive constraints","falsifier":"met sufficiently for current run — specialist listings already surface PCB version, ports and system compatibility","status":"FALSIFIED"}

END REPORT
