# -*- coding: utf-8 -*-
"""
Build 6 Greenfield-style Luxury Service Detail Pages for Nha Khoa Kim Dung
Standardized against Greenfield Dental (nhakhoagreenfield.com/vi):
1. trong-rang-implant.html (Implant)
2. boc-rang-su.html (Răng sứ)
3. nieng-rang-tham-my.html (Invisalign)
4. nieng-rang-mac-cai.html (Niềng răng mắc cài)
5. tay-trang-rang.html (Tẩy trắng)
6. nha-khoa-tong-quat.html (Nha khoa tổng quát)
"""

import os
import re

WEBSITE_DIR = os.path.join(os.path.dirname(__file__), 'website')

SERVICES = {
    'trong-rang-implant.html': {
        'title': 'Trồng Răng Implant Kỹ Thuật Số – Nha Khoa Kim Dung',
        'meta_desc': 'Cấy ghép răng Implant kỹ thuật số chuẩn Thụy Sĩ, Mỹ, Hàn Quốc tại Nha Khoa Kim Dung Thái Nguyên. Không đau, tích hợp xương 99.8%, bảo hành trọn đời.',
        'hero': {
            'tagline': 'CÔNG NGHỆ CẤY GHÉP IMPLANT ĐẲNG CẤP QUỐC TẾ',
            'title': 'Khôi Phục Răng Đã Mất — Ăn Nhai Chắc Khỏe Tự Nhiên Như Thật',
            'desc': 'Ứng dụng định vị phẫu thuật 3D Cone Beam, hệ thống trụ Implant chính hãng Thụy Sĩ, Mỹ & Hàn Quốc. Tích hợp xương nhanh chóng, không đau, bảo hành trọn đời.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/hero-clinic.jpg',
            'trust': [
                'Trụ chính hãng từ 14.500.000đ',
                'Trả góp 0% lãi suất linh hoạt',
                'Tỷ lệ tích hợp thành công 99.8%'
            ]
        },
        'benefits': {
            'tagline': 'TẠI SAO CHỌN IMPLANT?',
            'title': 'Lợi Ích Vượt Trội Của Cấy Ghép Implant',
            'desc': 'Implant là tiêu chuẩn vàng khôi phục răng mất, thay thế cả chân và thân răng hoàn hảo nhất hiện nay.',
            'items': [
                {
                    'icon': 'fa-solid fa-tooth',
                    'title': 'Ăn nhai như răng thật',
                    'desc': 'Khôi phục 99% lực cắn tự nhiên, thoải mái thưởng thức mọi món ăn yêu thích mà không lo rơi rớt hay xê dịch.'
                },
                {
                    'icon': 'fa-solid fa-shield-halved',
                    'title': 'Bảo tồn xương hàm',
                    'desc': 'Trụ titanium kích thích tái tạo mô xương sinh học, ngăn ngừa hoàn toàn hiện tượng tiêu xương và hóp má lão hóa.'
                },
                {
                    'icon': 'fa-solid fa-circle-check',
                    'title': 'Không mài răng kế cận',
                    'desc': 'Khác với cầu răng sứ truyền thống, cấy implant hoàn toàn độc lập, không xâm lấn hay ảnh hưởng đến các răng khỏe bên cạnh.'
                },
                {
                    'icon': 'fa-solid fa-award',
                    'title': 'Tuổi thọ vĩnh viễn',
                    'desc': 'Với cấu tạo titanium tinh khiết tương thích sinh học cao, trụ implant tích hợp vững chắc và tồn tại trọn đời khi chăm sóc đúng cách.'
                },
                {
                    'icon': 'fa-solid fa-heart-pulse',
                    'title': 'Không đau, lành thương nhanh',
                    'desc': 'Phẫu thuật nhẹ nhàng với công nghệ định vị 3D và gây tê hiện đại, bệnh nhân hoàn toàn êm ái và có thể sinh hoạt bình thường.'
                },
                {
                    'icon': 'fa-solid fa-star',
                    'title': 'Thẩm mỹ tự nhiên tuyệt mỹ',
                    'desc': 'Mão sứ nguyên khối Cercon/Emax bên trên được thiết kế màu sắc, vân răng tự nhiên trùng khớp 100% với hàm răng thật.'
                }
            ]
        },
        'pricing': {
            'tagline': 'BẢNG GIÁ MINH BẠCH',
            'title': 'Chi Phí Cấy Ghép Implant Trọn Gói',
            'desc': 'Giá niêm yết công khai, cam kết không phát sinh. Hỗ trợ trả góp 0% lãi suất liên kết 25+ ngân hàng.',
            'tiers': [
                {
                    'name': 'Implant Dentium Hàn Quốc',
                    'sub': 'Dòng trụ phổ biến thế giới',
                    'price': '14.500.000đ',
                    'unit': '/ trụ hoàn thiện',
                    'popular': False,
                    'features': [
                        'Trụ Titanium Dentium chính hãng',
                        'Khớp nối Abutment tiêu chuẩn',
                        'Tặng mão răng sứ Titan cao cấp',
                        'Miễn phí chụp phim CT Cone Beam 3D',
                        'Bảo hành chính hãng 10 năm'
                    ]
                },
                {
                    'name': 'Implant Hiossen Hoa Kỳ',
                    'sub': 'Chuẩn FDA Hoa Kỳ - Khuyên dùng',
                    'price': '19.000.000đ',
                    'unit': '/ trụ hoàn thiện',
                    'popular': True,
                    'features': [
                        'Trụ Titanium Hiossen USA tinh khiết',
                        'Thiết kế xoắn tối ưu nén xương sinh học',
                        'Tặng kèm mão toàn sứ Cercon HT Đức',
                        'Miễn phí máng định vị phẫu thuật 3D',
                        'Rút ngắn thời gian lành thương 4-6 tuần',
                        'Bảo hành chính hãng 15 năm'
                    ]
                },
                {
                    'name': 'Implant Straumann Thụy Sĩ',
                    'sub': 'Đỉnh cao công nghệ thế giới',
                    'price': '31.500.000đ',
                    'unit': '/ trụ hoàn thiện',
                    'popular': False,
                    'features': [
                        'Công nghệ bề mặt SLActive ưa nước độc quyền',
                        'Tích hợp xương thần tốc chỉ sau 3-4 tuần',
                        'Áp dụng hoàn hảo cho ca xương mỏng, tiêu xương',
                        'Tặng mão toàn sứ Emax Thụy Sĩ cao cấp',
                        'Bảo hành chính hãng TRỌN ĐỜI toàn cầu'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'QUY TRÌNH ĐIỀU TRỊ',
            'title': 'Quy Trình Cấy Ghép Implant Chuẩn Y Khoa',
            'desc': 'Quy trình vô trùng khép kín 1 phòng phẫu thuật riêng biệt, tuân thủ nghiêm ngặt chỉ dẫn của Hiệp hội Implant Quốc tế (ITI).',
            'steps': [
                {
                    'num': '01',
                    'title': 'Thăm khám & Chụp CT 3D',
                    'desc': 'Chụp phim CT Cone Beam 3D khảo sát mật độ xương hàm, tầm soát xoang hàm và lập kế hoạch kỹ thuật số.',
                    'tag': '✦ Khảo sát chính xác'
                },
                {
                    'num': '02',
                    'title': 'Cấy ghép trụ Implant',
                    'desc': 'Tiến hành cấy trụ vào xương hàm bằng máng dẫn đường phẫu thuật 3D. Thời gian chỉ 15-20 phút/trụ, hoàn toàn không đau.',
                    'tag': '✦ Nhẹ nhàng, êm ái'
                },
                {
                    'num': '03',
                    'title': 'Tích hợp & Gắn răng tạm',
                    'desc': 'Trụ implant tích hợp bền chắc với tế bào xương. Bác sĩ gắn răng tạm để khách hàng sinh hoạt và ăn nhai tự tin.',
                    'tag': '✦ Thẩm mỹ tức thì'
                },
                {
                    'num': '04',
                    'title': 'Lắp mão sứ & Tái khám',
                    'desc': 'Lắp mão toàn sứ cao cấp được chế tác riêng bằng công nghệ CAD/CAM, kiểm tra khớp cắn chuẩn xác và dặn dò bảo dưỡng.',
                    'tag': '✦ Nụ cười hoàn mỹ'
                }
            ]
        },
        'criteria': {
            'tagline': 'CHỈ ĐỊNH PHÙ HỢP',
            'title': 'Ai Nên Lựa Chọn Cấy Ghép Implant?',
            'left_title': 'Trường hợp nên cấy ghép',
            'left_items': [
                ('Mất 1 hoặc nhiều răng xen kẽ', 'Cần khôi phục vị trí mất răng mà không muốn mài 2 răng thật bên cạnh để làm cầu răng.'),
                ('Mất toàn bộ răng một hàm hoặc hai hàm', 'Giải pháp phục hình toàn hàm All-on-4 hoặc All-on-6 giúp cố định trọn vẹn không cần tháo lắp.'),
                ('Răng bị hư tổn nặng, lung lay', 'Răng bị sâu vỡ lớn, viêm quanh cuống nặng không thể bảo tồn buộc phải nhổ bỏ.'),
                ('Khó chịu với hàm tháo lắp', 'Người đeo hàm giả tháo lắp bị lỏng lẻo, đau lợi, vướng víu và bất tiện khi ăn uống.')
            ],
            'right_title': 'Cam kết từ Nha Khoa Kim Dung',
            'right_items': [
                ('100% Trụ Implant chính hãng', 'Có tem truy xuất nguồn gốc CO/CQ, thẻ bảo hành điện tử chính hãng từ Thụy Sĩ, Mỹ, Hàn Quốc.'),
                ('Phòng phẫu thuật vô trùng tuyệt đối', 'Hệ thống đèn cực tím khử khuẩn không khí, dụng cụ đóng gói vô khuẩn riêng biệt từng ca.'),
                ('Đội ngũ bác sĩ chuyên khoa cấp I', 'Bác sĩ thực hiện có chứng chỉ cấy ghép Implant quốc tế với hàng nghìn ca phục hình thành công.'),
                ('Chính sách đồng hành trọn đời', 'Thăm khám, chụp phim kiểm tra và vệ sinh răng định kỳ hoàn toàn miễn phí sau phẫu thuật.')
            ]
        },
        'faq': [
            {
                'q': 'Cấy ghép Implant có đau không?',
                'a': 'Tại Nha Khoa Kim Dung, quy trình cấy ghép được thực hiện dưới sự hỗ trợ của công nghệ gây tê vi điểm tiên tiến và máng dẫn hướng 3D, giúp vết rạch siêu nhỏ. Đa số khách hàng chia sẻ chỉ cảm thấy hơi tức nhẹ và cấy ghép implant còn êm ái hơn việc nhổ một chiếc răng khôn.'
            },
            {
                'q': 'Sau khi cấy trụ bao lâu thì có thể ăn nhai bình thường?',
                'a': 'Ngay sau khi cấy trụ, bác sĩ sẽ gắn răng tạm để bạn có thể ăn các thức ăn mềm. Sau khoảng 4 - 12 tuần (tùy thuộc vào loại trụ và cơ địa từng người), trụ implant tích hợp hoàn toàn với xương hàm và lắp mão sứ cố định, bạn sẽ ăn nhai thoải mái mọi món ăn như răng thật.'
            },
            {
                'q': 'Trồng răng Implant có bền không? Tuổi thọ kéo dài bao lâu?',
                'a': 'Implant là phương pháp duy nhất khôi phục răng có tuổi thọ trọn đời. Nhờ đặc tính tương thích sinh học của Titanium, trụ implant sẽ hòa quyện thành một phần của xương hàm. Với việc vệ sinh răng miệng tốt và tái khám định kỳ, răng implant sẽ theo bạn suốt đời.'
            },
            {
                'q': 'Người cao tuổi hoặc có bệnh lý tiểu đường, huyết áp có cấy Implant được không?',
                'a': 'Hoàn toàn có thể. Trước khi thực hiện, bác sĩ sẽ xét nghiệm máu tổng quát và hội chẩn chuyên sâu. Miễn là các chỉ số huyết áp, đường huyết được kiểm soát ổn định, bác sĩ Kim Dung sẽ áp dụng phác đồ chuyên biệt an toàn tuyệt đối cho người lớn tuổi.'
            },
            {
                'q': 'Chi phí trọn gói trên đã bao gồm khớp nối và răng sứ chưa?',
                'a': 'Giá tại Nha Khoa Kim Dung là chi phí TRỌN GÓI cho 1 răng hoàn thiện, bao gồm: trụ Implant, khớp nối Abutment, mão răng sứ và chi phí chụp phim, xét nghiệm. Cam kết minh bạch không có bất kỳ phụ phí ẩn nào.'
            }
        ]
    },

    'boc-rang-su.html': {
        'title': 'Bọc Răng Sứ Thẩm Mỹ & Mặt Dán Sứ Veneer – Nha Khoa Kim Dung',
        'meta_desc': 'Bọc răng sứ thẩm mỹ, dán sứ Veneer không mài nhỏ răng tại Nha Khoa Kim Dung Thái Nguyên. Răng toàn sứ Cercon HT, Emax chính hãng Đức & Thụy Sĩ, bảo hành 15 năm.',
        'hero': {
            'tagline': 'THẨM MỸ NỤ CƯỜI CHUẨN NHÂN TƯỚNG HỌC & Y KHOA',
            'title': 'Răng Sứ Tự Nhiên Tinh Xảo — Nâng Tầm Nụ Cười Hoàn Hảo',
            'desc': 'Công nghệ thiết kế nụ cười kỹ thuật số Digital Smile Design (DSD), bảo tồn tối đa răng gốc. Răng toàn sứ cao cấp Đức & Thụy Sĩ không đen viền nướu, trong bóng tự nhiên.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/services/service-cosmetics.webp',
            'trust': [
                'Răng toàn sứ chính hãng Đức & Thụy Sĩ',
                'Bảo tồn tối đa răng thật, không mài nhỏ',
                'Bảo hành chính hãng lên đến 15 năm'
            ]
        },
        'benefits': {
            'tagline': 'NÂNG CẤP NỤ CƯỜI',
            'title': 'Lợi Ích Của Bọc Răng Sứ & Dán Sứ Veneer',
            'desc': 'Khắc phục toàn diện khuyết điểm răng ố vàng, sứt mẻ, lệch lạc nhẹ, mang lại nụ cười chuẩn tỷ lệ vàng.',
            'items': [
                {
                    'icon': 'fa-solid fa-gem',
                    'title': 'Thẩm mỹ tự nhiên trong trẻo',
                    'desc': 'Độ thấu quang và rìa cắn trong bóng tự nhiên như răng thật, không bị trắng bệch giả tạo dưới ánh đèn.'
                },
                {
                    'icon': 'fa-solid fa-shield-heart',
                    'title': 'Không đen viền nướu',
                    'desc': 'Chất liệu 100% toàn sứ nguyên khối cao cấp, tương thích sinh học tuyệt đối, không gây kích ứng nướu hay thâm đen chân răng.'
                },
                {
                    'icon': 'fa-solid fa-bolt',
                    'title': 'Cứng chắc gấp 5 lần răng thật',
                    'desc': 'Khả năng chịu lực uốn cong từ 900 - 1400 MPa, ăn nhai đồ dai cứng thoải mái mà không lo gãy vỡ hay mẻ răng.'
                },
                {
                    'icon': 'fa-solid fa-wand-magic-sparkles',
                    'title': 'Thiết kế nụ cười DSD 3D',
                    'desc': 'Xem trước kết quả nụ cười trên máy tính trước khi làm, điều chỉnh dáng răng hài hòa với nhân tướng và đường nét khuôn mặt.'
                },
                {
                    'icon': 'fa-solid fa-clock',
                    'title': 'Hoàn thiện chỉ sau 2-3 ngày',
                    'desc': 'Hệ thống Labo chế tác răng sứ công nghệ CAD/CAM robot hiện đại giúp rút ngắn thời gian điều trị tối đa, chỉ 2 lần hẹn.'
                },
                {
                    'icon': 'fa-solid fa-lock',
                    'title': 'Bền màu vĩnh viễn',
                    'desc': 'Bề mặt sứ phủ men Nano siêu mịn, kháng bám màu hoàn hảo từ cà phê, trà hay nước tương, nụ cười luôn trắng sáng bền lâu.'
                }
            ]
        },
        'pricing': {
            'tagline': 'BẢNG GIÁ DỊCH VỤ',
            'title': 'Bảng Giá Răng Toàn Sứ Thẩm Mỹ',
            'desc': 'Cam kết 100% phôi sứ chính hãng nhập khẩu có thẻ bảo hành IDPI chính hãng toàn cầu.',
            'tiers': [
                {
                    'name': 'Răng Sứ Zirconia DDBio',
                    'sub': 'Xuất xứ Đức - Bền chắc',
                    'price': '2.500.000đ',
                    'unit': '/ răng hoàn thiện',
                    'popular': False,
                    'features': [
                        'Khung sườn Zirconia nguyên khối Đức',
                        'Chịu lực 900 MPa ăn nhai tốt',
                        'Không đen viền nướu, thẩm mỹ ổn định',
                        'Miễn phí thiết kế nụ cười DSD',
                        'Bảo hành chính hãng 7 năm'
                    ]
                },
                {
                    'name': 'Răng Toàn Sứ Cercon HT',
                    'sub': 'Xuất xứ Đức - Khuyên dùng',
                    'price': '4.500.000đ',
                    'unit': '/ răng hoàn thiện',
                    'popular': True,
                    'features': [
                        'Phôi sứ Cercon HT cao cấp của Dentsply Sirona',
                        'Độ trong mờ tự nhiên vượt trội 43%',
                        'Chịu lực siêu việt lên đến 1200 MPa',
                        'Mài vi phẫu bảo tồn tối đa mô răng thật',
                        'Thẻ bảo hành quét mã QR chính hãng',
                        'Bảo hành chính hãng 10 năm'
                    ]
                },
                {
                    'name': 'Mặt Dán Sứ Veneer Emax',
                    'sub': 'Thụy Sĩ - Đỉnh cao bảo tồn',
                    'price': '6.500.000đ',
                    'unit': '/ răng hoàn thiện',
                    'popular': False,
                    'features': [
                        'Độ mỏng siêu việt chỉ 0.2 - 0.5 mm',
                        'Không cần mài răng hoặc chỉ nhám bề mặt',
                        'Chất liệu thủy tinh sứ Emax Press Thụy Sĩ',
                        'Độ phản quang và sắc thái màu đỉnh cao',
                        'Bảo tồn 100% tủy răng và men răng gốc',
                        'Bảo hành chính hãng 15 năm'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'QUY TRÌNH THỰC HIỆN',
            'title': 'Quy Trình Làm Răng Sứ 4 Bước Chuẩn Y Khoa',
            'desc': 'Từng công đoạn được thực hiện tỉ mỉ dưới kính lúp phóng đại, bảo đảm độ khít sát vi thể 0.01mm.',
            'steps': [
                {
                    'num': '01',
                    'title': 'Thăm khám & Thiết kế DSD',
                    'desc': 'Kiểm tra khớp cắn, chụp ảnh studio phân tích tỉ lệ nụ cười và lên bản vẽ thiết kế 3D nụ cười mong muốn.',
                    'tag': '✦ Cá nhân hóa dáng răng'
                },
                {
                    'num': '02',
                    'title': 'Chuẩn bị cùi răng & Lấy dấu 3D',
                    'desc': 'Sửa soạn mô răng tối thiểu không đau, quét dấu hàm kỹ thuật số bằng máy scan 3D hiện đại gửi đến Labo chế tác.',
                    'tag': '✦ Không đau, không ê buốt'
                },
                {
                    'num': '03',
                    'title': 'Chế tác Labo CAD/CAM',
                    'desc': 'Răng sứ được cắt gọt tự động bằng máy tiện 5 trục từ phôi sứ nguyên khối và đắp lớp màu thủ công tinh tế.',
                    'tag': '✦ Tinh xảo từng đường vân'
                },
                {
                    'num': '04',
                    'title': 'Thử dáng & Gắn cố định',
                    'desc': 'Khách hàng duyệt màu sắc và dáng răng trực tiếp trên miệng, sau đó bác sĩ dán răng vĩnh viễn bằng xi măng nha khoa sinh học.',
                    'tag': '✦ Tự tin tỏa sáng'
                }
            ]
        },
        'criteria': {
            'tagline': 'ĐỐI TƯỢNG PHÙ HỢP',
            'title': 'Khi Nào Bạn Nên Làm Răng Sứ Thẩm Mỹ?',
            'left_title': 'Trường hợp được khuyên dùng',
            'left_items': [
                ('Răng nhiễm màu nặng do kháng sinh', 'Răng bị ố vàng, nhiễm Tetracycline nặng mà phương pháp tẩy trắng răng không đem lại hiệu quả.'),
                ('Răng sứt mẻ, mòn men hoặc vỡ lớn', 'Răng bị mẻ do tai nạn hoặc mòn men gây ê buốt, cần bọc sứ để tái tạo hình thể và bảo vệ tủy răng.'),
                ('Răng thưa kẽ, hình dáng xấu', 'Răng cửa thưa, kích thước các răng không đều hoặc răng hình cánh bướm.'),
                ('Răng đã điều trị tủy', 'Răng sau khi diệt tủy trở nên giòn và dễ gãy vỡ, bắt buộc phải bọc sứ bảo vệ dài lâu.')
            ],
            'right_title': 'Tiêu chuẩn an toàn tại Kim Dung',
            'right_items': [
                ('Nguyên tắc bảo tồn mô răng gốc', 'Tuyệt đối không mài nhỏ răng thành que tăm, bảo vệ tối đa ngà răng và tủy sống.'),
                ('Đường hoàn tất tinh vi sát khít', 'Kỹ thuật lấy đường hoàn tất bờ vai/bờ vát giúp nướu ôm khít răng sứ, không đọng thức ăn.'),
                ('Khớp cắn chuẩn sinh lý', 'Không gây kênh cộm, không mỏi hàm hay ảnh hưởng tới khớp thái dương hàm.'),
                ('100% Vật liệu sứ chính hãng', 'Có thẻ bảo hành IDPI truy xuất nguồn gốc chính hãng từ nhà sản xuất quốc tế.')
            ]
        },
        'faq': [
            {
                'q': 'Bọc răng sứ có phải diệt tủy không?',
                'a': 'Tại Nha Khoa Kim Dung, nguyên tắc số 1 là bảo tồn tủy răng sống. Đa số các trường hợp bọc răng sứ thẩm mỹ hay dán sứ Veneer đều KHÔNG CẦN diệt tủy. Bác sĩ chỉ chỉ định lấy tủy khi răng đã bị viêm tủy nặng trước đó hoặc sâu vỡ lan đến buồng tủy.'
            },
            {
                'q': 'Làm răng sứ có bị hôi miệng hay viêm lợi không?',
                'a': 'Hoàn toàn KHÔNG nếu được thực hiện đúng kỹ thuật. Nguyên nhân gây hôi miệng hoặc viêm lợi ở các cơ sở kém uy tín là do mài phạm khoảng sinh học và lắp răng bị hở mép. Tại Kim Dung, răng sứ được quét 3D và tiện CNC sát khít 100%, nướu răng hoàn toàn khỏe mạnh, hồng hào.'
            },
            {
                'q': 'Dán sứ Veneer khác gì so với bọc răng sứ thông thường?',
                'a': 'Dán sứ Veneer là đỉnh cao của nha khoa thẩm mỹ bảo tồn. Bác sĩ chỉ cần làm nhám một lớp siêu mỏng 0.2 - 0.5mm ở mặt ngoài răng (thậm chí không cần mài), không tác động mặt trong và các góc cạnh. Phương pháp này giữ nguyên 100% răng thật bên trong.'
            },
            {
                'q': 'Răng sứ dùng được bao nhiêu năm?',
                'a': 'Răng toàn sứ chính hãng có tuổi thọ từ 15 đến 25 năm, thậm chí trọn đời nếu bạn chăm sóc vệ sinh đúng cách và tái khám lấy cao răng định kỳ mỗi 6 tháng.'
            },
            {
                'q': 'Bọc răng sứ có ăn uống bình thường được không?',
                'a': 'Răng toàn sứ có độ cứng chịu lực từ 900 - 1400 MPa (gấp 4-6 lần răng tự nhiên), do đó sau khi hoàn thiện bạn có thể ăn nhai hoàn toàn thoải mái mọi món ăn thường ngày mà không phải kiêng khem phức tạp.'
            }
        ]
    },

    'nieng-rang-tham-my.html': {
        'title': 'Niềng Răng Máng Trong Suốt Invisalign – Nha Khoa Kim Dung',
        'meta_desc': 'Niềng răng máng trong suốt Invisalign chính hãng Hoa Kỳ tại Nha Khoa Kim Dung. Vô hình, êm ái, biết trước kết quả 3D ClinCheck, trả góp 0% lãi suất.',
        'hero': {
            'tagline': 'CHỈNH NHA KỸ THUẬT SỐ HÀNG ĐẦU HOA KỲ',
            'title': 'Niềng Răng Vô Hình Invisalign — Nụ Cười Đẹp Không Lộ Mắc Cài',
            'desc': 'Khay niềng trong suốt độc quyền SmartTrack ôm sát khít răng, tháo lắp linh hoạt khi ăn uống và vệ sinh. Biết trước hành trình dịch chuyển răng qua mô phỏng 3D ClinCheck.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/services/service-invisalign.webp',
            'trust': [
                'Xem trước kết quả nụ cười với ClinCheck 3D',
                'Trả góp 0% lãi suất chỉ từ 2.000.000đ/tháng',
                'Bác sĩ đạt chứng chỉ Platinum Invisalign quốc tế'
            ]
        },
        'benefits': {
            'tagline': 'ĐẶC QUYỀN CÔNG NGHỆ',
            'title': 'Tại Sao Hàng Triệu Người Chọn Invisalign?',
            'desc': 'Trải nghiệm hành trình làm đẹp tinh tế, không ai nhận ra bạn đang niềng răng.',
            'items': [
                {
                    'icon': 'fa-solid fa-eye-slash',
                    'title': 'Vô hình gần như tuyệt đối',
                    'desc': 'Khay niềng bằng vật liệu SmartTrack trong suốt siêu mỏng, người đối diện rất khó nhận biết ngay cả ở cự ly gần.'
                },
                {
                    'icon': 'fa-solid fa-utensils',
                    'title': 'Tháo lắp dễ dàng tiện lợi',
                    'desc': 'Tự do tháo khay khi ăn uống những món yêu thích và đánh răng, dùng chỉ nha khoa dễ dàng như bình thường.'
                },
                {
                    'icon': 'fa-solid fa-feather',
                    'title': 'Êm ái, không tổn thương môi má',
                    'desc': 'Không có dây cung hay mắc cài kim loại sắc nhọn, không lo cọ xát gây nhiệt miệng hay chảy máu nướu.'
                },
                {
                    'icon': 'fa-solid fa-laptop-medical',
                    'title': 'Biết trước kết quả qua ClinCheck 3D',
                    'desc': 'Phần mềm độc quyền mô phỏng chính xác từng bước di chuyển răng và hình ảnh nụ cười hoàn thiện ngay từ ngày đầu tiên.'
                },
                {
                    'icon': 'fa-solid fa-calendar-check',
                    'title': 'Giảm số lần tới nha khoa',
                    'desc': 'Bệnh nhân được nhận bộ khay theo giai đoạn và tự thay tại nhà mỗi 1-2 tuần, chỉ cần tái khám kiểm tra mỗi 6-8 tuần.'
                },
                {
                    'icon': 'fa-solid fa-shield-halved',
                    'title': 'Bảo tồn men răng tối đa',
                    'desc': 'Không đọng vôi răng hay sâu răng quanh mắc cài, giữ hàm răng luôn sạch sẽ, thơm tho suốt quá trình chỉnh nha.'
                }
            ]
        },
        'pricing': {
            'tagline': 'BẢNG GIÁ INVISALIGN',
            'title': 'Bảng Giá Niềng Răng Trong Suốt Invisalign Hoa Kỳ',
            'desc': 'Cam kết khay niềng chính hãng sản xuất trực tiếp tại nhà máy Align Technology Hoa Kỳ.',
            'tiers': [
                {
                    'name': 'Invisalign Express',
                    'sub': 'Mức độ nhẹ (Dưới 7 khay)',
                    'price': '35.000.000đ',
                    'unit': '/ trọn gói điều trị',
                    'popular': False,
                    'features': [
                        'Dành cho răng chen chúc hoặc thưa nhẹ',
                        'Khắc phục tái phát sau niềng răng trước đây',
                        'Thời gian điều trị thần tốc 3 - 6 tháng',
                        'Quét dấu hàm 3D bằng máy iTero Element',
                        'Tặng kèm 1 bộ hàm duy trì sau niềng'
                    ]
                },
                {
                    'name': 'Invisalign Moderate',
                    'sub': 'Mức độ vừa - Khuyên dùng',
                    'price': '65.000.000đ',
                    'unit': '/ trọn gói điều trị',
                    'popular': True,
                    'features': [
                        'Số lượng lên tới 20 - 26 cặp khay',
                        'Điều trị răng khấp khểnh, hô móm mức độ trung bình',
                        'Phần mềm mô phỏng ClinCheck 3D chuẩn xác',
                        'Thời gian điều trị trung bình 9 - 14 tháng',
                        'Bác sĩ theo dõi sát sao tiến độ di chuyển răng',
                        'Hỗ trợ trả góp 0% lãi suất theo từng đợt'
                    ]
                },
                {
                    'name': 'Invisalign Comprehensive',
                    'sub': 'Gói toàn diện - Không giới hạn',
                    'price': '89.000.000đ',
                    'unit': '/ trọn gói điều trị',
                    'popular': False,
                    'features': [
                        'Không giới hạn số lượng khay điều trị',
                        'Giải quyết mọi ca sai lệch khớp cắn phức tạp nhất',
                        'Miễn phí khay tinh chỉnh bổ sung trong 5 năm',
                        'Tặng gói tẩy trắng răng công nghệ Laser sau tháo niềng',
                        'Tặng bộ hàm duy trì Vivera cao cấp Hoa Kỳ'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'LỘ TRÌNH ĐIỀU TRỊ',
            'title': 'Hành Trình Kiến Tạo Nụ Cười Cùng Invisalign',
            'desc': 'Quy trình chuẩn hóa quốc tế với sự đồng hành 1:1 của bác sĩ chỉnh nha chuyên khoa.',
            'steps': [
                {
                    'num': '01',
                    'title': 'Scan 3D iTero & Khám chuyên sâu',
                    'desc': 'Sử dụng máy scan iTero Lumina thế hệ mới quét 6000 tấm ảnh/giây, ghi lại chính xác từng milimet khớp cắn.',
                    'tag': '✦ Không cần lấy dấu cao su'
                },
                {
                    'num': '02',
                    'title': 'Xem trước nụ cười ClinCheck',
                    'desc': 'Bác sĩ cùng chuyên gia Align Technology thiết kế phác đồ 3D cá nhân hóa. Bạn được xem trước nụ cười hoàn mỹ.',
                    'tag': '✦ Thấy trước tương lai'
                },
                {
                    'num': '03',
                    'title': 'Nhận bộ khay từ Hoa Kỳ',
                    'desc': 'Bộ khay được in 3D riêng biệt và chuyển từ Mỹ về. Bác sĩ gắn Attachment và hướng dẫn cách đeo, vệ sinh khay.',
                    'tag': '✦ Đeo 20-22h mỗi ngày'
                },
                {
                    'num': '04',
                    'title': 'Theo dõi tiến trình & Đeo duy trì',
                    'desc': 'Tái khám định kỳ mỗi 6-8 tuần kiểm tra độ dịch chuyển. Sau khi hoàn tất, đeo khay duy trì để giữ nụ cười đẹp vĩnh viễn.',
                    'tag': '✦ Nụ cười đều đẹp bền lâu'
                }
            ]
        },
        'criteria': {
            'tagline': 'ĐỐI TƯỢNG PHÙ HỢP',
            'title': 'Ai Nên Chọn Niềng Răng Trong Suốt?',
            'left_title': 'Trường hợp lý tưởng',
            'left_items': [
                ('Người làm công việc giao tiếp nhiều', 'Doanh nhân, giáo viên, MC, tiếp viên hàng không, người thường xuyên gặp gỡ khách hàng.'),
                ('Răng khấp khểnh, chen chúc hoặc thưa', 'Cần dàn đều răng về đúng vị trí cung hàm một cách kín đáo và thẩm mỹ.'),
                ('Khớp cắn hở, cắn sâu, cắn chéo', 'Sai lệch khớp cắn ảnh hưởng chức năng ăn nhai và thẩm mỹ đường nét khuôn mặt.'),
                ('Người ở xa, du học sinh, bận rộn', 'Không có nhiều thời gian đi tái khám siết mắc cài hàng tháng tại nha khoa.')
            ],
            'right_title': 'Cam kết từ Nha Khoa Kim Dung',
            'right_items': [
                ('100% Khay niềng nhập khẩu Hoa Kỳ', 'Có mã định danh cá nhân khắc laser trên từng khay niềng chính hãng.'),
                ('Bác sĩ chỉnh nha chứng chỉ Quốc tế', 'Trực tiếp lên kế hoạch ClinCheck và đồng hành trong suốt quá trình niềng.'),
                ('Cam kết hiệu quả bằng hợp đồng', 'Đảm bảo răng chạy chuẩn theo phác đồ mô phỏng đã thống nhất ban đầu.'),
                ('Chính sách trả góp linh hoạt 0%', 'Chia nhỏ chi phí đóng theo từng tháng giúp bạn an tâm làm đẹp.')
            ]
        },
        'faq': [
            {
                'q': 'Niềng răng Invisalign có hiệu quả bằng niềng răng mắc cài không?',
                'a': 'Hoàn toàn tương đương. Với công nghệ vật liệu SmartTrack thế hệ mới kết hợp cùng các điểm tạo lực Attachment siêu nhỏ dán lên răng, Invisalign có khả năng điều trị thành công hầu hết các ca phức tạp từ hô móm, khớp cắn ngược đến răng khấp khểnh nặng.'
            },
            {
                'q': 'Một ngày tôi cần phải đeo khay niềng bao nhiêu tiếng?',
                'a': 'Để đạt hiệu quả tối ưu theo đúng lộ trình, bạn cần đeo khay niềng từ 20 đến 22 tiếng mỗi ngày. Bạn chỉ nên tháo khay ra khi ăn uống các món ăn nóng/cứng và khi đánh răng.'
            },
            {
                'q': 'Niềng răng Invisalign có đau không?',
                'a': 'Invisalign được đánh giá là phương pháp chỉnh nha êm ái nhất hiện nay. Trong 1-2 ngày đầu tiên khi đổi sang khay mới, bạn chỉ có cảm giác hơi căng tức nhẹ do các răng bắt đầu dịch chuyển. Cảm giác này sẽ nhanh chóng biến mất.'
            },
            {
                'q': 'Bao nhiêu tuổi thì có thể bắt đầu niềng răng Invisalign?',
                'a': 'Invisalign có các dòng sản phẩm dành riêng cho từng độ tuổi: Invisalign First (cho trẻ em từ 6-10 tuổi can thiệp sớm), Invisalign Teen (cho lứa tuổi thanh thiếu niên) và Invisalign Adults (cho người trưởng thành mọi độ tuổi).'
            },
            {
                'q': 'Hình thức trả góp niềng răng tại Kim Dung như thế nào?',
                'a': 'Bạn chỉ cần thanh toán trước từ 30% chi phí ban đầu khi nhận khay. Số tiền còn lại sẽ được chia đều trả góp hàng tháng với lãi suất 0% trong suốt thời gian điều trị mà không phát sinh thêm bất kỳ chi phí nào.'
            }
        ]
    },

    'nieng-rang-mac-cai.html': {
        'title': 'Niềng Răng Mắc Cài Chuẩn Y Khoa – Nha Khoa Kim Dung Thái Nguyên',
        'meta_desc': 'Niềng răng mắc cài kim loại, mắc cài sứ tự buộc chuẩn y khoa tại Nha Khoa Kim Dung. Khắc phục triệt để răng hô, móm, khấp khểnh. Trả góp 0% chỉ từ 1 triệu/tháng.',
        'hero': {
            'tagline': 'CHỈNH NHA CHUẨN KHỚP CẮN & THẨM MỸ GƯƠNG MẶT',
            'title': 'Niềng Răng Mắc Cài — Nụ Cười Đều Đẹp, Góc Nghiêng Cân Đối',
            'desc': 'Giải pháp chỉnh nha kinh điển với lực kéo chính xác, hiệu quả bền vững cho mọi ca răng hô, móm, khấp khểnh phức tạp. Hợp đồng cam kết tiến độ và trả góp chỉ từ 1.000.000đ/tháng.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/services/service-invisalign.webp',
            'trust': [
                'Trả góp 0% chỉ từ 1.000.000đ/tháng',
                'Bác sĩ chuyên khoa chỉnh nha trên 12 năm kinh nghiệm',
                'Hợp đồng cam kết hiệu quả rõ ràng'
            ]
        },
        'benefits': {
            'tagline': 'HIỆU QUẢ VƯỢT TRỘI',
            'title': 'Ưu Điểm Vàng Của Niềng Răng Mắc Cài',
            'desc': 'Kiểm soát lực kéo răng 3 chiều chuẩn xác, đem lại khớp cắn chuẩn sinh lý và thẩm mỹ tối ưu.',
            'items': [
                {
                    'icon': 'fa-solid fa-bullseye',
                    'title': 'Giải quyết triệt để mọi ca khó',
                    'desc': 'Đặc biệt hiệu quả với các ca sai lệch nặng: hô hàm, móm nặng, răng xoay trục, răng ngầm mà khay niềng khó thực hiện.'
                },
                {
                    'icon': 'fa-solid fa-piggy-bank',
                    'title': 'Chi phí tiết kiệm, hợp lý nhất',
                    'desc': 'Mức đầu tư hợp lý nhất trong tất cả các phương pháp chỉnh nha, cực kỳ phù hợp với học sinh, sinh viên và người trẻ.'
                },
                {
                    'icon': 'fa-solid fa-gauge-high',
                    'title': 'Lực kéo ổn định, liên tục',
                    'desc': 'Dây cung và mắc cài tạo lực siết liên tục 24/7, giúp răng dịch chuyển tuần tự và chuẩn xác theo đúng phác đồ của bác sĩ.'
                },
                {
                    'icon': 'fa-solid fa-stopwatch',
                    'title': 'Rút ngắn thời gian với mắc cài tự buộc',
                    'desc': 'Công nghệ nắp trượt tự động giảm tối đa lực ma sát, hạn chế đau nhức và rút ngắn thời gian điều trị từ 4 - 6 tháng.'
                },
                {
                    'icon': 'fa-solid fa-face-smile',
                    'title': 'Thẩm mỹ cùng mắc cài sứ',
                    'desc': 'Chất liệu sứ sinh học màu sắc tương đồng với màu men răng tự nhiên, giúp người niềng tự tin thoải mái giao tiếp.'
                },
                {
                    'icon': 'fa-solid fa-heart-pulse',
                    'title': 'Cải thiện tiêu hóa & khớp hàm',
                    'desc': 'Đưa khớp cắn về vị trí chuẩn giúp việc nghiền nát thức ăn dễ dàng hơn, bảo vệ đường tiêu hóa và khớp thái dương hàm.'
                }
            ]
        },
        'pricing': {
            'tagline': 'CHI PHÍ ĐIỀU TRỊ',
            'title': 'Bảng Giá Niềng Răng Mắc Cài Minh Bạch',
            'desc': 'Giá trọn gói cho 2 hàm, cam kết không phát sinh chi phí trong suốt quá trình niềng.',
            'tiers': [
                {
                    'name': 'Mắc Cài Kim Loại Chuẩn',
                    'sub': 'Tiết kiệm chi phí nhất',
                    'price': '25.000.000đ',
                    'unit': '/ trọn gói 2 hàm',
                    'popular': False,
                    'features': [
                        'Chất liệu hợp kim y khoa chống gỉ cao cấp',
                        'Hiệu quả nắn chỉnh tối ưu cho mọi lứa tuổi',
                        'Đa dạng màu thun niềng trẻ trung, cá tính',
                        'Tặng gói chụp phim X-quang Panorama & Cephalo',
                        'Trả góp 0% chỉ từ 1.000.000đ/tháng'
                    ]
                },
                {
                    'name': 'Mắc Cài Kim Loại Tự Buộc',
                    'sub': 'Thông minh - Khuyên dùng',
                    'price': '35.000.000đ',
                    'unit': '/ trọn gói 2 hàm',
                    'popular': True,
                    'features': [
                        'Hệ thống nắp trượt thông minh tự đóng mở',
                        'Giảm 80% lực ma sát, ít đau nhức khó chịu',
                        'Rút ngắn thời gian niềng răng từ 4 - 6 tháng',
                        'Dễ dàng vệ sinh, hạn chế bám dính thức ăn',
                        'Khoảng cách giữa các lần tái khám dài hơn (6-8 tuần)'
                    ]
                },
                {
                    'name': 'Mắc Cài Sứ Thẩm Mỹ Pha Lê',
                    'sub': 'Thẩm mỹ cao, khó nhận biết',
                    'price': '45.000.000đ',
                    'unit': '/ trọn gói 2 hàm',
                    'popular': False,
                    'features': [
                        'Hạt mắc cài bằng sứ sinh học cao cấp nguyên khối',
                        'Màu sắc trùng khớp với men răng tự nhiên',
                        'Góc cạnh được bo tròn êm dịu cho môi má',
                        'Không bị bám màu hay đổi màu theo thời gian',
                        'Tặng kèm 1 bộ hàm duy trì tháo lắp sau niềng'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'QUY TRÌNH CHUẨN Y KHOA',
            'title': 'Quy Trình Chỉnh Nha 4 Bước Tại Kim Dung',
            'desc': 'Bác sĩ chuyên khoa trực tiếp theo dõi và siết mắc cài trong từng giai đoạn.',
            'steps': [
                {
                    'num': '01',
                    'title': 'Thăm khám & Phân tích phim',
                    'desc': 'Chụp phim X-quang sọ nghiêng Cephalo và Panorama, lấy dấu hàm phân tích chỉ số góc xương và trục răng.',
                    'tag': '✦ Đo đạc chuẩn xác'
                },
                {
                    'num': '02',
                    'title': 'Ký hợp đồng điều trị',
                    'desc': 'Bác sĩ trao đổi phác đồ chi tiết, thời gian dự kiến và ký cam kết kết quả điều trị bằng văn bản pháp lý.',
                    'tag': '✦ Minh bạch quyền lợi'
                },
                {
                    'num': '03',
                    'title': 'Gắn mắc cài & Điều trị',
                    'desc': 'Vệ sinh răng miệng tổng quát và gắn mắc cài lên bề mặt răng. Bác sĩ hướng dẫn chế độ ăn uống và vệ sinh.',
                    'tag': '✦ Bắt đầu dịch chuyển'
                },
                {
                    'num': '04',
                    'title': 'Tái khám định kỳ & Tháo niềng',
                    'desc': 'Tái khám mỗi tháng để thay dây cung và kích hoạt lực. Tháo mắc cài khi răng đều đẹp và đeo hàm duy trì.',
                    'tag': '✦ Nụ cười tỏa sáng'
                }
            ]
        },
        'criteria': {
            'tagline': 'CHỈ ĐỊNH ĐIỀU TRỊ',
            'title': 'Trường Hợp Cần Niềng Răng Mắc Cài',
            'left_title': 'Khuyết điểm nên khắc phục',
            'left_items': [
                ('Răng hô, vẩu, chìa ra ngoài', 'Hàm trên chìa ra phía trước nhiều khiến môi không khép kín tự nhiên, mất tự tin góc nghiêng.'),
                ('Răng móm (khớp cắn ngược)', 'Răng hàm dưới phủ ra ngoài răng hàm trên, khuôn mặt có dạng gãy hoặc lưỡi cày.'),
                ('Răng khấp khểnh, chen chúc lộn xộn', 'Các răng mọc chen chúc, lệch khỏi cung hàm gây dắt thức ăn và nguy cơ sâu răng cao.'),
                ('Khớp cắn sâu, cắn hở, cắn đối đầu', 'Răng cửa không chạm nhau hoặc hàm trên phủ sâu toàn bộ hàm dưới ảnh hưởng ăn nhai.')
            ],
            'right_title': 'Cam kết từ Nha Khoa Kim Dung',
            'right_items': [
                ('Bác sĩ chuyên khoa giàu kinh nghiệm', 'Trực tiếp Bác sĩ CKI Chỉnh nha nắn chỉnh, không giao phó cho kỹ thuật viên.'),
                ('Vật liệu chính hãng 3M & Ormco Hoa Kỳ', 'Toàn bộ mắc cài và dây cung nhập khẩu chính hãng từ các thương hiệu hàng đầu thế giới.'),
                ('Hạn chế tối đa việc nhổ răng', 'Ứng dụng các khí cụ nong hàm, di xa răng hiện đại để bảo tồn răng tự nhiên tối đa.'),
                ('Hợp đồng cam kết rõ ràng', 'Minh bạch chi phí, thời gian và kết quả trước khi bắt đầu điều trị.')
            ]
        },
        'faq': [
            {
                'q': 'Niềng răng mắc cài có đau không?',
                'a': 'Trong khoảng 3-5 ngày đầu sau khi gắn mắc cài hoặc mỗi lần siết dây cung định kỳ, bạn sẽ cảm thấy ê tức nhẹ do răng bắt đầu chịu lực dịch chuyển. Cảm giác này hoàn toàn nằm trong ngưỡng chịu đựng và sẽ giảm dần sau vài ngày. Mắc cài tự buộc sẽ êm ái hơn mắc cài thường rất nhiều.'
            },
            {
                'q': 'Niềng răng có bắt buộc phải nhổ răng không?',
                'a': 'Không phải ca nào cũng cần nhổ răng. Tại Kim Dung, bác sĩ luôn ưu tiên bảo tồn răng thật bằng các kỹ thuật như nong hàm, mài kẽ hoặc di xa cung răng. Chỉ những ca răng quá chen chúc hoặc hô nặng thiếu khoảng trống trầm trọng mới cần nhổ răng để đạt thẩm mỹ tối ưu.'
            },
            {
                'q': 'Thời gian niềng răng mắc cài thường mất bao lâu?',
                'a': 'Thời gian trung bình dao động từ 18 đến 24 tháng tùy thuộc vào mức độ sai lệch của răng và độ tuổi của bệnh nhân. Với trẻ em ở giai đoạn phát triển hoặc ca sai lệch nhẹ, thời gian có thể rút ngắn chỉ từ 12 - 15 tháng.'
            },
            {
                'q': 'Mắc cài tự buộc khác gì so với mắc cài truyền thống?',
                'a': 'Mắc cài truyền thống dùng thun buộc để giữ dây cung, dễ bị dão và tạo ma sát lớn. Mắc cài tự buộc có nắp trượt thông minh giữ dây cung tự do, giảm ma sát tối đa, ít đau hơn, dễ vệ sinh và giúp rút ngắn thời gian điều trị từ 4 - 6 tháng.'
            },
            {
                'q': 'Chính sách trả góp niềng răng tại Kim Dung như thế nào?',
                'a': 'Bạn chỉ cần thanh toán trước 30% khi gắn mắc cài. Số tiền còn lại được chia đều trả góp không lãi suất chỉ từ 1.000.000đ/tháng trong suốt quá trình điều trị.'
            }
        ]
    },

    'tay-trang-rang.html': {
        'title': 'Tẩy Trắng Răng Công Nghệ Cao Không Ê Buốt – Nha Khoa Kim Dung',
        'meta_desc': 'Tẩy trắng răng công nghệ Laser WhiteMax Hoa Kỳ tại Nha Khoa Kim Dung Thái Nguyên. Bật 2-4 tông trắng sáng sau 45 phút, an toàn tuyệt đối, không ê buốt.',
        'hero': {
            'tagline': 'CÔNG NGHỆ ÁNH SÁNG XANH WHITE MAX HOA KỲ',
            'title': 'Tẩy Trắng Răng An Toàn — Bật 2 Đến 4 Tông Chỉ Sau 45 Phút',
            'desc': 'Ứng dụng công nghệ Laser WhiteMax kích hoạt phân tử làm trắng sâu vào men răng mà không gây mòn men hay ê buốt. Thuốc tẩy trắng chính hãng chuẩn FDA, bảo vệ nướu tối đa.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/services/service-whitening.webp',
            'trust': [
                'Bật 2 - 4 tông trắng sáng tự nhiên chỉ sau 45 phút',
                'Hoàn toàn không ê buốt, an toàn tuyệt đối cho men răng',
                'Thuốc chính hãng Opalescence & Philips Zoom Hoa Kỳ'
            ]
        },
        'benefits': {
            'tagline': 'HIỆU QUẢ TỨC THÌ',
            'title': 'Lợi Ích Của Tẩy Trắng Răng WhiteMax',
            'desc': 'Khôi phục nụ cười rạng rỡ, tự tin cuốn hút chỉ sau một lần hẹn duy nhất.',
            'items': [
                {
                    'icon': 'fa-solid fa-wand-magic-sparkles',
                    'title': 'Bật tông trắng sáng tức thì',
                    'desc': 'Hạt hoạt tính thâm nhập phá vỡ chuỗi liên kết màu sắc cứng đầu, giúp răng trắng sáng bật từ 2 - 4 tông chỉ sau 45 phút.'
                },
                {
                    'icon': 'fa-solid fa-shield-heart',
                    'title': 'Không ê buốt, không hại men răng',
                    'desc': 'Ánh sáng lạnh kết hợp gel bù khoáng ngừa nhạy cảm, giữ men răng nguyên vẹn, êm ái nhẹ nhàng suốt quá trình thực hiện.'
                },
                {
                    'icon': 'fa-solid fa-circle-check',
                    'title': 'Đạt chuẩn an toàn FDA Hoa Kỳ',
                    'desc': 'Thuốc tẩy trắng chính hãng nhập khẩu từ Mỹ, nồng độ được kiểm soát chính xác theo tiêu chuẩn an toàn nha khoa quốc tế.'
                },
                {
                    'icon': 'fa-solid fa-umbrella',
                    'title': 'Bảo vệ mô mềm và nướu răng',
                    'desc': 'Quy trình cách ly nướu chuyên nghiệp bằng đập cao su và gel cô lập nướu Dam, tránh tuyệt đối tiếp xúc với môi má.'
                },
                {
                    'icon': 'fa-solid fa-clock-rotate-left',
                    'title': 'Duy trì độ trắng từ 2 - 3 năm',
                    'desc': 'Hiệu quả trắng sáng duy trì dài lâu nếu bạn tuân thủ chế độ vệ sinh và hạn chế các thực phẩm quá đậm màu.'
                },
                {
                    'icon': 'fa-solid fa-star',
                    'title': 'Nâng tầm nhan sắc tức thì',
                    'desc': 'Nụ cười trắng sáng giúp bạn trẻ trung hơn, tự tin tỏa sáng trong các sự kiện quan trọng, buổi tiệc, phỏng vấn hay đám cưới.'
                }
            ]
        },
        'pricing': {
            'tagline': 'BẢNG GIÁ DỊCH VỤ',
            'title': 'Bảng Giá Tẩy Trắng Răng Minh Bạch',
            'desc': 'Trọn gói liệu trình bao gồm cạo vôi răng và đánh bóng làm sạch trước khi tẩy trắng.',
            'tiers': [
                {
                    'name': 'Gói Tẩy Trắng Tại Nhà',
                    'sub': 'Chủ động, tiện lợi',
                    'price': '1.200.000đ',
                    'unit': '/ trọn bộ sản phẩm',
                    'popular': False,
                    'features': [
                        'Lấy dấu đúc máng tẩy cá nhân hóa ôm khít răng',
                        'Bộ 2 tuýp thuốc tẩy trắng Opalescence chính hãng Mỹ',
                        'Bác sĩ hướng dẫn tỉ mỉ liều lượng và cách đeo máng',
                        'Sử dụng thuận tiện vào buổi tối khi đi ngủ',
                        'Hiệu quả trắng sáng rõ rệt sau 7 - 10 ngày'
                    ]
                },
                {
                    'name': 'Laser WhiteMax Phòng Khám',
                    'sub': 'Nhanh chóng - Khuyên dùng',
                    'price': '2.200.000đ',
                    'unit': '/ liệu trình 45 phút',
                    'popular': True,
                    'features': [
                        'Miễn phí lấy cao răng và đánh bóng bề mặt men răng',
                        'Cách ly nướu an toàn tuyệt đối với gel chuyên dụng',
                        'Chiếu ánh sáng Laser WhiteMax kích hoạt 3 chu kỳ',
                        'Bật ngay 2 - 4 tông màu răng sau 45 phút',
                        'Thoa gel bù khoáng Fluoride ngừa ê buốt độc quyền'
                    ]
                },
                {
                    'name': 'Gói Kết Hợp Đôi Hoàn Hảo',
                    'sub': 'Hiệu quả trắng sáng vĩnh viễn',
                    'price': '3.200.000đ',
                    'unit': '/ combo trọn gói',
                    'popular': False,
                    'features': [
                        'Trọn gói 1 buổi tẩy trắng Laser WhiteMax tại phòng khám',
                        'Tặng bộ máng tẩy cá nhân hóa cao cấp',
                        'Tặng thêm 2 tuýp thuốc duy trì tại nhà',
                        'Duy trì độ trắng sáng bền vững lên đến 3 - 5 năm',
                        'Giải pháp toàn diện nhất cho người răng ố vàng lâu năm'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'QUY TRÌNH THỰC HIỆN',
            'title': 'Quy Trình Tẩy Trắng 4 Bước Nhanh Gọn',
            'desc': 'Thực hiện trực tiếp trong phòng điều trị tiêu chuẩn vô trùng khép kín.',
            'steps': [
                {
                    'num': '01',
                    'title': 'Thăm khám & So màu răng',
                    'desc': 'Bác sĩ kiểm tra men răng, so sánh tông màu hiện tại trên bảng so màu Vita và chụp ảnh lưu hồ sơ theo dõi.',
                    'tag': '✦ Đánh giá mức độ ố vàng'
                },
                {
                    'num': '02',
                    'title': 'Vệ sinh & Cách ly nướu',
                    'desc': 'Cạo sạch vôi răng mảng bám, đeo dụng cụ banh miệng và bôi gel cách ly bảo vệ nướu và mô mềm tuyệt đối.',
                    'tag': '✦ Bảo vệ an toàn 100%'
                },
                {
                    'num': '03',
                    'title': 'Thoa thuốc & Chiếu Laser',
                    'desc': 'Thoa đều gel làm trắng lên mặt ngoài răng, chiếu ánh sáng Laser WhiteMax kích hoạt phân tử bẻ gãy mảng bám màu.',
                    'tag': '✦ 45 phút êm ái'
                },
                {
                    'num': '04',
                    'title': 'So màu & Thoa bù khoáng',
                    'desc': 'Làm sạch gel thuốc, so lại tông màu răng sau khi tẩy (sáng hơn 2-4 tông) và thoa kem bù khoáng chống ê buốt.',
                    'tag': '✦ Nụ cười trắng sáng'
                }
            ]
        },
        'criteria': {
            'tagline': 'ĐỐI TƯỢNG PHÙ HỢP',
            'title': 'Ai Nên Thực Hiện Tẩy Trắng Răng?',
            'left_title': 'Trường hợp chỉ định tốt',
            'left_items': [
                ('Răng ố vàng do thực phẩm màu', 'Uống nhiều cà phê, trà, rượu vang, nước ngọt có ga hoặc hút thuốc lá thường xuyên.'),
                ('Răng ngả vàng tự nhiên do tuổi tác', 'Lớp men răng mòn dần theo thời gian để lộ lớp ngà răng màu vàng bên trong.'),
                ('Cần làm đẹp cấp tốc cho sự kiện', 'Chuẩn bị chụp ảnh cưới, phỏng vấn xin việc, đi sự kiện hoặc gặp gỡ đối tác.'),
                ('Người có men răng khỏe mạnh', 'Muốn cải thiện màu sắc nụ cười trở nên rạng rỡ, cuốn hút hơn.')
            ],
            'right_title': 'Lưu ý từ Bác sĩ Kim Dung',
            'right_items': [
                ('Điều trị bệnh lý răng miệng trước', 'Nếu có răng sâu, viêm nướu hay mòn cổ răng cần được hàn trám và chữa trị dứt điểm trước khi tẩy.'),
                ('Không áp dụng cho răng bọc sứ', 'Thuốc tẩy trắng chỉ có tác dụng bẻ gãy liên kết màu trên men răng thật, không đổi màu răng sứ.'),
                ('Phụ nữ có thai và trẻ em dưới 16 tuổi', 'Chưa nên thực hiện tẩy trắng răng để đảm bảo an toàn sinh học tốt nhất.'),
                ('Chế độ ăn kiêng màu 48h đầu', 'Hạn chế các thức ăn, đồ uống sẫm màu trong 48 giờ sau tẩy để giữ màu trắng sáng bền nhất.')
            ]
        },
        'faq': [
            {
                'q': 'Tẩy trắng răng có làm mòn hay hỏng men răng không?',
                'a': 'Hoàn toàn KHÔNG. Thuốc tẩy trắng răng chính hãng bản chất là phản ứng oxy hóa khử để cắt đứt các chuỗi protein tạo màu hữu cơ trong ngà răng, không hề bào mòn hay làm mất đi lớp men răng tự nhiên của bạn.'
            },
            {
                'q': 'Trong và sau khi tẩy trắng răng có bị ê buốt không?',
                'a': 'Với công nghệ Laser WhiteMax và gel bù khoáng tại Nha Khoa Kim Dung, hơn 95% khách hàng không hề có cảm giác ê buốt. Một số ít khách hàng có men răng nhạy cảm có thể thấy hơi châm chích nhẹ trong vài tiếng đầu và sẽ hết hẳn sau 24 giờ.'
            },
            {
                'q': 'Hiệu quả tẩy trắng răng giữ được trong bao lâu?',
                'a': 'Màu răng trắng sáng thường duy trì từ 2 đến 3 năm. Độ bền màu phụ thuộc lớn vào thói quen ăn uống và chăm sóc răng miệng của bạn. Nếu hạn chế thuốc lá, cà phê và vệ sinh răng miệng tốt, răng sẽ giữ được độ trắng rất lâu.'
            },
            {
                'q': 'Sau khi tẩy trắng răng cần kiêng những gì?',
                'a': 'Trong vòng 48 giờ đầu tiên sau khi tẩy, bạn nên kiêng các loại đồ uống có màu đậm như cà phê, trà đặc, nước ngọt có ga, nước tương, cà ri và không hút thuốc lá. Nên ăn các thực phẩm có màu trắng hoặc trong như cơm, sữa, cháo trắng, ức gà.'
            },
            {
                'q': 'Nên chọn tẩy trắng tại phòng khám hay làm tại nhà?',
                'a': 'Tẩy trắng tại phòng khám phù hợp nếu bạn muốn có nụ cười trắng sáng ngay lập tức chỉ sau 45 phút dưới sự theo dõi trực tiếp của bác sĩ. Tẩy trắng tại nhà phù hợp nếu bạn có nhiều thời gian và muốn chủ động chia nhỏ thời gian làm đẹp.'
            }
        ]
    },

    'nha-khoa-tong-quat.html': {
        'title': 'Nha Khoa Tổng Quát – Chăm Sóc Nụ Cười Toàn Diện Tại Kim Dung',
        'meta_desc': 'Dịch vụ nha khoa tổng quát tại Nha Khoa Kim Dung Thái Nguyên: lấy cao răng siêu âm, trám răng thẩm mỹ, nhổ răng khôn Piezotome, điều trị tủy không đau.',
        'hero': {
            'tagline': 'CHĂM SÓC RĂNG MIỆNG TOÀN DIỆN CHUẨN Y KHOA',
            'title': 'Nha Khoa Tổng Quát — Nền Tảng Cho Nụ Cười Khỏe Mạnh Trọn Đời',
            'desc': 'Lấy cao răng siêu âm êm ái, hàn trám răng thẩm mỹ tàng hình, nhổ răng khôn Piezotome sóng siêu âm không đau lành thương nhanh. Quy trình vô trùng tuyệt đối chuẩn Bộ Y Tế.',
            'bg_img': 'https://www.nhakhoagreenfield.com/images/services/service-general.webp',
            'trust': [
                'Trang thiết bị hiện đại chuẩn y khoa quốc tế',
                'Đội ngũ bác sĩ tận tâm, điều trị không đau',
                'Phòng khám vô trùng khép kín 100%'
            ]
        },
        'benefits': {
            'tagline': 'BẢO VỆ RĂNG MIỆNG',
            'title': 'Tầm Quan Trọng Của Nha Khoa Tổng Quát',
            'desc': 'Phòng bệnh hơn chữa bệnh — chăm sóc răng miệng định kỳ giúp bảo tồn tối đa hàm răng thật tự nhiên.',
            'items': [
                {
                    'icon': 'fa-solid fa-pump-soap',
                    'title': 'Lấy cao răng siêu âm êm ái',
                    'desc': 'Sóng rung siêu âm bóc tách sạch sẽ 100% mảng bám vôi răng cứng đầu dưới nướu mà không gây đau, không chảy máu.'
                },
                {
                    'icon': 'fa-solid fa-tooth',
                    'title': 'Hàn trám thẩm mỹ tàng hình',
                    'desc': 'Chất liệu Composite cao cấp tái tạo hoàn hảo hình thể răng sâu, sứt mẻ trùng khớp màu men răng, không thể nhận biết.'
                },
                {
                    'icon': 'fa-solid fa-wave-square',
                    'title': 'Nhổ răng khôn Piezotome không đau',
                    'desc': 'Công nghệ rung siêu âm nhẹ nhàng cắt đứt dây chằng quanh răng, bảo vệ xương ổ răng, không sưng má, lành thương sau 24h.'
                },
                {
                    'icon': 'fa-solid fa-shield-virus',
                    'title': 'Điều trị tủy vi phẫu triệt để',
                    'desc': 'Hệ thống định vị chóp răng và trâm xoay dẻo giúp làm sạch buồng tủy viêm triệt để, dứt điểm cơn đau nhức tức thì.'
                },
                {
                    'icon': 'fa-solid fa-stethoscope',
                    'title': 'Phát hiện sớm bệnh lý nguy hiểm',
                    'desc': 'Khám định kỳ giúp tầm soát kịp thời sâu răng ngầm, viêm nha chu tụt lợi, mòn cổ chân răng và các tổn thương niêm mạc.'
                },
                {
                    'icon': 'fa-solid fa-smile-beam',
                    'title': 'Hơi thở thơm tho, tự tin',
                    'desc': 'Loại bỏ hoàn toàn vi khuẩn gây mùi trú ngụ trong các kẽ răng và túi lợi, mang lại sự tự tin trọn vẹn trong giao tiếp.'
                }
            ]
        },
        'pricing': {
            'tagline': 'BẢNG GIÁ DỊCH VỤ',
            'title': 'Bảng Giá Dịch Vụ Nha Khoa Tổng Quát',
            'desc': 'Chi phí hợp lý, phục vụ tận tình chu đáo cho cả người lớn và trẻ em.',
            'tiers': [
                {
                    'name': 'Lấy Cao Răng Siêu Âm',
                    'sub': 'Chăm sóc định kỳ 6 tháng/lần',
                    'price': '150.000đ - 250.000đ',
                    'unit': '/ buổi (2 hàm)',
                    'popular': False,
                    'features': [
                        'Sử dụng đầu rung siêu âm êm ái không buốt',
                        'Làm sạch toàn diện mảng bám trên và dưới nướu',
                        'Đánh bóng bề mặt răng bằng chổi cước nha khoa',
                        'Bôi gel sát khuẩn nướu ngừa viêm nha chu',
                        'Bác sĩ kiểm tra tổng quát toàn bộ hàm răng'
                    ]
                },
                {
                    'name': 'Trám Răng Thẩm Mỹ',
                    'sub': 'Tái tạo răng sâu, mẻ - Khuyên dùng',
                    'price': '250.000đ - 450.000đ',
                    'unit': '/ răng sâu / sứt mẻ',
                    'popular': True,
                    'features': [
                        'Chất liệu Composite 3M nhập khẩu Hoa Kỳ',
                        'Tái tạo hình dáng răng tự nhiên như ban đầu',
                        'Màu sắc đồng nhất hoàn hảo với men răng thật',
                        'Chiếu đèn quang trùng hợp đông cứng tức thì',
                        'Bảo hành độ bền mối hàn trám 1 năm'
                    ]
                },
                {
                    'name': 'Nhổ Răng Khôn Piezotome',
                    'sub': 'Sóng siêu âm không đau',
                    'price': '1.000.000đ - 2.500.000đ',
                    'unit': '/ răng (tùy độ khó)',
                    'popular': False,
                    'features': [
                        'Chụp phim CT 3D định vị chính xác vị trí dây thần kinh',
                        'Công nghệ rung siêu âm Piezotome bóc tách êm ru',
                        'Không rạch vạt lớn, không đau, hạn chế sưng nề',
                        'Đặt màng huyết tương giàu tiểu cầu PRF lành thương siêu tốc',
                        'Tặng thuốc kháng sinh giảm đau cao cấp sau nhổ'
                    ]
                }
            ]
        },
        'workflow': {
            'tagline': 'QUY TRÌNH CHĂM SÓC',
            'title': 'Quy Trình Khám Chữa Chuẩn Y Khoa',
            'desc': 'Tất cả dụng cụ được hấp sấy tiệt trùng tuyệt đối bằng máy hấp áp suất Autoclave theo tiêu chuẩn Bộ Y Tế.',
            'steps': [
                {
                    'num': '01',
                    'title': 'Thăm khám & Chụp X-quang',
                    'desc': 'Bác sĩ kiểm tra toàn diện mô răng, nướu, lưỡi và chụp phim kỹ thuật số phát hiện các tổn thương tiềm ẩn.',
                    'tag': '✦ Tầm soát kỹ lưỡng'
                },
                {
                    'num': '02',
                    'title': 'Tư vấn phác đồ điều trị',
                    'desc': 'Thông báo rõ tình trạng răng miệng, giải pháp điều trị tối ưu và chi phí minh bạch trước khi thực hiện.',
                    'tag': '✦ Thống nhất phương án'
                },
                {
                    'num': '03',
                    'title': 'Điều trị nhẹ nhàng, không đau',
                    'desc': 'Tiến hành thủ thuật trong phòng điều trị vô trùng, áp dụng kỹ thuật gây tê êm dịu và thao tác khéo léo.',
                    'tag': '✦ An tâm, thoải mái'
                },
                {
                    'num': '04',
                    'title': 'Dặn dò chăm sóc tại nhà',
                    'desc': 'Bác sĩ hướng dẫn phương pháp vệ sinh răng miệng đúng cách và hẹn lịch kiểm tra định kỳ mỗi 6 tháng.',
                    'tag': '✦ Đồng hành bảo vệ'
                }
            ]
        },
        'criteria': {
            'tagline': 'DẤU HIỆU CẦN KHÁM',
            'title': 'Khi Nào Bạn Cần Tới Phòng Khám Nha Khoa?',
            'left_title': 'Triệu chứng thường gặp',
            'left_items': [
                ('Chảy máu chân răng, nướu sưng đỏ', 'Dấu hiệu của viêm nướu, vôi răng tích tụ nhiều hoặc bệnh lý viêm nha chu tiến triển.'),
                ('Răng đau nhức, buốt khi ăn nóng lạnh', 'Răng bị sâu ăn vào men ngà, mòn cổ răng hoặc viêm tủy răng cần điều trị sớm.'),
                ('Răng khôn mọc lệch, sưng đau lợi trùm', 'Răng số 8 mọc ngầm, đâm ngang vào răng số 7 gây giắt thức ăn và nguy cơ tiêu xương răng kế bên.'),
                ('Hơi thở có mùi hôi dù đã đánh răng', 'Vi khuẩn tích tụ trong các ổ vôi răng dưới nướu hoặc lỗ sâu răng chưa được làm sạch.')
            ],
            'right_title': 'Cam kết từ Nha Khoa Kim Dung',
            'right_items': [
                ('100% Vô trùng khép kín', 'Mỗi khách hàng một bộ khay dụng cụ và tay khoan riêng biệt, loại bỏ nguy cơ lây nhiễm chéo.'),
                ('Trang thiết bị hiện đại', 'Máy lấy cao răng siêu âm, máy định vị chóp Dentsply, máy nhổ răng Piezotome tiên tiến.'),
                ('Bác sĩ thao tác nhẹ nhàng, tâm lý', 'Luôn lắng nghe, thấu hiểu cảm giác sợ đau của khách hàng để tạo sự thoải mái tối đa.'),
                ('Chi phí hợp lý, minh bạch', 'Báo giá chính xác trước khi làm, tuyệt đối không chèo kéo hay phát sinh thêm chi phí.')
            ]
        },
        'faq': [
            {
                'q': 'Bao lâu thì nên đi lấy cao răng một lần?',
                'a': 'Bác sĩ nha khoa khuyến cáo nên đi lấy cao răng định kỳ từ 3 đến 6 tháng một lần. Lấy cao răng định kỳ giúp loại bỏ hoàn toàn mảng bám vôi răng cứng đầu chứa hàng triệu vi khuẩn, phòng ngừa triệt để bệnh viêm nướu, tụt lợi, hôi miệng và viêm nha chu.'
            },
            {
                'q': 'Lấy cao răng bằng sóng siêu âm có làm mòn men răng không?',
                'a': 'Hoàn toàn KHÔNG. Máy lấy cao răng siêu âm hoạt động dựa trên cơ chế rung dao động của sóng siêu âm với tần số an toàn để làm vỡ vụn mảng bám vôi răng, đầu máy không hề chà xát hay gây tổn thương đến cấu trúc men răng.'
            },
            {
                'q': 'Trám răng thẩm mỹ có bền không? Dùng được bao lâu?',
                'a': 'Miếng hàn trám Composite thẩm mỹ tại Kim Dung có tuổi thọ trung bình từ 3 đến 5 năm hoặc lâu hơn tùy vào vị trí trám và chế độ ăn nhai. Nhờ công nghệ chiếu đèn quang trùng hợp và keo dán sinh học thế hệ mới, vết trám bám dính cực kỳ chắc chắn.'
            },
            {
                'q': 'Nhổ răng khôn bằng máy Piezotome có đau không?',
                'a': 'Công nghệ Piezotome sử dụng bước sóng siêu âm có chọn lọc để bóc tách dây chằng quanh chân răng mà không làm tổn thương các mô mềm và mạch máu xung quanh. Kết hợp thuốc tê chất lượng cao, quá trình nhổ răng diễn ra hoàn toàn nhẹ nhàng, ít chảy máu và giảm sưng đau tối đa.'
            },
            {
                'q': 'Răng đã lấy tủy có cần bọc sứ không?',
                'a': 'Có, rất nên bọc sứ. Răng sau khi điều trị diệt tủy sẽ mất đi nguồn cung cấp máu và dinh dưỡng, khiến thân răng trở nên giòn, xốp và rất dễ nứt vỡ khi ăn nhai đồ cứng. Bọc một mão răng sứ bên ngoài sẽ bảo vệ răng tồn tại bền vững trọn đời.'
            }
        ]
    }
}

DOCTORS = [
    {
        'name': 'Bác sĩ CKI Thùy Chi',
        'role': 'Trưởng khoa Cấy ghép Implant & Phục hình',
        'desc': 'Tốt nghiệp ĐH Y Hà Nội, hơn 12 năm kinh nghiệm cấy ghép Implant chuyên sâu và phục hình răng thẩm mỹ quốc tế.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-1755314936.png.webp'
    },
    {
        'name': 'Bác sĩ Thanh Thủy',
        'role': 'Chuyên gia Chỉnh nha & Nụ cười',
        'desc': 'Chứng chỉ Chỉnh nha Invisalign Platinum Hoa Kỳ, thực hiện thành công hơn 1.500 ca niềng răng mắc cài và máng trong suốt.',
        'img': 'https://nhakhoakimdung.vn/thumbs/500x550x1/upload/news/thiet-ke-chua-co-ten-2-1755315466.png.webp'
    },
    {
        'name': 'Bác sĩ Cố Vấn Kim Dung',
        'role': 'Cố vấn Chuyên môn Cấp cao',
        'desc': 'Hơn 20 năm cống hiến trong ngành Răng Hàm Mặt, chuyên gia xử lý các ca phục hồi toàn hàm và sai lệch khớp cắn phức tạp.',
        'img': 'https://nhakhoakimdung.vn/thumbs/400x440x1/upload/news/thiet-ke-chua-co-ten-1755314936.png.webp'
    },
    {
        'name': 'Bác sĩ Điều trị Tổng quát',
        'role': 'Chuyên khoa Nha khoa Vi phẫu & Thẩm mỹ',
        'desc': 'Tận tâm, thao tác nhẹ nhàng, giàu kinh nghiệm trong nhổ răng khôn không đau Piezotome và điều trị tủy vi phẫu.',
        'img': 'https://nhakhoakimdung.vn/thumbs/400x440x1/upload/news/thiet-ke-chua-co-ten-2-1755315466.png.webp'
    }
]

SMILE_GALLERY = [
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-1.jpg', 'Phục hồi nụ cười tự tin rạng ngời'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-2.jpg', 'Khớp cắn chuẩn, nụ cười tỏa sáng'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-3.jpg', 'Hàm răng đều đặn trắng sáng tự nhiên'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-4.jpg', 'Ăn nhai chắc khỏe trọn đời'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-5.jpg', 'Tự tin giao tiếp và thành công hơn'),
    ('https://greenfield-clinic-files.s3.ap-southeast-1.amazonaws.com/marketing/implant-gallery/smile-6.jpg', 'Thay đổi diện mạo, nâng tầm nhan sắc')
]


def generate_main_content(service_filename, data):
    hero = data['hero']
    benefits = data['benefits']
    pricing = data['pricing']
    workflow = data['workflow']
    criteria = data['criteria']
    faqs = data['faq']

    # Trust badges
    trust_html = "".join([f'<span><i class="fa-solid fa-circle-check"></i> {t}</span>' for t in hero['trust']])

    # 6 Benefits HTML
    benefits_html = ""
    for b in benefits['items']:
        benefits_html += f"""
        <div class="gf-benefit-card">
          <div class="gf-benefit-icon"><i class="{b['icon']}"></i></div>
          <h3 class="gf-benefit-title">{b['title']}</h3>
          <p class="gf-benefit-desc">{b['desc']}</p>
        </div>"""

    # 3 Pricing Tiers HTML
    pricing_html = ""
    for p in pricing['tiers']:
        popular_class = "popular" if p['popular'] else ""
        badge_html = '<div class="gf-pricing-badge">★ Khuyên Dùng</div>' if p['popular'] else ''
        features_html = "".join([f'<li><i class="fa-solid fa-check"></i> <span>{f}</span></li>' for f in p['features']])
        pricing_html += f"""
        <div class="gf-pricing-card {popular_class}">
          {badge_html}
          <div class="gf-pricing-header">
            <h3 class="gf-pricing-title">{p['name']}</h3>
            <div class="gf-pricing-subtitle">{p['sub']}</div>
            <div class="gf-pricing-amount">{p['price']}</div>
            <div class="gf-pricing-unit">{p['unit']}</div>
          </div>
          <ul class="gf-pricing-features">
            {features_html}
          </ul>
          <a href="dat-lich.html" class="gf-pricing-btn">Đăng Ký Tư Vấn Ngay</a>
        </div>"""

    # 4 Workflow Steps HTML
    workflow_html = ""
    for s in workflow['steps']:
        workflow_html += f"""
        <div class="gf-workflow-card">
          <div class="gf-workflow-num">{s['num']}</div>
          <h3 class="gf-workflow-title">{s['title']}</h3>
          <p class="gf-workflow-desc">{s['desc']}</p>
          <div class="gf-workflow-tag">{s['tag']}</div>
        </div>"""

    # Criteria HTML
    left_items_html = "".join([f"""
      <li class="gf-criteria-item">
        <div class="gf-criteria-icon"><i class="fa-solid fa-check"></i></div>
        <div>
          <strong>{item[0]}</strong>
          <p>{item[1]}</p>
        </div>
      </li>""" for item in criteria['left_items']])

    right_items_html = "".join([f"""
      <li class="gf-criteria-item">
        <div class="gf-criteria-icon"><i class="fa-solid fa-shield-halved"></i></div>
        <div>
          <strong>{item[0]}</strong>
          <p>{item[1]}</p>
        </div>
      </li>""" for item in criteria['right_items']])

    # Smile Gallery HTML
    gallery_html = ""
    for g in SMILE_GALLERY:
        gallery_html += f"""
        <div class="gf-gallery-item">
          <img src="{g[0]}" alt="{g[1]}" loading="lazy">
          <div class="gf-gallery-overlay">
            <div class="gf-gallery-caption">{g[1]}</div>
          </div>
        </div>"""

    # Doctors HTML
    doctors_html = ""
    for d in DOCTORS:
        doctors_html += f"""
        <div class="gf-doctor-card">
          <div class="gf-doctor-img">
            <img src="{d['img']}" alt="{d['name']}" loading="lazy">
          </div>
          <div class="gf-doctor-body">
            <h3 class="gf-doctor-name">{d['name']}</h3>
            <div class="gf-doctor-role">{d['role']}</div>
            <p class="gf-doctor-desc">{d['desc']}</p>
            <a href="dat-lich.html" class="gf-btn-outline" style="padding: 10px; font-size: 0.85rem; text-align: center;">Đặt hẹn khám</a>
          </div>
        </div>"""

    # FAQ HTML
    faq_html = ""
    for idx, f in enumerate(faqs):
        active = "active" if idx == 0 else ""
        faq_html += f"""
        <div class="gf-faq-item {active}">
          <div class="gf-faq-question">
            <span>{f['q']}</span>
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="gf-faq-answer">
            {f['a']}
          </div>
        </div>"""

    main_html = f"""<main id="main-content" class="gf-theme-root">
  <!-- 1. HERO SECTION -->
  <section class="gf-service-hero">
    <div class="gf-service-hero-bg">
      <img src="{hero['bg_img']}" alt="{hero['title']}">
    </div>
    <div class="gf-service-hero-overlay"></div>
    <div class="wrap-content" style="position: relative; z-index: 3; width: 100%;">
      <div class="gf-service-hero-content">
        <div class="gf-service-tagline">✦ {hero['tagline']}</div>
        <h1 class="gf-service-hero-title">{hero['title']}</h1>
        <p class="gf-service-hero-desc">{hero['desc']}</p>
        <div class="gf-service-hero-actions">
          <a href="dat-lich.html" class="gf-btn-primary"><i class="fa-solid fa-calendar-check"></i> Đặt Lịch Thăm Khám Miễn Phí</a>
          <a href="tel:0862960886" class="gf-btn-outline"><i class="fa-solid fa-phone"></i> Hotline: 0862 960 886</a>
        </div>
        <div class="gf-service-hero-trust">
          {trust_html}
        </div>
      </div>
    </div>
  </section>

  <!-- 2. LỢI ÍCH ĐIỀU TRỊ (6 BENEFITS GRID) -->
  <section class="gf-section" style="background-color: #FFFFFF;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">{benefits['tagline']}</div>
        <h2 class="gf-title-display">{benefits['title']}</h2>
        <p class="gf-desc-lead">{benefits['desc']}</p>
      </div>
      <div class="gf-benefits-grid">
        {benefits_html}
      </div>
    </div>
  </section>

  <!-- 3. BẢNG GIÁ DỊCH VỤ MINH BẠCH (3-TIER PRICING) -->
  <section class="gf-section" style="background-color: #FBF9F2;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">{pricing['tagline']}</div>
        <h2 class="gf-title-display">{pricing['title']}</h2>
        <p class="gf-desc-lead">{pricing['desc']}</p>
      </div>
      <div class="gf-pricing-grid">
        {pricing_html}
      </div>
      <p style="text-align: center; color: #71717a; font-size: 0.88rem; margin-top: 32px; font-style: italic;">
        * Chi phí chính xác và phác đồ chi tiết sẽ được bác sĩ chuyên khoa tư vấn trực tiếp sau khi chụp phim thăm khám miễn phí.
      </p>
    </div>
  </section>

  <!-- 4. QUY TRÌNH ĐIỀU TRỊ CHUẨN Y KHOA (4 STEPS) -->
  <section class="gf-section" style="background-color: #FFFFFF;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">{workflow['tagline']}</div>
        <h2 class="gf-title-display">{workflow['title']}</h2>
        <p class="gf-desc-lead">{workflow['desc']}</p>
      </div>
      <div class="gf-workflow-grid">
        {workflow_html}
      </div>
    </div>
  </section>

  <!-- 5. AI PHÙ HỢP? (CANDIDATE CRITERIA) -->
  <section class="gf-section" style="background-color: #FBF9F2;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">{criteria['tagline']}</div>
        <h2 class="gf-title-display">{criteria['title']}</h2>
      </div>
      <div class="gf-criteria-grid">
        <div class="gf-criteria-card">
          <h3 class="gf-criteria-title"><i class="fa-solid fa-clipboard-check" style="color: #EABF0E;"></i> {criteria['left_title']}</h3>
          <ul class="gf-criteria-list">
            {left_items_html}
          </ul>
        </div>
        <div class="gf-criteria-card">
          <h3 class="gf-criteria-title"><i class="fa-solid fa-user-shield" style="color: #EABF0E;"></i> {criteria['right_title']}</h3>
          <ul class="gf-criteria-list">
            {right_items_html}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. THƯ VIỆN NỤ CƯỜI THỰC TẾ -->
  <section class="gf-section" style="background-color: #FFFFFF;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">KẾT QUẢ THỰC TẾ</div>
        <h2 class="gf-title-display">Thư Viện Nụ Cười Khách Hàng</h2>
        <p class="gf-desc-lead">Hình ảnh khách hàng thực tế sau khi điều trị tại Nha Khoa Kim Dung</p>
      </div>
      <div class="gf-gallery-grid">
        {gallery_html}
      </div>
    </div>
  </section>

  <!-- 7. ĐỘI NGŨ BÁC SĨ CHUYÊN GIA -->
  <section class="gf-section" style="background-color: #FBF9F2;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">ĐỘI NGŨ Y KHOA</div>
        <h2 class="gf-title-display">Bác Sĩ Chuyên Khoa Phụ Trách</h2>
        <p class="gf-desc-lead">Đội ngũ bác sĩ tu nghiệp chuyên sâu trong và ngoài nước, luôn tận tâm đồng hành</p>
      </div>
      <div class="gf-doctors-grid">
        {doctors_html}
      </div>
    </div>
  </section>

  <!-- 8. CÂU HỎI THƯỜNG GẶP (FAQ ACCORDION) -->
  <section class="gf-section" style="background-color: #FFFFFF;">
    <div class="wrap-content">
      <div class="gf-header-center">
        <div class="gf-tagline">GIẢI ĐÁP Y KHOA</div>
        <h2 class="gf-title-display">Câu Hỏi Thường Gặp</h2>
        <p class="gf-desc-lead">Những thắc mắc phổ biến của bệnh nhân trước khi tiến hành điều trị</p>
      </div>
      <div class="gf-faq-list">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- 9. CTA BANNER ĐẶT LỊCH HẸN -->
  <section class="gf-section" style="background-color: #18181b; color: #FFFFFF;">
    <div class="wrap-content">
      <div class="gf-cta-box" style="background: #27272a !important; border-color: rgba(234, 191, 14, 0.4) !important;">
        <div class="gf-pill-label">✦ ĐẶT LỊCH HẸN HÔM NAY</div>
        <h3 style="color: #FFFFFF !important;">Sẵn Sàng Lấy Lại Nụ Cười Tự Tin Rạng Rỡ?</h3>
        <p style="color: rgba(255, 255, 255, 0.8) !important;">
          Đặt lịch ngay hôm nay để nhận miễn phí gói khám tổng quát & chụp phim CT Cone Beam 3D trị giá 500.000đ.
        </p>
        <div class="gf-cta-meta" style="color: rgba(255, 255, 255, 0.7) !important;">
          <span><i class="fa-solid fa-clock" style="color: #EABF0E;"></i> 08:00 - 19:30 (Cả T7 & CN)</span>
          <span><i class="fa-solid fa-map-pin" style="color: #EABF0E;"></i> Số 15 Bắc Sơn, P. Quang Trung, TP. Thái Nguyên</span>
        </div>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
          <a href="dat-lich.html" class="gf-btn-primary" style="font-size: 1rem;"><i class="fa-solid fa-calendar-check"></i> Đặt Lịch Khám Miễn Phí</a>
          <a href="tel:0862960886" class="gf-btn-outline-gold" style="font-size: 1rem;"><i class="fa-solid fa-phone"></i> Gọi 0862 960 886</a>
        </div>
      </div>
    </div>
  </section>
</main>"""
    return main_html


def build_page(target_filename, data, template_html):
    # Split template into pre-main and post-main
    main_start = template_html.find('<main id="main-content">')
    if main_start == -1:
        main_start = template_html.find('<main')
    main_end = template_html.find('</main>') + len('</main>')

    pre_main = template_html[:main_start]
    post_main = template_html[main_end:]

    # Update title and meta description
    pre_main = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', pre_main, count=1)
    pre_main = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["meta_desc"]}">', pre_main, count=1)

    # Ensure greenfield-theme.css is linked
    if 'greenfield-theme.css' not in pre_main:
        pre_main = pre_main.replace(
            '<link href="assets/css/ui-ux-pro-max.css?v=3.0" rel="stylesheet">',
            '<link href="assets/css/ui-ux-pro-max.css?v=3.0" rel="stylesheet">\n    <link href="assets/css/greenfield-theme.css?v=3.0" rel="stylesheet">'
        )

    # Inject Tailwind Play CDN with preflight: false to power all Greenfield utility classes safely
    if 'cdn.tailwindcss.com' not in pre_main:
        tailwind_script = """    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        corePlugins: {
          preflight: false,
        }
      }
    </script>\n"""
        pre_main = pre_main.replace('</head>', f'{tailwind_script}</head>')

    # Generate new main section using Greenfield Dental exact HTML DOM structure
    from generate_greenfield_services import build_greenfield_main
    new_main = build_greenfield_main(target_filename, data)

    full_html = pre_main + new_main + post_main
    target_path = os.path.join(WEBSITE_DIR, target_filename)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"[OK] Generated {target_filename} ({len(full_html)} bytes)")


def main():
    # Read template from trong-rang-implant.html
    template_path = os.path.join(WEBSITE_DIR, 'trong-rang-implant.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    for filename, data in SERVICES.items():
        build_page(filename, data, template_html)

    print("\n[SUCCESS] All 6 Greenfield-style service detail pages generated successfully!")


if __name__ == '__main__':
    main()
