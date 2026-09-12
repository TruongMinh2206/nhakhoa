import os
import re
import glob
import json
import urllib.request
import urllib.parse

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "website")
BASE_URL = "https://nhakhoakimdung.vn"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("[1/5] Dang lay template giao dien (CSS, Header, Footer) tu website goc...")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(f"{BASE_URL}/", headers=headers)
try:
    with urllib.request.urlopen(req, timeout=15) as res:
        live_html = res.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error fetching live site: {e}")
    live_html = ""

# Extract <head> styles and scripts
head_inner = ""
header_block = ""
footer_block = ""
bottom_scripts = ""

if live_html:
    # Extract head content
    head_m = re.search(r'<head>(.*?)</head>', live_html, re.DOTALL | re.IGNORECASE)
    if head_m:
        head_inner = head_m.group(1)
        # Remove <base ...> if present so it doesn't break local relative routing
        head_inner = re.sub(r'<base[^>]*>', '', head_inner, flags=re.IGNORECASE)
        # Ensure relative asset links in head have absolute domain
        head_inner = re.sub(r'href="(assets/[^"]+)"', rf'href="{BASE_URL}/\1"', head_inner)
        head_inner = re.sub(r'src="(assets/[^"]+)"', rf'src="{BASE_URL}/\1"', head_inner)

    # Extract <header>...</header>
    header_m = re.search(r'(<header>.*?</header>)', live_html, re.DOTALL | re.IGNORECASE)
    if header_m:
        header_block = header_m.group(1)

    # Extract <footer>...</footer>
    footer_m = re.search(r'(<footer.*?</footer\s*>)', live_html, re.DOTALL | re.IGNORECASE)
    if footer_m:
        footer_block = footer_m.group(1)

    # Extract scripts after footer
    footer_end_pos = live_html.find('</footer')
    if footer_end_pos != -1:
        after_footer = live_html[footer_end_pos:]
        script_matches = re.findall(r'<script.*?</script>', after_footer, re.DOTALL | re.IGNORECASE)
        extra_widgets = re.findall(r'<(div|ul)[^>]+id="(?:hotline|social|toolbar)"[^>]*>.*?</\1>', after_footer, re.DOTALL | re.IGNORECASE)
        bottom_scripts = "\n".join(extra_widgets + script_matches)
        bottom_scripts = re.sub(r'src="(assets/[^"]+)"', rf'src="{BASE_URL}/\1"', bottom_scripts)
        bottom_scripts = re.sub(r'src="(\./assets/[^"]+)"', rf'src="{BASE_URL}/\1"', bottom_scripts)

print("[2/5] Dang quet cac file JSON crawl duoc...")
json_files = glob.glob(os.path.join(WORKSPACE_DIR, "**/*.json"), recursive=True)
json_files = [f for f in json_files if "metadata" in open(f, encoding='utf-8', errors='ignore').read(500)]

print(f"Tim thay {len(json_files)} trang crawl.")

url_to_html = {}
file_entries = []

