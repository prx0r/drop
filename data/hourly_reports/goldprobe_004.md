# Gold Probe — Agent-Native Supplier OS — 2026-09-07 19:27 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 08:33:09 -0400

# Gold Probe — Agent-Native Supplier OS

Observed: 2026-09-07T19:27:32+07:00

## 1. EXECUTIVE ALPHA

### 1) Fresh ROI evidence clears the bar in garage-door / emergency home service, but it strengthens B more than C.
Workiz published a case on Gold Eagle Services in which Genius AI Answering generated **$23,758 in revenue from AI-handled conversations in 30 days**. Operator Keating Kuhn says the system answers in **under two minutes, 24/7** and can schedule jobs, add notes and cancel jobs. This is useful because it maps a concrete intervention to booked revenue rather than merely claiming that calls were answered.

Source: https://www.workiz.com/blog/case-study/gold-eagle-services-case-study/

Interpretation: B/ROI gets a meaningful positive update for high-intent inbound service businesses. It does **not** prove incremental revenue versus a controlled counterfactual, and it does not establish that an external Supplier OS owns the resulting data.

### 2) A second garage-door operator supplies more granular ROI evidence across phone + follow-up automation.
A recent Workiz case on a small garage-door company reports that owner Andre has **50 automations** handling estimate follow-up, pre-job reminders, post-job invoice follow-up, review requests and receipt delivery. His AI receptionist reportedly answered **500+ calls**, directly generating **$7,600**, plus **$3,600** attributed to automated text/email responses.

Source: https://www.workiz.com/blog/case-study/how-a-small-garage-door-company-uses-ai-to-outperform-industry-giants/

Interpretation: this is stronger evidence for the broader Supplier-OS workflow than reception alone. The valuable workflow surface extends from intake into quote follow-up, payment collection and reputation. But again, the value accrues inside Workiz unless a third-party layer owns the normalized event stream.

### 3) The operational graph we want is already becoming explicit inside incumbent FSMs.
Workiz documents automatic assignment using **technician availability + skills/job types + service areas**, with configurable advance notice from **1 hour to 7 days**. Service-area boundaries can be defined by ZIP-radius or custom area and enforced strictly by the answering agent. Workiz also exposes job, lead, lost-lead, team, time-off and payment operations through its developer API.

Sources:
- https://help.workiz.com/hc/en-us/articles/43952232552081-Automatically-assigning-jobs-to-techs-with-Genius-Answering
- https://help.workiz.com/hc/en-us/articles/39806226542353-Preventing-Genius-Answering-from-booking-outside-of-your-service-areas
- https://developer.workiz.com/

This is the most important update to thesis C. The data needed for a supply graph is technically real and structured, but it already exists in the contractor's system of record. A third-party Supplier OS needs to own a **cross-contractor event that incumbents cannot reconstruct**, not simply mirror schedules and jobs.

### 4) Australia/Simpro shows AI front-desk supply becoming crowded and price-bounded.
Simpro's marketplace now contains multiple AI receptionist/automation vendors. LANA publicly prices:
- AI receptionist: **$300/month + $1,000 training**
- AI qualifies call + books job: **$399/month + $1,500 training**
- CRM + AI receptionist + JMS: **$600/month + $3,500 workshops/training**

Its higher tier includes quote chasing, invoice chasing, review requests and rebooking. Separately, Supportiyo and CallCrewAI both offer Simpro-native call/booking/admin automation.

Sources:
- https://marketplace.simprogroup.com/apps/lana-software-ai-receptionist
- https://marketplace.simprogroup.com/apps/supportiyo
- https://marketplace.simprogroup.com/apps/callcrewai

Interpretation: A/adoption is plausible, but a generic AI front desk is rapidly becoming a marketplace feature category. Onboarding/training cost remains non-trivial, which matters for a free wedge.

### 5) Simpro's own bundling is an explicit strategic threat to standalone Supplier OS.
Simpro says its group serves **24,000+ trade businesses and 450,000 users** across the US, Australia and UK. Its Lightning upgrade bundles AI agents across collections follow-up, job preparation, payment processing and customer communication. Launch pricing was a **15% uplift**, moving to **25% post-promotion**.

Source: https://www.simprogroup.com/company/press/simpro-group-unveils-lightning

This attacks both the standalone product and the data moat: an incumbent already owns job history, schedules, quoting, invoicing and workforce state and can price AI as an increment on the core system.

### 6) Thesis C should be narrowed to demand-side exhaust the contractor/FSM does not naturally optimize for.
The highest-value proprietary fields are increasingly likely to be:

**requested service × postcode × requested time × urgency × qualification state × quoted/declined/not-served reason × contractor acceptance/rejection × eventual reroute/completion**.

The strongest unique events are the ones occurring **between businesses**, especially rejected/out-of-area/no-capacity demand and rerouting. A single contractor CRM knows its own lost lead; it does not know which nearby qualified contractor eventually accepted that exact job, at what lead time, and with what outcome.

**Current split:**
- A ADOPTION: SUPPORTED in several US home-service operator cases; still vertical/geography dependent.
- B ROI: SUPPORTED for selected high-intent inbound workflows, but vendor case-study bias remains material.
- C DATA FLYWHEEL: OPEN. Technical data generation is clearly feasible; defensible cross-contractor aggregation and permission are not yet proven.

---

## 2. NEW CONTRACTOR VERTICAL × COUNTRY CELLS

