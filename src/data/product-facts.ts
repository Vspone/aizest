/**
 * Single source of truth for product facts that appear on more than one page.
 *
 * Why this file exists: an outdated "74 languages" figure was hardcoded in 27
 * places across 11 files because there was no shared constant. Update the value
 * here and every page that imports it follows.
 *
 * RULES
 *  - Only put a fact here if it is verifiable against the vendor's own docs.
 *  - Always record `verified` (date) and `source` (URL) next to the fact.
 *  - Never merge different models' figures into one headline number.
 */

/**
 * ElevenLabs text-to-speech language coverage, per model.
 * Verified 2026-11-18 against https://elevenlabs.io/docs/overview/models
 *
 * IMPORTANT: these are per-model text-to-speech figures. They are NOT a
 * platform-wide guarantee that every ElevenLabs feature (dubbing,
 * speech-to-speech, voice design) covers the same set of languages.
 *
 * Note on Flash v2.5 = 32: the docs list it as all 29 Multilingual v2
 * languages plus hu, no, vi. Do not "round" it or derive it at runtime.
 */
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

  /** Badges, cards and titles where only the flagship figure fits. */
  compact: '90+ languages (Eleven v4)',
} as const;
