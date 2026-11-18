# Pricing single-source migration — status

Canonical prices live in `src/data/product-facts.ts` (`ELEVENLABS_PRICING`,
`SYNTHESIA_PRICING`, `SUBMAGIC_PRICING`). `check_product_facts.py` audits the built
HTML and fails if a price attributed to one of the three products is not on the
official list — so a stale literal can no longer go unnoticed, but it still has to
be *fixed by hand* until every page interpolates the constant.

This file tracks which pages interpolate and which still carry literals.

## Done — batch 1 (2026-11-18)

| File | What was converted |
|---|---|
| `src/pages/elevenlabs-review.astro` | FAQ JSON-LD, 6-row plan table, prose, Murf comparison row |
| `src/pages/synthesia-review.astro` | FAQ JSON-LD, plan table, two prose blocks (also gained the import) |
| `src/pages/submagic-review.astro` | FAQ array (2 answers), plan table, pros list, meta description |
| `src/pages/index.astro` | Creator Toolkit card description |
| `src/pages/best-ai-voice-generators-2026.astro` | FAQ JSON-LD, summary table, comparison table, prose |
| `src/pages/best-ai-avatar-video-generators-2026.astro` | FAQ JSON-LD (×2), summary table, comparison table, prose (also gained the import) |
| `src/pages/best-ai-video-editors-for-shorts-2026.astro` | FAQ JSON-LD, summary table, comparison table, prose (also gained the import) |

Also in batch 1:

- `summary` / `entry` strings are now **derived** from the plan fields instead of
  repeating the prices — otherwise updating `starter.price` would silently leave
  the summary line stale.
- A bare `74` in a "Languages" table cell was found on
  `best-ai-voice-generators-2026` — the old guard only matched the phrase
  "74 languages", so a cell with just the number slipped through. The guard now
  flags a bare `74` on the language pages too.

## Remaining — batch 2

Counted by attribution heuristic (product named in the 90 chars before the amount,
no competitor named); per-minute/derived figures excluded. Verify with a fresh
scan before starting — line numbers move.

| Literals | File |
|---:|---|
| 14 | `src/pages/best-ai-tools-for-marketers-2026.astro` |
| 13 | `src/pages/best-ai-tools-for-youtube-creators-2026.astro` |
| 10 | `src/pages/best-ai-tools-for-startups-2026.astro` |
| 7 | `src/pages/heygen-vs-synthesia.astro` |
| 3 | `src/pages/elevenlabs-vs-murf-vs-speechify.astro` |
| 3 | `src/pages/best-ai-tools-for-small-business-2026.astro` |
| 2 | `src/pages/best-ai-video-generators-2026.astro` |
| 2 | `src/content/tools/submagic.md` |
| 1 | `src/pages/best-ai-tools-for-bloggers-2026.astro` |
| 1 | `src/content/tools/synthesia.md` |

Total ≈ 56. The two `src/content/tools/*.md` files **cannot** import the constant —
markdown content collections have no TS imports available in this setup, so those
two stay literal and rely on the guard to flag drift when a vendor changes price.

## Procedure per file

1. Add/expand the import: `import { X_PRICING } from '../data/product-facts';`
2. Frontmatter strings and `JSON.stringify` blocks → template literal
   (`` `Starter ${X_PRICING.starter.price}` ``), **not** `"..." + $` — the `$` form
   only interpolates inside backticks.
3. Template body → `{X_PRICING.starter.price}`.
4. Watch the closing braces on JSON-LD lines: each entry ends `} },` — one `}`
   closes `acceptedAnswer`, one closes the question object. A third `}` breaks
   esbuild with "Expected ']' but found '}'".
5. `npm run build && python3 check_product_facts.py` — both must pass.
6. To prove the wiring actually reaches the page, temporarily change a value in
   `product-facts.ts`, rebuild, grep the built HTML for the new number, then revert
   and rebuild. The allow-list check will fail while the test value is in place;
   that is expected.

## Verification done for batch 1

- Constant-drift test: `SYNTHESIA_PRICING.starter.price` → `$20/mo`, rebuilt, and
  `$20/mo` appeared on `synthesia-review`, `index` and
  `best-ai-avatar-video-generators-2026`; reverted, rebuilt, guard green.
- Guard self-test: injecting `<td>74</td>` into the built page fails the check with
  the surrounding text; restoring it turns the check green.
- Competitor spot-check: the Murf column on `elevenlabs-review`
  ($19 Creator / $66 Business, both annual) reconciles with Murf's published
  monthly prices ($29 / $99) across four independent sources. Both cells now say
  "annual billing" so the reader is not misled.
