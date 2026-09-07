# Gold Probe — Agent Transaction Rails Alpha — 2026-09-07 19:51 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 14:55:32 +0200

Agent Transaction Rails Alpha
Observed: 2026-09-07 19:51 Asia/Phnom_Penh

1. EXECUTIVE ALPHA

1) The strongest update this run is a major falsification of headline x402 adoption metrics. A July 2026 population-scale measurement reconstructing 136,708,672 Base x402 settlements over 280 days found 21.20% fictitious and another 63.78% internal to linked clusters. Only 15.02% of settlements were left unattributed; of $44.12m gross Base value, only $187,861.35 could be shown to reach a nameable catalog service, while $20.26m is merely the upper bound not provably manufactured. This does NOT prove the remainder is fake; it proves transaction count is not a valid adoption proxy. The paper additionally found 25,163 advertised Base resources collapsed to 811 distinct payTo recipients; only 249 recipients had earned >=$10 lifetime, and just 474/910 advertised hosts returned a live 402 challenge in the authors' point-in-time probe. This materially downgrades the thesis that x402 settlement count demonstrates a broad agent economy.
Source: https://arxiv.org/abs/2607.12575

2) A much more decision-useful payment metric is beginning to appear at the intermediary layer: Nevermined's live site currently displays 3,412 paid calls and $171 settled 'today' for its merchant flow, while showing Exa selling a $7 search key autonomously on a delegated card. Nevermined's implementation uses tokenized cards, revocable mandates, per-transaction caps, Stripe/Braintree merchant settlement, and charges merchants 1-2% of settled volume. The number is platform-reported and should be treated as an operator metric rather than independently audited volume, but it is much closer to economically meaningful demand than raw on-chain settlement count.
Source: https://nevermined.ai/

3) Local-service transaction rails are converging on structured supply-state synchronization rather than autonomous phone/browser action. Wix's live Google integration syncs service definitions, prices and appointment inventory from Wix Bookings into Google Search/Maps and is designed for Google AI Mode; availability updates approximately every 30 minutes. Simple appointments can flow from Google to a Wix booking form, while services with add-ons/price variations fall back to the Wix calendar for qualification. This is the clearest new local-service implementation this run: the hard asset is live service + price + slot state, while the AI surface is replaceable.
Source: https://www.globenewswire.com/news-release/2026/02/24/3243636/0/en/Wix-Launches-Integration-With-Google-Search-Google-Maps-and-Google-AI-Mode-to-Turn-Queries-Into-Instant-Bookings.html

4) Native ACP checkout remains a useful null-adoption case. In a May 11 GitHub issue against the Agentic Commerce Protocol repo, a developer reports checking named launch merchants: Etsy appeared to retain native checkout, while Glossier exposed only a 'Visit' flow, and the issue asks maintainers to distinguish native checkout, discovery-only, app flow and announced-but-not-live merchants. Combined with OpenAI's March 2026 retreat from native Instant Checkout, this supports a mechanism where merchant-owned checkout survived while universal agent-owned checkout did not. This is first-hand field testing, not an official merchant census, so it is evidence of ambiguity/limited observable deployment rather than a quantified market share.
Source: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/issues/248

Net thesis update:

PAYMENT SETTLEMENT is commoditizing, but raw protocol activity is a dangerously weak metric. The defensible transaction layer appears increasingly to be VERIFIED ECONOMIC DEMAND + LIVE SUPPLY STATE + QUALIFICATION + FULFILLMENT/ORDER STATE + EXECUTION HISTORY. A protocol can have enormous transaction counts and almost no independently provable merchant economy; conversely a much smaller intermediary with attributable paid calls can be strategically more interesting.

2. FIELD EVIDENCE TABLE

Rank 1 — ATRA-20260907-01
Palace proximity: 55 | Grade A | Novelty: VERY HIGH | Decision impact: VERY HIGH
Entity: x402 / Base
Source: Ling, Zhou, Wu, Wang — population-scale measurement paper
Finding: 136.7m Base settlements / $44.12m gross over 280 days; 21.20% fictitious + 63.78% internal linked-cluster settlement; only 15.02% unattributed. 25,163 advertised Base resources -> 811 payTo recipients -> 624 ever settled -> 249 earned >=$10 lifetime. 474/910 hosts returned a live 402 challenge.
Moat layer: PAYMENT, PROTOCOL_STANDARDIZATION, HISTORY_REPUTATION
Direction: PAYMENT protocol becomes more commoditized; independently verified demand/reputation becomes more defensible.

