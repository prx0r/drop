from .scoring import score


def markdown_report(ops, limit=50):
    ranked = sorted(ops, key=score, reverse=True)[:limit]
    lines = [
        "# Ranked boring-infra opportunities", "",
        "Score prioritizes verified demand, workflow value, recurrence, WTP, simplicity, data access and distribution, then penalizes platform/support/regulatory burden.", "",
        "| # | Score | Opportunity | Pattern | Niche | Economic event |",
        "|---:|---:|---|---|---|---|"
    ]
    for i, op in enumerate(ranked, 1):
        lines.append(f"| {i} | {score(op):.1f} | {op.name} | {op.pattern} | {op.niche} | {op.economic_event} |")
    lines += ["", "## Detail", ""]
    for op in ranked:
        lines += [
            f"### {op.name} — {score(op):.1f}/100",
            f"- **Niche:** {op.niche}",
            f"- **Problem:** {op.problem}",
            f"- **Pattern:** {op.pattern}",
            f"- **Notes:** {op.notes}", ""
        ]
    return "\n".join(lines)
