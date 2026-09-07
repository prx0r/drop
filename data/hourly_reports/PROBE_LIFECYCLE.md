# Probe Lifecycle Management

*Every probe has a lifecycle: initial value → saturation → retirement. Track it. Replace it. Keep learning.*

---

## The Problem

Our current probes (Product-Market, Supplier Margin, Free-Traffic, Commerce Trace, Store Launch Blueprint) were designed for discovery. They're excellent at finding opportunities.

But they have diminishing returns:
- First 20 reports: insanely valuable
- Reports 21-50: still useful but repetitive
- Reports 51+: saturated, mostly confirming what we already know

**We need to track this and swap probes when they stop producing new information.**

---

## The Probe Registry

```json
{
  "probe_registry": {
    "active_probes": [
      {
        "probe_id": "product-market-radar",
        "name": "Product-Market Opportunity Radar",
        "type": "discovery",
        "status": "active",
        "reports_generated": 25,
        "first_report": "2026-09-07T00:38:00Z",
        "last_report": "2026-09-07T05:00:00Z",
        "novelty_score": 0.65,
        "novelty_trend": "declining",
        "saturation_threshold": 0.3,
        "retirement_action": "replace_with_market_gap_scanner"
      },
      {
        "probe_id": "supplier-margin-radar",
        "name": "Supplier Margin Radar",
        "type": "validation",
        "status": "active",
        "reports_generated": 9,
        "first_report": "2026-09-07T04:00:00Z",
        "last_report": "2026-09-07T06:00:00Z",
        "novelty_score": 0.70,
        "novelty_trend": "stable",
        "saturation_threshold": 0.3,
        "retirement_action": "keep_until_blockers_resolved"
      },
      {
        "probe_id": "free-traffic-radar",
        "name": "Free-Traffic Query Radar",
        "type": "discovery",
        "status": "active",
        "reports_generated": 5,
        "first_report": "2026-09-07T04:00:00Z",
        "last_report": "2026-09-07T06:00:00Z",
        "novelty_score": 0.60,
        "novelty_trend": "declining",
        "saturation_threshold": 0.3,
        "retirement_action": "reduce_to_decisions_only"
      },
      {
        "probe_id": "commerce-trace-radar",
        "name": "Commerce Trace Radar",
        "type": "intelligence",
        "status": "active",
        "reports_generated": 9,
        "first_report": "2026-09-07T05:00:00Z",
        "last_report": "2026-09-07T06:00:00Z",
        "novelty_score": 0.72,
        "novelty_trend": "stable",
        "saturation_threshold": 0.3,
        "retirement_action": "reduce_to_grade_a_only"
      },
      {
        "probe_id": "store-launch-blueprint",
        "name": "Store Launch Blueprint Engine",
        "type": "planning",
        "status": "active",
        "reports_generated": 7,
        "first_report": "2026-09-07T05:00:00Z",
        "last_report": "2026-09-07T06:00:00Z",
        "novelty_score": 0.40,
        "novelty_trend": "declining",
        "saturation_threshold": 0.3,
        "retirement_action": "conditional_only"
      }
    ],
    "probe_queue": [
      {
        "probe_id": "market-gap-scanner",
        "name": "Market Gap Scanner",
        "type": "discovery",
        "description": "Scans product × country cells for merchant gaps using Prisjakt/Hinta.fi data",
        "prerequisite": "Prisjakt API access",
        "estimated_novelty": 0.85,
        "estimated_cost": "€0"
      },
      {
        "probe_id": "installed-base-monitor",
        "name": "Installed Base Monitor",
        "type": "monitoring",
        "description": "Tracks installed base growth vs merchant coverage over time",
        "prerequisite": "None",
        "estimated_novelty": 0.80,
        "estimated_cost": "€0"
      },
      {
        "probe_id": "regulatory-compliance-tracker",
        "name": "Regulatory Compliance Tracker",
        "type": "monitoring",
        "description": "Tracks regulatory changes that create/destroy opportunities",
        "prerequisite": "None",
        "estimated_novelty": 0.75,
        "estimated_cost": "€0"
      },
      {
        "probe_id": "price-dispersion-scanner",
        "name": "Price Dispersion Scanner",
        "type": "discovery",
        "description": "Finds products with high price dispersion across markets",
        "prerequisite": "Prisjakt API access",
        "estimated_novelty": 0.70,
        "estimated_cost": "€0"
      }
    ]
  }
}
```

---

## Freshness Tracking

### How to Measure Novelty

After each report, score it 0-1:

