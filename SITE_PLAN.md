# aizest.net — AI Tools Directory Site

Build a complete AI tools directory and review website using Astro + Tailwind CSS.

## Site Info
- Domain: aizest.net (pointed to Vercel later)
- Language: English
- Audience: Global (SEO targeted)
- Monetization: Affiliate links + Google AdSense

## Pages to Build

1. **Homepage** (`/`) — Hero with tagline "Discover the Best AI Tools for Every Task", search bar, category grid (10 categories), featured tools section
2. **Category page** (`/category/[slug]`) — Filtered list of tools in that category
3. **Tool detail page** (`/tool/[slug]`) — Full tool page with description, features, pricing, pros/cons, CTA button with affiliate link
4. **Best of list** (`/best/best-ai-writing-tools-2026`) — Ranked listicle
5. **About page** (`/about`)

## Categories (10)
1. writing — Writing & Content
2. image — Image Generation
3. video — Video Creation
4. audio — Audio & Voice
5. coding — Coding & Development
6. marketing — Marketing & SEO
7. productivity — Productivity
8. data — Data & Analytics
9. design — Design & Creative
10. business — Business & Finance

## Tech Requirements
- Astro (static site generation)
- Tailwind CSS for styling (clean, modern, dark+light mode)
- TypeScript strict mode
- Content Collections for tools (Markdown frontmatter)
- Responsive design (mobile-first)
- SEO: meta tags, Open Graph, sitemap, canonical URLs
- Fast page loads (Lighthouse 90+)

## Tool Content (src/content/tools/ — create these 10 files)
Each is a .md file with frontmatter + body. Realistic content.

1. **chatgpt.md** — Chat GPT, category: writing, description: "Advanced AI chatbot by OpenAI for conversation, writing, and problem-solving"
2. **jasper.md** — Jasper AI, category: writing, description: "AI writing assistant for marketing copy and blog content"
3. **midjourney.md** — Midjourney, category: image, description: "AI image generator creating stunning visuals from text prompts"
4. **canva.md** — Canva AI, category: design, description: "AI-powered design platform with text-to-image and magic editing"
5. **elevenlabs.md** — ElevenLabs, category: audio, description: "AI voice synthesis with natural, human-like speech"
6. **copilot.md** — GitHub Copilot, category: coding, description: "AI pair programmer that suggests code in real-time"
7. **notion.md** — Notion AI, category: productivity, description: "AI-enhanced workspace for notes, docs, and project management"
8. **perplexity.md** — Perplexity AI, category: data, description: "AI-powered search engine with cited answers"
9. **synthesia.md** — Synthesia, category: video, description: "AI video generation with realistic AI avatars"
10. **runway.md** — Runway ML, category: video, description: "Creative AI tools for video editing and generation"

Best-of page: `/src/content/pages/best-ai-writing-tools-2026.md`

## Design Style
- Clean, minimal, professional
- Accent color: vibrant blue (#3B82F6)
- Cards with subtle shadows, rounded corners
- Clear CTA buttons (affiliate links)
- Category badges with different colors
- Star ratings for tools

## Build Command
After building, ensure `npm install` and `npm run build` work cleanly.
