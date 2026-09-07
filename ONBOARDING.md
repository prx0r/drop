# ONBOARDING.md — Fresh Agent Guide

*Start here. This is everything you need to know to work in this repo.*

---

## 1. What Is This Project?

**Drop** is an autonomous geographic commerce allocator. It discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.

**The three businesses:**
1. **Agent-Native Commerce** — Specialist products, compatibility-heavy ecommerce
2. **Agent-Native Services** — EV, heat pumps, solar, HVAC
3. **Agent-Native Supplier OS** — AI receptionist, CRM, booking

All three share the same data infrastructure.

---

## 2. The Architecture

```
schemas/     → Canonical Pydantic models (one source of truth)
pipelines/   → Pure transform functions (no I/O)
storage/     → BigQuery + local JSON (I/O layer)
prompts/     → Agent instructions (MD files)
tests/       → Test suite
dashboard/   → Next.js visualization
```

**Key principle:** Pipelines are pure functions. `Input → Transform → Output`. No I/O in transforms.

---

## 3. Quick Start

```bash
# 1. Check what exists
cat active/BLOCKERS.md
cat active/CANDIDATES.md
cat active/SCRATCHPAD.md

# 2. Run tests
cd /root/drop && python3 -m pytest tests/ -q

# 3. Check BigQuery
python3 -c "from google.cloud import bigquery; print('BigQuery OK')"

# 4. Check MCP
python3 -c "from mcp_server_bigquery.server import main; print('MCP OK')"
```

---

## 4. Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | 10 binding rules |
| `HANDOVER.md` | Operational bible |
| `SPEC.md` | Architecture decisions |
| `schemas/observation.py` | Atomic fact |
| `schemas/hypothesis.py` | Testable claim |
| `schemas/kernel.py` | Market intelligence |
| `schemas/candidate.py` | Product × Country |
| `pipelines/gmail_import.py` | Email → Observations |
| `pipelines/state_machine.py` | Observations → State |
| `pipelines/hypothesis_ledger.py` | Observations → Hypotheses |
| `pipelines/evi_planner.py` | Unknowns → Research |
| `pipelines/kernel_generator.py` | Observations → Kernels |
| `storage/bigquery.py` | BigQuery I/O |
| `tests/test_e2e.py` | End-to-end tests |

---

## 5. BigQuery

```
53 tables
1,974 rows
80 graph nodes
239 graph edges
42 observations
```

Query via MCP or direct:
```python
from google.cloud import bigquery
client = bigquery.Client()
result = client.query("SELECT COUNT(*) FROM drop.country_data").result()
```

---

## 6. The Three Businesses

| Business | What | Moat |
|----------|------|------|
| Commerce | Products + compatibility | Decision engine |
| Services | Contractors + AI receptionist | Live supply data |
| Supplier OS | CRM + invoicing + parts | Contractor lock-in |

**The flywheel:** provider usage → better data → more bookings → more provider demand → more usage

---

## 7. What NOT To Do

- Don't use old code from `legacy/`
- Don't import from `services/` (old, broken)
- Don't assume margins — use real data
- Don't claim "tests pass" without showing output
- Don't bypass the redteam protocol

---

## 8. Where to Find Things

```bash
# Find a concept
grep -rn "concept" schemas/ pipelines/ storage/

# Find a file
find . -name "*.py" | grep concept

# Check BigQuery
python3 -c "from google.cloud import bigquery; print('OK')"

# Run tests
python3 -m pytest tests/ -q
```

---

*Last updated: 2026-09-08*