```python
def score_novelty(report, previous_reports):
    """Score how much new information this report provides."""
    new_findings = 0
    for finding in report["findings"]:
        is_novel = True
        for prev in previous_reports[-10:]:  # Check last 10 reports
            for prev_finding in prev["findings"]:
                if similar(finding, prev_finding):
                    is_novel = False
                    break
        if is_novel:
            new_findings += 1
    
    novelty = new_findings / max(1, len(report["findings"]))
    return novelty
```

### The Freshness Curve

```
Report #  | Novelty Score | Status
1         | 0.95          | INSANELY VALUABLE
5         | 0.80          | Very valuable
10        | 0.65          | Still useful
20        | 0.45          | Diminishing returns
30        | 0.30          | SATURATION THRESHOLD
50        | 0.15          | Retire
```

### When to Swap a Probe

```python
def should_swap(probe):
    """Determine if a probe should be replaced."""
    if probe["novelty_score"] < probe["saturation_threshold"]:
        return True, probe["retirement_action"]
    if probe["novelty_trend"] == "declining" and probe["reports_generated"] > 20:
        return True, probe["retirement_action"]
    return False, None
```

---

## The Probe Queue

When a probe saturates, swap in the next one from the queue:

```python
def swap_probe(saturated_probe_id, probe_queue):
    """Replace a saturated probe with the next one in queue."""
    # Find the saturated probe
    for i, probe in enumerate(probe_queue):
        if probe["estimated_novelty"] > 0.5:  # Still fresh
            # Remove from queue
            new_probe = probe_queue.pop(i)
            # Add to active
            active_probes.append(new_probe)
            print(f"Swapped {saturated_probe_id} → {new_probe['name']}")
            return True
    print("No fresh probes in queue")
    return False
```

---

## Probe Specifications (for Queue)

### Market Gap Scanner
```json
{
  "probe_id": "market-gap-scanner",
  "type": "discovery",
  "description": "Scans product × country cells for merchant gaps using Prisjakt/Hinta.fi data",
  "data_sources": ["Prisjakt API", "Hinta.fi", "Google Shopping"],
  "output": "Ranked list of product × country cells with GOOD_SELLER_GAP scores",
  "refresh_frequency": "daily",
  "prerequisites": ["Prisjakt Partner API access"],
  "estimated_novelty": 0.85,
  "estimated_cost": "€0",
  "lifecycle": "initial 20 runs → novelty 0.85, then declining as market is mapped"
}
```

### Installed Base Monitor
```json
{
  "probe_id": "installed-base-monitor",
  "type": "monitoring",
  "description": "Tracks installed base growth vs merchant coverage over time",
  "data_sources": ["National statistics", "Industry reports", "Google Trends"],
  "output": "Time-series of installed_base vs merchant_count per ecosystem",
  "refresh_frequency": "monthly",
  "prerequisites": ["None"],
  "estimated_novelty": 0.80,
  "estimated_cost": "€0",
  "lifecycle": "continually fresh — new data every month"
}
```

### Regulatory Compliance Tracker
```json
{
  "probe_id": "regulatory-compliance-tracker",
  "type": "monitoring",
  "description": "Tracks regulatory changes that create/destroy opportunities",
  "data_sources": ["Government websites", "Industry associations", "Legal databases"],
  "output": "Alerts on regulatory changes affecting installed base ecosystems",
  "refresh_frequency": "weekly",
  "prerequisites": ["None"],
  "estimated_novelty": 0.75,
  "estimated_cost": "€0",
  "lifecycle": "continually fresh — regulations change periodically"
}
```

---

## The Self-Updating Probe Concept

Some probes can be designed to remain continually fresh:

### Continually Fresh Probes
- **Installed Base Monitor** — new data every month
- **Price Dispersion Scanner** — prices change daily
- **Regulatory Tracker** — regulations change periodically
- **Competitor Quality Scanner** — merchants update sites

### Saturating Probes
- **Product-Market Radar** — same categories, same findings
- **Free-Traffic Radar** — same queries, same opportunities
- **Store Launch Blueprint** — same format, same verdicts

### The Goal
Design probes that are **self-updating** — they pull new data each run and always produce fresh insights. Avoid probes that just reconfirm what we already know.

---

## The Monitoring Dashboard

```sql
-- Which probes are still producing novel findings?
SELECT 
  probe_id,
  reports_generated,
  novelty_score,
  novelty_trend,
  CASE 
    WHEN novelty_score < 0.3 THEN 'RETIRE'
    WHEN novelty_score < 0.5 THEN 'WATCH'
    ELSE 'ACTIVE'
  END as status
FROM probe_registry
ORDER BY novelty_score DESC
```

This tells us: **which probes are still worth running?**