### US — Garage door / emergency home service
**Why interesting:** phone-led, urgent, schedulable, geography-bound, strong value of speed.

**Observed pain:** delayed callback loses urgent jobs; operator evidence emphasizes response speed.

**Observed workflow:** AI call answering -> qualification -> booking -> notes/cancellation -> follow-up automation -> invoice/review workflow.

**Verified outcome:** Gold Eagle case attributes $23,758 revenue to AI-handled conversations in 30 days. Separate garage-door case attributes $7,600 to 500+ AI-handled calls plus $3,600 to automated SMS/email.

**A status:** SUPPORTED, with vendor-case caveat.
**B status:** SUPPORTED, with attribution/counterfactual caveat.
**C status:** OPEN.

### Australia — Electrical/plumbing/roofing/remedial/fire businesses on Simpro
**Why interesting:** mature FSM installed base plus several independent AI-front-desk vendors means adoption plumbing exists.

**Observed workflow:** inbound qualification, job creation, quote chase, invoice chase, review request, service rebooking.

**Verified software economics:** LANA $300/$399/$600 monthly tiers, plus $1,000/$1,500/$3,500 setup/training depending on tier.

**A status:** OPEN-SUPPORTED directionally; marketplace presence is not usage/retention data.
**B status:** OPEN; no accepted operator ROI metric from LANA this run.
**C status:** AGAINST naïve version because Simpro remains the system of record.

### GLOBAL/US — Workiz-based home-service operators
**Why interesting:** Workiz exposes exactly the operational fields relevant to a supplier graph: lead status, jobs, technician assignment, service areas, time off, payment state and lead loss.

**A:** SUPPORTED by operator cases.
**B:** SUPPORTED in selected cases.
**C:** OPEN; API accessibility makes extraction possible but simultaneously lowers exclusivity.

---

## 3. FIELD EVIDENCE TABLE

| Rank | Evidence | Palace proximity | Novelty | Decision impact | Grade |
|---|---|---:|---|---|---|
| 1 | Gold Eagle Services: $23,758 revenue from AI-handled conversations in 30 days; sub-2-minute response | 90 | HIGH | Strong B/ROI update | A |
| 2 | Garage-door operator Andre: 500+ calls -> $7,600; automated text/email -> $3,600; 50 automations | 88 | HIGH | Broadens value beyond answering | A |
| 3 | Workiz assignment model: availability + skills + service area + advance-notice state | 95 | HIGH | Proves supply state can be represented structurally | A |
| 4 | Workiz API: jobs/leads/lost status/payments/team/time-off | 95 | HIGH | C technically feasible, but not exclusive | A |
| 5 | LANA/Simpro pricing and workflow tiers | 85 | HIGH | Establishes competitive price/onboarding bounds | A |
| 6 | Simpro Lightning: 24k businesses / 450k users; AI bundled at 15%-25% uplift | 95 | HIGH | Strong adversarial evidence vs standalone wedge | A |
| 7 | First-hand small-service owner tracked 47 missed calls in 30 days | 65 | MEDIUM | Pain validation only; outcome unknown | B |

---

## 4. EXACT WORDS

**Keating Kuhn / Gold Eagle Services operator, via Workiz:** “When Genius Answering answers the phone, it's able to schedule a job.”
Context: describing why the system functions as an operational front desk rather than message taking.
Source: https://www.workiz.com/blog/case-study/gold-eagle-services-case-study/

**Andre / garage-door operator, via Workiz:** “The automations are amazing in that they free me up.”
Context: operator says approximately 50 automations now cover recurring admin workflows.
Source: https://www.workiz.com/blog/case-study/how-a-small-garage-door-company-uses-ai-to-outperform-industry-giants/

**Workiz documentation:** “Availability (openings in their schedule that accommodate the job duration)”
Context: one of the explicit inputs for AI technician assignment.
Source: https://help.workiz.com/hc/en-us/articles/43952232552081-Automatically-assigning-jobs-to-techs-with-Genius-Answering

**First-hand small service-business owner:** “we missed 47 calls in 30 days.”
Context: owner says the company is the owner plus two workers and phone coverage disappears while they are on jobs.
Source: https://www.reddit.com/r/AiForSmallBusiness/comments/1rmfih3/anyone_switched_to_an_ai_receptionist/

---

## 5. ADOPTION EVIDENCE

### For
1. Gold Eagle is using AI answering operationally enough to attribute one month of booked revenue to it.
2. Andre's garage-door business has moved far beyond a receptionist trial into approximately 50 automations spanning the customer lifecycle.
3. Workiz has productized AI answering, service-area gating and automatic technician assignment rather than treating voice AI as an external experiment.
4. Simpro's marketplace contains several competing receptionist/automation products, implying sufficient customer demand to support a partner category.
5. Simpro itself is bundling autonomous back-office agents into its platform for a base of 24,000+ trade businesses.

### Against / caveats
1. Most hard numbers are vendor-published case studies, creating selection bias.
2. Marketplace listing != active usage or retention.
3. LANA charges meaningful setup/training fees, showing onboarding is not zero-friction.
4. Customer tolerance remains imperfect. A June 2026 Reddit commenter reported abandoning a plumber after its AI receptionist repeatedly failed to capture name/problem/phone number. This is qualitative but directly relevant failure evidence.
Source: https://www.reddit.com/r/aiToolForBusiness/comments/1u3q2xh/removed/