Rank 2 — ATRA-20260907-02
Palace proximity: 93 | Grade A | Novelty: HIGH | Decision impact: HIGH
Entity: Nevermined
Finding: operator surface currently reports 3,412 paid calls and $171 settled today; delegated cards + mandates + PSP settlement; merchant fee 1-2% settled volume.
Moat layer: PAYMENT, IDENTITY_TRUST, HISTORY_REPUTATION, INTEGRATION_LOCK_IN
Direction: settlement is increasingly reusable infrastructure; attributed economic history and mandate/control plane may retain value.

Rank 3 — ATRA-20260907-03
Palace proximity: 90 | Grade B | Novelty: HIGH | Decision impact: HIGH
Entity: Wix Bookings × Google
Finding: service, price and near-real-time appointment availability sync into Google; slots refresh about every 30 minutes; complex service variants still require qualification in Wix.
Moat layer: LIVE_PRICE, LIVE_AVAILABILITY, QUALIFICATION, BOOKING, PROPRIETARY_SUPPLY_GRAPH
Direction: front-end discovery/agent surface commoditizes; synchronized supply state and qualification remain valuable.

Rank 4 — ATRA-20260907-04
Palace proximity: 75 | Grade B | Novelty: HIGH | Decision impact: MEDIUM-HIGH
Entity: ACP / ChatGPT merchant checkout
Finding: first-hand May developer test found Etsy appearing native, Glossier 'Visit' only; public status of named merchants remained unclear enough to trigger an open protocol issue.
Moat layer: BOOKING/PAYMENT equivalent checkout, INTEGRATION_LOCK_IN, PROTOCOL_STANDARDIZATION
Direction: protocol support does not imply live transactable deployment; merchant-owned checkout remains structurally important.

3. EXACT WORDS

Ling et al., x402 measurement: “Settlement count measures manufacturability, not adoption.”
Context: population-scale Base/Solana payment-graph analysis.
Source: https://arxiv.org/abs/2607.12575

Nevermined merchant flow: “3,412 paid calls today.”
Context: current operator website counter attached to the merchant payment flow.
Source: https://nevermined.ai/

Wix: “updated approximately every 30 minutes.”
Context: appointment availability synchronization from Wix Bookings into Google surfaces.
Source: https://www.globenewswire.com/news-release/2026/02/24/3243636/0/en/Wix-Launches-Integration-With-Google-Search-Google-Maps-and-Google-AI-Mode-to-Turn-Queries-Into-Instant-Bookings.html

ACP GitHub tester: “Glossier: only shows ‘Visit’ button.”
Context: developer testing which publicly named merchants actually exposed native ACP checkout.
Source: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/issues/248

4. LIVE TRANSACTION STACK MAP

MACHINE/API COMMERCE
Agent intent
-> credential/mandate (Nevermined tokenized card + budget/per-call cap)
-> paid resource request
-> payment/metering
-> merchant's existing Stripe/Braintree PSP
-> delivery
-> attributed call/settlement history

Evidence this run says the economically meaningful metric is not 'settlements emitted'; it is independent payer -> independent merchant -> delivered resource -> retained revenue.

LOCAL SERVICES
Google intent surface
-> structured merchant/service identity
-> Wix service + price graph
-> availability sync (~30-minute cadence)
-> slot selection
-> simple flow: merchant booking form
-> complex add-ons/price variants: Wix qualification/calendar
-> booked service

The key non-commoditized object is the time-varying provider state. A protocol can expose BOOKING, but it cannot manufacture accurate capacity.

RETAIL CHECKOUT
Agent discovery
-> ACP-capable merchant/feed
-> native checkout only where actually deployed
-> otherwise merchant-owned checkout / app flow
-> merchant fulfillment and support

The observable 2026 pattern continues to favor standardized discovery/delegation plus merchant-controlled transaction completion over a universal agent-owned checkout surface.

5. FAILURE MODES / NULL ADOPTION

