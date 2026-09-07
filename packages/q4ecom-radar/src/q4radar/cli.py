from __future__ import annotations

import os
from pathlib import Path
import typer
from .pipeline import Scanner
from .report import write_reports
from .database import Database
from .sources import DemoSource, GoogleAdsKeywordSource, GoogleTrendsAlphaSource, SerpApiShoppingSource, SerpApiTrendsSource, CJSource, MetaAdLibrarySource, CSVObservationSource

app = typer.Typer(help="Q4 ecommerce opportunity scanner")


def _cfg() -> str: return os.getenv("Q4RADAR_CONFIG_DIR", "config")
def _dbp() -> str: return os.getenv("Q4RADAR_DB", "data/q4radar.sqlite3")


def _sources(demo: bool, csv_file: str | None):
    if demo:
        src = [DemoSource()]
    else:
        candidates = [GoogleAdsKeywordSource(), GoogleTrendsAlphaSource(), SerpApiTrendsSource(), SerpApiShoppingSource(), CJSource(), MetaAdLibrarySource()]
        src = [x for x in candidates if getattr(x, "enabled", True)]
    if csv_file:
        src.append(CSVObservationSource(csv_file))
    return src


@app.command("init-db")
def init_db():
    Database(_dbp())
    typer.echo(f"Initialized {_dbp()}")


@app.command()
def scan(
    markets: str = typer.Option("GB,NO,DK", help="Comma-separated ISO country codes"),
    products: str = typer.Option("", help="Optional comma-separated product slugs"),
    demo: bool = typer.Option(False, help="Use deterministic synthetic data; never treat as market evidence"),
    csv_file: str = typer.Option("", help="Optional observation CSV to merge"),
    out_dir: str = typer.Option("reports", help="Report output directory"),
):
    market_codes=[x.strip().upper() for x in markets.split(",") if x.strip()]
    product_slugs=[x.strip() for x in products.split(",") if x.strip()] or None
    sources=_sources(demo, csv_file or None)
    if not sources:
        raise typer.BadParameter("No live source credentials configured. Use --demo or provide an observation CSV.")
    scanner=Scanner(_cfg(),_dbp(),sources)
    result=scanner.run(market_codes,product_slugs)
    paths=write_reports(result,out_dir,_cfg())
    typer.echo(f"Run: {result.run_id}")
    for s in result.scores[:15]: typer.echo(f"{s.market:2} {s.total_score:5.1f} {s.verdict:6} {s.product_slug}")
    for k,v in paths.items(): typer.echo(f"{k}: {v}")


@app.command()
def serve(host: str="127.0.0.1", port: int=8765):
    import uvicorn
    uvicorn.run("q4radar.api:app", host=host, port=port, reload=False)


@app.command("show-sources")
def show_sources():
    items=[GoogleAdsKeywordSource(), GoogleTrendsAlphaSource(), SerpApiTrendsSource(), SerpApiShoppingSource(), CJSource(), MetaAdLibrarySource()]
    for x in items: typer.echo(f"{x.name:30} {'ENABLED' if getattr(x,'enabled',True) else 'disabled'}")


if __name__ == "__main__": app()
