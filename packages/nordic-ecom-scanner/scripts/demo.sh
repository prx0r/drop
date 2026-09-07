#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export ECSCAN_DB="${ECSCAN_DB:-./scanner_demo.sqlite}"
python -m nordic_arbitrage.cli init
python -m nordic_arbitrage.cli seed
python -m nordic_arbitrage.cli score
python -m nordic_arbitrage.cli rank --limit 15
python -m nordic_arbitrage.cli export --out ranked_opportunities.csv
