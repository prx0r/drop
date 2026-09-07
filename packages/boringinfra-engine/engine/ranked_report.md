# Ranked boring-infra opportunities

Score prioritizes verified demand, workflow value, recurrence, WTP, simplicity, data access and distribution, then penalizes platform/support/regulatory burden.

| # | Score | Opportunity | Pattern | Niche | Economic event |
|---:|---:|---|---|---|---|
| 1 | 82.2 | Public Tender Change Radar | event_monitor | specialist contractors/consultancies | revenue_won |
| 2 | 82.1 | Vertical Form Backend | vertical_form_backend | web agencies serving one trade | labor_and_revenue |
| 3 | 80.9 | Practice Statement Normalizer | document_normalizer | UK accountants/bookkeepers | labor_saved |
| 4 | 79.4 | Field Service Ops Adapter | workflow_adapter | 3-30 person trade/service firms | revenue_and_labor |
| 5 | 79.2 | Supplier Price List Normalizer | document_normalizer | distributors/installers | labor_and_margin |
| 6 | 78.4 | Xero Practice Ops Adapter | workflow_adapter | UK accountancy practices | labor_saved |
| 7 | 78.3 | UK Business Identity Validation API | api_aggregator | UK B2B onboarding | risk_and_labor |
| 8 | 77.7 | Trade Supplier Invoice Normalizer | document_normalizer | UK trades + bookkeepers | labor_saved |
| 9 | 77.6 | Certification Renewal Radar | event_monitor | SMBs with staff/equipment certifications | loss_prevented |
| 10 | 77.3 | Planning Permit Opportunity Radar | event_monitor | architects/surveyors/installers | revenue_won |
| 11 | 77.3 | Legacy Portal Browser Assistant | browser_extension | one profession / one authorized portal | labor_saved |
| 12 | 74.7 | Data Export Backup for One SaaS | hosted_utility | SMBs using one sticky SaaS | risk_prevented |
| 13 | 74.1 | Specialist Job Board Meta Directory | directory_data_asset | fragmented profession | revenue_won |
| 14 | 74.0 | Hosted Open Source Vertical Primitive | hosted_infra | one professional niche | ops_saved |
| 15 | 73.0 | Niche Verified Vendor Directory | directory_data_asset | high-value specialist procurement | revenue_won |
| 16 | 69.7 | Agency Client Portal Thin Layer | workflow_adapter | small agencies/consultancies | labor_saved |
| 17 | 53.0 | Generic Uptime Monitor | generic_monitor | developers | risk_prevented |
| 18 | 47.7 | Generic Agent Hosting | generic_hosting | AI enthusiasts | ops_saved |
| 19 | 42.9 | Generic PDF Parser | generic_parser | everyone | labor_saved |

## Detail

### Public Tender Change Radar — 82.2/100
- **Niche:** specialist contractors/consultancies
- **Problem:** Firms miss tenders/amendments across public procurement feeds
- **Pattern:** event_monitor
- **Notes:** Use official public feeds/APIs; qualify to should-we-bid alert.

### Vertical Form Backend — 82.1/100
- **Niche:** web agencies serving one trade
- **Problem:** Generic form submissions require manual qualification and CRM entry
- **Pattern:** vertical_form_backend
- **Notes:** Return a structured job/lead object and webhook, not merely email.

### Practice Statement Normalizer — 80.9/100
- **Niche:** UK accountants/bookkeepers
- **Problem:** Recurring statements require manual cleanup before accounting import
- **Pattern:** document_normalizer
- **Notes:** Start with 3 statement types and one Xero/QuickBooks target.

### Field Service Ops Adapter — 79.4/100
- **Niche:** 3-30 person trade/service firms
- **Problem:** Lead->quote->job->follow-up data moves manually across inbox and field system
- **Pattern:** workflow_adapter
- **Notes:** Pick one incumbent + trade + country first.

