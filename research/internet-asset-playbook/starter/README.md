# Minimal Directory Starter

This is intentionally boring: a dependency-free Python static-site generator.

It demonstrates the correct architecture for validating a niche before installing a large framework.

## Features

- reads structured listings from JSON;
- requires source URL and verification date;
- generates index and detail pages;
- generates sitemap and robots.txt;
- defaults to `noindex` / blocked crawling until you explicitly publish;
- refuses `--publish` if data quality checks fail;
- clearly labels sponsored listings;
- includes last-verified and source links.

## Run

```bash
python validate.py
python sitegen.py
```

Preview the `dist/` folder locally.

Only after replacing sample records with real sourced data:

```bash
python sitegen.py --publish --base-url https://example.com
```

## Important

The sample data is fictional and is intentionally marked as such. Do not publish it. Replace it with primary-source-backed records first.
