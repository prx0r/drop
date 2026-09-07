# Gold Probe — Agent-Native Supplier OS — 2026-09-07 18:24 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 07:26:59 -0400

# Gold Probe — Agent-Native Supplier OS

## 1. EXECUTIVE ALPHA

### 1) The strongest new evidence this hour is for thesis C — but in a narrower form than originally assumed.
A first-hand 2026 roofing deployment reported that the AI receptionist’s automatically generated lead spreadsheet became unexpectedly valuable because it captured *every* caller, including non-bookers, outside-service-area callers, after-hours callers, stale leads and jobs that never progressed. The operator later mined old records for follow-up and recovered work from leads months later. This is the clearest field evidence so far that the AI front desk can create a proprietary exhaust layer that did not previously exist in the contractor’s workflow.

The important implication is that the moat is probably **not “we know the contractor’s calendar.”** Incumbent vertical CRMs increasingly have calendar/customer/job data already. The new asset is closer to **demand exhaust + rejection reasons + timing + service-area mismatch + unbooked intent + recovery history**, normalized across many fragmented contractors.

### 2) Standalone AI phone answering is already commoditizing outside the US.
Eliocall now publicly claims 120+ equipped professionals in France, a 4.9/5 customer rating, launch pricing from €149/month, setup commonly within 24 hours, live calendar access, qualification, call summaries, routing and multilingual support. Its own public product page says it is already serving plumbers, electricians, heating engineers, restaurants, property agencies and other SMBs.

This is strategically important because it means “free AI receptionist” is becoming a **distribution wedge**, not a product moat. The technical feature set is quickly becoming table stakes.

### 3) The adoption bottleneck is moving from voice quality to trust, distribution and workflow integration.
A first-hand founder/operator post about a French trades-focused AI receptionist reported ~120 paying customers and said the AI itself was the easy part; the hard parts were telecom regulation, convincing older tradespeople to trust it, and acquiring customers. The founder reported cold-calling tradespeople at roughly one deal per 50 calls. That is materially different from the earlier US evidence: it suggests **sales/distribution friction may exceed technical friction** in fragmented trades.

### 4) The market is now crowded enough that “AI receptionist for plumbers/HVAC” is itself a weak startup thesis.
A July 2026 builder seeking validation for another contractor receptionist was told by community members that the category was already extremely competitive. A separate plumber/electrician/HVAC seller charging $500 setup + $300 recurring reported trouble landing clients. This is low-grade evidence, but it points in the same direction as the official product proliferation: the wedge must be deeper than voice answering.

### 5) Housecall Pro is pushing AI deeper into the system-of-record layer.
Housecall Pro’s July 22, 2026 AI Team documentation says AI teammates are now available directly inside accounts, with most enabled by default; CSR AI is the optional 24/7 call-answering add-on. This weakens the thesis that a standalone Supplier OS can win solely by replacing the front desk. Incumbent FSM systems can bundle AI against their existing customer/job/calendar data.

**Updated thesis:**

> The best Supplier OS wedge is not “AI receptionist.” It is **free/cheap workflow capture that creates a cross-contractor demand-and-capacity graph incumbents cannot see across businesses**: rejected jobs, service-area misses, urgency, requested job types, quote ranges, time-to-accept, unserved demand, booking outcomes and recovery outcomes.

---

## 2. NEW CONTRACTOR VERTICAL × COUNTRY CELLS

| Country | Vertical | New evidence | Adoption | ROI | Data-flywheel potential | Status |
|---|---|---|---|---|---|---|
| FR | Plumbers / electricians / heating engineers | Eliocall says 120+ pros equipped; €149+/mo; 24h setup; calendars + qualification + summaries | SUPPORTED | PARTIALLY SUPPORTED; product claims not independently audited | HIGH if call outcomes/rejections normalized | OPEN |
| US | Roofing | First-hand 4-month deployment reports 2–3 extra jobs/week and unexpected value from full call/lead ledger | SUPPORTED, evidence=B | SUPPORTED directionally, exact economics incomplete | VERY HIGH: unbooked + outside-area + after-hours + stale lead history | SUPPORTED |
| US | Painting / concrete | Same implementer says pattern repeated after roofing | WEAK-POSITIVE | UNKNOWN | MEDIUM-HIGH if replicated with real records | OPEN |
| US | Multi-trade Housecall Pro users | AI layer increasingly native to FSM | HIGH incumbent adoption | incumbent ROI proposition strong | LOW for basic customer/job/calendar data; potential only in cross-business external graph | THESIS C NARROWED |

