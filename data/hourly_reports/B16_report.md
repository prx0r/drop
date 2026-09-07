# GoldProbe B16 — Germany Legacy Elevator Parts / Service / Modernization

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**Parts obsolescence is real, but the naive middleman opportunity is largely absorbed by Germany's mature support ecosystem.**

Current German housing-industry reporting puts the stock at roughly **800,000 elevators with an average age around 35 years**.

Source: https://www.haufe.de/immobilien/zeitschrift/wohnungswirtschaft/die-wohnungswirtschaft-ausgabe-92026-wohnungswirtschaft/aufzugsanlagen-wie-smarte-wartung-ausfaelle-verhindert-696340.html

The harder regulatory dataset is even more valuable: **723,270 lifts underwent recurring statutory inspection in 2025**. Outcomes:

- **10.8% significant defects**
- **0.8% dangerous defects**
- **64.7% minor defects**
- **23.7% defect-free**
- about **3,000 immediate shutdowns**.

Source: https://www.tuv.com/presse/de/meldungen/anlagensicherheitsreport2025-aufzuege.html

Derived only as context, 10.8% of 723,270 is about **78,113 significant-defect inspection outcomes**. This is not a unique-customer count.

## The inspection clock is unusually clean

German BetrSichV requires a main inspection no later than every two years and an intermediate inspection halfway between main inspections, by an approved inspection body.

Source: https://www.gesetze-im-internet.de/betrsichv_2015/anhang_2.html

That creates an effectively annual independent compliance event:

`inspection -> report -> remediation -> reinspection`.

A significant defect requires remediation/reinspection; a dangerous defect can force immediate shutdown.

## The remediation channel remains open

BAuA states that the operator is responsible for maintenance and must use competent personnel or a suitable qualified contractor. It does **not** require the original manufacturer.

Source: https://www.baua.de/DE/Themen/Arbeitsgestaltung/Maschinen-und-Betriebssicherheit/Anlagen-und-Betriebssicherheit/FAQ/04FAQ.html

This is important:

**diagnosis is regulated and independent; remediation is a qualified private market chosen by the owner.**

## The report literally becomes a purchasing object

FB-Aufzüge explicitly tells customers without an existing service contract to send the TÜV/DEKRA inspection report and lift description so it can quote the repair.

Source: https://fbaufzuege.de/service/uebersicht-servicevertraege.php

Aufzugsmanagement Gottwald sells a service obtaining up to **three comparison offers** for repairs and TÜV defect remediation.

Source: https://www.aufzug-beratung.de/preise/

That strongly supports:

### `REGULATORY_REPORT_BECOMES_PURCHASE_SPEC`

An independent compliance report can standardize the problem enough that private suppliers quote against it.

## Obsolescence is unquestionably a real clock

Schindler's current modernization ladder:
- ReStore: **15+ years / >2m trips** — controller, frequency converter, fixtures
- ReNew: **25+ years / >3.5m trips**
- RePlace: **30+ years**.

Sources:
https://www.schindler.de/de/aufzuege/modernisierung/restore.html
https://www.schindler.de/de/elevators/modernization/renew.html
https://www.schindler.de/de/aufzuege/modernisierung/replace.html

KONE independently says around **20 years** is a typical tipping point for controllers, power electronics and door systems: breakdown risk and repair cost rise while parts become hard or unavailable.

Source: https://www.kone.de/bestandsgebaeude/aufzuege-modernisieren/modernisieren-auf-stand-der-technik.aspx

So B15's parts-support clock is not a boiler-specific effect.

## But OEM discontinuation does not equal asset death

This is B16's strongest falsification.

TK Elevator says **more than 50% of its maintenance portfolio is equipment from other manufacturers**. Its ITS network repairs/refurbishes rare electronics such as control boards and drives across major brands.

Source: https://www.tkelevator.com/de-de/service/

Hauer currently advertises **>15,000 parts from >50 manufacturers**.

Source: https://hauer-ersatzteile.de/

DAS Aufzüge says it can repair controllers/inverters/electronics and, when some components are no longer available, can sometimes design/manufacture replacements.

