from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings
class RunwayAdapter:
    BASE="https://api.dev.runwayml.com"
    VERSION="2024-11-06"
    def _h(self):
        if not settings.runway_api_key: raise NotConfigured("RUNWAY_API_KEY required")
        return {"Authorization":f"Bearer {settings.runway_api_key}","X-Runway-Version":self.VERSION,"Content-Type":"application/json"}
    def image_to_video(self,image_url:str,prompt:str,duration:int=5,model:str="gen4.5",ratio:str="1280:720"):
        body={"promptImage":image_url,"promptText":prompt,"model":model,"ratio":ratio,"duration":duration}
        with httpx.Client(timeout=45) as client: r=client.post(f"{self.BASE}/v1/image_to_video",headers=self._h(),json=body)
        if r.status_code>=400: raise AdapterError(f"Runway {r.status_code}: {r.text[:800]}")
        return r.json()
