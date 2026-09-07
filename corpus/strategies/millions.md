Yes. This dig produced several **better sources than the polished success stories**, especially failures where we can see exactly what happened in the first 5–14 days.

The corpus is starting to look surprisingly good.

## Best new live / low-capital Google dropshipping experiments

| Source                                              | Starting state                           | Actual observed data                                                                        | Outcome                              |                     Research value |
| --------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------: |
| **18-year-old red-light mask test — July 2026**     | Standard Shopping, $289 product          | **10 days, $315 spend, 148 clicks, $2.10 CPC, 86% impression share, 0 ATC, 0 sales**        | Killed campaign                      |                     **S+ failure** |
| **Lumbar pillow — Apr 2026**                        | Standard Shopping, $20/day, CJ           | **2 weeks, $173 spend, 81 clicks, 4 ATCs, 1 checkout, 0 sales**                             | Failing                              |                     **S+ failure** |
| **New Shopping campaign barely serving — May 2026** | Manual CPC, then Max Clicks, then manual | Day 1–5 impressions: **1, 0, 3, 2, 0**                                                      | Operator kept changing campaign/feed |                  **S early-state** |
| **Pitiful_Gene795 — Apr 2026**                      | High-ticket Standard Shopping            | Days 1–4 no sales → days 5–6 movement → **~$10k by day 10**                                 | Winner                               |                **S+ longitudinal** |
| **Helena / girlfromblacksea — 2019**                | <$1k total business budget, 300 products | day 1: 200 impressions/0 clicks → Max Clicks → first sale within hours → 7 orders in 3 days | Eventually profitable                |            **S+ experiment diary** |
| **Merten — 2017**                                   | AdWords then $5/day Shopping             | $50 Google spend/0 orders → $150/2 orders → **Shopping at $5/day**                          | Shopping follow-up incomplete        |                  **S low-capital** |
| **$15/day Shopping — Oct 2025**                     | Manual CPC                               | ~4 days, **3.4k impressions, 102 clicks, $79 spend, 1 sale**                                | Early validation                     |                   **S low-budget** |
| **Day 26 diary — May 2026**                         | Shopping-led store                       | **$2,184 previous-day revenue**; feed/title changes + SKU splitting documented              | Scaling                              |                             **A+** |
| **$30/day PMax — Feb 2025**                         | 60-product store                         | Day 4 of PMax: **4–5 conversions/day**                                                      | Working                              | **A**, but store already validated |
| **Theo $0→$10k challenge**                          | New store                                | **$100 ads → $1,183 revenue → $643 reported profit** after first checkpoint                 | Winner                               |    **S commercial/operator claim** |

The two **failure cases** are particularly valuable.

### $289 red-light mask: near-perfect negative experiment

A first-time operator ran a brand-new store in July 2026 with:

```text
Product             $289
Campaign             Standard Shopping
Bid strategy         Maximize Clicks
Market               US

Days                 10
Spend                ~$315
Clicks               148
Average CPC          ~$2.10
Impression share     86%

Add to carts         0
Sales                0
```

They also did the economics themselves and concluded that at realistic cold-traffic conversion rates their expected CAC was around **$680 against roughly $245 contribution margin**, so they paused it. ([Reddit][1])

This is almost more useful than a winning case because:

```text
high impression share
+
plenty of clicks
+
zero ATC
```

means this was **not primarily an ads-delivery problem**.

It points toward:

```text
offer
trust
product-market fit
pricing
brand credibility
landing page
```

rather than “Google needs more time.”

That's a useful state classification.

---

## Another near-perfect failure: $20/day lumbar pillow

April 2026:

```text
Product              $64.99
Supplier             CJ Dropshipping
Shipping             12–15 days

Campaign             Standard Shopping
Daily budget         $20
Max CPC              $3

~2 weeks:
Sessions             143
Shopping clicks       81
CTR                   1.00%
Average CPC           $2.13
Spend                 $173

ATC                   4
Checkout              1
Sales                 0
```

([Reddit][2])

This is excellent because it gives us the **whole upper funnel**.

Compare it with the mask:

```text
MASK
click → no ATC

PILLOW
click → ATC → checkout → no purchase
```

