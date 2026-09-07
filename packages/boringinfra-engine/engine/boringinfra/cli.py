import argparse
import json
from pathlib import Path
from .db import connect, upsert, all_ops
from .seeds import SEEDS
from .scoring import score, score_breakdown
from .importers import import_csv
from .report import markdown_report

RECIPES = {
"document_normalizer": {
  "shape":"one recurring ugly input -> deterministic clean output",
  "mvp":["one input format","one target schema","preview/validation","export","saved mapping"],
  "pricing":"per document or £19-£199/month",
  "moat":"edge-case corpus, mappings, target integrations"
},
"workflow_adapter": {
  "shape":"one sticky incumbent -> five high-frequency expert jobs",
  "mvp":["OAuth/API","domain objects","dry run","validation","approval","activity log"],
  "pricing":"£20-£100/user/month or workspace pricing",
  "moat":"safe execution + workflow knowledge"
},
"event_monitor": {
  "shape":"valuable external event -> precise low-latency alert",
  "mvp":["lawful sources","normalize","classify","dedupe","email/Slack/webhook","feedback"],
  "pricing":"£49-£499/month depending on event value",
  "moat":"coverage, precision, latency, workflow integration"
},
"api_aggregator": {
  "shape":"many suppliers -> one schema, balance and invoice",
  "mvp":["common schema","routing","retry/fallback","metering","audit log"],
  "pricing":"subscription + credits/usage",
  "moat":"compatibility + reliability + billing simplicity"
},
"directory_data_asset": {
  "shape":"fragmented market -> buyer decision surface -> supplier-funded distribution",
  "mvp":["taxonomy","100-500 entities","hard filters","claim/update","analytics"],
  "pricing":"featured placement, verification, sponsorship, leads",
  "moat":"structured data + buyer audience + freshness"
},
"browser_extension": {
  "shape":"existing portal -> fewer repetitive clicks/data transfers",
  "mvp":["context detection","local extraction","autofill/validate","audit note"],
  "pricing":"£10-£50/user/month",
  "moat":"workflow-native convenience"
},
}


def cmd_seed(args):
    conn=connect(args.db)
    for op in SEEDS: upsert(conn, op)
    print(f"Seeded {len(SEEDS)} opportunities into {args.db}")


def cmd_rank(args):
    conn=connect(args.db)
    ops=sorted(all_ops(conn), key=score, reverse=True)[:args.limit]
    for i, op in enumerate(ops, 1):
        print(f"{i:2d}. {score(op):5.1f}  {op.name}  [{op.niche}]")
        if args.explain:
            print(json.dumps(score_breakdown(op), indent=2))


def cmd_report(args):
    conn=connect(args.db)
    text=markdown_report(all_ops(conn), args.limit)
    Path(args.out).write_text(text, encoding='utf-8')
    print(args.out)


def cmd_import(args):
    conn=connect(args.db)
    n=import_csv(args.csv, conn)
    print(f"Imported {n} rows")


def cmd_transplant(args):
    r=RECIPES.get(args.pattern)
    if not r:
        print("Known patterns:", ", ".join(sorted(RECIPES)))
        raise SystemExit(2)
    out={
      "niche":args.niche,
      "pattern":args.pattern,
      **r,
      "interview_questions":[
        f"Show me the actual file/page/system used for this job in {args.niche}.",
        "How often do you do it and how many minutes does it take?",
        "What happens when it is late or wrong?",
        "What exact output do you need next?",
        "Would you pay to have the result delivered automatically?"
      ],
      "first_test":"perform the job manually for 3 prospects and charge at least one before automating"
    }
    print(json.dumps(out, indent=2))


def build_parser():
    p=argparse.ArgumentParser(prog="boringinfra")
    sub=p.add_subparsers(required=True)
    s=sub.add_parser("seed"); s.add_argument("--db", default="opportunities.db"); s.set_defaults(func=cmd_seed)
    r=sub.add_parser("rank"); r.add_argument("--db", default="opportunities.db"); r.add_argument("--limit", type=int, default=30); r.add_argument("--explain", action="store_true"); r.set_defaults(func=cmd_rank)
    m=sub.add_parser("report"); m.add_argument("--db", default="opportunities.db"); m.add_argument("--out", default="ranked_report.md"); m.add_argument("--limit", type=int, default=50); m.set_defaults(func=cmd_report)
    i=sub.add_parser("import-csv"); i.add_argument("csv"); i.add_argument("--db", default="opportunities.db"); i.set_defaults(func=cmd_import)
    t=sub.add_parser("transplant"); t.add_argument("--pattern", required=True); t.add_argument("--niche", required=True); t.set_defaults(func=cmd_transplant)
    return p


def main():
    args=build_parser().parse_args(); args.func(args)

if __name__ == "__main__": main()
