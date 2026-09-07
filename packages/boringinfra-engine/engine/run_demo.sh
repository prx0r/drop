#!/usr/bin/env bash
set -euo pipefail
python -m boringinfra.cli seed --db opportunities.db
python -m boringinfra.cli rank --db opportunities.db --limit 20
python -m boringinfra.cli report --db opportunities.db --out ranked_report.md
python -m unittest discover -s tests -v
