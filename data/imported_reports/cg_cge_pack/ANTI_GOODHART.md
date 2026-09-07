# Anti-Goodhart Rules

## Rule 1 — score is downstream of evidence

CGE never sees a writable `score`.

CG computes metrics from evidence.

## Rule 2 — no mutable evidence in the genome

Campaign genome contains choices, not facts.

Bad gene:
`gross_margin = 0.35`

Good gene:
`supplier_candidate_set = ["SUP-ONNINEN"]`

Evidence compiler later discovers actual cost.

## Rule 3 — threshold changes are a new rubric

An optimizer cannot reduce:
`min_annual_events 1000 -> 100`

to rescue a niche.

## Rule 4 — unknown is a state, not a value

`UNKNOWN != 0 != FAIL`.

## Rule 5 — hidden suite

Keep some:
- buyer journeys;
- compatibility exclusions;
- incumbent prompts;
- stock freshness traps

proposer-blind.

## Rule 6 — incumbent benchmark cannot be selected by proposer

The judge resolves "best incumbent" from the evidence snapshot / benchmark registry.

CGE cannot choose a weak competitor.

## Rule 7 — atomicity cannot be widened to steal denominator

If:
`Allaway KP filters`

does not have enough demand, CGE cannot silently use:
`all Finnish home appliances`

as installed-base denominator.

The denominator entity must map to the exact atom through verified graph edges.

## Rule 8 — market transfer must reset local facts

Moving FI → NO invalidates:
- local stock;
- local price;
- buyer-role evidence;
- local incumbent benchmark;
- platform/localization evidence.

Only globally portable OEM compatibility facts may transfer.

## Rule 9 — failed campaigns are training data

Record exact kill reason.

CGE uses kill patterns to avoid rediscovering:
- installer-selected residential PCBs;
- excellent specialist incumbents;
- B2B-only product in D2C channel.

## Rule 10 — live outcomes dominate proxies

After 50+ real orders:
- actual wrong-part rate;
- actual returns;
- actual CVR;
- actual contribution;
- actual human intervention

replace proxy estimates wherever compatible.

## Rule 11 — no "rubric prose" in candidate generation prompt

The proposer may know gate names and public criteria.

It should not be given secret examples/answers.

## Rule 12 — research budgets are real costs

Store:
- token cost;
- API cost;
- scraper cost;
- human minutes;
- supplier outreach count;
- ad spend.

A "better" campaign that required £5,000 research to discover is not automatically better than one verified for £20.
