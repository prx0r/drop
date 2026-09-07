# User Message — Installed Base Refinements + Self-Service Ratio

*Sent: 2026-09-07*
*Status: SAVED WORD-FOR-WORD*

---

Yes. That is the main flaw.

**A huge installed base does not automatically create a huge ecommerce opportunity.** For heat pumps, much of the economically valuable lifecycle event is:

> "My heat pump is dying" → installer diagnoses → installer supplies replacement unit → installer fits it.

In Finland, refrigerant-system installation/repair requires qualified professionals, and current replacement sellers typically sell the whole job as an installed package. One Finnish installer describes the replacement journey almost exactly as **send photos → receive quote → installer removes old unit and installs new one**, with typical installed replacement around €2,000–€3,500. ([AaltoAir][1])

So I was over-weighting **1.8–2M installed heat pumps** as though all lifecycle spend was accessible to Shopify. It isn't.

## The correct equation

Our old mental model was roughly:

```
installed base
× replacement rate
× compatibility difficulty
= opportunity
```

It needs another brutal filter:

```
ECOMMERCE OPPORTUNITY =

installed_base
× annual_failure_events
× CUSTOMER_PURCHASABLE_SHARE
× online_purchase_share
× information_gap
× probability_we_get_selected
× contribution_profit
```

`CUSTOMER_PURCHASABLE_SHARE` is critical.

For a heat pump:

```
WHOLE UNIT             very low
compressor             very low
refrigerant components very low
main PCB               low/medium
sensor                  medium
Wi-Fi module            high
remote                  very high
filters                 very high
covers/accessories      high
```

So **"Finnish heat-pump replacement" is an excellent macro signal but potentially a mediocre direct ecommerce TAM.**

---

# Mitsubishi remotes specifically illustrate both sides

They are genuinely consumer-purchasable. Finnish retailers currently sell Mitsubishi remotes directly around **€99–€141**, and buyers are told to verify exact indoor-unit series/generation. ([Innoair][2])

So the problem exists.

But that reveals flaw #2:

> **The easy-to-sell subset may be too economically small.**

500,000 Mitsubishi units sounds enormous.

But suppose:

```
500,000 installed units

× 2% annual remote/control replacement
= 10,000 events/year

× €120 average order
= €1.2m total theoretical annual retail

× 20% market capture
= €240k revenue

× 30% gross margin
= €72k gross profit
```

Those are illustrative assumptions, not measured rates—but they show why **installed-base numbers can seduce us**.

The real question isn't "how many heat pumps?"

It's:

> **How many independently purchasable compatibility events occur each year?**

That is the number Snowball needs.

---

# There are several other serious flaws in the thesis

### 1. We may optimize beautifully for an agent that never gets asked

The query has to actually happen.

A consumer might not say:

> "What replacement PCB fits my Mitsubishi MSZ-FH35VE?"

They may say:

> "Heat pump stopped working."

And ChatGPT correctly tells them:

> call a technician.

We never enter the purchase funnel.

The best GeoDrop subgraphs therefore have a strong natural consumer action:

```
"I lost this remote."
"This connector broke."
"I need another filter."
"This pump switch cracked."
"I need an adapter for these two devices."
```

Much stronger than:

```
"My complex appliance isn't working."
```

---

### 2. Identification has to be possible without professional diagnosis

This is huge.

A customer can photograph:

```
remote
connector
filter
pressure switch
valve
adapter
charger
battery
```

and plausibly identify it.

They often cannot visually determine:

```
compressor fault
PCB fault
sensor fault
refrigerant leak
motor winding failure
```

So add:

```
VISUAL_DIAGNOSABILITY
```

to Snowball.

Photo-first agent commerce wants objects where **the thing needing replacement is itself observable**.

---

### 3. "Machine-readable" doesn't mean "Google ranks us first"

This is another place we must avoid fooling ourselves.

Google's new Merchant Center fields are very exciting because they make products more understandable to AI Mode.

But Google has **not** said:

> "More `product_detail` fields = higher ranking."

