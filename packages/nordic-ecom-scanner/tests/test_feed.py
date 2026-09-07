import csv
from nordic_arbitrage.feed import build_feed


def test_build_feed(tmp_path):
    src = tmp_path / "in.csv"
    out = tmp_path / "out.csv"
    fields = ["id","title","description","link","image_link","availability","price","brand"]
    with src.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerow({
            "id":"x1","title":"Handle","description":"Solid handle","link":"https://x.test/p/1",
            "image_link":"https://x.test/i.jpg","availability":"in_stock","price":"199 NOK","brand":"Example"
        })
    assert build_feed(str(src), str(out)) == 1
    assert out.exists()
