# GitHub ↔ X Rabbit Hole Discovery

*Generated: 2026-09-07*
*Status: VERIFIED — All claims backed by public sources*

---

## Executive Summary

The biggest discovery is that the useful alpha is **not merely "engineers building agentic commerce."** We can now see several actual decision functions in public code.

The strongest new artifact is **Shopify's own agent-facing Global Catalog instructions**. It publicly tells an agent what should be treated as a hard exclusion versus a soft ranking signal. Combined with Anthropic's open ranker, NVIDIA's recommendation pipeline, Timefold's scheduler, and Probook's public dispatch features, we can reconstruct a surprisingly complete Agent Commerce / Supplier OS architecture.

---

## The GitHub ↔ X Hidden-Goat Graph

| Person               | Public identity                 | GitHub                       | Why they matter                                                                                                                                                            |
| -------------------- | ------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gil Greenberg**    | **X `@gilgNYC`**                | **`gil--`**                  | Shopify engineer; open-sourced an iMessage shopping agent actually exercised against real merchants. Also contributes directly to Shopify's UCP tooling. |
| **Ilya Grigorik**    | **X `@igrigorik`**              | **`igrigorik`**              | Central Shopify/UCP architect. Following his PRs/replies exposes capabilities before normal ecommerce discourse catches up.                                                |
| **Ali Shazal**       | LinkedIn verified; X unresolved | **`alishazal`**              | Committer on Anthropic's new `commerce-agents` repo and co-author of Anthropic's production commerce-agent playbook.                                                       |
| **Matthew Koen**     | LinkedIn verified; X unresolved | unresolved                   | Anthropic Applied AI; co-author of commerce-agent blueprint. Publicly discusses production workflows involving appointments/revenue/automation.                            |
| **Geoffrey De Smet** | **X `@GeoffreyDeSmet`**         | **`ge0ffrey`**               | Timefold CTO / OptaPlanner creator. This is the optimization layer beneath a Probook-like dispatch brain.                                                                  |
| **Jing Li**          | social unresolved               | **`jingyli`**                | Google/UCP contributor behind Location/serviceability capabilities relevant to local services.                                                                             |
| **Lee Hwa**          | social unresolved               | **`lhwa`**                   | Meta contributor to ACP proposals around product feeds, feed provenance and pricing.                                                                                       |
| **Alex Springer**    | OpenAttribution public identity | **`jalexspringer`**          | Building the attribution layer for recording what content agents retrieved/cited before a transaction.                                                                     |
| **Radovan Synek**    | blog/LinkedIn                   | **`rsynek`**                 | Timefold routing/optimization engineer; very relevant to field-service scheduling.                                                                                         |
| **Lukáš Petrovický** | public professional profile     | **`triceo`**                 | Core Timefold solver engineer.                                                                                                                                             |
| **Antonio Martinez** | LinkedIn/NVIDIA verified        | NVIDIA blueprint contributor | Working directly on NVIDIA's open agentic-retail recommendation/search implementation.                                                                                     |
| **George Eliadis**   | **X `@georgeprobook`**          | unresolved                   | Probook founder. Public signal is extraordinary; actual dispatcher code appears private.                                                                                   |
| **Lewis Zhang**      | LinkedIn verified               | unresolved                   | Probook CTO. Particularly interesting because he previously worked on Roblox player/server matching.                                                                       |

---

## Key Discoveries

### 1. Gil Greenberg is the new hidden goat

This came from following **Ilya → X activity → Gil → GitHub**, exactly the GitGoblin pattern.

Gil's repo `gil--/ucp-agent-imessage` is an invite-only iMessage shopping-agent proof of concept. The README says it **runs and has been exercised against real merchants**. It searches Shopify's Global Catalog, keeps separate carts for different merchants, creates checkout, links Shop identity and—in approved conditions—can complete an exact purchase.

The architecture reveals:

