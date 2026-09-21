/**
 * Nha Khoa Kim Dung - UI/UX Pro Max Dynamic Controller
 * Features: Frosted Glass Sticky Header, Floating Action Dock,
 * Smart Appointment Booking Modal, Toast Notifications, Smooth Interactions
 */

(function () {
  'use strict';

  // 1. Toast Notification System
  function showToast(message, type = 'success') {
    let container = document.getElementById('uupm-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'uupm-toast-container';
      container.className = 'uupm-toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `uupm-toast toast-${type}`;
    const icon = type === 'success' ? '✓' : 'ℹ';
    toast.innerHTML = `
      <span style="font-weight: 800; font-size: 16px; color: ${type === 'success' ? '#10B981' : '#EABF0E'};">${icon}</span>
      <div style="font-size: 14px; font-weight: 500; line-height: 1.4;">${message}</div>
    `;

    container.appendChild(toast);
    requestAnimationFrame(() => {
      toast.classList.add('show');
    });

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 4500);
  }

  // 2. Sticky Header Shadow on Scroll
  function initHeaderScroll() {
    const header = document.querySelector('.header') || document.querySelector('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        header.classList.add('uupm-scrolled');
      } else {
        header.classList.remove('uupm-scrolled');
      }
    }, { passive: true });
  }

  // 3. Inject Floating Quick Action Dock
  function initFloatingDock() {
    if (document.getElementById('uupm-floating-dock')) return;

    // Hide old hotline, social widgets, and legacy duplicate scroll-to-top buttons
    const oldHotline = document.querySelector('#hotline');
    if (oldHotline) oldHotline.style.display = 'none';
    const oldSocial = document.querySelector('#social');
    if (oldSocial) oldSocial.style.display = 'none';

    // Neutralize legacy NN_FRAMEWORK.GoTop to prevent duplicate injection
    if (window.NN_FRAMEWORK) {
      window.NN_FRAMEWORK.GoTop = function () {};
    }

    const removeLegacyScrollToTop = () => {
      document.querySelectorAll('.scrollToTop, .scrollToTopMobile, .BackToTop_backToTopContainer__cIh7P').forEach(el => el.remove());
    };
    removeLegacyScrollToTop();
    window.addEventListener('scroll', removeLegacyScrollToTop, { passive: true });

    const dock = document.createElement('div');
    dock.id = 'uupm-floating-dock';
    dock.className = 'uupm-floating-dock';
    dock.innerHTML = `
      <a href="tel:0862960886" class="uupm-dock-btn btn-call" title="Gọi Hotline 24/7" aria-label="Gọi hotline">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        <span class="dock-label">0862 960 886</span>
      </a>
      <a href="http://zalo.me/0862960886" target="_blank" rel="noopener noreferrer" class="uupm-dock-btn btn-zalo" title="Chat qua Zalo" aria-label="Chat Zalo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.03 2 11c0 2.87 1.5 5.43 3.84 7.04L5 22l4.24-1.41C10.15 20.84 11.06 21 12 21c5.52 0 10-4.03 10-9s-4.48-9-10-9z"/></svg>
        <span class="dock-label">Chat Zalo</span>
      </a>
      <a href="dat-lich.html" class="uupm-dock-btn btn-book" id="uupm-open-booking" title="Đặt Lịch Khám Ngay" aria-label="Đặt lịch khám">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        <span class="dock-label">Đặt Lịch Hẹn</span>
      </a>
      <button type="button" class="uupm-dock-btn btn-top" id="uupm-btn-top" title="Lên đầu trang" aria-label="Lên đầu trang">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
    `;
    document.body.appendChild(dock);

    // Scroll to Top behavior & Mobile Smart Auto-Hide
    const btnTop = document.getElementById('uupm-btn-top');
    if (btnTop) {
      btnTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    let lastScrollY = window.scrollY;
    const scrollThreshold = 8;
    let isTicking = false;

    window.addEventListener('scroll', () => {
      if (!isTicking) {
        window.requestAnimationFrame(() => {
          const currentScrollY = window.scrollY;
          const diff = currentScrollY - lastScrollY;

          // Back to top visibility
          if (btnTop) {
            if (currentScrollY > 300) {
              btnTop.classList.add('visible');
            } else {
              btnTop.classList.remove('visible');
            }
          }

          // Mobile Smart Auto-Hide: Hide dock on scroll down, show on scroll up
          if (window.innerWidth <= 768) {
            const isNearBottom = (window.innerHeight + currentScrollY) >= (document.documentElement.scrollHeight - 60);

            if (isNearBottom || currentScrollY < 60) {
              // At very top or near page bottom -> Always show dock
              dock.classList.remove('uupm-dock-hidden');
              if (btnTop) btnTop.classList.remove('uupm-dock-hidden');
            } else if (diff > scrollThreshold && currentScrollY > 80) {
              // Scrolling down -> Hide dock smoothly
              dock.classList.add('uupm-dock-hidden');
              if (btnTop) btnTop.classList.add('uupm-dock-hidden');
            } else if (diff < -scrollThreshold) {
              // Scrolling up -> Show dock immediately
              dock.classList.remove('uupm-dock-hidden');
              if (btnTop) btnTop.classList.remove('uupm-dock-hidden');
            }
          } else {
            dock.classList.remove('uupm-dock-hidden');
            if (btnTop) btnTop.classList.remove('uupm-dock-hidden');
          }

          lastScrollY = currentScrollY;
          isTicking = false;
        });
        isTicking = true;
      }
    }, { passive: true });
  }

  // 4. Smart Appointment Booking Modal
  function initBookingModal() {
    if (document.getElementById('uupm-booking-modal')) return;

    const modalOverlay = document.createElement('div');
    modalOverlay.id = 'uupm-booking-modal';
    modalOverlay.className = 'uupm-modal-overlay';
    modalOverlay.innerHTML = `
      <div class="uupm-modal" role="dialog" aria-labelledby="modal-title" aria-modal="true">
        <div class="uupm-modal-header">
          <h3 id="modal-title">Đặt Lịch Khám & Tư Vấn</h3>
          <p>Bác sĩ chuyên khoa Nha Khoa Kim Dung tư vấn miễn phí</p>
          <button type="button" class="uupm-modal-close" id="uupm-modal-close" aria-label="Đóng">&times;</button>
        </div>
        <div class="uupm-modal-body">
          <form id="uupm-appointment-form">
            <div class="uupm-form-group">
              <label for="uupm-name">Họ và tên *</label>
              <input type="text" id="uupm-name" name="name" placeholder="Ví dụ: Nguyễn Văn A" required>
            </div>
            <div class="uupm-form-group">
              <label for="uupm-phone">Số điện thoại liên hệ *</label>
              <input type="tel" id="uupm-phone" name="phone" placeholder="Ví dụ: 0912 345 678" required pattern="[0-9\\s\\-\\.\\+]{9,15}">
            </div>
            <div class="uupm-form-group">
              <label for="uupm-service">Dịch vụ quan tâm</label>
              <select id="uupm-service" name="service">
                <option value="Trồng răng Implant">Trồng răng Implant chuẩn Hàn/Mỹ</option>
                <option value="Niềng răng thẩm mỹ">Niềng răng thẩm mỹ (Mắc cài / Khay trong suốt)</option>
                <option value="Bọc răng sứ">Bọc răng sứ / Dán sứ Veneer cao cấp</option>
                <option value="Nhổ răng khôn Piezotome">Nhổ răng khôn công nghệ siêu âm Piezotome</option>
                <option value="Tẩy trắng răng">Tẩy trắng răng Laser Whitening</option>
                <option value="Khám tổng quát & Cạo vôi">Khám tổng quát & Cạo vôi răng</option>
                <option value="Nha khoa trẻ em">Nha khoa trẻ em không đau</option>
                <option value="Dịch vụ khác">Dịch vụ khác / Khám tư vấn chung</option>
              </select>
            </div>
            <div class="uupm-form-group">
              <label for="uupm-date">Thời gian mong muốn khám</label>
              <input type="date" id="uupm-date" name="date">
            </div>
            <div class="uupm-form-group">
              <label for="uupm-note">Mô tả tình trạng răng (nếu có)</label>
              <textarea id="uupm-note" name="note" rows="2" placeholder="Ví dụ: Răng đau nhức, muốn tư vấn bọc sứ..."></textarea>
            </div>
            <button type="submit" class="uupm-btn uupm-btn-primary" style="width: 100%; margin-top: 8px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13"></path><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
              Xác Nhận Đặt Hẹn Ngay
            </button>
          </form>
        </div>
      </div>
    `;
    document.body.appendChild(modalOverlay);

    // Set default date to tomorrow
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const dateInput = document.getElementById('uupm-date');
    if (dateInput) {
      dateInput.value = tomorrow.toISOString().split('T')[0];
      dateInput.min = new Date().toISOString().split('T')[0];
    }

    // Modal open/close handlers
    const openModal = () => {
      modalOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
      setTimeout(() => document.getElementById('uupm-name')?.focus(), 100);
    };

    const closeModal = () => {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    };

    document.getElementById('uupm-modal-close')?.addEventListener('click', closeModal);

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
        closeModal();
      }
    });

    // If on dat-lich.html, make the floating dock booking button scroll to the form smoothly
    const bookDockBtn = document.getElementById('uupm-open-booking');
    if (bookDockBtn && window.location.pathname.includes('dat-lich')) {
      bookDockBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const formCard = document.querySelector('.gf-booking-card') || document.getElementById('gf-main-booking-form');
        if (formCard) formCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    }

    // Modal popup is explicitly triggered by elements with data-open-modal="booking"
    document.querySelectorAll('[data-open-modal="booking"]').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
      });
    });

    // Form Submission
    const form = document.getElementById('uupm-appointment-form');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const name = document.getElementById('uupm-name').value.trim();
      const phone = document.getElementById('uupm-phone').value.trim();
      const service = document.getElementById('uupm-service').value;

      if (!name || !phone) {
        showToast('Vui lòng điền đầy đủ Họ tên và Số điện thoại', 'info');
        return;
      }

      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Đang xử lý đặt hẹn...';

      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Xác Nhận Đặt Hẹn Ngay';
        closeModal();
        form.reset();
        showToast(`🎉 Cảm ơn ${name}! Nha Khoa Kim Dung đã ghi nhận lịch hẹn [${service}]. Bác sĩ sẽ gọi tới ${phone} trong ít phút để xác nhận.`);
      }, 700);
    });
  }

  // 5. Active Tab Dynamic Highlighter
  function initActiveNavigation() {
    let currentPath = window.location.pathname;
    let currentFile = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';
    if (!currentFile || currentFile === '/') currentFile = 'index.html';

    const links = document.querySelectorAll('.menu ul.ulmn > li > a, .menu-mobile ul > li > a');
    if (!links.length) return;

    // First remove active from all
    links.forEach(l => l.classList.remove('active'));

    let matched = false;

    // Exact match
    links.forEach(l => {
      const href = l.getAttribute('href');
      if (href && href === currentFile) {
        l.classList.add('active');
        matched = true;
      }
    });

    // Semantic category matching for subpages
    if (!matched) {
      links.forEach(l => {
        const href = l.getAttribute('href') || '';
        if (href.includes('bang-gia.html') && currentFile.includes('bang-gia')) {
          l.classList.add('active');
          matched = true;
        } else if ((href.includes('dich-vu') || l.textContent.includes('Dịch vụ')) && (
          currentFile.includes('implant') || currentFile.includes('rang-su') ||
          currentFile.includes('nieng-rang') || currentFile.includes('nho-rang') ||
          currentFile.includes('cao-rang') || currentFile.includes('tay-trang') ||
          currentFile.includes('tram-rang') || currentFile.includes('tong-quat') ||
          currentFile.includes('ham-thao-lap') || currentFile.includes('tre-em')
        )) {
          l.classList.add('active');
          const pRow = l.closest('.flex.items-center.justify-between');
          if (pRow) pRow.classList.add('active');
          matched = true;
        } else if (href.includes('doi-ngu.html') && (currentFile.includes('doi-ngu') || currentFile.includes('bac-si'))) {
          l.classList.add('active');
          matched = true;
        } else if (href.includes('tin-tuc.html') && (
          currentFile.includes('tin-tuc') || currentFile.includes('kien-thuc') ||
          currentFile.includes('bien-chung') || currentFile.includes('nguyen-nhan') ||
          currentFile.includes('ly-do') || currentFile.includes('vi-sao')
        )) {
          l.classList.add('active');
          matched = true;
        } else if (href.includes('lien-he.html') && currentFile.includes('lien-he')) {
          l.classList.add('active');
          matched = true;
        } else if (href.includes('dat-lich.html') && currentFile.includes('dat-lich')) {
          l.classList.add('active');
          matched = true;
        } else if (href.includes('gioi-thieu.html') && currentFile.includes('gioi-thieu')) {
          l.classList.add('active');
          matched = true;
        }
      });
    }

    // Default to index.html if still not matched and on home
    if (!matched && (currentFile === 'index.html' || currentFile === '')) {
      links.forEach(l => {
        const href = l.getAttribute('href') || '';
        if (href === 'index.html' || href === './' || href === '/') {
          l.classList.add('active');
        }
      });
    }
  }

  // 6. Bulletproof Search & Arrow Icons (Native SVG)
  function initSearchAndArrowIcons() {
    // Search icon in header & mobile search
    const searchBtns = document.querySelectorAll('.search label, .search-menu p');
    searchBtns.forEach(btn => {
      btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>';
    });

    // Angle right icon in mobile menu
    const menuCollapses = document.querySelectorAll('.menu-mobile .scroll');
    menuCollapses.forEach(el => {
      if (!el.querySelector('svg')) {
        el.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; margin:auto;"><polyline points="9 18 15 12 9 6"></polyline></svg>';
      }
    });
  }

  // 7. DOM Initialization
  // 7. Unified Button Ripple & Tactile Feedback Controller
  function initUnifiedButtons() {
    // Dynamic Touch/Click Ripple Effect
    document.addEventListener('pointerdown', (e) => {
      const btn = e.target.closest(
        '.uupm-btn, .view-button, .more button, ' +
        'input[type="submit"], input[type="reset"], .btn-primary, .btn-secondary, ' +
        '.uupm-dock-btn, .uupm-modal-submit, .search label, .-prev-blog, .-next-blog, .accordion-button, .uupm-mobile-toggle'
      );
      if (!btn || btn.disabled) return;

      btn.classList.add('uupm-btn-pressed');

      // Native Ripple Animation (for non-input elements)
      if (btn.tagName !== 'INPUT' && !btn.classList.contains('accordion-button')) {
        const rect = btn.getBoundingClientRect();
        const ripple = document.createElement('span');
        ripple.className = 'uupm-ripple';
        const size = Math.max(rect.width, rect.height) * 1.5;
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${e.clientX - rect.left - size / 2}px`;
        ripple.style.top = `${e.clientY - rect.top - size / 2}px`;
        btn.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
      }
    });

    const clearPressed = () => {
      document.querySelectorAll('.uupm-btn-pressed').forEach(el => el.classList.remove('uupm-btn-pressed'));
    };
    document.addEventListener('pointerup', clearPressed);
    document.addEventListener('pointercancel', clearPressed);

    // Form feedback on submission
    document.querySelectorAll('form').forEach(form => {
      if (form.id === 'uupm-appointment-form') return; // Handled by modal
      form.addEventListener('submit', (e) => {
        const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');
        if (submitBtn) {
          const originalVal = submitBtn.value || submitBtn.textContent;
          if (submitBtn.tagName === 'INPUT') {
            submitBtn.value = 'Đang gửi...';
          } else {
            submitBtn.textContent = 'Đang gửi...';
          }
          setTimeout(() => {
            if (submitBtn.tagName === 'INPUT') {
              submitBtn.value = originalVal;
            } else {
              submitBtn.textContent = originalVal;
            }
          }, 3000);
        }
      });
    });

    // Mobile Hamburger Menu Toggle Controller
    initMobileMenuToggle();
  }

  // 8. Mobile Menu Controller
  function initMobileMenuToggle() {
    const mobileMenu = document.getElementById('menu-mobile');
    if (!mobileMenu) return;

    // Move menu-mobile to document.body to avoid CSS stacking context clipping from header
    if (mobileMenu.parentElement !== document.body) {
      document.body.appendChild(mobileMenu);
    }

    // Inject hamburger toggle button into header if not present
    let toggleBtn = document.getElementById('uupm-mobile-toggle');
    if (!toggleBtn) {
      toggleBtn = document.createElement('button');
      toggleBtn.id = 'uupm-mobile-toggle';
      toggleBtn.className = 'uupm-mobile-toggle';
      toggleBtn.type = 'button';
      toggleBtn.setAttribute('aria-label', 'Mở menu điều hướng');
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.innerHTML = `
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
      `;

      // Insert into .logo-banner or .head-bottom .wrap-content or header
      const targetContainer = document.querySelector('.logo-banner') || 
                              document.querySelector('.head-bottom .wrap-content') ||
                              document.querySelector('header');
      if (targetContainer) {
        targetContainer.appendChild(toggleBtn);
      }
    }

    // Ensure Backdrop element exists
    let backdrop = document.getElementById('uupm-menu-backdrop');
    if (!backdrop) {
      backdrop = document.createElement('div');
      backdrop.id = 'uupm-menu-backdrop';
      backdrop.className = 'uupm-menu-backdrop';
      document.body.appendChild(backdrop);
    }

    const openMobileMenu = () => {
      mobileMenu.classList.add('show');
      mobileMenu.style.visibility = 'visible';
      mobileMenu.style.transform = 'translateX(0)';
      backdrop.classList.add('show');
      toggleBtn.classList.add('is-active');
      toggleBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      document.documentElement.style.overflow = 'hidden';
    };

    const closeMobileMenu = () => {
      mobileMenu.classList.remove('show');
      mobileMenu.style.transform = '';
      backdrop.classList.remove('show');
      toggleBtn.classList.remove('is-active');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
      setTimeout(() => {
        if (!mobileMenu.classList.contains('show')) {
          mobileMenu.style.visibility = 'hidden';
        }
      }, 350);
    };

    // Toggle button click & touch
    toggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (mobileMenu.classList.contains('show')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });

    // Backdrop click
    backdrop.addEventListener('click', (e) => {
      e.preventDefault();
      closeMobileMenu();
    });

    // Close button click
    const closeBtns = mobileMenu.querySelectorAll('.btn-close-menu, [data-bs-dismiss="offcanvas"]');
    closeBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        closeMobileMenu();
      });
    });

    // Submenu accordion toggle for "Dịch vụ" (tapping "Dịch vụ" or arrow opens dropdown)
    const serviceItems = mobileMenu.querySelectorAll('nav.menu-mobile > ul > li');
    serviceItems.forEach(li => {
      const subMenu = li.querySelector('.dropdown-service-mobile, #menu-product');
      if (!subMenu) return;

      const toggleScroll = li.querySelector('.scroll, [data-bs-toggle="collapse"]');
      const serviceLink = li.querySelector(':scope > div > a, :scope > a');
      const serviceRow = li.querySelector('.flex.items-center.justify-between');

      const toggleServiceDropdown = (e) => {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        const isOpen = subMenu.classList.contains('show');
        if (isOpen) {
          subMenu.classList.remove('show');
          if (toggleScroll) toggleScroll.classList.remove('is-expanded');
          if (serviceRow) serviceRow.classList.remove('is-expanded');
        } else {
          subMenu.classList.add('show');
          if (toggleScroll) toggleScroll.classList.add('is-expanded');
          if (serviceRow) serviceRow.classList.add('is-expanded');
        }
      };

      // Tapping the full service row toggles dropdown
      if (serviceRow) {
        serviceRow.addEventListener('click', toggleServiceDropdown);
      }
      if (toggleScroll) {
        toggleScroll.addEventListener('click', toggleServiceDropdown);
      }
      if (serviceLink) {
        serviceLink.addEventListener('click', toggleServiceDropdown);
        serviceLink.setAttribute('href', 'javascript:void(0)');
      }

      // Remove "Tất cả dịch vụ" and any legacy dich-vu.html items completely
      subMenu.querySelectorAll('li').forEach(itemLi => {
        const itemA = itemLi.querySelector('a');
        if (!itemA) return;
        const h = itemA.getAttribute('href') || '';
        const txt = itemA.textContent || '';
        if (h.includes('dich-vu.html') || txt.includes('Tất cả dịch vụ')) {
          itemLi.remove();
        }
      });
    });

    // Ensure "Bảng giá" is present in mobile menu if missing
    const menuList = mobileMenu.querySelector('nav.menu-mobile > ul');
    if (menuList) {
      const hasBangGia = Array.from(menuList.querySelectorAll('a')).some(a => (a.getAttribute('href') || '').includes('bang-gia'));
      if (!hasBangGia) {
        const dichVuLi = Array.from(menuList.querySelectorAll(':scope > li')).find(li => {
          const a = li.querySelector(':scope > a, :scope > div > a');
          return a && (a.getAttribute('href') || '').includes('dich-vu');
        });
        const bangGiaLi = document.createElement('li');
        bangGiaLi.className = 'group';
        bangGiaLi.innerHTML = '<a class="transition" href="bang-gia.html" title="Bảng giá"><i class="fa-solid fa-file-invoice-dollar"></i> Bảng giá</a>';
        if (dichVuLi && dichVuLi.nextSibling) {
          menuList.insertBefore(bangGiaLi, dichVuLi.nextSibling);
        } else {
          menuList.appendChild(bangGiaLi);
        }
      }
    }

    // Close when clicking navigation links, BUT EXCLUDE the parent "Dịch vụ" toggle link!
    mobileMenu.querySelectorAll('a').forEach(a => {
      const isParentServiceToggle = a.closest('li')?.querySelector('.dropdown-service-mobile') && 
                                    !a.closest('.dropdown-service-mobile');
      if (isParentServiceToggle) {
        return; // Don't close on clicking the parent service toggle
      }
      a.addEventListener('click', () => {
        closeMobileMenu();
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('show')) {
        closeMobileMenu();
      }
    });
  }

  // 9. Dropdown Menu Controller (Greenfield Style)
  function initDropdownMenu() {
    const dropdownParents = document.querySelectorAll('.menu ul li.has-dropdown');
    dropdownParents.forEach(parent => {
      const link = parent.querySelector(':scope > a');
      const dropdown = parent.querySelector('.dropdown-menu-service');
      if (!link || !dropdown) return;

      // Handle click on touch devices and desktop: prevent 404 on deleted dich-vu.html
      link.addEventListener('click', (e) => {
        e.preventDefault();
        if (window.innerWidth <= 1024) {
          parent.classList.toggle('is-open');
        }
      });
    });

    // Safely reroute any lingering dich-vu.html links across the site to prevent 404
    document.querySelectorAll('a[href*="dich-vu.html"]').forEach(a => {
      if (a.closest('.has-dropdown') || a.closest('.menu-mobile')) {
        a.setAttribute('href', 'javascript:void(0)');
      } else {
        a.setAttribute('href', 'trong-rang-implant.html');
      }
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      dropdownParents.forEach(parent => {
        if (!parent.contains(e.target)) {
          parent.classList.remove('is-open');
        }
      });
    });
  }

  // 10. FAQ Accordion Controller (Greenfield Native & Class-based)
  function initFaqAccordion() {
    // Greenfield native button pattern
    const faqButtons = document.querySelectorAll('.faq-accordion-btn, .space-y-3 button');
    faqButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.rounded-2xl');
        if (!card) return;
        const answer = card.querySelector('.faq-accordion-content, .faq-answer');
        const icon = btn.querySelector('svg, i');
        const isExpanded = card.classList.contains('is-open');

        // Close other items in the same container
        const container = card.parentElement;
        if (container) {
          container.querySelectorAll('.rounded-2xl.is-open').forEach(sibling => {
            if (sibling !== card) {
              sibling.classList.remove('is-open');
              const sibAnswer = sibling.querySelector('.faq-accordion-content, .faq-answer');
              const sibIcon = sibling.querySelector('svg, i');
              if (sibAnswer) sibAnswer.style.display = 'none';
              if (sibIcon) sibIcon.style.transform = '';
            }
          });
        }

        const isPlus = icon && (icon.innerHTML.includes('M12 4v16') || icon.innerHTML.includes('fa-plus'));
        const rotateVal = isPlus ? 'rotate(45deg)' : 'rotate(180deg)';

        if (isExpanded) {
          card.classList.remove('is-open');
          if (answer) answer.style.display = 'none';
          if (icon) icon.style.transform = '';
        } else {
          card.classList.add('is-open');
          if (answer) answer.style.display = 'block';
          if (icon) icon.style.transform = rotateVal;
        }
      });
    });

    // Also support legacy .gf-faq-item
    const faqItems = document.querySelectorAll('.gf-faq-item');
    faqItems.forEach(item => {
      const question = item.querySelector('.gf-faq-question');
      if (!question) return;
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        const parent = item.parentElement;
        if (parent) {
          parent.querySelectorAll('.gf-faq-item.active').forEach(sibling => {
            if (sibling !== item) sibling.classList.remove('active');
          });
        }
        item.classList.toggle('active', !isActive);
      });
    });
  }

  // 12. Lightweight Video Facade (Zero-lag YouTube loader)
  function initVideoFacades() {
    const facades = document.querySelectorAll('.video-facade');
    facades.forEach(facade => {
      facade.addEventListener('click', function () {
        const vid = this.getAttribute('data-video-id');
        if (!vid) return;
        const start = this.getAttribute('data-video-start') || '0';
        const iframe = document.createElement('iframe');
        iframe.className = 'absolute inset-0 w-full h-full';
        iframe.src = `https://www.youtube.com/embed/${vid}?autoplay=1&start=${start}`;
        iframe.title = 'Video player';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;
        this.innerHTML = '';
        this.appendChild(iframe);
      });
    });
  }

  // 13. Unified Scroll Reveal Animation Engine (Synchronized across entire website)
  function initScrollRevealAnimations() {
    if (!('IntersectionObserver' in window)) return;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    document.documentElement.classList.add('has-scroll-anim');

    // Select candidate sections
    const allSections = Array.from(document.querySelectorAll('section, .gf-booking-section'));
    const sections = allSections.filter(sec => {
      if (sec.closest('header') || sec.closest('.header') || sec.closest('.menu-mobile') ||
          sec.closest('footer') || sec.closest('#uupm-booking-modal') || sec.closest('#uupm-floating-dock') ||
          sec.classList.contains('wrap-menu') || sec.id === 'menu-mobile') {
        return false;
      }
      return true;
    });

    sections.forEach(sec => {
      // 1. Tag Section Header
      const header = sec.querySelector('.gf-header-center, .anim-header, .title-main, .sec-title, div[class*="text-center mb-"]');
      if (header && !header.classList.contains('uupm-anim-header') && !header.classList.contains('anim-header')) {
        header.classList.add('uupm-anim-header');
      }

      // Check if process/steps section
      const secText = (sec.textContent || '').toLowerCase();
      const isProcessSection = sec.id === 'quy-trinh' ||
                               sec.querySelector('.visit-step-item, .timeline, [class*="timeline"]') !== null ||
                               (secText.includes('quy trình') && sec.querySelector('[data-step], .grid, .flex'));

      if (isProcessSection) {
        const steps = sec.querySelectorAll('.visit-step-item, .step-anim-item, .step-anim-card, [class*="step-card"], [data-step]');
        if (steps.length > 0) {
          steps.forEach((st, idx) => {
            if (!st.classList.contains('step-anim-item') && !st.classList.contains('step-anim-card')) {
              st.classList.add('uupm-anim-step-ltr');
            }
            st.style.setProperty('--anim-delay', `${(idx * 0.1 + 0.05).toFixed(2)}s`);
          });
        }
      }

      // 2. Tag Cards and Grids (Doctors, Services, Features, Pricing, Reasons, Reviews)
      const gridContainers = sec.querySelectorAll('.gf-services-grid, .grid, .gf-booking-grid, .row');
      gridContainers.forEach(grid => {
        if (grid.closest('#quy-trinh')) return;
        const children = Array.from(grid.children).filter(child => {
          return !child.classList.contains('uupm-anim-header') && !child.tagName.match(/^H[1-6]$/);
        });

        children.forEach((child, idx) => {
          if (!child.classList.contains('uupm-anim-card') &&
              !child.classList.contains('why-anim-card') &&
              !child.classList.contains('price-anim-card') &&
              !child.classList.contains('step-anim-card') &&
              !child.classList.contains('step-anim-item') &&
              !child.classList.contains('uupm-anim-step-ltr')) {
            child.classList.add('uupm-anim-card');
          }
          child.style.setProperty('--anim-delay', `${(Math.min(idx, 8) * 0.09 + 0.05).toFixed(2)}s`);
        });
      });

      // 3. Tag FAQ / Accordion items
      const faqItems = sec.querySelectorAll('.accordion-item, .gf-faq-item, .faq-card, .faq-anim-item');
      if (faqItems.length > 0) {
        faqItems.forEach((item, idx) => {
          if (!item.classList.contains('uupm-anim-faq') &&
              !item.classList.contains('faq-anim-item') &&
              !item.classList.contains('whatis-anim-item')) {
            item.classList.add('uupm-anim-faq');
          }
          item.style.setProperty('--anim-delay', `${(idx * 0.07 + 0.05).toFixed(2)}s`);
        });
      }

      // 4. Tag CTA blocks / Form cards
      const ctas = sec.querySelectorAll('.faq-anim-cta, .gf-booking-card');
      ctas.forEach(cta => {
        if (!cta.classList.contains('uupm-anim-cta') && !cta.classList.contains('uupm-anim-card')) {
          cta.classList.add('uupm-anim-cta');
        }
      });
    });

    // Setup IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      rootMargin: '0px 0px -40px 0px',
      threshold: 0.06
    });

    sections.forEach(sec => {
      const rect = sec.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        setTimeout(() => sec.classList.add('is-revealed'), 60);
      } else {
        observer.observe(sec);
      }
    });
  }

  // 11. Handle URL Query Parameters on Booking Page
  function initBookingParams() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const doctorParam = urlParams.get('doctor');
      const serviceParam = urlParams.get('dich-vu') || urlParams.get('service');

      const docSelect = document.getElementById('gf-doctor') || document.getElementById('bk_doctor') || document.getElementById('booking-doctor');
      if (docSelect && doctorParam) {
        const normDoc = doctorParam.trim().toLowerCase();
        for (let i = 0; i < docSelect.options.length; i++) {
          const optVal = (docSelect.options[i].value || '').trim().toLowerCase();
          const optTxt = (docSelect.options[i].text || '').trim().toLowerCase();
          if ((optVal && (optVal.includes(normDoc) || normDoc.includes(optVal))) ||
              (optTxt && (optTxt.includes(normDoc) || normDoc.includes(optTxt)))) {
            docSelect.selectedIndex = i;
            break;
          }
        }
      }

      const srvSelect = document.getElementById('gf-service') || document.getElementById('booking-service');
      if (srvSelect && serviceParam) {
        const normService = serviceParam.trim().toLowerCase();
        for (let i = 0; i < srvSelect.options.length; i++) {
          const optVal = (srvSelect.options[i].value || '').trim().toLowerCase();
          const optTxt = (srvSelect.options[i].text || '').trim().toLowerCase();
          if ((optVal && (optVal.includes(normService) || normService.includes(optVal))) ||
              (optTxt && (optTxt.includes(normService) || normService.includes(optTxt)))) {
            srvSelect.selectedIndex = i;
            srvSelect.style.borderColor = '#EABF0E';
            srvSelect.style.boxShadow = '0 0 0 3px rgba(234, 191, 14, 0.25)';
            break;
          }
        }
      }

      if (doctorParam || serviceParam) {
        setTimeout(() => {
          const formSec = document.getElementById('gf-main-booking-form') ||
                          document.querySelector('.gf-booking-card') ||
                          document.getElementById('booking-section');
          if (formSec) {
            formSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }, 400);
      }
    } catch (e) {
      console.warn('Init booking params error:', e);
    }
  }

  // 12. Header Address Click -> Google Maps
  function initHeaderAddressMap() {
    const mapsUrl = 'https://maps.app.goo.gl/uF5jZ8gQ5bZ4uL4J8';

    document.addEventListener('click', function (e) {
      const infoHead = e.target.closest('.info-head');
      if (infoHead) {
        e.preventDefault();
        window.open(mapsUrl, '_blank', 'noopener,noreferrer');
      }
    });

    document.querySelectorAll('.info-head').forEach((el) => {
      el.setAttribute('title', 'Xem vị trí Nha Khoa Kim Dung trên Google Maps');
      el.setAttribute('role', 'link');
      el.setAttribute('tabindex', '0');
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          window.open(mapsUrl, '_blank', 'noopener,noreferrer');
        }
      });
    });
  }

  // 12b. Footer Address Click -> Google Maps
  function initFooterAddressMap() {
    const mapsUrl = 'https://maps.app.goo.gl/uF5jZ8gQ5bZ4uL4J8';

    function isAddressElement(el) {
      if (!el) return false;
      const text = (el.textContent || '').trim();
      const hasIcon = el.querySelector('.fa-location-dot, img[src*="Group"]');
      const isAddrText = text.includes('Bắc Sơn') || text.includes('Bac Son') || text.includes('Địa chỉ');
      const isNotOther = !text.includes('0862') && !text.includes('Hotline') && !text.includes('Email') && !text.includes('@') && !text.includes('Giờ làm việc') && !text.includes('Working Hours');
      return (hasIcon || isAddrText) && isNotOther;
    }

    document.addEventListener('click', function (e) {
      const p = e.target.closest('.content-footer p, .gf-contact-row, .box-footer p');
      if (p && isAddressElement(p)) {
        const link = e.target.closest('a');
        if (link && (link.href.startsWith('tel:') || link.href.startsWith('mailto:'))) {
          return;
        }
        e.preventDefault();
        window.open(mapsUrl, '_blank', 'noopener,noreferrer');
      }
    });

    document.querySelectorAll('.content-footer p, .gf-contact-row, .box-footer p').forEach(el => {
      if (isAddressElement(el)) {
        el.classList.add('uupm-footer-address');
        el.setAttribute('title', 'Xem vị trí Nha Khoa Kim Dung trên Google Maps');
        el.setAttribute('role', 'link');
        el.setAttribute('tabindex', '0');
        el.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            window.open(mapsUrl, '_blank', 'noopener,noreferrer');
          }
        });
      }
    });
  }

  // 12c. Quick Price Tabs Controller (Implant, Niềng răng, Răng sứ, Nhổ răng)
  function initPriceTabs() {
    window.switchGfPriceTab = function (index, clickedBtn) {
      const idx = parseInt(index, 10);
      const btn = clickedBtn || document.querySelectorAll('.gf-calc-tabs .gf-calc-tab')[idx];
      const container = btn ? btn.closest('.gf-calc-tabs') : document.querySelector('.gf-calc-tabs');

      if (container) {
        const tabs = container.querySelectorAll('.gf-calc-tab');
        tabs.forEach((tab, i) => {
          if (tab === btn || i === idx) {
            tab.classList.add('active');
            tab.setAttribute('aria-selected', 'true');
          } else {
            tab.classList.remove('active');
            tab.setAttribute('aria-selected', 'false');
          }
        });
      }

      const card = container ? container.closest('.gf-calc-card') || container.parentElement : document;
      const panes = card.querySelectorAll('.gf-price-pane');

      panes.forEach((pane, i) => {
        const paneId = pane.id;
        const matches = (paneId && paneId === `gf-price-pane-${idx}`) || i === idx;
        if (matches) {
          pane.style.display = 'block';
          pane.classList.add('active-pane');
        } else {
          pane.style.display = 'none';
          pane.classList.remove('active-pane');
        }
      });

      if (localStorage.getItem('site_lang') === 'en' && typeof translateDomToEnglish === 'function') {
        translateDomToEnglish();
      }
    };

    document.querySelectorAll('.gf-calc-tabs .gf-calc-tab').forEach((tab, i) => {
      tab.setAttribute('role', 'tab');
      tab.setAttribute('tabindex', '0');
      tab.addEventListener('click', function (e) {
        e.preventDefault();
        window.switchGfPriceTab(i, this);
      });
      tab.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          window.switchGfPriceTab(i, this);
        }
      });
    });
  }

  // Immediate global fallback assignment
  window.switchGfPriceTab = function (index, clickedBtn) {
    const idx = parseInt(index, 10);
    const btn = clickedBtn || document.querySelectorAll('.gf-calc-tabs .gf-calc-tab')[idx];
    const container = btn ? btn.closest('.gf-calc-tabs') : document.querySelector('.gf-calc-tabs');

    if (container) {
      const tabs = container.querySelectorAll('.gf-calc-tab');
      tabs.forEach((tab, i) => {
        if (tab === btn || i === idx) {
          tab.classList.add('active');
          tab.setAttribute('aria-selected', 'true');
        } else {
          tab.classList.remove('active');
          tab.setAttribute('aria-selected', 'false');
        }
      });
    }

    const card = container ? container.closest('.gf-calc-card') || container.parentElement : document;
    const panes = card.querySelectorAll('.gf-price-pane');

    panes.forEach((pane, i) => {
      const paneId = pane.id;
      const matches = (paneId && paneId === `gf-price-pane-${idx}`) || i === idx;
      if (matches) {
        pane.style.display = 'block';
        pane.classList.add('active-pane');
      } else {
        pane.style.display = 'none';
        pane.classList.remove('active-pane');
      }
    });

    if (localStorage.getItem('site_lang') === 'en' && typeof translateDomToEnglish === 'function') {
      translateDomToEnglish();
    }
  };

  // 13. Full-Site Bilingual Language Switcher (Tiếng Việt <-> English)
  const DICT_VI_EN = [
    // Header Navigation
    { vi: 'TRANG CHỦ', en: 'HOME' },
    { vi: 'Trang chủ', en: 'Home' },
    { vi: 'GIỚI THIỆU', en: 'ABOUT US' },
    { vi: 'Giới thiệu', en: 'About Us' },
    { vi: 'DỊCH VỤ', en: 'SERVICES' },
    { vi: 'Dịch vụ', en: 'Services' },
    { vi: 'BẢNG GIÁ', en: 'PRICING' },
    { vi: 'Bảng giá', en: 'Pricing' },
    { vi: 'BÁC SĨ', en: 'DOCTORS' },
    { vi: 'Bác sĩ', en: 'Doctors' },
    { vi: 'TIN TỨC& ƯU ĐÃI', en: 'NEWS & OFFERS' },
    { vi: 'TIN TỨC & ƯU ĐÃI', en: 'NEWS & OFFERS' },
    { vi: 'Tin tức & Ưu đãi', en: 'News & Offers' },
    { vi: 'Tin tức &amp; Ưu đãi', en: 'News & Offers' },
    { vi: 'TIN TỨC', en: 'NEWS' },
    { vi: 'Tin tức', en: 'News' },
    { vi: 'LIÊN HỆ', en: 'CONTACT' },
    { vi: 'Liên hệ', en: 'Contact' },
    { vi: 'Tìm kiếm', en: 'Search' },
    { vi: 'Bạn cần tìm dịch vụ gì', en: 'What service are you looking for?' },

    // Header Gold Ribbon & Info
    { vi: 'Đặt lịch hẹn', en: 'Book Appointment' },
    { vi: 'ĐẶT LỊCH HẸN', en: 'BOOK APPOINTMENT' },
    { vi: 'Đặt lịch khám', en: 'Book Appointment' },
    { vi: 'ĐẶT LỊCH KHÁM', en: 'BOOK APPOINTMENT' },
    { vi: 'Đặt lịch', en: 'Book Appointment' },
    { vi: 'ĐẶT LỊCH', en: 'BOOK APPOINTMENT' },
    { vi: 'Hotline 24/7', en: 'Hotline 24/7' },
    { vi: 'Số 15, đường Bắc Sơn kéo dài, P. Quang Trung, TP. Thái Nguyên', en: '15 Bac Son Ext., Quang Trung, TP. Thai Nguyen' },
    { vi: 'Số 15, Đường Bắc Sơn kéo dài, P. Quang Trung, TP. Thái Nguyên', en: '15 Bac Son Ext., Quang Trung, TP. Thai Nguyen' },
    { vi: 'Nụ cười hoàn hảo- Chìa khóa thành công', en: 'Perfect Smile - Key to Success' },
    { vi: 'Nụ cười hoàn hảo - Chìa khóa thành công', en: 'Perfect Smile - Key to Success' },

    // Services Submenu
    { vi: 'Cấy ghép răng implant', en: 'Dental Implant Placement' },
    { vi: 'Răng sứ', en: 'Porcelain Teeth' },
    { vi: 'Bọc răng sứ, mặt dán sứ', en: 'Porcelain Crowns & Veneers' },
    { vi: 'Bọc răng sứ', en: 'Porcelain Crowns' },
    { vi: 'Niềng răng máng trong suốt', en: 'Clear Aligner Orthodontics' },
    { vi: 'Niềng răng mắc cài', en: 'Braces Orthodontics' },
    { vi: 'Niềng răng kim loại & sứ', en: 'Metal & Ceramic Braces' },
    { vi: 'Niềng răng kim loại &amp; sứ', en: 'Metal & Ceramic Braces' },
    { vi: 'Niềng răng thẩm mỹ', en: 'Cosmetic Orthodontics' },
    { vi: 'Tẩy trắng', en: 'Teeth Whitening' },
    { vi: 'Tẩy trắng răng an toàn', en: 'Safe Teeth Whitening' },
    { vi: 'Tẩy trắng răng', en: 'Teeth Whitening' },
    { vi: 'Nha khoa tổng quát', en: 'General Dentistry' },
    { vi: 'Khám, vệ sinh, trám răng', en: 'Exam, Cleaning & Fillings' },
    { vi: 'Hàm tháo lắp', en: 'Removable Dentures' },
    { vi: 'Điều trị tủy - Hàn trám', en: 'Root Canal & Fillings' },
    { vi: 'Lấy cao răng', en: 'Dental Scaling' },
    { vi: 'Nhổ răng khôn', en: 'Wisdom Tooth Extraction' },

    // Floating Dock
    { vi: 'Gọi hotline', en: 'Call Hotline' },
    { vi: 'Gọi Hotline 24/7', en: 'Call Hotline 24/7' },
    { vi: 'Chat qua Zalo', en: 'Chat via Zalo' },
    { vi: 'Chat Zalo', en: 'Chat Zalo' },
    { vi: 'Đặt Lịch Hẹn', en: 'Book Appointment' },
    { vi: 'Đặt Lịch Khám Ngay', en: 'Book Appointment' },
    { vi: 'Lên đầu trang', en: 'Back to Top' },

    // Booking Modal & Forms
    { vi: 'ĐẶT LỊCH KHÁM NHANH', en: 'QUICK APPOINTMENT' },
    { vi: 'Đặt Lịch Khám Trực Tuyến', en: 'Online Appointment Booking' },
    { vi: 'Đặt Lịch Khám Ngay Hôm Nay', en: 'Book Your Appointment Today' },
    { vi: 'Đặt lịch khám với bác sĩ', en: 'Book Consultation with Doctor' },
    { vi: 'Họ và tên quý khách', en: 'Your Full Name' },
    { vi: 'Họ và tên', en: 'Full Name' },
    { vi: 'Số điện thoại liên hệ', en: 'Contact Phone Number' },
    { vi: 'Số điện thoại', en: 'Phone Number' },
    { vi: 'Chọn dịch vụ nha khoa', en: 'Select Dental Service' },
    { vi: 'Chọn dịch vụ', en: 'Select Service' },
    { vi: 'Chọn bác sĩ khám', en: 'Select Doctor' },
    { vi: 'Chọn bác sĩ', en: 'Select Doctor' },
    { vi: 'Ngày mong muốn khám', en: 'Preferred Date' },
    { vi: 'Ngày khám', en: 'Appointment Date' },
    { vi: 'Ghi chú thêm tình trạng răng...', en: 'Notes on your dental condition...' },
    { vi: 'Ghi chú...', en: 'Notes...' },
    { vi: 'XÁC NHẬN ĐẶT LỊCH HẸN', en: 'CONFIRM APPOINTMENT' },
    { vi: 'Gửi thông tin đặt lịch', en: 'Submit Appointment' },
    { vi: 'ĐẶT LỊCH NGAY', en: 'BOOK NOW' },
    { vi: 'Đặt lịch ngay', en: 'Book Now' },
    { vi: 'Đang xác nhận lịch hẹn...', en: 'Confirming appointment...' },
    { vi: 'Đặt Lịch Khám Thành Công!', en: 'Appointment Booked Successfully!' },
    { vi: 'Đặt lịch hẹn khác', en: 'Book Another Appointment' },
    { vi: 'Hoặc gọi trực tiếp Hotline ưu tiên:', en: 'Or call priority hotline directly:' },
    { vi: 'Ưu đãi 15% khi đặt lịch online qua website', en: '15% discount for online booking via website' },

    // Common CTAs & Buttons
    { vi: 'Tư vấn ngay', en: 'Consult Now' },
    { vi: 'TƯ VẤN NGAY', en: 'CONSULT NOW' },
    { vi: 'Xem chi tiết', en: 'View Details' },
    { vi: 'XEM CHI TIẾT', en: 'VIEW DETAILS' },
    { vi: 'Xem thêm', en: 'Read More' },
    { vi: 'XEM THÊM', en: 'READ MORE' },
    { vi: 'Xem bảng giá chi tiết', en: 'View Detailed Price List' },
    { vi: 'Xem bảng giá', en: 'View Price List' },
    { vi: 'Đăng ký tư vấn', en: 'Request Consultation' },
    { vi: 'Gửi tin nhắn', en: 'Send Message' },
    { vi: 'Gửi thông tin', en: 'Send Information' },
    { vi: 'Đóng lại', en: 'Close' },
    { vi: 'Quay lại', en: 'Back' },

    // Table Headers & Pricing
    { vi: 'BẢNG GIÁ DỊCH VỤ NHA KHOA', en: 'DENTAL SERVICE PRICE LIST' },
    { vi: 'Bảng Giá Dịch Vụ Nha Khoa', en: 'Dental Service Price List' },
    { vi: 'Bảng Giá Nha Khoa Chi Tiết', en: 'Detailed Dental Price List' },
    { vi: 'Chi phí minh bạch - Cam kết không phát sinh', en: 'Transparent Pricing - No Hidden Costs' },
    { vi: 'STT', en: 'No.' },
    { vi: 'Đơn vị', en: 'Unit' },
    { vi: 'Chi phí (VNĐ)', en: 'Price (VND)' },
    { vi: 'Bảo hành', en: 'Warranty' },
    { vi: 'Hành động', en: 'Action' },
    { vi: 'Trọn đời', en: 'Lifetime' },
    { vi: 'Miễn phí', en: 'Free' },
    { vi: 'Răng', en: 'Tooth' },
    { vi: 'Hàm', en: 'Arch' },
    { vi: 'Gói', en: 'Package' },
    { vi: 'Liệu trình', en: 'Course' },
    { vi: 'Lần', en: 'Session' },
    { vi: '10 năm', en: '10 Years' },
    { vi: '5 năm', en: '5 Years' },
    // Quick Price Calculator Tabs & Cards
    { vi: 'Chi phí minh bạch', en: 'Transparent Pricing' },
    { vi: 'Cấy Ghép Implant', en: 'Dental Implant' },
    { vi: 'Niềng Răng Thẩm Mỹ', en: 'Cosmetic Braces' },
    { vi: 'Răng Sứ Thẩm Mỹ', en: 'Porcelain Crowns' },
    { vi: 'Nhổ Răng & Tổng Quát', en: 'Extraction & General' },
    { vi: 'Implant Dentium (Hàn Quốc)', en: 'Implant Dentium (Korea)' },
    { vi: 'Trụ + Abutment chính hãng · Bảo hành 10 năm', en: 'Genuine fixture + abutment · 10-year warranty' },
    { vi: 'Implant Straumann (Thụy Sĩ)', en: 'Implant Straumann (Switzerland)' },
    { vi: 'Tích hợp xương tức thì · Bảo hành trọn đời', en: 'Immediate osseointegration · Lifetime warranty' },
    { vi: 'Implant Neodent (Brazil)', en: 'Implant Neodent (Brazil)' },
    { vi: 'Công nghệ tập đoàn Straumann · Bảo hành 15 năm', en: 'Straumann Group technology · 15-year warranty' },
    { vi: 'Mắc Cài Kim Loại Chuẩn', en: 'Standard Metal Braces' },
    { vi: 'Hiệu quả cao, bền chắc · Trả góp từ 1tr/tháng', en: 'High efficiency, durable · Installment from 1M/mo' },
    { vi: 'Mắc Cài Sứ Tự Buộc', en: 'Self-Ligating Ceramic Braces' },
    { vi: 'Thẩm mỹ kín đáo, êm ái · Rút ngắn thời gian niềng', en: 'Discreet aesthetics · Shorter treatment time' },
    { vi: 'Khay Trong Suốt Invisalign', en: 'Invisalign Clear Aligners' },
    { vi: 'Nhập khẩu Hoa Kỳ · Tháo lắp linh hoạt, vô hình', en: 'USA imported · Removable & invisible' },
    { vi: 'Răng Sứ Titan Chuẩn', en: 'Standard Titanium Porcelain' },
    { vi: '1.500.000đ / Răng', en: '1,500,000 VND / Tooth' },
    { vi: 'Ăn nhai bền chắc · Bảo hành chính hãng 5 năm', en: 'Strong chewing force · 5-year warranty' },
    { vi: 'Toàn Sứ Cercon HT (Đức)', en: 'Cercon HT All-Ceramic (Germany)' },
    { vi: '4.500.000đ / Răng', en: '4,500,000 VND / Tooth' },
    { vi: 'Trong bóng tự nhiên · Bảo hành chính hãng 10 năm', en: 'Natural translucency · 10-year warranty' },
    { vi: 'Dán Sứ Veneer Emax', en: 'Emax Porcelain Veneer' },
    { vi: '6.500.000đ / Răng', en: '6,500,000 VND / Tooth' },
    { vi: 'Siêu mỏng 0.3mm · Không mài nhỏ răng gốc', en: 'Ultra-thin 0.3mm · Minimal tooth prep' },
    { vi: 'Lấy Cao Răng Sóng Siêu Âm', en: 'Ultrasonic Dental Scaling' },
    { vi: '150.000đ - 250.000đ', en: '150,000 - 250,000 VND' },
    { vi: 'Vệ sinh sạch mảng bám, êm ái, đánh bóng răng', en: 'Gentle plaque removal & teeth polishing' },
    { vi: 'Nhổ Răng Khôn Piezotome', en: 'Piezotome Wisdom Tooth Extraction' },
    { vi: '800.000đ - 2.500.000đ', en: '800,000 - 2,500,000 VND' },
    { vi: 'Sóng siêu âm không đau, liền nướu nhanh', en: 'Painless ultrasound, fast tissue recovery' },
    { vi: 'Hàn Trám Răng Thẩm Mỹ', en: 'Cosmetic Composite Filling' },
    { vi: '300.000đ - 500.000đ', en: '300,000 - 500,000 VND' },
    { vi: 'Composite thẩm mỹ trùng khớp màu men răng', en: 'Natural aesthetic composite enamel match' },
    { vi: 'Xem đầy đủ bảng giá chi tiết các dịch vụ', en: 'View complete detailed price list' },

    // Section Titles
    { vi: 'VÌ SAO NÊN CHỌN NHA KHOA KIM DUNG?', en: 'WHY CHOOSE KIM DUNG DENTAL?' },
    { vi: 'ĐỘI NGŨ BÁC SĨ CHUYÊN GIA', en: 'EXPERT DOCTOR TEAM' },
    { vi: 'ĐỘI NGŨ BÁC SĨ', en: 'DOCTOR TEAM' },
    { vi: 'BÁC SĨ CHUYÊN KHOA', en: 'DENTAL SPECIALISTS' },
    { vi: 'CƠ SỞ VẬT CHẤT & CÔNG NGHỆ', en: 'FACILITIES & MODERN TECHNOLOGY' },
    { vi: 'HÌNH ẢNH KHÁCH HÀNG THỰC TẾ', en: 'REAL CUSTOMER RESULTS' },
    { vi: 'HÌNH ẢNH KHÁCH HÀNG', en: 'CUSTOMER GALLERY' },
    { vi: 'CẢM NHẬN KHÁCH HÀNG', en: 'PATIENT TESTIMONIALS' },
    { vi: 'TIN TỨC & KIẾN THỨC NHA KHOA', en: 'DENTAL NEWS & INSIGHTS' },
    { vi: 'CÂU HỎI THƯỜNG GẶP (FAQ)', en: 'FREQUENTLY ASKED QUESTIONS (FAQ)' },
    { vi: 'CÂU HỎI THƯỜNG GẶP', en: 'FREQUENTLY ASKED QUESTIONS' },
    { vi: 'Hỏi & Đáp Nha Khoa', en: 'Dental Q&A' },

    // Section 2 Giới thiệu: 30 Năm - Điều Quý Giá Nhất Là Niềm Tin
    { vi: '30 NĂM', en: '30 YEARS' },
    { vi: 'ĐIỀU QUÝ GIÁ NHẤT LÀ NIỀM TIN', en: 'THE MOST PRECIOUS VALUE IS TRUST' },
    { vi: '30 năm không chỉ được tính bằng thời gian.', en: '30 years is not merely measured by time.' },
    { vi: '30 năm được tính bằng những nụ cười đã được trao đi và những niềm tin được gửi lại.', en: '30 years is measured by every smile delivered and every trust returned.' },
    { vi: 'Video khách hàng', en: 'Customer Story' },
    { vi: 'Gắn kết gia đình', en: 'Family Connection' },
    { vi: 'Đồng hành từ thanh xuân', en: 'Lifelong Companionship' },
    { vi: 'Điểm tựa y khoa thân thuộc', en: 'Familiar Dental Haven' },
    { vi: 'Tri kỷ 30 năm phát triển', en: '30-Year Cherished Journey' },
    { vi: '“Có những khách hàng giới thiệu cha mẹ, vợ/chồng, con cái.”', en: '“There are customers who introduce their parents, spouse, and children.”' },
    { vi: 'Có những khách hàng giới thiệu cha mẹ, vợ/chồng, con cái.', en: 'There are customers who introduce their parents, spouse, and children.' },
    { vi: '“Có người đến Kim Dung khi còn trẻ.”', en: '“There are those who first came to Kim Dung in their youth.”' },
    { vi: 'Có người đến Kim Dung khi còn trẻ.', en: 'There are those who first came to Kim Dung in their youth.' },
    { vi: '“Sau nhiều năm quay lại cùng gia đình.”', en: '“Returning years later together with their family.”' },
    { vi: 'Sau nhiều năm quay lại cùng gia đình.', en: 'Returning years later together with their family.' },
    { vi: '“Có những khách hàng trở thành một phần trong hành trình phát triển của phòng khám.”', en: "“There are customers who have become an enduring part of our clinic's journey.”" },
    { vi: 'Có những khách hàng trở thành một phần trong hành trình phát triển của phòng khám.', en: "There are customers who have become an enduring part of our clinic's journey." },
    { vi: 'Không có lời khẳng định nào quý giá hơn khi một người an tâm trao gửi nụ cười của đấng sinh thành, bạn đời và con cái cho cùng một đội ngũ bác sĩ suốt nhiều năm.', en: 'No affirmation is more profound than when a patient wholeheartedly entrusts the smiles and health of their parents, spouse, and children to our medical team across generations.' },
    { vi: 'Bắt đầu từ những ngày thanh xuân tìm kiếm sự tự tin cho nụ cười, để rồi qua từng cột mốc trưởng thành trong cuộc sống, Kim Dung vẫn luôn là nơi được trao trọn niềm tin.', en: "Starting from youth's journey toward a confident smile, and continuing through life's meaningful milestones, Kim Dung remains their steadfast and trusted dental destination." },
    { vi: 'Dù thời gian trôi qua hay công việc đưa đi xa, mỗi khi cần chăm sóc răng miệng, Kim Dung vẫn là điểm tựa y khoa thân thuộc mà họ an tâm dẫn cả tổ ấm cùng quay trở lại.', en: 'No matter how much time passes or where life leads, whenever dental care is needed, Kim Dung is the welcoming haven where they confidently bring their entire family back.' },
    { vi: 'Từ những ngày đầu khởi dựng cho đến diện mạo hiện đại hôm nay, sự tin yêu và đồng hành bền bỉ của quý khách chính là tài sản vô giá nâng bước Kim Dung suốt 30 năm qua.', en: "From our earliest days to our modern clinic today, our patients' steadfast trust and companionship have been the most invaluable asset guiding Kim Dung throughout our 30-year journey." },


    // Footer
    { vi: 'HỆ THỐNG NHA KHOA KIM DUNG', en: 'KIM DUNG DENTAL SYSTEM' },
    { vi: 'NHA KHOA KIM DUNG', en: 'KIM DUNG DENTAL CLINIC' },
    { vi: 'THÔNG TIN LIÊN HỆ', en: 'CONTACT INFORMATION' },
    { vi: 'DỊCH VỤ NỔI BẬT', en: 'FEATURED SERVICES' },
    { vi: 'CHÍNH SÁCH & QUY ĐỊNH', en: 'POLICIES & REGULATIONS' },
    { vi: 'KẾT NỐI VỚI CHÚNG TÔI', en: 'CONNECT WITH US' },
    { vi: 'Địa chỉ:', en: 'Address:' },
    { vi: 'Điện thoại:', en: 'Phone:' },
    { vi: 'Giờ làm việc:', en: 'Working Hours:' },
    { vi: 'Thứ 2 - Chủ Nhật: 08:00 - 19:30', en: 'Monday - Sunday: 08:00 - 19:30' },
    { vi: 'Bản quyền thuộc về Nha Khoa Kim Dung', en: 'Copyright © Kim Dung Dental Clinic. All Rights Reserved.' },
    { vi: 'Chính sách bảo mật', en: 'Privacy Policy' },
    { vi: 'Chính sách dịch vụ', en: 'Service Policy' },
    { vi: 'Chính sách thanh toán', en: 'Payment Policy' }
  ];

  function translateDomToEnglish() {
    const walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          const tag = parent.tagName.toLowerCase();
          if (['script', 'style', 'noscript', 'textarea', 'code', 'pre'].includes(tag)) {
            return NodeFilter.FILTER_REJECT;
          }
          if (parent.closest('.header-lang-badge') || parent.closest('.uupm-lang-dropdown') || parent.closest('.uupm-mobile-lang-switch')) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const nodes = [];
    let curr;
    while ((curr = walker.nextNode())) {
      nodes.push(curr);
    }

    nodes.forEach(node => {
      const text = node.nodeValue;
      const trimmed = text.trim();
      if (node.__origVi === undefined) {
        node.__origVi = text;
      }

      // Exact match first
      for (let i = 0; i < DICT_VI_EN.length; i++) {
        const item = DICT_VI_EN[i];
        if (trimmed === item.vi) {
          node.nodeValue = text.replace(item.vi, item.en);
          return;
        }
      }

      // Phrase replacement
      let updated = text;
      let changed = false;
      for (let i = 0; i < DICT_VI_EN.length; i++) {
        const item = DICT_VI_EN[i];
        if (item.vi.length > 3 && updated.includes(item.vi)) {
          updated = updated.split(item.vi).join(item.en);
          changed = true;
        }
      }
      if (changed) {
        node.nodeValue = updated;
      }
    });

    // Attributes (placeholder, title, aria-label)
    document.querySelectorAll('[placeholder], [title], [aria-label]').forEach(el => {
      if (el.closest('.uupm-lang-dropdown') || el.closest('.uupm-mobile-lang-switch')) return;
      ['placeholder', 'title', 'aria-label'].forEach(attr => {
        const val = el.getAttribute(attr);
        if (!val) return;
        const key = `__origVi_${attr}`;
        if (el[key] === undefined) {
          el[key] = val;
        }
        for (let i = 0; i < DICT_VI_EN.length; i++) {
          const item = DICT_VI_EN[i];
          if (val.trim() === item.vi) {
            el.setAttribute(attr, item.en);
            break;
          }
        }
      });
    });
  }

  function restoreDomToVietnamese() {
    const walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          return node.__origVi !== undefined ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
        }
      }
    );
    const nodes = [];
    let curr;
    while ((curr = walker.nextNode())) {
      nodes.push(curr);
    }
    nodes.forEach(node => {
      if (node.__origVi !== undefined) {
        node.nodeValue = node.__origVi;
      }
    });

    document.querySelectorAll('[placeholder], [title], [aria-label]').forEach(el => {
      ['placeholder', 'title', 'aria-label'].forEach(attr => {
        const key = `__origVi_${attr}`;
        if (el[key] !== undefined) {
          el.setAttribute(attr, el[key]);
        }
      });
    });
  }

  function initGoogleTranslateScript() {
    if (window.googleTranslateLoaded) return;
    window.googleTranslateLoaded = true;

    if (!document.getElementById('google_translate_element')) {
      const div = document.createElement('div');
      div.id = 'google_translate_element';
      div.style.cssText = 'position:absolute;top:-9999px;left:-9999px;visibility:hidden;width:0;height:0;';
      document.body.appendChild(div);
    }

    window.googleTranslateElementInit = function () {
      try {
        new window.google.translate.TranslateElement({
          pageLanguage: 'vi',
          includedLanguages: 'vi,en',
          autoDisplay: false
        }, 'google_translate_element');
      } catch (err) {
        console.warn('Google Translate Init:', err);
      }
    };

    const script = document.createElement('script');
    script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    script.async = true;
    script.onerror = function () {
      console.warn('Google Translate script offline - relying on instant UI dictionary.');
    };
    document.head.appendChild(script);
  }

  function triggerGoogleTranslate(lang) {
    const host = window.location.hostname;
    document.cookie = `googtrans=/vi/${lang}; path=/;`;
    if (host) {
      document.cookie = `googtrans=/vi/${lang}; domain=${host}; path=/;`;
    }

    const combo = document.querySelector('.goog-te-combo');
    if (combo) {
      if (combo.value !== lang) {
        combo.value = lang;
        combo.dispatchEvent(new Event('change'));
      }
    }
  }

  function applyLanguage(lang) {
    const isEn = lang === 'en';

    // 1. Update all badges on page
    document.querySelectorAll('.header-lang-badge').forEach(badge => {
      const img = badge.querySelector('img.lang-flag') || badge.querySelector('img');
      const span = badge.querySelector('span');
      if (isEn) {
        if (img) {
          img.src = 'https://flagcdn.com/24x18/gb.png';
          img.alt = 'EN';
        }
        if (span) {
          span.innerHTML = 'EN <i class="fa-solid fa-chevron-down"></i>';
        }
      } else {
        if (img) {
          img.src = 'https://flagcdn.com/24x18/vn.png';
          img.alt = 'VN';
        }
        if (span) {
          span.innerHTML = 'VI <i class="fa-solid fa-chevron-down"></i>';
        }
      }
    });

    // 2. Update active option in dropdowns and mobile switches
    document.querySelectorAll('.uupm-lang-option').forEach(opt => {
      const optLang = opt.getAttribute('data-lang');
      if (optLang === lang) {
        opt.classList.add('active');
      } else {
        opt.classList.remove('active');
      }
    });

    // 3. Apply DOM translation
    if (isEn) {
      document.body.classList.add('site-lang-en');
      translateDomToEnglish();
    } else {
      document.body.classList.remove('site-lang-en');
      if (document.querySelector('html.translated-ltr') || document.querySelector('font')) {
        localStorage.setItem('site_lang', 'vi');
        document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        const host = location.hostname;
        if (host) {
          document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=" + host + "; path=/;";
        }
        document.cookie = "googtrans=/vi/vi; path=/;";
        window.location.reload();
        return;
      }
      restoreDomToVietnamese();
    }

    // 4. Trigger Google Translate for deep paragraphs
    triggerGoogleTranslate(lang);

    // 5. Save preference
    localStorage.setItem('site_lang', lang);
  }

  function closeAllLangDropdowns() {
    document.querySelectorAll('.header-lang-badge').forEach(b => b.classList.remove('uupm-lang-open'));
    document.querySelectorAll('.uupm-lang-dropdown').forEach(d => d.classList.remove('show'));
  }

  function initMobileHeaderLanguage() {
    const logoBanner = document.querySelector('.logo-banner');
    if (!logoBanner || document.getElementById('uupm-mobile-head-lang')) return;

    const langBadge = document.createElement('div');
    langBadge.id = 'uupm-mobile-head-lang';
    langBadge.className = 'header-lang-badge uupm-mobile-head-badge';
    const cur = localStorage.getItem('site_lang') || 'vi';
    const isEn = cur === 'en';
    langBadge.innerHTML = `
      <img src="https://flagcdn.com/24x18/${isEn ? 'gb' : 'vn'}.png" alt="${isEn ? 'EN' : 'VI'}" class="lang-flag" width="20" height="20">
      <span>${isEn ? 'EN' : 'VI'} <i class="fa-solid fa-chevron-down"></i></span>
    `;

    const toggle = logoBanner.querySelector('.uupm-mobile-toggle') || logoBanner.querySelector('.menu-res') || logoBanner.querySelector('.btn-support');
    if (toggle && toggle.parentNode === logoBanner) {
      logoBanner.insertBefore(langBadge, toggle);
    } else {
      logoBanner.appendChild(langBadge);
    }
  }

  function initLanguageSwitcher() {
    initMobileHeaderLanguage();

    // Inject dropdown into all .header-lang-badge
    document.querySelectorAll('.header-lang-badge').forEach(badge => {
      if (!badge.querySelector('.uupm-lang-dropdown')) {
        const dd = document.createElement('div');
        dd.className = 'uupm-lang-dropdown';
        dd.innerHTML = `
          <button type="button" class="uupm-lang-option" data-lang="vi">
            <div class="uupm-opt-left">
              <img src="https://flagcdn.com/24x18/vn.png" alt="VN" style="width:20px;height:20px;border-radius:50%;object-fit:cover;">
              <span>Tiếng Việt</span>
            </div>
            <i class="fa-solid fa-check uupm-opt-check"></i>
          </button>
          <button type="button" class="uupm-lang-option" data-lang="en">
            <div class="uupm-opt-left">
              <img src="https://flagcdn.com/24x18/gb.png" alt="EN" style="width:20px;height:20px;border-radius:50%;object-fit:cover;">
              <span>English</span>
            </div>
            <i class="fa-solid fa-check uupm-opt-check"></i>
          </button>
        `;
        badge.appendChild(dd);
      }
    });

    // Also inject mobile language switcher into mobile menu if present
    const mobileNav = document.querySelector('#menu-mobile .head-menu') || document.querySelector('.menu-mobile');
    if (mobileNav && !document.getElementById('uupm-mobile-lang-box')) {
      const mBox = document.createElement('div');
      mBox.id = 'uupm-mobile-lang-box';
      mBox.className = 'uupm-mobile-lang-switch';
      mBox.style.cssText = 'display:flex;align-items:center;justify-content:center;gap:10px;padding:12px;margin:12px 14px;background:#FFFFFF;border-radius:14px;border:1.5px solid #EABF0E;box-shadow:0 4px 12px rgba(234,191,14,0.12);';
      mBox.innerHTML = `
        <button type="button" class="uupm-lang-option" data-lang="vi" style="flex:1;display:flex;align-items:center;justify-content:center;gap:8px;padding:8px 12px;border-radius:10px;border:none;cursor:pointer;font-weight:700;font-size:13px;font-family:'Be Vietnam Pro',sans-serif;">
          <img src="https://flagcdn.com/24x18/vn.png" alt="VN" style="width:20px;height:20px;border-radius:50%;object-fit:cover;">
          <span>Tiếng Việt</span>
        </button>
        <button type="button" class="uupm-lang-option" data-lang="en" style="flex:1;display:flex;align-items:center;justify-content:center;gap:8px;padding:8px 12px;border-radius:10px;border:none;cursor:pointer;font-weight:700;font-size:13px;font-family:'Be Vietnam Pro',sans-serif;">
          <img src="https://flagcdn.com/24x18/gb.png" alt="EN" style="width:20px;height:20px;border-radius:50%;object-fit:cover;">
          <span>English</span>
        </button>
      `;
      mobileNav.parentNode.insertBefore(mBox, mobileNav.nextSibling);
    }

    // Delegated click handler for badges and options
    document.addEventListener('click', (e) => {
      const option = e.target.closest('.uupm-lang-option');
      const badge = e.target.closest('.header-lang-badge');

      if (option) {
        e.stopPropagation();
        e.preventDefault();
        const targetLang = option.getAttribute('data-lang') || 'vi';
        applyLanguage(targetLang);
        closeAllLangDropdowns();
        showToast(targetLang === 'en' ? 'Switched to English' : 'Đã chuyển sang Tiếng Việt', 'success');
        return;
      }

      if (badge) {
        e.stopPropagation();
        const dd = badge.querySelector('.uupm-lang-dropdown');
        const isOpen = dd && dd.classList.contains('show');
        closeAllLangDropdowns();
        if (!isOpen && dd) {
          badge.classList.add('uupm-lang-open');
          dd.classList.add('show');
        }
        return;
      }

      closeAllLangDropdowns();
    });

    // Load Google Translate script asynchronously
    initGoogleTranslateScript();

    // Initialize saved language
    const savedLang = localStorage.getItem('site_lang') || 'vi';
    applyLanguage(savedLang);
  }

  // 14. DOM Initialization
  function init() {
    initHeaderScroll();
    initFloatingDock();
    initBookingModal();
    initActiveNavigation();
    initSearchAndArrowIcons();
    initUnifiedButtons();
    initDropdownMenu();
    initFaqAccordion();
    initVideoFacades();
    initScrollRevealAnimations();
    initBookingParams();
    initHeaderAddressMap();
    initFooterAddressMap();
    initPriceTabs();
    initLanguageSwitcher();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // 12. Global Doctor Booking Handler & Form Submit
  window.selectDoctor = function(doctorName) {
    const docSelect = document.getElementById('gf-doctor') || document.getElementById('bk_doctor') || document.getElementById('booking-doctor');
    if (docSelect) {
      for (let i = 0; i < docSelect.options.length; i++) {
        if (docSelect.options[i].value.includes(doctorName) || doctorName.includes(docSelect.options[i].value)) {
          docSelect.selectedIndex = i;
          break;
        }
      }
    }

    const srvSelect = document.getElementById('gf-service') || document.getElementById('booking-service');
    if (srvSelect && doctorName) {
      const srvText = (doctorName.includes('Thùy Chi') || doctorName.includes('Thanh Thủy'))
        ? 'Niềng'
        : doctorName.includes('Phục Hình')
          ? 'Sứ'
          : doctorName.includes('Kim Dung')
            ? 'Implant'
            : '';
      if (srvText) {
        for (let i = 0; i < srvSelect.options.length; i++) {
          if (srvSelect.options[i].value.includes(srvText) || srvSelect.options[i].text.includes(srvText)) {
            srvSelect.selectedIndex = i;
            break;
          }
        }
      }
    }

    const targetSec = document.getElementById('booking-section') || document.getElementById('dat-lich-kham');
    if (targetSec) {
      targetSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setTimeout(() => {
        const nameInput = document.getElementById('gf-name') || document.getElementById('booking-name') || document.getElementById('bk_name');
        if (nameInput) {
          nameInput.focus();
        }
      }, 600);
    } else {
      window.location.href = 'dat-lich.html?doctor=' + encodeURIComponent(doctorName);
    }
  };

  window.handleGfBookingSubmit = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const form = document.getElementById('gf-appointment-form');
    if (!form) return;
    const name = document.getElementById('gf-name')?.value.trim() || 'Quý khách';
    const phone = document.getElementById('gf-phone')?.value.trim() || '';
    const doctor = document.getElementById('gf-doctor')?.value || 'Bác sĩ chuyên khoa';
    const service = document.getElementById('gf-service')?.value || 'Tư vấn nha khoa';

    const submitBtn = form.querySelector('.gf-form-submit');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="margin-right:8px;"></i><span>Đang xác nhận lịch hẹn...</span>';
    }

    setTimeout(() => {
      form.innerHTML = `
        <div style="text-align: center; padding: 36px 20px;">
          <div style="width: 56px; height: 56px; border-radius: 50%; background: #FEF9E6; border: 2px solid #EABF0E; color: #B89307; display: inline-flex; align-items: center; justify-content: center; font-size: 26px; margin-bottom: 16px;">
            <i class="fa-solid fa-check"></i>
          </div>
          <h3 style="font-size: 22px; font-weight: 800; color: #18181b; margin-bottom: 8px;">Đặt Lịch Khám Thành Công!</h3>
          <p style="font-size: 15px; color: #475569; max-width: 540px; margin: 0 auto 18px; line-height: 1.6;">
            Cảm ơn <strong>${name}</strong> đã đặt lịch hẹn với <strong>${doctor}</strong> (${service}). Đội ngũ bác sĩ và trợ lý y tế của Nha Khoa Kim Dung sẽ gọi tới số <strong>${phone}</strong> trong vòng 15 phút để xác nhận chi tiết.
          </p>
          <div style="display: inline-flex; gap: 12px; flex-wrap: wrap; justify-content: center; margin-top: 10px;">
            <a href="tel:0862960886" class="gf-btn-primary" style="padding: 10px 22px; font-size: 14px;">
              <i class="fa-solid fa-phone"></i> <span>Hotline: 0862 960 886</span>
            </a>
            <button type="button" onclick="location.reload()" style="padding: 10px 20px; border-radius: 12px; border: 1.5px solid #cbd5e1; background: #fff; color: #334155; font-weight: 700; font-size: 14px; cursor: pointer;">
              Đặt lịch hẹn khác
            </button>
          </div>
        </div>
      `;
    }, 600);
  };
})();

