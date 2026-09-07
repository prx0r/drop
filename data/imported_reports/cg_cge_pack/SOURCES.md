# Source / Repo Notes

## Repositories reviewed

### CG
https://github.com/prx0r/cg

Key observed design:
- deterministic agentic evolution laboratory;
- content-addressed RunReceipt;
- hard quality gates;
- Wilson/bootstrap stats;
- lexicographic selection;
- sealed evaluation;
- worldpack distribution.

Relevant files:
- README.md
- SPEC.md
- docs/GUIDE.md
- cogym_kernel/eval/gates.py
- cogym_kernel/worlds/toy.py
- worldpacks/README.md

### CGE
https://github.com/prx0r/cge

Key differences:
- space-expansion charter;
- scoring feedback;
- peer-reviewed evolution;
- adversarial benchmark generation;
- mutation guidance;
- MAP-Elites/diversity mechanisms.

Relevant files:
- SPEC.md ADR-11
- cogym_kernel/eval/scoring_feedback.py
- cogym_kernel/evo/peer_reviewed_loop.py
- cogym_kernel/evo/loop.py

Both repos currently declare the same Python project/package name:
`cogym-kernel` / `cogym_kernel`.

### Drop
https://github.com/prx0r/drop

Relevant recent architecture commits:
- 364ec66 — canonical campaign format
- 020e937 — red-team audit
- 4b45ab5 — campaign validation rubric
- 4c43f02 — maritime/B2B schema gaps
- 20ee796 — campaign mutation architecture

Critical issue in the draft mutation architecture:
it contains an example where BigQuery mining yields a proposed mutation with
`suggested_value = "verified"` and score impact. The new architecture deliberately removes this mechanism.

## BigQuery

Official documentation:
- Table snapshots:
  https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro
- Create snapshots:
  https://docs.cloud.google.com/bigquery/docs/table-snapshots-create
- Historical queries / FOR SYSTEM_TIME AS OF:
  https://docs.cloud.google.com/bigquery/docs/access-historical-data

Current docs state BigQuery table snapshots preserve table contents at a point in time and can preserve state beyond the normal time-travel window.

## Evolution design inspiration

Google DeepMind AlphaEvolve:
https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

The relevant pattern is:
LLM/proposer creativity + automated objective evaluator + evolutionary archive.

For Drop, the evaluator must be stricter because market evidence is external and partially unknown:
- proposer does not define truth;
- hard constraints precede optimization;
- evidence acquisition is a separate action problem.

Constrained Bayesian optimization / unknown-constraint active learning:
https://arxiv.org/abs/2310.08751

Used only as conceptual inspiration for separating:
- feasible-region discovery;
- objective optimization;
- information acquisition.