Those should trigger completely different diagnoses.

And the pillow has an obvious potential friction point: a pain-relief product with a **12–15 day stated fulfillment time**.

---

# The funniest—and very useful—new Day 1 trace

Someone launched a new Shopping campaign on **May 4, 2026**.

Actual impressions:

```text
Day 1      1
Day 2      0
Day 3      3
Day 4      2
Day 5      0
```

During those five days they:

```text
started Manual CPC
changed bids several times
switched to Maximize Clicks
switched back ~24h later
changed Shopify/GMC feed structure
```

([Reddit][3])

This is hilarious because it's almost a controlled example of:

> **OBSERVE ≠ ACT**

There is essentially no data, but the operator is changing everything.

That belongs in our dataset as:

```json
{
  "state": "NO_DELIVERY",
  "evidence_count": 6,
  "actions": [
    "CHANGE_BIDS",
    "CHANGE_BIDDING_STRATEGY",
    "CHANGE_BIDDING_STRATEGY",
    "CHANGE_FEED"
  ],
  "diagnosis": "INSUFFICIENT_EVIDENCE_AND_EXCESS_INTERVENTION"
}
```

This stuff is exactly what an operator model needs.

---

# Helena's diary remains one of the best things on the internet

I dug further into the `girlfromblacksea` thread.

She explicitly started with a **maximum $1,000 investment** because she wanted testing rather than heavy upfront spending.

Initial store:

```text
~300 AliExpress products
no ecommerce experience
broad niche
```

Google Shopping:

```text
Merchant Center approval:     ~3 days

Initial bid:
enhanced bidding $0.15

First day:
~200 impressions
0 clicks
```

Then:

```text
switch → Maximize Clicks
```

and she reports her **first sale within several hours**.

Next three days:

```text
7 orders
~50% loss
```

But she intentionally used those losses as market-research spend.

She analyzed the product/query data, found one promising sub-niche, and **deleted 95% of the original products**.

Then:

```text
next month
~$1,000 revenue
roughly break-even
```

Then she experimented with:

```text
bid levels
negative keywords
queries
new related products
```

and reports approximately:

```text
next month
$300 net profit
~250 listings
```

Her big discovery was that roughly **40% of her search traffic was generic queries that didn't convert**, so she started aggressively excluding them. ([AliDropship Forum][4])

And her conclusions were essentially:

```text
high-ticket products
SKU-specific bidding
negative keywords
query analysis
add products people actually search for
```

That's 2019—and it looks remarkably similar to what our 2026 cases are independently telling us.

---

# There is even a literal `$5/day` Shopping experiment

An AliDropship forum user called **merten** maintained a running store diary in 2017.

Google Search/AdWords phase:

```text
$50 spent
0 orders

CTR:
8–15%

actual spend:
~$5–6/day
```

Later:

```text
~$150 Google spend
2 sales

avg CPC:
~$0.80
```

He concluded Search wasn't working well enough and then wrote:

```text
"I'm doing google shopping now for 5usd a day."
```

At the same checkpoint, his broader group of stores had finally become profitable, although unfortunately he never returned with a clean Shopping-only follow-up. ([AliDropship Forum][5])

Not a success story.

Still extremely valuable.

It demonstrates someone genuinely experimenting with **$5/day**, rather than retrospectively saying beginners can.

---

# The 2026 winner trajectory is the mirror image

Pitiful_Gene795 gives us almost the opposite transition.

Their high-ticket product went:

```text
Day 1       dead
Day 2       dead
Day 3       dead
Day 4       still dead

Day 5–6     movement begins

then:
5× ROAS day
6× ROAS day
8× ROAS day

by ~Day 10:
~$10,000 revenue
```

They report Shopify showing 22 purchases while Google attributed 16, so even their attribution didn't neatly reconcile. ([Reddit][6])

That is extremely useful paired with the red-light-mask failure.

### They initially look similar

```text
             MASK              PITIFUL

Day 1        bad               bad
Day 2        bad               bad
Day 3        bad               bad
Day 4        bad               bad
```

But:

```text
MASK
148 clicks
0 ATC
economics impossible

→ kill
```

