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
    featured: z.boolean().default(false),
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
  }),
});

export const collections = {
  tools: tools,
};