```
DISCOVER → Shopify Global Catalog (anonymous)
CART → merchant-specific, reversible
CHECKOUT → agent credential, reviewable
PURCHASE → buyer-linked Shop credential, exact amount approval, idempotent
```

The LLM **doesn't own the transaction**. Gil explicitly separates:

```
MODEL: interpret intent, compare products, propose tools, recommend
DETERMINISTIC APPLICATION: trusted product provenance, merchant identity,
  cart state, checkout state, budget, payment credential,
  authorization, exact-total approval, purchase completion
```

**Use the LLM for fuzzy matching/reasoning. Never use it as the ledger or authorization system.**

---

### 2. Shopify has published an Agent SEO operator manual

Shopify's public `Shopify/ucp-cli` contains a skill designed for agents using the Global Catalog.

#### Soft ranking context
- intent, country, region, postal code, currency, language, eligibility

#### Hard filters
- price, availability, ships_to, ships_from, condition, taxonomy/category, product attributes, ratings, price tier

#### Search heuristics
- **Pagination gives more of the same ranking.** If results aren't satisfying intent, change the query first—synonyms, narrower/broader terms, brand names—rather than blindly paging.

The shopping agent loop:

```
intent → translate to catalog vocabulary → retrieve → bad candidate set?
  yes → reformulate query
  no → hard filters → reason about survivors
```

---

### 3. Anthropic published a reference ranking function

`anthropics/commerce-agents` — official reference implementation.

#### Text-field weighting
```
title        3.0
brand        2.0
category     2.0
attributes   1.5
description  1.0
```

#### Ranking pipeline
```
apply hard filters → calculate relevance → remove score == 0
best_score = highest candidate
keep only: candidate_score >= best_score × 0.50
try soft filters → if soft filters remove everything: abandon them
sort by relevance → rating breaks relevance ties
```

#### Higher-level search skill
```
extract: budget, recipient, dates, size, intended use, dealbreakers
USER STATED constraint → hard filter
ASSUMED preference → search/query wording
phrase the request in catalog vocabulary, not customer's wording
```

---

### 4. NVIDIA exposes a more sophisticated recommender

```
USER/CART → EMBEDDING RETRIEVAL (top K) → USER UNDERSTANDING AGENT + NLI ALIGNMENT AGENT
  → CONTEXT SYNTHESIS → ITEM RANKER → DETERMINISTIC GUARD
```

#### Candidate intent score
```
0.8 – 1.0   strong fit
0.4 – 0.7   moderate fit
0.0 – 0.3   weak fit
```

Primary candidates: `alignment_score > 0.7 AND product not in cart`. Backfill if < 3 survive.

Final priority: `1. CROSS-SELL FIT, 2. ALIGNMENT SCORE, 3. DIVERSITY`

Deterministic validation: `product exists, stock > 0, margin acceptable, not in cart`

---

### 5. NVIDIA's promotion decision function

Precomputed signals: inventory pressure, competitive pricing position, seasonality, product lifecycle, demand velocity, allowed margin-safe actions.

| Condition                             | Action               |
| ------------------------------------- | -------------------- |
| Low inventory                         | No promo             |
| High inventory + already below market | None / free shipping |
| High inventory + at market            | 5%                   |
| High inventory + above market         | 10%                  |

Modifiers:
- peak/post-season → discount +1 tier
- pre-season → free shipping
- clearance → discount +1
- new arrival → reduce to free shipping
- demand slowing → discount +1
- demand rising → discount -1

The server removes actions violating margins. The LLM merely chooses among **safe actions**.

---

### 6. Probook + Timefold = Supplier OS optimization

Probook dispatch features:
```
technician skill / experience, geography, availability,
historical performance, conversion / close rate, ticket size,
job type, job priority, customer context, equipment context,
ETA, forecasted revenue
```

Timefold solver hierarchy:
```
HARD: capacity, must finish before end time
MEDIUM: maximize jobs assigned
SOFT: minimize driving time
```

