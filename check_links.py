import os
import re
from collections import defaultdict

dist = 'dist'
html_files = []
for root, dirs, files in os.walk(dist):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f'Found {len(html_files)} HTML files')

broken = []
external_count = 0
vague_anchors = []
internal_link_count = 0

for html_file in html_files:
    rel_path = os.path.relpath(html_file, dist)
    with open(html_file, 'r', errors='ignore') as f:
        content = f.read()
    
    for match in re.finditer(r'href="([^"]+)"', content):
        href = match.group(1)
        
        if href.startswith('http://') or href.startswith('https://'):
            external_count += 1
            continue
        if href.startswith('mailto:') or href.startswith('#') or href.startswith('//'):
            continue
        if not href.startswith('/'):
            continue
        
        internal_link_count += 1
        
        # Normalize
        target = href
        if target.endswith('/'):
            target = target + 'index.html'
        elif not target.endswith(('.html', '.xml', '.css', '.js', '.svg', '.png', '.jpg', '.webp', '.ico', '.json', '.txt')):
            target = target.rstrip('/') + '/index.html'
        
        full_path = os.path.join(dist, target.lstrip('/'))
        if not os.path.exists(full_path):
            broken.append((href, rel_path))

print(f'Internal links checked: {internal_link_count}')
print(f'External links skipped: {external_count}')
print(f'Broken internal links: {len(broken)}')
if broken:
    print('--- BROKEN LINKS ---')
    for href, source in broken:
        print(f'  {href}  (from {source})')
else:
    print('  ✅ No broken links found!')

# Check anchor text quality
for html_file in html_files:
    rel_path = os.path.relpath(html_file, dist)
    with open(html_file, 'r', errors='ignore') as f:
        content = f.read()
    for match in re.finditer(r'<a\s+href="([^"]*)"[^>]*>([^<]+)</a>', content):
        text = match.group(2).strip().lower()
        href = match.group(1)
        if href.startswith('http') or href.startswith('mailto') or href.startswith('#') or href.startswith('//'):
            continue
        if text in ['click here', 'here', 'this', 'link', 'more', 'read more', 'go', 'this link']:
            vague_anchors.append((text, href, rel_path))

print(f'\nVague anchor texts found: {len(vague_anchors)}')
if vague_anchors:
    for text, href, source in vague_anchors:
        print(f'  "{text}" -> {href}  (from {source})')
else:
    print('  ✅ No vague anchor texts found!')
