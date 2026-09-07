#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m giftradar.cli rank --root . --out reports
printf '\nSample product blueprint:\n'
PYTHONPATH=src python -m giftradar.cli spec family-annual-newspaper --root .
