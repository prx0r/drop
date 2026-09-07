# Handover Protocol

*Hard structured data. Questions, prompts, checklists. Not prose — protocol.*
*Every section is a checkpoint. Complete it before acting.*

---

## Section 1: Orientation Checklist

Before doing anything, verify:

- [ ] Read `active/BLOCKERS.md` — what's stopping progress
- [ ] Read `active/CANDIDATES.md` — what's in the pipeline
- [ ] Read `active/SCRATCHPAD.md` — what was last done
- [ ] Read `probes/FRESHNESS_TRACKER.md` — which probes are still valuable
- [ ] Read `HANDOVER.md` — complete context dump
- [ ] Read `critique.md` — what's broken and how to fix it
- [ ] Read `output/WINNING_FORMULA.md` — the 7 laws
- [ ] Read `output/CANONICAL_STRATEGY.md` — the playbook

---

## Section 2: Data Protocol

### Sources of Truth

| Data Type | Location | Format | Update Frequency |
|-----------|----------|--------|------------------|
| Graph (nodes, edges) | BigQuery `drop.graph_nodes`, `drop.graph_edges` | SQL | On observation |
| Observations | BigQuery `drop.observations` | SQL | On observation |
| Outcomes | BigQuery `drop.outcomes` | SQL | On outcome |
| Hypotheses | BigQuery `drop.hypotheses` | SQL | On update |
| Probes | BigQuery `drop.probes_v2` | SQL | After each run |
| Products | BigQuery `drop.products` | SQL | On update |
| Merchants | BigQuery `drop.merchants` | SQL | On update |

### What Lives Where

| Type | Location | Format |
|------|----------|--------|
| Schemas | `schemas/` | JSON |
| Code | `services/` | Python |
| Intelligence | `output/` | Markdown + JSON |
| Configuration | `data/` | JSON + CSV |
| Country packs | `countries/` | JSON |
| Stale files | `*/stale/` | Original format |

### Rules

1. **BigQuery is source of truth** for queryable data
2. **Repo stores schemas, code, intelligence, config**
3. **Never invent data** — unknown = null
4. **Every observation has provenance** — source, confidence, measurement_type
5. **Scores are null unless formulaic** — no naked numbers

---

## Section 3: Action Protocol

### Before Every Action

```bash
cat active/BLOCKERS.md
cat active/CANDIDATES.md
cat active/SCRATCHPAD.md
```

### After Every Action

```bash
echo "$(date -Iseconds): [action]" >> active/SCRATCHPAD.md
echo "$(date -Iseconds): [decision] — [reasoning]" >> active/DECISIONS.md
echo "$(date -Iseconds): [problem]" >> active/PROBLEMS.md  # if any
```

### Email Protocol

1. Check Gmail for probe reports and supplier responses
2. Log every email in `active/EMAIL_LOG.md`
3. Follow up after 48h if no response
4. Templates in `/emails/templates/`

### Data Protocol

- BigQuery = truth for queryable data
- Repo = schemas + code + intelligence + config
- Never invent data
- Every observation: source + confidence + measurement_type

### Probe Protocol

1. Check `probes/FRESHNESS_TRACKER.md`
2. If novelty < 0.30, swap with next from queue
3. Log every probe run with timestamp
4. Update graph nodes with new observations

---

## Section 4: Decision Framework

### When to LAUNCH

- [ ] Supplier approved
- [ ] Product feed ready
- [ ] Store built
- [ ] Free listings activated
- [ ] 14-day observation complete
- [ ] >100 impressions
- [ ] >10 clicks
- [ ] Break-even CVR < realistic

### When to KILL

- [ ] 100 clicks, 0 orders
- [ ] Break-even CVR > 3%
- [ ] Headroom < 1.0
- [ ] Supplier rejects
- [ ] >7 day delivery
- [ ] GTIN sellers > 20

### When to SCALE

- [ ] Positive contribution profit for 14 days
- [ ] P(profitable) > 0.7
- [ ] Supplier capacity confirmed
- [ ] Operations stable

---

## Section 5: Economic Model

### CM0-CM3

| Level | Formula |
|-------|---------|
| CM0 | revenue - COGS - shipping - duties - payments - refunds - returns |
| CM1 | CM0 - ad_spend |
| CM2 | CM1 - ai_tokens - scraping - image_generation - agent_compute |
| CM3 | CM2 - domains - human - samples - setup |

**Primary optimization target: CM2**

### Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Contribution per click | (CVR × margin) - CPC | > 0 |
| Headroom | (CVR × margin) / CPC | > 1.5 |
| Break-even CVR | CPC / margin | < 1% |
| Good Seller Gap | demand × (1 / (1 + good_sellers)) | > 50 |

---

## Section 6: Quick Commands

```bash
# Score candidates
python3 services/research/scoring_pipeline.py --report

# Generate hypotheses
python3 services/research/hypothesis_generator.py

# Design probes
python3 services/research/probe_designer.py

# Check BigQuery
python3 -c "
from google.cloud import bigquery
client = bigquery.Client()
for t in ['graph_nodes', 'graph_edges', 'probes_v2', 'outcomes']:
    q = f'SELECT COUNT(*) as cnt FROM `{client.project}.drop.{t}`'
    r = client.query(q).result()
    print(f'{t}: {list(r)[0][\"cnt\"]} rows')
"

# Check email
python3 -c "
import subprocess
result = subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GMAIL_ADDRESS', '--vault', 'oracle'], capture_output=True, text=True)
print(result.stdout)
"
```

---

## Section 7: Stale File Rules

### When to Move to Stale

- Data superseded by newer analysis
- Candidates killed or outdated
- Strategy replaced by better approach
- Format replaced by better schema
- Information absorbed into BigQuery

### How to Move

```bash
mkdir -p output/stale
mv output/OLD_FILE.md output/stale/
echo "Moved to stale because: [reason]" >> output/stale/README.md
```

### Never Delete

Stale files are historical evidence of what we tried and what we learned.

---

## Section 8: The Reward Function

```python
def reward(outcome):
    profit = outcome["revenue"] - outcome["ad_spend"] - outcome["cogs"]
    information = calculate_information_gain(outcome)
    return profit + information * 0.1
```

**Primary reward = realized economic contribution (CM2).**
Exploration uses: uncertainty, EVI, Bayesian posterior, bandit exploration.
Keep these separate.
