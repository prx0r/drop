from __future__ import annotations
import hashlib
import hmac
import os
import time
from collections import defaultdict, deque
from fastapi import Header, HTTPException, Request


def require_admin(x_admin_token: str | None = Header(default=None)) -> None:
    expected = os.getenv("ADMIN_TOKEN")
    if not expected:
        raise HTTPException(status_code=503, detail="admin endpoints disabled until ADMIN_TOKEN is configured")
    if not x_admin_token or not hmac.compare_digest(x_admin_token, expected):
        raise HTTPException(status_code=401, detail="invalid admin token")

class RateLimiter:
    def __init__(self, requests: int = 120, window_seconds: int = 60):
        self.requests = requests
        self.window_seconds = window_seconds
        self.buckets: dict[str, deque[float]] = defaultdict(deque)

    async def __call__(self, request: Request, call_next):
        now = time.monotonic()
        ip = request.client.host if request.client else "unknown"
        bucket = self.buckets[ip]
        while bucket and bucket[0] <= now - self.window_seconds:
            bucket.popleft()
        if len(bucket) >= self.requests:
            raise HTTPException(status_code=429, detail="rate limit exceeded")
        bucket.append(now)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request.headers.get("X-Request-ID") or hashlib.sha256(f"{ip}:{now}".encode()).hexdigest()[:16]
        return response
