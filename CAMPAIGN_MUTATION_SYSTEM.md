# Campaign Mutation System — Architecture

*Generated: 2026-09-07*
*Status: DESIGN — How to implement rubric-based mutation*

---

## The Problem

We have:
- 30+ campaigns in markdown/JSON format
- BigQuery graphs with country data, installed base, products, signals
- A validation rubric (binary gate + 20-score)
- No automated way to:
  - Validate campaigns against the rubric
  - Track mutations (field changes → score changes)
  - Identify bottlenecks (which fields are blocking ATTACK status)
  - Mine BigQuery for data that improves scores

---

## The Solution: Campaign Mutation Engine

### Architecture

```
BIGQUERY GRAPHS
     │
     ▼
CAMPANN MUTATION ENGINE
     │
     ├── Load campaigns from JSON files
     ├── Load rubric from CAMPAIGN_VALIDATION_RUBRIC.md
     ├── For each campaign:
     │     ├── Run binary gate
     │     ├── Run score rubric
     │     ├── Identify bottlenecks (UNKNOWN fields)
     │     ├── Mine BigQuery for missing data
     │     ├── Propose mutations
     │     └── Track mutations
     ├── Save results to BigQuery
     └── Generate reports
```

### BigQuery Tables

#### `campaigns`
```sql
CREATE TABLE drop.campaigns (
  campaign_id STRING,
  track STRING,
  status STRING,
  binary_gate JSON,
  score INTEGER,
  rubric_scores JSON,
  bottlenecks JSON,
  mutations JSON,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)
```

#### `campaign_mutations`
```sql
CREATE TABLE drop.campaign_mutations (
  mutation_id STRING,
  campaign_id STRING,
  field STRING,
  old_value JSON,
  new_value JSON,
  reason STRING,
  score_impact INTEGER,
  new_total INTEGER,
  new_status STRING,
  created_at TIMESTAMP
)
```

#### `campaign_bottlenecks`
```sql
CREATE TABLE drop.campaign_bottlenecks (
  bottleneck_id STRING,
  campaign_id STRING,
  gate_or_field STRING,
  current_value STRING,
  required_value STRING,
  data_source STRING,
  query STRING,
  created_at TIMESTAMP
)
```

---

## The Mutation Loop

```text
1. LOAD all campaigns from JSON files in thesisTesting/

2. FOR each campaign:
   a. RUN binary gate
      - If any NO → mark as REJECT, log reason
      - If all YES → proceed to score

   b. RUN score rubric (20 statements)
      - For each statement, check if verified
      - If UNKNOWN → mark as bottleneck
      - Calculate total score

   c. IDENTIFY bottlenecks
      - Which fields are UNKNOWN?
      - Which fields need data?
      - Which BigQuery table has the data?

   d. MINE BigQuery for missing data
      - Query country_data for installed base
      - Query products for compatibility
      - Query dropintel_signals for market evidence
      - Query competitor_data for specialist count

   e. PROPOSE mutations
      - For each bottleneck, propose a mutation
      - Calculate score impact
      - If score ≥ 160 → propose ATTACK status

   f. TRACK mutations
      - Log each mutation to campaign_mutations
      - Update campaign score and status

3. SAVE results to BigQuery

4. GENERATE report
   - Which campaigns are ATTACK ready
   - Which campaigns need verification
   - Which campaigns should be killed
   - What mutations had the biggest impact
```

---

## Implementation Options

### Option A: Standalone Python Script

Create `/root/drop/scripts/campaign_mutator.py` that:
1. Reads all campaign JSONs
2. Runs the rubric
3. Queries BigQuery
4. Outputs mutations

**Pros:** Simple, fast, no dependencies
**Cons:** Manual execution, no API

### Option B: GitGoblin Extension

Add a new GitGoblin command `gitgoblin mutate` that:
1. Reads campaigns from BigQuery
2. Runs the rubric
3. Queries BigQuery graphs
4. Proposes mutations
5. Saves results back to BigQuery

**Pros:** Integrated with GitGoblin, API available
**Cons:** More complex, requires GitGoblin changes

### Option C: BigQuery Stored Procedures

Create BigQuery stored procedures that:
1. Validate campaigns against rubric
2. Identify bottlenecks
3. Query related data
4. Output recommendations

**Pros:** Runs in BigQuery, no local execution
**Cons:** Limited logic, no external API calls

### Option D: Hybrid (Recommended)

1. **BigQuery** stores campaigns, mutations, bottlenecks
2. **Python script** runs the rubric and mines data
3. **GitGoblin API** exposes results
4. **Drop dashboard** visualizes mutations

---

## The Rubric as Code

