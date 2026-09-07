# Proposed Operator CLI

These are proposed wrapper commands; they do not claim to exist in the repos yet.

```bash
# 1. validate campaign JSON
drop-campaign validate campaigns/FI-UFH-LEGACY-CONTROLS-0001.json

# 2. compile current verified evidence
drop-campaign compile FI-UFH-LEGACY-CONTROLS-0001 \
  --as-of 2026-09-07T21:30:00+07:00 \
  --rubric drop-hcc-v2.0 \
  --out runs/ufh-v1/

# 3. submit frozen bundle to trusted CG judge service
drop-campaign judge runs/ufh-v1/bundle.json

# 4. if blocked, ask CGE for proposals
drop-campaign propose FI-UFH-LEGACY-CONTROLS-0001 \
  --cg-result runs/ufh-v1/result.public.json \
  --budget 20

# 5. inspect quarantine
drop-campaign mutations FI-UFH-LEGACY-CONTROLS-0001

# 6. approve an actual research action
drop-campaign action approve RA-...

# 7. ingest evidence collected from action
drop-campaign evidence ingest action-results/RA-....json
drop-campaign evidence verify EV-...

# 8. compile + replay automatically
drop-campaign cycle FI-UFH-LEGACY-CONTROLS-0001

# 9. only after CG claim
drop-campaign launch-manifest FI-... --cg-run RUN-...
```

## Batch over all campaigns

```bash
drop-campaign cycle-all --country FI --max-research-eur 50
```

Output:
- eligible;
- blocked by gate;
- rejected;
- rerouted;
- highest-EVI action.

## Discovery mode

```bash
drop-campaign discover --country NO --asset-class maritime \
  --population 100 --cge-budget 500
```

Flow:
1. typed genes from BigQuery graph;
2. CGE proposes atoms;
3. Drop compiles evidence;
4. CG filters;
5. CGE expands around survivors/kills;
6. no Gold Campaign until evidence gates pass.