Source: https://das-aufzuege.de/service/reparaturen-und-ersatzteile-fuer-aufzuege/

Therefore:

### `SUPPORT_ECOSYSTEM_DELAYS_OBSOLESCENCE`

OEM EOL is only a modernization trigger if the independent support graph cannot bridge it economically.

## Generic parts finding is already mature

The market already has:
- all-brand parts specialists
- photo/nameplate identification
- rare/obsolete part sourcing
- board/drive refurbishment
- custom replacement possibilities.

So a generic "upload a photo and find an elevator part" product is **HOLD**.

## Routine service is open and competitive

Marklem currently advertises one example:
- 4 stops / 3 visits: **€569/year**
- emergency-call device rental: **€499/year**
- fault travel: **€35**
- labour: **€86/hour**, net.

Source: https://marklem-aufzuege.de/kostenvergleich

Bauleo's 2026 commercial cost reference gives broader context:
- basic maintenance avg **€1,265/year**, range €805–€1,955
- controller modernization avg **€10,925**, range €7,475–€15,525
- partial modernization avg **€36,800**, range €25,300–€51,750.

Source: https://www.bauleo.ai/baupreise/aufzugstechnik

Scopes differ, so these are not a matched market-price survey.

But the order-of-magnitude jump matters: €36,800 is about **29.1 years** of the reference basic-maintenance price.

The expensive decision is modernization, not shaving €100 from annual maintenance.

## Owner-side procurement is already an industry

HUNDT CONSULT says it currently manages:
- **65,000 assets**
- **10,000 analyses/reports per year**
- **2,500 modernizations per year**
- 150 specialists.

Source: https://www.hundt-consult.de/

UPDOWN offers contract management, quote comparison, invoice review, ZÜS/deadline tracking and dashboards.

Source: https://liftmanagement.updown-ingenieure.de/

That produces another candidate:

### `OWNER_SIDE_PROCUREMENT_LAYER_EMERGES`

When an asset is expensive, regulated, technically opaque and contract-heavy, a specialist buyer/manager appears on the owner's side.

This is commercially validating but whitespace-negative.

## Best narrow opportunity

### Legacy Elevator Supportability Passport — small portfolios only

Input:
- ZÜS report
- manufacturer/model/year
- controller/drive photos
- service contract
- last 24 months of invoices/faults
- modernization quote.

Output:
1. defect-to-remediation map
2. controller/drive generation
3. OEM part availability
4. refurbished/independent alternatives
5. custom-part possibility
6. repair vs module modernization vs full modernization
7. normalized scope
8. benchmarked maintenance/repair quote
9. qualified bidders
10. reinspection evidence pack.

The potential wedge is property managers/WEGs too small for full human lift-management consulting. That segment remains unvalidated.

## What B16 proved

- Germany's lift ecosystem is old enough for parts support to matter.
- electrical/control obsolescence can precede structural asset death.
- parts availability is a modernization trigger.
- owners retain meaningful provider choice.
- statutory inspection produces mandatory remediation.
- standardized report-to-private-quote workflows are real.

## What B16 falsified

- discontinued OEM part automatically forces modernization.
- rare parts are necessarily unavailable to independents.
- quote comparison is undeveloped.
- fragmented service implies greenfield marketplace whitespace.

## Orchard update

`PARTS_OBSOLESCENCE_TRIGGERS_CHANNEL_EXIT` becomes:

> parts obsolescence creates **channel-exit pressure**, but `SUPPORT_ECOSYSTEM_DEPTH` determines whether that pressure actually converts into modernization.

`PUBLIC_DIAGNOSIS_PRIVATE_REMEDIATION_HANDOFF` is now **strongly replicated**:
- Ireland septic inspection
- Germany elevator ZÜS inspection.

## Autonomous next probe — B17 UK fire-door inspection/remediation

This is selected to test `REGULATORY_REPORT_BECOMES_PURCHASE_SPEC` in a different safety asset.

Hypothesis:

> recurring legally required fire-door inspections can create a high-intent report-to-remediation market if building owners retain supplier choice and inspection/remediation have not already been vertically integrated.
