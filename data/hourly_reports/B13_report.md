# GoldProbe B13 — US Hail/Storm Insurance-Funded Roofing

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Does massive event-funded demand still create middleman whitespace once a market becomes mature?

## Executive result

**Mostly no. This is an excellent negative control.**

The money is enormous:
- State Farm alone paid **>$5.6B in hail claims in 2025**
- Texas alone accounted for **$1.4B**
- >50,000 State Farm claims followed March 2026 Midwest storms
- Verisk's Xactimate subset contains **$23B of 2025 roof replacement-cost estimates**

But the market is not supply-starved.

US Census counted **25,519 employer roofing establishments in 2023**:
- **16,661 (65.3%)** had fewer than five employees
- **20,487 (80.3%)** had fewer than ten.

The industry is simultaneously extremely fragmented at the bottom and heavily professionalized at the top.

## Hard event data

Insurance Information Institute, citing NOAA/NWS, reports **5,432 hail events of at least 1 inch in 2025**, including Texas 902, Kansas 375, Oklahoma 369 and Nebraska 315.

State Farm separately paid >$5.6B in hail claims, showing the insurer transaction scale.

## Claims economics

Verisk's 2025 roof report, limited to its Xactimate dataset, reports:
- **$23B** total roof RCV estimates
- **$17,631** average replacement estimate
- **$4,699** average repair estimate
- nearly **20%** of roofing claim assignments with non-recoverable depreciation.

Average repair estimate / replacement estimate = **26.7%**.

These are estimates, not final claim payments.

## Coverage architecture can dominate physical damage

Texas DOI gives a clean illustrative example.

Same $10,000 roof replacement, $4,000 deductible:
- RCV policy pays **$6,000**
- 5-year ACV roof example pays **$4,500**
- 10-year ACV roof pays **$3,000**
- 20-year ACV roof pays **$0**

The physical job did not change. The policy did.

That produces `COVERAGE_ARCHITECTURE_CHANGES_TRANSACTION_VALUE`.

## Trust becomes scarce after storms

NICB says contractor-fraud reports increased **38% from 2023 to 2025** and explicitly warns about storm-chasing contractors, manufactured roof damage, AOB abuse, upfront-payment theft, inferior work and falsified documentation.

This gives us `EVENT_SUPPLY_SURGE_CREATES_TRUST_SCARCITY`.

UK PFR after flood:
> too little qualified supply.

US hail roofing:
> a flood of contractor supply, including low-trust transient supply.

So event demand has at least two distinct supply regimes.

## Role legality is part of the market

Texas prohibits a roofer who performs the work from acting as the public adjuster, and prohibits deductible waivers/rebates. Colorado has similar restrictions.

This makes a generic "we negotiate your insurance then send our roofer" product dangerous.

A neutral tool can document, explain and compare; claim representation can require licensing and state-specific treatment.

## Claims workflow is already industrialized

Verisk agreed to acquire AccuLynx for **$2.35B**. AccuLynx is residential roofing contractor SaaS; Verisk already owns core property-estimating/claims workflow.

That is a hard signal that the insurer ↔ contractor workflow network is mature and strategically valuable.

The likely wedge is therefore not another marketplace.

## What remains interesting

### RoofClaim Passport / Storm Second Opinion
Potentially:
1. storm/date evidence
2. roof age/material
3. policy ACV/RCV/deductible explanation
4. damage photo evidence
5. repair-vs-replace scope comparison
6. contractor identity/local tenure/licensing/insurance verification
7. line-item differences across estimates
8. impact-resistant/FORTIFIED rebuild options
9. insurer-ready evidence record

Without crossing into regulated public-adjusting work.

## Resilience is already institutionalizing

IBHS tested 24 impact-resistant shingle products in 2025, covering roughly 95% of annual IR shingle sales.

FORTIFIED ended 2025 with >2,000 providers and surpassed 100,000 total designations in May 2026.

Texas maintains insurance credits for qualifying impact-resistant roofs.

So post-claim rebuilding can also contain a risk-payer-funded resilience-upgrade cell—but this is already an emerging standards ecosystem, not greenfield product discovery.

## What B13 falsified

- fragmented contractors ≠ marketplace whitespace
- billions of insurer spend ≠ cheap customer acquisition
- event-gated demand ≠ supply shortage
- generic hail-roof leadgen ≠ attractive just because intent is huge

## What B13 supported

- claim gatekeeper remains powerful
- trust can become scarcer than raw contractor capacity
- policy architecture changes funded job value
- mature claims-network infrastructure compresses neutral routing value
- resilience verification can still carry value

## Next autonomous probe — B14 US home-warranty HVAC

B14 removes catastrophe dynamics while keeping:
- expensive installed asset
- third-party payer
- repair/replacement event
- coverage rules
- assigned contractors
- network software/process.

Hypothesis:

> **If a payer owns contractor assignment and covered repair economics, fragmented physical service supply becomes irrelevant to a neutral marketplace.**

That will tell us whether `MATURE_CLAIM_NETWORK_COMPRESSES_NEUTRAL_ROUTING` is a general transaction-rights mechanism rather than a storm-roofing artifact.
