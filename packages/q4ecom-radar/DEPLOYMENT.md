# Deployment / Production Checklist

## 1. Credentials

Populate `.env` with only the adapters you can access. Never commit `.env`.

Minimum recommended live stack:

- Google Ads API credentials
- CJ access token
- SerpApi key

## 2. Initial validation

```bash
pip install -e '.[google,dev]'
pytest -q
q4radar show-sources
q4radar scan --markets GB,NO,DK --products compression-packing-cubes,espresso-accessory-bundle,dog-car-hammock,boot-dryer
```

Inspect the newest `reports/scan-*.md` and `reports/scan-*.csv`.

## 3. API deployment

Docker:

```bash
docker compose up -d --build
curl http://localhost:8765/health
```

Put a reverse proxy/auth layer in front of `/scan` if exposed to the internet; scans consume paid API quota.

## 4. Scheduling

Start once daily. Only increase cadence when data changes quickly enough to justify quota/cost.

```cron
15 6 * * * cd /opt/q4ecom-radar-2026 && .venv/bin/q4radar scan --markets GB,NO,DK,SE,DE,NL,CH >> data/cron.log 2>&1
```

## 5. Feedback loop

After a real product test, add actual measurements to a CSV or build another source adapter:

- impressions
- clicks
- CTR
- CPC
- add-to-cart rate
- checkout rate
- conversion rate
- AOV
- refunds/returns
- realized shipping time
- realized contribution margin

Do not tune weights based on one test. After 20–50 resolved hypotheses, fit/calibrate the score against actual contribution/profit outcomes.

## 6. Q4 guardrails

Before moving a product from `TEST` to serious spend:

- sample physically inspected
- delivery time verified to target country
- VAT/customs path confirmed
- product safety documentation checked
- trademark/design/patent screen performed
- returns address/process workable
- checkout displays total price and delivery truthfully
- at least one differentiated creative and product-page angle
- no fake urgency, reviews or savings claims
