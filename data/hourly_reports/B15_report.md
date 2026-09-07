# GoldProbe B15 — UK Boiler / Home-Emergency Cover

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Does `PAYER_DISPATCH_RIGHTS_CLOSE_MARKET` replicate independently outside US home warranties?

## Executive result

**Yes — strongly.**

The UK is especially useful because the physical trade market is extremely open while the insured transaction can be extremely closed.

English Housing Survey data estimates **21.2 million English households (86%) used gas-fired main heating in 2023-24**.

Source:
https://www.gov.uk/government/statistics/english-housing-survey-2023-to-2024-low-carbon-technologies-in-english-homes-fact-sheet/english-housing-survey-2023-to-2024-low-carbon-technologies-in-english-homes-fact-sheet

Gas Safe Register had **151,701 registered engineers at 31 March 2023**, and consumers can openly search registered businesses by postcode.

Yet once a household enters a British Gas/HomeServe cover claim, the transaction rights change.

---

## 1. Physical market: open and enormous

The 2024 English Housing Survey says **93% of dwellings have central heating**.

By 2024:
- condensing boiler: **19%**
- condensing-combination boiler: **63%**.

Source:
https://www.gov.uk/government/statistics/chapters-for-english-housing-survey-2024-to-2025-headline-findings-on-housing-quality-and-energy-efficiency/chapter-2-energy-efficiency

So this is an enormous mature installed-asset ecosystem.

Gas Safe supply is also huge and openly searchable.

A naive GoldProbe might therefore say:

> 21m gas-heated homes + 150k engineers = fantastic routing marketplace.

B15 shows why that is incomplete.

---

## 2. British Gas creates its own private service economy

Centrica reported **2.899 million British Gas Services & Solutions customers in 2024**.

It also performed:
- **304,000 on-demand jobs**
- **81,000 boiler installs**
- contract customer retention of **86%**.

Source:
https://www.centrica.com/media/2pjoazw0/annual-report-and-accounts-2024-untagged.pdf

Those 2.899m customers are **not** all HomeCare boiler policyholders; the definition includes contract and on-demand services.

Centrica's current 2026 business page says British Gas has a **7,000+ engineering force** and describes Services & Solutions as the UK's No.1 boiler installer.

Source:
https://www.centrica.com/our-businesses/retail/british-gas/

That's vertically integrated distribution.

---

## 3. HomeCare closes the covered transaction

Current British Gas HomeCare includes:

- unlimited boiler repairs
- parts and labour
- annual service
- £0 / £60 / £99 excess options
- up to £1,000 access/make-good per repair
- its engineer network
- emergency/priority servicing.

Source:
https://www.britishgas.co.uk/cover/boiler-and-heating.html

At that point the customer isn't shopping 150,000 Gas Safe engineers.

They contact British Gas.

So again:

```text
PHYSICAL OPENNESS
huge

TRANSACTION_RIGHT OPENNESS
low while covered
```

B14 replicates perfectly.

---

## 4. Age changes one specific right: replacement

British Gas says it covers boilers of any age if they're working and parts remain obtainable.

But free replacement if the boiler can't be repaired is generally limited to:

- boiler **under 7 years**
- or under **10 years if British Gas installed it and continuously covered it**.

For older boilers it will still attempt repair, but free replacement isn't included under that condition.

Source:
https://www.britishgas.co.uk/cover/guides/boiler-warranty-homecare.html

This gives us a more precise mechanism than:

> old assets lose cover.

They don't necessarily.

### `AGE_CHANGES_REPLACEMENT_RIGHT_NOT_REPAIR_RIGHT`

A payer can preserve repair entitlement while progressively transferring replacement risk back to the owner.

---

## 5. Parts availability is an explicit underwriting gate

British Gas says that during the initial visit for an older boiler it checks that:

- the model can be supported
- **spare parts are still available**.

If it cannot cover the boiler, it tells the customer and discusses alternatives.

That's fascinating.

The actual ageing clock isn't simply:

```text
year 12
→ old
```

It can be:

```text
manufacturer stops part
→ insurance/serviceability changes
→ replacement transaction
```

---

## 6. HomeServe makes that parts clock even harder

HomeServe's policy definition of **Beyond Repair** includes:

- parts unavailable within **28 days**
- parts no longer manufactured
- required parts retail cost exceeding **85% of new appliance retail cost**.

Source policy:
https://www.homeserve.co.uk/-/media/UK/Documents/TermsAndConditions/P/R6P_20250804_tac_v1.pdf

This creates:

## `PARTS_OBSOLESCENCE_TRIGGERS_CHANNEL_EXIT`

> A long-lived asset can become economically dead not because its hardware failed catastrophically, but because the support ecosystem can no longer furnish a particular component quickly/economically.

This potentially generalizes extraordinarily well to:
- elevators
- automatic gates
- ventilation controls
- industrial boards
- pumps
- older appliances
- medical equipment.

---

## 7. HomeServe has hard transaction-right closure

The current policy says:

- work by people **not authorized by HomeServe is not covered**
- HomeServe books one of **its engineers**
- excess is paid before engineer dispatch.

For a covered replacement:
- under 7 years: installation included
- **7 years or older: customer pays installation**
- current example installation starts around **£1,239**
- replacement **must be by a HomeServe-appointed installer**
- no cash alternative
- upgrades/corrections to bad prior installation are customer-funded.

