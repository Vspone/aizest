#!/usr/bin/env python3
"""
Guard: stop ElevenLabs language-coverage figures from drifting again.

Context: an outdated "74 languages" figure was hardcoded in 27 places across 11
files, because every page carried its own literal copy. The figures now live in
src/data/product-facts.ts (ELEVENLABS_LANGS), but two things can still go wrong:

  1. Someone types a fresh literal into a page instead of using the constant.
  2. Someone updates the constant but misses a file that quotes the prose
     (markdown content such as content/tools/elevenlabs.md cannot import it).

This script reads the built HTML, which is the only place where both imported
constants and copied markdown have already been resolved.

Usage:
    python3 check_product_facts.py          # verify dist/
    python3 check_product_facts.py --src    # also scan source for stale literals
Exit code 1 on failure, so it can gate a build.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, 'dist')
SRC = os.path.join(ROOT, 'src')

# Single source of truth. Keep in sync with src/data/product-facts.ts.
CANON_DIGITS = {'90', '70', '32', '29'}   # v4/v4 Turbo, v3, Flash v2.5, Multilingual v2
CANON_LABEL = 'v4=90+  v3=70+  Flash v2.5=32  Multilingual v2=29'

# Figures that are simply wrong for ElevenLabs and must never reappear.
FORBIDDEN = ['74']

# Pages that make ElevenLabs language claims. 'index' is a special path.
PAGES = [
    'elevenlabs-review', 'tool/elevenlabs',
    'best-ai-voice-generators-2026', 'best-ai-audio-tools-2026',
    'best-ai-tools-for-youtube-creators-2026', 'best-ai-tools-for-marketers-2026',
    'best-ai-tools-for-startups-2026', 'best-free-ai-tools-2026',
    'elevenlabs-vs-murf-vs-speechify', 'index',
]

# Other voice products whose language counts are legitimately different.
COMPETITORS = [
    'Murf', 'Speechify', 'PlayHT', 'Play.ht', 'Descript', 'Kits AI', 'Resemble',
    'WellSaid', 'LOVO', 'Polly', 'Azure', 'Google Cloud', 'Amazon',
]

NUM_LANG = re.compile(r'(\d{2,3})\+?\s*(?:languages|langs)\b', re.I)
SENTENCE = re.compile(r'[^.!?]+[.!?]?')


def html_path(page: str) -> str:
    return os.path.join(DIST, 'index.html' if page == 'index' else os.path.join(page, 'index.html'))


def strip_tags(html: str) -> str:
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<[^>]+>', ' ', html)
    return ' '.join(html.split())


def check_dist():
    problems = []
    for page in PAGES:
        path = html_path(page)
        if not os.path.exists(path):
            problems.append(f'{page}: built file missing ({path})')
            continue
        text = strip_tags(open(path, encoding='utf-8', errors='replace').read())

        # 1. Forbidden legacy figures, wherever they appear on these pages.
        for bad in FORBIDDEN:
            if re.search(rf'\b{bad}\+?\s*languages?\b', text, re.I):
                problems.append(f'{page}: stale "{bad} languages" claim')

        # 2. Sentence-level check: if a sentence is about ElevenLabs alone and
        #    makes a language-count claim, the number must be canonical.
        #    Flattened tables lose cell boundaries, so the previous sentence is
        #    included when deciding whether a competitor is also in play.
        sentences = SENTENCE.findall(text)
        for idx, sentence in enumerate(sentences):
            if 'ElevenLabs' not in sentence:
                continue
            context = (sentences[idx - 1] + ' ' + sentence) if idx else sentence
            if any(c.lower() in context.lower() for c in COMPETITORS):
                continue                      # mixed table row / comparison — ambiguous
            for m in NUM_LANG.finditer(sentence):
                if m.group(1) not in CANON_DIGITS:
                    snippet = sentence.strip()[:160]
                    problems.append(
                        f'{page}: "{m.group(0)}" is not a per-model figure → {snippet}')

        # 3. Core pages must keep the per-model framing and the qualifier.
        if page in ('elevenlabs-review', 'tool/elevenlabs'):
            for need in ('90+', '70+', '32', '29'):
                if need not in text:
                    problems.append(f'{page}: missing per-model figure {need}')
            low = text.lower()
            if 'varies by model' not in low and 'depends on the model' not in low:
                problems.append(f'{page}: missing "varies by model" qualifier')
    return problems


def check_src():
    """Catch hardcoded literals that should be the constant instead."""
    problems = []
    stale = re.compile(r'\b74\s+languages?\b', re.I)
    skip = {os.path.join(SRC, 'data', 'product-facts.ts')}  # documents the old value on purpose
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
                rel = os.path.relpath(path, ROOT)
                problems.append(f'{rel}:{line}: hardcoded "74 languages" literal')
    return problems


def main():
    problems = check_dist()
    if '--src' in sys.argv:
        problems += check_src()

    if problems:
        print(f'FAIL — {len(problems)} product-fact problem(s):\n')
        for p in problems:
            print('  •', p)
        print('\nFix by editing src/data/product-facts.ts and reusing the constant,')
        print('or by correcting the copy that quotes it.')
        return 1

    print(f'OK — ElevenLabs language coverage consistent across {len(PAGES)} pages')
    print(f'   canonical: {CANON_LABEL}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