### Supplier Price List Normalizer — 79.2/100
- **Niche:** distributors/installers
- **Problem:** Weekly supplier files use different SKUs/layouts and require manual merge
- **Pattern:** document_normalizer
- **Notes:** Canonical SKU mapping + price-change alerts.

### Xero Practice Ops Adapter — 78.4/100
- **Niche:** UK accountancy practices
- **Problem:** Staff repeatedly compile client queries, exceptions and evidence around Xero workflows
- **Pattern:** workflow_adapter
- **Notes:** Draft/suggest first; approval before consequential financial changes.

### UK Business Identity Validation API — 78.3/100
- **Niche:** UK B2B onboarding
- **Problem:** Apps combine multiple validations and normalize inconsistent identifiers
- **Pattern:** api_aggregator
- **Notes:** Bundle lawful data sources; UK-native schema is the wedge.

### Trade Supplier Invoice Normalizer — 77.7/100
- **Niche:** UK trades + bookkeepers
- **Problem:** Supplier invoices need line-item/job coding before job-cost/accounting import
- **Pattern:** document_normalizer
- **Notes:** Wedge is supplier-specific layout + job reference handling.

### Certification Renewal Radar — 77.6/100
- **Niche:** SMBs with staff/equipment certifications
- **Problem:** Renewal dates are scattered and missed
- **Pattern:** event_monitor
- **Notes:** Start CSV/manual evidence; integrate sources later.

### Planning Permit Opportunity Radar — 77.3/100
- **Niche:** architects/surveyors/installers
- **Problem:** Local professionals find project opportunities too late
- **Pattern:** event_monitor
- **Notes:** Geo + classification + entity resolution is the moat.

### Legacy Portal Browser Assistant — 77.3/100
- **Niche:** one profession / one authorized portal
- **Problem:** Users retype/copy the same structured fields in a legacy portal
- **Pattern:** browser_extension
- **Notes:** No access-control bypasses; operate inside authorized user session.

### Data Export Backup for One SaaS — 74.7/100
- **Niche:** SMBs using one sticky SaaS
- **Problem:** Businesses want scheduled readable backups but exports are manual
- **Pattern:** hosted_utility
- **Notes:** Official API + customer-owned storage + restore path.

### Specialist Job Board Meta Directory — 74.1/100
- **Niche:** fragmented profession
- **Problem:** Candidates/recruiters search many association/company boards
- **Pattern:** directory_data_asset
- **Notes:** Recruiters/boards fund distribution; candidate side free.

### Hosted Open Source Vertical Primitive — 74.0/100
- **Niche:** one professional niche
- **Problem:** Teams want open-source capability without operating it
- **Pattern:** hosted_infra
- **Notes:** Sell SLA/upgrades/backups/policy/templates rather than generic hosting.

### Niche Verified Vendor Directory — 73.0/100
- **Niche:** high-value specialist procurement
- **Problem:** Buyers cannot filter suppliers by hard operational requirements
- **Pattern:** directory_data_asset
- **Notes:** Monetize verification, leads and featured category only after buyer traffic.

### Agency Client Portal Thin Layer — 69.7/100
- **Niche:** small agencies/consultancies
- **Problem:** Client requests/approvals/files are fragmented across email
- **Pattern:** workflow_adapter
- **Notes:** Integrate existing storage/PM tools; don't become a full PSA.

### Generic Uptime Monitor — 53.0/100
- **Niche:** developers
- **Problem:** Monitor website uptime
- **Pattern:** generic_monitor
- **Notes:** Included deliberately as a lower-scoring commoditized baseline.

### Generic Agent Hosting — 47.7/100
- **Niche:** AI enthusiasts
- **Problem:** Deploy an agent without setup
- **Pattern:** generic_hosting
- **Notes:** Evidence suggests workflow-specific adapters outperform generic hosting.

### Generic PDF Parser — 42.9/100
- **Niche:** everyone
- **Problem:** Extract fields from arbitrary PDFs
- **Pattern:** generic_parser
- **Notes:** Included as a warning: broad AI parsing without workflow ownership is weak.