Likewise:

```
related_product
Q&A
manuals
MPN
images
```

increase our machine-readable evidence surface.

They **do not guarantee selection**.

Google may still favor:

- established merchant trust;
- price;
- delivery;
- reviews;
- historical performance;
- marketplace breadth;
- feed quality;
- conversion likelihood.

So this is an **information advantage**, not a cheat code.

---

### 4. The authoritative source may beat us automatically

Suppose ChatGPT resolves:

> Mitsubishi remote `E2281J426`.

Then it finds:

```
Mitsubishi authorized dealer
€139
in stock

ours
€145
dropshipped
```

Why should it choose us?

It probably shouldn't.

Therefore merely rewriting an existing SKU beautifully isn't enough.

We need to own the **uncertain step before the SKU is known**:

```
USER:
"I have this old remote."

OURS:
identify generation
resolve SKU
explain compatibility
provide current successor
```

Once the exact commodity SKU is known, price/logistics start dominating again.

**The information moat is upstream of fulfillment.**

---

### 5. Suppliers can destroy our margin

Classic dropshipping flaw remains.

Beautiful agent data can't save:

```
retail €139

wholesale €112
shipping €9
payment €4
return reserve €5
support €3
Google Ads €15
```

We're dead.

So no subgraph becomes `LAUNCH` before we have **actual dealer net pricing**.

This remains the biggest missing field in much of Snowball.

---

### 6. Wrong-part returns can erase the whole business

Compatibility-heavy products are attractive because information is difficult.

Unfortunately, that's also what makes them dangerous.

If we confidently sell the wrong €130 component:

```
outbound shipping
return shipping
customer service
opened packaging
supplier restocking fee
ad spend
```

can vaporize several successful orders.

So compatibility needs evidence states:

```
VERIFIED
manufacturer explicitly lists fit

INFERRED_HIGH
same assembly / authoritative cross-reference

UNCERTAIN
visual similarity only

CONTRADICTED
explicitly not compatible
```

Only `VERIFIED` should get:

> **Guaranteed fit**

This is potentially a real competitive advantage.

---

### 7. The local-language advantage isn't permanent

Norwegian/Finnish fragmentation is a real current opportunity.

But LLM translation is excellent and multinational merchants will increasingly enrich catalogs centrally.

So:

> "We're Norwegian"

is not a moat.

The enduring part is:

```
Norwegian installed-base knowledge
+
legacy model aliases
+
local suppliers
+
local inventory
+
historical generations
+
actual compatibility evidence
```

Language is the wedge.

**The graph is the moat.**

---

### 8. Google/ChatGPT may simply choose marketplaces

This is perhaps the largest strategic risk.

If the exact part is available:

```
Amazon
eBay
FixPart
OEM
```

with excellent price, delivery, returns and thousands of reviews, the agent may sensibly choose them.

Our solution should not require winning every transaction.

Potentially:

```
RESOLUTION ENGINE
      ↓
best outcome

our Shopify        → margin
Amazon/eBay        → affiliate
OEM                → affiliate/referral
local supplier     → referral
technician         → service referral
```

That is stronger than insisting:

> "Everything must be dropshipped through our Shopify."

But you want niches you can OWN, so ideally we find cases where **no dominant merchant has clean coverage yet**.

---

# This changes which niches I like

Once I add **customer replaceability + visual diagnosability**, my rankings change.

## Much stronger

### Norwegian cabin water components

Things like:

```
pressure switches
pump heads
filters
membranes
connectors
12V pumps
control switches
heater controllers
```

Cabin owners are unusually likely to DIY small infrastructure because the property may be remote and these are comparatively simple components.

Much closer to:

> "this exact plastic/electrical thing broke; get me another."

### Marine retrofit adapters

Excellent.

User often knows the problem:

> "I upgraded this display and this old transducer connector doesn't fit."

No technician necessarily required.

High-value certainty.

Small shipping.

Lots of legacy equipment.

### Garage/gate control ecosystem

