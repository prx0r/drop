# Deep-niche transplants

These are **not clones** of the case studies. Each applies a proven economic recipe to another workflow. Scores are directional and are also included in `data/opportunity_seeds.csv`.

## Tier 1 — build/validate first

### 1. Practice Statement Normalizer for UK accountants
**Recipe:** ugly input → exact clean output.  
**Input:** PDFs/CSVs from niche banks, card processors, lenders, marketplaces and payment providers.  
**Output:** Xero/QuickBooks-compatible CSV + reconciliation-ready categories.  
**Buyer:** small accountancy/bookkeeping practices.  
**Why asymmetric:** monthly recurring task; every client adds volume; errors have direct labor cost; a practice can justify £49–£199/month.  
**MVP:** support 3 high-pain statement types, not “all banks.”  
**Distribution:** accountant communities, Xero ecosystem consultants, exact-search landing pages (“X statement to Xero CSV”).

### 2. Trade Supplier Invoice Normalizer
**Recipe:** ugly input → exact clean output.  
**Input:** emailed/PDF invoices from builders' merchants and trade suppliers.  
**Output:** line-item CSV/Xero bills/job-costing import mapped to project/reference.  
**Buyer:** small builders, electricians, plumbers, bookkeepers serving trades.  
**Wedge:** line items + job references, not generic invoice OCR.

### 3. Xero Practice Ops Adapter
**Recipe:** sticky incumbent → expert adapter.  
**Jobs:** chase missing documents, create standardized draft notes, classify exceptions, summarize unreconciled transactions, prepare client query lists, export evidence packs.  
**Buyer:** bookkeeping/accountancy practice.  
**Safety:** suggestions/drafts first; approvals before financial changes.  
**Pricing:** per practice/seat, not token usage.

### 4. ServiceM8/Fergus-style Field Ops Adapter
**Recipe:** sticky incumbent → expert adapter.  
**Jobs:** convert incoming email/SMS/web lead into job, draft quote from template, chase approval, schedule follow-up, summarize site notes, prepare invoice handoff.  
**Buyer:** 3–30 person service firms.  
**Wedge:** one trade first (e.g. heat pumps, commercial electrical, pest control), one country.

### 5. Public Tender Change Radar
**Recipe:** valuable event → instant alert.  
**Sources:** official public procurement portals and RSS/API feeds where available.  
**Event:** new tender / amendment / deadline change matching a specific capability/geography.  
**Buyer:** small specialist contractors/consultancies.  
**Output:** alert + qualification summary + deadline + required documents + CRM webhook.  
**Why better than generic tender search:** every alert is normalized to “should we bid?”

### 6. Planning / Permit Opportunity Radar
**Recipe:** valuable public event → alert.  
**Sources:** local authority planning/permit data where lawful and public.  
**Buyer:** architects, surveyors, specialist installers, arborists, heritage consultants, drainage firms.  
**Event value:** a single won project can fund months of monitoring.  
**Moat:** local taxonomy + geo matching + entity resolution.

### 7. Vertical Form Backend for Agencies Serving One Trade
**Recipe:** Web3Forms primitive + vertical object.  
Instead of “form to email,” produce a **qualified lead/job object** with service type, postcode, urgency, attachments, consent, spam checks and webhook into CRM/job-management software.  
**Buyer:** web agencies and trade businesses.  
**Pricing:** per site or agency bundle.

### 8. Legacy Portal Browser Assistant
**Recipe:** browser-native workflow helper.  
**Target:** a legal/authorized portal with repetitive data entry used by a narrow profession.  
**MVP:** autofill from local templates, copy structured data between tabs, validate required fields, create audit note.  
**Rule:** do not bypass access controls or automate prohibited actions.  
**Buyer:** professionals who spend hours in the same portal weekly.

## Tier 2 — attractive after interviews

### 9. UK Business Identity Validation API
**Recipe:** one API key for related validation.  
Bundle lawful/public/company-provided checks such as Companies House identifier normalization, VAT-format validation, postcode/address normalization, domain/email checks and duplicate detection into one schema.  
**Buyer:** B2B onboarding tools, accountants, agencies, marketplaces.  
**Wedge:** UK-native schema and error semantics.

### 10. Agency Client Portal “Thin Layer”
**Recipe:** boring client-facing infra.  
Do not build a PSA. Provide one hosted branded surface for file requests, approvals, status, recurring deliverables and payment links, integrating with the agency's existing tools.

### 11. Supplier Price-List Normalizer
**Recipe:** messy file → normalized catalog.  
**Buyer:** distributors, installers, independent retailers.  
**Input:** weekly Excel/PDF/email price lists from multiple suppliers.  
**Output:** canonical SKU/price/availability feed + change alerts.  
**Recurring loop:** every supplier update triggers value.

### 12. Insurance Commission Statement Reconciler
**Recipe:** statement → reconciliation output.  
**Buyer:** small brokerages/finance intermediaries.  
**Wedge:** one statement format + one accounting target first.  
**Note:** do not make regulated advice decisions; keep scope to reconciliation/operations.

### 13. Property Management Rent-Roll Normalizer
**Recipe:** export transformation.  
Convert rent rolls/statements from one property system or letting-agent export into the exact reporting/accounting format another party requires.

### 14. Certification / Renewal Radar
**Recipe:** valuable deadline/event → alert.  
**Buyer:** companies managing recurring staff/equipment/vendor certifications.  
**Value:** missing a renewal causes downtime or lost work.  
**MVP:** CSV import + reminders + evidence links, then integrate official sources.

### 15. Niche Vendor Directory with Verification
**Recipe:** directory → supplier-funded monetization.  
Pick a purchase where buyers care about hard filters: geography, certification, machine capability, lead time, insurance, minimum order, supported standard.  
**Monetize:** verification, lead routing, featured slots, RFQ responses, sponsored category.

### 16. Specialist Job-Board Meta Directory
**Recipe:** JobBoardSearch translated into a profession where jobs live across association boards, company pages and specialist agencies.  
**Monetize:** boards/recruiters pay for visibility; candidate side remains free.

## Tier 3 — good recipes, more platform/operational risk

### 17. Public Community Intent Monitor
Monitor lawful/public community sources for requests matching an expensive B2B service; route only high-confidence opportunities. Avoid private-account automation or ToS-hostile scraping.

### 18. Niche Local Search Ops
Apply Local SEO Bot economics to a single vertical + country with a repeatable checklist, GBP integration and proof-of-calls/reporting.

### 19. Hosted Open-Source Workflow Primitive
Pick a proven open-source utility used by a narrow industry and sell hosting, upgrades, backups, access control and support. The moat is industry defaults, templates and integrations.

### 20. Data Export / Backup for One SaaS
Many SMB SaaS products make migration/export tedious. Offer scheduled export to customer-owned storage with human-readable snapshots and restore tooling, using official APIs where possible.

# Highest-conviction sequence

1. Interview 10 accountants/bookkeepers + 10 field-service operators.
2. Ask for the actual ugly files/screens/screenshots that waste time.
3. Pick the task that occurs at least monthly and currently costs >£30 in labor per customer.
4. Build the transformation/action before building a dashboard.
5. Charge the first customer before adding breadth.
6. Add integrations only when three paying users request the same one.
