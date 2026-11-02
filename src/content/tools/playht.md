---
name: "PlayHT (PlayAI)"
slug: "playht"
description: "Discontinued AI voice platform. PlayHT was acquired by Meta in July 2025 and permanently shut down on December 31, 2025 — the domain no longer resolves."
category: "audio"
website: "https://play.ht"
pricing: "Discontinued — platform shut down December 31, 2025"
scores:
  ease_of_use: 8.3
  pricing_value: 9.3
  quality: 8.9
  speed: 8.1
  overall: 8.6
best_for: "Historical reference — no longer available"
last_verified: 2026-11-02
featured: false
rating: 4.3
discontinued: true
discontinued_date: "December 31, 2025"
discontinued_note: "Meta acquired the PlayAI team in July 2025. The API went offline in late July 2025, new sign-ups stopped in August 2025, and the platform was permanently shut down on December 31, 2025. All accounts, API keys, cloned voices, and saved audio were deleted with no export path. The play.ht and play.ai domains do not resolve as of November 2026."
successor: "elevenlabs"
features:
  - "900+ ultra-realistic AI voices across 140+ languages (at time of shutdown)"
  - "Voice cloning from short audio samples (at time of shutdown)"
  - "Real-time streaming TTS API (at time of shutdown)"
  - "SSML tag support for fine-grained speech control (at time of shutdown)"
  - "Podcast and dialogue generation with multiple voices (at time of shutdown)"
  - "Word-level timestamps for synchronization (at time of shutdown)"
pros:
  - "Had one of the largest voice libraries at 900+ voices in 140+ languages"
  - "Voice cloning quality was strong from short audio samples"
  - "Real-time streaming API was well documented for developers"
  - "Multi-voice dialogue was useful for podcast and narration workflows"
cons:
  - "No longer available — the platform shut down permanently on December 31, 2025"
  - "All user data, voice clones, and API keys were deleted at shutdown"
  - "No export or migration tool was provided to customers"
  - "Anyone who built on the API had to re-integrate from scratch"
pricing_tiers: []
---

**PlayHT is no longer available.** PlayHT — later branded PlayAI — was a text-to-speech and voice cloning platform that competed with ElevenLabs and Murf. Meta acquired the PlayAI team in July 2025, and the consumer platform was permanently shut down on **December 31, 2025**.

## What happened

The shutdown followed a clear timeline:

- **July 2025** — Meta acquired the PlayAI team (~35 people), absorbed into Meta Superintelligence Labs
- **Late July 2025** — the PlayHT API went offline ahead of the announced schedule
- **August 2025** — new sign-ups stopped
- **December 31, 2025** — platform fully shut down; accounts, saved audio, and voice clones permanently deleted
- **2026** — the `play.ht` and `play.ai` domains stopped resolving entirely

There is no recovery path. Voice clones and saved audio were deleted with no export tool, so any project that referenced a PlayHT voice ID must be rebuilt on another platform.

## What to use instead

The right replacement depends on what you used PlayHT for:

| If you used PlayHT for… | Use instead | Why |
|---|---|---|
| **Voiceover production for video or podcasts** | [ElevenLabs](/tool/elevenlabs) | Closest functional match — instant and professional voice cloning, 74 languages, API with low-latency streaming, paid plans from $6/month |
| **Business and training voiceovers** | [Murf AI](/tool/murf) | Curated 200+ licensed voices with a studio editor aimed at non-technical teams |
| **Reading documents aloud (consumer use)** | Speechify | PlayHT had no real successor for the listening use case — Speechify is the closest |

Read the full [ElevenLabs vs Murf vs Speechify comparison](/elevenlabs-vs-murf-vs-speechify) for current pricing and a migration checklist.

## Migration checklist

1. **Audit lost references.** Any script, project, or integration pointing at a PlayHT voice ID will no longer resolve.
2. **Re-clone your voice** on the new platform — you need a fresh audio sample, and cloning consent must be re-established.
3. **Rebuild pronunciation dictionaries.** Acronyms, brand names, and numbers are handled differently on every platform.
4. **Update API integrations** — endpoint and authentication must be swapped, not just the key.
5. **Confirm commercial licensing** on the new plan before publishing anything generated.

## Point-in-time reference

For anyone comparing historical pricing or researching the market: at the time of shutdown, PlayHT offered a free tier (5,000 characters/month, non-commercial), a Creator plan at $31.20/month (300,000 characters/year, commercial rights, 3 cloned voices), and a Pro plan at $99/month (1 million characters/year, unlimited cloning, real-time API). These prices are no longer purchasable and appear here only as historical record.
