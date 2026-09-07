# v1 -> v2 Migration

`segments.jsonl` is retained for backward compatibility but deprecated for new research. Its functions split into `ecosystems.jsonl`, `problems.jsonl`, `queries.jsonl`, `source_archetypes.jsonl` and `source_target_gaps.jsonl`.

v1 `score_model.json` is superseded by separate discovery and launch score models. Existing v1 product-market scores remain historical records and are labeled with the v2 launch score contract; do not retroactively change historical component values without a new score snapshot.
