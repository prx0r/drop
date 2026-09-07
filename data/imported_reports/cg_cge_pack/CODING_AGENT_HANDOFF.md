# Coding Agent Handoff Prompt

Implement the Drop × CG × CGE campaign evolution system from this pack.

## Repositories

- `prx0r/drop` — domain/control plane.
- `prx0r/cg` — authoritative deterministic judge.
- `prx0r/cge` — untrusted proposer/space expansion.

## Non-negotiable architecture

1. Campaign facts are not mutable genes.
2. Evidence is append-only and provenance-backed.
3. CG is the only authoritative gate evaluator.
4. CGE cannot see secret cases.
5. CGE cannot mutate rubric/evidence/observed metric paths.
6. UNKNOWN fails closed for promotion.
7. Every campaign mutation creates a child version.
8. Every CG evaluation binds campaign version + evidence snapshot + rubric version.
9. BigQuery is evidence/analytics; Hydra is derived/rebuildable memory.
10. Do not install CG and CGE into one Python environment; they use the same package name.

## Build order

### PR 1 — drop schema + deterministic local validator
- Add `campaign.schema.v2.json`.
- Add `mutation.schema.v1.json`.
- Add `rubric.drop-hcc-v2.yaml`.
- Add mutation allow/deny path validation.
- Add unit tests.

### PR 2 — BigQuery migrations
Use `BIGQUERY_DDL.sql`.
No destructive migration of existing tables.

### PR 3 — evidence compiler
Compile a campaign to frozen bundle from verified evidence rows.
Content hash all inputs.

### PR 4 — CG worldpack
Add `drop.campaign_gate-v1`.
Use current CG `QualityGate`, Wilson and bootstrap code.
No network calls.

### PR 5 — CG secret suite
Add sealed validation/secret fixtures.
Proposer cannot read them.

### PR 6 — CGE adapter
Typed mutation operators only.
Output JSON Patch-style mutations.
Admission quarantine in Drop.

### PR 7 — evidence acquisition actions
Research action queue + result ingestion.
No automation should fake supplier contact completion.

### PR 8 — end-to-end test
Run:
- UFH blocked example;
- Allaway D2C example;
- AKVA B2B reroute example.

## Required CI properties

- determinism;
- forbidden mutation rejection;
- null/UNKNOWN semantics;
- evidence hash binding;
- cross-country evidence invalidation;
- secret-suite isolation;
- replay from receipt;
- BQ projection rebuild.

## Do not do

- Do not optimize a 0–200 subjective scalar.
- Do not let LLM assign confidence percentages.
- Do not automatically write `verified=true`.
- Do not make external web calls inside CG evaluation.
- Do not duplicate rubric logic inside CGE.