---

## 3. FIELD EVIDENCE TABLE

### ANSO-20260907-1801 — Roofing call-exhaust graph
**Palace proximity:** 78/100  
**Evidence grade:** B — first-hand implementer describing a real contractor deployment, but not independently audited.

**Source:** Reddit, r/AiForSmallBusiness, May 14 2026  
https://www.reddit.com/r/AiForSmallBusiness/comments/1td7kvv/built_an_ai_receptionist_for_a_roofer_who_missed/

**Exact words:** “The lead spreadsheet I almost didn't build... Turned out to be one of the most valuable pieces of the whole thing.”

**Detailed claim:** The system captured every call and outcome into a spreadsheet. The contractor discovered visibility into booked calls, non-bookers, callers outside the service area, after-hours demand and stale leads, then used old records for outbound recovery. The author reports the roofer now books 2–3 additional jobs per week and pays $350/month. They also state the same pattern appeared in painting and concrete deployments.

**Mechanism:** voice front desk → comprehensive demand-event log → previously invisible lost/rejected demand becomes queryable → recovery + future routing + supply intelligence.

**Moat implication:** Strongest evidence yet for PROPRIETARY_SUPPLY_GRAPH, but specifically at the *unserved-demand/event-history* layer rather than generic CRM fields.

**Belief delta:** STRONGLY_FOR thesis C, FOR thesis A/B.

---

### ANSO-20260907-1802 — France: receptionist category already commercial
**Palace proximity:** 90/100  
**Evidence grade:** A for product/adoption claims as first-party company disclosure; B for effectiveness claims.

**Source:** Eliocall official site, observed Sep 7 2026  
https://eliocall.com/

**Exact words:** “Déjà +120 pros équipés en France” and “dès 149 €/mois.”

**Detailed claim:** Eliocall says it has 120+ equipped professionals in France, a 4.9/5 rating, starting pricing of €149/month, typical setup in under 24 hours, calendar access, real-time booking, qualification, SMS/WhatsApp/email summaries, contextual transfer, multilingual handling and European/French hosting. It targets plumbers, electricians, heating engineers and multiple adjacent service verticals.

**Mechanism:** low-friction verticalized onboarding + local language/regulatory positioning + complete basic phone workflow.

**Moat implication:** Basic reception/booking is commoditizing. Local trust/compliance and distribution can still differentiate, but they are not durable data moats by themselves.

**Belief delta:** FOR adoption; AGAINST “voice receptionist is defensible.”

---

### ANSO-20260907-1803 — Founder reports distribution > AI difficulty
**Palace proximity:** 82/100  
**Evidence grade:** B — claimed founder/operator metrics, partially corroborated by official site.

**Source:** Reddit / SideProject, Aug 3 2026  
https://www.reddit.com/r/SideProject/comments/1venlw9/i_built_an_ai_receptionist_for_tradespeople_and/

**Exact words:** “the AI part was the easy bit.”

**Detailed claim:** The poster says the French trades receptionist reached around 120 paying customers. They report telecom-number regulation, trust among older plumbers/electricians and distribution as the major constraints; cold calling reportedly closes about one deal per 50 calls. The 120-customer claim is directionally corroborated by Eliocall’s current public site.

**Mechanism:** technical commoditization shifts competitive bottleneck to trust, local compliance, onboarding and channel distribution.

**Moat implication:** A free Supplier OS must have a radically cheap acquisition path or piggyback on an existing contractor channel. Product-led signup alone may not overcome trust friction.

**Belief delta:** AGAINST easy adoption at scale despite product utility; FOR localized vertical go-to-market.

---

### ANSO-20260907-1804 — FSM incumbents bundle AI into system of record
**Palace proximity:** 95/100  
**Evidence grade:** A — current first-party product documentation.

**Source:** Housecall Pro Help Center, Jul 22 2026  
https://help.housecallpro.com/en/articles/9311875-ai-team-overview

**Exact words:** “The AI Team is now available for Housecall Pro accounts.”

**Detailed claim:** Housecall Pro now embeds an AI Team directly into customer accounts. Most AI teammates are included and enabled by default; CSR AI is an optional 24/7 call-answering add-on. This places AI inside an incumbent FSM already holding jobs, customers, schedules and business workflows.