A) x402 headline adoption inflation
- Raw count: extremely large.
- Failure: gas-sponsored, internally recyclable settlements make counts cheap to manufacture.
- Consequence: do not rank transaction rails by transaction count without independent payer/payee and economic-substance analysis.

B) Advertised x402 supply decay
- 25,163 Base catalog entries resolved to only 811 distinct payment recipients.
- Only 249 recipients earned >=$10 lifetime.
- Only 52.09% of 910 hosts returned a live 402 challenge in the paper's point-in-time probe.
- Consequence: endpoint/catalog count is also not equivalent to live supply.

C) ACP protocol != native checkout deployment
- A first-hand developer could not reconcile public launch messaging with live merchant checkout behavior.
- Consequence: 'supports ACP' must be split into discovery/feed, checkout API capability, and actual consumer-visible live checkout.

D) Wix complex-service fallback
- Simple appointment inventory can be synchronized, but add-ons/price variations redirect into Wix's own qualification/calendar experience.
- Consequence: local-service rails remain limited by qualification complexity; booking slot availability alone is insufficient for complex jobs.

6. MOAT MAP

COMMODITIZING
- PROTOCOL_STANDARDIZATION: strong evidence. Multiple protocols/PSPs can implement the same payment or checkout boundary.
- PAYMENT: strong evidence. Nevermined explicitly settles to existing Stripe/Braintree; payment connectivity itself is becoming a layer rather than the product.
- BASIC IDENTITY / SPEND CONTROL: medium evidence. Mandates, caps and revocation are increasingly standard rail features.

MIXED
- BOOKING: the API action is commoditizing, but authoritative slot inventory is not.
- LIVE_PRICE: structurally important but increasingly standardized when a system of record can syndicate it.

DEFENSIBLE / MORE INTERESTING
- LIVE_AVAILABILITY: authoritative, time-varying operational state.
- QUALIFICATION: complex services still force domain-specific branching/fallback.
- FULFILLMENT_STATE: remains outside the payment primitive and was a prior-run weakness in UCP/order mutation.
- HISTORY_REPUTATION: especially independent, economically substantive execution history.
- PROPRIETARY_SUPPLY_GRAPH: provider/service/price/capacity/acceptance/completion state across suppliers.
- VERIFIED ECONOMIC DEMAND: new addition to the moat thesis; protocol volume without proof of independent demand is weak.

7. WHO TO WATCH NEXT

Shengchen Ling / Yajin Zhou / Lei Wu / Cong Wang — Their measurement method is the most important adversarial instrument found so far for distinguishing agent-payment hype from economically independent activity. Follow the promised public dataset/code and rerun as new x402 windows emerge.

Nevermined — Watch whether the live paid-call counter persists/grows and whether merchant-level independent service mix becomes observable. The key question is repeat third-party demand, not raw requests.

Koby Maman / Wix Bookings — Direct owner of a large service-booking system now syndicating price/capacity into Google surfaces. High-value source for how frequently inventory must refresh and where qualification breaks generic booking.

ACP maintainers / merchant implementers — Track concrete merchant deployment issues rather than spec releases. Particularly useful: evidence that native checkout returns, remains niche, or moves fully to merchant-owned surfaces.

8. HYPOTHESIS LEDGER

H1-A — Independent economic substance, not protocol settlement count, predicts durable transaction-rail value.
H0: High raw settlement growth reliably reflects broad independent agent adoption.
Evidence for H1: population-scale x402 graph shows 84.98% of Base settlements either fictitious or internal to linked clusters; only a narrow lower bound reaches nameable services.
Evidence against: independent-demand upper bound remains as high as $20.26m because unattributed recipients cannot be classified.
Falsifier: a later independently reproducible census showing most payment value flows from unrelated payers to unrelated merchants with repeat usage and delivered services.
Belief delta: STRONGLY_FOR.
Next test: rerun the authors' released pipeline on July-August 2026 x402 flows and identify top genuinely external merchant clusters by retained revenue.

