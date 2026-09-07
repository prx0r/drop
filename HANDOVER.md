# Handover — 2026-09-07

*For next agent: What was built, what works, what's next*

---

## What Was Built This Session

### 1. Intelligence System
- GitGoblin: 41 seeds, 7,271 observations, 1,666 entities
- GoldProbe: 33 reports imported
- Market research: Web search for Shopify, Merchant Center, agentic commerce
- 170 niches analyzed, 25 campaigns created

### 2. Campaign System
- 25 active campaigns in `campaigns/active/`
- Each with: competitor analysis, gap assessment, product catalog, pricing, ad strategy
- Validation rubric (binary gate + 20-score)
- CG worldpack for automated evaluation

### 3. Infrastructure
- Shopify setup guide created
- Merchant Center feed strategy defined
- Agentic Storefronts documentation imported
- Voiceagent cloned and analyzed

---

## What Actually Works

### voiceagent (the runtime)

```bash
cd /root/voiceagent
cp .env.example .env
pip install -r requirements.txt
./scripts/run.sh
# open http://localhost:8080
```

**Already has:**
- Graph-grounded chat (lexical matching + neighbor expansion)
- Business YAML configuration
- Voice adapter (edge TTS)
- API endpoints (/chat, /graph/search, /health)
- Norwegian language handling
- Product nodes with compatibility info
- Policy nodes, service nodes, FAQ nodes
- Escalation rules
- Tool registry
- Session management

**Config files:**
- `knowledge/balcony_door_hardware_no.yaml` — Norwegian balcony door (20 nodes, 15 edges)
- `knowledge/hottub_controls_en.yaml` — Hot tub controls
- `knowledge/generic_service_business.yaml` — Template

### CG Worldpack

```python
import cogym_kernel.worlds.drop_campaign_gate
from cogym_kernel.worlds.registry import create

world = create('drop.campaign_gate')
state = world.reset(instance_id='TEST', seed=42)
# ... evaluate campaign
```

**Works:** Evaluates 12 gates, scores 20 rubric items, determines verdict.

---

## What's Next (Priority Order)

### Immediate (this week)
1. **Demote 25 ACTIVE campaigns** to truthful states (candidates/blocked/benchmark)
2. **Restore Allaway + AKVA** into canonical campaign registry
3. **Define subgraph.schema.v1** — typed entities and edges
4. **Turn balcony-door YAML** into first evidence-backed real subgraph

### Short-term (next 2 weeks)
5. **Modify voiceagent** to load compiled Drop graphs
6. **Build Shopify compiler** — graph → products/metafields/supplemental feed
7. **Stand up Shopify test store** — Norwegian balcony-door hardware
8. **Enable Shopify Catalog + Google & YouTube**
9. **Add Merchant Center supplemental data** — compatibility attributes

### Medium-term (next month)
10. **Test live /api/ucp/mcp** against 50 compatibility questions
11. **Build 3 subgraphs in parallel:**
    - NO balcony/window hardware
    - Nordic recliner controls
    - Nordic hot-tub panels
12. **Launch Google Ads test** — exact/phrase, Norwegian, £10/day

---

## Architecture

```
               DROP GRAPH
                   │
        ┌──────────┼────────────┐
        ↓          ↓            ↓
      HUMAN      GOOGLE       SHOPIFY
      PDP        AI MODE      CATALOG/UCP
        │          │            │
        └──────────┼────────────┘
                   ↓
              CUSTOMER AGENT
                   ↑
                   │
             VOICEAGENT
```

**The product is:** one verified compatibility graph that compiles losslessly into every human and agent commerce surface.

---

## Key Files

### Drop repo
- `campaigns/active/` — 25 campaigns (need reclassification)
- `THESIS.md` — Core thesis
- `HCC_V2.md` — 20 campaigns with corrected scoring
- `SHOPIFY_SETUP_GUIDE.md` — Shopify setup instructions

### Voiceagent repo
- `knowledge/balcony_door_hardware_no.yaml` — Norwegian config
- `app/graph.py` — Graph implementation
- `app/main.py` — FastAPI server
- `app/flow.py` — Conversation flow

### CG repo
- `cogym_kernel/worlds/drop_campaign_gate.py` — Campaign evaluation worldpack

---

## Commands

```bash
# Voiceagent
cd /root/voiceagent && ./scripts/run.sh

# CG evaluation
cd /root/cg && python3 -c "from cogym_kernel.worlds.registry import create; w=create('drop.campaign_gate'); print(w.worldpack_id)"

# Drop campaigns
ls /root/drop/campaigns/active/

# GitGoblin
cd /root/gitgoblin && gitgoblin scan agent_commerce --expand 1 --no-research
```

---

## Critical Insight

**voiceagent is the runtime, not a separate project.**

Voice is one channel. Web chat is another. Product finder is another. Shopify PDP is another. Google is another. ChatGPT/Shopify Catalog is another.

Evolve voiceagent into **Drop Resolver Runtime**.

Don't build another commerce-agent repo.
