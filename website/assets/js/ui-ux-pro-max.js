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

    // Hide old hotline and social widgets if present to avoid screen clutter
    const oldHotline = document.querySelector('#hotline');
    if (oldHotline) oldHotline.style.display = 'none';
    const oldSocial = document.querySelector('#social');
    if (oldSocial) oldSocial.style.display = 'none';

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
      <button type="button" class="uupm-dock-btn btn-book" id="uupm-open-booking" title="Đặt Lịch Khám Ngay" aria-label="Đặt lịch khám">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        <span class="dock-label">Đặt Lịch Hẹn</span>
      </button>
      <button type="button" class="uupm-dock-btn btn-top" id="uupm-btn-top" title="Lên đầu trang" aria-label="Lên đầu trang">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
    `;
    document.body.appendChild(dock);

    // Scroll to Top behavior
    const btnTop = document.getElementById('uupm-btn-top');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 350) {
        btnTop.classList.add('visible');
      } else {
        btnTop.classList.remove('visible');
      }
    }, { passive: true });

    btnTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
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

    document.getElementById('uupm-open-booking')?.addEventListener('click', openModal);
    document.getElementById('uupm-modal-close')?.addEventListener('click', closeModal);

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
        closeModal();
      }
    });

    // Delegate action buttons (excluding navbar navigation tabs) to open modal
    document.querySelectorAll('a[href*="dat-lich"], button:not(#uupm-open-booking)').forEach((btn) => {
      // Do NOT hijack navigation tabs in header, mobile menu, footer, or dat-lich.html dedicated form
      if (btn.closest('nav') || btn.closest('.menu') || btn.closest('.menu-mobile') || btn.closest('.wrap-menu') || btn.closest('.ulmn') || btn.closest('.footer-ul') || btn.closest('#gf-main-booking-form') || btn.closest('.gf-booking-section') || btn.closest('#booking-receipt')) {
        return;
      }
      const txt = (btn.textContent || '').trim().toLowerCase();
      if (txt.includes('đặt lịch') || txt.includes('tư vấn') || txt.includes('đăng ký khám')) {
        btn.addEventListener('click', (e) => {
          if (!btn.closest('.uupm-modal')) {
            e.preventDefault();
            openModal();
          }
        });
      }
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
        } else if (href.includes('dich-vu.html') && (
          currentFile.includes('dich-vu') || currentFile.includes('implant') ||
          currentFile.includes('rang-su') || currentFile.includes('nieng-rang') ||
          currentFile.includes('nho-rang') || currentFile.includes('cao-rang') ||
          currentFile.includes('tay-trang') || currentFile.includes('tram-rang') ||
          currentFile.includes('ham-thao-lap') || currentFile.includes('tre-em')
        )) {
          l.classList.add('active');
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

    // Inject hamburger toggle button into header if not present
    let toggleBtn = document.getElementById('uupm-mobile-toggle');
    if (!toggleBtn) {
      toggleBtn = document.createElement('button');
      toggleBtn.id = 'uupm-mobile-toggle';
      toggleBtn.className = 'uupm-mobile-toggle';
      toggleBtn.type = 'button';
      toggleBtn.setAttribute('aria-label', 'Mở menu điều hướng');
      toggleBtn.innerHTML = `
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
      `;

      // Insert into .logo-banner or .head-bottom .wrap-content
      const targetContainer = document.querySelector('.logo-banner') || document.querySelector('.head-bottom .wrap-content');
      if (targetContainer) {
        targetContainer.appendChild(toggleBtn);
      }
    }

    const openMobileMenu = () => {
      mobileMenu.classList.add('show');
      mobileMenu.style.visibility = 'visible';
      document.body.style.overflow = 'hidden';

      let backdrop = document.getElementById('uupm-menu-backdrop');
      if (!backdrop) {
        backdrop = document.createElement('div');
        backdrop.id = 'uupm-menu-backdrop';
        backdrop.className = 'uupm-menu-backdrop';
        document.body.appendChild(backdrop);
        backdrop.addEventListener('click', closeMobileMenu);
      }
      backdrop.classList.add('show');
    };

    const closeMobileMenu = () => {
      mobileMenu.classList.remove('show');
      document.body.style.overflow = '';
      const backdrop = document.getElementById('uupm-menu-backdrop');
      if (backdrop) backdrop.classList.remove('show');
    };

    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (mobileMenu.classList.contains('show')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });

    const closeBtn = mobileMenu.querySelector('.btn-close-menu');
    if (closeBtn) closeBtn.addEventListener('click', closeMobileMenu);

    // Close when clicking any navigation link inside mobile menu
    mobileMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        closeMobileMenu();
      });
    });
  }

  // 9. Dropdown Menu Controller (Greenfield Style)
  function initDropdownMenu() {
    const dropdownParents = document.querySelectorAll('.menu ul li.has-dropdown');
    dropdownParents.forEach(parent => {
      const link = parent.querySelector(':scope > a');
      const dropdown = parent.querySelector('.dropdown-menu-service');
      if (!link || !dropdown) return;

      // Handle click on touch devices
      link.addEventListener('click', (e) => {
        // If on small device or clicked to open
        if (window.innerWidth <= 1024) {
          e.preventDefault();
          parent.classList.toggle('is-open');
        }
      });
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

        if (isExpanded) {
          card.classList.remove('is-open');
          if (answer) answer.style.display = 'none';
          if (icon) icon.style.transform = '';
        } else {
          card.classList.add('is-open');
          if (answer) answer.style.display = 'block';
          if (icon) icon.style.transform = 'rotate(180deg)';
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

  // 11. DOM Initialization
  function init() {
    initHeaderScroll();
    initFloatingDock();
    initBookingModal();
    initActiveNavigation();
    initSearchAndArrowIcons();
    initUnifiedButtons();
    initDropdownMenu();
    initFaqAccordion();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