### A — current belief
**SUPPORTED for high-intent US home services; OPEN by country/vertical.**

Highest-EVI test: 20-contractor outbound test in one vertical offering free missed-call recovery with no CRM migration; measure connection -> install -> still-active day 30 -> % calls routed through agent.

LIVE_EXPERIMENT_REQUIRED.

---

## 6. ROI / UNIT-ECONOMIC EVIDENCE

### Gold Eagle
Observed attributed revenue: **$23,758 / 30 days** from AI-handled conversations.
Missing denominator: total calls, total business revenue, baseline missed-call revenue and platform cost were not reported in the source excerpt available this run.
Therefore incremental ROI cannot be computed honestly.

### Garage-door operator
Observed: **500+ AI calls -> $7,600** attributed revenue; automated texts/emails -> **$3,600** additional attributed revenue.
Missing: period length, total revenue, gross margin, Workiz software cost and counterfactual human conversion.

### LANA pricing bound
$300/month AI answering + $1,000 training.
$399/month AI qualification/booking + $1,500 training.
$600/month broader CRM/JMS AI automation + $3,500 workshops/training.
This gives a verified competitive willingness-to-charge reference, not willingness-to-pay or ROI.

### B — current belief
**SUPPORTED that measurable value can exist. NOT proven that a free standalone Supplier OS has positive unit economics.**

Highest-EVI test: instrument one contractor for 30 days with caller-level provenance. Randomly route eligible after-hours/missed-call leads between current process and AI recovery; compare booked rate, gross-profit contribution, human minutes, cancellation and no-show. This is the cleanest causal test.

LIVE_EXPERIMENT_REQUIRED.

---

## 7. DATA-FLYWHEEL EVIDENCE

### Evidenced fields now available in incumbent workflows
From Workiz documentation/API:
- service_area
- job_type / skill
- technician availability
- scheduled time
- advance notice
- lead status
- lost lead state
- job status
- assignment
- time off
- payment event
- client/job address
- job source
- call history/recording in Workiz Phone

Workiz's calendar sync documentation explicitly syncs entity type, client name, job type, scheduled time, address, status and assigned technician. Its API exposes create/update/assign and lost-lead operations.

Sources:
- https://help.workiz.com/hc/en-us/articles/18055867663889-Syncing-your-Workiz-schedule-with-your-personal-calendar
- https://developer.workiz.com/

### What remains UNKNOWN
No accepted source this run proves that contractors will grant an independent intermediary rights to:
- aggregate data across contractors;
- expose live capacity externally;
- retain longitudinal rejected-demand history;
- share pricing/acceptance/completion for routing competitors' jobs;
- permit derived cross-business benchmarking/resale.

### Key falsification
The naïve C thesis — “give away receptionist, therefore own availability/service-area/job data” — is **weakened**. Those fields are already first-class objects in Workiz/Simpro/ServiceTitan. Merely copying them creates integration dependency rather than a moat.

### Refined C thesis
The defensible graph must contain **inter-company relational state** that a single FSM cannot observe:

`demand_event -> contractor_1 rejected(reason) -> contractor_2 unavailable -> contractor_3 accepted -> quoted -> booked -> completed/cancelled -> realized lead time / price / outcome`

This would produce empirical routing intelligence across the market: actual availability, real acceptance behavior, effective service radius, urgency tolerance, price bands and completion history.

### C — current belief
**OPEN. Technical generation: strongly supported. Proprietary ownership/permission: unproven.**

Highest-EVI test: obtain consent from 5 contractors in one postcode cluster to pool only non-PII operational events. Track 100 demand events and determine whether rejected jobs can be rerouted while preserving contractor control. Success metric is not calls answered; it is % demand events yielding a cross-contractor state transition unavailable from any one CRM.

LIVE_EXPERIMENT_REQUIRED.

---

## 8. COMPETITOR / SUBSTITUTE MAP

### Workiz
Native AI answering + phone + messages + online booking + service areas + skill/availability-based assignment + lost-lead state + automations + API. Strongest threat this run because the desired Supplier-OS graph is already close to its internal data model.

### Simpro / Lightning
Large installed FSM base; AI agents embedded into collections, job preparation, payments and communications. 24,000+ businesses / 450,000 users claimed across group. AI sold as an uplift to the core system rather than standalone SaaS.

### LANA
Third-party Simpro marketplace entrant. Verified $300-$600/month plus meaningful onboarding fees. Covers reception through quote/invoice/review/rebooking.

### Supportiyo
Simpro-native AI receptionist focused on high call concurrency and direct job creation/booking. Price on application.

### CallCrewAI
Simpro-connected inbound/outbound operations covering calls, email, recurring scheduling, invoice reminders and communications.

### Human answering services
Still a substitute but qualitatively weaker when they cannot transact inside FSM. First-hand small-business testimony describes paying $300+/month for message taking and still having to call prospects back; this is one operator, not a market-wide price benchmark.
Source: https://www.reddit.com/r/AiForSmallBusiness/comments/1rmfih3/anyone_switched_to_an_ai_receptionist/

---

## 9. HARD FALSIFICATIONS / NULL RESULTS

