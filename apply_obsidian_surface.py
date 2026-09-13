# -*- coding: utf-8 -*-
import re
import os

# 1. Update greenfield-theme.css with Obsidian Dark Palette
gf_css_path = r"d:\Work\clone\clone\website\assets\css\greenfield-theme.css"
with open(gf_css_path, "r", encoding="utf-8") as f:
    gf_css = f.read()

# Replace tokens
gf_css = re.sub(r'--gf-bg-darkest:\s*#[0-9a-fA-F]+;', '--gf-bg-darkest: #0f1012;', gf_css)
gf_css = re.sub(r'--gf-bg-dark:\s*#[0-9a-fA-F]+;', '--gf-bg-dark: #151619;', gf_css)
gf_css = re.sub(r'--gf-bg-surface:\s*#[0-9a-fA-F]+;', '--gf-bg-surface: #1c1d22;', gf_css)
gf_css = re.sub(r'--gf-bg-charcoal:\s*#[0-9a-fA-F]+;', '--gf-bg-charcoal: #121316;', gf_css)

# Replace hero overlay green rgba(12, 28, 17, ...) with obsidian charcoal rgba(15, 16, 18, ...)
gf_css = re.sub(r'rgba\(\s*12\s*,\s*28\s*,\s*17\s*,', 'rgba(15, 16, 18,', gf_css)

# Replace image background placeholders
gf_css = gf_css.replace('#0c1810', '#16171b')
gf_css = gf_css.replace('#162419', '#16171b')

# Replace footer background
gf_css = gf_css.replace('#08140c', '#0b0c0e')
gf_css = gf_css.replace('#050d08', '#070809')

# Replace text on primary button to dark obsidian
gf_css = gf_css.replace('color: #0c1c11', 'color: #0f1012')

with open(gf_css_path, "w", encoding="utf-8") as f:
    f.write(gf_css)
print("Updated greenfield-theme.css with Obsidian Surface #1c1d22")

# 2. Update greenfield_main.html & index.html input backgrounds
frag_path = r"d:\Work\clone\clone\website\greenfield_main.html"
with open(frag_path, "r", encoding="utf-8") as f:
    frag = f.read()

frag = frag.replace('#193021', '#25262c')

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
else:
    idx_content = idx_content.replace('#193021', '#25262c')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated index.html with Obsidian Surface #1c1d22")

