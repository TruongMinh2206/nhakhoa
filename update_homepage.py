# -*- coding: utf-8 -*-
import re
import os

index_path = r"d:\Work\clone\clone\website\index.html"
backup_path = r"d:\Work\clone\clone\website\index.html.bak"
main_fragment_path = r"d:\Work\clone\clone\website\greenfield_main.html"

# Read original backup
with open(backup_path, "r", encoding="utf-8") as f:
    orig = f.read()

with open(main_fragment_path, "r", encoding="utf-8") as f:
    new_main = f.read()

# 1. Add greenfield-theme.css into <head>
css_link = '    <link href="assets/css/greenfield-theme.css" rel="stylesheet">\n'
if "assets/css/greenfield-theme.css" not in orig:
    if 'assets/css/ui-ux-pro-max.css' in orig:
        orig = orig.replace(
            '<link href="assets/css/ui-ux-pro-max.css" rel="stylesheet">',
            '<link href="assets/css/ui-ux-pro-max.css" rel="stylesheet">\n' + css_link
        )
    else:
        orig = orig.replace('</head>', css_link + '</head>')

# 2. Find exact <main id="main-content"> and <footer class="wrap-footer">
m_tag = '<main id="main-content">'
f_tag = '<footer class="wrap-footer">'
m_pos = orig.find(m_tag)
f_pos = orig.find(f_tag)

if m_pos == -1 or f_pos == -1:
    raise ValueError(f"Could not find tags: m_pos={m_pos}, f_pos={f_pos}")

print(f"Replacing from offset {m_pos} to {f_pos}")
updated_html = orig[:m_pos] + new_main + "\n" + orig[f_pos:]

# 3. Clean up stray 'div' before <script> after footer
updated_html = re.sub(r'</footer>\s*div\s*<script>', '</footer>\n<script>', updated_html)

# 4. Add helper script for price tabs & booking submit
helper_script = """
<script>
function switchGfPriceTab(idx, btn) {
  document.querySelectorAll('.gf-price-pane').forEach((p, i) => {
    p.style.display = (i === idx) ? 'block' : 'none';
  });
  document.querySelectorAll('.gf-calc-tab').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
}

function handleGfBookingSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('gf-name') ? document.getElementById('gf-name').value.trim() : '';
  const phone = document.getElementById('gf-phone') ? document.getElementById('gf-phone').value.trim() : '';
  const service = document.getElementById('gf-service') ? document.getElementById('gf-service').value : '';
  if (!phone) {
    alert('Vui lòng nhập số điện thoại để phòng khám liên hệ tư vấn.');
    return;
  }
  if (window.showToast) {
    window.showToast('🎉 Cảm ơn quý khách ' + name + '! Nha Khoa Kim Dung đã ghi nhận lịch hẹn [' + service + ']. Bác sĩ sẽ liên hệ ' + phone + ' trong 15 phút.');
  } else {
    alert('🎉 Cảm ơn quý khách ' + name + '! Nha Khoa Kim Dung đã ghi nhận lịch hẹn [' + service + ']. Bác sĩ sẽ liên hệ ' + phone + ' trong ít phút.');
  }
  e.target.reset();
}
</script>
"""

if "switchGfPriceTab" not in updated_html:
    updated_html = updated_html.replace("</body>", helper_script + "\n</body>")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Successfully replaced entire main body with Greenfield structure!")

