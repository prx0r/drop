# Implementation Blueprint

## Minimal architecture

```text
Marketplace/Shopify checkout
        |
        v
Personalization intake
        |
        +--> secure uploads (private object store)
        |
        v
Structured order facts --------------+
        |                              |
        v                              v
Deterministic transforms       LLM copy/narrative
(chart math, OCR check,        grounded only in
image metadata, puzzle         supplied/computed facts
validation, dedupe)             |
        |                       |
        +-----------+-----------+
                    v
             Product document model
                    |
             render preview/assets
                    |
          automated quality checks
                    |
              buyer approval
                    |
         POD quote/order adapter
                    |
             tracking + reminder
```

## Recommended services

The package is provider-agnostic, but current research validates the following infrastructure patterns:

- **Books:** Lulu API or Gelato; both explicitly support personalized book workflows.
- **Cards/multipage print:** Prodigi/Gelato; Prodigi v4 quote API is included as a non-ordering adapter.
- **Simple Etsy POD personalization:** Printify automated text/image mapping and live preview.
- **Object storage:** any private S3-compatible bucket with signed URLs.
- **Database:** Postgres for customer/occasion graph; SQLite is sufficient for local prototyping.
- **Generation:** any OpenAI-compatible LLM plus a separate image model where needed.

## Data schema worth preserving

### Recipient
- internal id
- display name
- relation label (optional)
- occasion ids
- address encrypted / only if user chooses to store
- style preferences
- approved media collection references

### Occasion
- recipient id
- type
- date
- reminder lead time
- last artifact/product
- last order date

### Gift project
- immutable user inputs snapshot
- deterministic computed facts
- generation model/version/prompt template version
- final approved text/layout
- print assets checksums
- fulfillment quote/order id

## Critical architecture rule

Never let a generative model become the system of record for facts.

Examples:
- astrology positions come from a chart engine;
- dates/names come from structured customer input;
- recipe quantities come from buyer-approved transcription;
- crossword validity comes from a solver;
- order pricing comes from a fulfillment quote.

The LLM is a **renderer/interpreter**, not the source of truth.

## One-click preview loop

A winning product should minimize the time between input and “wow”:

1. ask only the minimum fields;
2. render a representative partial preview;
3. let the buyer edit the highest-risk fields;
4. only ask for secondary information after they have seen value.

For a newspaper, five fields can be enough to show a front-page draft. For a game deck, show five cards. For an astrology book, show cover + two sample spreads after birth data is computed.

## Manual-first validation

Automation is not the first milestone. The first milestone is proof that customers want the output.

For the first 20 orders:
- permit a manual review queue;
- measure minutes/order;
- record every customer correction;
- turn repeated corrections into deterministic validators;
- only then remove the human review step where safe.

## KPI set

### Demand
- search/listing impressions
- click-through
- favorite/save rate
- add-to-cart
- conversion

### Personalization UX
- form start → complete
- average input time
- preview edit rate
- abandonment by field

### Economics
- actual POD product cost
- shipping
- marketplace/payment fees
- refund/reprint rate
- support minutes/order
- contribution margin before CAC
- CAC and contribution after CAC

### Moat
- % buyers saving a recipient/occasion
- reminders set
- repeat purchase rate
- gift attach rate
- % projects created from previously stored recipient data

## Shipping/Q4 guardrail

The order system must know the latest safe production date per SKU/destination. When the physical SLA becomes unsafe, automatically switch the listing/landing page to a digital version or “gift certificate + physical item follows” offer. Never sell delivery certainty the supplier cannot meet.
