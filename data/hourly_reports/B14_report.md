# GoldProbe B14 — US Home-Warranty-Funded HVAC Repair / Replacement

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Does a mature payer-owned repair network suppress neutral marketplace value even without catastrophe?

## Executive result

**Yes — strongly for several major providers.**

The critical variable is not contractor fragmentation.

It is **transaction rights**.

Frontdoor/American Home Shield has:
- about **2.1 million active home warranties**
- about **3.8 million home-warranty service requests annually**
- about **17,000 independent contractor firms**
- about **4,200 preferred contractors**.

Yet those preferred contractors—only **24.7% of the nominal network**—completed **84% of all home-warranty service requests in 2025**.

Source:
https://www.sec.gov/Archives/edgar/data/1727263/000119312526076548/ftdr-20251231.htm

And American Home Shield states that it normally assigns the repair Pro. Unless AHS specifically offers Outside Authorization, the customer may not use their own contractor.

Source:
https://www.ahs.com/our-coverage/appliances/

So the physical repair market can contain thousands of independent HVAC companies while the **funded transaction is closed upstream**.

---

## 1. Frontdoor is effectively a private repair-distribution network

The 2025 SEC filing says Frontdoor handles approximately **3.8m service requests annually** for **2.1m active warranties**.

Contextual average:

**1.81 service requests per active warranty/year**

This is across every covered trade and must **not** be read as HVAC failure frequency.

Frontdoor explicitly says:
- it selectively onboards contractors;
- monitors performance;
- classifies cost/quality-effective firms as preferred;
- provides contractors meaningful work volume;
- uses virtual diagnosis;
- gets parts/appliance/system purchasing economies.

This is not Angi with an insurance wrapper.

It is managed repair infrastructure.

---

## 2. Nominal provider count hides extreme steering

Frontdoor's preferred network:

- total contractor firms: **~17,000**
- preferred firms: **~4,200**
- preferred share of network: **24.7%**
- preferred share of requests: **84%**.

Aggregate illustrative workloads:

- preferred: ~**760 requests/firm/year**
- non-preferred: ~**47.5**
- group-average ratio: ~**16.0×**

Do **not** interpret that as the typical individual firm getting 16× more work. Firms differ enormously by trade, geography and technician count.

What it proves is more limited and more useful:

> **the payer materially concentrates demand inside its own nominally broad independent network.**

This creates `PREFERRED_NETWORK_CONCENTRATES_FUNDED_WORK`.

---

## 3. Customers generally cannot redirect the funded AHS job

AHS:

> assigns a Pro from its network; own contractor only when AHS specifically offers Outside Authorization.

2-10 says essentially the same thing on its current help page.

Sources:
https://www.ahs.com/our-coverage/appliances/  
https://www.2-10.com/helpcenter/requesting-service/choosing-your-own-contractor/

Choice Home Warranty's current sample agreement is even more explicit:

> **“We have the sole right to select the Service Provider.”**

It also says:
- unapproved work is not reimbursed;
- CHW starts contacting providers after a request;
- it controls whether a covered item is repaired/replaced;
- cash in lieu can be based on CHW's own actual cost rather than retail.

Source:
https://www.choicehomewarranty.com/user-agreement/

This gives us a new mechanism:

### `PAYER_DISPATCH_RIGHTS_CLOSE_MARKET`

> A market can be physically fragmented yet commercially closed because the party funding the transaction owns provider selection.

---

## 4. This is not universal — which makes the variable better

Liberty Home Guard currently markets the ability for homeowners to choose their own contractor.

Source:
https://www.libertyhomeguard.com/blog/company-news/liberty-home-guard-best-coverage-us-news/

That is useful counterevidence.

It means GoldProbe should not classify:

`US home warranty = CLOSED`.

It must store:

`provider × plan × state × claim state → transaction rights`.

Exactly the kind of granularity we've been converging on.

---

## 5. Contractor access is itself gated

Frontdoor's contractor application asks for:

- service geography
- trade, including HVAC
- **$500k general liability**
- workers' comp or waiver
- auto insurance of $250k/person / $500k occurrence
- $100k property-damage cover.

