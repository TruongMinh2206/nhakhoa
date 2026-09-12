import os
import re
import glob

WEBSITE_DIR = r"c:\Users\ADMIN\Downloads\clone\clone\website"

# 1. New Clean Pricing Content for bang-gia.html
PRICING_HTML = """
<div class="wrap-container py-12" style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;">
    <!-- Breadcrumb & Title -->
    <div style="text-align: center; margin-bottom: 48px;">
        <span class="uupm-badge uupm-badge-gold" style="margin-bottom: 12px; font-size: 13px;">Minh Bạch - Tiêu Chuẩn Bộ Y Tế</span>
        <h1 style="font-size: 32px; font-weight: 800; color: #0F172A; margin: 12px 0 16px 0;">BẢNG GIÁ DỊCH VỤ NHA KHOA KIM DUNG</h1>
        <p style="color: #64748B; font-size: 16px; max-width: 720px; margin: 0 auto; line-height: 1.6;">
            Cam kết chi phí minh bạch, tư vấn phác đồ điều trị tận tâm trước khi thực hiện. Áp dụng chính sách trả góp 0% lãi suất cho niềng răng và trồng răng Implant.
        </p>
    </div>

    <!-- 3 Highlighted Promo Cards -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 48px;">
        <div class="uupm-pricing-card">
            <span class="uupm-badge" style="width: fit-content; margin-bottom: 12px;">Ưu Đãi Đặc Biệt</span>
            <h3 style="font-size: 22px; margin-bottom: 8px;">Niềng Răng Thẩm Mỹ</h3>
            <p style="color: #64748B; font-size: 14px; margin-bottom: 16px;">Công nghệ chỉnh nha 3D cá nhân hóa - Thấy trước kết quả sau 7 ngày.</p>
            <div style="margin-bottom: 20px;">
                <span style="font-size: 13px; color: #94A3B8;">Chỉ từ</span>
                <div class="uupm-price-tag" style="font-size: 28px; color: #0EA5E9;">18.000.000đ</div>
                <span style="font-size: 13px; color: #10B981; font-weight: 600;">Trả góp 0% từ 1 triệu/tháng</span>
            </div>
            <button type="button" class="uupm-btn uupm-btn-primary" style="margin-top: auto;">Nhận Báo Giá Chi Tiết</button>
        </div>

        <div class="uupm-pricing-card featured">
            <span class="uupm-pricing-badge">Được Chọn Nhiều Nhất</span>
            <span class="uupm-badge" style="width: fit-content; margin-bottom: 12px;">Bảo Hành 15 Năm</span>
            <h3 style="font-size: 22px; margin-bottom: 8px;">Trồng Răng Implant</h3>
            <p style="color: #64748B; font-size: 14px; margin-bottom: 16px;">Phục hình răng đã mất, ăn nhai chắc khỏe như răng thật trọn đời.</p>
            <div style="margin-bottom: 20px;">
                <span style="font-size: 13px; color: #94A3B8;">Chỉ từ</span>
                <div class="uupm-price-tag" style="font-size: 28px; color: #0284C7;">12.500.000đ <span style="font-size: 14px; font-weight: normal; color: #64748B;">/ Trụ</span></div>
                <span style="font-size: 13px; color: #10B981; font-weight: 600;">Tặng kèm Abutment & Răng sứ</span>
            </div>
            <button type="button" class="uupm-btn uupm-btn-accent" style="margin-top: auto;">Đặt Hẹn Khám & Chụp CT 3D</button>
        </div>

        <div class="uupm-pricing-card">
            <span class="uupm-badge" style="width: fit-content; margin-bottom: 12px;">Đẳng Cấp Nụ Cười</span>
            <h3 style="font-size: 22px; margin-bottom: 8px;">Răng Sứ Thẩm Mỹ</h3>
            <p style="color: #64748B; font-size: 14px; margin-bottom: 16px;">Bọc răng sứ chính hãng nhập khẩu Đức, Mỹ, Thụy Sĩ tự nhiên không đen viền nướu.</p>
            <div style="margin-bottom: 20px;">
                <span style="font-size: 13px; color: #94A3B8;">Chỉ từ</span>
                <div class="uupm-price-tag" style="font-size: 28px; color: #0EA5E9;">1.500.000đ <span style="font-size: 14px; font-weight: normal; color: #64748B;">/ Răng</span></div>
                <span style="font-size: 13px; color: #10B981; font-weight: 600;">Bảo hành chính hãng 10-15 năm</span>
            </div>
            <button type="button" class="uupm-btn uupm-btn-primary" style="margin-top: auto;">Tư Vấn Chọn Dáng Răng</button>
        </div>
    </div>

    <!-- Detailed Pricing Tables by Category -->
    <div style="margin-bottom: 40px;">
        <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 16px; color: #0F172A; display: flex; align-items: center; gap: 10px;">
            <span style="display: inline-block; width: 6px; height: 24px; background: #0EA5E9; border-radius: 4px;"></span>
            1. Bảng Giá Niềng Răng - Chỉnh Nha Thẩm Mỹ
        </h2>
        <div style="overflow-x: auto;">
            <table class="uupm-pricing-table">
                <thead>
                    <tr>
                        <th style="width: 40%;">Phương Pháp / Dịch Vụ</th>
                        <th style="width: 20%;">Đơn Vị</th>
                        <th style="width: 25%;">Chi Phí Trọn Gói</th>
                        <th style="width: 15%; text-align: center;">Hành Động</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Niềng răng mắc cài kim loại tiêu chuẩn</strong><br><small style="color: #64748B;">Hiệu quả cao, bền bỉ, tiết kiệm chi phí</small></td>
                        <td>2 hàm</td>
                        <td><span class="uupm-price-tag">20.000.000đ - 28.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Niềng răng mắc cài tự buộc / tự đóng</strong><br><small style="color: #64748B;">Rút ngắn 3-6 tháng điều trị, giảm đau ma sát</small></td>
                        <td>2 hàm</td>
                        <td><span class="uupm-price-tag">30.000.000đ - 38.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Niềng răng mắc cài sứ thẩm mỹ</strong><br><small style="color: #64748B;">Màu sứ tiệp màu răng, thẩm mỹ khi giao tiếp</small></td>
                        <td>2 hàm</td>
                        <td><span class="uupm-price-tag">35.000.000đ - 45.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Niềng răng khay trong suốt Invisalign (Mỹ)</strong><br><small style="color: #64748B;">Gần như vô hình, tháo lắp linh hoạt ăn uống</small></td>
                        <td>Trọn gói</td>
                        <td><span class="uupm-price-tag">55.000.000đ - 95.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Category 2: Implant -->
    <div style="margin-bottom: 40px;">
        <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 16px; color: #0F172A; display: flex; align-items: center; gap: 10px;">
            <span style="display: inline-block; width: 6px; height: 24px; background: #0EA5E9; border-radius: 4px;"></span>
            2. Bảng Giá Trồng Răng Implant (Bảo Hành Chính Hãng)
        </h2>
        <div style="overflow-x: auto;">
            <table class="uupm-pricing-table">
                <thead>
                    <tr>
                        <th style="width: 40%;">Loại Trụ Implant</th>
                        <th style="width: 20%;">Xuất Xứ</th>
                        <th style="width: 25%;">Chi Phí / Trụ</th>
                        <th style="width: 15%; text-align: center;">Hành Động</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Implant Dentium Hàn Quốc</strong><br><small style="color: #64748B;">Tích hợp xương nhanh, chi phí tối ưu nhất</small></td>
                        <td>Hàn Quốc</td>
                        <td><span class="uupm-price-tag">12.500.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Implant Osstem Hàn Quốc</strong><br><small style="color: #64748B;">Top 1 thương hiệu Implant tại châu Á</small></td>
                        <td>Hàn Quốc</td>
                        <td><span class="uupm-price-tag">14.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Implant ETK / Tekka Pháp</strong><br><small style="color: #64748B;">Xử lý bề mặt SA, rút ngắn thời gian lành thương</small></td>
                        <td>Pháp</td>
                        <td><span class="uupm-price-tag">20.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Implant Straumann SLA (Thụy Sĩ)</strong><br><small style="color: #64748B;">Chuẩn cao cấp thế giới, bảo hành trọn đời</small></td>
                        <td>Thụy Sĩ</td>
                        <td><span class="uupm-price-tag">30.000.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Category 3: General and surgery -->
    <div style="margin-bottom: 48px;">
        <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 16px; color: #0F172A; display: flex; align-items: center; gap: 10px;">
            <span style="display: inline-block; width: 6px; height: 24px; background: #0EA5E9; border-radius: 4px;"></span>
            3. Nha Khoa Tổng Quát, Nhổ Răng Khôn & Tẩy Trắng
        </h2>
        <div style="overflow-x: auto;">
            <table class="uupm-pricing-table">
                <thead>
                    <tr>
                        <th style="width: 40%;">Dịch Vụ Điều Trị</th>
                        <th style="width: 20%;">Đơn Vị</th>
                        <th style="width: 25%;">Chi Phí Niêm Yết</th>
                        <th style="width: 15%; text-align: center;">Hành Động</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Lấy cao răng siêu âm & Đánh bóng</strong></td>
                        <td>2 hàm</td>
                        <td><span class="uupm-price-tag">150.000đ - 250.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Nhổ răng khôn Piezotome không đau</strong></td>
                        <td>1 răng</td>
                        <td><span class="uupm-price-tag">800.000đ - 2.500.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Tẩy trắng răng Laser Whitening tại phòng</strong></td>
                        <td>Liệu trình</td>
                        <td><span class="uupm-price-tag">1.800.000đ - 2.500.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Trám răng Composite thẩm mỹ</strong></td>
                        <td>1 răng</td>
                        <td><span class="uupm-price-tag">200.000đ - 450.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                    <tr>
                        <td><strong>Điều trị tủy răng công nghệ vi phẫu</strong></td>
                        <td>1 răng</td>
                        <td><span class="uupm-price-tag">500.000đ - 1.500.000đ</span></td>
                        <td style="text-align: center;"><button type="button" class="uupm-btn uupm-btn-primary" style="padding: 6px 14px; font-size: 13px; min-height: 36px;">Đặt hẹn</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Contact & Booking CTA Banner -->
    <div style="background: linear-gradient(135deg, #0EA5E9 0%, #0369A1 100%); border-radius: 20px; padding: 36px; text-align: center; color: #FFFFFF; box-shadow: var(--uupm-shadow-lg);">
        <h3 style="font-size: 26px; color: #FFFFFF !important; margin-bottom: 10px;">Bạn Chưa Biết Răng Của Mình Phù Hợp Với Dịch Vụ Nào?</h3>
        <p style="color: rgba(255, 255, 255, 0.9) !important; max-width: 600px; margin: 0 auto 24px auto; font-size: 15px;">
            Đến ngay Nha Khoa Kim Dung để được thăm khám tổng quát, chụp phim CT ConeBeam 3D và tư vấn hoàn toàn MIỄN PHÍ.
        </p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <button type="button" class="uupm-btn uupm-btn-accent" style="font-size: 16px; padding: 14px 28px;">
                📅 Đặt Lịch Khám Miễn Phí Ngay
            </button>
            <a href="tel:0862960886" class="uupm-btn" style="background: #FFFFFF; color: #0284C7 !important; font-size: 16px; padding: 14px 28px;">
                📞 Gọi Bác Sĩ: 0862 960 886
            </a>
        </div>
    </div>
</div>
"""