**Mechanism:** incumbent system-of-record bundles automation into existing data and workflow distribution.

**Moat implication:** Generic CRM/calendar/job-history ingestion is not proprietary enough. A new entrant needs information incumbents do not naturally observe across companies.

**Belief delta:** STRONGLY_AGAINST generic Supplier OS differentiation; STRONGLY_FOR cross-company demand graph thesis.

---

## 4. EXACT WORDS

1. Roofing implementer, May 2026: **“The lead spreadsheet I almost didn't build... Turned out to be one of the most valuable pieces of the whole thing.”**  
Source: https://www.reddit.com/r/AiForSmallBusiness/comments/1td7kvv/built_an_ai_receptionist_for_a_roofer_who_missed/

2. Eliocall founder/operator post, Aug 2026: **“the AI part was the easy bit.”**  
Source: https://www.reddit.com/r/SideProject/comments/1venlw9/i_built_an_ai_receptionist_for_tradespeople_and/

3. Housecall Pro, Jul 2026: **“The AI Team is now available for Housecall Pro accounts.”**  
Source: https://help.housecallpro.com/en/articles/9311875-ai-team-overview

4. Eliocall official site: **“Déjà +120 pros équipés en France.”**  
Source: https://eliocall.com/

---

## 5. ADOPTION EVIDENCE

### Stronger this run
- France now has a locally positioned trades/SMB AI receptionist publicly claiming 120+ equipped pros and €149+/month pricing.
- Roofing first-hand case reports four months of sustained use and 2–3 extra jobs per week.
- Housecall Pro has moved AI directly inside existing FSM accounts.

### Friction that remains
- French founder/operator says trust among older tradespeople is harder than model quality.
- Reported cold-calling efficiency of roughly 1 customer per 50 calls suggests acquisition can dominate economics.
- August 2026 roofing buyer explicitly says cost is secondary to “spin up quickly and not have to oversee,” suggesting setup/maintenance burden is an adoption variable distinct from price.

---

## 6. ROI / UNIT-ECONOMIC EVIDENCE

### Evidence-backed
- Roofing implementer reports 2–3 incremental jobs/week from the deployment; reported service price: $350/month.
- Eliocall public pricing begins at €149/month.

### Still UNKNOWN
- Gross incremental contribution per recovered roofing job.
- Retention/churn for Eliocall’s 120+ professionals.
- CAC/payback for French cold-call acquisition.
- Incremental revenue attributable to Eliocall rather than merely calls handled.
- Whether low-volume trades justify an always-on agent after call capture becomes ubiquitous in incumbent software.

**ROI thesis status:** SUPPORTED for high-value missed-call verticals, not proven universally.

---

## 7. DATA-FLYWHEEL EVIDENCE

### Strong new mechanism
The roofing case exposes a richer proprietary object than the original proposed graph:

**Demand Event**
- caller / timestamp
- geography
- requested service
- urgency
- acquisition source if known
- booking requested Y/N
- booked Y/N
- reason not booked
- outside service area Y/N
- unavailable slot / capacity conflict
- quoted / not quoted
- price/range if given
- human escalation Y/N
- follow-up required
- subsequent recovery
- eventual job outcome

Across hundreds of contractors this can generate:
- real demand by postcode × hour × service;
- unmet-demand hotspots;
- service-area mismatch;
- capacity shortages;
- categories contractors reject;
- actual response/booking behavior;
- seasonality;
- price-response curves where lawful/observable;
- reliability/completion history if later workflow data is captured.

This is substantially more defensible than a static contractor directory.

### Key danger
If each incumbent FSM logs the same information and exposes cross-customer benchmarking, the moat shrinks. The unique asset must therefore be **cross-platform + cross-contractor + transaction/rejection-history normalized**, ideally acquired through being the neutral front door.

---

## 8. COMPETITOR / SUBSTITUTE MAP

| Layer | Evidence this run | Strategic interpretation |
|---|---|---|
| Basic voice answering | Eliocall €149+, 120+ pros | Commoditizing |
| Booking/calendar | Eliocall + Housecall Pro | Commoditizing |
| CRM/job system | Housecall Pro | Incumbent advantage |
| Qualification | Eliocall + multiple platforms | Commoditizing |
| Call summaries/logs | Eliocall / roofing DIY deployment | Commodity individually |
| Cross-business rejected-demand history | No dominant incumbent found this run | Potential moat |
| Cross-platform capacity/service graph | No dominant incumbent found this run | Potential moat |
| Acquisition/distribution to small trades | Eliocall founder says hard | Core execution risk |

