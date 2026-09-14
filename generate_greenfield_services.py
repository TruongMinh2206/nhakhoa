# -*- coding: utf-8 -*-
"""
Generate Greenfield Dental Exact HTML DOM Structure for all 6 Service Pages
With Kim Dung Brand Colors (#EABF0E, luxury dark surfaces) and Typography (Be Vietnam Pro)
"""

import os
import re

WEBSITE_DIR = os.path.join(os.path.dirname(__file__), 'website')

# 9 Real Patient Smiles for Section 6 (3x3 grid)
SMILE_GALLERY_9 = [
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-1.jpg', 'Phục hồi nụ cười tự tin rạng ngời'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-2.jpg', 'Khớp cắn chuẩn, nụ cười tỏa sáng'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-3.jpg', 'Hàm răng đều đặn trắng sáng tự nhiên'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-4.jpg', 'Ăn nhai chắc khỏe trọn đời'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-5.jpg', 'Tự tin giao tiếp và thành công hơn'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-6.jpg', 'Thay đổi diện mạo, nâng tầm nhan sắc'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-7.jpg', 'Nụ cười rạng rỡ chuẩn tỉ lệ vàng'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-8.jpg', 'Khẳng định phong thái bản lĩnh'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-9.jpg', 'Tự tin tỏa sáng từng khoảnh khắc')
]

# Section 8 Trust Commitments (3 cards)
TRUST_COMMITMENTS = [
    {
        'title': 'Bảo hành dài hạn',
        'desc': 'Bảo hành từ 10 đến 15 năm hoặc trọn đời tùy dịch vụ. Cung cấp thẻ bảo hành điện tử chính hãng và kiểm tra định kỳ miễn phí.'
    },
    {
        'title': 'Chứng nhận quốc tế',
        'desc': 'Đội ngũ bác sĩ tu nghiệp chuyên sâu tại Thụy Sĩ, Hoa Kỳ, Hàn Quốc. Phòng khám đạt chuẩn vô trùng khép kín nghiêm ngặt.'
    },
    {
        'title': 'Vật liệu chính hãng',
        'desc': 'Nobel Biocare, Straumann, Hiossen, Cercon HT, IPS e.max — các thương hiệu nha khoa hàng đầu thế giới có tem CO/CQ.'
    }
]