Source:
https://www.homeserve.co.uk/-/media/UK/Documents/TermsAndConditions/P/R6P_20250804_tac_v1.pdf

This is near-perfect independent replication of the US AHS/Choice architecture.

---

## 8. HomeServe's current retail coverage

Current advertised first-year offers include:

- boiler cover, £100 excess: **£6.99/month**
- boiler cover, £60 excess: **£9.99/month**
- boiler + central heating, £60 excess: **£11.99/month**.

It advertises a nationwide Gas Safe network and unlimited claims.

Source:
https://www.homeserve.co.uk/insurance-cover/gas-and-boiler-comparison

Again: not a contractor directory.

A managed repair network.

---

## 9. The coverage boundary has real monetary consequence

HomeServe/BCIS's current 2026 cost guide gives:

- boiler service: **£182**
- seized pump: **£471**
- PCB replacement: **£442**
- boiler replacement supply/install: **£3,847**.

Source:
https://www.homeserve.co.uk/knowledge-hub/home-maintenance-advice/how-much-to-save-for-home-repairs/

British Gas says its average one-off chargeable boiler repair was **£235**, based on Jun–Oct 2024 completed jobs.

Source:
https://www.britishgas.co.uk/home-services/boilers-and-heating/boiler-and-heating-repair.html

So normal repair may be cheap relative to replacement.

The transaction changes abruptly when:

- critical part disappears
- boiler crosses serviceability threshold
- repair is uneconomic
- free replacement entitlement disappears.

That's the GoldProbe cell.

---

## 10. The customer-funded boundary is not fully open either

A crucial complication:

HomeServe currently works with **BOXT** for new boiler replacement and advertises **£200 off** for HomeServe customers.

Source:
https://www.homeserve.co.uk/heating/

British Gas is itself a major boiler installer.

So:

```text
cover ends
→ customer now needs replacement
```

doesn't guarantee:

```text
customer enters Google/open market
```

The payer already owns the failure relationship and can route replacement to itself/a partner.

### `PAYER_OWNS_FAILURE_TO_REPLACEMENT_FUNNEL`

This could be one of the strongest reasons many apparently perfect aftermarket lead-gen ideas underperform.

---

## 11. B15 strongly promotes the B14 mechanism

### `PAYER_DISPATCH_RIGHTS_CLOSE_MARKET`
**REPLICATED STRONGLY**

US:
- AHS/2-10/Choice
- payer authorization
- payer assigns provider
- closed funded transaction.

UK:
- HomeServe unauthorized work excluded
- HomeServe engineer dispatched
- appointed replacement installer
- British Gas own 7,000+ engineer force.

This now deserves permanent GoldProbe pattern status.

Refined statement:

> **A third-party payer/service plan can contractually close an otherwise highly fragmented trade market by controlling authorization, dispatch and replacement provider.**

This is stronger and more precise than `CHANNEL_OPENNESS`.

---

## 12. `COVERAGE_BOUNDARY_CREATES_OPEN_MARKET_SPILLOVER`

Also independently supported.

US HVAC:
- cap/exclusion/denial/outside authorization.

UK boiler:
- old boiler replacement right ends
- 7+ replacement installation becomes customer-funded
- obsolete parts can terminate coverability.

However:

> **spillover can be immediately recaptured by the payer's own replacement funnel.**

So the downstream model needs:

### `spillover_recapture`

not merely `coverage boundary`.

---

## 13. The exact UK opportunity

Not:

> Find a boiler engineer.

Not for covered customers.

Potentially:

### Legacy Boiler Coverage / Replacement Passport

Input:
- model + GC number/photo
- estimated install date
- insurer/cover provider
- plan
- part/fault
- repair history.

Return:
1. boiler age evidence
2. part availability
3. insurer supportability
4. free-replacement entitlement
5. customer-paid installation exposure
6. excluded remedial/sludge/upgrade items
7. current repair-vs-replace economics
8. provider's own replacement funnel
9. independent options once customer genuinely has transaction freedom.

It is much narrower and much more defensible.

---

## 14. B15 falsification review

### Strongly supported
- provider dispatch closes covered repair;
- age can change replacement entitlement independently of repair entitlement;
- parts obsolescence creates channel exit;
- provider can recapture the replacement transaction.

### Falsified
- huge Gas Safe supply automatically creates lead-gen opportunity.
- old boiler necessarily loses all repair cover.
- the customer necessarily becomes open-market once repair cover ends.

### Missing
- actual volume of boilers rejected due obsolete parts;
- annual beyond-repair volume;
- customer conversion from cover failure → provider replacement;
- brand/model-specific spare-part survival curves.

Those missing numbers are now particularly interesting.

---

## 15. Autonomous B16 — Germany legacy elevators

B15's highest-information new mechanism is:

### `PARTS_OBSOLESCENCE_TRIGGERS_CHANNEL_EXIT`

The cleanest stress test is a much longer-lived embedded asset.

**Germany elevators/lifts**:

- decades-long physical life
- proprietary controllers/drives/door systems
- mandatory safety inspections
- maintenance contracts
- expensive downtime
- modernization
- OEM and independent service channels
- exact legacy-part compatibility.

Hypothesis:

> **For very long-lived installed assets, control/parts obsolescence may trigger modernization earlier than structural asset death; intermediary value exists only if OEM service lock-in is incomplete and identifying viable legacy components/successor modules remains difficult.**

That takes the orchard into a substantially different industrial/service domain rather than repeatedly finding another boiler analogue.
