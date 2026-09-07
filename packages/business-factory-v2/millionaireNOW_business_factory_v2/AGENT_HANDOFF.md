# Coding-agent handoff

## Objective
Take exactly ONE kernel to first revenue. Do not productionize all five simultaneously.

## Recommended first sprint: Database Reactivator
1. Add CSV upload parser and dedupe by normalized email/phone.
2. Add per-client tenancy and encrypted secrets.
3. Add a review UI for eligibility/drafts/approvals.
4. Add client-authorized Gmail/CRM sending only after compliance review; maintain hard opt-out suppression.
5. Add calendar outcome webhook and held-appointment verification.
6. Price first deal as no setup + £X per held appointment or 10–20% of attributable gross profit.

## Second sprint: Signal Radar
1. Run a nightly Planning Data ingestion job.
2. Persist API cursor/checkpoint and fetch failures.
3. Improve classifier from customer feedback, not LLM vibes.
4. Add postcode/radius geometry.
5. Build one landing page per REAL covered territory only.
6. Add Stripe only after someone agrees to pay.

## Engineering rules
- Do not let LLM output overwrite sourced facts.
- Do not scrape a source whose terms prohibit it; prefer official APIs/feeds.
- Never rank suppliers by commission.
- Never send marketing to an ineligible/opted-out reactivation contact.
- Preserve every factual source observation with timestamp and hash.
- Any "estimated savings" must state whether arithmetic, customer-quoted, or sourced benchmark.
- Add integrations behind adapters; tests must run without internet.

## Acceptance criteria before public launch
- tenant isolation
- long random admin/customer auth secrets
- HTTPS behind Caddy/Nginx
- backups
- privacy/terms/disclosure pages
- deletion/export workflow for personal data
- source-specific ToS review
- monitoring and alerts
- payment/refund logic where applicable
