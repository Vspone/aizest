# Pricing single-source migration — status

Canonical prices live in `src/data/product-facts.ts` (`ELEVENLABS_PRICING`,
`SYNTHESIA_PRICING`, `SUBMAGIC_PRICING`). `check_product_facts.py` audits the built
HTML and fails if a price attributed to one of the three products is not on the
official list — so a stale literal cannot go unnoticed.

## Done — batch 1 (2026-11-18)

| File | What was converted |
|---|---|
| `elevenlabs-review.astro` | FAQ JSON-LD, 6-row plan table, prose, Murf comparison row |
| `synthesia-review.astro` | FAQ JSON-LD, plan table, prose, comparison row |
| `submagic-review.astro` | FAQ array, plan table, pros list, meta description |
| `index.astro` | Creator Toolkit card description |
| `best-ai-voice-generators-2026.astro` | FAQ JSON-LD, summary table, comparison table, prose |
| `best-ai-avatar-video-generators-2026.astro` | FAQ JSON-LD ×2, summary table, comparison table, prose |
| `best-ai-video-editors-for-shorts-2026.astro` | FAQ JSON-LD, summary table, comparison table, prose |

## Done — batch 2 (2026-11-18)

| File | What was converted |
|---|---|
| `best-ai-tools-for-marketers-2026.astro` | FAQ JSON-LD, summary table, comparison table, prose, "Pricing:" lines |
| `best-ai-tools-for-youtube-creators-2026.astro` | FAQ JSON-LD ×3, summary table, comparison table, three "Pricing:" lines, pros/cons cell |
| `best-ai-tools-for-startups-2026.astro` | FAQ JSON-LD, summary table, comparison table, two "Pricing:" lines, prose |
| `heygen-vs-synthesia.astro` | pricing table cells, review pricing line, head-to-head row, FAQ, prose |
| `elevenlabs-vs-murf-vs-speechify.astro` | FAQ, entry-price line |
| `best-ai-tools-for-small-business-2026.astro` | two "Pricing:" lines, upsell list range |
| `best-ai-video-generators-2026.astro` | comparison row, "Pricing:" line |
| `best-ai-tools-for-bloggers-2026.astro` | two "Pricing:" lines, comparison row |
| `best-free-ai-tools-2026.astro` | "Pricing:" line |
| `best-ai-audio-tools-2026.astro` | "Pricing:" line |
| `best-ai-music-generators-2026.astro` | "Pricing:" line |

Every `.astro` page that quotes one of the three vendors now imports the constant.
`summary` / `entry` are derived from the plan fields rather than repeating prices,
so a vendor price change has exactly one place to land.

## `src/content/tools/*.md` — solved at the render layer

Markdown frontmatter cannot import TypeScript, so the three tool pages cannot read
the constants directly. But the page that renders them can:

`src/pages/tool/[slug].astro` now destructures the markdown values as
`pricingRaw` / `tiersRaw`, then builds `pricing` and `pricing_tiers` from a
`FACT_PRICING` map keyed by slug and plan name. Everything downstream — the hero
price, every plan card, the FAQ answer, the Offer JSON-LD, the CTA wording — reads
the overlaid values, i.e. the constants.

Three properties fall out of this:

1. **Unknown plan names fail the build.** If a vendor renames a tier and the
   markdown is updated without the map, the build throws
   `<slug>: plan "X" has no entry in FACT_PRICING…` instead of silently rendering
   the stale markdown price. Verified by renaming Submagic's "Pro" to "Pro Max".
2. **The markdown copies are inert but not unguarded.** `pricing` and
   `pricing_tiers[].price` still exist in the markdown because the JSON API
   (`/api/tools.json`), the homepage list and the `/alternatives/` tables read them
   straight from the collection. `check_md_mirror()` asserts each of those 14
   strings still appears on the built tool page — which is only true while they
   match the constants. Renaming a price in `product-facts.ts` makes that check
   fail on all four affected mirrors.
3. **The markdown bodies carry no prices.** Submagic's body had its own pricing
   table and a credits sentence; both are gone, replaced by prose that points at the
   plan cards. ElevenLabs' body had "The $5/month Starter plan" (the annual rate
   presented as monthly) and a `$22 Creator tier` in the cons list — both rewritten
   without numbers. That removes the only place where a markdown file could
   contradict the rendered page.

Drift test after the change: `SYNTHESIA_PRICING.starter.price` → `$21/mo`, rebuild,
`$21/mo ($14/mo billed yearly)` appears on `/tool/synthesia/`; the guard then
reports 21 stale-price claims plus 4 drifted markdown mirrors. Reverted, rebuilt,
green.

## Guard behaviour (as of the markdown layer)

`python3 check_product_facts.py` — run against `dist/`, exit 1 on failure.

1. **Language coverage** — 10 pages; `74` is forbidden as a phrase *and* as a bare
   number (a table cell reading just `<td>74</td>` used to slip through).
2. **Price attribution** — 127 claims. The lead-in is the current *sentence or
   table row*, not a fixed 90-character window: a long sentence can name the
   product first and the price 150 characters later, which the old window missed.
   `</td>`/`</th>` collapse to whitespace so a row keeps its product name; `</tr>`,
   `</p>`, `</li>`, `</h*>` start a new unit. Excluded as non-plan figures:
   per-minute economics, deltas, approximations, related-tool carousels.
3. **Unevaluated template literals** — any `${X_PRICING…}` or bare `X_PRICING.` in
   the built HTML fails.
4. **Markdown price mirrors** — 14 strings; each must appear on its built tool page.

All four have been self-tested by injecting the failure and confirming the check
fails, then restoring it.

## Errors found and fixed during the migration

- `best-ai-tools-for-small-business-2026`: Synthesia Starter listed as `$18/mo`.
- `best-ai-tools-for-small-business-2026`: Synthesia given a **Creator** tier at
  `$59/month` — that is ElevenLabs' tier name; `$59` is Synthesia's Pro *annual*
  price.
- `heygen-vs-synthesia`: Synthesia given a **Creator** tier at `$89/mo`, annual
  quoted as `$64/mo`, credits as "30 min". Synthesia's tiers are Basic / Starter /
  **Pro** / Enterprise; Pro is `$89/mo` or `$59/mo` billed yearly (`$708/yr`),
  6,000 credits ≈ 60 minutes.
- Four pages sold ElevenLabs' entry plan as `$5/mo` — that is the *annual* price.
  Monthly list is `$6/mo`. All four now say `$6/mo` with the yearly figure labelled.
- `best-ai-voice-generators-2026`: a bare `74` in the Languages table cell.
- Murf column on `elevenlabs-review` verified against four sources ($19 Creator /
  $66 Business annual vs $29 / $99 monthly) and now labelled as annual.

## Verification log

- Constant-drift test: `SYNTHESIA_PRICING.starter.price` → `$20/mo`, rebuild, and
  `$20/mo` appeared on `synthesia-review`, `index` and
  `best-ai-avatar-video-generators-2026`; reverted, rebuilt, guard green.
- Guard self-tests: bare `74` → fails; long-sentence `$18/mo` → fails;
  `${SYNTHESIA_PRICING.starter.price}` leak → fails. All restore to green.
- Competitor spot-check: Murf $19/$66 (annual) and Synthesia 140+ languages on all
  tiers (1-Click translation is the Enterprise-only part) both confirmed against
  vendor pages before leaving them alone.
