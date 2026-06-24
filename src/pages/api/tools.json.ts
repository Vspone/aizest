import { getCollection } from 'astro:content';

export const prerender = true;

export async function GET() {
  const tools = await getCollection('tools');
  const index = tools.map(tool => ({
    name: tool.data.name,
    slug: tool.data.slug,
    description: tool.data.description,
    category: tool.data.category,
    pricing: tool.data.pricing,
    rating: tool.data.rating,
    features: tool.data.features?.slice(0, 3) || [],
    featured: tool.data.featured || false,
  }));
  return new Response(JSON.stringify(index));
}
