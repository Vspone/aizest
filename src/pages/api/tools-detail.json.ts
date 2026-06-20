import { getCollection } from 'astro:content';

export const prerender = true;

export async function GET() {
  const tools = await getCollection('tools');
  const detail = tools.map(tool => ({
    slug: tool.data.slug,
    name: tool.data.name,
    description: tool.data.description,
    category: tool.data.category,
    pricing: tool.data.pricing,
    rating: tool.data.rating,
    features: tool.data.features,
    pros: tool.data.pros,
    cons: tool.data.cons,
    pricing_tiers: tool.data.pricing_tiers,
    affiliate_url: tool.data.affiliate_url,
    website: tool.data.website,
    featured: tool.data.featured,
  }));
  return new Response(JSON.stringify(detail));
}