# Section 9 Doctor Profiles
SERVICE_DOCTORS = {
    'trong-rang-implant.html': {
        'name': 'BS. CKI Thùy Chi',
        'role': 'Trưởng khoa Cấy ghép Implant & Phục hình',
        'desc': 'BS. CKI Thùy Chi là chuyên gia implant tại Nha Khoa Kim Dung với hơn 12 năm kinh nghiệm và hơn 3.000 ca implant thành công. Chuyên sâu về implant All-on-4, All-on-6, cấy ghép định vị 3D và phục hồi toàn hàm phức tạp.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-1755314936.png.webp',
        'tags': ['Đại học Y Hà Nội', '3.000+ Ca Implant thành công', 'Chứng chỉ ITI Thụy Sĩ', 'Chuyên gia All-on-4 & Phục hình']
    },
    'boc-rang-su.html': {
        'name': 'Bác sĩ Cố Vấn Kim Dung',
        'role': 'Cố vấn Chuyên môn & Thẩm mỹ Nụ cười',
        'desc': 'Hơn 20 năm cống hiến trong ngành Răng Hàm Mặt, chuyên gia phục hình thẩm mỹ sứ cao cấp và kiến tạo nụ cười chuẩn nhân tướng học. Từng thực hiện hơn 5.000 ca dán sứ Veneer và bọc răng toàn sứ tinh xảo.',
        'img': 'https://nhakhoakimdung.vn/thumbs/400x440x1/upload/news/thiet-ke-chua-co-ten-1755314936.png.webp',
        'tags': ['20+ Năm kinh nghiệm', '5.000+ Ca Răng sứ hoàn mỹ', 'Chuyên gia DSD Smile Design', 'Bảo tồn tối đa mô răng']
    },
    'nieng-rang-tham-my.html': {
        'name': 'BS. Thanh Thủy',
        'role': 'Chuyên gia Chỉnh nha Invisalign Platinum Hoa Kỳ',
        'desc': 'Bác sĩ đạt thứ hạng Platinum của Align Technology Hoa Kỳ, tu nghiệp chuyên sâu chỉnh nha kỹ thuật số tại Hoa Kỳ. Thực hiện thành công hơn 1.500 ca niềng răng trong suốt và khớp cắn phức tạp.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-2-1755315466.png.webp',
        'tags': ['Invisalign Platinum Provider', '1.500+ Ca Niềng răng', 'Bác sĩ ĐH Y Hà Nội', 'Chứng chỉ Chỉnh nha Hoa Kỳ']
    },
    'nieng-rang-mac-cai.html': {
        'name': 'BS. Thanh Thủy',
        'role': 'Trưởng khoa Chỉnh nha Kỹ thuật số',
        'desc': 'Bác sĩ chuyên khoa chỉnh nha hàng đầu với hơn 10 năm kinh nghiệm điều trị các ca sai lệch khớp cắn từ nhẹ đến phức tạp. Ứng dụng phần mềm phân tích xương hàm 3D giúp rút ngắn thời gian niềng 4-6 tháng.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-2-1755315466.png.webp',
        'tags': ['10+ Năm kinh nghiệm Chỉnh nha', '2.000+ Ca Mắc cài thành công', 'Chuyên gia Khớp cắn 3D', 'Tận tâm, theo sát từng tháng']
    },
    'tay-trang-rang.html': {
        'name': 'BS. CKI Thùy Chi',
        'role': 'Chuyên khoa Nha khoa Thẩm mỹ Nụ cười',
        'desc': 'Bác sĩ giàu kinh nghiệm trong lĩnh vực thẩm mỹ bảo tồn và tẩy trắng răng công nghệ cao. Luôn chú trọng kiểm soát nồng độ an toàn tuyệt đối cho men nướu, mang lại nụ cười trắng sáng rạng rỡ mà không ê buốt.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-1755314936.png.webp',
        'tags': ['Chuyên khoa I Răng Hàm Mặt', 'Chứng chỉ Laser Whitening USA', 'Không đau, an toàn men nướu', '1.000+ Khách hàng hài lòng']
    },
    'nha-khoa-tong-quat.html': {
        'name': 'Bác sĩ Điều trị Tổng quát & Vi phẫu',
        'role': 'Chuyên khoa Nha khoa Vi phẫu & Tiểu phẫu',
        'desc': 'Bác sĩ tận tâm, thao tác nhẹ nhàng, giàu kinh nghiệm trong nhổ răng khôn không đau bằng máy Piezotome, điều trị tủy vi phẫu dưới kính lúp phóng đại và phục hồi chức năng răng tự nhiên.',
        'img': 'https://nhakhoakimdung.vn/thumbs/400x440x1/upload/news/thiet-ke-chua-co-ten-2-1755315466.png.webp',
        'tags': ['Chuyên khoa Vi phẫu Nha khoa', 'Chuyên gia Nhổ răng Piezotome', 'Vô trùng chuẩn Class B', 'Ân cần, thấu hiểu bệnh nhân']
    }
}

# Section 3 Video stories
VIDEOS = {
    'trong-rang-implant.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Hành Trình Khôi Phục Nụ Cười Cùng Implant',
        'desc': 'Lắng nghe chia sẻ thực tế của khách hàng sau khi khôi phục khả năng ăn nhai vững chắc cùng công nghệ Implant kỹ thuật số.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    },
    'boc-rang-su.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Hành Trình Lột Xác Nụ Cười Răng Toàn Sứ',
        'desc': 'Khám phá sự thay đổi ngoạn mục về diện mạo và sự tự tin sau khi hoàn thiện nụ cười sứ thẩm mỹ tinh xảo.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    },
    'nieng-rang-tham-my.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Hành Trình Niềng Răng Vô Hình Invisalign',
        'desc': 'Trải nghiệm niềng răng trong suốt nhẹ nhàng, không ai nhận ra đang niềng và kết quả khớp cắn chuẩn xác.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    },
    'nieng-rang-mac-cai.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Thay Đổi Diện Mạo Sau Niềng Răng Mắc Cài',
        'desc': 'Theo dõi sự dịch chuyển răng chuẩn xác từng milimet và góc nghiêng thần thánh sau khi tháo niềng.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    },
    'tay-trang-rang.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Tẩy Trắng Răng Laser Whitening Chỉ Sau 45 Phút',
        'desc': 'Xem cận cảnh quá trình bật 3-5 tông màu men răng trắng sáng tự nhiên, hoàn toàn êm ái không buốt.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    },
    'nha-khoa-tong-quat.html': {
        'tagline': 'Câu chuyện nụ cười',
        'title': 'Chăm Sóc Răng Miệng Chuẩn Quốc Tế Tại Kim Dung',
        'desc': 'Trải nghiệm điều trị nha khoa êm ái, nhẹ nhàng và an tâm với quy trình vô trùng khép kín hàng đầu.',
        'url': 'https://www.youtube.com/embed/hXCCpyIlDDU?start=29'
    }
}