Remote, receiver, photocell, control unit, adapter.

Extremely photographable.

Very compatibility-heavy.

Consumer often buys directly.

Need to find an underserved geography/brand generation because the broad niche has incumbents.

### Commercial equipment consumable/easy parts

Coffee machine:

```
seal
basket
valve
knob
sensor
filter
```

Restaurant equipment:

```
thermostat
switch
seal
handle
basket
```

The business has urgency and will happily photograph a broken component.

---

# Weaker than I previously thought

### Whole heat-pump lifecycle

Excellent graph.

Weak direct-to-consumer ecommerce across much of the graph.

Keep it as:

> **consumer-safe control/accessory subgraph**

rather than whole heat pump.

### EV charger replacement

Same issue.

A broken charger often becomes:

> electrician/service company.

Accessories can be ecommerce, but installed-base maturity is limited.

### Heat-pump PCBs/compressors

They look attractive due to £/€ value.

But likely technician procurement.

Wrong buyer.

---

# There's a really important new metric

Call it:

## **Self-Service Resolution Ratio**

For every subgraph:

```
Of 100 problems involving this installed asset,
how many can realistically go:

photo
→ identify
→ buy item
→ user installs/swaps
→ solved

WITHOUT
professional diagnosis or regulated work?
```

Rough conceptual examples:

| Subgraph | Self-service ratio |
| --- | ---: |
| Remote controls | Very high |
| Filters | Very high |
| Marine adapters | High |
| Cabin pump switches | High |
| Garage remotes | High |
| Robot-mower chargers | High |
| Heat-pump Wi-Fi interfaces | Medium-high |
| Appliance pumps | Medium |
| Heat-pump PCB | Low |
| Compressor | Near zero |
| Whole heat pump | Near zero |

This should be a **multiplicative factor**, not a minor score.

---

# Another metric: "pre-SKU uncertainty"

This may be our most important advantage.

Consider two products.

### Product A

User searches:

> `Bosch 00631200`

They already know the SKU.

We're just another merchant.

### Product B

User says:

> "This came out of the water system in my 2008 Norwegian cabin."

and uploads a photo.

That's where we can add enormous value.

Define:

```
PRE_SKU_UNCERTAINTY =
how difficult is it for a nonexpert
to translate their physical problem
into an exact purchasable SKU?
```

We want **high uncertainty but high resolvability**.

That's the sweet spot.

---

# So the actual winning function becomes

```
GEODROP_AGENT_SCORE =

installed_base
× replacement_event_rate
× SELF_SERVICE_RESOLUTION
× PRE_SKU_UNCERTAINTY
× visual_identifiability
× compatibility_complexity
× digital_supplier_gap
× supplier_accessibility
× gross_profit_per_resolution
× local_language_fragmentation

÷
wrong_fit_risk
÷ marketplace_quality
÷ regulatory_friction
```

That is much better than our previous model.

And I suspect it will push **heat-pump remotes down slightly while pushing cabin components, marine retrofit components and similarly boring user-swappable legacy hardware up substantially.**

## The heat-pump lesson

So your instinct is correct:

**No, "1.8M heat pumps and 33% replacements" does not by itself justify a dropshipping store.**

In fact, the replacement-wave statistic largely describes **installer revenue**, because whole heat-pump replacement requires skilled work and refrigerant handling. ([AaltoAir][1])

What it *does* tell us is:

> Finland contains an enormous aging installed base worth mining for **specific consumer-purchasable failure surfaces**.

That's still useful—but it's a lead generator for subgraph discovery, not the business thesis itself.

The sharper opportunity is:

> **Find physical systems with millions of installed units where a meaningful fraction of failures reduce to "identify this weird replaceable object correctly and get it to me."**

That is the version I would now make Snowball optimize for.

[1]: https://aaltoair.fi/artikkelit/ilmalampopumpun-vaihto-vanhan-tilalle
[2]: https://www.innoair.fi/ilmalampopumppujen-suodattimet-ja-kaukosaatimet

---

*Source: User message*
