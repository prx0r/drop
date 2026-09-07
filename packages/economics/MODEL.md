# Economic Model

## Core Formula

```
expected_profit_per_click = (expected_CVR × pre_ad_contribution) - expected_CPC
```

## Components

### Landed Cost
```
landed_cost = supplier_price + supplier_shipping + duties + fulfillment
```

### Pre-Ad Contribution
```
pre_ad_contribution = selling_price - landed_cost - payment_fees - expected_refunds - variable_costs
```

Where:
- payment_fees = 2.9% + $0.20 (Stripe/PayPal)
- expected_refunds = 5% of selling_price
- variable_costs = customer service, returns handling

### Break-Even Calculations
```
break_even_CVR = expected_CPC / pre_ad_contribution
break_even_CPC = expected_CVR × pre_ad_contribution
```

### Economic Headroom
```
economic_headroom = (expected_CVR × pre_ad_contribution) / expected_CPC
```

Interpretation:
- < 1.0: structurally unattractive
- ~1.0: razor thin
- 1.25: marginal
- 1.5+: interesting
- 2.0+: strong room for error

### Scenario Analysis

Run three scenarios:
- Pessimistic: CVR = 0.2%, CPC = $2.00
- Base: CVR = 0.5%, CPC = $1.00
- Optimistic: CVR = 1.0%, CPC = $0.50

Record all assumptions explicitly.

## Example

Product: Red-light therapy mask
- Selling price: $289
- Supplier price: $50
- Shipping: $15
- Landed cost: $65
- Payment fees: $8.58 (2.9% + $0.20)
- Expected refunds: $14.45 (5%)
- Pre-ad contribution: $200.97
- Base CVR: 0.5%
- Base CPC: $1.00
- Expected profit/click: $0.005 (break-even)
- Economic headroom: 1.0x

**Verdict: WEAK** — not enough room for error.
