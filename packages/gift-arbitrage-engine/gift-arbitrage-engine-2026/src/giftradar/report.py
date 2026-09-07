from __future__ import annotations
from pathlib import Path
import csv, json
from jinja2 import Template

MD_HEAD = """# Gift Arbitrage Radar — ranked opportunities\n\nScores are screening scores, not revenue forecasts. Marketplace review counts and result counts are demand proxies, not unit-sales data. Economics are illustrative until a live fulfillment quote and marketplace fee calculation are supplied.\n\n| Rank | Opportunity | Score | Verdict | Price midpoint | Illustrative GM | Evidence |\n|---:|---|---:|---|---:|---:|---:|\n"""

def write_reports(scores, out_dir: str):
    p = Path(out_dir); p.mkdir(parents=True, exist_ok=True)
    rows = [s.model_dump() for s in scores]
    (p/"ranked.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    with (p/"ranked.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["rank","slug","name","total","verdict","price_mid","cogs_mid","gross_margin_pct","evidence_count","reasons","risks"])
        w.writeheader()
        for i,s in enumerate(scores,1):
            w.writerow({"rank":i,"slug":s.slug,"name":s.name,"total":s.total,"verdict":s.verdict,"price_mid":s.price_mid,"cogs_mid":s.cogs_mid,"gross_margin_pct":s.gross_margin_pct,"evidence_count":s.evidence_count,"reasons":"; ".join(s.reasons),"risks":"; ".join(s.risks)})
    md = [MD_HEAD]
    for i,s in enumerate(scores,1):
        md.append(f"| {i} | {s.name} | {s.total:.1f} | {s.verdict} | ${s.price_mid:.2f} | {s.gross_margin_pct:.0f}% | {s.evidence_count} |")
    md.append("\n## Top-candidate notes\n")
    for i,s in enumerate(scores[:15],1):
        md.append(f"### {i}. {s.name} — {s.total:.1f} / {s.verdict}\n")
        md.append("**Why:** " + "; ".join(s.reasons) + "\n")
        if s.risks: md.append("**Risks:** " + "; ".join(s.risks) + "\n")
    (p/"ranked.md").write_text("\n".join(md), encoding="utf-8")
    tpl = Template('''<!doctype html><html><head><meta charset="utf-8"><title>Gift Arbitrage Radar</title><style>body{font-family:system-ui;max-width:1200px;margin:40px auto;padding:0 20px}table{border-collapse:collapse;width:100%}th,td{padding:9px;border-bottom:1px solid #ddd;text-align:left}.BUILD{font-weight:700}small{color:#555}</style></head><body><h1>Gift Arbitrage Radar — 2026 Q4</h1><p><small>Screening model: demand proof × personalization × AI labor removal × gifting/Q4 × economics × repeatability, penalized for saturation, IP, privacy and support burden.</small></p><table><tr><th>#</th><th>Opportunity</th><th>Score</th><th>Verdict</th><th>Mid price</th><th>Illustrative GM</th><th>Evidence</th></tr>{% for s in scores %}<tr><td>{{loop.index}}</td><td>{{s.name}}</td><td>{{'%.1f'|format(s.total)}}</td><td class="{{s.verdict}}">{{s.verdict}}</td><td>${{'%.2f'|format(s.price_mid)}}</td><td>{{'%.0f'|format(s.gross_margin_pct)}}%</td><td>{{s.evidence_count}}</td></tr>{% endfor %}</table><h2>Top 15</h2>{% for s in scores[:15] %}<h3>{{loop.index}}. {{s.name}}</h3><p>{{s.reasons|join('; ')}}</p>{% if s.risks %}<p><b>Risks:</b> {{s.risks|join('; ')}}</p>{% endif %}{% endfor %}</body></html>''')
    (p/"ranked.html").write_text(tpl.render(scores=scores), encoding="utf-8")
