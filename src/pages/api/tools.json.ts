import { getCollection } from 'astro:content';

export const prerender = true;

export async function GET() {
  const tools = await getCollection('tools');
  const index = tools.map(tool => ({
    name: tool.data.name,
    slug: tool.data.slug,
    description: tool.data.description,
    category: tool.data.category,
  }));
  return new Response(JSON.stringify(index));
}