```python
class CampaignRubric:
    def __init__(self):
        self.binary_gate = [
            ("B1", "installed_base_exists", self.check_installed_base),
            ("B2", "lifecycle_trigger_exists", self.check_lifecycle_trigger),
            ("B3", "compatibility_problem_exists", self.check_compatibility),
            ("B4", "local_supply_exists", self.check_local_supply),
            ("B5", "consumer_can_self_identify", self.check_self_identify),
            ("B6", "shippable_without_technician", self.check_shippable),
            ("B7", "no_single_specialist", self.check_specialist),
            ("B8", "supplier_will_sell", self.check_supplier),
            ("B9", "compatibility_proven", self.check_compatibility_proven),
            ("B10", "legal_responsibility_explicit", self.check_legal),
        ]
        
        self.score_rubric = [
            ("S1", "identity_requires_photo", 10, 0),
            ("S2", "wrong_part_has_cost", 10, 0),
            ("S3", "supersession_complex", 10, 0),
            ("S4", "installed_base_large", 10, 0),
            ("S5", "replacement_frequency", 10, 0),
            ("S6", "multiple_suppliers", 10, 0),
            ("S7", "supplier_has_feed", 10, 0),
            ("S8", "supplier_direct_ship", 10, -10),
            ("S9", "small_parcel", 10, 0),
            ("S10", "photo_identifiable", 10, 0),
            ("S11", "aov_high", 10, -10),
            ("S12", "margin_verified", 10, 0),
            ("S13", "wrong_part_rate_low", 10, -10),
            ("S14", "best_specialist_weak", 10, -10),
            ("S15", "oem_not_competing", 10, -10),
            ("S16", "marketplace_not_dominant", 10, -10),
            ("S17", "native_language_advantage", 10, 0),
            ("S18", "local_terminology_nontrivial", 10, 0),
            ("S19", "fits_gmc", 10, 0),
            ("S20", "fits_shopify", 10, 0),
        ]
    
    def validate(self, campaign: dict) -> dict:
        # Run binary gate
        gate_results = {}
        for gate_id, field, checker in self.binary_gate:
            gate_results[gate_id] = checker(campaign)
        
        # If any NO, reject
        if any(v == "NO" for v in gate_results.values()):
            return {
                "status": "REJECT",
                "binary_gate": gate_results,
                "score": 0,
                "reason": f"Failed gate: {[k for k,v in gate_results.items() if v == 'NO']}"
            }
        
        # Run score rubric
        scores = {}
        for score_id, field, yes_score, no_score in self.score_rubric:
            scores[score_id] = self.check_score(campaign, field, yes_score, no_score)
        
        total = sum(scores.values())
        
        # Determine status
        if total >= 160:
            status = "ATTACK"
        elif total >= 120:
            status = "VERIFY"
        elif total >= 80:
            status = "SCAN"
        else:
            status = "REJECT"
        
        return {
            "status": status,
            "binary_gate": gate_results,
            "scores": scores,
            "total": total
        }
    
    def identify_bottlenecks(self, campaign: dict, validation: dict) -> list:
        bottlenecks = []
        
        # Check binary gate UNKNOWNs
        for gate_id, result in validation["binary_gate"].items():
            if result == "UNKNOWN":
                bottlenecks.append({
                    "type": "gate",
                    "field": gate_id,
                    "current": "UNKNOWN",
                    "required": "YES"
                })
        
        # Check score rubric UNKNOWNs
        for score_id, score in validation["scores"].items():
            if score == 0:  # Could be YES or UNKNOWN
                bottlenecks.append({
                    "type": "score",
                    "field": score_id,
                    "current": "UNKNOWN",
                    "required": "verified"
                })
        
        return bottlenecks
    
    def mine_bigquery(self, campaign: dict, bottlenecks: list) -> dict:
        """Query BigQuery for missing data."""
        # This would connect to BigQuery and run queries
        # Returns suggested mutations
        mutations = []
        
        for bottleneck in bottlenecks:
            # Query BigQuery for relevant data
            # If found, propose mutation
            mutations.append({
                "field": bottleneck["field"],
                "suggested_value": "verified",
                "source": "bigquery",
                "score_impact": "+10"
            })
        
        return mutations
```

---

## How GitGoblin Helps

GitGoblin can:
1. **Monitor GitHub** for new releases, PRs, issues related to our campaigns
2. **Detect when a specialist improves** (new features, better documentation)
3. **Alert when a competitor appears** (new Shopify store, new Merchant Center feed)
4. **Track OEM announcements** (new product launches, discontinuations)

This feeds into the mutation engine:
- If a specialist improves → update best_specialist score
- If a competitor appears → update marketplace dominance score
- If an OEM announces discontinuation → update supersession graph

---

## Next Steps

1. Create `/root/drop/scripts/campaign_mutator.py`
2. Load all campaign JSONs
3. Run rubric against each
4. Query BigQuery for missing data
5. Output mutations
6. Save to BigQuery
7. Create GitGoblin command `gitgoblin mutate`