whereas Pitiful's eventual downstream behavior changed.

So the actual lesson is **not**:

> Always wait ten days.

It's:

> Don't use elapsed time as the kill criterion. Use accumulated evidence.

That's a much better rule.

---

# Another contemporary low-budget datapoint

A ~$15/day manual Shopping operator reported after roughly four days:

```text
Daily budget          $15

Impressions         3,422
Clicks                102
CTR                  2.98%
Avg CPC              $0.78
Spend               $79.25

Sales                   1
```

That's basically the kind of experiment we want to run.

Not enough data to optimize intelligently yet—but enough to establish:

```text
Google serves product       ✓
people click                 ✓
someone purchases            ✓
```

Then calculate whether the economics close.

---

# And a useful $0-ish Google case appeared

A newer ecommerce operator documented their first week while spending only **a few pounds per day**, roughly £20–30 total.

The interesting part:

**their first two sales weren't attributed to the ads at all.**

They said the sales arrived through **Google organic/free Shopping**, shortly after correcting a Merchant Center GTIN issue. ([Reddit][7])

That reinforces something important for us:

```text
Merchant Center setup
≠ merely preparation for ads

Merchant Center itself
= acquisition channel
```

So the `$0 → $10/day` approach isn't theoretical.

---

# Theo's newer challenge is much better than his old origin story

His 2025 public challenge has an actual checkpoint video:

**“I Made $1183 From $100 Ad Spend ($0-$10k Dropshipping Challenge) - Ep.5”**

The video description explicitly indexes the whole series:

```text
Ep1  Start new store
Ep2  Live product research
Ep3  Build Shopify store
Ep4  Google campaign
Ep5  $1,183 from $100 spend
Ep6  2-week result
Ep7  32-day result
```

Episode 5 reports:

```text
Revenue            $1,183
Ads                ~$100
Reported profit      $643
Reported margin       55%
Period              3 days
```

and explicitly includes a P&L section. ([YouTube][8])

Then his two-week update reports:

```text
Revenue             $4,806
Orders                  13
Reported profit      $2,021

Longest drought:
6 straight days
without a sale
```

([LinkedIn][9])

That's excellent transcript material.

Self-reported + seller-of-education, obviously—but the chronology is unusually extractable.

---

# Another YouTube series lead: Kyle Bell

This is less proven but exactly the format we're looking for.

**Kyle Bell — “Day 1: Getting Started With Google Ads Dropshipping”**

He says he's building a new store from scratch to $1,000/day and documenting each step as a series. The video had only ~1.5k views when indexed, which makes it more interesting to me than the usual giant-channel retrospective case study. ([YouTube][10])

I'd harvest the channel and look for every subsequent store update.

---

# Arthur & Bryan have one particularly data-rich video we should extract

Their February 2026 video claims to show a brand-new store going from `$0 → $10k/day` in about two weeks and specifically says it breaks out:

```text
ad spend
revenue
ROAS
profit margins
day by day
```

with:

```text
Day 1 reported ROAS       ~4×
reported margin            ~50%
```

([YouTube][11])

They're selling education, so credibility weight goes down.

But **data density goes up**.

That's perfect for our `external_operator_trace` table where evidence quality is encoded separately.

---

# GitHub turned up something unexpectedly relevant

The strongest personal repo I found is:

### `downbythebay7-code/pretzel-outlet-feed-automation`

This appears to be tooling for an actual project called **Pretzel Outlet**, rather than a generic tutorial.

The author describes it as automation for:

```text
CJdropshipping
      ↓
product data
      ↓
CSV Google feed
      ↓
Google Merchant Center
      ↓
scheduled Vercel cron
```

with GTIN/MPN enrichment and feed-error handling.

The repository contains an actual serverless update script rather than just a README.

And look what the script actually does:

```text
CJ API
↓
electronics
home/kitchen
beauty
health/fitness
pet
baby
fashion

↓
fetch pages of products

↓
normalize:
id
title
description
link
image_link
price
availability
brand
product_type

↓
generate:
products.json
products.csv
```

That is basically a primitive implementation of the pipeline we've been describing.