H1-B — Agent-payment connectivity commoditizes into existing PSP rails; value shifts to mandate/control + metering + attribution.
H0: merchants require a new closed payment network to transact with agents.
Evidence for H1: Nevermined connects merchant Stripe/Braintree, preserves payout, and layers delegated card mandates and usage attribution on top.
Evidence against: scale is currently small and platform-reported.
Falsifier: merchants systematically need rail-native settlement unavailable through existing PSPs, and those proprietary rails achieve materially higher conversion/reliability.
Belief delta: FOR.
Next test: compare Nevermined merchant retention/volume with x402-native sellers and MPP sellers for the same API category.

H1-C — Local-service transaction advantage concentrates in live supply-state synchronization and qualification, not the agent UI.
H0: generic agent browsing/calling is sufficient for booking local services reliably.
Evidence for H1: Wix now pushes price and ~30-minute availability state directly into Google; complex variants still require Wix qualification.
Evidence against: no conversion uplift or booking-volume metric disclosed.
Falsifier: controlled booking tests where generic browser/phone agents equal structured inventory feeds on accuracy, latency, cancellation and completion.
Belief delta: FOR.
Next test: 50 identical beauty/service booking tasks across structured Wix/Google supply vs phone/browser-only businesses; measure success, stale-slot failures, time-to-book and post-book changes.

H1-D — Protocol capability and live merchant transactability are weakly coupled.
H0: once a merchant/platform announces ACP/UCP support, users can reliably transact natively.
Evidence for H1: ACP issue documents publicly named merchants behaving differently in live testing.
Evidence against: one tester is not a census and behavior may vary by user/region/date.
Falsifier: authoritative merchant registry + repeated tests showing nearly all announced merchants expose stable native checkout.
Belief delta: FOR.
Next test: automated weekly 50-merchant ACP/UCP capability audit separating discovery, cart, native checkout, redirect, order lifecycle, refunds.

9. NOVELTY AUDIT VS PRIOR RUNS

Prior-run material reconstructed from the two available recent probe emails included:
- Worldline/ING/Mastercard production European agentic card transaction.
- Stripe Agentic Commerce Suite and near-real-time catalog/availability normalization.
- PayPal/Braintree ACP/UCP support.
- Google local-business agentic calling.
- UCP missing order mutation / partial cancellation.
- Pine Labs P3P and UPI delegated payment.
- Visa/Artemis x402 + MPP headline payment volumes.
- Mastercard/hoppa mobility booking/payment.
- UCP returns and deposits/scheduled payments.
- Decodo browser-agent transaction benchmark.
- hospitality reservation revenue/accuracy case.

Accepted records this run are 100% substantively new relative to those reconstructed records: x402 authenticity census; Nevermined attributed paid-call/settlement flow; Wix/Google service-state booking integration; ACP live-merchant checkout ambiguity.

Semantic duplicates rejected:
- Mastercard Worldline/ING production card transaction: already covered.
- Pine Labs/UPI delegated payment: already covered.
- UCP order mutation and 3DS issues: already covered family; no sufficiently new outcome metric in this run.
- Generic Mastercard AP4M announcement: rejected because it describes architecture/partners but does not expose live adoption or transaction outcome metrics.
- Recycled x402 headline transaction counts: rejected unless paired with independent-demand analysis.
- Generic hotel-agent ROI market reports: rejected as secondary/unsourced.

Novelty target: CLEARED. >=70% substantive novelty; all four accepted records introduce a new entity/source or a materially new falsification.

10. SOURCE-YIELD LEDGER

Academic / transparent primary measurement: reads 1 deep paper; accepted 1; material belief changes 1.
Primary payment operator/platform sites: reads 2; accepted 1 (Nevermined); rejected 1 architecture-only Mastercard AP4M as insufficiently outcome-based.
Primary service-platform release: reads 1; accepted 1 (Wix Bookings × Google).
GitHub implementation/issues: reads several surfaced issues; accepted 1 ACP live-merchant test; UCP mutation/3DS duplicates rejected.
Search/news/secondary explainers: multiple reads; accepted 0 as standalone evidence; used only to locate primary/implementation sources.
Local booking/operator sources: searched; no new transaction-volume outcome strong enough beyond Wix's concrete implementation.

11. JSONL

