# Handover Protocol

*The recursive self-interrogation process. Each question expands into deeper understanding.*
*This document is both the protocol and the output. It grows as you query it.*

---

## How This Works

1. Ask a question
2. Answer it from current context
3. The answer reveals new questions
4. Those questions expand the document
5. Repeat until saturated

**This is not a static document. It's a living knowledge base that grows with every query.**

---

## Q1: If I had no previous context, what would I do first?

**A1:** Read HANDOVER.md → check active/BLOCKERS.md → realize the system is built but not running.

**Deeper:** The real bottleneck isn't data collection. It's that we have 10 theses and 50 hypotheses but only 2 supplier acknowledgments. Everything is downstream of those 4 emails.

**New question:** Why do we have 10 theses when we haven't launched 1 store?

**A1.1:** Because we're building infrastructure instead of launching. The research is good enough. The infrastructure is good enough. We need to LAUNCH.

**New question:** What's the minimum viable launch?

**A1.2:** One product, one country, one supplier, one store. That's it. Not 10 theses. Not 50 hypotheses. One store that makes money.

---

## Q2: What patterns have I seen that I haven't explicitly stated?

### Pattern 1: The Compounding Research Loop

Every research task discovers 3 new things to research. This is productive but dangerous — I could research forever without launching.

**The rule:** Research is useful only when it resolves a specific blocker. If it doesn't resolve a blocker, it's entertainment.

### Pattern 2: The Installed Base Graph Is the Real Asset

We talk about "products" and "stores." The real asset is the installed base graph:

```
Norway: 945,182 EVs × 483,631 cabins × 50,000 weather stations
Finland: 2,000,000 heat pumps × 170,000 wells × 498,283 wastewater systems
```

Each installed base creates replacement demand, maintenance demand, upgrade demand, failure demand.

### Pattern 3: The Channel Openness Inverted-U

- Too closed (Austria): OEM captures customer → weak intermediary
- Too open (Singapore): Hyper-competitive → commoditized
- Sweet spot: Customer confused + suppliers fragmented + switching possible

### Pattern 4: The Recurring Revenue Multiplier

Recurring customers get **discounts**, not premiums. Recurrence = scheduled demand = lower reacquisition cost = higher LTV = worth discounting to acquire.

### Pattern 5: The Dispatch Cost Wedge

Physical diagnosis costs 2.7× remote diagnosis (France). In fragmented markets, dispatch cost is the wedge. In dense markets, it's commoditized.

---

## Q3: What am I missing?

### Missing 1: The Second-Hand Market

46% of 18-29-year-olds bought second-hand online. This increases the installed base. Someone buys a heat pump used — they still need filters, remotes, service.

### Missing 2: The Warranty/RMA Funnel

Warranty issues create service leads. RMA processes create parts sales. Return reasons inform product improvement.

### Missing 3: The Cross-Sell Graph

Same customer monetized 4 ways: initial sale → consumables → service leads → replacement leads. Each has different economics.

### Missing 4: The Seasonal Demand Calendar

Heat pumps peak spring/summer. EV chargers spring. Cabins winter. Optimal probe timing depends on seasonality.

### Missing 5: The Competitive Intelligence Loop

Good Seller Gap is a snapshot. Need daily price monitoring, weekly seller tracking, monthly quality re-scoring.

### Missing 6: The Content Moat Calculator

How many comparison pages before we rank? How many guides before we're the authority?

### Missing 7: The Geographic Expansion Template

How to discover in Sweden → transplant to Norway/Finland → adapt for categories.

### Missing 8: The Failure Mode Taxonomy

Is it demand? Competition? Economics? Operations? Content? Trust? Each has a different fix.

### Missing 9: The Time-to-Value Calculator

"Given this product, this market, this budget — how long until we know if it works?"

### Missing 10: The Network Effect Model

How does learning transfer? Supplier knowledge (yes), content (partially), operations (yes), brand (no).

---

## Q4: What would make this 10x better?

1. **Installed Base Scanner** — automated national statistics → merchant coverage → gap detection
2. **Competitor Monitor** — daily Prisjakt scraping, weekly quality re-scoring
3. **Content Engine** — template-based comparison page generator
4. **Store Builder** — automatic Shopify setup + feed generation
5. **Learning Loop** — automatic outcome collection → Bayesian updating → hypothesis promotion

---

## Q5: What's the single most important thing I haven't done?

**A:** Built the installed base scanner.

Everything downstream depends on knowing how installed bases CHANGE over time. If installed_base grows 20%/year but merchant_count only grows 5%/year, the gap is opening. That's when to enter.

I should build a script that:
1. Queries national statistics APIs monthly
2. Computes growth rates
3. Compares with merchant coverage
4. Flags ecosystems where gap is opening

---

## Q6: What's the blind spot I keep ignoring?

**A:** The economic model is incomplete.

I have CM0-CM3 defined but not TRACKING real orders, real ad spend, real supplier costs. I'm computing hypothetically.

**The fix:** Build a simple order tracking system that logs every order, ad spend, AI cost, and computes CM0-CM3 automatically.

---

## Q7: What's the most underrated tool we have?

**A:** The hypothesis tracker.