---

## 9. HARD FALSIFICATIONS / NULL RESULTS

### KILL: “AI receptionist itself is the product moat.”
Evidence now weighs strongly against this. Multiple vertically integrated and standalone products offer the core bundle.

### WEAKEN: “Free receptionist guarantees easy contractor adoption.”
Utility is not the only barrier. Trust, telecom setup, local regulation, onboarding and distribution remain meaningful.

### WEAKEN: “Calendar + price + customer data automatically becomes proprietary.”
Incumbent FSMs already possess much of this. The new entrant’s moat must come from data incumbents cannot see, especially cross-business unmet demand and routing/outcome history.

### OPEN: “Rejected-demand exhaust is valuable enough to justify giving software away.”
This is now the highest-value Supplier OS hypothesis and requires a live experiment.

---

## 10. HYPOTHESIS LEDGER

### A — ADOPTION
**H1:** Fragmented trades contractors with meaningful missed-call volume will adopt a managed AI front desk when setup burden is near zero and it integrates into their existing number/calendar.

**H0:** Trust, customer preference, onboarding and distribution friction outweigh missed-call ROI for enough small contractors that adoption remains expensive.

**Evidence for:** 120+ Eliocall pros; roofing deployment; ServiceTitan/Housecall Pro category movement.

**Evidence against:** French founder reports distribution and trust harder than AI; cold-call close rate allegedly ~1/50.

**Belief:** FOR.

**Falsifier:** In a 30-contractor targeted trial, <20% activate after a zero-cost managed setup and <50% of activated users retain after 60 days despite demonstrable missed calls.

**Next best test:** 30 managed installs across three trades, recording activation/retention and onboarding minutes.

### B — ROI
**H1:** In high-ticket emergency/inspection trades, recovered missed/after-hours calls create contribution well above the marginal cost of voice automation.

**H0:** Many recovered calls are spam, low-intent, outside service area or would have converted later anyway, making apparent booking uplift economically weak.

**Evidence for:** roofing implementer claims 2–3 extra jobs/week; prior ServiceTitan evidence shows high booking rates in HVAC/plumbing.

**Evidence against:** no audited gross contribution or counterfactual in the roofing case.

**Belief:** FOR, not calibrated.

**Falsifier:** controlled before/after or holdout shows recovered-call gross contribution <2× total platform/voice/support cost after 60 days.

**Next best test:** missed-call holdout by time window or rotating call-forward experiment.

### C — DATA FLYWHEEL
**H1:** The front desk can accumulate a cross-contractor demand exhaust—especially rejected/unbooked demand, geography, urgency, service type, timing and recovery outcomes—that incumbent single-business FSMs cannot reproduce.

**H0:** contractors’ incumbent CRMs already capture enough of this, data rights prevent aggregation, or records are too noisy/inconsistent to become commercially useful.

**Evidence for:** roofing deployment discovered unexpected value from full lead spreadsheet; Housecall Pro evidence clarifies what incumbent-owned data looks like and therefore where whitespace remains.

**Belief:** STRONGLY_FOR as a mechanism worth testing; commercial value still UNKNOWN.

**Falsifier:** after 25 live contractors, <60% of call events can be normalized into stable service/geography/outcome fields OR >80% of those fields are already exportable from incumbent systems with equal coverage.

**Next best test:** ingest 5,000 real call events from 20–30 contractors and measure normalization completeness, unique-field share vs incumbent CRM exports, and whether rejected-demand patterns predict bookable overflow opportunities.

---

## 11. WHO TO WATCH NEXT

- **Eliocall founders/team** — unusually valuable because they are already at ~120 French professionals and appear directly exposed to trades trust/distribution problems.
- **Housecall Pro AI Team / CSR AI product group** — shows how quickly system-of-record incumbents absorb reception and workflow automation.
- **Independent roofing/trades voice-agent deployers** — especially those publishing full call logs, booking/non-booking distributions and retention rather than demos.
- **Cross-contractor overflow / dispatch networks** — strategically important next source class because they may reveal whether rejected demand is already monetized elsewhere.

---

## 12. NOVELTY AUDIT

Prior Supplier OS report focused heavily on ServiceTitan’s Bill Joplin / Superior Plumbing evidence and concluded that reception itself is commoditizing while proprietary supply data matters more.

