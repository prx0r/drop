from __future__ import annotations
import httpx
from datetime import date, timedelta
from .base import NotConfigured, AdapterError
from ..settings import settings

class MerchantReportsAdapter:
    BASE = "https://merchantapi.googleapis.com/reports/v1"
    def _auth(self):
        if not settings.merchant_account_id or not settings.merchant_access_token:
            raise NotConfigured("MERCHANT_ACCOUNT_ID and MERCHANT_ACCESS_TOKEN are required")
        return {"Authorization": f"Bearer {settings.merchant_access_token}", "Content-Type":"application/json"}
    def search(self, query: str, page_size: int = 1000) -> list[dict]:
        url = f"{self.BASE}/accounts/{settings.merchant_account_id}/reports:search"
        results, token = [], None
        with httpx.Client(timeout=45) as client:
            while True:
                body = {"query": query, "pageSize": min(page_size, 1000)}
                if token: body["pageToken"] = token
                r = client.post(url, headers=self._auth(), json=body)
                if r.status_code >= 400:
                    raise AdapterError(f"Merchant API {r.status_code}: {r.text[:800]}")
                data = r.json(); results.extend(data.get("results", [])); token = data.get("nextPageToken")
                if not token: break
        return results
    def best_sellers(self, country: str, category_id: str | None = None, granularity: str = "WEEKLY", report_date: str | None = None) -> list[dict]:
        # Google's weekly examples require an explicit report_date. Default to the
        # previous completed Monday rather than pretending today's partial week is final.
        if report_date is None:
            today = date.today()
            this_monday = today - timedelta(days=today.weekday())
            report_date = (this_monday - timedelta(days=7)).isoformat()
        fields = "report_date, report_granularity, report_country_code, report_category_id, title, brand, rank, previous_rank, relative_demand, previous_relative_demand, relative_demand_change, variant_gtins, inventory_status, brand_inventory_status"
        where = [f"report_date = '{report_date}'", f"report_granularity = '{granularity}'", f"report_country_code = '{country}'"]
        if category_id: where.append(f"report_category_id = {category_id}")
        q = f"SELECT {fields} FROM best_sellers_product_cluster_view WHERE " + " AND ".join(where) + " ORDER BY rank ASC LIMIT 500"
        return self.search(q)
    def price_competitiveness(self, country: str) -> list[dict]:
        q = f"SELECT id, offer_id, title, brand, price, report_country_code, benchmark_price FROM price_competitiveness_product_view WHERE report_country_code = '{country}' LIMIT 1000"
        return self.search(q)
