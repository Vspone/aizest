import re, os

overlong = []
for root, dirs, files in os.walk('src/pages'):
    for f in files:
        if not f.endswith('.astro'): continue
        path = os.path.join(root, f)
        with open(path, 'r', errors='ignore') as fh:
            content = fh.read()
        for m in re.finditer(r'description="([^"]{150,})"', content):
            overlong.append((len(m.group(1)), path, m.group(1)[:80]))

overlong.sort(key=lambda x: -x[0])
print(f"Descriptions > 150 chars after fix: {len(overlong)}")
for length, path, preview in overlong:
    print(f"  {length}ch  {os.path.basename(path):45s} {preview}...")
if not overlong:
    print("  ✅ All descriptions under 150 chars!")
