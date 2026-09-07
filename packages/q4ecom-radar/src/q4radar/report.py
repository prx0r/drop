from __future__ import annotations

import csv
import html
import json
from pathlib import Path
from .models import ScanResult
from .config import load_products, load_markets


def write_reports(result: ScanResult, out_dir: str, config_dir: str) -> dict[str,str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    products = load_products(config_dir)
    markets = load_markets(config_dir)
    stem = f"scan-{result.run_id}"
    json_path = out / f"{stem}.json"
    csv_path = out / f"{stem}.csv"
    md_path = out / f"{stem}.md"
    html_path = out / f"{stem}.html"
    json_path.write_text(result.model_dump_json(indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        fields = ["rank","market","product","cluster","score","verdict","retail_usd","landed_cost_usd","gross_margin_pct","markup_x","breakeven_cac_usd","reasons","risks","missing_signals"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for i,s in enumerate(result.scores,1):
            p = products[s.product_slug]
            w.writerow({
                "rank":i,"market":s.market,"product":p.name,"cluster":p.cluster,"score":s.total_score,"verdict":s.verdict,
                "retail_usd":s.economics.get("retail_price_gross_usd"),"landed_cost_usd":s.economics.get("landed_cost_usd"),
                "gross_margin_pct":s.economics.get("gross_margin_pct"),"markup_x":s.economics.get("retail_to_landed_markup_x"),
                "breakeven_cac_usd":s.economics.get("breakeven_cac_usd"),"reasons":"; ".join(s.reasons),
                "risks":"; ".join(s.risks),"missing_signals":"; ".join(s.missing_signals),
            })

    lines = [f"# Q4 Ecom Radar — {result.run_id}", "", f"Markets: {', '.join(result.markets)}", f"Sources: {', '.join(result.sources)}", "",
             "> Scores are screening signals, not profit forecasts. Demo-source evidence is synthetic and must not be used to place ad spend.", "",
             "| # | Market | Product | Score | Verdict | Markup | Margin |", "|---:|---|---|---:|---|---:|---:|"]
    for i,s in enumerate(result.scores[:60],1):
        p=products[s.product_slug]
        lines.append(f"| {i} | {markets[s.market].name} | {p.name} | {s.total_score:.1f} | {s.verdict} | {s.economics.get('retail_to_landed_markup_x') or '-'}× | {s.economics.get('gross_margin_pct') or '-'}% |")
    lines += ["", "## Top opportunities"]
    for s in result.scores[:15]:
        p=products[s.product_slug]
        lines += [f"### {p.name} — {markets[s.market].name} — {s.total_score:.1f} {s.verdict}",
                  f"**Why:** {'; '.join(s.reasons)}.", f"**Risks:** {'; '.join(s.risks) if s.risks else 'No major heuristic flag; still perform supplier/IP/compliance checks.'}",
                  f"**Economics:** {json.dumps(s.economics)}", ""]
    md_path.write_text("\n".join(lines), encoding="utf-8")

    rows = []
    for i,s in enumerate(result.scores,1):
        p=products[s.product_slug]
        rows.append(f"<tr><td>{i}</td><td>{html.escape(s.market)}</td><td>{html.escape(p.name)}</td><td>{s.total_score:.1f}</td><td>{s.verdict}</td><td>{s.economics.get('retail_to_landed_markup_x') or ''}</td><td>{s.economics.get('gross_margin_pct') or ''}</td></tr>")
    html_path.write_text(f"""<!doctype html><html><head><meta charset='utf-8'><title>Q4 Ecom Radar</title>
<style>body{{font-family:system-ui;max-width:1100px;margin:40px auto;padding:0 20px}}table{{border-collapse:collapse;width:100%}}td,th{{padding:8px;border-bottom:1px solid #ddd;text-align:left}}th{{position:sticky;top:0;background:white}}.note{{padding:12px;background:#f5f5f5}}</style></head><body>
<h1>Q4 Ecom Radar</h1><p class='note'>Run {html.escape(result.run_id)}. Screening signal only; synthetic demo data is not market evidence.</p>
<table><thead><tr><th>#</th><th>Market</th><th>Product</th><th>Score</th><th>Verdict</th><th>Markup ×</th><th>Gross margin %</th></tr></thead><tbody>{''.join(rows)}</tbody></table></body></html>""", encoding="utf-8")
    return {"json":str(json_path),"csv":str(csv_path),"markdown":str(md_path),"html":str(html_path)}
