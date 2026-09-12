import os
import glob
import re

WEBSITE_DIR = r"c:\Users\ADMIN\Downloads\clone\clone\website"

html_files = glob.glob(os.path.join(WEBSITE_DIR, "*.html"))

def get_active_tab(filename):
    fn = os.path.basename(filename).lower()
    if fn == "index.html":
        return "home"
    elif "gioi-thieu" in fn:
        return "intro"
    elif "bang-gia" in fn:
        return "pricing"
    elif "doi-ngu" in fn or "bac-si" in fn or "ban-tran-bao-han" in fn or "co-nga-uan" in fn or "thuy-dung" in fn or "anh-nguyen-cong-phuong" in fn:
        return "team"
    elif "dat-lich" in fn:
        return "booking"
    elif "lien-he" in fn:
        return "contact"
    elif any(k in fn for k in ["tin-tuc", "kien-thuc", "bai-viet", "bien-chung", "hau-qua", "nguyen-nhan", "ly-do", "vi-sao", "bi-quyet", "bat-mi", "hoi-mieng", "huong-dan", "ky-ket", "giai-ma"]):
        return "news"
    else:
        # services or default
        return "service"

updated = 0
for filepath in html_files:
    filename = os.path.basename(filepath)
    active_key = get_active_tab(filename)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Build exact menu block
    act = {
        "home": "active" if active_key == "home" else "",
        "intro": "active" if active_key == "intro" else "",
        "service": "active" if active_key == "service" else "",
        "pricing": "active" if active_key == "pricing" else "",
        "team": "active" if active_key == "team" else "",
        "booking": "active" if active_key == "booking" else "",
        "news": "active" if active_key == "news" else "",
        "contact": "active" if active_key == "contact" else ""
    }

    new_ulmn = f"""<ul class="flex flex-wrap items-center justify-between ulmn gap-10">
<li><a class="transition {act['home']}".strip() href="index.html" title="Trang chủ">Trang chủ</a></li>
<li><a class="transition {act['intro']}".strip() href="gioi-thieu.html" title="Giới thiệu">Giới thiệu</a></li>
<li><a class="transition {act['service']}".strip() href="dich-vu.html" title="Dịch vụ">Dịch vụ</a></li>
<li><a class="transition {act['pricing']}".strip() href="bang-gia.html" title="Bảng giá">Bảng giá</a></li>
<li><a class="transition {act['team']}".strip() href="doi-ngu.html" title="Đội ngũ">Đội ngũ</a></li>
<li><a class="transition {act['booking']}".strip() href="dat-lich.html" title="Đặt lịch">Đặt lịch</a></li>
<li><a class="transition {act['news']}".strip() href="tin-tuc.html" title="Tin tức">Tin tức</a></li>
<li><a class="transition {act['contact']}".strip() href="lien-he.html" title="Liên hệ">Liên hệ</a></li>
</ul>""".replace(".strip()", "")

    # Regex replace ulmn
    ulmn_pattern = r'<ul class="[^"]*ulmn[^"]*">.*?</ul>'
    if re.search(ulmn_pattern, content, flags=re.DOTALL):
        content = re.sub(ulmn_pattern, new_ulmn, content, count=1, flags=re.DOTALL)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1

print(f"Updated menu with accurate active tabs for {updated} files!")
