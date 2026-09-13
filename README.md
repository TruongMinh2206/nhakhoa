# Nha Khoa Kim Dung - Website (Nâng cấp UI/UX Pro Max)

Dự án website Nha Khoa Kim Dung đầy đủ các trang dịch vụ, bảng giá, giới thiệu, đội ngũ và tin tức, đã được nâng cấp toàn diện bằng hệ thống trí tuệ thiết kế **[UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**.

## Điểm nâng cấp UI/UX Pro Max
- **Phong cách**: **Soft UI Evolution** dành riêng cho phòng khám nha khoa (Dental Practice) với chiều sâu tinh tế, bóng đổ đa tầng mềm mại và góc bo chuẩn y tế `rounded-2xl`.
- **Hệ màu nhận diện thương hiệu Kim Dung**: 
  - Primary / Main: `#EABF0E` (Vàng hoàng kim sang trọng)
  - Dark: `#B89307`
  - Hover: `#D4AC0B`
  - Accent / Glow: `#FDE047`
- **Kiểu chữ**: `Plus Jakarta Sans` cho tiêu đề và `Noto Sans` cho nội dung (hỗ trợ tiếng Việt 100% không lỗi font).
- **Thanh liên hệ nổi thông minh (Floating Quick Action Dock)**:
  - 📞 Hotline 24/7 (`0862960886`)
  - 💬 Chat Zalo trực tiếp
  - 📅 Đặt lịch khám nhanh
  - ⬆️ Nút cuộn về đầu trang mượt mà
- **Modal Popup Đặt Lịch Khám Thông Minh**: Mở nhanh khi nhấn "Đặt lịch" / "Tư vấn" trên bất kỳ trang nào, có kiểm tra dữ liệu và thông báo Toast xác nhận tức thì.
- **Sửa lỗi Bảng giá (`bang-gia.html`)**: Khắc phục lỗi crash PHP gốc, tái tạo bảng giá dịch vụ chuẩn y tế (Implant, Niềng răng, Răng sứ, Nhổ răng khôn...).

## Cấu trúc thư mục
- `website/`: Chứa toàn bộ 67 trang HTML hoàn chỉnh của website (`index.html`, `bang-gia.html`, `dich-vu.html`, v.v.).
  - `assets/css/ui-ux-pro-max.css`: Design system CSS Soft UI Evolution.
  - `assets/js/ui-ux-pro-max.js`: Controller cho modal đặt lịch, thanh nổi, sticky header và toast.
- `.agents/skills/ui-ux-pro-max/`: Bộ công cụ và cơ sở dữ liệu trí tuệ thiết kế (192 màu, 79 style, 74 typography, 119 UX rules).
- `design-system/nha-khoa-kim-dung/MASTER.md`: File quy chuẩn thiết kế đã được trích xuất cho dự án.
- `build_site.py`: Script Python tự động chuyển đổi dữ liệu crawl thành website HTML (đã nhúng UI-UX Pro Max).
- `start_server.bat`: File khởi động nhanh web server local trên Windows.

## Cách chạy trên máy tính
1. **Cách 1**: Nhấp đúp vào file `start_server.bat` trên Windows.
2. **Cách 2**: Chạy qua dòng lệnh:
   ```bash
   cd website
   python -m http.server 8000
   ```
   Sau đó truy cập: `http://localhost:8000`

## Tra cứu công cụ thiết kế UI-UX Pro Max
```bash
python .agents/skills/ui-ux-pro-max/scripts/search.py "dental clinic" --design-system
python .agents/skills/ui-ux-pro-max/scripts/search.py "healthcare" --domain color
python .agents/skills/ui-ux-pro-max/scripts/search.py "form" --domain ux
```