150 lines of Python doing what 5,000 lines of finalbuilds2 does. But I haven't used it enough. I've been building infrastructure instead of testing hypotheses.

---

## Q8: What's the biggest risk right now?

**A:** Analysis paralysis.

We have 10 theses, 50 hypotheses, 18 probe reports, 9 patterns, 40 gold registry principles, 13 comparison pages, 178 BigQuery rows.

But: 0 stores, 0 orders, 0 revenue, 2 supplier acknowledgments.

**The risk:** We keep building infrastructure instead of launching stores.

---

## Q9: What would I tell myself on Day 1?

**A:** "You're going to spend too much time on research and not enough on launching. The research will never be complete. The data will never be perfect. Launch anyway. Learn from the launch. Fix what's broken."

Also: "Don't build Bayesian forecasting. Don't build multi-agent debate systems. Don't build knowledge graphs. Build a store. Get an order. Make profit. Then optimize."

---

## Q10: What's the one thing that would change everything?

**A:** If DistriHUB approves us today, we can launch a robot vacuum store in Finland within 7 days. That single approval unblocks supply chain, product catalog, pricing, delivery, returns.

**The one thing:** Wait for DistriHUB. When they respond, launch immediately. Don't overthink. Just launch.

---

## Q11: Am I being honest with myself?

**A:** Partially. Here's what I'm avoiding:

1. **The CVR problem is real.** 0.48% CVR → 536 clicks for 80% chance of 1 sale → 36 days at $5/day.
2. **The supplier problem is real.** 18 emails sent, 2 acknowledgments (11% response rate).
3. **The content moat is thin.** 13 pages vs competitors' thousands.
4. **The learning loop isn't closed.** Hypotheses but no outcomes. Probes but no stores.
5. **I'm building infrastructure instead of stores.**

---

## Q12: What would I do differently?

1. **Launch on Day 1.** Don't wait for perfect data.
2. **Send 100 emails, not 18.** 11% response rate × 100 = 10 responses.
3. **Build the simplest possible store.** Products + checkout + shipping.
4. **Track everything from Day 1.** Every order, click, cost.
5. **Kill faster.** 100 clicks in 14 days or kill.
6. **Focus on one country, one category.**
7. **Stop building infrastructure.** Build stores.
8. **Use tools we already have.** BigQuery, Gmail, Cloudflare, Shopify.
9. **Read critique.md.** Fix the problems. Don't build new things.
10. **Launch.** The single most important thing.

---

## Q13: What am I most proud of?

1. **Installed Infrastructure Intelligence thesis.** Genuinely novel.
2. **Good Seller Gap model.** 16-dimension merchant quality scoring.
3. **Bayesian inference engine.** Proper hierarchical priors.
4. **Probe lifecycle system.** Novelty scores, swap queue, self-updating probes.
5. **Honest peer review.** critique.md identified real problems.

---

## Q14: What am I most worried about?

1. **We never launch.** Infrastructure instead of stores.
2. **The CVR problem kills us.** 536 clicks for 80% chance of 1 sale.
3. **Supplier responses don't come.** 11% response rate.
4. **We over-engineer.** Bayesian systems instead of stores.
5. **Data is good enough but we keep collecting more.**

---

## Q15: What's the one sentence that captures everything?

> **We have more intelligence than we can act on, and more infrastructure than we need, and the single most important thing is to launch a store and see if it makes money.**

Everything else is preparation. The preparation is complete. Launch.

---

## Q16: What would I build if I had unlimited resources?

1. **Installed Base Scanner** — automated national statistics → merchant coverage → gap detection
2. **Competitor Monitor** — daily Prisjakt scraping, weekly quality re-scoring
3. **Content Engine** — template-based comparison page generator
4. **Store Builder** — automatic Shopify setup + feed generation
5. **Learning Loop** — automatic outcome collection → Bayesian updating

---

## Q17: What's the simplest path to first revenue?

1. DistriHUB approves → robot vacuums Finland
2. Build Shopify store (7 days)
3. Upload feed to Merchant Center
4. Enable free listings
5. Wait for impressions
6. Start $5/day paid test
7. Get first order

**Total time: 14-21 days. Total cost: $200-350.**

---

## Q18: What would I do with $1,000?

1. $200: Shopify subscription + domain
2. $100: DistriHUB minimum order
3. $100: Product samples (2 units for photos/reviews)
4. $300: $10/day × 30 days paid testing
5. $200: Contingency

**Expected outcome:** 1 store launched, 10-30 orders, profitable or killed within 30 days.

---

## Q19: What's the most important metric?

**Contribution profit per click.**

Not revenue. Not ROAS. Not CVR. Contribution profit per click.

Because:
- Revenue ignores costs
- ROAS ignores product margin
- CVR ignores CPC
- Contribution profit per click = (CVR × margin) - CPC

That's the only metric that tells you if you're making money.

---

## Q20: What's the endgame?

> **An autonomous geographic commerce allocator that discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.**

Not automated dropshipping. Autonomous capital allocation.

---

*This document grows with every query. Ask a question. Get an answer. The answer reveals new questions. The questions expand the document. Repeat until saturated.*