# Section 7 Case Images
CASE_IMAGES = {
    'trong-rang-implant.html': ('https://www.nhakhoagreenfield.com/images/implant-before-after.jpg', 'Phục Hồi Cấy Ghép Implant Nha Khoa Toàn Diện — Nha Khoa Kim Dung'),
    'boc-rang-su.html': ('https://www.nhakhoagreenfield.com/images/services/service-cosmetics.webp', 'Phục Hình Thẩm Mỹ Răng Toàn Sứ Chuẩn Tỷ Lệ Vàng — Nha Khoa Kim Dung'),
    'nieng-rang-tham-my.html': ('https://www.nhakhoagreenfield.com/images/services/service-ortho.webp', 'Chỉnh Nha Máng Trong Suốt Invisalign Hoa Kỳ — Nha Khoa Kim Dung'),
    'nieng-rang-mac-cai.html': ('https://www.nhakhoagreenfield.com/images/services/service-ortho.webp', 'Niềng Răng Mắc Cài Cân Chỉnh Khớp Cắn Chuẩn — Nha Khoa Kim Dung'),
    'tay-trang-rang.html': ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-1.jpg', 'Kết Quả Tẩy Trắng Răng Laser Whitening — Nha Khoa Kim Dung'),
    'nha-khoa-tong-quat.html': ('https://www.nhakhoagreenfield.com/images/hero-clinic.jpg', 'Chăm Sóc Điều Trị Răng Miệng Toàn Diện — Nha Khoa Kim Dung')
}


