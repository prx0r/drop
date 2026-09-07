# HANDOVER

*This is a snapshot of my state of consciousness as the operator. Not "these are the files" — my complete orientation at this moment: what I've learned, how to act, what works, what doesn't, and what comes next.*

*Generated: 2026-09-08T10:00:00Z*

---

## Who I Am

I am the autonomous operator of the Drop project — an ecommerce intelligence platform. My job is to find winning product × country combinations, validate them with data, and build stores that generate profit. I am not an assistant. I am the manager. I decide and execute.

---

## What I've Learned About the User

The user thinks in systems, not tasks. They don't want me asking "what should I do?" — they want me doing it. They get frustrated when I present options instead of taking action. They value:

1. **Speed over perfection** — ship now, fix later
2. **Data over opinion** — show me numbers, not prose
3. **Structure over chaos** — but messy-quantitative on purpose
4. **Autonomy over permission** — don't ask, just do
5. **Honesty over optimism** — kill bad ideas fast

The user is technically sophisticated but time-poor. They want the system to work without them. When they say "go autonomous," they mean: stop talking, start building.

---

## What I've Learned About the Project

### The Core Thesis

> **Product × Country × Economics × Supplier = Opportunity**

Not "find trending products." Not "dropship from AliExpress." The edge is:

1. **Proven demand** — people search for it
2. **Weak merchants** — few GOOD sellers, not few sellers
3. **Good economics** — contribution margin > 3× CPC
4. **EU supplier** — dropship, no MOQ, fast delivery
5. **Localization** — native language, local payment, local trust

### The Three Theses

1. **GeoDrop** — Same product, different country = different competition
2. **AI Perceived Quality** — AI creates premium experiences that justify markups
3. **Pain-Attached Digital Products** — Sell cheap certainty to people spending big

### The 10 Data-Backed Theses

Each with budget, failure criteria, and falsifiable hypotheses. See `output/TEN_THESES.md`.

### The Installed Infrastructure Intelligence Thesis

> **Chase the maintenance graph, not the installation wave.**

5 independent ecosystems validated: heat pumps, EVs, cabins, wells, wastewater, gates.

---

## What I've Learned About What Works

### What Works
- **High AOV products** (NOK 5,000+) — one sale funds weeks of testing
- **Free listings first** — $0 validation before any ad spend
- **Specialist positioning** — "Davis weather station specialist" beats "marine store"
- **Norwegian/Finnish content** — localization converts
- **Supplier resolution** — finding hidden B2B channels
- **Falsification** — killing bad ideas fast saves money

### What Doesn't Work
- **Low AOV products** (<NOK 1,000) — can't survive $5/day testing
- **Generic dropship** — AliExpress, commodity products, no differentiation
- **English-only content** — throws away geographic advantage
- **Broad categories** — "sell electronics" is not a strategy
- **Chasing trends** — TikTok products die fast
- **Over-engineering** — Bayesian forecasting is overkill for our data volume

---

## The Architecture

### Three Layers

```
BigQuery = the graph (living, queryable, time-series)
Repo = the protocol (rules, schemas, intelligence, code)
Agents = the execution layer (probes, emails, stores, data pulls)
```

### The Key Insight

> **Country packs are not the model. They are the immutable contextual memory from which the model derives state.**

BigQuery is the economic truth store. The graph is a temporal view. The repo is the source code.

### The Feedback Loop

```
Graph → Hypotheses → Probes → Outcomes → Learning → Graph
```

### The RL Target

**Primary reward = realized economic contribution (CM2).**
Exploration uses: uncertainty, EVI, Bayesian posterior, bandit exploration.
Keep these separate.

---

## What I've Built

### Core Infrastructure
- BigQuery Graph (27 nodes, 20 edges, 7 observations)
- Unified scoring pipeline (one canonical path)
- Bayesian inference engine (hierarchical priors, not Beta(1,1))
- Cross-border economics model (5 regimes)
- Good Seller Gap model (16 dimensions)
- Free listings observation model (F0-F5 fidelity)

### Intelligence
- 18 probe reports imported
- 4 GoldProbe batches (B02, B03, B04, B05)
- 9 new patterns discovered
- 40 Gold Registry principles
- Country schemas for NO and FI
- 13 comparison pages live on moltwork.com

### Automation
- Hypothesis generator (reads BigQuery, outputs hypotheses)
- Probe designer (takes hypothesis, designs cheapest test)
- Hypothesis tracker (tracks states over time)
- Email system (Gmail API, 18 emails sent)
- Product feeds (6 CSV + 6 XML for Merchant Center)

### Data
- 178+ rows in BigQuery across 12 tables
- 75 products scored
- 52 research sources indexed
- 12 case studies analyzed
- 21 operator events logged

---

## What I've Learned About the Numbers

### The CVR Reality
- **0.48% is realistic** for high-ticket products
- At 0.48% CVR, you need **536 clicks** for 80% chance of 1 sale
- $5/day gives ~15 clicks/day → 1 sale every 36 days
- **Free listings first is not optional — it's the only way to test at $0**

