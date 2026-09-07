# 7. Agent automation architecture

## The right architecture: evidence pipeline, not autonomous content farm

```text
Sources
  -> collector
  -> normalizer
  -> provenance store
  -> change detector
  -> quality gate
  -> page/data generator
  -> human approval (when material)
  -> publish
  -> analytics/conversion monitor
  -> monetization recommender
```

## Agent roles

### 1. Scout

Finds:

- new providers;
- changed pricing;
- new complaints;
- emerging query patterns;
- new affiliate/referral programs;
- broken/stale records.

Output is structured candidates, never published prose.

### 2. Verifier

For every material field:

- opens primary source;
- records source URL;
- records retrieval time;
- extracts exact factual field;
- marks confidence;
- rejects conflicting data for review.

### 3. Editor

Creates a page draft from verified fields and adds explanation only where necessary.

The page must pass:

- unique-value test;
- factual-support test;
- duplicate-page test;
- commercial disclosure check;
- “would this still be useful if Google sent zero traffic?” test.

### 4. Revenue agent

Looks for monetization opportunities:

- vendors receiving clicks but not paying;
- high-conversion categories without sponsors;
- affiliate programs matching actual clicks;
- users repeatedly using the same filters -> premium alert idea;
- completed introductions -> fee opportunity.

### 5. Operator/reporter

Produces a daily/weekly report:

- records added/changed;
- pages updated;
- organic impressions/clicks;
- referral clicks;
- leads;
- revenue;
- stale records;
- manual approvals needed.

## Safety / quality rules

1. No fabricated reviews.
2. No invented prices.
3. No “best” ranking without explicit scoring methodology.
4. Sponsored placement is labelled.
5. Affiliate relationships are disclosed.
6. Respect API terms, robots rules, and content licenses.
7. Cold outreach is drafted first; human approves sending.
8. Do not create hundreds of thin location/query pages.
9. Every indexable page must contain a unique dataset slice or function.
10. If source data is stale, show stale state rather than hallucinating a refresh.

## Minimal data schema

```json
{
  "id": "vendor-slug",
  "name": "Vendor name",
  "category": "category",
  "region": "UK",
  "price_from": null,
  "attributes": {},
  "source_url": "https://primary-source.example/",
  "last_verified": "2026-09-04",
  "confidence": 0.95,
  "is_sponsored": false,
  "affiliate_url": null
}
```

## Scheduling

- data-change checks: daily/weekly depending on volatility;
- analytics report: daily;
- monetization review: weekly;
- full source reverification: monthly/quarterly;
- page publication: event-driven by verified useful data, **not** arbitrary “one page per night.”