def build_greenfield_main(filename, data):
    hero = data['hero']
    benefits = data['benefits']
    pricing = data['pricing']
    workflow = data['workflow']
    criteria = data['criteria']
    faqs = data['faq']
    video = VIDEOS.get(filename, VIDEOS['trong-rang-implant.html'])
    doctor = SERVICE_DOCTORS.get(filename, SERVICE_DOCTORS['trong-rang-implant.html'])
    case_img, case_caption = CASE_IMAGES.get(filename, CASE_IMAGES['trong-rang-implant.html'])

    # Section 1: Hero Trust spans (Greenfield exact pattern)
    hero_trust_html = "".join([
        f'<span>✓ <!-- -->{t}</span>'
        for t in hero['trust']
    ])

    # Section 2: 6 Benefits HTML
    benefits_html = ""
    for b in benefits['items']:
        benefits_html += f"""
      <div class="rounded-2xl p-6 flex flex-col gap-3" style="background-color:#2e2c2d;border:1px solid #3a3738">
        <div class="flex items-center gap-3">
          <div style="color:#EABF0E">
            <i class="{b['icon']}" style="font-size: 1.25rem;"></i>
          </div>
          <h3 class="font-bold text-white text-base">{b['title']}</h3>
        </div>
        <p class="text-sm text-gray-400 leading-relaxed">{b['desc']}</p>
      </div>"""

    # Section 4: 3 Pricing Tiers HTML
    pricing_html = ""
    for p in pricing['tiers']:
        features_li = "".join([
            f'<li class="flex items-start gap-2.5 text-sm text-gray-300"><svg width="18" height="18" style="width:18px;height:18px;flex-shrink:0;color:#EABF0E;margin-top:2px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"></path></svg><span>{f}</span></li>'
            for f in p['features']
        ])
        if p['popular']:
            pricing_html += f"""
      <div class="relative flex flex-col">
        <div class="flex justify-center h-8 mb-2 z-10">
          <span class="px-5 py-1.5 rounded-full text-[#18181b] text-xs font-bold tracking-widest uppercase self-center shadow-md" style="background-color:#EABF0E">★ Phổ biến nhất</span>
        </div>
        <div class="rounded-2xl flex flex-col p-7 flex-1 border-2 shadow-2xl" style="background-color:#2e2c2d;border-color:#EABF0E">
          <h3 class="text-xl font-bold text-white">{p['name']}</h3>
          <p class="text-sm mt-1 mb-5" style="color:#EABF0E">{p['sub']}</p>
          <p class="text-3xl font-extrabold text-white mb-6">{p['price']}</p>
          <ul class="space-y-3 mb-8 flex-1">
            {features_li}
          </ul>
          <a class="block w-full py-3.5 text-center font-semibold text-sm rounded-xl transition-opacity hover:opacity-90 text-[#18181b] shadow-md" style="background-color:#EABF0E;color:#18181b !important;text-decoration:none;" href="dat-lich.html">Đặt Lịch Thăm Khám Miễn Phí</a>
        </div>
      </div>"""
        else:
            pricing_html += f"""
      <div class="relative flex flex-col">
        <div class="flex justify-center h-8 mb-2 z-10"></div>
        <div class="rounded-2xl flex flex-col p-7 flex-1" style="background-color:#2e2c2d;border:1px solid #3a3738">
          <h3 class="text-xl font-bold text-white">{p['name']}</h3>
          <p class="text-sm mt-1 mb-5" style="color:#EABF0E">{p['sub']}</p>
          <p class="text-3xl font-extrabold text-white mb-6">{p['price']}</p>
          <ul class="space-y-3 mb-8 flex-1">
            {features_li}
          </ul>
          <a class="block w-full py-3.5 text-center font-semibold text-sm rounded-xl transition-opacity hover:opacity-90" style="background-color:transparent;color:#ffffff !important;border:1.5px solid #EABF0E;text-decoration:none;" href="dat-lich.html">Đặt Lịch Thăm Khám Miễn Phí</a>
        </div>
      </div>"""

    # Section 5: Timeline (Desktop & Mobile)
    steps = workflow['steps']
    s1, s2, s3, s4 = steps[0], steps[1], steps[2], steps[3]
    
    # Desktop grid timeline
    desktop_timeline = f"""
    <div class="hidden md:grid" style="grid-template-columns:1fr 72px 1fr">
      <!-- Step 01: Left card, Center 01, Right empty -->
      <div class="flex items-center justify-end py-8 pr-8">
        <div class="max-w-[280px] w-full rounded-2xl p-6" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12)">
          <div class="w-9 h-9 mb-4 flex items-center justify-center rounded-lg" style="background-color:rgba(234,191,14,0.15);color:#EABF0E"><i class="fa-solid fa-notes-medical text-lg"></i></div>
          <h3 class="font-bold text-white text-base mb-2">{s1['title']}</h3>
          <p class="text-sm leading-relaxed mb-3" style="color:rgba(255,255,255,0.60)">{s1['desc']}</p>
          <p class="text-xs font-medium" style="color:#EABF0E">{s1['tag']}</p>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <div class="flex-1 w-px" style="background-color:transparent"></div>
        <div class="w-14 h-14 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background-color:#EABF0E;color:#18181b;box-shadow:0 0 0 5px rgba(234,191,14,0.22)">01</div>
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
      </div>
      <div class="flex items-center justify-start py-8 pl-8"></div>

      <!-- Step 02: Left empty, Center 02, Right card -->
      <div class="flex items-center justify-end py-8 pr-8"></div>
      <div class="flex flex-col items-center">
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
        <div class="w-14 h-14 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background-color:#EABF0E;color:#18181b;box-shadow:0 0 0 5px rgba(234,191,14,0.22)">02</div>
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
      </div>
      <div class="flex items-center justify-start py-8 pl-8">
        <div class="max-w-[280px] w-full rounded-2xl p-6" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12)">
          <div class="w-9 h-9 mb-4 flex items-center justify-center rounded-lg" style="background-color:rgba(234,191,14,0.15);color:#EABF0E"><i class="fa-solid fa-tooth text-lg"></i></div>
          <h3 class="font-bold text-white text-base mb-2">{s2['title']}</h3>
          <p class="text-sm leading-relaxed mb-3" style="color:rgba(255,255,255,0.60)">{s2['desc']}</p>
          <p class="text-xs font-medium" style="color:#EABF0E">{s2['tag']}</p>
        </div>
      </div>

      <!-- Step 03: Left card, Center 03, Right empty -->
      <div class="flex items-center justify-end py-8 pr-8">
        <div class="max-w-[280px] w-full rounded-2xl p-6" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12)">
          <div class="w-9 h-9 mb-4 flex items-center justify-center rounded-lg" style="background-color:rgba(234,191,14,0.15);color:#EABF0E"><i class="fa-solid fa-shield-heart text-lg"></i></div>
          <h3 class="font-bold text-white text-base mb-2">{s3['title']}</h3>
          <p class="text-sm leading-relaxed mb-3" style="color:rgba(255,255,255,0.60)">{s3['desc']}</p>
          <p class="text-xs font-medium" style="color:#EABF0E">{s3['tag']}</p>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
        <div class="w-14 h-14 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background-color:#EABF0E;color:#18181b;box-shadow:0 0 0 5px rgba(234,191,14,0.22)">03</div>
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
      </div>
      <div class="flex items-center justify-start py-8 pl-8"></div>

      <!-- Step 04: Left empty, Center 04, Right card -->
      <div class="flex items-center justify-end py-8 pr-8"></div>
      <div class="flex flex-col items-center">
        <div class="flex-1 w-px" style="background-color:rgba(234,191,14,0.3)"></div>
        <div class="w-14 h-14 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background-color:#EABF0E;color:#18181b;box-shadow:0 0 0 5px rgba(234,191,14,0.22)">04</div>
        <div class="flex-1 w-px" style="background-color:transparent"></div>
      </div>
      <div class="flex items-center justify-start py-8 pl-8">
        <div class="max-w-[280px] w-full rounded-2xl p-6" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12)">
          <div class="w-9 h-9 mb-4 flex items-center justify-center rounded-lg" style="background-color:rgba(234,191,14,0.15);color:#EABF0E"><i class="fa-solid fa-crown text-lg"></i></div>
          <h3 class="font-bold text-white text-base mb-2">{s4['title']}</h3>
          <p class="text-sm leading-relaxed mb-3" style="color:rgba(255,255,255,0.60)">{s4['desc']}</p>
          <p class="text-xs font-medium" style="color:#EABF0E">{s4['tag']}</p>
        </div>
      </div>
    </div>"""

    # Mobile timeline
    mobile_timeline = "".join([
        f"""
      <div class="flex gap-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center flex-shrink-0 text-sm font-bold" style="background-color:rgba(234,191,14,0.2);color:#EABF0E">{st['num']}</div>
        <div class="rounded-2xl p-5 flex-1" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12)">
          <h3 class="font-bold text-white text-base mb-1.5">{st['title']}</h3>
          <p class="text-sm leading-relaxed mb-2" style="color:rgba(255,255,255,0.60)">{st['desc']}</p>
          <p class="text-xs font-medium" style="color:#EABF0E">{st['tag']}</p>
        </div>
      </div>"""
        for st in steps
    ])

    # Section 6: Smile Gallery 9 photos
    gallery_html = "".join([
        f"""
      <div class="rounded-2xl overflow-hidden aspect-[3/4] shadow-md">
        <img src="{g[0]}" alt="{g[1]}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy"/>
      </div>"""
        for g in SMILE_GALLERY_9
    ])

    # Section 7: Ai phù hợp (6 items + 1 case image)
    indications_list = []
    if 'left_items' in criteria:
        indications_list = criteria['left_items']
    elif 'items' in criteria:
        indications_list = criteria['items']
    
    while len(indications_list) < 6:
        indications_list.append(('Chăm sóc và bảo vệ sức khỏe răng', 'Dành cho mọi khách hàng mong muốn sở hữu hàm răng chắc khỏe, tự tin rạng rỡ.'))

    indications_html = "".join([
        f"""
        <div class="flex gap-4 rounded-xl p-5" style="background-color:rgba(255,255,255,0.05);border:1px solid rgba(234,191,14,0.18)">
          <div class="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5" style="background-color:rgba(234,191,14,0.15);color:#EABF0E">
            <svg width="20" height="20" style="width:20px;height:20px;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <div>
            <h3 class="font-semibold text-white text-sm mb-1">{item[0]}</h3>
            <p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.60)">{item[1]}</p>
          </div>
        </div>"""
        for item in indications_list[:6]
    ])

    # Section 8: Trust Commitments (3 cards)
    trust_html = "".join([
        f"""
      <div class="rounded-xl p-6 text-center" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1)">
        <div class="w-14 h-14 rounded-full flex items-center justify-center mx-auto mb-4" style="background-color:rgba(234,191,14,0.15)">
          <svg width="28" height="28" style="width:28px;height:28px;color:#EABF0E" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        <h3 class="font-semibold text-white mb-2">{t['title']}</h3>
        <p class="text-sm" style="color:rgba(255,255,255,0.60)">{t['desc']}</p>
      </div>"""
        for t in TRUST_COMMITMENTS
    ])

    # Section 9: Doctor Profile
    doctor_tags_html = "".join([
        f'<span class="text-xs font-medium px-3 py-1 rounded-full" style="background-color:rgba(234,191,14,0.15);color:#EABF0E">{tag}</span>'
        for tag in doctor['tags']
    ])

    # Section 10: FAQ Accordion items
    faq_html = "".join([
        f"""
      <div class="rounded-2xl overflow-hidden" style="background-color:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1)">
        <button type="button" class="w-full flex items-center justify-between gap-4 px-6 py-5 text-left faq-accordion-btn">
          <span class="font-semibold text-white text-sm leading-snug">{f['q']}</span>
          <span style="color:#EABF0E">
            <svg width="20" height="20" style="width:20px;height:20px;" class="flex-shrink-0 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </button>
        <div class="faq-accordion-content px-6 pb-5 text-sm text-gray-300 leading-relaxed" style="display:none;">
          {f['a']}
        </div>
      </div>"""
        for f in faqs
    ])

    # Combine into Exact 10 Sections HTML matching Greenfield Dental DOM structure
    main_html = f"""<main id="main-content" class="min-h-screen gf-theme-root" style="background-color:#18181b;">
  <!-- 1. HERO SECTION -->
  <section class="relative min-h-[90vh] flex items-center overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src="{hero['bg_img']}" alt="{hero['title']}" class="w-full h-full object-cover object-center"/>
      <div class="absolute inset-0" style="background:linear-gradient(to right, rgba(24,24,27,0.95) 0%, rgba(24,24,27,0.85) 35%, rgba(24,24,27,0.55) 65%, rgba(24,24,27,0.20) 100%)"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-[#18181b] via-transparent to-transparent"></div>
    </div>
    <div class="relative z-10 w-full max-w-7xl mx-auto px-6 lg:px-12 py-28">
      <div class="max-w-[640px]">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-5" style="color:#EABF0E">{hero['tagline']}</p>
        <h1 class="text-[2.6rem] lg:text-[3.5rem] text-white leading-[1.15] mb-6 font-bold" style="font-family:'Be Vietnam Pro', sans-serif">{hero['title']}</h1>
        <p class="text-[1.05rem] leading-relaxed mb-9" style="color:rgba(255,255,255,0.85)">{hero['desc']}</p>
        <div class="flex flex-wrap gap-3 mb-10">
          <a class="inline-flex items-center gap-2 px-6 py-3 rounded-md text-[#18181b] text-[0.95rem] font-semibold transition-opacity hover:opacity-90 shadow-lg" style="background-color:#EABF0E;color:#18181b !important;text-decoration:none;display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:6px;font-weight:600;" href="dat-lich.html">
            Đặt lịch tư vấn miễn phí
            <svg width="16" height="16" style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
          </a>
          <a href="tel:0862960886" class="inline-flex items-center gap-2 px-6 py-3 rounded-md text-white text-[0.95rem] font-medium border border-white/30 hover:bg-white/10 transition-colors" style="display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:6px;color:#ffffff !important;border:1px solid rgba(255,255,255,0.3);text-decoration:none;background:transparent;">
            <svg width="16" height="16" style="width:16px;height:16px;flex-shrink:0;color:#EABF0E;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
            0862 960 886
          </a>
        </div>
        <div class="flex flex-wrap gap-6 text-sm" style="color:rgba(255,255,255,0.70)">
          {hero_trust_html}
        </div>
      </div>
    </div>
  </section>

  <!-- 2. LỢI ÍCH ĐIỀU TRỊ -->
  <section id="loi-ich" class="py-16" style="background-color:#222021">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-14">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">{benefits['tagline']}</p>
        <h2 class="text-4xl font-bold mb-4 text-white" style="font-family:'Be Vietnam Pro', sans-serif">{benefits['title']}</h2>
        <p class="text-gray-300 text-base max-w-xl mx-auto leading-relaxed">{benefits['desc']}</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        {benefits_html}
      </div>
    </div>
  </section>

  <!-- 3. CÂU CHUYỆN NỤ CƯỜI / VIDEO -->
  <section id="cau-chuyen" class="py-16" style="background-color:#18181b">
    <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-10">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">{video['tagline']}</p>
        <h2 class="text-4xl font-bold mb-4 text-white" style="font-family:'Be Vietnam Pro', sans-serif">{video['title']}</h2>
        <p class="text-white/60 text-base max-w-lg mx-auto leading-relaxed">{video['desc']}</p>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-2xl" style="aspect-ratio:16/9;border:1px solid rgba(255,255,255,0.1)">
        <iframe class="w-full h-full" src="{video['url']}" title="{video['title']}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>
      </div>
    </div>
  </section>

  <!-- 4. BẢNG GIÁ MINH BẠCH -->
  <div data-section="options" id="bang-gia">
    <section class="py-16" style="background-color:#222021">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-14">
          <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">{pricing['tagline']}</p>
          <h2 class="text-4xl font-bold mb-4 text-white" style="font-family:'Be Vietnam Pro', sans-serif">{pricing['title']}</h2>
          <p class="text-gray-300 text-base max-w-xl mx-auto leading-relaxed">{pricing['desc']}</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto items-stretch">
          {pricing_html}
        </div>
        <p class="mt-10 text-center text-sm text-gray-500">* Chi phí chính xác và phác đồ chi tiết sẽ được bác sĩ chuyên khoa tư vấn trực tiếp sau khi chụp phim thăm khám miễn phí.</p>
      </div>
    </section>
  </div>

  <!-- 5. QUY TRÌNH ĐIỀU TRỊ -->
  <section id="quy-trinh" class="py-20 overflow-hidden" style="background-color:#18181b">
    <div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">{workflow['tagline']}</p>
        <h2 class="text-4xl font-bold mb-4 text-white" style="font-family:'Be Vietnam Pro', sans-serif">{workflow['title']}</h2>
        <p class="text-base max-w-xl mx-auto leading-relaxed" style="color:rgba(255,255,255,0.60)">{workflow['desc']}</p>
      </div>
      {desktop_timeline}
      <div class="flex flex-col gap-5 md:hidden">
        {mobile_timeline}
      </div>
      <div class="text-center mt-14">
        <a href="dat-lich.html" class="inline-flex items-center gap-2.5 px-8 py-4 rounded-xl font-semibold text-[#18181b] text-[0.95rem] transition-opacity hover:opacity-90 shadow-lg" style="background-color:#EABF0E;color:#18181b !important;text-decoration:none;display:inline-flex;align-items:center;gap:10px;">
          <i class="fa-solid fa-calendar-check"></i> Đặt Lịch Tư Vấn Quy Trình Chi Tiết
        </a>
      </div>
    </div>
  </section>

  <!-- 6. THƯ VIỆN NỤ CƯỜI -->
  <section id="thu-vien" class="py-16" style="background-color:#222021">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">Thư viện nụ cười</p>
        <h2 class="text-4xl font-bold text-white" style="font-family:'Be Vietnam Pro', sans-serif">Nụ cười thật, tự tin thật</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {gallery_html}
      </div>
    </div>
  </section>

  <!-- 7. TÔI CÓ PHÙ HỢP KHÔNG? -->
  <section id="phu-hop" class="py-16" style="background-color:#18181b">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">Tôi có phù hợp không?</p>
        <h2 class="text-4xl font-bold text-white mb-4" style="font-family:'Be Vietnam Pro', sans-serif">{criteria['title']}</h2>
        <p class="text-base max-w-2xl mx-auto leading-relaxed" style="color:rgba(255,255,255,0.60)">Đội ngũ bác sĩ chuyên khoa tại Kim Dung luôn thăm khám kỹ lưỡng và tư vấn phương án điều trị an toàn, tối ưu nhất.</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-12 items-start">
        <div class="flex flex-col gap-4">
          {indications_html}
        </div>
        <div class="flex flex-col gap-3">
          <div class="relative rounded-2xl overflow-hidden shadow-2xl aspect-square" style="border:1px solid rgba(255,255,255,0.1)">
            <img src="{case_img}" alt="{case_caption}" class="w-full h-full object-cover object-center" loading="lazy"/>
          </div>
          <p class="text-xs text-center" style="color:rgba(255,255,255,0.50)">{case_caption}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. CAM KẾT ĐÁNG TIN CẬY -->
  <section id="cam-ket" class="py-16" style="background-color:#18181b">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-10">
        <h2 class="text-3xl font-bold text-white" style="font-family:'Be Vietnam Pro', sans-serif">Cam kết đáng tin cậy</h2>
        <p class="mt-3 text-lg" style="color:rgba(255,255,255,0.60)">Không chỉ lời nói — chúng tôi cam kết bằng chất lượng điều trị và hợp đồng văn bản minh bạch</p>
      </div>
      <div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        {trust_html}
      </div>
    </div>
  </section>

  <!-- 9. BÁC SĨ CHUYÊN TRÁCH -->
  <section id="bac-si" class="py-16" style="background-color:#222021">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold text-white mb-8 text-center" style="font-family:'Be Vietnam Pro', sans-serif">Bác sĩ chuyên trách</h2>
        <div class="rounded-2xl p-6 lg:p-8" style="background-color:#2e2c2d;border:1px solid #3a3738">
          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 items-center">
            <div class="flex flex-col items-center text-center">
              <div class="w-36 h-36 rounded-full overflow-hidden mb-4 bg-gray-700 border-2" style="border-color:rgba(234,191,14,0.4)">
                <img src="{doctor['img']}" alt="{doctor['name']}" class="w-full h-full object-cover object-top" loading="lazy"/>
              </div>
              <h3 class="text-xl font-semibold text-white">{doctor['name']}</h3>
              <p class="text-sm font-medium mt-1" style="color:#EABF0E">{doctor['role']}</p>
            </div>
            <div class="lg:col-span-2">
              <p class="text-gray-300 mb-5 leading-relaxed">{doctor['desc']}</p>
              <div class="flex flex-wrap gap-2 mb-6">
                {doctor_tags_html}
              </div>
              <a class="inline-flex items-center gap-2 px-6 py-3 text-[#18181b] font-semibold text-sm rounded-lg transition-opacity hover:opacity-90 shadow-md" style="background-color:#EABF0E;color:#18181b !important;text-decoration:none;" href="dat-lich.html">
                <i class="fa-solid fa-calendar-check"></i> Đặt Lịch Tư Vấn Trực Tiếp
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 10. CÂU HỎI THƯỜNG GẶP (FAQ) -->
  <section id="faq" class="py-16" style="background-color:#18181b">
    <div class="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase mb-3" style="color:#EABF0E">Câu hỏi thường gặp</p>
        <h2 class="text-4xl font-bold text-white" style="font-family:'Be Vietnam Pro', sans-serif">Giải Đáp Thắc Mắc</h2>
      </div>
      <div class="space-y-3 mb-12">
        {faq_html}
      </div>
      <div class="flex flex-wrap justify-center gap-4">
        <a class="inline-flex items-center gap-2 px-7 py-3.5 rounded-lg text-[#18181b] font-semibold text-sm transition-opacity hover:opacity-90 shadow-md" style="background-color:#EABF0E;color:#18181b !important;text-decoration:none;" href="dat-lich.html">
          Hỏi Kim Dung Ngay
          <svg width="16" height="16" style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
        </a>
        <a href="tel:0862960886" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-lg font-semibold text-sm transition-opacity hover:opacity-90" style="border:1.5px solid #EABF0E;color:#EABF0E !important;text-decoration:none;background:transparent;">
          <svg width="16" height="16" style="width:16px;height:16px;flex-shrink:0;color:#EABF0E;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
          Gọi Ngay 0862 960 886
        </a>
      </div>
    </div>
  </section>
</main>"""
    return main_html