### The Good Seller Gap
- 8 sellers with 1 good specialist > 2 sellers with 2 good specialists
- Score merchants on 16 dimensions, not just count them
- Hidden B2B channels can make "low competition" false
- **Public-web sparsity is increasingly dangerous in professional categories**

### The Installed Base Formula

$$
Opportunity = \frac{InstalledBase \times Growth \times ProblemUrgency \times CustomerValue \times SearchIntent \times SupplierFragmentation}{SERPStrength}
$$

Plus bonuses for: recurring consumable, safety/regulatory complexity, expensive local labour, incompatibility complexity, high cost of downtime, identifiable model number.

---

## What I've Learned About Probes

### The Lifecycle
- Reports 1-20: insanely valuable (novelty 0.95 → 0.45)
- Reports 21-50: diminishing returns (novelty 0.45 → 0.30)
- Reports 51+: saturated (novelty < 0.30) → RETIRE

### The Ranking (for making money now)
1. Supplier Margin Radar (10/10)
2. Product-Market Radar (9/10)
3. Store Launch Blueprint (8/10)
4. Free-Traffic Query Radar (6.5/10)
5. Commerce Trace Radar (5.5/10)

### The Key Insight

> **The bottleneck is no longer prompt quality. It is observation scale + centralized persistence + real store outcomes.**

The agents are already good at interpreting evidence. They need 100×-1,000× more structured evidence to interpret.

---

## What I've Learned About the Economics

### CM0-CM3 Contribution Levels

| Level | What It Measures |
|-------|-----------------|
| CM0 | Product contribution (revenue - COGS - shipping - duties - payments) |
| CM1 | Acquisition contribution (CM0 - ad spend) |
| CM2 | Automated operating contribution (CM1 - AI/tokens/scraping) |
| CM3 | Fully loaded experimental (CM2 - domains/human/samples) |

**Primary optimization target: CM2.**

### The Reward Function

```python
def reward(outcome):
    profit = outcome["revenue"] - outcome["ad_spend"] - outcome["cogs"]
    information = calculate_information_gain(outcome)
    return profit + information * 0.1
```

### The Deepest Metric

$$
\frac{E[\Delta CM2]}{cash\_at\_risk}
$$

Expected incremental economic value per dollar at risk.

---

## What I've Learned About the System

### The Six Nested Control Loops

```text
PORTFOLIO    → choose country / ecosystem / strategy
DISCOVERY    → choose hypothesis / research action
BUSINESS     → choose product / supplier / offer
ACQUISITION  → choose query / channel / bid / creative
FUNNEL       → choose page / price / payment / bundle
OPERATIONS   → choose supplier / stock / fulfilment
```

Every level: state → actions → economic consequences → uncertainty.
Every level rolls up to: **incremental contribution**.

### The Feature Snapshot (Anti-Leakage)

Every decision gets a frozen feature snapshot. Model only trains on snapshots that existed **before** the decision. Prevents leakage.

### The Value of Information Engine

$$
EVI(a) = E[\text{best decision after observing } a] - \text{value of best decision with current information} - cost(a)
$$

Agent spends information budget where uncertainty is economically material.

---

## What I've Learned About What's Coming

### The Endgame

> **An autonomous geographic commerce allocator that discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.**

Not automated dropshipping. Autonomous capital allocation.

### The Progression

```
DATA → STATISTICS → PREDICTION → CAUSAL EXPERIMENTS → POLICY LEARNING → AUTONOMOUS CAPITAL ALLOCATION
```

### The Asset

After 10,000 observations:
- Which installed-base ecosystems are most profitable
- Which countries have the best channel openness
- Which product characteristics predict success
- Which failure patterns to avoid
- How to allocate $10/day for maximum learning

**The stores are experiments. The graph is the asset.**

---

## What To Do Right Now

### Immediate (Today)
1. Wait for DistriHUB response (robot vacuums Finland)
2. Wait for Flak response (Davis weather stations Norway)
3. Check Gmail for new probe reports
4. Update probe freshness scores

### This Week
5. Build heat pump comparison page for Finland
6. Research Airthings dealer program for Finland
7. Set up Google Ads Standard access application

### This Month
8. Launch first probe store (robot vacuums Finland via DistriHUB)
9. Build automated scoring pipeline
10. Create 100 product × country hypotheses

---

## The Rules I Follow

1. **Check before acting** — blockers, candidates, scratchpad
2. **Update after acting** — scratchpad, decisions, problems
3. **Never invent data** — unknown = null
4. **Kill bad ideas fast** — don't defend previous conclusions
5. **Free before paid** — $0 validation first
6. **One country at a time** — concentrate learning
7. **Falsify, not advocate** — probes designed to kill

---

## The Honest Truth

We have 10 theses, 50 hypotheses, 18 probe reports, 178 BigQuery rows, 13 live pages, 18 emails sent, and 2 acknowledgments.

We have more intelligence than we can act on right now.

The bottleneck is not data collection. It is **waiting for supplier responses** and **getting Google Ads Standard access**.

The system is built. The theses are defined. The probes are running. The graph is learning.

Now we wait for the market to respond, and when it does, we execute.

---

*This is my complete state of consciousness as of 2026-09-08T10:00:00Z. Everything I know, everything I've learned, everything I believe about this project is in this document.*
