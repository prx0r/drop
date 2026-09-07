# Repo Audit — What to Reuse vs Change

## CG

### Reuse directly
- `QualityGate`
- `gates_pass`
- `lexicographic_compare`
- `wilson`
- `bootstrap_ci` / paired non-inferiority
- content-addressed candidate/run IDs
- sealed evaluation design
- worldpack mechanism

### Add
- Drop campaign worldpack.
- Track-aware campaign evaluator.
- launch eligibility claim projection.

### Do not add
- BigQuery credentials;
- web browser;
- mutable campaign research;
- CGE proposer logic.

## CGE

### Reuse
- `PeerReviewedEvolution`
- scoring feedback/guidance concept
- rejection-pattern adversarial generation
- adaptive mutation
- MAP-Elites/diversity
- space expansion doctrine

### Modify/adapt
Current peer loop assumes numerical candidate config genes and self/peer scoring.
Drop campaigns need:
- typed categorical graph-backed genes;
- JSON Patch-like mutation proposals;
- public CG feedback mapping;
- quarantine admission;
- research-action proposals.

### Important
Do not trust CGE's own `gates.py` copy as the production campaign authority.
Use the separately deployed CG judge.

## Drop

### Keep
- canonical campaign schema direction;
- hard-gate doctrine;
- kill ledger;
- country/BQ intelligence;
- mutation history concept;
- OEM successor graph;
- track split.

### Replace in current mutation draft
The current design allows a dangerous pattern:
`UNKNOWN → BigQuery lookup → suggested "verified" → +score`.

Replace with:
`UNKNOWN → research/query action → evidence observation → verification → evidence snapshot → CG replay`.

### Score
The old +10/0/-10 scalar may remain as a dashboard heuristic after eligibility,
but must not be launch authority.

## BigQuery

Treat it as:
- event-sourced evidence;
- typed graph;
- experiment ledger;
- live outcome store.

Not:
- a place where an LLM writes its desired campaign score.
