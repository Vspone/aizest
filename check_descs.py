#!/usr/bin/env python3
"""Audit <meta name="description"> across the built site.

Scans dist/ rather than src/ on purpose. Most pages get their description from
markdown frontmatter or a template string, so grepping src/pages/*.astro for
description="..." sees only a fraction of the site — the previous version of
this script reported 3 overlong descriptions while 155 pages were actually
over the limit.

Severity:
  ERROR  missing, empty, duplicated across pages, doubled punctuation, or
         longer than 200 chars. Exits 1.
  WARN   between 161 and 200 chars. Length is not a ranking factor — the only
         cost is that Google truncates the tail of the snippet — so these are
         reported, not failed.
"""
import re
import os
import sys
import collections

DIST = 'dist'
HARD_MAX = 200
SOFT_MAX = 160

errors = []
warnings = []
rows = []

if not os.path.isdir(DIST):
    print(f'❌ {DIST}/ not found — run `npm run build` first.')
    sys.exit(1)

for root, _dirs, files in os.walk(DIST):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        rel = path[len(DIST):].replace('/index.html', '') or '/'
        html = open(path, errors='ignore').read()
        m = re.search(r'<meta name="description" content="([^"]*)"', html)
        if not m:
            errors.append(f'{rel}: no <meta name="description">')
            continue
        desc = (
            m.group(1)
            .replace('&amp;', '&')
            .replace('&quot;', '"')
            .replace('&#39;', "'")
            .replace('&lt;', '<')
            .replace('&gt;', '>')
        )
        if not desc.strip():
            errors.append(f'{rel}: empty description')
            continue
        rows.append((rel, desc))

        frag = re.search(r'\S*[.,;:]{2,}\S*', desc)
        if frag:
            errors.append(f'{rel}: doubled punctuation near "{frag.group(0)[:40]}"')
        if len(desc) > HARD_MAX:
            errors.append(f'{rel}: {len(desc)} chars (hard cap {HARD_MAX})')
        elif len(desc) > SOFT_MAX:
            warnings.append((len(desc), rel))

for desc, count in collections.Counter(d for _r, d in rows).items():
    if count > 1:
        pages = [r for r, d in rows if d == desc][:4]
        errors.append(f'{count} pages share one description: {pages} — "{desc[:60]}…"')

warnings.sort(key=lambda x: -x[0])

print(f'checked {len(rows)} pages')
if warnings:
    print(f'⚠️  {len(warnings)} description(s) between {SOFT_MAX + 1} and {HARD_MAX} chars (may be truncated, not a ranking issue)')
    for n, rel in warnings[:8]:
        print(f'     {n}ch  {rel}')
    if len(warnings) > 8:
        print(f'     … and {len(warnings) - 8} more')

if errors:
    print(f'\n❌ {len(errors)} description error(s):')
    for e in errors:
        print(f'   {e}')
    sys.exit(1)

print(f'✅ no duplicate, missing, doubled-punctuation or >{HARD_MAX}-char descriptions')
