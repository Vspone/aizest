import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const tools = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/tools" }),
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    description: z.string(),
    category: z.string(),
    website: z.string().url(),
    pricing: z.string(),
    affiliate_url: z.string().optional(),
    // affiliate: true only when we have a real, approved affiliate relationship
    // and the URL carries a tracking parameter. Drives rel="sponsored nofollow"
    // and the on-page disclosure. Everything else is a plain official link.
    affiliate: z.boolean().default(false),
    featured: z.boolean().default(false),
    best_for: z.string().optional(),
    last_verified: z.union([z.string(), z.date()]).optional(),
    needs_vps: z.boolean().default(false),
    scores: z
      .object({
        ease_of_use: z.number().optional(),
        pricing_value: z.number().optional(),
        quality: z.number().optional(),
        speed: z.number().optional(),
        overall: z.number().optional(),
      })
      .partial()
      .optional(),
    rating: z.number().min(0).max(5),
    features: z.array(z.string()),
    pricing_tiers: z.array(
      z.object({
        name: z.string(),
        price: z.string(),
        features: z.array(z.string()),
      })
    ),
    pros: z.array(z.string()),
    cons: z.array(z.string()),
    pubDate: z.date().optional(),
    discontinued: z.boolean().default(false),
    discontinued_date: z.string().optional(),
    discontinued_note: z.string().optional(),
    successor: z.string().optional(),
  }),
});

export const collections = {
  tools: tools,
};
