PYTHON ?= python
DB ?= scanner.sqlite

install:
	$(PYTHON) -m pip install -e '.[dev]'

test:
	PYTHONPATH=src $(PYTHON) -m pytest -q

demo:
	ECSCAN_DB=$(DB) PYTHONPATH=src $(PYTHON) -m nordic_arbitrage.cli init
	ECSCAN_DB=$(DB) PYTHONPATH=src $(PYTHON) -m nordic_arbitrage.cli seed
	ECSCAN_DB=$(DB) PYTHONPATH=src $(PYTHON) -m nordic_arbitrage.cli score
	ECSCAN_DB=$(DB) PYTHONPATH=src $(PYTHON) -m nordic_arbitrage.cli rank --limit 20

serve:
	ECSCAN_DB=$(DB) PYTHONPATH=src uvicorn nordic_arbitrage.api:app --host 0.0.0.0 --port 8080
