# Nha Khoa Kim Dung - Website

Dự án clone và tái tạo website tĩnh Nha Khoa Kim Dung đầy đủ các trang dịch vụ, bảng giá, giới thiệu, đội ngũ và tin tức.

## Cấu trúc thư mục
- `website/`: Chứa toàn bộ 70 trang HTML hoàn chỉnh của website (trang chủ `index.html`, `bang-gia.html`, `dich-vu.html`, v.v.).
- `build_site.py`: Script Python tự động chuyển đổi dữ liệu cào từ Firecrawl thành website HTML.
- `start_server.bat`: File khởi động nhanh web server local trên Windows.

## Cách chạy trên máy tính
1. **Cách 1**: Nhấp đúp vào file `start_server.bat` trên Windows.
2. **Cách 2**: Chạy qua dòng lệnh:
   ```bash
   cd website
   python -m http.server 8000
   ```
   Sau đó truy cập: `http://localhost:8000`
