# Schema Corrections from B04 Review

*Critical corrections to probe schema design. Save word for word.*
*Generated: 2026-09-08T07:00:00Z*

---

## The Division

> **GoldProbe research = broad, source-dense, auditable market intelligence.**
> **BigQuery agent = deterministic compression, scoring, graph construction and hypothesis analysis.**

---

## Schema Corrections

| Old Pattern | Problem | New Rule |
|-------------|---------|----------|
| `score: 8.8` | Analyst intuition disguised as number | `null` unless produced by versioned formula from stored metrics |
| `confidence: 0.85` | Usually arbitrary | Store source quality, directness, recency, comparability, coverage separately |
| One `installed_base` number | Mixes devices, households, cumulative installs, registered systems | Typed observations; never silently equate them |
| `maintenance_probability: 1.0` because required | Requirement ≠ compliance | Store `required_interval`; observed compliance is separate |
| Wide `spend_data` row | Mixes providers and incompatible services | Atomic price observations; derived metrics reference exact rows |
| `channel_openness: high` | Interpretation masquerading as data | Store OEM restrictions, independent prices, provider/search snapshots, service-network evidence |
| `total_sellers: 50` | Search results aren't a census | Store query + geography + timestamp + returned-result sample |
| Search volume/CPC placeholders | Extremely dangerous | `null` unless authenticated source actually available |
| Failure rates like `0.05` | Easy to invent | `null` unless cohort/repair evidence |
| Estimated conversion/lead value | Experiment assumption, not market intelligence | Separate hypothesis table |
| One probe → "new pattern" | Manufactures emergence | One probe → **mechanism candidate**; independent replication → pattern |

---

## Key Principle

> A truthful one-point observation is better than a synthetic series.

Don't manufacture time-series. Store what we actually observed, when, and how.
