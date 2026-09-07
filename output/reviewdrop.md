# Review: Drop — Ecommerce Intelligence Platform

*Full strategic review. 2026-09-06.*

---

## What This Repo Is

A monorepo for building evidence-selected, low-capital specialist ecommerce stores. The thesis: can an autonomous system find product-country arbitrage that human operators miss, and exploit it with $0–10/day budgets?

The answer is yes, but only if the system is disciplined about what it measures.

---

## The Corpus Is Stronger Than It Looks

On paper: 12 case studies, 52 sources, 15 strategy rules, 6 schemas, 5 research docs.

In reality: there's a complete economic model, a Bayesian scoring engine, a state machine, a funnel classifier, an EVOI calculator, and a full opportunity filter with 46 passing tests. This is not a research stub — it's a working analytical pipeline that just hasn't been connected to live data yet.

**Key files that matter most:**

| File | Why |
|------|-----|
| `packages/economics/model.py` | The money math. Landed cost, contribution, break-even CVR, headroom. |
| `packages/scoring/bayesian.py` | Beta-binomial CVR updating. The right way to handle small samples. |
| `packages/scoring/gates.py` | 7 hard gates. Prevents the system from falling in love with bad ideas. |
| `services/research/evoi.py` | Expected Value of Information. Tells you the cheapest next test. |
| `services/research/pipeline.py` | The main scoring pipeline. SerpApi → normalize → score → output. |
| `output/ALGORITHM.md` | The complete algorithmic opportunity filter. Worth reading in full. |

---

## What's Actually Working

1. **Economic model** — clean, correct, well-tested. The headroom bands (<1.0 structurally losing, >2.0 interesting) are the right abstraction.

2. **Bayesian CVR updating** — properly handles the "100 clicks = kill" fallacy. Beta-binomial with posterior predictive. This is the kind of thing that separates signal from noise at small scale.

3. **Hard gates** — 7 gates that prevent bad products from scoring well no matter what. Positive economics, plausible paid economics, data confidence, SKU saturation, supplier viability, query intent, free signal. Gate-first design is correct.

4. **EVOI** — the "what should we test next?" calculator. Free listing test ($0) vs $5/day test vs deep research. This is how you allocate limited budget.

5. **State machine** — DISCOVERED → RESEARCH → TEST → OPTIMIZE → SCALE → KILL. Clean lifecycle management.

6. **Funnel classifier** — classifies traffic stages and explains why premature kills happen. "100 clicks with 0 orders" might be a funnel problem, not a product problem.

---

## What's Broken or Missing

### The data gap is the real problem

Everything downstream of "we have live data" works. The problem is upstream:

- **No Merchant Center data** — we can't see what's popular in target countries
- **No Keyword Planner data** — we can't measure search demand per country
- **No live Shopping CPC data** — we're using estimates, not auction reality
- **No comparison site data** — Prisjakt, Hintaopas, PriceRunner are untapped
- **No supplier feed** — real costs are unknown for most candidates

The scoring engine is a sports car with no fuel.

### The candidates are stale

`real_candidates.json` has 10 products from weeks ago. The red-light mask and lumbar pillow were useful test cases but they're not real opportunities. The baby stroller (CAND-003) was the best candidate but has no live data behind it.

### No ingestion pipeline

There's no way to:
1. Pull new product data from Google APIs
2. Score it automatically
3. Track how scores change over time
4. Record what we tested and what happened

The `data/operator_events.json` has 21 manual entries. This needs to be automated.

### Duplicated data across three locations

`data/`, `corpus/`, and `research/` all contain the same files. The canonical location should be `data/`. The research bundle is useful as a portable export but shouldn't be edited directly.

### No integration with the Lab

The drop repo is standalone. It doesn't talk to WorkerKit, MWGym, HydraDB, or Oracle. The scoring pipeline exists but isn't part of the 21-step loop.

---

## Insights From the Research

### The millions docs are gold

Four research documents totaling 150K+ bytes of operator knowledge:

1. **millions.md** — Failure cases ($289 red-light mask: 0 sales, 148 clicks; lumbar pillow: 0 sales, 81 clicks). Key insight: $10k/day case has 0.48% CVR, not 4-5%. Most operators overestimate CVR by 10x.

