# Trust Boundaries & Anti-Goodhart Contract

## Actors

| Actor | May propose campaign? | May add raw evidence? | May verify evidence? | May calculate final gates? | May see secret suite? |
|---|---:|---:|---:|---:|---:|
| Drop generator agent | YES | NO | NO | NO | NO |
| CGE proposer | YES | NO | NO | NO | NO |
| Web/data collector | NO | YES | NO | NO | NO |
| Evidence verifier | NO | NO | YES | NO | NO |
| CG judge | NO | NO | consumes verified | YES | YES |
| Human | YES | YES | YES | policy-controlled | policy-controlled |

## Evidence immutability

An evidence row is append-only.

Corrections:
- create new row;
- link `supersedes_evidence_id`;
- never rewrite the old observation.

## Campaign immutability

A mutation creates:

```text
parent campaign version
       ↓ mutation receipt
child campaign version
```

Never update an old campaign version in place.

## Rubric immutability during an evolution run

A rubric may evolve globally through deliberate versioning.

It cannot change inside a campaign optimization lineage merely because candidates fail.

Any rubric change:
- new `rubric_version_id`;
- all historical campaigns can be replayed;
- leaderboard results never mix rubric versions without explicit migration.

## Secret suite

CGE should not see:
- hidden compatibility counterexamples;
- hidden incumbent benchmark prompts;
- hidden buyer-role edge cases.

Otherwise campaign text can overfit the known test set.

## No "verified" mutation operator

There is intentionally no mutation:
`SET_GATE_PASS`.

There is intentionally no mutation:
`SET_MARGIN`.

There is intentionally no mutation:
`SET_INSTALLED_BASE`.

Only evidence compiler can bind measured values to metrics.

## No LLM confidence as probability

Forbidden:
```json
{"supplier_access_probability": 0.83}
```
if 0.83 came from model judgment.

Permitted:
- empirical Beta posterior from prior supplier-contact outcomes;
- Wilson interval from sampled buyer-role observations;
- explicit source tier;
- unknown.

## Provenance quorum

For a hard factual gate:
- Tier A direct source can suffice;
- otherwise two independent Tier B sources;
- behavioral claims can use systematic Tier C samples;
- generative AI output is discovery only.

## Fail closed

When data is missing:
- do not use zero;
- do not use population mean;
- do not interpolate silently;
- do not let CGE pick a favorable default.

Return `UNKNOWN`.
