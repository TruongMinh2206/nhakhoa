# -*- coding: utf-8 -*-
import re
import os

MAIN_COLOR = "#EABF0E"
MAIN_HOVER = "#D4AC0B"
MAIN_DARK = "#B89307"
MAIN_LIGHT = "#FEFCE8"
MAIN_100 = "#FEF08A"
MAIN_SECONDARY = "#FDE047"

# 1. Update ui-ux-pro-max.css
uupm_css_path = r"d:\Work\clone\clone\website\assets\css\ui-ux-pro-max.css"
with open(uupm_css_path, "r", encoding="utf-8") as f:
    uupm_css = f.read()

# Replace root variables
uupm_css = re.sub(r'--uupm-primary:\s*#[0-9a-fA-F]+;', f'--uupm-primary: {MAIN_COLOR};', uupm_css)
uupm_css = re.sub(r'--uupm-primary-hover:\s*#[0-9a-fA-F]+;', f'--uupm-primary-hover: {MAIN_HOVER};', uupm_css)
uupm_css = re.sub(r'--uupm-primary-dark:\s*#[0-9a-fA-F]+;', f'--uupm-primary-dark: {MAIN_DARK};', uupm_css)
uupm_css = re.sub(r'--uupm-primary-light:\s*#[0-9a-fA-F]+;', f'--uupm-primary-light: {MAIN_LIGHT};', uupm_css)
uupm_css = re.sub(r'--uupm-primary-100:\s*#[0-9a-fA-F]+;', f'--uupm-primary-100: {MAIN_100};', uupm_css)
uupm_css = re.sub(r'--uupm-secondary:\s*#[0-9a-fA-F]+;', f'--uupm-secondary: {MAIN_SECONDARY};', uupm_css)
uupm_css = re.sub(r'--uupm-border-focus:\s*#[0-9a-fA-F]+;', f'--uupm-border-focus: {MAIN_COLOR};', uupm_css)

# Replace remaining direct color references in ui-ux-pro-max.css
uupm_css = uupm_css.replace("#0EA5E9", MAIN_COLOR)
uupm_css = uupm_css.replace("#0284C7", MAIN_HOVER)
uupm_css = uupm_css.replace("#0369A1", MAIN_DARK)

# Replace shadow rgba(14, 165, 233, ...) with rgba(234, 191, 14, ...)
uupm_css = re.sub(r'rgba\(\s*14\s*,\s*165\s*,\s*233\s*,', 'rgba(234, 191, 14,', uupm_css)

# Update menu text color on yellow background for perfect contrast
uupm_css = re.sub(
    r'(\.menu\s+ul\.ulmn\s*>\s*li\s*>\s*a\s*\{[^}]*?color:\s*)#FFFFFF(\s*!important;)',
    r'\g<1>#1a1a1a\g<2>',
    uupm_css
)

# Button text on gold gradient: make text dark for sharp legibility
uupm_css = re.sub(
    r'(\.uupm-btn-primary[^{]*\{[^}]*?color:\s*)#FFFFFF(\s*!important;)',
    r'\g<1>#122417\g<2>',
    uupm_css
)

# Modal header text on gold
uupm_css = re.sub(
    r'(\.uupm-modal-header\s+h3\s*\{[^}]*?color:\s*)#FFFFFF(\s*!important;)',
    r'\g<1>#122417\g<2>',
    uupm_css
)
uupm_css = re.sub(
    r'(\.uupm-modal-close\s*\{[^}]*?color:\s*)#FFFFFF(\s*!important;)',
    r'\g<1>#122417\g<2>',
    uupm_css
)

with open(uupm_css_path, "w", encoding="utf-8") as f:
    f.write(uupm_css)
print("Updated ui-ux-pro-max.css with #EABF0E")

# 2. Update greenfield-theme.css
gf_css_path = r"d:\Work\clone\clone\website\assets\css\greenfield-theme.css"
with open(gf_css_path, "r", encoding="utf-8") as f:
    gf_css = f.read()

