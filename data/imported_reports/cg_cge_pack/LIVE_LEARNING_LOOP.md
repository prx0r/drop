# Live Learning Loop

Once a campaign launches, the target changes from proxy evidence to actual outcomes.

## Live metrics

Per order:
- exact query / resolver path;
- asset/model selected;
- compatibility confidence source;
- SKU purchased;
- supplier;
- gross revenue;
- supplier cost;
- shipping;
- payment fee;
- ad attribution;
- return;
- wrong part;
- resolution success;
- human intervention;
- time to resolution.

## Outcome hierarchy

### Tier 0 — proxy
Installed base, search, public stock.

### Tier 1 — intent
Resolver sessions, exact-part searches, checkout starts.

### Tier 2 — transaction
Orders, contribution.

### Tier 3 — resolution
Correct part, no return, problem solved.

**Tier 3 is the real fitness function.**

## CG live world — later

Create `drop.live_campaign-v1`.

Candidate genes:
- SKU scope;
- supplier routing;
- page/Q&A structure;
- resolver question order;
- paid keyword scope;
- stock freshness cutoff.

Gates:
- wrong-part rate;
- refund/return rate;
- legal/safety;
- customer support burden;
- supplier SLA.

Objectives:
- contribution;
- resolution success;
- CAC;
- human minutes/order.

Again:
gates dominate revenue.

## Counterfactual learning

CG's fork primitive is ideal:

Example:
- Same traffic episode;
- change supplier routing only;
- compare contribution / ETA.

Or:
- same resolver journey;
- change question order;
- compare ambiguity reduction.

## Promotion across niches

A successful campaign creates reusable priors:
- supplier-contact success by supplier class;
- buyer-selector rate by component type;
- expected return rate by compatibility complexity;
- incumbent gap patterns by country/sector.

CGE then uses these to generate better new campaigns.