[Pretzel Outlet Feed Automation on GitHub](https://github.com/downbythebay7-code/pretzel-outlet-feed-automation?utm_source=chatgpt.com)

### Important caveat

I would **not copy the implementation blindly**.

For example it hardcodes:

```text
availability = in stock
brand = CJdropshipping
```

rather than deriving those faithfully from supplier/product data.

That's exactly the sort of feed shortcut that can cause Merchant Center quality/compliance problems.

But architecturally?

Very relevant.

---

# `dropshipping-intel` is almost our research CLI concept

Another personal repo:

### `daniel-silva-perez/dropshipping-intel`

It is a TypeScript CLI designed around:

```text
product research
price tracking
competitor comparison
profit analysis
SQLite persistence
CSV/JSON exports
```

The author explicitly frames it as turning fragmented commerce research into a repeatable structured workflow. However, the public version currently uses **mock/demo data**, not genuine live supplier APIs.

So:

**architecture = useful**

**data = not useful**

[dropshipping-intel on GitHub](https://github.com/daniel-silva-perez/dropshipping-intel?utm_source=chatgpt.com)

This maps uncannily well onto our:

```text
market_product
keyword
supplier
economics
action
outcome
```

model.

---

# There's also an old dropshipping profit calculator worth stealing from

### `jamiewtam/profit-calc-react`

The README itself is useless boilerplate, but the code tree is much more revealing.

Its COGS module explicitly includes:

```text
Aliexpress.js
CJDropshipping.js
COGSByDate/
ManualCOGS/
```

That's useful because **daily supplier COGS reconciliation** is exactly the thing most Google dropshipping case studies omit.

[profit-calc-react on GitHub](https://github.com/jamiewtam/profit-calc-react?utm_source=chatgpt.com)

I'd investigate its API/backend before reusing anything, but the data model is relevant.

---

# Other GitHub pieces worth indexing

These aren't all dropshipping-specific, but they solve pieces of the exact system:

| Repo                                                 | Useful piece                                                                            |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `lucianfialho/gmp-cli`                               | Merchant Center CLI: products → CSV/raw JSON, issues, availability, GTINs, disapprovals |
| `elfeffe/google-shopping-product-feed`               | Simple programmatic Google Shopping feed generator                                      |
| `d1m007/gshoppingflux`                               | Current PrestaShop Shopping feed: multilang, multicurrency, reviews, inventory, cron    |
| `mardab96/google-ads-skills`                         | Agent-friendly Shopping feed QA, conversion tracking audit, landing-page analysis       |
| `google-marketing-solutions/feedgen`                 | Automated feed title/description/attribute improvement                                  |
| `google/shopping_insider`                            | Retail feed/performance diagnostics                                                     |
| `google-marketing-solutions/shopping-report-builder` | Pull Merchant Center reports programmatically                                           |

The personal `gmp-cli` is particularly interesting because it can emit Merchant Center product status to **CSV while retaining full API JSON**, including availability, price, GTIN, disapprovals and issue codes. ([GitHub][12])

FeedGen is useful specifically because its stated purpose is improving query matching, feed coverage and CTR by optimizing titles/descriptions/missing attributes. ([GitHub][13])

---

# What the failure data is starting to tell us

This is actually more interesting than finding another big winner.

We now have enough early-stage cases to identify at least five distinct failure states:

```text
STATE A
0 impressions
→ feed/bid/eligibility/market problem

STATE B
impressions but no clicks
→ offer/title/image/price/query-match problem

STATE C
clicks but no ATC
→ product/offer/trust/landing-page problem

STATE D
ATC/checkout but no purchase
→ shipping/payment/trust/price friction

STATE E
sales but unprofitable
→ economics/acquisition problem
```

And we now have **real public examples of almost every state**.

Most importantly, the July mask case shows why a rigid rule like:

> “Let Google run for 14 days.”

is wrong.

After:

```text
148 clicks
0 add-to-carts
```

you have substantially more evidence than someone who has run for five days and received six impressions.

**Evidence volume matters more than calendar time.**

That's one of the strongest conclusions from this new research.

---

## The sources I would crawl next

There are now four rabbit holes worth exhausting rather than broadly Googling forever:

1. **AliDropship forum user histories** — Helena/merten-style diaries contain wonderfully messy genuine longitudinal data.
2. **Reddit author histories** for every 2026 first-week post—find Day 1, Day 7, Day 30 from the same usernames.
3. **Theo/Kyle/Arthur-Bryan YouTube series** — transcript every episode and extract all dates/numbers/actions.
4. **GitHub commit histories** for personal Merchant Center/dropshipping stores—commits themselves can become an operator timeline: feed fix → GTIN addition → pricing change → GMC problem → subsequent feature.

The direction I would take the dataset now is **not just “successful Google dropshipping case studies.”**

I'd call the corpus something like:

```text
google_commerce_operator_traces
```

and deliberately ingest **every failure, stalled campaign, first-week experiment and abandoned store we can find**.

That dataset will teach us considerably more about when to **wait, fix, kill or scale** than another hundred millionaire screenshots.

[1]: https://www.reddit.com/r/Dropshipping_Guide/comments/1uv4b65/18yo_ran_google_shopping_for_a_289_health_device/?utm_source=chatgpt.com "18yo, ran Google Shopping for a $289 health device, 148 clicks, 0 sales, paused today honest feedback wanted"
[2]: https://www.reddit.com/r/dropshipping/comments/1sl3sn7/0_sales_in_2_weeks_on_google_shopping_143/?utm_source=chatgpt.com "0 Sales in 2 Weeks on Google Shopping — 143 Sessions, $173 Spent. What Am I Missing?"
[3]: https://www.reddit.com/r/googleads/comments/1t9xwj6/new_google_shopping_campaign_barely_spending/?utm_source=chatgpt.com "New Google Shopping campaign barely spending"
[4]: https://forum.alidropship.com/threads/how-i-got-my-first-sales-with-google-shopping-with-no-experience-in-e-com-and-digital-marketing-with-detailed-reports.14144/?utm_source=chatgpt.com "How I got my first sales with Google Shopping with no experience in E-com and digital marketing {with detailed reports} | AliExpress drop shipping forum – expert drop shipping community!"
[5]: https://forum.alidropship.com/threads/my-dropshipping-journey.586/?utm_source=chatgpt.com "My Dropshipping Journey | AliExpress drop shipping forum – expert drop shipping community!"
[6]: https://www.reddit.com/r/dropshipping/comments/1sbobsp/day_4_dead_store_day_10_10k_wtf_just_happened/?utm_source=chatgpt.com "day 4: dead store 💀 day 10: $10k… wtf just happened"
[7]: https://www.reddit.com/r/dropship/comments/1k6q68q?utm_source=chatgpt.com "A few questions from someone new to e-Commerce"
[8]: https://www.youtube.com/watch?v=OfxrWoqrd2Y&utm_source=chatgpt.com "I Made $1183 From $100 Ad Spend ($0-$10k Dropshipping Challenge) - Ep.5 - YouTube"
[9]: https://www.linkedin.com/posts/theo-clarke-2a7128200_i-built-a-brand-new-ecom-store-and-in-just-activity-7343276747238354946-68BH?utm_source=chatgpt.com "I built a brand new ecom store… And in just 2 weeks, I made $4,806 from only 13 orders. With $2,021 in pure profit. But here’s the wild part: I had 6 straight days of ZERO sales. This isn’t some… | Theo Clarke"
[10]: https://www.youtube.com/watch?v=OjfnEIjDmAY&utm_source=chatgpt.com "Day 1: Getting Started With Google Ads Dropshipping - YouTube"
[11]: https://www.youtube.com/watch?v=ryE3ITeQUtA&utm_source=chatgpt.com "$0 to $10K/Day Google Ads Dropshipping in 2 Weeks [Step-by-Step] - YouTube"
[12]: https://github.com/lucianfialho/gmp-cli?utm_source=chatgpt.com "GitHub - lucianfialho/gmp-cli · GitHub"
[13]: https://github.com/google-marketing-solutions/feedgen?utm_source=chatgpt.com "GitHub - google-marketing-solutions/feedgen: Optimise Shopping feeds with Generative AI · GitHub"