# Process bang-gia.html
bang_gia_path = os.path.join(WEBSITE_DIR, "bang-gia.html")
if os.path.exists(bang_gia_path):
    with open(bang_gia_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Fix Title
    html = re.sub(r"<title>Array to string conversion</title>", "<title>Bảng Giá Dịch Vụ Nha Khoa Kim Dung 2026 - Chi Phí Trọn Gói, Minh Bạch</title>", html, flags=re.IGNORECASE)
    
    # Replace broken <main id="main-content">...</main>
    main_pattern = r"(<main id=\"main-content\">)(.*?)(</main>)"
    if re.search(main_pattern, html, flags=re.DOTALL):
        html = re.sub(main_pattern, rf"\1\n{PRICING_HTML}\n\3", html, flags=re.DOTALL)
        print("Replaced main-content in bang-gia.html with clean pricing table!")

    with open(bang_gia_path, "w", encoding="utf-8") as f:
        f.write(html)

# Now iterate over all html files in website and inject CSS and JS
all_html_files = glob.glob(os.path.join(WEBSITE_DIR, "*.html"))
css_tag = '<link href="assets/css/ui-ux-pro-max.css" rel="stylesheet">\n'
js_tag = '<script src="assets/js/ui-ux-pro-max.js" defer></script>\n'

updated_count = 0
for file_path in all_html_files:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    changed = False

    # Inject CSS before </head> if not present
    if "ui-ux-pro-max.css" not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"{css_tag}</head>", 1)
            changed = True

    # Inject JS before </body> if not present
    if "ui-ux-pro-max.js" not in content:
        if "</body>" in content:
            content = content.replace("</body>", f"{js_tag}</body>", 1)
            changed = True

    # Fix any remaining "Array to string conversion" in title
    if "Array to string conversion" in content:
        content = content.replace("<title>Array to string conversion</title>", "<title>Nha Khoa Kim Dung – Nha Khoa Uy Tín Hàng Đầu Thái Nguyên</title>")
        changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Successfully updated {updated_count} / {len(all_html_files)} HTML files with UI/UX Pro Max!")
