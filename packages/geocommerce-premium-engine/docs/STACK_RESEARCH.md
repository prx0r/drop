# Tool stack research

## Core: own the product truth
The engine, not a third-party dropshipping app, is the source of truth. Third-party tools are adapters for sourcing, importing, fulfillment, research or creative production.

## Google Ads API
Use KeywordPlanIdeaService for country/language keyword discovery and historical metrics. Current official samples reference v25 and raw REST calls of the form:
`POST https://googleads.googleapis.com/v25/customers/{CUSTOMER_ID}:generateKeywordIdeas`
Historical metrics provide average monthly searches, competition index, and low/high top-of-page bid percentiles. Cache monthly.

## Merchant API
`POST https://merchantapi.googleapis.com/reports/v1/accounts/{ACCOUNT_ID}/reports:search`
Use MCQL for best sellers, price competitiveness, product issues, performance and competitive visibility. Market Insights requires account eligibility, so the engine can also operate with Google Ads + supplier + licensed SERP evidence before eligibility.

## DataForSEO
Useful for bulk country/language keyword data. Its Google Ads search-volume endpoint accepts location/language and up to 1,000 keywords in a live request. Treat it as secondary evidence and normalize returned monetary fields before comparing with local prices.

## SerpApi
Useful for literal Google Shopping snapshots with location/gl/hl controls. This is optional because official Google APIs already provide much of the economic signal.

## Kopy
Kopy publicly supports importing product pages from several ecommerce platforms, translation and AI copy/page generation. No dependable public developer API was found in this research. The repo therefore exports a Kopy handoff manifest rather than inventing an endpoint or automating its UI.

## AutoDS
AutoDS added an approval-gated API in 2026. Public documentation says it supports product imports, automated orders, sourcing and product data. Access requires application/approval and an activation fee. Implement after credentials/docs are issued; do not reverse-engineer private endpoints.

## CJdropshipping
CJ exposes public developer APIs for product search, product details, inventory and orders. The codebase includes a real product-search adapter using documented API2 endpoints. This is useful for broad discovery, but premium products should still pass sample, warranty and supplier-quality gates.

## Shopify Markets
Shopify's 2026 Storefront/Admin APIs support market-aware countries, currencies, languages, translations and market web presences. Use one product/canonical truth layer and publish market-specific content/price experiences. Duties/taxes require HS code and origin data for accurate calculation.

## Support
Gorgias AI Agent can answer pre/post-purchase questions and hand over to a human on Shopify. Tidio similarly supports catalog-aware product recommendations, multilingual support and video calls. The repo keeps its own guarded advisor/support API so a store can start cheaply and later attach Gorgias/Tidio.

## Voice escalation
Twilio Programmable Voice supports outbound calls and status callbacks. Use this for “request a call” escalation, not autonomous sales calls without appropriate consent/compliance.

## AI video/media
Runway now exposes dedicated Product Ad and Product UGC recipes and general image-to-video APIs. Veo 3.1 supports up to three reference images and image-to-video, including 1080p/4K options. Use reference images + a verification QA gate; synthetic media must not demonstrate nonexistent product behavior.

OpenAI Sora should not be a new dependency here: OpenAI currently states that the Sora API is scheduled to shut down on 2026-09-24.

## Source URLs
- Kopy: https://www.kopy.app/
- AutoDS API: https://help.autods.com/en/articles/12699964-autods-api-feature-automate-product-imports-orders-and-sourcing
- CJ product API: https://developers.cjdropshipping.com/en/api/api2/api/product.html
- Shopify localization: https://shopify.dev/docs/api/storefront/latest/objects/Localization
- Shopify translations: https://shopify.dev/docs/api/admin-graphql/latest/mutations/translationsRegister
- Runway Product Ad: https://docs.dev.runwayml.com/recipes/product-ad/
- Runway Product UGC: https://docs.dev.runwayml.com/recipes/product-ugc/
- Veo 3.1: https://ai.google.dev/gemini-api/docs/veo
- Gorgias AI Agent: https://www.gorgias.com/ai-agent
- Tidio Shopify: https://www.tidio.com/integrations/shopify/
- Twilio Voice: https://www.twilio.com/docs/voice/api
