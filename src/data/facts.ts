/**
 * Single source of truth for tool facts that appear in prose across the site.
 *
 * Why this file exists: the same number used to be written by hand in three or
 * four places (.md description, review page body, listicle table, homepage card).
 * ElevenLabs' language count had drifted into 20+ / 29+ / 30+ / 35+ / 60+ / 70+ / 74
 * across seven files before this was consolidated on 2026-11-18.
 *
 * Rules:
 *  - Change a number HERE first, then run scripts/aizest-facts-audit.sh.
 *    The script scans every .astro and .md for a language-count claim and fails
 *    if the value disagrees with this table.
 *  - `languages` is the vendor's own published figure for language support on
 *    the entry paid tier. Where a vendor publishes a different figure for a
 *    narrower feature (e.g. voice cloning, dubbing), record it under the
 *    matching key so the two are never conflated:
 *      - heygen.dubbingLanguages (40) is NOT heygen.languages (175)
 *      - synthesia.voiceCloningLanguages (32) is NOT synthesia.languages (140)
 *  - `verified` is the date the vendor page was last read. Anything older than
 *    ~90 days should be treated as suspect.
 */

export const LANGUAGES = {
  elevenlabs: 74,
  synthesia: 140,
  heygen: 175,
  murf: 35,
  speechify: 60,
  veed: 100,
  submagic: 123,
  fliki: 80,
  rytr: 30,
  writesonic: 25,
  canva: 100,
} as const;

/** Languages that belong to a specific sub-feature, never the headline number. */
export const FEATURE_LANGUAGES = {
  'heygen.dubbing': 40,
  'synthesia.voiceCloning': 32,
} as const;

/** Avatar / voice library sizes, same drift problem. */
export const LIBRARY_SIZES = {
  'synthesia.avatars.starter': '125+',
  'synthesia.avatars.enterprise': '240+',
  'synthesia.voices': '1,000+',
  'heygen.avatars': '700+',
  'elevenlabs.voices': 'hundreds',
  'speechify.voices': '1,000+',
  'murf.voices': '150+',
} as const;

/**
 * Headline prices per tool, matching the `pricing` field in each
 * src/content/tools/<slug>.md. Kept here so a facts audit can catch a listicle
 * quoting an old number. Prices are the entry paid tier, monthly unless noted.
 */
export const ENTRY_PRICES = {
  elevenlabs: '$6/mo',
  synthesia: '$19/mo',
  submagic: '$19/mo ($12/mo yearly)',
  murf: '$19/mo',
  speechify: '$29/mo',
  heygen: '$29/mo',
  descript: '$16/mo',
  runway: '$12/mo (annual)',
  semrush: '$139/mo',
  jasper: '$69/mo',
  surfer: '$49/mo',
  hubspot: '$20/mo/seat',
  canva: '$144/yr',
  bolt: '$25/mo',
  notion: '$20/member/mo',
} as const;

export const FACTS_VERIFIED = '2026-11-18';
