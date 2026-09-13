# -*- coding: utf-8 -*-
import re
import os

font_face_block = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700&display=swap');

@font-face {
  font-family: 'MontserratBold';
  src: local('Montserrat Bold'), local('Montserrat-Bold'),
       url('https://fonts.gstatic.com/s/montserrat/v26/JTUSjIg1_i6t8kCHKm459WlhyyTh89Y.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'MontserratRegular';
  src: local('Montserrat Regular'), local('Montserrat-Regular'),
       url('https://fonts.gstatic.com/s/montserrat/v26/JTUSjIg1_i6t8kCHKm459WlhyyTh89Y.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
"""

# 1. Update greenfield-theme.css
gf_css_path = r"d:\Work\clone\clone\website\assets\css\greenfield-theme.css"
with open(gf_css_path, "r", encoding="utf-8") as f:
    gf_css = f.read()

# Replace top imports
gf_css = re.sub(r"@import\s+url\('https://fonts\.googleapis\.com/[^']*'\);", "", gf_css)
gf_css = font_face_block.strip() + "\n\n" + gf_css.strip()

# Replace font variables
gf_css = re.sub(
    r"--gf-font-display:[^;]+;",
    "--gf-font-display: 'MontserratBold', 'Montserrat', sans-serif;",
    gf_css
)
gf_css = re.sub(
    r"--gf-font-sans:[^;]+;",
    "--gf-font-sans: 'MontserratRegular', 'Montserrat', sans-serif;",
    gf_css
)

# Replace any lingering Cormorant or Plus Jakarta Sans
gf_css = gf_css.replace("'Cormorant Garamond', Georgia, serif", "'MontserratBold', 'Montserrat', sans-serif")
gf_css = gf_css.replace("'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", "'MontserratRegular', 'Montserrat', sans-serif")
gf_css = gf_css.replace("var(--gf-font-display)", "'MontserratBold', 'Montserrat', sans-serif")
gf_css = gf_css.replace("var(--gf-font-sans)", "'MontserratRegular', 'Montserrat', sans-serif")

# Ensure headings strictly use MontserratBold
gf_css = re.sub(
    r"(\.gf-theme-root\s+h1[^{]*\{[^}]*?font-family:\s*)[^;!]+(!important)?;",
    r"\g<1>'MontserratBold', 'Montserrat', sans-serif !important;",
    gf_css
)

# Ensure body and paragraphs strictly use MontserratRegular
gf_css = re.sub(
    r"(\.gf-theme-root\s+p[^{]*\{[^}]*?font-family:\s*)[^;!]+(!important)?;",
    r"\g<1>'MontserratRegular', 'Montserrat', sans-serif !important;",
    gf_css
)

with open(gf_css_path, "w", encoding="utf-8") as f:
    f.write(gf_css)
print("Updated greenfield-theme.css with MontserratBold & MontserratRegular")


# 2. Update ui-ux-pro-max.css
uupm_css_path = r"d:\Work\clone\clone\website\assets\css\ui-ux-pro-max.css"
with open(uupm_css_path, "r", encoding="utf-8") as f:
    uupm_css = f.read()

# Make sure font faces exist at top
if "@font-face" not in uupm_css:
    uupm_css = font_face_block.strip() + "\n\n" + uupm_css

# Replace font variables
uupm_css = re.sub(
    r"--uupm-font-heading:[^;]+;",
    "--uupm-font-heading: 'MontserratBold', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;",
    uupm_css
)
uupm_css = re.sub(
    r"--uupm-font-body:[^;]+;",
    "--uupm-font-body: 'MontserratRegular', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;",
    uupm_css
)

# Headings rule
old_heading_rule = re.compile(
    r'h1,\s*h2,\s*h3,\s*h4,\s*h5,\s*h6,\s*\.title-main[^{]*\{[^}]*?\}',
    re.DOTALL
)

new_heading_rule = """h1, h2, h3, h4, h5, h6,
.title-main, .title-about-us, .name-service, .title-detail h1,
[class*="title-"], [class*="heading-"], .name-doctor, .name-news,
.gf-title-display, .gf-hero-title, .gf-service-title, .gf-why-title,
.gf-patient-name, .gf-doctor-name, .gf-cta-box h3, .gf-calc-label {
  font-family: 'MontserratBold', 'Montserrat', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: -0.01em;
}"""

if old_heading_rule.search(uupm_css):
    uupm_css = old_heading_rule.sub(new_heading_rule, uupm_css)
else:
    uupm_css += "\n" + new_heading_rule

# Body / Text rule
old_body_rule = re.compile(
    r'body,\s*button,\s*input,\s*select,\s*textarea,\s*label,\s*p,\s*a[^{]*\{[^}]*?\}',
    re.DOTALL
)

new_body_rule = """body, button, input, select, textarea, label,
p, a, span:not(.fa):not([class*="fa-"]):not([class*="icon"]):not(.scroll),
div:not(.fa):not([class*="fa-"]):not([class*="icon"]):not(.swiper-button-prev):not(.swiper-button-next),
li:not(.fa):not([class*="fa-"]), td, th,
.gf-desc-lead, .gf-hero-desc, .gf-service-desc, .gf-why-desc,
.gf-quote-text, .gf-review-text, .gf-doctor-desc, .gf-calc-detail {
  font-family: 'MontserratRegular', 'Montserrat', sans-serif !important;
}"""

if old_body_rule.search(uupm_css):
    uupm_css = old_body_rule.sub(new_body_rule, uupm_css)
else:
    uupm_css += "\n" + new_body_rule

with open(uupm_css_path, "w", encoding="utf-8") as f:
    f.write(uupm_css)
print("Updated ui-ux-pro-max.css with MontserratBold & MontserratRegular")