### Genuinely new this run
- France-specific commercialization: Eliocall 120+ pros, €149+/month, current local feature set.
- First-hand founder report that distribution/trust/telecom regulation are harder than AI, with claimed ~1/50 cold-call conversion.
- Roofing call-ledger case revealing *unbooked/rejected/stale demand exhaust* as an emergent data asset.
- Housecall Pro’s July 2026 AI-Team bundling as direct evidence of incumbent system-of-record encroachment.
- Refined data-moat thesis from generic “availability/pricing graph” to **cross-business demand-event + rejection + capacity history**.

### Semantic duplicates rejected
- Repeated ServiceTitan 80–90% booking-rate stories already used in the previous report.
- Generic “contractors miss calls” posts with no deployment/outcome data.
- AI receptionist builders asking for beta users without real adoption or results.
- Generic product announcements without workflow/outcome evidence.

Estimated substantive novelty vs prior run: >80%.

---

## 13. SOURCE-YIELD LEDGER

| Source family | Useful reads | Accepted | Material belief changes | Next action |
|---|---:|---:|---:|---|
| First-hand Reddit implementers | 8+ | 2 | 2 | EXPLOIT selectively; high noise but excellent unexpected mechanisms |
| Official vertical SaaS docs | 4+ | 1 | 1 | EXPLOIT; strong for incumbent boundary |
| Official AI receptionist operator sites | 3+ | 1 | 1 | EXPLOIT for adoption/pricing, discount marketing ROI claims |
| Generic AI receptionist communities | several | 0 | 0 | DEPRIORITIZE unless actual logs/retention/economics |
| ServiceTitan | rechecked | 0 new | 0 | TEMPORARILY DEPRIORITIZE due prior-run saturation |

---

## 14. JSONL — COMMON SCHEMA

