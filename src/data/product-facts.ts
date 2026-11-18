/**
 * Single source of truth for product facts that appear on more than one page.
 *
 * Why this file exists: an outdated "74 languages" figure was hardcoded in 27
 * places across 11 files, and an outdated Synthesia price in 6 more. One fact,
 * many copies, no owner. Update a value here and every page that imports it
 * follows; check_product_facts.py fails the build check if a page drifts.
 *
 * RULES
 *  - Only put a fact here if it is verifiable against the vendor's own page.
 *  - Always record `verified` (date) and `source` (URL) next to the fact.
 *  - Never merge different plans or models into one headline number.
 *  - If you could not verify something, say so in a comment instead of guessing.
 */

/* ────────────────────────────────────────────────────────────────────────────
 * ElevenLabs — text-to-speech language coverage, per model
 * Verified 2026-11-18 against https://elevenlabs.io/docs/overview/models
 *
 * IMPORTANT: these are per-model text-to-speech figures. They are NOT a
 * platform-wide guarantee that every ElevenLabs feature (dubbing,
 * speech-to-speech, voice design) covers the same set of languages.
 *
 * Flash v2.5 = 32 because the docs list it as all 29 Multilingual v2 languages
 * plus hu, no, vi. Do not "round" it or derive it at runtime.
 *
 * Vendor inconsistency worth knowing: ElevenLabs' *pricing* page comparison
 * table still shows a flat "74" for languages across all TTS plans, while its
 * model docs give the per-model figures above. We follow the model docs because
 * they are the specific claim; the "74" is stale.
 * ──────────────────────────────────────────────────────────────────────────── */
export const ELEVENLABS_LANGS = {
  verified: '2026-11-18',
  source: 'https://elevenlabs.io/docs/overview/models',

  // Per-model figures — use these, never a literal number in a page
  v4: '90+',
  v4Turbo: '90+',
  v3: '70+',
  flash: '32',
  multilingualV2: '29',

  /** Standalone paragraph, or a self-contained answer (body copy, FAQ answers). */
  full:
    'ElevenLabs offers multiple text-to-speech models with different language coverage. ' +
    'Eleven v4 supports 90+ languages, Eleven v3 supports 70+ languages, ' +
    'Flash v2.5 supports 32 languages, and Multilingual v2 supports 29 languages. ' +
    'Language availability varies by model.',

  /** Mid-sentence enumeration where the sentence already supplies the framing. */
  inline: '90+ on Eleven v4, 70+ on v3, 32 on Flash v2.5, 29 on Multilingual v2',

  /** Table cells and comparison rows — shortest unambiguous form. */
  table: '90+ (v4) / 70+ (v3) / 32 (Flash v2.5) / 29 (Multilingual v2)',

  /** Single cell inside an already-labelled "Languages" column. */
  cell: '90+ (v4)',

  /** Badges, cards and titles where only the flagship figure fits. */
  compact: '90+ languages (Eleven v4)',
} as const;

/* ────────────────────────────────────────────────────────────────────────────
 * ElevenLabs — plans and allowances
 * Verified 2026-11-18 against https://elevenlabs.io/pricing (ElevenCreative)
 *
 * All products draw from one shared monthly credit pool.
 * Annual billing = 2 months free (annual price = monthly × 10).
 * Credits reset monthly; unused roll over up to 2 months on paid plans.
 * ──────────────────────────────────────────────────────────────────────────── */
const EL_PLANS = {
  free: { price: '$0', credits: '10,000', note: 'no commercial licence, no rollover' },
  starter: { price: '$6/mo', annual: '$5/mo', credits: '30,000', note: 'commercial licence + Instant Voice Cloning' },
  creator: { price: '$22/mo', annual: '$18.33/mo', credits: '121,000', note: 'first Professional Voice Cloning tier' },
  pro: { price: '$99/mo', annual: '$82.50/mo', credits: '600,000', note: '44.1kHz PCM output via API' },
  scale: { price: '$299/mo', annual: '$249.17/mo', credits: '1.8M', note: '3 workspace seats' },
  business: { price: '$990/mo', annual: '$825/mo', credits: '6M', note: '10 PVC slots, 10 seats' },
} as const;

export const ELEVENLABS_PRICING = {
  ...EL_PLANS,
  verified: '2026-11-18',
  source: 'https://elevenlabs.io/pricing',

  /** Short line used in summary cards and CTA blocks. Derived — never retype. */
  summary: `Free (${EL_PLANS.free.credits} credits/mo) · Starter ${EL_PLANS.starter.price} · Creator ${EL_PLANS.creator.price}`,
  /** One-line value proposition for tables. */
  entry: `Free / ${EL_PLANS.starter.price}`,
} as const;