Reconstructed objective:
```
eligible(job, tech) = skills/license fit ∧ service area ∧ availability
  ∧ schedule feasibility ∧ equipment/job requirements

score(job, tech) ≈
  + w1 × P(conversion | technician, job)
  + w2 × expected_ticket_value
  + w3 × skill_fit
  + w4 × customer/technician affinity
  - w5 × travel_time
  - w6 × predicted lateness
  - w7 × schedule_disruption
  + w8 × job_priority
  + w9 × utilization/fairness
```

---

### 7. Business Arena = long-horizon agent business simulation

Alibaba/Accio team's `CommerceAgentBench` + `BusinessArena`:

```
source products → allocate capital → enter markets → price → advertise
replenish → negotiate → handle customers → stay compliant → react to demand
```

Economic equation: `business value = deployed capital × capital turnover × realized margin`

---

### 8. The canonical algorithm

```
USER INTENT → QUERY NORMALIZATION → HARD ELIGIBILITY GATE
  (stock, price, location, service area, skills, shipping, deadlines)
  → CANDIDATE RECALL (lexical / embedding / graph)
  → RELEVANCE PRUNE
  → MULTI-OBJECTIVE RANK (intent fit, quality, value, trust, price, margin, delivery, diversity)
  → DETERMINISTIC GUARD
  → HUMAN/AGENT CHOICE
  → AUTHORIZATION GATE
  → TRANSACTION → OUTCOME DATA → learning
```

That is **Supplier OS**. Not "LLM does everything." But constraint solver + retrieval/ranker + prediction models + state machine + LLM reasoning around the ambiguous edges.

---

## The Five Core Repos

```text
Shopify/ucp-cli
anthropics/commerce-agents
gil--/ucp-agent-imessage
NVIDIA-AI-Blueprints/Retail-Agentic-Commerce
TimefoldAI/timefold-quickstarts
```

## The Eight Watching Repos

```text
Universal-Commerce-Protocol/ucp
agentic-commerce-protocol/agentic-commerce-protocol
Accio-org/CommerceAgentBench
Accio-org/BusinessArena
agentcommercekit/ack
openattribution-org/*
```

---

## What to Monitor

The **highest-alpha signals** are diffs that change:

```text
ranking fields
filter semantics
constraint weights
search context
eligibility
trust/provenance
personalization
price/availability freshness
merchant identity
checkout capability
dispatch objective
attribution
```

This is the `ALGO_SURFACE_CHANGED` detector.

---

## Crawl Log

1. Started from `@georgeprobook` → Probook → founder/team pages → Sequoia profile → Lewis Zhang
2. Confirmed Summers autonomous-booking claim; found 2,542 vs 2,873 discrepancy; kept 2,542
3. Extracted Probook's publicly disclosed dispatcher features
4. Searched Probook/Lewis GitHub; found tempting `lzhang` matches but they were unrelated; rejected
5. Pivoted through UCP/ACP protocol engineers
6. Followed Ilya's X activity → Gil Greenberg
7. Found `gil--/ucp-agent-imessage`; inspected real-merchant architecture and `src/agent.ts`
8. Followed Gil into `Shopify/ucp-cli`
9. Found explicit soft-context vs hard-filter split and search heuristics
10. Opened `anthropics/commerce-agents`; located actual reference search ranker
11. Traced commit to Ali Shazal, then Anthropic's commerce article to Matthew Koen
12. Tried to resolve X identities; rejected unverified names
13. Followed recommender implementations into NVIDIA Retail Agentic Commerce
14. Extracted recommendation YAML: 0.7 cutoff, NLI bands, candidate backfill
15. Found NVIDIA's promotion arbiter decision table
16. Followed Probook optimization into Timefold
17. Extracted hard/medium/soft solver hierarchy
18. Followed Timefold maintainers to Geoffrey De Smet / Radovan Synek / Lukáš Petrovický
19. Opened Alibaba's CommerceAgentBench + BusinessArena
20. Checked ACK/OpenAttribution as identity/trust/attribution layer