2. **millions2.md** — Deep math on the $10k/day case. 7,500 sessions for 36 orders. $389 AOV. Campaign structure barely changed. Product was baby/toddler $300-500. The lesson: product × query × economics IS the strategy.

3. **millions3transcript.md** — Video transcript of a store scaling to €10k+/day. 100% Google fashion dropshipping. $30-40k+ days after 3 weeks. Key: Google Shopping, not Facebook.

4. **millions4.md** — Bryan Arthur's $20M revenue blueprint. 20 Google stores, 200k+ orders, ~20% net profit. Full playbook from niche selection to team building. This is the most complete operator guide in the corpus.

### The governing rule

From bigreview.md: **"Score contribution profit per click, not ROAS."** This is the single most important insight in the entire repo. ROAS is a vanity metric. Contribution profit per click tells you if you can scale.

### The 14-dimension opportunity rubric

From dev-plan.md: a scoring framework across 14 dimensions. Useful but needs to be connected to live data. Currently it's a rubric without inputs.

### Norway/Finland as test markets

The corpus identifies Norway as an ideal first market:
- $10.35B e-commerce market
- 86% online shoppers
- High AOV
- High CPC but high contribution per order
- VOEC customs complexity ( manageable)
- Prisjakt as a free data source

Finland is similar but smaller. Both are EU-adjacent with good payment infrastructure.

---

## The Google API Opportunity

We now have:
- Google Ads API (test mode, pending approval)
- Merchant Center API (live)
- $20/week free credits on GCP
- SerpApi key (500+ credits remaining)

### What we can do with Merchant Center API

**Popular Products report** — Google explicitly lets you filter by country, including countries you don't sell in yet. This is a free, first-party demand scanner. We can pull:
- What products are popular in Norway/Finland/Denmark/Sweden
- Popularity rank and trends
- Price ranges
- Category breakdowns

This alone is worth more than any third-party product research tool.

### What we can do with Google Ads API (once approved)

**Keyword Planner** — country-filtered search volume, competition, bid estimates. This gives us the demand × cost matrix per product per country.

**Auction Insights** — who's competing in Shopping auctions. Real competitor data, not estimates.

**Shopping metrics** — real CTR, CPC, impression share once we're running ads.

### What we can do with $20/week GCP credits

- BigQuery for analysis
- Vertex AI for product classification
- Cloud Storage for feed files
- Compute Engine for scheduled scraping

### Budget allocation for $20/week

| Use | Weekly Cost | Purpose |
|-----|-------------|---------|
| BigQuery | $5 | Analyze Merchant Center data at scale |
| SerpApi | $0 (free tier) | Product research, competitor analysis |
| Vertex AI | $10 | Product classification, content generation |
| Cloud Storage | $2 | Feed storage, data backups |
| Compute Engine | $3 | Scheduled data pulls |
| **Reserve** | **$0** | Buffer for spikes |

---

## The Foreign-Product Scanner Thesis

The most interesting thread in the entire repo is the foreign-product scanner concept:

> **Proven product × local demand × few competent sellers × weak merchant experience × usable supplier × cheap advertising relative to contribution margin.**

This is fundamentally different from "find winning products." It's "find products that are already winning elsewhere but are poorly served in a specific market."

The key insight: **Google Merchant Center's Popular Products report can show you what's popular in countries you don't sell in.** That's a free, first-party demand signal that no third-party tool can match.

The pipeline:
1. Pull popular products per country from Merchant Center
2. Cross-reference with Prisjakt/PriceRunner for seller density
3. Score merchant quality (images, content, reviews, shipping)
4. Measure Keyword Planner demand × CPC per country
5. Find suppliers with EU/Nordic warehousing
6. Calculate real economics
7. Rank by `GOOD_SELLER_GAP × ECONOMIC_HEADROOM`

This is buildable with the APIs we have.

---

## Open Threads

### 1. The "why hasn't someone already done this?" question

Every opportunity needs to answer: if this is so good, why aren't 15 competent sellers already there? The answer might be:
- Supplier won't authorize more retailers (moat if we can get in)
- Product isn't certified locally (kill)
- Manufacturer dominates sales (kill)
- Everyone buys from Sweden (interesting but complicated)
- Norway has weird import economics (could be manageable)
- Demand is mostly product research, nobody buys locally (kill)

