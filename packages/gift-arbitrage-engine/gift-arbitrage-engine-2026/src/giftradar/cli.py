from __future__ import annotations
from pathlib import Path
import json
import typer
from .pipeline import Radar
from .report import write_reports
from .gift_specs import build_spec
from .models import GiftSpecRequest

app = typer.Typer(no_args_is_help=True)

def radar(root: str) -> Radar:
    r = Path(root)
    return Radar(str(r/"config"), str(r/"data"/"evidence.yml"))

@app.command()
def rank(root: str = ".", out: str = "reports"):
    scores = radar(root).rank()
    write_reports(scores, str(Path(root)/out))
    for i,s in enumerate(scores[:20],1):
        typer.echo(f"{i:2d}. {s.total:5.1f} {s.verdict:5s}  {s.name}")

@app.command()
def spec(slug: str, root: str = "."):
    r = radar(root)
    o = r.opportunities[slug]
    req = GiftSpecRequest(opportunity_slug=slug)
    typer.echo(json.dumps(build_spec(o, req).model_dump(), indent=2))

@app.command()
def evidence(key: str, root: str = "."):
    e = radar(root).evidence[key]
    typer.echo(json.dumps(e.model_dump(), indent=2))

if __name__ == "__main__": app()
