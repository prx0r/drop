from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .db import init_db
from .feed import build_feed
from .live_scan import observe_query
from .pipeline import ranked, score_all
from .providers.dataforseo import DataForSEOKeywordProvider
from .providers.serper import SerperShoppingProvider
from .reporting import export_ranked
from .seed import seed_from_csv


def default_seed() -> str:
    return str(Path(__file__).resolve().parents[2] / "data" / "live_screening_candidates.csv")


def main(argv=None):
    p = argparse.ArgumentParser(prog="ecomscan")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    s = sub.add_parser("seed")
    s.add_argument("--csv", default=default_seed())
    s.add_argument("--append", action="store_true")
    sub.add_parser("score")
    r = sub.add_parser("rank")
    r.add_argument("--limit", type=int, default=20)
    r.add_argument("--country")
    r.add_argument("--gate")
    e = sub.add_parser("export")
    e.add_argument("--out", default="ranked.csv")
    e.add_argument("--country")
    o = sub.add_parser("observe")
    o.add_argument("--country", required=True)
    o.add_argument("--query", required=True)
    o.add_argument("--with-keywords", action="store_true", help="also query DataForSEO")
    f = sub.add_parser("feed")
    f.add_argument("--input", required=True)
    f.add_argument("--out", required=True)

    args = p.parse_args(argv)
    if args.cmd == "init":
        init_db(); print(f"initialized {os.getenv('ECSCAN_DB','scanner.sqlite')}")
    elif args.cmd == "seed":
        init_db(); n = seed_from_csv(args.csv, replace=not args.append); print(f"seeded {n} candidates")
    elif args.cmd == "score":
        n = score_all(); print(f"scored {n} candidates")
    elif args.cmd == "rank":
        for row in ranked(limit=args.limit, country=args.country, gate=args.gate):
            econ = json.loads(row["economics_json"])
            print(f"{row['score_total']:6.2f} {row['gate']:17s} {row['country']} | {row['niche'][:26]:26s} | {row['product_name'][:52]:52s} | contribution {econ['contribution_after_ads_local']}")
    elif args.cmd == "export":
        n = export_ranked(args.out, country=args.country); print(f"exported {n} rows to {args.out}")
    elif args.cmd == "observe":
        init_db()
        shopping = SerperShoppingProvider()
        keyword_provider = DataForSEOKeywordProvider() if args.with_keywords else None
        payload = observe_query(query=args.query, country=args.country, shopping=shopping, keywords=keyword_provider)
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.cmd == "feed":
        n = build_feed(args.input, args.out); print(f"validated/exported {n} feed rows to {args.out}")


if __name__ == "__main__":
    main()
