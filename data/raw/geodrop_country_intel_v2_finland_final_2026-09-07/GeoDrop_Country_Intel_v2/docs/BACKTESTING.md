# Backtesting & Strategy Learning

## Why ecommerce backtests fail
The dominant failure is look-ahead bias: today's seller census, price, report, search volume or known winner is silently used to make a historical decision. Other failures are survivor bias, cherry-picked candidate universes, reconstructed CPCs, mutable strategy definitions and evaluating only launched winners.

## Protocol
1. Freeze `strategy_id@version`.
2. Freeze candidate universe before ranking; log rejected candidates too.
3. Set `as_of` decision timestamp.
4. Resolve every referenced observation/snapshot to `available_at`.
5. Reject TRUE_HISTORICAL evaluation if any required evidence was unavailable/unknown at `as_of`.
6. Score with the frozen code/version only.
7. Store ranking and predicted probabilities before outcomes.
8. Evaluate later against standardized outcomes.

## Preferred evidence classes
`PROSPECTIVE_SHADOW` > `TRUE_HISTORICAL` > `RECONSTRUCTED_HISTORICAL` for confidence in strategy performance.

## Metrics
- precision@k / validation hit rate
- false-positive rate + reason taxonomy
- false-negative audits where feasible
- time to falsification
- capital spent per validated winner
- median realized contribution per probe
- contribution after returns/warranty
- calibration / Brier score for probabilistic predictions
- rank correlation of discovery/launch scores with realized economics
- performance by country, ecosystem, AOV, source-market type and acquisition channel

## Bayesian paid-probe rule
For qualified-click conversion, Beta prior may start `Beta(1,1)` unless a frozen empirical prior exists. Posterior after `o` orders from `n` qualified clicks: `Beta(1+o, 1+n-o)`. Compare posterior probability that CVR exceeds contribution-derived break-even CVR. Do not impose arbitrary day-count kills.
