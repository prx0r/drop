# Probe Freshness Tracker

*Track novelty_score over time for each probe. When it drops below saturation_threshold, swap with next from queue.*

---

## Current State

| Probe | Reports | Novelty | Trend | Status |
|-------|---------|---------|-------|--------|
| Supplier Margin Radar | 9 | 0.70 | stable | ACTIVE |
| Product-Market Radar | 25 | 0.65 | declining | ACTIVE |
| Free-Traffic Query | 5 | 0.60 | declining | ACTIVE |
| Commerce Trace | 9 | 0.72 | stable | ACTIVE |
| Store Launch Blueprint | 7 | 0.40 | declining | ACTIVE |

## Freshness History

### Supplier Margin Radar
```
Report 1:  novelty 0.95 (Testo hidden channel discovered)
Report 3:  novelty 0.85 (RIDGID/Onninen Nordic channels)
Report 5:  novelty 0.75 (Makita authorization blocker)
Report 7:  novelty 0.70 (Hunter Finland stock blocker)
Report 9:  novelty 0.70 (stable — each candidate has different channels)
```

### Product-Market Radar
```
Report 1:  novelty 0.95 (first candidate discoveries)
Report 5:  novelty 0.80 (cross-country validation)
Report 10: novelty 0.70 (same categories being scanned)
Report 15: novelty 0.60 (permutations of same families)
Report 20: novelty 0.50 (needs broader SKU universe)
Report 25: novelty 0.45 (declining — same categories)
```

### Free-Traffic Query Radar
```
Report 1:  novelty 0.90 (first query clusters)
Report 3:  novelty 0.75 (decision problems identified)
Report 5:  novelty 0.60 (same categories, same queries)
```

### Commerce Trace Radar
```
Report 1:  novelty 0.85 (first longitudinal traces)
Report 5:  novelty 0.75 (new Grade A traces found)
Report 9:  novelty 0.72 (stable — value is cumulative)
```

### Store Launch Blueprint
```
Report 1:  novelty 0.80 (first verdicts)
Report 3:  novelty 0.60 (same format, same verdicts)
Report 5:  novelty 0.45 (becoming deterministic)
Report 7:  novelty 0.40 (should be pure state machine)
```

## Swap Decisions

| Probe | When to Swap | What to Swap With |
|-------|-------------|-------------------|
| Product-Market Radar | novelty < 0.40 | Market Gap Scanner |
| Free-Traffic Query | novelty < 0.40 | Price Dispersion Scanner |
| Store Launch Blueprint | novelty < 0.30 | Becomes deterministic |

## Self-Updating Probes (Never Saturate)

| Probe | Why It Stays Fresh |
|-------|-------------------|
| Installed Base Monitor | New data every month from national statistics |
| Price Dispersion Scanner | Prices change daily |
| Regulatory Tracker | Regulations change periodically |

---

## The Key Insight

> **The bottleneck is no longer prompt quality. It is observation scale + centralized persistence + real store outcomes.**

The scheduled agents are already fairly strong at interpreting evidence. We need to give them **100×-1,000× more structured evidence to interpret** rather than keep making their prompts longer.
