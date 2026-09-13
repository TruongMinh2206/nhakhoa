# -*- coding: utf-8 -*-
import re

frag_path = r"d:\Work\clone\clone\website\greenfield_main.html"
with open(frag_path, "r", encoding="utf-8") as f:
    frag = f.read()

# Replace any dark input styles in form with clean ivory/white styles
frag = frag.replace('style="background: #25262c; color: #fff;"', 'style="background: #FFFDF6; color: #18181b;"')
frag = frag.replace('style="background: #193021; color: #fff;"', 'style="background: #FFFDF6; color: #18181b;"')

# Replace reviewer avatar color to warm gold #EABF0E with dark text
frag = frag.replace('style="background:#2D6A4F;"', 'style="background:#EABF0E; color:#18181b; font-weight:800;"')
frag = frag.replace('style="background:#c9964a;"', 'style="background:#EABF0E; color:#18181b; font-weight:800;"')

with open(frag_path, "w", encoding="utf-8") as f:
    f.write(frag)
print("Updated greenfield_main.html")

idx_path = r"d:\Work\clone\clone\website\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

m_tag = '<main id="main-content"'
f_tag = '<footer class="wrap-footer">'
m_pos = idx_content.find(m_tag)
f_pos = idx_content.find(f_tag)

if m_pos != -1 and f_pos != -1:
    idx_content = idx_content[:m_pos] + frag + "\n" + idx_content[f_pos:]
    print("Re-injected updated fragment into index.html")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated index.html")