/* ────────────────────────────────────────────────────────────────────────────
 * Synthesia — plans and allowances
 * Verified 2026-11-18 against https://www.synthesia.io/pricing
 *
 * Basic is free with a watermark. Starter removes it. Yearly billing saves up
 * to 4 months. The "$9"/"$49" figures are first-month promos, not list price.
 * 1-Click Translations into 140+ languages is listed as an Enterprise feature.
 * ──────────────────────────────────────────────────────────────────────────── */
const SYNTH_PLANS = {
  basic: { price: '$0', credits: '500', note: 'watermarked, 9 avatars, 10 min Studio video' },
  starter: { price: '$19/mo', annual: '$14/mo', annualTotal: '$168/yr', credits: '1,250', creditsPer: 'month', note: 'no watermark, 125+ avatars, 3 guests' },
  pro: { price: '$89/mo', annual: '$59/mo', annualTotal: '$708/yr', credits: '6,000', creditsPer: 'month', note: '5 personal avatars, branded pages, interactive video' },
  enterprise: { price: 'Custom', credits: 'Custom', note: 'unlimited minutes, 140+ language translation, SSO' },
} as const;

export const SYNTHESIA_PRICING = {
  ...SYNTH_PLANS,
  verified: '2026-11-18',
  source: 'https://www.synthesia.io/pricing',

  /** First-month promo prices — legal to mention, but must be labelled as promo. */
  promo: { starterFirstMonth: '$9', proFirstMonth: '$49' },

  summary: `Free (${SYNTH_PLANS.basic.credits} credits/mo) · Starter ${SYNTH_PLANS.starter.price} · Pro ${SYNTH_PLANS.pro.price}`,
  entry: `Free / ${SYNTH_PLANS.starter.price}`,
} as const;

/* ────────────────────────────────────────────────────────────────────────────
 * Submagic — plans and allowances
 * Verified 2026-11-18 against https://www.submagic.co/pricing
 *
 * Monthly list prices are not printed directly on the page; they are confirmed
 * by the advertised annual savings: (39-23)x12 = $192, (69-41)x12 = $336,
 * (19-12)x12 = $84. All three reconcile, so the monthly figures below are the
 * vendor's own numbers rather than an estimate.
 *
 * No watermark on any paid tier. No permanent free plan — the trial is the only
 * no-card entry point. Video length is 2/5/30 minutes by tier.
 * ──────────────────────────────────────────────────────────────────────────── */
const SUB_PLANS = {
  starter: { price: '$19/mo', amount: '$19', annual: '$12/mo', annualAmount: '$12', credits: '45 credits = 15 videos or 5 Magic Clips', creditsNum: '45', videos: '15', maxLength: '2 min' },
  pro: { price: '$39/mo', amount: '$39', annual: '$23/mo', annualAmount: '$23', credits: '120 credits = 40 videos or 15 Magic Clips', creditsNum: '120', videos: '40', maxLength: '5 min' },
  business: { price: '$69/mo', amount: '$69', annual: '$41/mo', annualAmount: '$41', credits: '300 credits = 100 videos or 37 Magic Clips', creditsNum: '300', videos: '100', maxLength: '30 min' },
} as const;

export const SUBMAGIC_PRICING = {
  ...SUB_PLANS,
  verified: '2026-11-18',
  source: 'https://www.submagic.co/pricing',

  summary: `Starter ${SUB_PLANS.starter.price} · Pro ${SUB_PLANS.pro.price} · Business ${SUB_PLANS.business.price} (yearly ${SUB_PLANS.starter.annual}, ${SUB_PLANS.pro.annual}, ${SUB_PLANS.business.annual})`,
  entry: `Free trial / ${SUB_PLANS.starter.price}`,
} as const;

/* ────────────────────────────────────────────────────────────────────────────
 * Guard allow-lists — consumed by check_product_facts.py
 *
 * Any price attributed to one of these products in built HTML must appear in
 * its list below. Add a value here only after checking the vendor page and
 * bumping `verified` above.
 * ──────────────────────────────────────────────────────────────────────────── */
export const PRICE_ALLOWLIST = {
  ElevenLabs: ['$0', '$6', '$5', '$22', '$18.33', '$99', '$82.50', '$299', '$249.17', '$990', '$825'],
  Synthesia: ['$0', '$9', '$19', '$14', '$168', '$49', '$89', '$59', '$708'],
  Submagic: ['$0', '$19', '$12', '$39', '$23', '$69', '$41'],
} as const;
