# What did not go well in v1

The first factory had good business logic and a strong handoff, but its own P0 list revealed the gap: several production basics were deferred instead of implemented. It did not ship a test suite, migration/provenance framework, shared auth/rate limiting, or enough end-to-end money/outcome states. Some apps were closer to algorithm demos than sellable operating kernels.

V2 fixes the most important issues now:
- pinned dependencies
- shared SQLite schema initialization
- request IDs and rate limiting
- admin-token protection for sensitive mutation/export operations
- immutable-ish provenance observations (new rows + content hashes)
- event/outcome ledgers
- deterministic, inspectable scoring
- official live adapters for Planning Data and Contracts Finder
- explicit compliance gate for reactivation
- test suite covering every app and critical failure modes
- static audit script

Still deliberately NOT implemented: payments, mass sending, customer OAuth, full CRM/ERP ingestion, browser scraping, or autonomous legal/compliance decisions. Those create cost/risk before customer proof.
