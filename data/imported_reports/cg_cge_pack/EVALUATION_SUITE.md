# Evaluation Suite Design

## 1. Route suite

Cases ask:
- who notices?
- who diagnoses?
- who selects SKU?
- who installs?
- who pays?

Hidden traps:
- public checkout exists but installer selects;
- consumer can install but warranty requires pro;
- professional buyer selects and self-installs onboard.

## 2. Compatibility suite

Minimum:
- exact positive fit;
- exact negative fit;
- supersession;
- adapter-required;
- serial threshold;
- visually similar but incompatible;
- same OEM wrong generation.

Target:
>=50 cases; promotion target lower 95% confidence bound >= configured threshold.

## 3. Incumbent suite

30–50 fixed prompts.

Measure:
- fully correct resolution;
- executable answer;
- negative compatibility;
- supersession;
- stock/price current;
- merchant route.

Secret subset prevents cherry-picking only questions incumbents answer badly.

## 4. Evidence-quality suite

Reject:
- unsourced market estimate;
- stale stock;
- retailer claim used as safety authority;
- model-generated percentage;
- source from wrong country/generation.

## 5. Market denominator suite

Check:
`installed_base observation subject`
maps to
`campaign atom`.

Reject denominator leakage.

## 6. Economics suite

Require:
- real supplier cost sample;
- shipping;
- fees;
- returns assumptions/source;
- real currency.

No guessed margin.

## 7. Platform/retrieval suite

Separate:
- eligibility;
- feed completeness;
- actual share-of-answer.

Never score "has Merchant Center fields" as "will rank first".

## 8. Adversarial case generation

CGE can generate public adversarial cases from observed failure patterns.

CG maintains a secret static + refreshed set.

## 9. Cross-time replay

When new evidence arrives:
- rerun previous champions against new snapshot;
- detect decay;
- specialist improvements can demote a campaign.

This turns campaign selection into a continuously falsifiable process.