for jf in json_files:
    try:
        with open(jf, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        continue
    
    meta = data.get('metadata', {})
    url = meta.get('url', '').strip()
    if not url:
        continue

    parsed = urllib.parse.urlparse(url)
    slug = parsed.path.strip('/')
    
    if not slug:
        html_name = "index.html"
    else:
        safe_slug = re.sub(r'[^a-zA-Z0-9_\-]', '_', slug)
        html_name = f"{safe_slug}.html"

    url_to_html[url] = html_name
    url_to_html[f"{BASE_URL}/{slug}"] = html_name
    url_to_html[f"/{slug}"] = html_name
    if slug:
        url_to_html[slug] = html_name

    file_entries.append((jf, data, html_name, url, slug))

print(f"[3/5] Da lap ban do {len(file_entries)} trang HTML.")

def rewrite_assets_and_links(html_text):
    # 1. Convert relative asset URLs to absolute live site URLs
    html_text = re.sub(r'(src|href|srcset)=["\'](assets/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)
    html_text = re.sub(r'(src|href|srcset)=["\'](upload/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)
    html_text = re.sub(r'(src|href|srcset)=["\'](thumbs/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)
    html_text = re.sub(r'(src|href|srcset)=["\']/(assets/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)
    html_text = re.sub(r'(src|href|srcset)=["\']/(upload/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)
    html_text = re.sub(r'(src|href|srcset)=["\']/(thumbs/[^"\']+)["\']', rf'\1="{BASE_URL}/\2"', html_text)

    # 2. Fix url('assets/...') in styles
    html_text = re.sub(r'url\(["\']?(assets/[^"\')]+)["\']?\)', rf'url("{BASE_URL}/\1")', html_text)
    html_text = re.sub(r'url\(["\']?(upload/[^"\')]+)["\']?\)', rf'url("{BASE_URL}/\1")', html_text)

    # 3. Rewrite internal page links to .html files
    for orig_url, target_file in sorted(url_to_html.items(), key=lambda x: -len(x[0])):
        if not orig_url:
            continue
        pattern = rf'href=["\']{re.escape(orig_url)}/?["\']'
        html_text = re.sub(pattern, f'href="{target_file}"', html_text)

    # Fix home links href="" or href="/"
    html_text = re.sub(r'href=["\'](https://nhakhoakimdung\.vn/?|/|)#?["\']', 'href="index.html"', html_text)

    return html_text

def remove_addtoany(text):
    while True:
        start = text.find('<div id="addtoany"')
        if start == -1:
            start = text.find("<div id='addtoany'")
        if start == -1:
            break
        
        pos = start
        depth = 0
        end_pos = -1
        while pos < len(text):
            if text[pos:pos+4] == '<div':
                depth += 1
                pos += 4
            elif text[pos:pos+6] == '</div>':
                depth -= 1
                pos += 6
                if depth == 0:
                    end_pos = pos
                    break
            else:
                pos += 1
        
        if end_pos != -1:
            text = text[:start].rstrip(' \t') + text[end_pos:]
        else:
            break
    return text

def remove_debug_panels(text):
    # Error pages from the source site can append Laravel debug panels to the crawled body.
    debug_start = re.search(r'<section[^>]*>\s*<a[^>]+id=["\'](?:stack|context)["\'][^>]*>', text, re.IGNORECASE)
    if debug_start:
        text = text[:debug_start.start()].rstrip()
    return text

if header_block:
    header_block = rewrite_assets_and_links(header_block)
    # Remove hardcoded active class so page-specific matching works cleanly
    header_block = re.sub(r'(<a\s+class="[^"]*?)active\s*([^"]*?"\s+href="index\.html")', r'\1\2', header_block)
if footer_block:
    footer_block = rewrite_assets_and_links(footer_block)

print("[4/5] Dang render va xuat cac file HTML...")

count = 0
for jf, data, html_name, page_url, slug in file_entries:
    meta = data.get('metadata', {})
    title = meta.get('title') or "Nha Khoa Kim Dung"
    desc = meta.get('description') or ""
    raw_html = data.get('html', '')

    body_m = re.search(r'<body[^>]*>(.*?)</body>', raw_html, re.DOTALL | re.IGNORECASE)
    if body_m:
        content = body_m.group(1).strip()
    else:
        content = raw_html

    # Clean recaptcha / iframe / AddToAny bloat
    content = remove_addtoany(content)
    content = remove_debug_panels(content)
    content = re.sub(r'<div class="rc-anchor.*?</div></div></div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<textarea id="g-recaptcha-response.*?</textarea>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div style="display: none;" data-original-tag="iframe"></div>', '', content)

    page_header = ""
    if '<header' not in content.lower() and header_block:
        page_header = header_block

    page_footer = ""
    if '<footer' not in content.lower() and footer_block:
        page_footer = footer_block

    content = rewrite_assets_and_links(content)

    final_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
{head_inner}
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" crossorigin="anonymous">
    <link href="assets/css/ui-ux-pro-max.css" rel="stylesheet">
</head>
<body>
{page_header}
<main id="main-content">
{content}
</main>
{page_footer}
{bottom_scripts}
<script src="assets/js/ui-ux-pro-max.js" defer></script>
</body>
</html>
"""

    out_path = os.path.join(OUTPUT_DIR, html_name)
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(final_html)
    count += 1

print(f"[5/5] Hoan thanh! Da tao {count} file HTML vao thu muc: {OUTPUT_DIR}")