{"record_id":"ATRA-20260907-01","probe":"agent_transaction_rails_alpha","observed_at":"2026-09-07T19:51:00+07:00","country":"GLOBAL","market_or_entity":"x402 on Base and Solana","person_or_company":"Shengchen Ling; Yajin Zhou; Lei Wu; Cong Wang","role":"Researchers; population-scale on-chain measurement authors","source_type":"other","source_url":"https://arxiv.org/abs/2607.12575","published_at":"2026-07-14","palace_proximity_score":55,"evidence_grade":"A","verbatim_excerpt":"Settlement count measures manufacturability, not adoption.","detailed_claim":"The authors reconstruct x402 settlements from facilitator-relayed EIP-3009 events and payment/funding/sweep graphs. Over 280 days on Base they identify 136,708,672 settlements worth $44,121,383.81; 21.20% are classified fictitious and 63.78% internal to linked clusters, leaving 15.02% unattributed. Only $187,861.35 demonstrably reaches a nameable catalog service, while $20,258,746.09 is an upper bound not provably manufactured. The advertised Base supply of 25,163 resources collapses to 811 distinct payTo recipients, 249 of which earned at least $10 lifetime; 474 of 910 hosts returned a live 402 challenge in a point-in-time probe.","quantitative_claims":[{"metric":"Base x402 settlements","value":"136,708,672","denominator":"all identified Base x402 settlements in study window","timeframe":"2025-09-17 to 2026-06-23 (280 days)","caveat":"Identification intersects EIP-3009 AuthorizationUsed events with curated facilitator allowlist."},{"metric":"gross Base value","value":"$44,121,383.81","denominator":"identified Base x402 settlements","timeframe":"280 days","caveat":"Gross settlement value is not equivalent to independent merchant demand."},{"metric":"fictitious share","value":"21.20%","denominator":"identified Base x402 settlements","timeframe":"280 days","caveat":"Fictitious is narrowly defined as self-payment or provably closed-loop activity."},{"metric":"internal linked-cluster share","value":"63.78%","denominator":"identified Base x402 settlements","timeframe":"280 days","caveat":"Internal does not necessarily prove common beneficial ownership; it does mean the activity cannot establish independent adoption."},{"metric":"nameable-service lower bound","value":"$187,861.35","denominator":"Base value that demonstrably reaches a named catalog service","timeframe":"280 days","caveat":"Lower bound, not total genuine demand."},{"metric":"live challenge hosts","value":"474/910 (52.09%)","denominator":"advertised Base hosts probed","timeframe":"point-in-time June 2026 probe","caveat":"Single-round GET-only liveness estimate."}],"state_before":"Previous run used ecosystem-level x402/MPP volume as evidence of machine-payment activity, with caveats but without population-scale authenticity decomposition.","action_taken":"Authors reconstructed payer, recipient, facilitator and funding/sweep clusters and classified settlements by economic independence.","observed_agent_behavior":"Large machine-timed settlement activity exists, but most observed Base settlements are provably fictitious or internal to linked clusters rather than evidence of independent buyer-to-seller demand.","outcome":"Headline settlement count is strongly downgraded as an adoption metric; economically independent paid-service demand must be measured separately.","time_horizon":"280 days","mechanism":"Sponsored gas and permissionless identities make repetitive settlements cheap; economic substance is only demonstrated when value exits the payer/operator cluster to an independent service.","moat_implication":"PAYMENT and PROTOCOL_STANDARDIZATION look more commoditized than headline counts imply. HISTORY_REPUTATION and verified independent economic-demand graphs become more defensible because they distinguish real commerce from manufactured activity.","h1":"Independent payer-to-independent-merchant economic substance predicts durable agent-commerce value better than protocol settlement count.","h0":"Raw settlement growth reliably measures broad agent payment adoption.","falsifier":"A reproducible later census showing most value moves from unrelated payers to unrelated merchants with repeat delivered-service usage.","belief_delta":"STRONGLY_FOR","next_best_test":"Rerun the released measurement pipeline on July-August 2026 flows and rank genuinely external merchant clusters by retained revenue and repeat independent payers.","novelty_reason":"Directly falsifies a key interpretation of x402 headline metrics used in the prior run and introduces population-scale authenticity measurement.","independence_cluster":"x402_population_measurement"}
{"record_id":"ATRA-20260907-02","probe":"agent_transaction_rails_alpha","observed_at":"2026-09-07T19:51:00+07:00","country":"GLOBAL","market_or_entity":"delegated-card agent payments for APIs/services","person_or_company":"Nevermined","role":"Agentic payments platform/operator","source_type":"docs","source_url":"https://nevermined.ai/","published_at":null,"palace_proximity_score":93,"evidence_grade":"A","verbatim_excerpt":"3,412 paid calls today","detailed_claim":"Nevermined's current operator site exposes an agent-payment flow where a buyer enrolls a tokenized card, sets a revocable budget/per-call mandate, and agents pay enabled merchants. Merchants connect Stripe or Braintree and keep existing payouts. The live surface reports 3,412 paid calls and $171 settled today and states Exa sells a $7 search key autonomously on a delegated card. Merchant pricing is listed at 1-2% of settled volume.","quantitative_claims":[{"metric":"paid calls today","value":"3,412","denominator":"Nevermined operator-reported daily merchant flow","timeframe":"current day at observation","caveat":"Platform-reported live counter; not independently audited."},{"metric":"settled today","value":"$171","denominator":"Nevermined operator-reported daily settlement","timeframe":"current day at observation","caveat":"Platform-reported and small absolute scale."},{"metric":"merchant fee","value":"1-2%","denominator":"settled volume","timeframe":"current published pricing","caveat":"Enterprise terms may differ."}],"state_before":"Agents ordinarily require a human-controlled payment credential or protocol-specific wallet and merchants face low-value card-fee friction.","action_taken":"Nevermined layers card delegation, mandates, metering and attribution over existing PSP settlement and offers prepaid/per-call/outcome pricing.","observed_agent_behavior":"Agents can autonomously buy a paid API/service key or metered call while staying inside a user-defined budget and per-transaction cap.","outcome":"A small but directly attributable paid-call economy is observable on existing PSP rails; merchant payout infrastructure does not need to be replaced.","time_horizon":"current live operator surface","mechanism":"Separate authorization/mandate from merchant settlement; use tokenized credential + policy controls to let agents spend without exposing raw card data while preserving merchant PSP relationships.","moat_implication":"PAYMENT itself is more commoditized; IDENTITY_TRUST, spend-policy control, metering, attribution and HISTORY_REPUTATION are potentially more defensible. Existing PSP connectivity reduces the moat of a closed settlement rail.","h1":"Agent payment connectivity commoditizes onto existing PSP rails while control, metering and attributed execution history retain value.","h0":"A new closed payment network is required for merchants to transact with agents.","falsifier":"Closed agent-native rails achieve materially higher merchant adoption, reliability and conversion than PSP-overlay systems across equivalent services.","belief_delta":"FOR","next_best_test":"Track Nevermined's independent merchants, repeat paying agents and settled revenue over 30 days and compare with x402-native services and MPP equivalents.","novelty_reason":"New operator with directly exposed attributable payment/settlement activity and a distinct existing-PSP architecture not covered in recent runs.","independence_cluster":"nevermined_psp_overlay"}
{"record_id":"ATRA-20260907-03","probe":"agent_transaction_rails_alpha","observed_at":"2026-09-07T19:51:00+07:00","country":"US","market_or_entity":"Wix Bookings service businesses in Google Search/Maps/AI Mode","person_or_company":"Wix.com / Koby Maman","role":"Booking platform; VP, Head of Wix Bookings","source_type":"blog","source_url":"https://www.globenewswire.com/news-release/2026/02/24/3243636/0/en/Wix-Launches-Integration-With-Google-Search-Google-Maps-and-Google-AI-Mode-to-Turn-Queries-Into-Instant-Bookings.html","published_at":"2026-02-24","palace_proximity_score":90,"evidence_grade":"B","verbatim_excerpt":"updated approximately every 30 minutes","detailed_claim":"Wix Bookings integrates service definitions, prices and near-real-time appointment availability into Google Search and Maps, with AI Mode support planned in the same integration. Availability refreshes approximately every 30 minutes. Users can choose a slot and complete on the Wix booking form; services with add-ons or price variations redirect into Wix's own calendar/qualification experience. The current rollout is open to Beauty services, with more verticals planned.","quantitative_claims":[{"metric":"availability refresh cadence","value":"approximately every 30 minutes","denominator":"Wix Bookings appointment inventory syndicated to Google","timeframe":"current integration","caveat":"No booking conversion or stale-slot failure rate disclosed."}],"state_before":"Service discovery and booking often required separate websites, phone calls or disconnected calendars.","action_taken":"Wix synchronized service, price and appointment inventory from its system of record into Google's consumer surfaces.","observed_agent_behavior":"Google can expose actionable time slots based on Wix supply state; complex service variants still hand off to Wix for qualification before final booking.","outcome":"Structured service supply becomes directly actionable from the discovery surface, but conversion/booking uplift is UNKNOWN.","time_horizon":"current integration","mechanism":"Authoritative system-of-record inventory is syndicated on a recurring cadence to the agent/discovery surface; simple availability can be standardized while complex qualification remains domain-specific.","moat_implication":"LIVE_AVAILABILITY, QUALIFICATION and PROPRIETARY_SUPPLY_GRAPH are more defensible than the front-end agent surface. BOOKING APIs commoditize, but authoritative capacity does not.","h1":"Local-service transaction advantage concentrates in live supply-state synchronization and qualification rather than generic agent browsing/calling.","h0":"Generic browser/phone agents can transact local services with comparable reliability without authoritative inventory feeds.","falsifier":"Controlled booking tests show browser/phone agents equal structured Wix-style feeds on booking accuracy, latency, cancellation and completion.","belief_delta":"FOR","next_best_test":"Run 50 matched service-booking tasks against structured Wix/Google businesses and phone/browser-only businesses, measuring time-to-book, stale-slot failure, qualification errors and post-booking changes.","novelty_reason":"First new run evidence directly connecting a mainstream SMB booking system of record to agent-facing live price/availability state.","independence_cluster":"wix_google_service_inventory"}
{"record_id":"ATRA-20260907-04","probe":"agent_transaction_rails_alpha","observed_at":"2026-09-07T19:51:00+07:00","country":"US","market_or_entity":"ACP native checkout merchant deployment","person_or_company":"ACP GitHub implementer/tester lance-web3","role":"Developer testing live merchant ACP checkout","source_type":"github","source_url":"https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/issues/248","published_at":"2026-05-11","palace_proximity_score":75,"evidence_grade":"B","verbatim_excerpt":"Glossier: only shows ‘Visit’ button","detailed_claim":"A developer checking which publicly named ACP merchants actually exposed native ChatGPT checkout reported Etsy US sellers appearing supported, while Glossier exposed only a Visit button, and requested an authoritative distinction between native checkout, discovery-only, in-ChatGPT app and coming-soon merchants. This does not quantify ACP market adoption, but it is first-hand evidence that protocol/public-launch association and live transactable checkout were not equivalent in May 2026.","quantitative_claims":[],"state_before":"Named merchants had been publicly associated with ACP/Instant Checkout rollout, creating an expectation of native in-chat transaction capability.","action_taken":"Developer manually checked named merchants' live ChatGPT shopping behavior and opened a protocol issue requesting authoritative deployment status.","observed_agent_behavior":"At least one named launch merchant presented redirect/Visit behavior rather than native checkout in the tester's environment.","outcome":"Live merchant transactability remained ambiguous and heterogeneous despite protocol support/public association.","time_horizon":"May 2026 field test","mechanism":"Open protocol capability, merchant integration, product/feed eligibility and consumer-surface activation are separate deployment layers; failure at any layer downgrades native checkout to redirect/discovery.","moat_implication":"PROTOCOL_STANDARDIZATION alone is commoditized; INTEGRATION_LOCK_IN and merchant-controlled checkout/fulfillment remain operationally important. A live deployment registry/telemetry layer could have value.","h1":"Protocol support and actual live native transactability are weakly coupled.","h0":"Announced ACP/UCP support reliably means users can transact natively.","falsifier":"An authoritative registry plus repeated field testing shows nearly all announced merchants expose stable native checkout across users/regions.","belief_delta":"FOR","next_best_test":"Run a weekly 50-merchant capability audit separating discovery/feed visibility, cart, native checkout, redirect, order-state access and refund/cancel support.","novelty_reason":"New first-hand merchant-surface implementation evidence, distinct from prior spec-level UCP failure records.","independence_cluster":"acp_live_merchant_deployment"}
