# Machine-readable data plan

Use the included canonical schemas to build a replayable state/action/outcome dataset.

### State
- market rank / demand bucket / rank change
- keyword volume / CPC / competition
- own price vs benchmark
- impressions / clicks / CTR / CPC
- ATC / checkout / purchase / CVR
- COGS / gross profit / contribution profit
- inventory / supplier latency / payment holds

### Action
- title/feed edit
- price change
- budget/bid change
- campaign split
- Standard Shopping -> PMax/value bidding transition
- SKU add/kill/promote
- landing-page/CRO change
- supplier/market expansion

### Outcome windows
Store `t+1d`, `t+7d`, `t+14d`, `t+30d` outcomes. Conversion lag means short windows should not be treated as final truth.

### External case studies
Treat them as **operator policy traces**, not ground-truth causal data. Keep provenance, confidence, commercial incentive and whether the post was contemporaneous.
