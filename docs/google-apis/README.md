# Google API Docs — Drop Project

## APIs We're Using

### 1. Merchant API (LIVE)
- **Docs:** https://developers.google.com/merchant/api
- **Quickstart:** https://developers.google.com/merchant/api/guides/quickstart
- **Auth:** OAuth 2.0 with `https://www.googleapis.com/auth/content` scope
- **Account:** 5849184805 (Moltwork)
- **Status:** Registered, API developer role assigned

**Key endpoints:**
- `GET /accounts/v1/accounts/{id}` — account info
- `GET /accounts/v1/accounts/{id}/productInputs` — list products
- `POST /accounts/v1/accounts/{id}/productInputs` — insert product
- `GET /datasources/v1/accounts/{id}/dataSources` — list data sources
- `POST /accounts/v1/accounts/{id}/developerRegistration:registerGcp` — register GCP project

### 2. Google Ads API (TEST MODE)
- **Docs:** https://developers.google.com/google-ads/api
- **Quickstart:** https://developers.google.com/google-ads/api/docs/get-started
- **Auth:** OAuth 2.0 with `https://www.googleapis.com/auth/adwords` scope
- **Account:** 3775149829
- **Status:** Developer token pending Standard access
- **Config:** `/root/google-ads.yaml`

**Key endpoints:**
- `GoogleAdsService.SearchStream` — query campaigns/keywords
- `KeywordPlanIdeaService.GenerateKeywordIdeas` — keyword research
- `CustomerService.ListAccessibleCustomers` — list accounts

### 3. BigQuery API (LIVE)
- **Docs:** https://docs.cloud.google.com/bigquery
- **Auth:** OAuth 2.0 with `https://www.googleapis.com/auth/cloud-platform` scope
- **Project:** project-ff2366d2-8fda-4fcb-9ba
- **Dataset:** `drop`
- **Tables:** sources, case_studies, products, keyword_data, competitor_data, operator_events, popular_products

**Key endpoints:**
- `GET /bigquery/v2/projects/{project}/datasets` — list datasets
- `POST /bigquery/v2/projects/{project}/queries` — run SQL
- `POST /bigquery/v2/projects/{project}/datasets/{dataset}/tables` — create table
- `POST /bigquery/v2/projects/{project}/datasets/{dataset}/tables/{table}/insertAll` — insert rows

## Credential Files

| File | Purpose |
|------|---------|
| `/root/google-ads.yaml` | Google Ads Python client config |
| `/root/drop/secrets/oauth-tokens.json` | OAuth access/refresh tokens |
| `/root/drop/secrets/client-secrets.json` | OAuth client secrets |

## Token Refresh

```python
import json, urllib.parse, urllib.request

data = urllib.parse.urlencode({
    "client_id": "<CLIENT_ID>",
    "client_secret": "<CLIENT_SECRET>",
    "refresh_token": "<REFRESH_TOKEN>",
    "grant_type": "refresh_token",
}).encode()

req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
resp = urllib.request.urlopen(req)
tokens = json.loads(resp.read())
# tokens["access_token"] — valid for ~1 hour
```

## Pending Actions

1. **Apply for Google Ads Standard access** — unlocks Keyword Planner, Auction Insights, real campaigns
2. **Insert products via Merchant API** — populate the product feed
3. **Set up scheduled data pulls** — automate Popular Products, competitor data
