#!/usr/bin/env python3
"""
Guard: stop ElevenLabs / Synthesia / Submagic facts from drifting.

Context: an outdated "74 languages" figure was hardcoded in 27 places and an
outdated Synthesia price in 6 more, because every page carried its own literal
copy. Canonical values now live in src/data/product-facts.ts. Two failure modes
remain, and this script catches both:

  1. Someone types a stale literal into a page instead of using the constant.
  2. Someone updates the constant but misses a file that quotes the prose
     (markdown content such as content/tools/*.md cannot import it).

It reads the built HTML, which is the only place where imported constants and
copied markdown have both been resolved.

Usage:
    python3 check_product_facts.py          # verify dist/
    python3 check_product_facts.py --src    # also scan source for stale literals
Exit code 1 on failure, so it can gate a build.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, 'dist')
SRC = os.path.join(ROOT, 'src')
FACTS_TS = os.path.join(SRC, 'data', 'product-facts.ts')

# ── ElevenLabs language coverage ────────────────────────────────────────────
CANON_DIGITS = {'90', '70', '32', '29'}   # v4/v4 Turbo, v3, Flash v2.5, Multilingual v2
CANON_LABEL = 'v4=90+  v3=70+  Flash v2.5=32  Multilingual v2=29'
FORBIDDEN_LANG = ['74']

LANG_PAGES = [
    'elevenlabs-review', 'tool/elevenlabs',
    'best-ai-voice-generators-2026', 'best-ai-audio-tools-2026',
    'best-ai-tools-for-youtube-creators-2026', 'best-ai-tools-for-marketers-2026',
    'best-ai-tools-for-startups-2026', 'best-free-ai-tools-2026',
    'elevenlabs-vs-murf-vs-speechify', 'index',
]

# ── Price attribution ───────────────────────────────────────────────────────
# Any $ amount whose 90-character lead-in names exactly one of our affiliate
# products (and no competitor) must be one of that product's known prices.
OURS = ['ElevenLabs', 'Synthesia', 'Submagic']
COMPETITORS = [
    'Murf', 'Speechify', 'PlayHT', 'Play.ht', 'Descript', 'Kits AI', 'Resemble',
    'WellSaid', 'LOVO', 'Polly', 'Azure', 'HeyGen', 'CapCut', 'VEED', 'InVideo',
    'Opus Clip', 'Canva', 'Colossyan', 'Elai', 'Synthesys', 'Pictory', 'Fliki',
    'AIVA', 'Kits', 'Mubert', 'Soundraw', 'Boomy', 'Udio', 'Suno', 'Beatoven',
    'LALAL', 'Adobe', 'Runway', 'Pika', 'Luma',
]

AMOUNT = re.compile(r'\$\s?\d{1,3}(?:,\d{3})*(?:\.\d+)?')
LEAD = 90            # characters of context before the amount
SENTENCE = re.compile(r'[^.!?]+[.!?]?')
NUM_LANG = re.compile(r'(\d{2,3})\+?\s*(?:languages|langs)\b', re.I)


def parse_allowlist(path: str) -> dict:
    """Read PRICE_ALLOWLIST straight out of the TypeScript file (no TS runner here)."""
    body = open(path, encoding='utf-8').read()
    m = re.search(r'PRICE_ALLOWLIST\s*=\s*\{(.*?)\n\}\s*as const', body, re.S)
    if not m:
        raise SystemExit('check_product_facts: PRICE_ALLOWLIST not found in product-facts.ts')
    out = {}
    for prod, vals in re.findall(r'(\w+):\s*\[([^\]]*)\]', m.group(1)):
        out[prod] = set(json.loads('[' + vals.replace("'", '"') + ']'))
    return out


def strip_tags(html: str) -> str:
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<[^>]+>', ' ', html)
    return ' '.join(html.split())


def html_path(page: str) -> str:
    return os.path.join(DIST, 'index.html' if page == 'index' else os.path.join(page, 'index.html'))


def all_pages():
    for root, _dirs, files in os.walk(DIST):
        if 'index.html' in files:
            rel = os.path.relpath(root, DIST)
            yield ('index' if rel == '.' else rel.replace(os.sep, '/')), os.path.join(root, 'index.html')


def check_languages(problems):
    for page in LANG_PAGES:
        path = html_path(page)
        if not os.path.exists(path):
            problems.append(f'{page}: built file missing ({path})')
            continue
        text = strip_tags(open(path, encoding='utf-8', errors='replace').read())

        for bad in FORBIDDEN_LANG:
            if re.search(rf'\b{bad}\+?\s*languages?\b', text, re.I):
                problems.append(f'{page}: stale "{bad} languages" claim')

        sentences = SENTENCE.findall(text)
        for idx, sentence in enumerate(sentences):
            if 'ElevenLabs' not in sentence:
                continue
            context = (sentences[idx - 1] + ' ' + sentence) if idx else sentence
            if any(c.lower() in context.lower() for c in COMPETITORS):
                continue
            for m in NUM_LANG.finditer(sentence):
                if m.group(1) not in CANON_DIGITS:
                    problems.append(
                        f'{page}: "{m.group(0)}" is not a per-model figure → {sentence.strip()[:150]}')

        if page in ('elevenlabs-review', 'tool/elevenlabs'):
            for need in ('90+', '70+', '32', '29'):
                if need not in text:
                    problems.append(f'{page}: missing per-model figure {need}')
            low = text.lower()
            if 'varies by model' not in low and 'depends on the model' not in low:
                problems.append(f'{page}: missing "varies by model" qualifier')


def check_prices(problems, allow):
    checked = 0
    for page, path in all_pages():
        text = strip_tags(open(path, encoding='utf-8', errors='replace').read())
        if not any(p in text for p in OURS):
            continue
        for m in AMOUNT.finditer(text):
            lead_raw = text[max(0, m.start() - LEAD):m.start()]
            lead = lead_raw.lower()
            ours = [p for p in OURS if p.lower() in lead]
            if len(ours) != 1:
                continue                     # no product, or ambiguous comparison
            if any(c.lower() in lead for c in COMPETITORS):
                continue                     # price probably belongs to the competitor
            prod = ours[0]

            # Derived or aggregate figures are not plan prices: cost-per-minute,
            # deltas ("the extra $10 buys"), approximations and bundle totals.
            before = lead_raw.rstrip()
            if before.endswith(('≈', '~', '+', '-', 'about', 'around', 'roughly', 'under', 'over', 'extra')):
                continue
            after = text[m.end():m.end() + 8].strip().lower()
            if after.startswith(('/min', 'per min', '/ minute')):
                continue
            if 'similar to' in lead:
                continue                     # related-tools carousel, not this product

            amount = re.sub(r'\s+', '', m.group(0))
            # normalise "$19.00" → "$19"
            amount = re.sub(r'\.00$', '', amount)
            checked += 1
            if amount not in allow.get(prod, set()):
                start = max(0, m.start() - 70)
                snippet = text[start:m.end() + 40]
                problems.append(f'{page}: {prod} shown as {amount} (not an official price) → …{snippet}…')
    return checked


def check_src(problems):
    stale = re.compile(r'\b74\s+languages?\b', re.I)
    skip = {FACTS_TS}
    for root, _dirs, files in os.walk(SRC):
        for name in files:
            if not name.endswith(('.astro', '.md', '.mdx', '.ts', '.js')):
                continue
            path = os.path.join(root, name)
            if path in skip:
                continue
            body = open(path, encoding='utf-8', errors='replace').read()
            for m in stale.finditer(body):
                line = body[:m.start()].count('\n') + 1
                problems.append(f'{os.path.relpath(path, ROOT)}:{line}: hardcoded "74 languages" literal')


def main():
    problems = []
    allow = parse_allowlist(FACTS_TS)

    check_languages(problems)
    price_checks = check_prices(problems, allow)
    if '--src' in sys.argv:
        check_src(problems)

    if problems:
        print(f'FAIL — {len(problems)} product-fact problem(s):\n')
        for p in problems:
            print('  •', p)
        print('\nFix by editing src/data/product-facts.ts and reusing the constant,')
        print('or by correcting the copy that quotes it.')
        return 1

    print(f'OK — language coverage consistent across {len(LANG_PAGES)} pages')
    print(f'   canonical: {CANON_LABEL}')
    print(f'OK — {price_checks} attributed price claim(s) checked, all official')
    print(f'   allow-lists: {", ".join(f"{k} ({len(v)})" for k, v in allow.items())}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