1. **KILL: standalone AI receptionist as the moat.** Too many incumbents/partners now provide it; feature differentiation is decaying.
2. **WEAKEN: calendar/service-area data itself as proprietary moat.** Workiz directly models availability, skills, service areas, assignments and lead states.
3. **WEAKEN: free alone guarantees adoption.** LANA's paid setup fees indicate real implementation/configuration labor; qualitative reports still show customer-facing failure modes.
4. **NOT PROVEN: contractors will share data across businesses.** This is the core unresolved C question.
5. **NOT PROVEN: vendor-attributed revenue equals incremental profit.** No clean holdout/control evidence cleared the bar this run.

---

## 10. HYPOTHESIS LEDGER — A / B / C

### A — ADOPTION
**H1:** Contractors with urgent inbound demand will adopt AI front desk when it can book into their actual operational system with little workflow change.

**H0:** Trust, onboarding, customer aversion and incumbent-native AI prevent meaningful standalone adoption.

**Evidence for:** two operational Workiz cases; several Simpro marketplace products; Workiz-native booking/dispatch functionality.

**Evidence against:** meaningful training fees; a direct customer failure report; incumbent bundling.

**Falsifier:** <20% activation or <50% 30-day retention in a free/no-migration pilot after contractors agree pain exists.

**Belief delta:** FOR.

**Next test:** 20-contractor pilot with real call forwarding, not survey intent.

### B — ROI
**H1:** Fast AI response + booking/follow-up recovers enough high-intent jobs to materially exceed software/telephony cost.

**H0:** AI mostly handles calls humans would have converted anyway, while failures/cancellations offset savings.

**Evidence for:** Gold Eagle $23,758/30 days attributed revenue; garage-door operator $7,600 from 500+ AI-handled calls plus $3,600 follow-up attribution.

**Evidence against:** vendor selection bias; lack of randomized control; missing gross-margin denominator.

**Falsifier:** controlled pilot shows no statistically/materially meaningful incremental gross profit or admin-time reduction after accounting for cancellations/errors.

**Belief delta:** FOR.

**Next test:** caller-level randomized after-hours holdout.

### C — DATA FLYWHEEL
**H1:** A cross-contractor front desk can accumulate real-time acceptance/rejection/rerouting/completion events that no individual FSM possesses and use them to build superior supply routing.

**H0:** contractors/FSMs retain the useful data; privacy/integration constraints block pooling; independent layer merely mirrors incumbent records.

**Evidence for:** APIs and AI workflows clearly generate structured operational fields; out-of-area/skill/availability decisions are explicit machine-readable events.

**Evidence against:** incumbents already own most single-business state; no accepted proof of cross-business pooling permission or external availability publication.

**Falsifier:** 5-10 contractor pilot cannot obtain durable consent/data rights or pooled events fail to improve routing versus static directory + individual calendars.

**Belief delta:** NEUTRAL / refined rather than strengthened.

**Next test:** 100-demand-event cross-contractor routing pilot.

---

## 11. WHO TO WATCH NEXT

**Keating Kuhn / Gold Eagle Services** — operator with revenue attribution tied directly to AI-handled conversations. Highest value follow-up is denominator data: call count, baseline booking, cancellation and margin.

**Andre / garage-door operator featured by Workiz** — unusually broad automation footprint. Follow up for time horizon, staff avoided, invoice DSO and which automations produce actual dollars.

**Workiz product/engineering team** — their Answering + Service Areas + Scheduling + API model is effectively a reference architecture for what supply-state fields can be operationalized today.

**LANA Software** — Australia-focused Simpro/ServiceM8/AroFlo/Ascora/OpenSolar integration; useful for observing onboarding effort and whether $1k-$3.5k training is a true necessity.

**Hermia** — Simpro marketplace tool capturing fault, address, hazards, isolation, access, billing contact, availability and property/building type from inbound enquiries. Important because it shows the front desk can generate richer qualification state than generic phone metadata.
Source: https://marketplace.simprogroup.com/apps/hermia

**Simpro Lightning team** — critical adversary: if incumbents increasingly bundle autonomous back-office agents, standalone Supplier OS must create value outside a single system of record.

---

## 12. NOVELTY AUDIT

Prior reports reconstructed from the recent Supplier-OS email sequence focused on:
- ServiceTitan Riley / Superior Plumbing / Bill Joplin call-booking evidence;
- ServiceTitan's internal voice-agent dashboard and native access to customer history/capacity;
- Jobber Receptionist commoditization;
- Eliocall France adoption/pricing;
- roofing call-ledger / rejected-demand exhaust;
- Housecall Pro incumbent embedding.

### Deliberately rejected duplicates this run
- Riley 80% booking result: DUPLICATE.
- Superior Plumbing 80% / 30% escalation: DUPLICATE.
- Bill Joplin 1,300+ calls / >90% booking / 72% no-human result: DUPLICATE.
- Jobber $29 receptionist framing: DUPLICATE.
- Eliocall France pricing/adoption: DUPLICATE.
- generic “missed calls cost contractors money” commentary: REJECTED absent primary data.

### New substantive evidence accepted
1. Gold Eagle / Workiz attributed revenue.
2. Garage-door operator 500+ AI calls / revenue + 50-automation footprint.
3. Workiz skill + availability + service-area assignment state.
4. Workiz API operational objects including lost leads and payments.
5. LANA Australia verified pricing/setup economics.
6. Simpro Lightning installed-base + bundled-AI pricing threat.
7. Small-service-business owner's measured 47 missed calls/30 days as lower-grade pain evidence.