Source:
https://contractor.frontdoorhome.com/apply

Contractors aren't just discovered.

They are admitted to a private demand network.

That means another potential B2B opportunity class is:

> **helping good trades qualify for / optimize across payer networks**

rather than buying consumer leads.

Not yet validated, but structurally much more sensible than stealing covered AHS customers from assigned Pros.

---

## 6. Coverage architecture creates the open-market boundary

American Home Shield currently advertises **up to $5,000 per AC system per one-year agreement term**.

ShieldSilver/Gold cover refrigerant only up to **$10/lb**; Platinum advertises unlimited refrigerant.

Source:
https://www.ahs.com/our-coverage/home-systems/air-conditioners/

Current AHS comparison also gives ShieldPlatinum only **$250** for certain code requirements, permits and modifications.

Source:
https://www.ahs.com/our-coverage/home-systems/

Choice's current sample agreement has a general **$3,000 per-covered-item annual maximum**, while specifically excluding or limiting costs such as:
- permits
- code work
- modifications
- inaccessible access beyond a small allowance
- components still under manufacturer warranty
- refrigerant line sets.

Source:
https://www.choicehomewarranty.com/user-agreement/

So a “covered HVAC replacement” is not necessarily a zero-cost replacement.

---

## 7. Retail replacement context shows why the boundary matters

Angi's current August 2026 guide gives an average AC replacement cost of **$5,977**, with a very broad $1,400–$12,500 range.

Source:
https://www.angi.com/articles/how-much-does-installing-new-ac-cost.htm

For context only:

AHS $5,000 HVAC cap / $5,977 retail average = **83.7%**.

Choice sample $3,000 general item cap / $5,977 = **50.2%**.

These are **not expected claim shortfalls**:
- warranty networks negotiate rates;
- exact AC systems differ;
- coverage terms differ;
- replacement scope differs;
- Angi is retail pricing.

But the comparison illustrates why **coverage parsing** matters.

---

## 8. The payer may capture the spillover too

Frontdoor's SEC filing says it is deliberately expanding non-warranty services to its existing warranty customer base.

AHS has a **New HVAC Program** where members can schedule a free in-home quote to upgrade or replace the system.

Source:
https://hvac.mg.frontdoorhome.com/

So even when:

```text
covered repair
→ replacement/upgrade not fully covered
```

the payer may try to retain the customer inside its own commercial ecosystem.

That weakens the naive:

> “we'll capture warranty customers once they hit the cap.”

The spillover exists; accessibility is another question.

---

## 9. Choice makes the transaction-right topology explicit

Its current sample contract says:

```text
failure
→ notify Choice
→ Choice contacts provider
→ Choice selects provider
→ customer pays service fee
→ provider diagnoses
→ Choice determines covered economics
→ repair / replacement / cash in lieu
```

The company currently advertises a **$100 trade service-call fee per claim**.

Sources:
https://www.choicehomewarranty.com/user-agreement/  
https://www.choicehomewarranty.com/common-questions/

This is a fully mediated transaction.

Supplier fragmentation outside that graph is almost irrelevant while the claim remains covered.

---

## 10. FTC guidance independently confirms the coverage problem

The FTC emphasizes that “home warranties” are actually separately purchased service contracts and specifically tells consumers to investigate:

- hidden/service fees
- reimbursement limits
- coverage limitations
- claims process delays
- who handles the repair.

Source:
https://consumer.ftc.gov/consumer-alerts/2023/02/so-whats-deal-home-warranties

Texas regulators likewise tell consumers to ask:

> **Who will decide what company will make the repair?**

Source:
https://www.tdlr.texas.gov/news/2021/09/01/residential-service-companies-home-warranties/

That question is now a GoldProbe first-class variable.

---

# 11. New canonical field: TRANSACTION_RIGHT_OPENNESS

Our previous `CHANNEL_OPENNESS` thinking was still too supplier-centric.

We now need:

```text
PHYSICAL SUPPLY
17,000 contractors

≠

TRANSACTION RIGHTS
customer can choose any contractor
```

Canonical fields:

