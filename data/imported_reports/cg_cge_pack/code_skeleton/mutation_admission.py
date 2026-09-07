"""Mutation admission guard.

CGE is not trusted. Every proposed patch is checked before a child campaign
version can be created.
"""
from __future__ import annotations

FORBIDDEN_PREFIXES = (
    "/evidence_bindings",
    "/hard_gate_results",
    "/observed_metrics",
    "/rubric",
    "/rubric_version",
)

ALLOWED_BY_FAMILY = {
    "NARROW": ("/atom/generation_scope", "/atom/component_scope"),
    "REROUTE": ("/track", "/distribution_strategy", "/supplier_strategy/transaction_route"),
    "SUPPLY_SWAP": ("/supplier_strategy/candidate_supplier_ids",
                    "/supplier_strategy/transaction_route"),
    "GEOGRAPHIC_TRANSFER": ("/country", "/language",
                            "/supplier_strategy/candidate_supplier_ids"),
    "GRAPH_DEEPEN": ("/atom/component_scope", "/atom/triggers"),
}

def admit(mutation: dict) -> tuple[bool, list[str]]:
    errors = []
    family = mutation["mutation_type"]
    if family == "RESEARCH_ACTION":
        return True, []

    allowed = ALLOWED_BY_FAMILY.get(family, ())
    for op in mutation.get("operations", []):
        path = op["path"]
        if any(path.startswith(p) for p in FORBIDDEN_PREFIXES):
            errors.append(f"forbidden evidence/judge path: {path}")
            continue
        if allowed and not any(path.startswith(p) for p in allowed):
            errors.append(f"path not allowed for {family}: {path}")
    return (not errors), errors