**Novelty target:** met. >70% of accepted material is substantively different from the reconstructed previous runs, with the majority involving companies/operators/source families absent from the prior two emails.

---

## 13. SOURCE-YIELD LEDGER

| Source family | Reads/searches | Accepted | Material belief changes |
|---|---:|---:|---|
| Workiz operator case studies | 3 | 2 | B strengthened; workflow broadened |
| Workiz docs/API | 8+ | 4 | C refined; incumbent data ownership threat strengthened |
| Simpro marketplace | 5 | 4 | A competition/pricing bound; onboarding friction |
| Simpro corporate | 2 | 1 | standalone moat weakened |
| Reddit first-hand | ~10 surfaced | 2 | pain validation + customer failure mode |
| ServiceTitan | many surfaced | 0 new | rejected as semantic duplicates this run |
| generic AI-receptionist marketing | many | 0 | rejected |

Yield lesson: **FSM documentation and operator cases are currently much higher-signal than generic AI receptionist founder posts.** The next run should rotate harder into UK/Australia contractor owners, API/marketplace reviews, churn/implementation failures and invoice/collections workflows rather than more US voice-agent success stories.

---

## 14. JSONL — COMMON SCHEMA

```jsonl
{"record_id":"ANSO-20260907-1927-001","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"US","market_or_entity":"garage-door / emergency home services","person_or_company":"Gold Eagle Services / Keating Kuhn","role":"home-service operator","source_type":"case_study","source_url":"https://www.workiz.com/blog/case-study/gold-eagle-services-case-study/","published_at":"2025-12","palace_proximity_score":90,"evidence_grade":"A","verbatim_excerpt":"When Genius Answering answers the phone, it's able to schedule a job.","detailed_claim":"Workiz reports Gold Eagle Services used Genius AI Answering to respond to inbound customers in under two minutes 24/7, schedule jobs, add notes and cancel jobs, with $23,758 in revenue attributed to conversations AI handled over 30 days.","quantitative_claims":[{"metric":"revenue attributed to AI-handled conversations","value":"$23,758","denominator":"UNKNOWN","timeframe":"30 days","caveat":"vendor-published case study; incremental baseline and gross margin not reported"},{"metric":"response time","value":"under 2 minutes","denominator":"inbound leads","timeframe":"ongoing case period","caveat":"operator/vendor claim"}],"state_before":"Slower/manual response where urgent leads could be lost before callback","action_taken":"Deployed Workiz Genius AI Answering for immediate response and booking","observed_agent_behavior":"Answered, scheduled, added notes and could cancel jobs","outcome":"$23,758 attributed revenue in 30 days","time_horizon":"30 days","mechanism":"Immediate action on high-intent inbound demand reduces lead decay and converts calls directly into scheduled jobs.","moat_implication":"Supports reception as a valuable wedge but not as a moat; durable value requires ownership of downstream cross-contractor demand/acceptance state.","h1":"Fast AI response and booking materially recovers high-intent contractor demand.","h0":"AI mostly handles demand that would have converted anyway and vendor attribution overstates incremental value.","falsifier":"Randomized eligible-call holdout shows no material incremental gross profit or booking uplift after cancellations/errors.","belief_delta":"FOR","next_best_test":"Randomize after-hours eligible calls between current process and AI booking while tracking gross profit and completion.","novelty_reason":"New Workiz operator and revenue-attribution case not present in the previous Supplier-OS reports.","independence_cluster":"workiz-gold-eagle"}
{"record_id":"ANSO-20260907-1927-002","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"US","market_or_entity":"garage door services","person_or_company":"Andre / garage-door company featured by Workiz","role":"garage-door business operator","source_type":"case_study","source_url":"https://www.workiz.com/blog/case-study/how-a-small-garage-door-company-uses-ai-to-outperform-industry-giants/","published_at":"2026-07","palace_proximity_score":88,"evidence_grade":"A","verbatim_excerpt":"The automations are amazing in that they free me up.","detailed_claim":"Operator reports using roughly 50 automations spanning estimate follow-up, pre-job reminders, invoice follow-up, reviews and receipts. Workiz reports the AI receptionist answered 500+ calls generating $7,600, with automated text/email responses adding $3,600 attributed revenue.","quantitative_claims":[{"metric":"AI-handled calls","value":"500+","denominator":"UNKNOWN","timeframe":"UNKNOWN","caveat":"case study does not provide total inbound calls in retrieved evidence"},{"metric":"revenue from AI calls","value":"$7,600","denominator":"500+ AI-handled calls","timeframe":"UNKNOWN","caveat":"vendor attribution; counterfactual absent"},{"metric":"revenue from automated text/email","value":"$3,600","denominator":"UNKNOWN","timeframe":"UNKNOWN","caveat":"vendor attribution"},{"metric":"automations","value":"50","denominator":"business workflows","timeframe":"current case state","caveat":"operator statement"}],"state_before":"Recurring phone, quote, reminder, invoice and review admin required manual attention","action_taken":"Implemented Workiz AI answering plus approximately 50 automations","observed_agent_behavior":"Handled calls and automated follow-up across pre- and post-job workflows","outcome":"Attributed revenue plus reduced recurring admin burden","time_horizon":"UNKNOWN","mechanism":"Value compounds when front desk owns the whole administrative event chain rather than call answering alone.","moat_implication":"Broad workflow integration increases stickiness but also favors incumbent FSM platforms; third party needs cross-business data advantage.","h1":"Multi-workflow automation creates materially more ROI than isolated AI reception.","h0":"Most claimed value is attribution to workflows that would have happened manually and does not persist net of errors/software cost.","falsifier":"Instrumented before/after or holdout shows little incremental gross profit, DSO improvement or labor saving.","belief_delta":"FOR","next_best_test":"Obtain period, gross-margin, baseline admin hours, DSO and cancellation data from comparable garage-door operators.","novelty_reason":"New vertical/operator and lifecycle-wide automation evidence.","independence_cluster":"workiz-garage-door-andre"}
{"record_id":"ANSO-20260907-1927-003","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"US","market_or_entity":"Workiz field-service scheduling graph","person_or_company":"Workiz","role":"field-service software operator","source_type":"docs","source_url":"https://help.workiz.com/hc/en-us/articles/43952232552081-Automatically-assigning-jobs-to-techs-with-Genius-Answering","published_at":"2026-03-31","palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"Availability (openings in their schedule that accommodate the job duration)","detailed_claim":"Workiz documents AI technician assignment using schedule availability, job-type skills and service areas, with configurable advance notice from one hour to seven days or none. This is direct evidence that supply capacity can be represented as structured operational state rather than inferred from directory presence.","quantitative_claims":[{"metric":"minimum advance-notice configuration","value":"1 hour to 7 days or none","denominator":"AI-assigned bookings","timeframe":"current documented product","caveat":"configuration capability, not observed contractor capacity"}],"state_before":"AI-created jobs could remain unassigned pending human review","action_taken":"Enable automatic technician assignment in Genius Answering","observed_agent_behavior":"Chooses technician based on availability, skills and service area and offers earliest time respecting notice rules","outcome":"Structured automatic assignment is technically supported","time_horizon":"current product","mechanism":"Operational availability becomes computable when calendar openings, job duration, skill and geography are represented together.","moat_implication":"Strongly supports feasibility of a live supply graph but weakens exclusivity because incumbent FSM already models the core fields.","h1":"Structured job/skill/geography data is sufficient to expose useful live contractor supply state.","h0":"Real contractor capacity remains too exception-heavy for structured fields to represent reliably.","falsifier":"High rate of human overrides, cancellations or infeasible jobs despite matching documented state.","belief_delta":"FOR","next_best_test":"Measure override/cancellation rate for 100 automatically assigned jobs and classify missing state causing errors.","novelty_reason":"New incumbent implementation detail not covered in previous reports.","independence_cluster":"workiz-product-docs"}
{"record_id":"ANSO-20260907-1927-004","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"GLOBAL","market_or_entity":"Workiz API operational graph","person_or_company":"Workiz","role":"field-service platform / API operator","source_type":"docs","source_url":"https://developer.workiz.com/","published_at":null,"palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"Leads can be viewed individually or as a list, and can be filtered.","detailed_claim":"Workiz's developer API exposes jobs, leads, lead lost/reactivation/conversion state, assignment, team, time off and payment actions. This makes extraction and synchronization of useful operational supply events technically possible when a contractor authorizes access.","quantitative_claims":[],"state_before":"Operational state is held inside the contractor FSM","action_taken":"Authorize/use Workiz developer API","observed_agent_behavior":"UNKNOWN","outcome":"Jobs/leads/assignments/lost-state/time-off/payments are programmatically addressable","time_horizon":"current API","mechanism":"A Supplier OS can derive live supply state from authorized FSM events instead of repeatedly asking contractors to maintain duplicate data.","moat_implication":"Integration is feasible but data access alone is not proprietary; moat must come from cross-contractor normalization/routing/outcome history.","h1":"Authorized FSM integrations can cheaply seed a cross-contractor operational graph.","h0":"API access, permissions and heterogeneous schemas make normalization too costly and data remains owned/controlled by incumbents.","falsifier":"Pilot across 3 FSMs shows integration/normalization cost exceeds value or contractors refuse necessary data scopes.","belief_delta":"NEUTRAL","next_best_test":"Build minimal adapters for Workiz + Jobber + Simpro and compare a 12-field canonical demand/supply event schema.","novelty_reason":"Direct API-level evidence about technically extractable state.","independence_cluster":"workiz-api"}
{"record_id":"ANSO-20260907-1927-005","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"AU","market_or_entity":"tradie AI front desk on Simpro/ServiceM8/AroFlo/Ascora/OpenSolar","person_or_company":"LANA Software","role":"AI receptionist / contractor automation vendor","source_type":"docs","source_url":"https://marketplace.simprogroup.com/apps/lana-software-ai-receptionist","published_at":"2026-05-12","palace_proximity_score":85,"evidence_grade":"A","verbatim_excerpt":"AI Receptionist and booking jobs in your Job Management Software.","detailed_claim":"LANA's Simpro marketplace listing prices AI answering at $300/month plus $1,000 training; qualification/job booking at $399/month plus $1,500 training; and a broader CRM/front-desk/JMS workflow at $600/month plus $3,500 training/workshops, including quote chase, invoice chase, reviews and rebooking.","quantitative_claims":[{"metric":"AI receptionist subscription","value":"$300/month","denominator":"subscription","timeframe":"pricing updated 2026-05-12","caveat":"currency displayed as $ on marketplace listing; listing advises contacting vendor for current pricing"},{"metric":"AI receptionist training","value":"$1,000","denominator":"setup","timeframe":"pricing updated 2026-05-12","caveat":"marketplace listing"},{"metric":"qualification+booking subscription","value":"$399/month","denominator":"subscription","timeframe":"pricing updated 2026-05-12","caveat":"marketplace listing"},{"metric":"qualification+booking training","value":"$1,500","denominator":"setup","timeframe":"pricing updated 2026-05-12","caveat":"marketplace listing"},{"metric":"full CRM+AI receptionist+JMS","value":"$600/month","denominator":"subscription","timeframe":"pricing updated 2026-05-12","caveat":"marketplace listing"},{"metric":"full-tier training/workshops","value":"$3,500","denominator":"setup","timeframe":"pricing updated 2026-05-12","caveat":"marketplace listing"}],"state_before":"Contractor administrative workflows handled manually or by separate tools","action_taken":"Integrate AI receptionist/automation with job-management software","observed_agent_behavior":"Qualifies calls, creates jobs, chases quotes/invoices, requests reviews and rebooks service jobs","outcome":"Commercial product available; actual customer adoption/ROI UNKNOWN","time_horizon":"current listing","mechanism":"Vertical integration with FSM converts voice/text events into executable contractor workflow.","moat_implication":"Feature supply is crowded and onboarding remains costly; generic front desk is unlikely to be defensible.","h1":"Contractors will pay for integrated AI admin when it writes directly into existing JMS workflows.","h0":"Setup burden and incumbent AI prevent enough sustained third-party adoption.","falsifier":"Marketplace/vendor retention and active-customer data show low usage after onboarding or high churn.","belief_delta":"NEUTRAL","next_best_test":"Obtain active customer count, 90-day retention, call volume and setup labor per LANA customer.","novelty_reason":"New Australia-focused competitor with verified pricing and setup economics.","independence_cluster":"simpro-lana"}
{"record_id":"ANSO-20260907-1927-006","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"GLOBAL","market_or_entity":"Simpro Group incumbent FSM AI bundling","person_or_company":"Simpro Group","role":"field-service software platform","source_type":"blog","source_url":"https://www.simprogroup.com/company/press/simpro-group-unveils-lightning","published_at":"2026-05-13","palace_proximity_score":95,"evidence_grade":"A","verbatim_excerpt":"Lightning is available immediately to all Simpro, AroFlo and BigChange customers","detailed_claim":"Simpro Group says it serves more than 24,000 trade businesses and 450,000 users across the US, Australia and UK. Lightning embeds AI agents across collections follow-up, job preparation, payment processing and customer communication; the launch upgrade was 15% of existing contracts, with a stated 25% post-promotional uplift.","quantitative_claims":[{"metric":"trade businesses","value":"24,000+","denominator":"Simpro Group customer base","timeframe":"2026-05-13","caveat":"company-reported"},{"metric":"users","value":"450,000","denominator":"Simpro Group","timeframe":"2026-05-13","caveat":"company-reported"},{"metric":"Lightning launch uplift","value":"15%","denominator":"existing contract price","timeframe":"launch offer through 2026-05-31","caveat":"promotion"},{"metric":"post-promotional uplift","value":"25%","denominator":"existing contract price","timeframe":"after promotion","caveat":"company-reported pricing policy"}],"state_before":"Core FSM customers used scheduling/dispatch/quotes/invoices with separate or less autonomous AI","action_taken":"Simpro bundled AI agents into Lightning platform upgrade","observed_agent_behavior":"Handles collections follow-up, job preparation, payment processing and customer communication","outcome":"AI becomes an incumbent platform capability across a large installed base","time_horizon":"2026 launch","mechanism":"System-of-record vendors can attach AI cheaply because they already own the required operational context and permissions.","moat_implication":"Strongly against a standalone front-desk/data-copy moat; supports cross-business rejected-demand/routing graph as the differentiated layer.","h1":"Standalone Supplier OS can win by offering cheaper/free AI and aggregating cross-contractor state incumbents cannot see.","h0":"Incumbent FSM bundling captures both automation value and operational data, leaving little room for independent Supplier OS.","falsifier":"Independent front-desk layer achieves high adoption and demonstrably superior cross-contractor routing/data value despite incumbent AI availability.","belief_delta":"AGAINST","next_best_test":"Target contractors on heterogeneous/lightweight stacks rather than Simpro-heavy incumbents and compare activation/retention.","novelty_reason":"New incumbent bundling/installed-base/pricing evidence from Simpro rather than previously covered ServiceTitan/Housecall Pro.","independence_cluster":"simpro-lightning"}
{"record_id":"ANSO-20260907-1927-007","probe":"agent_native_supplier_os","observed_at":"2026-09-07T19:27:32+07:00","country":"US","market_or_entity":"small service business phone coverage","person_or_company":"anonymous small-service-business owner","role":"owner/operator; self-reports owner plus two workers","source_type":"reddit","source_url":"https://www.reddit.com/r/AiForSmallBusiness/comments/1rmfih3/anyone_switched_to_an_ai_receptionist/","published_at":"2026-03-06","palace_proximity_score":65,"evidence_grade":"B","verbatim_excerpt":"we missed 47 calls in 30 days","detailed_claim":"Owner of a small service business with two workers says they tracked 47 missed calls in a month while crews were on jobs. They also report trying a human answering service costing more than $300/month that mainly took messages, leaving the owner to call prospects back.","quantitative_claims":[{"metric":"missed calls","value":"47","denominator":"all calls UNKNOWN","timeframe":"30 days","caveat":"self-reported; owner estimates some may be spam"},{"metric":"human answering service cost","value":"$300+/month","denominator":"one owner's prior service","timeframe":"UNKNOWN","caveat":"single self-reported case"}],"state_before":"Owner/crew unavailable to answer phones while on jobs","action_taken":"Tracked missed calls and previously tried human answering service","observed_agent_behavior":"UNKNOWN","outcome":"47 missed calls measured; human answering service judged insufficient because it only took messages","time_horizon":"30 days for missed-call count","mechanism":"Very small crews face a real coverage constraint; value requires action/booking rather than message capture.","moat_implication":"Supports free AI front desk as acquisition wedge but provides no data-flywheel evidence.","h1":"Small crews have enough measurable missed-call pain to adopt an action-capable AI front desk.","h0":"Much missed-call volume is spam/low-value and owners/customers prefer direct human callback.","falsifier":"Instrumented call logs show low qualified missed-demand share or AI fails to improve booked/completed jobs.","belief_delta":"FOR","next_best_test":"Classify 100 missed calls across five 1-3 crew contractors into spam, existing customer, qualified new lead, booked and completed outcomes.","novelty_reason":"New measured first-hand pain record from a micro service business, distinct from enterprise FSM cases.","independence_cluster":"reddit-small-service-owner"}
```

