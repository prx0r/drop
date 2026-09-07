.PHONY: install seed test audit run demo
install:
	python -m pip install -r requirements.txt
seed:
	python scripts/seed_demo.py
test:
	pytest -q
audit:
	python scripts/audit.py
run:
	uvicorn geocommerce.app:app --reload --port 8080
demo: seed
	python scripts/scan_demo.py
