import argparse, html, json
from pathlib import Path
from urllib.parse import quote
from validate import validate

ROOT=Path(__file__).parent
DATA=ROOT/'data'/'listings.json'
DIST=ROOT/'dist'

def esc(x): return html.escape(str(x), quote=True)

def shell(title, body, indexable=False):
    robots='index,follow' if indexable else 'noindex,nofollow'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="{robots}"><title>{esc(title)}</title><style>body{{font-family:system-ui,sans-serif;max-width:900px;margin:40px auto;padding:0 16px;line-height:1.55}}.card{{border:1px solid #ddd;border-radius:12px;padding:16px;margin:12px 0}}.meta{{color:#666;font-size:.9rem}}.sponsor{{font-size:.75rem;border:1px solid #999;padding:2px 6px;border-radius:999px}}a{{color:inherit}}</style></head><body>{body}</body></html>'''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--publish', action='store_true')
    ap.add_argument('--base-url', default='https://example.com')
    args=ap.parse_args()
    records=json.loads(DATA.read_text())
    errors=validate(records, publishing=args.publish)
    if errors:
        raise SystemExit('\n'.join('ERROR: '+e for e in errors))
    DIST.mkdir(exist_ok=True)
    (DIST/'listing').mkdir(exist_ok=True)
    cards=[]
    urls=['/']
    for r in records:
        badge=' <span class="sponsor">Sponsored</span>' if r['is_sponsored'] else ''
        cards.append(f'''<div class="card"><h2><a href="listing/{quote(r['id'])}.html">{esc(r['name'])}</a>{badge}</h2><div class="meta">{esc(r['category'])} · {esc(r['region'])}</div><p>{esc(r['summary'])}</p><div class="meta">Verified {esc(r['last_verified'])}</div></div>''')
        attrs=''.join(f'<li><strong>{esc(k.replace("_"," ").title())}:</strong> {esc(v)}</li>' for k,v in r.get('attributes',{}).items())
        body=f'''<p><a href="../index.html">← All listings</a></p><h1>{esc(r['name'])}{badge}</h1><p>{esc(r['summary'])}</p><ul>{attrs}</ul><p class="meta">Category: {esc(r['category'])}<br>Region: {esc(r['region'])}<br>Last verified: {esc(r['last_verified'])}</p><p><a rel="nofollow" href="{esc(r['source_url'])}">Primary source</a></p>'''
        out=DIST/'listing'/f"{r['id']}.html"
        out.write_text(shell(r['name'],body,args.publish),encoding='utf-8')
        urls.append(f"/listing/{r['id']}.html")
    index_body='<h1>Verified Directory Demo</h1><p>This starter is noindex by default. Replace sample data with real sourced records before publishing.</p>'+''.join(cards)
    (DIST/'index.html').write_text(shell('Verified Directory Demo', index_body,args.publish),encoding='utf-8')
    if args.publish:
        robots='User-agent: *\nAllow: /\nSitemap: '+args.base_url.rstrip('/')+'/sitemap.xml\n'
    else:
        robots='User-agent: *\nDisallow: /\n'
    (DIST/'robots.txt').write_text(robots,encoding='utf-8')
    sitemap=''.join(f'<url><loc>{esc(args.base_url.rstrip("/")+u)}</loc></url>' for u in urls)
    (DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+sitemap+'</urlset>',encoding='utf-8')
    print(f'Built {len(records)} listings in {DIST} (publish={args.publish}).')

if __name__=='__main__': main()