## SUPPLIER-OS OPPORTUNITY JSON

```jsonl
{"country":"US","contractor_vertical":"garage door / emergency home services","avg_job_value":"UNKNOWN","pain_observations":["Gold Eagle operator emphasizes speed-to-lead and immediate booking","Separate garage-door operator uses AI across calls, estimates, reminders, invoices and reviews","500+ AI-handled calls and attributed revenue observed in vendor case"],"incumbent_tools":["Workiz Genius Answering","Workiz Automations","Workiz Phone"],"verified_software_price":"UNKNOWN","adoption_h1":"Urgent phone-led contractors adopt AI when it can transact directly in their existing schedule rather than merely take messages.","adoption_h0":"Customer trust/errors and existing FSM features limit sustained use.","adoption_falsifier":"<20% activation or <50% 30-day active retention in a no-migration pilot.","roi_h1":"Immediate response, booking and lifecycle follow-up recover enough jobs/admin time to materially exceed cost.","roi_h0":"Vendor attribution overstates incremental value and gross profit does not improve materially.","roi_falsifier":"Randomized holdout shows no material incremental gross profit/admin-hour improvement.","data_flywheel_h1":"Cross-contractor rejected/accepted demand events create routing intelligence unavailable to one garage-door company's CRM.","data_flywheel_h0":"Useful state remains siloed in Workiz and contractors will not permit pooling/rerouting.","data_flywheel_falsifier":"Five-contractor pilot cannot obtain durable consent or pooled events fail to improve routing.","proprietary_fields_possible":["availability","service_area","pricing","acceptance","completion","response_time"],"live_experiment_required":true,"status":"SUPPORTED"}
{"country":"AU","contractor_vertical":"electrical/plumbing/roofing/remedial/fire trades using Simpro-family systems","avg_job_value":"UNKNOWN","pain_observations":["LANA product explicitly automates inbound calls, qualification, quote chase, invoice chase, review requests and rebooking","Multiple Simpro marketplace vendors target the same front-desk/admin surface","Significant one-time training/workshop charges imply configuration burden"],"incumbent_tools":["Simpro","Simpro Lightning","LANA Software","Supportiyo","CallCrewAI","Hermia"],"verified_software_price":"LANA $300/month + $1,000 training; $399/month + $1,500 training; $600/month + $3,500 training/workshops (marketplace pricing updated 2026-05-12; currency shown as $)","adoption_h1":"Integrated AI front desk has enough value for tradies to adopt if it writes directly into their existing JMS.","adoption_h0":"Simpro's own AI plus onboarding friction makes third-party adoption weak or transient.","adoption_falsifier":"Marketplace active-customer/retention data shows low sustained usage.","roi_h1":"Quote/invoice/rebooking automation creates measurable value beyond call answering.","roi_h0":"Automation savings are too small relative to subscription/setup and human oversight.","roi_falsifier":"Customer-level labor/revenue/DSO metrics fail to exceed cost after 90 days.","data_flywheel_h1":"An independent layer spanning multiple JMSs can normalize demand and rejected-capacity events across contractors.","data_flywheel_h0":"Simpro remains the authoritative data owner and independent layer receives insufficient rights/coverage.","data_flywheel_falsifier":"Cross-platform pilot cannot access/retain normalized events or fails to improve routing.","proprietary_fields_possible":["availability","service_area","pricing","acceptance","completion","response_time"],"live_experiment_required":true,"status":"OPEN"}
```

# RUN CONCLUSION

The strongest strategic update is not “AI receptionist works.” That is becoming old news and increasingly commoditized.

The sharper thesis after this run is:

**The Supplier OS should treat the free front desk as instrumentation. The asset is a cross-contractor demand-execution graph, especially events that incumbent FSMs cannot see because they occur across business boundaries.**

The decisive unresolved experiment is C: can we get five contractors to permit enough normalized, non-PII operational data to reroute rejected demand and observe actual acceptance/completion? Until that works, the data-flywheel claim stays OPEN even though adoption and ROI have increasingly credible positive evidence.
