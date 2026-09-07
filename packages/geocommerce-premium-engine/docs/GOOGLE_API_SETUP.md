# Google API setup

## Google Ads
Environment:
- `GOOGLE_ADS_API_VERSION=v25`
- `GOOGLE_ADS_CUSTOMER_ID`
- `GOOGLE_ADS_MANAGER_CUSTOMER_ID` (if applicable)
- `GOOGLE_ADS_DEVELOPER_TOKEN`
- `GOOGLE_ADS_ACCESS_TOKEN`

The adapter uses documented REST endpoints and an already-issued OAuth access token. In production, add an OAuth refresh-token service rather than putting long-lived refresh secrets into this app.

`POST /v1/integrations/google-ads/historical` uses each market's Google geo target and language ID.

## Merchant API
Environment:
- `MERCHANT_ACCOUNT_ID`
- `MERCHANT_ACCESS_TOKEN`

The adapter calls:
`POST https://merchantapi.googleapis.com/reports/v1/accounts/{ACCOUNT_ID}/reports:search`

Market Insights eligibility is not guaranteed. Gracefully fall back to Ads keyword data + supplier data + optional licensed Shopping SERP evidence.

## Monetary normalization
Do not compare:
- DataForSEO CPC in USD;
- supplier cost in EUR;
- Norwegian benchmark price in NOK.

Convert all money to `market.currency` with a timestamped FX source before calling the opportunity scorer. The scorer deliberately hard-rejects currency mismatch.