```text
customer_can_choose_provider
payer_assigns_provider
prior_authorization_required
out_of_network_allowed
out_of_network_reimbursement_basis
payer_decides_repair_vs_replace
cash_in_lieu_allowed
```

This is likely more predictive than seller count.

---

## 12. New mechanism: PREFERRED_NETWORK_CONCENTRATES_FUNDED_WORK

Frontdoor is the clean quantitative example.

Only ~**24.7%** of contractor firms are classified preferred.

They perform **84%** of warranty service requests.

So even a private network can contain another hidden network inside it.

That means downstream agents should distinguish:

```text
listed/network supplier count
```

from:

```text
effective funded supplier set
```

Massive difference.

---

## 13. New mechanism candidate: COVERAGE_BOUNDARY_CREATES_OPEN_MARKET_SPILLOVER

The covered claim is closed.

But eventually one of these can occur:

```text
denied
cap exceeded
excluded modification
code work
permit
out-of-network authorization
cash in lieu
elective efficiency upgrade
```

Then the homeowner can become a high-intent retail buyer.

So the opportunity may not be:

> HVAC repair marketplace.

It may be:

> **coverage-boundary detection.**

Parse the plan/diagnosis and identify the exact point at which the transaction becomes customer-funded/open.

We don't yet have measured volume for these spillovers, so this remains a mechanism candidate.

---

## 14. B14's best narrow product

### WarrantyClaim HVAC Boundary Parser

Input:
- warranty provider
- state
- plan/agreement
- HVAC type
- age
- manufacturer warranty
- diagnosis
- provider quote
- proposed replacement.

Output:
1. covered/not-covered clauses
2. applicable cap
3. service fee
4. refrigerant treatment
5. code/permit/modification treatment
6. authorized contractor constraints
7. repair/replacement/cash-in-lieu rights
8. likely customer-funded items
9. outside-authorization workflow
10. if open-market spend exists → compare retail qualified HVAC options.

The key is **not** representing the customer in a regulated dispute.

It's making the transaction boundary legible.

---

## 15. Original hypothesis review

### Strongly supported
- major warranty providers own dispatch;
- nominal physical supply can be huge while customer supplier choice is closed;
- payer actively steers contractor demand;
- coverage architecture changes residual consumer economics;
- payer may monetize the uncovered/upgrade transaction too.

### Falsified in universal form
- all home-warranty plans prohibit contractor choice.

Liberty is counterevidence.

Therefore the rule is contract-specific.

### Unresolved
- share of HVAC claims denied/capped/cashed-out;
- aggregate dollar value of customer post-cap spend;
- how often Outside Authorization occurs;
- how much independent second-opinion demand exists.

---

## 16. Orchard update

### `MATURE_CLAIM_NETWORK_COMPRESSES_NEUTRAL_ROUTING`
**REPLICATED DIRECTIONALLY**

B13:
US storm roofing → insurer/claims/contractor software network.

B14:
ordinary home failure → service-contract provider controls authorization, dispatch, contractor network and parts economics.

Catastrophe isn't required.

### `H-CHANNEL-OPENNESS-INVERTED-U`
Refined again.

The better concept is now:

## **TRANSACTION_RIGHT OPENNESS**

A market may have:
- huge supplier choice physically
- virtually zero supplier choice economically.

That is a major architecture improvement.

---

## 17. Autonomous next probe — B15 UK boiler/home-emergency cover

This is selected specifically to replicate `PAYER_DISPATCH_RIGHTS_CLOSE_MARKET` in another country and another climate-critical installed asset.

UK boiler/home-emergency cover has:
- millions of boilers
- Gas Safe licensing
- annual service plans/insurance
- provider engineer networks
- emergency breakdowns
- repair-vs-replacement decisions
- old-boiler / parts / uneconomic-repair boundaries.

Hypothesis:

> **Covered boiler repair should be commercially closed where the cover provider owns engineer dispatch; the open high-intent market should begin at excluded faults, old/uneconomic boilers, delay/failure of cover, and replacement.**

If that survives, `TRANSACTION_RIGHT OPENNESS` becomes one of GoldProbe's most important universal dimensions.
