.PHONY: rank test api
rank:
	PYTHONPATH=src python -m giftradar.cli rank --root . --out reports

test:
	PYTHONPATH=src pytest -q

api:
	PYTHONPATH=src uvicorn giftradar.api:app --reload