```jsonl
{"record_id":"ANSO-20260907-1801","probe":"agent_native_supplier_os","observed_at":"2026-09-07T18:24:00+07:00","country":"US","market_or_entity":"roofing AI front desk / demand exhaust","person_or_company":"independent implementer + roofing contractor","role":"first-hand AI receptionist implementer","source_type":"reddit","source_url":"https://www.reddit.com/r/AiForSmallBusiness/comments/1td7kvv/built_an_ai_receptionist_for_a_roofer_who_missed/","published_at":"2026-05-14","palace_proximity_score":78,"evidence_grade":"B","verbatim_excerpt":"The lead spreadsheet I almost didn't build... Turned out to be one of the most valuable pieces of the whole thing.","detailed_claim":"Four-month roofing deployment reportedly books 2-3 extra jobs/week; full call ledger exposed booked, non-booked, outside-area, after-hours and stale demand that the contractor later mined for recovery. Author reports similar pattern in painting and concrete.","quantitative_claims":[{"metric":"incremental_jobs","value":"2-3 per week","denominator":"roofing deployment","timeframe":"reported after four months","caveat":"self-reported, not independently audited"},{"metric":"service_price","value":"$350/month","denominator":"deployment","timeframe":"May 2026","caveat":"reported in thread"}],"state_before":"missed calls largely invisible","action_taken":"AI answers, qualifies, books to Google Calendar and logs every call","observed_agent_behavior":"captures structured caller/service/booking events","outcome":"reported incremental jobs plus reusable stale/rejected lead history","time_horizon":"4 months","mechanism":"front desk creates demand-event exhaust absent from prior workflow","moat_implication":"cross-contractor rejected-demand and recovery history may be more defensible than generic CRM fields","h1":"front-desk exhaust creates proprietary cross-contractor demand graph","h0":"data is already present in incumbent CRMs or too noisy to monetize","falsifier":"<60% normalization completeness or >80% field duplication vs incumbent CRM exports in a 5k-call sample","belief_delta":"STRONGLY_FOR","next_best_test":"ingest 5,000 real calls across 20-30 contractors and compare unique normalized fields with incumbent exports","novelty_reason":"first evidence this series that an accidental call ledger itself became a valuable operational asset","independence_cluster":"reddit_roofing_implementer_2026-05"}
{"record_id":"ANSO-20260907-1802","probe":"agent_native_supplier_os","observed_at":"2026-09-07T18:24:00+07:00","country":"FR","market_or_entity":"trades AI receptionist","person_or_company":"Eliocall","role":"AI receptionist operator","source_type":"docs","source_url":"https://eliocall.com/","published_at":null,"palace_proximity_score":90,"evidence_grade":"A","verbatim_excerpt":"Déjà +120 pros équipés en France","detailed_claim":"Eliocall publicly claims 120+ equipped professionals, 4.9/5 rating, plans from €149/month, rapid setup, live calendar booking, qualification, contextual transfer and call summaries for French trades/SMBs.","quantitative_claims":[{"metric":"equipped_professionals","value":"120+","denominator":"France","timeframe":"observed Sep 2026","caveat":"first-party disclosure"},{"metric":"starting_price","value":"€149/month","denominator":"plan","timeframe":"Sep 2026","caveat":"first-party current pricing"}],"state_before":"UNKNOWN","action_taken":"deploy verticalized AI receptionist","observed_agent_behavior":"answers, qualifies, accesses calendars, books, routes, summarizes","outcome":"120+ professionals publicly claimed equipped","time_horizon":"UNKNOWN","mechanism":"localized low-friction receptionist product","moat_implication":"basic reception and booking are commoditizing","h1":"trades adopt localized managed AI reception","h0":"adoption remains niche due trust/workflow friction","falsifier":"high churn or weak active-use rate despite customer count","belief_delta":"FOR","next_best_test":"obtain active-call volume, retention and per-vertical cohort metrics","novelty_reason":"new non-US commercial adoption evidence","independence_cluster":"eliocall_first_party_2026-09"}
{"record_id":"ANSO-20260907-1803","probe":"agent_native_supplier_os","observed_at":"2026-09-07T18:24:00+07:00","country":"FR","market_or_entity":"trades AI receptionist distribution","person_or_company":"Eliocall founder/operator claim","role":"founder/operator","source_type":"reddit","source_url":"https://www.reddit.com/r/SideProject/comments/1venlw9/i_built_an_ai_receptionist_for_tradespeople_and/","published_at":"2026-08-03","palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"the AI part was the easy bit.","detailed_claim":"Founder/operator reports ~120 paying customers and says telecom regulation, trust among older tradespeople and distribution were harder than the AI; cold calling reportedly closes about one customer per 50 calls. Customer-count claim is directionally corroborated by company website.","quantitative_claims":[{"metric":"paying_customers","value":"~120","denominator":"company","timeframe":"Aug 2026","caveat":"self-reported; official site now says 120+ equipped"},{"metric":"cold_call_close_rate","value":"~1/50","denominator":"cold calls","timeframe":"reported Aug 2026","caveat":"self-reported, denominator details unavailable"}],"state_before":"working product","action_taken":"cold-call and onboard French trades","observed_agent_behavior":"UNKNOWN","outcome":"customer acquisition constrained by trust/distribution","time_horizon":"UNKNOWN","mechanism":"technical commoditization shifts bottleneck to trust/distribution","moat_implication":"free software alone may not solve CAC; channel access is strategic","h1":"zero-friction front desk yields cheap contractor acquisition","h0":"trust and distribution keep CAC high despite clear utility","falsifier":"managed zero-cost trials produce >30% activation from warm trade-channel distribution","belief_delta":"AGAINST","next_best_test":"compare cold outbound vs trade-association/manufacturer/channel partner acquisition cohorts","novelty_reason":"first quantified distribution-friction evidence in France","independence_cluster":"eliocall_founder_reddit_2026-08"}
{"record_id":"ANSO-20260907-1804","probe":"agent_native_supplier_os","observed_at":"2026-09-07T18:24:00+07:00","country":"US","market_or_entity":"Housecall Pro AI Team","person_or_company":"Housecall Pro","role":"vertical field-service software operator","source_type":"docs","source_url":"https://help.housecallpro.com/en/articles/9311875-ai-team-overview","published_at":"2026-07-22","palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"The AI Team is now available for Housecall Pro accounts.","detailed_claim":"Housecall Pro embeds multiple AI teammates directly into existing accounts; most are enabled by default, while CSR AI is an optional 24/7 call-answering add-on. Incumbent therefore combines AI with existing customer/job/calendar data.","quantitative_claims":[],"state_before":"FSM system of record","action_taken":"bundle AI workers into account","observed_agent_behavior":"supports answering/booking/reporting and other account workflows","outcome":"AI functionality distributed through incumbent installed base","time_horizon":"current as of Jul-Sep 2026","mechanism":"system-of-record incumbent bundles agent capability","moat_implication":"generic customer/job/calendar data is weak differentiation; cross-business rejected-demand data becomes more important","h1":"standalone Supplier OS can differentiate on proprietary supply data","h0":"incumbent FSM systems absorb the whole value chain","falsifier":"incumbents expose equivalent cross-business normalized rejected-demand/capacity intelligence","belief_delta":"FOR","next_best_test":"compare event-level export schemas across Housecall Pro, Jobber, ServiceTitan and Workiz against proposed cross-contractor graph","novelty_reason":"new incumbent-boundary evidence not used in prior report","independence_cluster":"housecallpro_docs_2026-07"}
```

