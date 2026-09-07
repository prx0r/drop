from __future__ import annotations
from .base import NotConfigured
from ..settings import settings
class VeoAdapter:
    """Builds a Gemini API Veo job spec.
    The official SDK is intentionally optional so the core service remains lightweight.
    """
    def build_job(self, *, prompt:str, reference_images:list[str], aspect_ratio:str="16:9", resolution:str="1080p") -> dict:
        if not settings.gemini_api_key: raise NotConfigured("GEMINI_API_KEY required for execution")
        return {"model":"veo-3.1-generate-preview","prompt":prompt,"reference_images":reference_images[:3],"aspect_ratio":aspect_ratio,"resolution":resolution,"duration_seconds":8}
