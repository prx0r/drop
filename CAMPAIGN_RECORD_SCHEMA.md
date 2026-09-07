# Campaign Record Schema + GitGoblin Mutation

*Generated: 2026-09-07*
*Status: ARCHITECTURE — How campaigns are validated, mutated, and tracked*

---

## The Principle

**Campaign JSON is immutable once created.** All changes go into a separate `campaign_records` table that tracks everything.

This gives us:
- Complete audit trail
- No lost history
- Mutation tracking
- GitGoblin integration
- Agent accountability

---

## Campaign Record Schema

```sql
CREATE TABLE drop.campaign_records (
  record_id STRING,
  campaign_id STRING,
  record_type STRING,  -- VALIDATION, SEARCH, MUTATION, NOTE, STATUS_CHANGE
  agent_id STRING,
  timestamp TIMESTAMP,
  content JSON,
  evidence JSON,
  score_before INTEGER,
  score_after INTEGER,
  status_before STRING,
  status_after STRING
)
```

---

## Record Types

### 1. VALIDATION

When we assess a campaign against the rubric.

```json
{
  "record_type": "VALIDATION",
  "agent_id": "agent-001",
  "timestamp": "2026-09-07T14:00:00Z",
  "content": {
    "binary_gate": {
      "B1": "YES",
      "B5": "PARTIAL",
      "B8": "YES"
    },
    "score": 170,
    "status": "ATTACK",
    "findings": ["B5 PARTIAL because NFC models require technician"]
  },
  "evidence": [],
  "score_before": 150,
  "score_after": 170,
  "status_before": "WATCH",
  "status_after": "ATTACK"
}
```

### 2. SEARCH

When we search for evidence to validate UNKNOWNs.

```json
{
  "record_type": "SEARCH",
  "agent_id": "agent-001",
  "timestamp": "2026-09-07T14:05:00Z",
  "content": {
    "query": "Helios ELS fan insert replacement DIY Germany",
    "results": [
      {
        "source": "https://www.skybad.de/en/helios-ventilator-einsatz-els-vn-60-8137",
        "finding": "Fan insert sold directly to consumers at EUR 155.56",
        "relevance": "HIGH"
      }
    ]
  },
  "evidence": [
    {
      "type": "web_search",
      "url": "https://www.skybad.de/en/helios-ventilator-einsatz-els-vn-60-8137",
      "date": "2026-09-07",
      "confidence": "HIGH"
    }
  ]
}
```

### 3. MUTATION

When a field changes based on evidence.

```json
{
  "record_type": "MUTATION",
  "agent_id": "agent-001",
  "timestamp": "2026-09-07T14:10:00Z",
  "content": {
    "field": "hard_gates.B8",
    "old_value": "UNKNOWN",
    "new_value": true,
    "reason": "Haustechnik Binder confirmed sells directly to consumers",
    "evidence_url": "https://haustechnik-binder.de/de/Lueftung/HELIOS-Ersatz-Ventilatoren-ELS-1984-bis-2008/"
  },
  "score_before": 150,
  "score_after": 160,
  "status_before": "VERIFY",
  "status_after": "ATTACK"
}
```

### 4. NOTE

When we add context or observations.

```json
{
  "record_type": "NOTE",
  "agent_id": "agent-001",
  "timestamp": "2026-09-07T14:15:00Z",
  "content": {
    "note": "NFC models require Helios App + authorised technician. Older non-NFC models (1984-2008) are simpler DIY replacement.",
    "category": "technical"
  }
}
```

### 5. STATUS_CHANGE

When status transitions.

```json
{
  "record_type": "STATUS_CHANGE",
  "agent_id": "agent-001",
  "timestamp": "2026-09-07T14:20:00Z",
  "content": {
    "old_status": "WATCH",
    "new_status": "ATTACK",
    "reason": "B8 verified, B5/B6/B10 PARTIAL, score 170/200"
  }
}
```

---

## How GitGoblin Mutates Campaigns

### 1. GitGoblin monitors GitHub

When a specialist improves, a competitor appears, or an OEM announces something:

```
GitGoblin signal detected
  ↓
Check if signal affects any campaign
  ↓
If yes, propose mutation
  ↓
Log mutation to campaign_records
```

### 2. Example: Specialist improves

```
Signal: Byggventilasjon adds 100 new Flexit products

Check: Does this affect HCC-NOR-FLEXIT-001?
  Yes → B7 (no single specialist) may change from YES to NO

Propose mutation:
  field: "hard_gates.B7"
  old_value: true
  new_value: false
  reason: "Byggventilasjon now covers 1000+ Flexit products"
  score_impact: -10 (S14 specialist penalty)

Log to campaign_records
```

### 3. Example: OEM announces discontinuation

```
Signal: Helios announces ELS NFC end-of-life

Check: Does this affect HCC-DE-HELIOS-ELS-001?
  Yes → installed_base may increase (forced replacement)

Propose mutation:
  field: "installed_base.description"
  old_value: "Helios ELS ventilation housings installed 1984-2008"
  new_value: "Helios ELS ventilation housings installed 1984-2008 + forced replacement wave"
  reason: "OEM end-of-life announcement"
  score_impact: +5

Log to campaign_records
```

---

## BigQuery Tables

### `campaigns` (immutable JSON)
```sql
CREATE TABLE drop.campaigns (
  campaign_id STRING,
  track STRING,
  status STRING,
  binary_gate JSON,
  score INTEGER,
  rubric_scores JSON,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)
```

### `campaign_records` (append-only log)
```sql
CREATE TABLE drop.campaign_records (
  record_id STRING,
  campaign_id STRING,
  record_type STRING,
  agent_id STRING,
  timestamp TIMESTAMP,
  content JSON,
  evidence JSON,
  score_before INTEGER,
  score_after INTEGER,
  status_before STRING,
  status_after STRING
)
```

### `campaign_bottlenecks` (current state)
```sql
CREATE TABLE drop.campaign_bottlenecks (
  campaign_id STRING,
  gate_or_field STRING,
  current_value STRING,
  required_value STRING,
  data_source STRING,
  query STRING,
  updated_at TIMESTAMP
)
```

---

## The Complete Flow

```
1. CREATE campaign JSON (immutable)
2. LOG validation record
3. FOR each UNKNOWN:
   a. LOG search record
   b. Find evidence
   c. LOG mutation record
   d. Update campaign JSON
   e. LOG status_change record
4. RE-VALIDATE
5. DECIDE: ATTACK / VERIFY / WATCH / REJECT
6. MONITOR with GitGoblin
7. LOG mutations as signals appear
8. RE-VALIDATE when mutations occur
```

---

## Agent Accountability

Every record has:
- `agent_id` — who did this
- `timestamp` — when
- `evidence` — what sources were used
- `score_before/after` — what changed
- `status_before/after` — what changed

This means:
- We can audit any campaign's history
- We can see which agent made which decision
- We can trace every score change to evidence
- We can prove due diligence

---

## Key Insight

The campaign JSON is the **current state**.
The campaign_records table is the **history**.

Together they give us:
- What we believe now (JSON)
- How we got there (records)
- What changed when (timestamps)
- Who changed it (agent_id)
- Why it changed (reason + evidence)
