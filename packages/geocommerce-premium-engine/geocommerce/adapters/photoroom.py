from __future__ import annotations

import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings


class PhotoroomAdapter:
    """Truth-preserving catalog image normalization via Photoroom Image Editing v2.

    Default mode deliberately avoids generative subject edits. It removes/replaces the
    background, normalizes padding, and adds a soft shadow while preserving the actual SKU.
    """
    URL = "https://image-api.photoroom.com/v2/edit"

    def _headers(self) -> dict[str, str]:
        if not settings.photoroom_api_key:
            raise NotConfigured("PHOTOROOM_API_KEY required")
        return {"x-api-key": settings.photoroom_api_key}

    def packshot_from_url(self, image_url: str, *, background: str = "FFFFFF", size: str = "1200x1200") -> bytes:
        params = {
            "imageUrl": image_url,
            "removeBackground": "true",
            "background.color": background,
            "outputSize": size,
            "padding": "0.10",
            "shadow.mode": "ai.soft",
            "export.format": "webp",
        }
        with httpx.Client(timeout=60) as client:
            r = client.get(self.URL, headers=self._headers(), params=params)
        if r.status_code >= 400:
            raise AdapterError(f"Photoroom {r.status_code}: {r.text[:800]}")
        return r.content
