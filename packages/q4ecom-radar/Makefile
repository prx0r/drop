.PHONY: install test demo serve
install:
	python -m pip install -e '.[dev]'
test:
	pytest -q
demo:
	q4radar scan --markets GB,NO,DK,SE,DE,NL,CH --demo
serve:
	q4radar serve --host 0.0.0.0 --port 8765
