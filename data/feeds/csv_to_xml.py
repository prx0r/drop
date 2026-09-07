#!/usr/bin/env python3
"""Convert CSV feeds to Google Merchant XML format."""
import csv, sys, os

def csv_to_xml(csv_path, xml_path, channel_title, channel_link):
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        products = list(reader)
    
    items = []
    for p in products:
        price_val = p.get('price', '0.00 EUR').split()[0]
        currency = 'EUR' if 'EUR' in p.get('price', '') else 'NOK'
        shipping_price = p.get('shipping_price', '0.00 EUR').split()[0]
        
        item = f"""<item>
  <g:id>{p.get('id', '')}</g:id>
  <g:title>{p.get('title', '')}</g:title>
  <g:description>{p.get('description', '')}</g:description>
  <g:link>{p.get('link', '')}</g:link>
  <g:image_link>{p.get('image_link', '')}</g:image_link>
  <g:availability>{p.get('availability', 'in_stock')}</g:availability>
  <g:condition>{p.get('condition', 'new')}</g:condition>
  <g:price>{price_val} {currency}</g:price>
  <g:brand>{p.get('brand', '')}</g:brand>
  <g:gtin>{p.get('gtin', '')}</g:gtin>
  <g:mpn>{p.get('mpn', '')}</g:mpn>
  <g:product_type>{p.get('product_type', '')}</g:product_type>
</item>"""
        items.append(item)
    
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
<channel>
<title>{channel_title}</title>
<link>{channel_link}</link>
<description>Product feed for {channel_title}</description>
{''.join(items)}
</channel>
</rss>"""
    
    with open(xml_path, 'w') as f:
        f.write(xml)
    print(f"[OK] {csv_path} → {xml_path} ({len(products)} products)")

if __name__ == "__main__":
    base = "/root/drop/data/feeds"
    feeds = [
        ("robot_vacuums_fi.csv", "robot_vacuums_fi.xml", "Robot Vacuums Finland", "https://moltwork.com/robotvacuum"),
        ("ev_chargers_fi.csv", "ev_chargers_fi.xml", "EV Chargers Finland", "https://moltwork.com/ev-charger"),
        ("air_purifiers_fi.csv", "air_purifiers_fi.xml", "Air Purifiers Finland", "https://moltwork.com/saastopuhdistin"),
        ("sleeping_bags_no.csv", "sleeping_bags_no.xml", "Sleeping Bags Norway", "https://moltwork.com/sovepose"),
        ("davis_norway_products.csv", "davis_norway_products.xml", "Davis Weather Stations Norway", "https://moltwork.com/davis"),
        ("heat_pumps_fi.csv", "heat_pumps_fi.xml", "Heat Pumps Finland", "https://moltwork.com/lampopumppu"),
    ]
    for csv_file, xml_file, title, link in feeds:
        csv_to_xml(os.path.join(base, csv_file), os.path.join(base, xml_file), title, link)