# Replace tokens
gf_css = re.sub(r'--gf-primary:\s*#[0-9a-fA-F]+;', f'--gf-primary: {MAIN_COLOR};', gf_css)
gf_css = re.sub(r'--gf-primary-hover:\s*#[0-9a-fA-F]+;', f'--gf-primary-hover: {MAIN_HOVER};', gf_css)
gf_css = re.sub(r'--gf-primary-light:\s*#[0-9a-fA-F]+;', f'--gf-primary-light: {MAIN_100};', gf_css)
gf_css = re.sub(r'--gf-mint:\s*#[0-9a-fA-F]+;', f'--gf-mint: {MAIN_COLOR};', gf_css)
gf_css = re.sub(r'--gf-mint-glow:\s*#[0-9a-fA-F]+;', f'--gf-mint-glow: {MAIN_SECONDARY};', gf_css)
gf_css = re.sub(r'--gf-gold:\s*#[0-9a-fA-F]+;', f'--gf-gold: {MAIN_COLOR};', gf_css)
gf_css = re.sub(r'--gf-gold-hover:\s*#[0-9a-fA-F]+;', f'--gf-gold-hover: {MAIN_HOVER};', gf_css)
gf_css = re.sub(r'--gf-gold-light:\s*#[0-9a-fA-F]+;', f'--gf-gold-light: {MAIN_COLOR};', gf_css)
gf_css = re.sub(r'--gf-border-accent:\s*[^;]+;', '--gf-border-accent: rgba(234, 191, 14, 0.45);', gf_css)

# Replace primary button text to dark on bright yellow background
gf_css = re.sub(
    r'(\.gf-btn-primary\s*\{[^}]*?color:\s*)#ffffff(\s*!important;)',
    r'\g<1>#0c1c11\g<2>',
    gf_css
)
gf_css = re.sub(
    r'(\.gf-btn-primary:hover\s*\{[^}]*?color:\s*)#ffffff(\s*!important;)',
    r'\g<1>#0c1c11\g<2>',
    gf_css
)
gf_css = re.sub(
    r'(\.gf-form-submit\s*\{[^}]*?color:\s*)#ffffff(\s*!important;)',
    r'\g<1>#0c1c11\g<2>',
    gf_css
)
gf_css = re.sub(
    r'(\.gf-calc-tab\.active[^{]*\{[^}]*?color:\s*)#ffffff(\s*!important;)',
    r'\g<1>#0c1c11\g<2>',
    gf_css
)
gf_css = re.sub(
    r'(\.gf-service-badge\s*\{[^}]*?color:\s*)[^;]+;',
    r'\g<1>#0c1c11 !important;',
    gf_css
)

# Replace shadow rgba(45, 106, 79, ...) with gold rgba(234, 191, 14, ...)
gf_css = re.sub(r'rgba\(\s*45\s*,\s*106\s*,\s*79\s*,', 'rgba(234, 191, 14,', gf_css)
gf_css = re.sub(r'rgba\(\s*126\s*,\s*207\s*,\s*160\s*,', 'rgba(234, 191, 14,', gf_css)

with open(gf_css_path, "w", encoding="utf-8") as f:
    f.write(gf_css)
print("Updated greenfield-theme.css with #EABF0E")

# 3. Update greenfield_main.html inline styles and index.html
def replace_inline_greens(text):
    text = text.replace("#6EE7B7", MAIN_COLOR)
    text = text.replace("#7ecfa0", MAIN_COLOR)
    text = text.replace("#2D6A4F", MAIN_COLOR)
    text = text.replace("#c9964a", MAIN_COLOR)
    text = text.replace("#f59e0b", MAIN_COLOR)
    return text

main_frag_path = r"d:\Work\clone\clone\website\greenfield_main.html"
with open(main_frag_path, "r", encoding="utf-8") as f:
    frag = f.read()

frag = replace_inline_greens(frag)
with open(main_frag_path, "w", encoding="utf-8") as f:
    f.write(frag)
print("Updated greenfield_main.html with #EABF0E")

index_path = r"d:\Work\clone\clone\website\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

m_tag = '<main id="main-content"'
f_tag = '<footer class="wrap-footer">'
m_pos = idx_content.find(m_tag)
f_pos = idx_content.find(f_tag)

if m_pos != -1 and f_pos != -1:
    idx_content = idx_content[:m_pos] + frag + "\n" + idx_content[f_pos:]
    print("Re-injected updated fragment into index.html")
else:
    idx_content = replace_inline_greens(idx_content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated index.html with #EABF0E")

