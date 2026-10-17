/**
 * TRANSITIONS & ANIMATIONS MODULE (TOÁN 11 MASTER)
 * 1. View Transitions API (Cross-Fade ATS)
 * 2. Sidebar Grid Accordion (grid-template-rows 0fr -> 1fr)
 * 3. Soft Start Entrance (0.4s)
 */

// Kích hoạt khi DOM sẵn sàng
document.addEventListener('DOMContentLoaded', function() {
    initSidebarGridAccordion();
    initSoftStartEntrance();
});

// Kích hoạt sớm Soft Start nếu DOM đã nạp xong
if (document.readyState !== 'loading') {
    initSoftStartEntrance();
}

/**
 * 1. Mở rộng Menu Sidebar (Grid Accordion)
 * Loại bỏ hoàn toàn thao tác bật/tắt display: none sang block.
 * Áp dụng kỹ thuật grid-template-rows chuyển từ 0fr sang 1fr kết hợp transition: 300ms ease-in-out.
 */
function initSidebarGridAccordion() {
    document.addEventListener('click', function(e) {
        const btn = e.target.closest('.sidebar-accordion .accordion-button');
        if (!btn) return;

        // Chặn hoàn toàn Bootstrap collapse plugin can thiệp inline style và display:none
        e.preventDefault();
        e.stopPropagation();

        const item = btn.closest('.accordion-item');
        const targetCollapse = item ? item.querySelector('.accordion-collapse') : null;
        if (!targetCollapse) return;

        const isCurrentlyOpen = targetCollapse.classList.contains('show');
        const accordionContainer = btn.closest('.sidebar-accordion');

        // Đóng các mục khác trong cùng danh mục menu khi mở mục mới (Accordion behavior)
        if (accordionContainer && !isCurrentlyOpen) {
            accordionContainer.querySelectorAll('.accordion-collapse.show').forEach(openCol => {
                if (openCol !== targetCollapse) {
                    openCol.classList.remove('show');
                    const otherBtn = openCol.closest('.accordion-item')?.querySelector('.accordion-button');
                    if (otherBtn) {
                        otherBtn.classList.add('collapsed');
                        otherBtn.setAttribute('aria-expanded', 'false');
                    }
                }
            });
        }

        if (isCurrentlyOpen) {
            targetCollapse.classList.remove('show');
            btn.classList.add('collapsed');
            btn.setAttribute('aria-expanded', 'false');
        } else {
            targetCollapse.classList.add('show');
            btn.classList.remove('collapsed');
            btn.setAttribute('aria-expanded', 'true');
        }
    }, true); // Bắt ở Capture phase để ngăn chặn Bootstrap Collapse JS
}

/**
 * 2. Tải nội dung bài học (Soft Start)
 * Thiết lập trạng thái gốc: opacity: 0 và transform: translateY(15px).
 * Kích hoạt chuyển tiếp về opacity: 1 và transform: translateY(0) trong 0.4s ngay khi DOM tải xong.
 */
function initSoftStartEntrance() {
    const mainEl = document.getElementById('spaMainContent') || document.querySelector('.main-column');
    if (!mainEl) return;

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            mainEl.classList.add('soft-start-ready');
        });
    });
}

/**
 * 3. View Transitions API Helper (ATS Seamless Cross-Fade)
 * @param {Function} domUpdateCallback - Callback thực hiện hoán đổi nội dung DOM
 * @returns {Promise<void>}
 */
async function executeAtsViewTransition(domUpdateCallback) {
    if (document.startViewTransition) {
        // Native View Transitions API
        const transition = document.startViewTransition(() => {
            domUpdateCallback();
        });
        await transition.finished.catch(() => {});
    } else {
        // Fallback Cross-Fade đối xứng không chớp trắng
        const viewContainer = document.getElementById('spaViewContainer');
        if (viewContainer) {
            viewContainer.classList.add('ats-crossfade-out');
            await new Promise(r => setTimeout(r, 150));
            domUpdateCallback();
            viewContainer.classList.remove('ats-crossfade-out');
            viewContainer.classList.add('ats-crossfade-in');
            setTimeout(() => viewContainer.classList.remove('ats-crossfade-in'), 250);
        } else {
            domUpdateCallback();
        }
    }
}

// Xuất các hàm để sử dụng ở bất kỳ đâu
window.initSidebarGridAccordion = initSidebarGridAccordion;
window.initSoftStartEntrance = initSoftStartEntrance;
window.executeAtsViewTransition = executeAtsViewTransition;
