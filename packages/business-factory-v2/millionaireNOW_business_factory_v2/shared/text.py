from __future__ import annotations
import re

WORD_RE = re.compile(r"[a-z0-9]+")

def tokens(text: str) -> set[str]:
    return set(WORD_RE.findall((text or "").lower()))

def overlap_score(text: str, desired: list[str]) -> float:
    if not desired:
        return 0.5
    hay = tokens(text)
    wants = set()
    for item in desired:
        wants |= tokens(item)
    if not wants:
        return 0.5
    return len(hay & wants) / len(wants)

def clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, v))
