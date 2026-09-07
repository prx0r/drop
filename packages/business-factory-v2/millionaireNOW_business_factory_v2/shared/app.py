from __future__ import annotations
from fastapi import FastAPI
from .security import RateLimiter


def make_app(title: str) -> FastAPI:
    app = FastAPI(title=title, version="2.0.0")
    app.middleware("http")(RateLimiter())

    @app.get("/health")
    def health():
        return {"ok": True, "app": title, "version": "2.0.0"}
    return app