## SUPPLIER-OS OPPORTUNITY JSON

```json
[
  {
    "country":"US",
    "contractor_vertical":"roofing",
    "avg_job_value":"UNKNOWN",
    "pain_observations":["owner physically unreachable while on roofs","after-hours calls previously died in voicemail","unbooked/outside-area/stale calls became visible only after full call logging"],
    "incumbent_tools":["Google Calendar","generic spreadsheets","multiple AI receptionist vendors"],
    "verified_software_price":"$350/month reported for specific independent deployment",
    "adoption_h1":"roofers with meaningful missed-call volume will retain a managed front desk that requires near-zero oversight",
    "adoption_h0":"trust and workflow edge cases make retention weak despite initial utility",
    "adoption_falsifier":"<50% 60-day retention across a 20-roofer managed trial",
    "roi_h1":"recovered calls generate gross contribution materially above automation cost",
    "roi_h0":"recovered calls are mostly low-value/non-incremental",
    "roi_falsifier":"holdout-adjusted recovered gross contribution <2x platform cost",
    "data_flywheel_h1":"call exhaust creates proprietary rejected-demand, urgency, geography and recovery history that was previously invisible",
    "data_flywheel_h0":"existing CRM exports duplicate the useful fields or normalization is too noisy",
    "data_flywheel_falsifier":"<60% normalized completeness or >80% field duplication versus incumbent CRM exports",
    "proprietary_fields_possible":["availability","service_area","pricing","acceptance","completion","response_time","rejection_reason","unserved_demand","urgency","recovery_outcome"],
    "live_experiment_required":true,
    "status":"SUPPORTED"
  },
  {
    "country":"FR",
    "contractor_vertical":"plumbing/electrical/heating trades",
    "avg_job_value":"UNKNOWN",
    "pain_observations":["calls arrive while technician is working","trust in automated receptionist is an adoption variable","customer acquisition to trades is reportedly laborious"],
    "incumbent_tools":["Eliocall","human secretary","voicemail","calendar tools"],
    "verified_software_price":"Eliocall from €149/month",
    "adoption_h1":"localized managed receptionist can achieve meaningful adoption among French trades",
    "adoption_h0":"trust/distribution/regulation keep adoption expensive despite utility",
    "adoption_falsifier":"managed free trials fail to achieve >20% activation among qualified missed-call businesses",
    "roi_h1":"one or more recovered high-value jobs monthly can justify €149+ software cost",
    "roi_h0":"incremental recovered contribution is insufficient or cannibalized",
    "roi_falsifier":"measured incremental gross contribution <2x platform cost over 60 days",
    "data_flywheel_h1":"front-desk usage can produce live rejected-demand, service-area, job-type and booking-state events across fragmented French trades",
    "data_flywheel_h0":"data remains siloed or too inconsistent/legally constrained for cross-business aggregation",
    "data_flywheel_falsifier":"contract/data-rights constraints or normalization failures prevent aggregation across >20 businesses",
    "proprietary_fields_possible":["availability","service_area","pricing","acceptance","completion","response_time","rejection_reason","requested_service"],
    "live_experiment_required":true,
    "status":"OPEN"
  }
]
```

## HIGHEST-EVI NEXT TEST

**Build/borrow the front desk only long enough to test the graph.** Recruit 20–30 contractors across roofing, plumbing and electrical; capture ~5,000 inbound call events; normalize every call into service, postcode, urgency, requested date, booking outcome, non-booking reason, outside-area flag and eventual job outcome. Then compare those fields with exports from each contractor’s incumbent CRM.

The thesis advances only if the neutral front desk creates a **materially richer cross-business rejected-demand/capacity dataset** than the incumbents already hold. If it does not, kill the data-flywheel story rather than building another AI receptionist.
