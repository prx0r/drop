# Active Learning / Expected Value of Information

## Why

Most campaigns should die before:
- building a store;
- contacting 50 suppliers;
- spending on ads;
- extracting 5,000 SKUs.

The system should choose the **cheapest high-kill-power question first**.

## Research action object

```json
{
  "action_type": "BUYER_ROLE_SAMPLE",
  "target_gate": "G4",
  "cost_eur": 0,
  "human_minutes": 15,
  "expected_resolution_probability": null,
  "expected_kill_probability": null
}
```

Probabilities are not LLM judgments.

They come from historical `research_action_outcomes` grouped by:
- gate;
- track;
- asset class;
- action type.

If no history exists, use an explicit broad prior.

## Simple first acquisition function

Before enough historical data exists:

```text
ACTION_PRIORITY =
  fatality_weight
× unresolved_gate_weight
× expected_source_strength
÷ (cash_cost + human_minutes_cost + latency_cost)
```

Suggested fatality ordering:

1. buyer / SKU-selector role
2. best-incumbent ownership gap
3. reseller permission
4. real supplier economics
5. annual addressable demand
6. compatibility proof
7. feed/retrieval details

Why:
if the consumer never selects the SKU, there is no D2C campaign.

## Learned EVI

After enough action outcomes:

```text
EVI(a) =
P(KILL | a, context) × downstream_cost_avoided
+
P(PASS | a, context) × expected_value_unlocked
-
action_cost
-
delay_cost
```

Use empirical/Bayesian estimates.

Example Beta prior:

```text
supplier_contact_reseller_success:
Beta(alpha, beta)
```

Update from actual contacts.

Never invent `P=0.78`.

## CG use

`drop.evidence_acquisition-v1` can rank candidate action plans against a frozen table of historical action priors.

CGE proposes action combinations.

CG judges whether an action plan:
- stays within budget;
- targets real UNKNOWN gates;
- uses acceptable evidence sources;
- minimizes expected waste.

## Human actions

Some gates are irreducibly human:
- opening trade account;
- negotiating direct ship;
- confirming warranty liability.

The optimizer should output them explicitly as `HUMAN_ACTION_REQUIRED`, not simulate completion.