### 2. The free listings play

Google free listings now show across Search, Shopping, Images, Lens, YouTube, Gemini. Norway and Finland are supported. The first test should be:
- 20 products
- Local-language store
- Correct Merchant feed
- Free listings only
- Observe impressions, queries, SKUs
- Zero ad spend

This is the cheapest possible market validation.

### 3. The "good seller gap" metric

Not just "how many sellers" but "how many GOOD sellers." A product with 8 sellers and 1 good specialist is more interesting than a product with 2 sellers and 2 good specialists.

### 4. The market asymmetry pattern

Germany proves the business. Norway provides the gap. Supplier bridges the two. If a product is popular in Germany with 34 sellers and 9 excellent specialists, but popular in Norway with 5 sellers and 0 excellent specialists, and the same EU supplier can serve both — that's the pattern.

### 5. The $20/day ceiling as a feature

The constraint of $0-10/day is actually an advantage. It forces:
- Free listings first (zero cost validation)
- Very controlled product groups (5-20 SKUs, not 5000)
- Clear decision gates at each phase
- Real learning from small experiments

### 6. The content moat

The biggest AI-native advantage isn't Photoshop. It's:
> "Tell me what you're trying to do, and I'll tell you exactly which model you should buy and why."

A local-language site with excellent decision support (comparison tables, use-case guides, compatibility info, expert recommendations) can compete on content even if it can't compete on price or reviews.

### 7. The data flywheel

Once we have live data:
- Merchant Center Popular Products → demand signals
- Keyword Planner → search volume × CPC
- Real Shopping campaigns → actual CPC, CTR, CVR
- Auction Insights → real competitors
- Price benchmarks → price positioning
- Search Console → organic queries

Each feeds back into the scoring model. The system gets smarter with every experiment.

### 8. The operator events are underutilized

`data/operator_events.json` has 21 events. Each one is a decision with a hypothesis and outcome. This is training data for the scoring model. We should be recording every decision automatically.

### 9. The Prisjakt integration

Prisjakt attempts to list every known national retailer for products. It refreshes prices and stock several times daily. It surfaces:
- Seller count
- Price history
- Stock status
- Delivery estimates
- Shop reviews

This is a free, structured competitor database for Nordic markets.

### 10. The feed optimization play

Once we have products, the feed is the experimental surface. FeedGen (already cloned) can optimize titles, descriptions, and attributes. FeedX can run A/B tests on feed variations. The feed is not just a data pipe — it's a controlled experiment framework.

---

## What I'd Do Next

1. **Wire Merchant Center Popular Products** → pull demand data for Norway/Finland/Denmark/Sweden
2. **Wire Keyword Planner** → get search volume × CPC per product per country
3. **Build Prisjakt scraper** → seller density, price history, stock status
4. **Refresh candidates** → re-score with live data
5. **Run first free listings test** → 20 products, local language, zero ad spend
6. **Record everything** → automatic operator events, not manual entries
7. **Apply for Google Ads Standard access** → unlock production API
8. **Build the 3-pass scanner** → machine scan (1000s), intelligence scan (100s), commercial verification (10s)
9. **Connect to Lab** → wire into WorkerKit/MWGym/HydraDB for tracking
10. **Ship the first store** → one country, lean catalog, free surfaces first

---

## The Bottom Line

The analytical infrastructure is surprisingly complete. The economic model, Bayesian scoring, hard gates, EVOI, and state machine are all working code with passing tests.

What's missing is the data pipeline: pull live demand, measure real competition, find real suppliers, calculate real economics.

The Google APIs we just set up are the missing link. Merchant Center Popular Products + Keyword Planner + Auction Insights give us the demand × competition × cost matrix that the scoring engine needs.

The foreign-product scanner concept — proven product × local demand × few good sellers × weak experience × usable supplier × cheap ads relative to contribution — is the right framework. It's buildable with what we have.

The constraint of $0-10/day is a feature, not a bug. It forces disciplined experimentation and prevents the "throw money at bad ideas" failure mode that kills most dropshipping operations.

The question isn't whether the system can find opportunities. It's whether we can build the data pipeline fast enough to feed the engine.
