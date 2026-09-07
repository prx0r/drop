from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings
class CJAdapter:
    BASE="https://developers.cjdropshipping.com/api2.0/v1"
    def _h(self):
        if not settings.cj_access_token: raise NotConfigured("CJ_ACCESS_TOKEN required")
        return {"CJ-Access-Token":settings.cj_access_token}
    def search_products(self, keyword:str, country_code:str|None=None, start_inventory:int=1, page:int=1, size:int=20):
        params={"page":page,"size":min(size,100),"keyWord":keyword,"startInventory":start_inventory}
        if country_code: params["countryCode"]=country_code
        with httpx.Client(timeout=45) as client: r=client.get(f"{self.BASE}/product/listV2",headers=self._h(),params=params)
        if r.status_code>=400: raise AdapterError(f"CJ {r.status_code}: {r.text[:800]}")
        return r.json()
    def product_details(self, *, pid:str|None=None, sku:str|None=None):
        params={"features":["enable_video"]}
        if pid: params["pid"]=pid
        elif sku: params["productSku"]=sku
        else: raise ValueError("pid or sku required")
        with httpx.Client(timeout=45) as client: r=client.get(f"{self.BASE}/product/query",headers=self._h(),params=params)
        if r.status_code>=400: raise AdapterError(f"CJ {r.status_code}: {r.text[:800]}")
        return r.json()
