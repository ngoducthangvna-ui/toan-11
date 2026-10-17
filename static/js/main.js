/**
 * Main JavaScript for TOAN 11 MASTER
 * Refactored: Data-Driven Sidebar, Event Delegation, Lazy Loading & Clean Modular Architecture
 */

// ==========================================================================
// 1. Data-Driven Curriculum Definition (Chapters 1 to 9 & 29 Lessons)
// ==========================================================================
const chaptersData = [
    {
        id: 1,
        volume: 1,
        title: "Chương 1: Lượng giác",
        icon: "bi-symmetry-horizontal",
        lessons: [
            { id: 1, title: "Bài 1: Giá trị lượng giác của góc lượng giác" },
            { id: 2, title: "Bài 2: Các công thức lượng giác trọng tâm" },
            { id: 3, title: "Bài 3: Hàm số lượng giác và đồ thị" },
            { id: 4, title: "Bài 4: Phương trình lượng giác cơ bản" }
        ]
    },
    {
        id: 2,
        volume: 1,
        title: "Chương 2: Dãy số, CSC & CSN",
        icon: "bi-sort-numeric-up",
        lessons: [
            { id: 1, title: "Bài 1: Dãy số và các tính chất" },
            { id: 2, title: "Bài 2: Cấp số cộng (CSC)" },
            { id: 3, title: "Bài 3: Cấp số nhân (CSN)" }
        ]
    },
    {
        id: 3,
        volume: 1,
        title: "Chương 3: Thống kê mẫu ghép nhóm",
        icon: "bi-bar-chart-line-fill",
        lessons: [
            { id: 1, title: "Bài 1: Thu thập và ghép nhóm số liệu" },
            { id: 2, title: "Bài 2: Các số đặc trưng đo xu thế trung tâm" }
        ]
    },
    {
        id: 4,
        volume: 1,
        title: "Chương 4: Song song không gian",
        icon: "bi-box",
        lessons: [
            { id: 1, title: "Bài 1: Điểm, đường thẳng và mặt phẳng trong không gian" },
            { id: 2, title: "Bài 2: Hai đường thẳng song song" },
            { id: 3, title: "Bài 3: Đường thẳng song song với mặt phẳng" },
            { id: 4, title: "Bài 4: Hai mặt phẳng song song" }
        ]
    },
    {
        id: 5,
        volume: 1,
        title: "Chương 5: Giới hạn & Liên tục",
        icon: "bi-infinity",
        lessons: [
            { id: 1, title: "Bài 1: Giới hạn của dãy số" },
            { id: 2, title: "Bài 2: Giới hạn của hàm số và các dạng vô định" },
            { id: 3, title: "Bài 3: Hàm số liên tục" }
        ]
    },
    {
        id: 6,
        volume: 2,
        title: "Chương 6: Mũ & Logarit",
        icon: "bi-graph-up-arrow",
        lessons: [
            { id: 1, title: "Bài 1: Phép tính lũy thừa với số mũ thực" },
            { id: 2, title: "Bài 2: Phép tính logarit" },
            { id: 3, title: "Bài 3: Hàm số mũ và Hàm số logarit" },
            { id: 4, title: "Bài 4: Phương trình và Bất phương trình mũ, logarit cơ bản" }
        ]
    },
    {
        id: 7,
        volume: 2,
        title: "Chương 7: Đạo hàm",
        icon: "bi-lightning-charge-fill",
        lessons: [
            { id: 1, title: "Bài 1: Định nghĩa và ý nghĩa của đạo hàm" },
            { id: 2, title: "Bài 2: Các quy tắc tính đạo hàm và đạo hàm hàm hợp" },
            { id: 3, title: "Bài 3: Đạo hàm cấp hai" }
        ]
    },
    {
        id: 8,
        volume: 2,
        title: "Chương 8: Vuông góc không gian",
        icon: "bi-bounding-box-circles",
        lessons: [
            { id: 1, title: "Bài 1: Góc giữa hai đường thẳng và hai đường thẳng vuông góc" },
            { id: 2, title: "Bài 2: Đường thẳng vuông góc với mặt phẳng" },
            { id: 3, title: "Bài 3: Hai mặt phẳng vuông góc" },
            { id: 4, title: "Bài 4: Khoảng cách và Góc trong không gian" }
        ]
    },
    {
        id: 9,
        volume: 2,
        title: "Chương 9: Xác suất",
        icon: "bi-dice-5-fill",
        lessons: [
            { id: 1, title: "Bài 1: Biến cố giao và quy tắc nhân xác suất" },
            { id: 2, title: "Bài 2: Biến cố hợp và quy tắc cộng xác suất" }
        ]
    }
];

// Monkey-patch document.addEventListener for DOMContentLoaded to support dynamic SPA scripts
const _originalAddEventListener = document.addEventListener;
document.addEventListener = function(type, listener, options) {
    if (type === 'DOMContentLoaded' && document.readyState !== 'loading') {
        setTimeout(listener, 1);
        return;
    }
    return _originalAddEventListener.call(this, type, listener, options);
};

// Global Toast Helper
function showToast(message, type = 'success') {
    const toastEl = document.getElementById('appToast');
    if (!toastEl) return;
    const msgEl = document.getElementById('appToastMessage');
    const iconEl = document.getElementById('appToastIcon');
    if (msgEl) msgEl.innerText = message;
    
    toastEl.className = 'toast align-items-center border-0 shadow-lg text-white';
    if (type === 'success') {
        toastEl.classList.add('bg-success');
        if (iconEl) iconEl.className = 'bi bi-check-circle-fill fs-5 text-white';
    } else if (type === 'danger' || type === 'error') {
        toastEl.classList.add('bg-danger');
        if (iconEl) iconEl.className = 'bi bi-exclamation-triangle-fill fs-5 text-white';
    } else {
        toastEl.classList.add('bg-primary');
        if (iconEl) iconEl.className = 'bi bi-info-circle-fill fs-5 text-white';
    }

    try {
        const bsToast = bootstrap.Toast.getOrCreateInstance(toastEl, { delay: 2800 });
        bsToast.show();
    } catch (_) {}
}

// Ultra-Fast Math Rendering (KaTeX auto-render prioritized with targeted scoping)
function renderMath(container) {
    if (!container) {
        // Scoped targeting: never render document.body to avoid layout thrashing and freezing
        container = document.querySelector('.lesson-article') || 
                    document.querySelector('.exam-view-page') || 
                    document.getElementById('quizForm') || 
                    document.getElementById('formulaCategoriesContainer') || 
                    document.getElementById('spaViewContainer');
    }
    if (!container) return;

    const renderOpts = {
        delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '\\[', right: '\\]', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false,
        ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"]
    };

    if (window.renderMathInElement) {
        try {
            window.renderMathInElement(container, renderOpts);
        } catch (_) {}
    } else {
        // If KaTeX auto-render script is still loading in head, poll briefly
        let retries = 0;
        const checkKaTeX = setInterval(() => {
            retries++;
            if (window.renderMathInElement) {
                clearInterval(checkKaTeX);
                try {
                    window.renderMathInElement(container, renderOpts);
                } catch (_) {}
            } else if (retries >= 20) {
                clearInterval(checkKaTeX);
            }
        }, 50);
    }
}
window.renderMath = renderMath;


// ==========================================================================
// 2. Data-Driven Sidebar Rendering Engine
// ==========================================================================
function renderSidebar(activeChapterId = null, activeLessonId = null) {
    const containers = document.querySelectorAll('#curriculumAccordion');
    if (!containers.length) return;

    if (activeChapterId === null) {
        const path = window.location.pathname;
        const match = path.match(/\/chapter\/(\d+)(?:\/lesson\/(\d+))?/);
        if (match) {
            activeChapterId = parseInt(match[1], 10);
            if (match[2]) activeLessonId = parseInt(match[2], 10);
        } else {
            // Default to Chapter 1 on home page and others
            activeChapterId = 1;
        }
    }

    let vol1Html = `
        <div class="volume-header volume-header-first">
            <i class="bi bi-book-half text-primary flex-shrink-0"></i> TẬP 1 (HỌC KÌ I)
        </div>
    `;

    let vol2Html = `
        <div class="volume-header">
            <i class="bi bi-book-fill text-success flex-shrink-0"></i> TẬP 2 (HỌC KÌ II)
        </div>
    `;

    chaptersData.forEach(ch => {
        const isOpen = (ch.id === Number(activeChapterId));
        const iconColor = ch.volume === 1 ? 'text-primary' : 'text-success';

        let lessonsHtml = '';
        ch.lessons.forEach(les => {
            const isActive = (ch.id === Number(activeChapterId) && les.id === Number(activeLessonId));
            lessonsHtml += `
                <a href="/chapter/${ch.id}/lesson/${les.id}" 
                   class="sidebar-lesson-link ${isActive ? 'active' : ''}"
                   data-lesson-id="ch${ch.id}_les${les.id}"
                   title="${les.title}">
                    <span class="lesson-link-text">${les.title}</span>
                    <i class="bi bi-check-circle-fill lesson-check-icon text-success d-none ms-1 flex-shrink-0"></i>
                </a>
            `;
        });

        const chHtml = `
            <div class="accordion-item border-0 mb-1 rounded-3 overflow-hidden" data-chapter-id="${ch.id}">
                <h2 class="accordion-header" id="heading-ch-${ch.id}">
                    <button class="accordion-button sidebar-ch-btn ${isOpen ? '' : 'collapsed'}" 
                            type="button" 
                            data-chapter-target="collapse-ch-${ch.id}" 
                            data-chapter-id="${ch.id}" 
                            aria-expanded="${isOpen ? 'true' : 'false'}">
                        <span class="chapter-btn-left">
                            <i class="bi ${ch.icon} ${iconColor} flex-shrink-0"></i>
                            <span class="sidebar-chapter-label">${ch.title}</span>
                        </span>
                    </button>
                </h2>
                <div id="collapse-ch-${ch.id}" class="sidebar-accordion-collapse ${isOpen ? 'show' : ''}" data-chapter-id="${ch.id}">
                    <div class="sidebar-accordion-inner">
                        <div class="sidebar-lessons-tree">
                            ${lessonsHtml}
                        </div>
                    </div>
                </div>
            </div>
        `;

        if (ch.volume === 1) {
            vol1Html += chHtml;
        } else {
            vol2Html += chHtml;
        }
    });

    const fullHtml = vol1Html + vol2Html;
    containers.forEach(c => {
        c.innerHTML = fullHtml;
    });

    // Update completed checkmarks in sidebar
    updateCompletedLessonCheckmarks();
}

// ==========================================================================
// 3. Event Delegation for Sidebar (Accordion Toggle & Lesson Selection)
// ==========================================================================
function initSidebarEventDelegation() {
    const sidebars = document.querySelectorAll('#desktopSidebar, #sidebarOffcanvas');
    sidebars.forEach(sidebar => {
        if (sidebar._hasSidebarEvents) return;
        sidebar._hasSidebarEvents = true;

        sidebar.addEventListener('click', function(e) {
            // A. Accordion Chapter Click (entire header or button)
            const chBtn = e.target.closest('.sidebar-ch-btn') || e.target.closest('.accordion-header')?.querySelector('.sidebar-ch-btn');
            if (chBtn) {
                e.preventDefault();
                e.stopPropagation();
                toggleChapterAccordion(chBtn);
                return;
            }

            // B. Lesson Link Selection (track last lesson)
            const lessonLink = e.target.closest('.sidebar-lesson-link');
            if (lessonLink) {
                const textEl = lessonLink.querySelector('.lesson-link-text');
                const title = textEl ? textEl.innerText.trim() : lessonLink.innerText.trim();
                const url = lessonLink.getAttribute('href');
                if (url && url !== '#') {
                    try {
                        const data = { title, url };
                        localStorage.setItem('toan11_last_lesson', JSON.stringify(data));
                        localStorage.setItem('lastVisitedLesson', JSON.stringify(data));
                    } catch (_) {}
                }
                closeMobileSidebar();
                return;
            }
        });
    });
}

function toggleChapterAccordion(btn) {
    const chapterId = btn.getAttribute('data-chapter-id') || 
                      btn.closest('.accordion-item')?.getAttribute('data-chapter-id');
    const targetId = btn.getAttribute('data-chapter-target') || (chapterId ? `collapse-ch-${chapterId}` : null);
    if (!targetId && !chapterId) return;

    const accordionItem = btn.closest('.accordion-item');
    const targetCollapse = accordionItem ? 
        accordionItem.querySelector('.sidebar-accordion-collapse') : 
        (targetId ? document.getElementById(targetId) : null);
        
    if (!targetCollapse) return;

    const isCurrentlyOpen = targetCollapse.classList.contains('show');
    const nextState = !isCurrentlyOpen;

    if (nextState) {
        // Accordion behavior: close other chapters
        document.querySelectorAll('.sidebar-accordion-collapse').forEach(c => {
            const id = c.getAttribute('data-chapter-id');
            if (id !== chapterId && c.id !== targetId) {
                c.classList.remove('show');
            }
        });
        document.querySelectorAll('.sidebar-ch-btn').forEach(b => {
            const id = b.getAttribute('data-chapter-id');
            const target = b.getAttribute('data-chapter-target');
            if (id !== chapterId && target !== targetId) {
                b.classList.add('collapsed');
                b.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Toggle across all instances of this chapter (desktop & offcanvas)
    const collSelector = chapterId ? `.sidebar-accordion-collapse[data-chapter-id="${chapterId}"]` : `#${targetId}`;
    const btnSelector = chapterId ? `.sidebar-ch-btn[data-chapter-id="${chapterId}"]` : `[data-chapter-target="${targetId}"]`;

    document.querySelectorAll(collSelector).forEach(c => {
        if (nextState) c.classList.add('show');
        else c.classList.remove('show');
    });

    document.querySelectorAll(btnSelector).forEach(b => {
        if (nextState) {
            b.classList.remove('collapsed');
            b.setAttribute('aria-expanded', 'true');
        } else {
            b.classList.add('collapsed');
            b.setAttribute('aria-expanded', 'false');
        }
    });

    saveSidebarState();
}

function saveSidebarState() {
    try {
        const openIds = [];
        const desktop = document.getElementById('desktopSidebar');
        const scope = desktop || document;
        scope.querySelectorAll('.sidebar-accordion-collapse.show').forEach(el => {
            const id = el.getAttribute('data-chapter-id');
            if (id && !openIds.includes(String(id))) {
                openIds.push(String(id));
            }
        });
        localStorage.setItem('toan11_open_chapters', JSON.stringify(openIds));
        sessionStorage.setItem('toan11_open_chapters', JSON.stringify(openIds));
    } catch (_) {}
}

function closeMobileSidebar() {
    const offcanvasEl = document.getElementById('sidebarOffcanvas');
    if (offcanvasEl && offcanvasEl.classList.contains('show') && window.bootstrap && window.bootstrap.Offcanvas) {
        try {
            const inst = bootstrap.Offcanvas.getInstance(offcanvasEl);
            if (inst) inst.hide();
        } catch (_) {}
    }
}

function updateCompletedLessonCheckmarks() {
    try {
        const completed = JSON.parse(localStorage.getItem('toan11_completed_lessons') || '[]');
        document.querySelectorAll('.sidebar-lesson-link').forEach(link => {
            const lessonId = link.getAttribute('data-lesson-id');
            const icon = link.querySelector('.lesson-check-icon');
            if (icon && lessonId) {
                if (completed.includes(lessonId)) {
                    icon.classList.remove('d-none');
                } else {
                    icon.classList.add('d-none');
                }
            }
        });
    } catch (_) {}
}

function initSidebarScrollTracking() {
    const desktop = document.getElementById('desktopSidebar');
    if (!desktop || desktop._scrollTracked) return;
    desktop._scrollTracked = true;

    let scrollTimeout = null;
    desktop.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            try {
                localStorage.setItem('toan11_sidebar_scroll', desktop.scrollTop);
                sessionStorage.setItem('toan11_sidebar_scroll', desktop.scrollTop);
            } catch (_) {}
        }, 60);
    }, { passive: true });
}

// ==========================================================================
// 4. Theme Management (Dark / Light Mode)
// ==========================================================================
function initTheme() {
    const themeBtn = document.getElementById('themeToggleBtn');
    const themeIcon = document.getElementById('themeIcon');
    const savedTheme = localStorage.getItem('toan11_theme') || 'light';

    document.documentElement.setAttribute('data-bs-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeBtn && !themeBtn._themeBound) {
        themeBtn._themeBound = true;
        themeBtn.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-bs-theme');
            const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-bs-theme', nextTheme);
            localStorage.setItem('toan11_theme', nextTheme);
            updateThemeIcon(nextTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'dark') {
            themeIcon.className = 'bi bi-sun-fill text-warning';
        } else {
            themeIcon.className = 'bi bi-moon-stars-fill';
        }
    }
}

// ==========================================================================
// 5. Learning Progress Tracker
// ==========================================================================
function initProgress() {
    const STORAGE_KEY = 'toan11_completed_lessons';
    let completedLessons = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    updateProgressUI();

    const markBtn = document.getElementById('markCompleteBtn');
    if (markBtn && !markBtn.dataset.bound) {
        markBtn.dataset.bound = 'true';
        const lessonId = markBtn.dataset.lessonId;
        const markText = document.getElementById('markCompleteText');

        if (completedLessons.includes(lessonId)) {
            setBtnCompleted(true);
        }

        markBtn.addEventListener('click', function() {
            const idx = completedLessons.indexOf(lessonId);
            if (idx === -1) {
                completedLessons.push(lessonId);
                setBtnCompleted(true);
                showToast('Đã hoàn thành bài học! Tiến độ +1', 'success');
            } else {
                completedLessons.splice(idx, 1);
                setBtnCompleted(false);
                showToast('Đã hủy đánh dấu hoàn thành bài học', 'info');
            }
            localStorage.setItem(STORAGE_KEY, JSON.stringify(completedLessons));
            updateProgressUI();
        });

        function setBtnCompleted(isDone) {
            const icon = markBtn.querySelector('i');
            if (isDone) {
                markBtn.className = 'btn btn-success btn-sm d-inline-flex align-items-center gap-1 shadow-sm';
                if (markText) markText.innerText = 'Đã hoàn thành bài này';
                if (icon) icon.className = 'bi bi-check-circle-fill text-white';
            } else {
                markBtn.className = 'btn btn-outline-success btn-sm d-inline-flex align-items-center gap-1';
                if (markText) markText.innerText = 'Đánh dấu đã học xong';
                if (icon) icon.className = 'bi bi-check2-circle';
            }
        }
    }

    const resetBtn = document.getElementById('resetProgressBtn');
    if (resetBtn && !resetBtn._resetBound) {
        resetBtn._resetBound = true;
        resetBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('Bạn có chắc chắn muốn đặt lại toàn bộ tiến độ học tập?')) {
                completedLessons = [];
                localStorage.setItem(STORAGE_KEY, JSON.stringify([]));
                updateProgressUI();
                if (markBtn) {
                    markBtn.className = 'btn btn-outline-success btn-sm d-inline-flex align-items-center gap-1';
                    const markText = document.getElementById('markCompleteText');
                    if (markText) markText.innerText = 'Đánh dấu đã học xong';
                }
            }
        });
    }

    function updateProgressUI() {
        const totalLessons = 29;
        const count = completedLessons.length;
        const percent = Math.min(100, Math.round((count / totalLessons) * 100));

        const bar = document.getElementById('overallProgressBar');
        const text = document.getElementById('overallProgressText');
        const counter = document.getElementById('completedLessonsCount');

        if (bar) bar.style.width = percent + '%';
        if (text) text.innerText = percent + '%';
        if (counter) counter.innerText = `${count}/${totalLessons} bài`;

        updateCompletedLessonCheckmarks();
    }
}

// ==========================================================================
// 6. Continue Learning Feature (Homepage CTA)
// ==========================================================================
function initContinueLearning() {
    const LAST_LESSON_KEY = 'toan11_last_lesson';
    const heroBtn = document.getElementById('heroPrimaryBtn');
    const heroText = document.getElementById('heroPrimaryBtnText');
    if (!heroBtn || !heroText) return;

    let savedLast = null;
    try {
        const raw = localStorage.getItem(LAST_LESSON_KEY) || localStorage.getItem('lastVisitedLesson');
        if (raw) savedLast = JSON.parse(raw);
    } catch (_) {}

    if (savedLast && savedLast.url && savedLast.title) {
        heroBtn.href = savedLast.url;
        heroText.innerText = `Tiếp tục học: ${savedLast.title}`;
    }
}

// ==========================================================================
// 7. Live Search & Homepage Card Filter
// ==========================================================================
function initSearch() {
    const searchInput = document.getElementById('globalSearchInput');
    const dropdown = document.getElementById('searchResultsDropdown');
    const clearHomeBtn = document.getElementById('clearHomeSearchBtn');
    if (!searchInput) return;

    let debounceTimer = null;
    let selectedSearchIdx = -1;

    function highlightSearchItem(idx) {
        if (!dropdown) return;
        const items = dropdown.querySelectorAll('.dropdown-item');
        if (!items.length) return;

        items.forEach((item, i) => {
            if (i === idx) {
                item.classList.add('search-active');
                item.scrollIntoView({ block: 'nearest' });
            } else {
                item.classList.remove('search-active');
            }
        });
        selectedSearchIdx = idx;
    }

    if (!searchInput._searchBound) {
        searchInput._searchBound = true;

        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            const query = this.value.trim();

            if (!query) {
                if (dropdown) dropdown.style.display = 'none';
                filterHomepageCards('');
                return;
            }

            filterHomepageCards(query);

            debounceTimer = setTimeout(() => {
                fetch(`/api/search?q=${encodeURIComponent(query)}`)
                    .then(r => r.json())
                    .then(data => {
                        renderSearchResults(data.results || [], query);
                    })
                    .catch(() => {
                        if (dropdown) dropdown.style.display = 'none';
                    });
            }, 180);
        });

        searchInput.addEventListener('keydown', function(e) {
            if (!dropdown || dropdown.style.display !== 'block') return;
            const items = dropdown.querySelectorAll('.dropdown-item');
            if (!items.length) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                selectedSearchIdx = (selectedSearchIdx + 1) % items.length;
                highlightSearchItem(selectedSearchIdx);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                selectedSearchIdx = (selectedSearchIdx - 1 + items.length) % items.length;
                highlightSearchItem(selectedSearchIdx);
            } else if (e.key === 'Enter') {
                if (selectedSearchIdx >= 0 && items[selectedSearchIdx]) {
                    e.preventDefault();
                    items[selectedSearchIdx].click();
                }
            } else if (e.key === 'Escape') {
                dropdown.style.display = 'none';
            }
        });
    }

    if (clearHomeBtn && !clearHomeBtn._clearBound) {
        clearHomeBtn._clearBound = true;
        clearHomeBtn.addEventListener('click', function() {
            searchInput.value = '';
            filterHomepageCards('');
            if (dropdown) dropdown.style.display = 'none';
        });
    }

    // Close dropdown on outside click
    document.addEventListener('click', function(e) {
        if (dropdown && !searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });

    function filterHomepageCards(query) {
        const cards = document.querySelectorAll('.chapter-card-col');
        const alertBox = document.getElementById('homeSearchAlert');
        const keywordSpan = document.getElementById('homeSearchKeyword');
        if (!cards.length) return;

        if (!query) {
            cards.forEach(c => c.classList.remove('d-none', 'search-matched'));
            if (alertBox) alertBox.classList.add('d-none');
            return;
        }

        const normQuery = query.toLowerCase();
        let matchCount = 0;

        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            if (text.includes(normQuery)) {
                card.classList.remove('d-none');
                card.classList.add('search-matched');
                matchCount++;
            } else {
                card.classList.add('d-none');
                card.classList.remove('search-matched');
            }
        });

        if (alertBox && keywordSpan) {
            alertBox.classList.remove('d-none');
            keywordSpan.innerText = `${query} (${matchCount} kết quả)`;
        }
    }

    function renderSearchResults(results, query) {
        if (!dropdown) return;
        if (!results.length) {
            dropdown.innerHTML = `<div class="p-3 text-muted text-center small">Không tìm thấy kết quả cho "<strong>${escapeHtml(query)}</strong>"</div>`;
            dropdown.style.display = 'block';
            return;
        }

        selectedSearchIdx = -1;
        let html = '';
        results.slice(0, 8).forEach(res => {
            const icon = res.type === 'lesson' ? 'bi-file-earmark-text text-primary' : 'bi-journal-bookmark text-success';
            html += `
                <a href="${res.url}" class="dropdown-item d-flex align-items-center gap-2 p-2 rounded-2 text-decoration-none">
                    <i class="bi ${icon} flex-shrink-0"></i>
                    <div class="flex-grow-1 overflow-hidden">
                        <div class="fw-semibold text-truncate small">${escapeHtml(res.title)}</div>
                        <div class="text-muted text-truncate" style="font-size:0.75rem;">${escapeHtml(res.subtitle || '')}</div>
                    </div>
                </a>
            `;
        });

        dropdown.innerHTML = html;
        dropdown.style.display = 'block';

        dropdown.querySelectorAll('.dropdown-item').forEach((item, i) => {
            item.addEventListener('mouseenter', () => highlightSearchItem(i));
        });
    }

    function escapeHtml(str) {
        if (!str) return '';
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
    }
}

// ==========================================================================
// 8. Interactive Quiz Engine & Lazy-Loaded Celebration
// ==========================================================================
function initQuiz() {
    const quizForm = document.getElementById('quizForm');
    if (!quizForm || quizForm._quizBound) return;
    quizForm._quizBound = true;

    const questionCards = document.querySelectorAll('.question-card');
    const submitBtn = document.getElementById('submitQuizBtn');
    const retryBtn = document.getElementById('retryQuizBtn');
    const resultCard = document.getElementById('quizResultCard');

    questionCards.forEach(card => {
        const labels = card.querySelectorAll('.option-label');
        labels.forEach(label => {
            label.addEventListener('click', function() {
                labels.forEach(l => l.classList.remove('selected'));
                this.classList.add('selected');
                const radio = this.querySelector('input[type="radio"]');
                if (radio) radio.checked = true;
            });
        });
    });

    if (submitBtn) {
        submitBtn.addEventListener('click', function() {
            let correctCount = 0;
            const total = questionCards.length;
            let unanswered = 0;

            questionCards.forEach(card => {
                const checked = card.querySelector('input[type="radio"]:checked');
                if (!checked) unanswered++;
            });

            if (unanswered > 0) {
                if (!confirm(`Bạn còn ${unanswered} câu chưa làm. Bạn có chắc chắn muốn nộp bài luôn không?`)) return;
            }

            questionCards.forEach(card => {
                const correctVal = parseInt(card.dataset.correct, 10);
                const qId = card.dataset.questionId;
                const checked = card.querySelector('input[type="radio"]:checked');
                const explanationBox = document.getElementById(`explanation-${qId}`);
                const statusBox = explanationBox ? explanationBox.querySelector('.explanation-status') : null;
                const labels = card.querySelectorAll('.option-label');

                card.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
                if (labels[correctVal]) labels[correctVal].classList.add('correct-choice');

                if (checked) {
                    const userVal = parseInt(checked.value, 10);
                    if (userVal === correctVal) {
                        correctCount++;
                        if (statusBox) statusBox.innerHTML = '<span class="badge bg-success"><i class="bi bi-check-lg"></i> Chính xác!</span>';
                    } else {
                        if (labels[userVal]) labels[userVal].classList.add('wrong-choice');
                        if (statusBox) statusBox.innerHTML = '<span class="badge bg-danger"><i class="bi bi-x-lg"></i> Chưa chính xác</span>';
                    }
                } else {
                    if (statusBox) statusBox.innerHTML = '<span class="badge bg-secondary"><i class="bi bi-dash-circle"></i> Chưa trả lời</span>';
                }

                if (explanationBox) explanationBox.classList.remove('d-none');
            });

            const score = ((correctCount / total) * 10).toFixed(1);
            const percent = Math.round((correctCount / total) * 100);

            // Update Result Banner
            const scoreEl = document.getElementById('resultScore');
            const progressEl = document.getElementById('resultProgressBar');
            const titleEl = document.getElementById('resultTitle');
            const feedbackEl = document.getElementById('resultFeedback');
            const iconEl = document.getElementById('resultIcon');

            if (scoreEl) scoreEl.innerText = `${score} / 10 điểm`;
            if (progressEl) progressEl.style.width = percent + '%';

            if (percent >= 80) {
                if (titleEl) titleEl.innerText = "🎉 Xuất sắc! Nắm vững kiến thức";
                if (feedbackEl) feedbackEl.innerText = `Bạn đã trả lời đúng ${correctCount}/${total} câu hỏi.`;
                if (iconEl) iconEl.innerHTML = '<i class="bi bi-trophy-fill text-warning fs-1"></i>';
                if (progressEl) progressEl.className = 'progress-bar progress-bar-striped bg-success';
                triggerConfetti();
            } else if (percent >= 50) {
                if (titleEl) titleEl.innerText = "👍 Khá tốt! Đạt yêu cầu cơ bản";
                if (feedbackEl) feedbackEl.innerText = `Bạn đã trả lời đúng ${correctCount}/${total} câu hỏi.`;
                if (iconEl) iconEl.innerHTML = '<i class="bi bi-award-fill text-info fs-1"></i>';
                if (progressEl) progressEl.className = 'progress-bar progress-bar-striped bg-info';
            } else {
                if (titleEl) titleEl.innerText = "📚 Cần ôn tập lại lý thuyết";
                if (feedbackEl) feedbackEl.innerText = `Bạn đã trả lời đúng ${correctCount}/${total} câu hỏi. Hãy xem lại phần giải thích!`;
                if (iconEl) iconEl.innerHTML = '<i class="bi bi-exclamation-triangle-fill text-danger fs-1"></i>';
                if (progressEl) progressEl.className = 'progress-bar progress-bar-striped bg-danger';
            }

            if (resultCard) {
                resultCard.classList.remove('d-none');
                resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            submitBtn.disabled = true;
            renderMath(quizForm);
        });
    }

    if (retryBtn) {
        retryBtn.addEventListener('click', function() {
            questionCards.forEach(card => {
                const qId = card.dataset.questionId;
                const explanationBox = document.getElementById(`explanation-${qId}`);
                if (explanationBox) explanationBox.classList.add('d-none');
                card.querySelectorAll('input[type="radio"]').forEach(r => {
                    r.disabled = false;
                    r.checked = false;
                });
                card.querySelectorAll('.option-label').forEach(l => {
                    l.className = 'option-label p-3 rounded-3 border d-flex align-items-center gap-3 cursor-pointer transition-all';
                });
            });

            if (resultCard) resultCard.classList.add('d-none');
            if (submitBtn) submitBtn.disabled = false;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
}

// Lazy-load confetti script on demand only when celebration triggers
function triggerConfetti() {
    if (typeof confetti === 'function') {
        confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
        return;
    }
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js';
    script.onload = function() {
        if (typeof confetti === 'function') {
            confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
        }
    };
    document.head.appendChild(script);
}

// ==========================================================================
// 9. Unified Keyboard Shortcuts (Search & Navigation)
// ==========================================================================
function initKeyboardShortcuts() {
    if (window._keyboardShortcutsInitialized) return;
    window._keyboardShortcutsInitialized = true;

    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K: Focus search
        if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
            const searchInput = document.getElementById('globalSearchInput');
            if (searchInput) {
                e.preventDefault();
                searchInput.focus();
                searchInput.select();
            }
            return;
        }

        // Alt + Left Arrow: Previous lesson
        if (e.altKey && (e.key === 'ArrowLeft' || e.key === 'Left')) {
            const prevBtn = document.getElementById('prevLessonBtn');
            if (prevBtn) {
                e.preventDefault();
                prevBtn.click();
            }
            return;
        }

        // Alt + Right Arrow: Next lesson
        if (e.altKey && (e.key === 'ArrowRight' || e.key === 'Right')) {
            const nextBtn = document.getElementById('nextLessonBtn');
            if (nextBtn) {
                e.preventDefault();
                nextBtn.click();
            }
            return;
        }
    });
}

// ==========================================================================
// 10. SPA Smooth Navigation Engine (Lazy Load Heavy Assets & History API)
// ==========================================================================
function initSpaRouter() {
    const pageCache = new Map();
    const CACHE_PREFIX = 'toan11_page_';

    function getCachedPage(key) {
        if (pageCache.has(key)) return pageCache.get(key);
        try {
            const stored = sessionStorage.getItem(CACHE_PREFIX + key);
            if (stored) {
                const data = JSON.parse(stored);
                pageCache.set(key, data);
                return data;
            }
        } catch (_) {}
        return null;
    }

    function setCachedPage(key, data) {
        pageCache.set(key, data);
        try {
            // Keep session cache within reasonable limits
            sessionStorage.setItem(CACHE_PREFIX + key, JSON.stringify(data));
        } catch (_) {}
    }

    const initialView = document.getElementById('spaViewContainer');
    const initialScripts = document.getElementById('spaScriptsContainer');
    if (initialView) {
        setCachedPage(window.location.pathname + window.location.search, {
            title: document.title,
            viewHtml: initialView.innerHTML,
            scriptsHtml: initialScripts ? initialScripts.innerHTML : '',
            timestamp: Date.now()
        });
    }

    const ProgressBar = {
        bar: document.getElementById('spaProgressBar'),
        timer: null,
        start() {
            if (!this.bar) return;
            clearTimeout(this.timer);
            this.bar.style.width = '0%';
            this.bar.classList.add('active');
            this.bar.classList.remove('done');
            this.timer = setTimeout(() => {
                if (this.bar) this.bar.style.width = '70%';
            }, 60);
        },
        finish() {
            if (!this.bar) return;
            clearTimeout(this.timer);
            this.bar.style.width = '100%';
            this.bar.classList.add('done');
            setTimeout(() => {
                if (this.bar) {
                    this.bar.classList.remove('active', 'done');
                    this.bar.style.width = '0%';
                }
            }, 300);
        }
    };

    function updateSidebarActive(targetPath, shouldScroll = true) {
        const cleanPath = targetPath.split('?')[0].split('#')[0];
        const match = cleanPath.match(/\/chapter\/(\d+)(?:\/lesson\/(\d+))?/);
        const activeChId = match ? match[1] : null;

        // If sidebar container is empty, render it
        const accordion = document.getElementById('curriculumAccordion');
        if (accordion && !accordion.children.length) {
            renderSidebar(activeChId ? parseInt(activeChId, 10) : 1);
        }

        const sidebarLinks = document.querySelectorAll('.sidebar-column a, #sidebarOffcanvas a');
        let activeLink = null;

        sidebarLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href) return;
            const linkPath = href.split('?')[0].split('#')[0];

            if (linkPath === cleanPath) {
                link.classList.add('active');
                activeLink = link;
            } else {
                link.classList.remove('active');
            }
        });

        if (activeChId) {
            document.querySelectorAll('.sidebar-accordion-collapse').forEach(c => {
                const id = c.getAttribute('data-chapter-id');
                if (id === activeChId) {
                    c.classList.add('show');
                } else {
                    c.classList.remove('show');
                }
            });
            document.querySelectorAll('.sidebar-ch-btn').forEach(btn => {
                const id = btn.getAttribute('data-chapter-id');
                if (id === activeChId) {
                    btn.classList.remove('collapsed');
                    btn.setAttribute('aria-expanded', 'true');
                } else {
                    btn.classList.add('collapsed');
                    btn.setAttribute('aria-expanded', 'false');
                }
            });
            saveSidebarState();
        }

        if (shouldScroll && activeLink) {
            setTimeout(() => {
                activeLink.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 120);
        }

        closeMobileSidebar();
        const dropdown = document.getElementById('searchResultsDropdown');
        if (dropdown) dropdown.style.display = 'none';
    }

    // Background Prefetcher (excludes heavy 3D and exam pages to save bandwidth)
    let prefetchTimer = null;
    function prefetchPage(url) {
        const urlObj = new URL(url, window.location.origin);
        const key = urlObj.pathname + urlObj.search;
        if (pageCache.has(key)) return;

        fetch(urlObj.href, { priority: 'low' })
            .then(res => {
                if (res.ok) return res.text();
                throw new Error('Prefetch failed');
            })
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const view = doc.getElementById('spaViewContainer');
                const scripts = doc.getElementById('spaScriptsContainer');
                if (view) {
                    pageCache.set(key, {
                        title: doc.title,
                        viewHtml: view.innerHTML,
                        scriptsHtml: scripts ? scripts.innerHTML : '',
                        timestamp: Date.now()
                    });
                }
            })
            .catch(() => {});
    }

    document.addEventListener('mouseover', function(e) {
        const link = e.target.closest('a[href]');
        if (!link) return;
        const href = link.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:')) return;

        try {
            const targetUrl = new URL(href, window.location.origin);
            if (targetUrl.origin !== window.location.origin) return;
            if (targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) return;
            // Lazy load requirement: do not background-fetch 3D or exam questions on hover
            if (targetUrl.pathname.startsWith('/api/') || targetUrl.pathname === '/hinh-hoc-3d' || targetUrl.pathname.startsWith('/exam/')) return;

            prefetchTimer = setTimeout(() => {
                prefetchPage(targetUrl.href);
            }, 80);
        } catch (_) {}
    });

    document.addEventListener('mouseout', function(e) {
        const link = e.target.closest('a[href]');
        if (link && prefetchTimer) {
            clearTimeout(prefetchTimer);
            prefetchTimer = null;
        }
    });

    async function executeScriptsFromContainer(scriptsContainer) {
        if (!scriptsContainer) return;
        const scripts = Array.from(scriptsContainer.querySelectorAll('script'));

        for (const oldScript of scripts) {
            if (oldScript.src) {
                if (oldScript.src.includes('three.min.js') && window.THREE) continue;
                if (oldScript.src.includes('OrbitControls.js') && window.THREE && window.THREE.OrbitControls) continue;
                if (oldScript.src.includes('geometry3d.js')) {
                    if (window.initGeometry3D) {
                        window.initGeometry3D();
                        continue;
                    }
                }

                await new Promise((resolve) => {
                    const newScript = document.createElement('script');
                    Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
                    newScript.onload = resolve;
                    newScript.onerror = resolve;
                    document.head.appendChild(newScript);
                });
            } else {
                try {
                    const newScript = document.createElement('script');
                    Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
                    newScript.textContent = oldScript.textContent;
                    document.body.appendChild(newScript);
                    newScript.remove();
                } catch (scriptErr) {
                    console.warn('Inline script execution warning:', scriptErr);
                }
            }
        }
    }

    async function navigateTo(url, isPopState = false) {
        const targetUrl = new URL(url, window.location.origin);
        const cacheKey = targetUrl.pathname + targetUrl.search;

        if (!isPopState && targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) {
            if (targetUrl.hash) {
                const targetEl = document.querySelector(targetUrl.hash);
                if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth' });
            }
            return;
        }

        updateSidebarActive(targetUrl.pathname, true);

        // Strict Resource Management: Cleanup 3D scene & cancel requestAnimationFrame before navigating away
        if (targetUrl.pathname !== '/hinh-hoc-3d' && window.cleanupGeometry3D) {
            try { window.cleanupGeometry3D(); } catch (_) {}
        }

        ProgressBar.start();

        try {
            let pageData = getCachedPage(cacheKey);

            if (!pageData) {
                const response = await fetch(targetUrl.href);
                if (!response.ok) {
                    window.location.href = targetUrl.href;
                    return;
                }
                const html = await response.text();
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const view = doc.getElementById('spaViewContainer');
                const scripts = doc.getElementById('spaScriptsContainer');

                if (!view) {
                    window.location.href = targetUrl.href;
                    return;
                }

                pageData = {
                    title: doc.title,
                    viewHtml: view.innerHTML,
                    scriptsHtml: scripts ? scripts.innerHTML : '',
                    timestamp: Date.now()
                };
                setCachedPage(cacheKey, pageData);
            }

            if (!isPopState) {
                history.pushState({ url: targetUrl.href }, '', targetUrl.href);
            }

            const viewContainer = document.getElementById('spaViewContainer');
            const scriptsContainer = document.getElementById('spaScriptsContainer');

            const performDomSwap = () => {
                document.title = pageData.title;
                if (viewContainer) {
                    viewContainer.innerHTML = pageData.viewHtml;
                }
                if (scriptsContainer) {
                    scriptsContainer.innerHTML = pageData.scriptsHtml;
                }
                window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
            };

            if (document.startViewTransition) {
                const transition = document.startViewTransition(performDomSwap);
                await transition.finished;
            } else {
                if (viewContainer) {
                    viewContainer.classList.add('spa-fade-out');
                    await new Promise(r => setTimeout(r, 90));
                    performDomSwap();
                    viewContainer.classList.remove('spa-fade-out');
                    viewContainer.classList.add('spa-fade-in');
                    setTimeout(() => viewContainer.classList.remove('spa-fade-in'), 180);
                } else {
                    performDomSwap();
                }
            }

            try {
                await executeScriptsFromContainer(scriptsContainer);
            } catch (scriptErr) {
                console.warn('SPA Script Execution Warning:', scriptErr);
            }

            renderMath(viewContainer);

            try { initProgress(); } catch (_) {}
            try { initContinueLearning(); } catch (_) {}
            try { initQuiz(); } catch (_) {}

            // Lazy initialization: 3D scene only runs when user visits /hinh-hoc-3d
            if (targetUrl.pathname === '/hinh-hoc-3d') {
                if (window.initGeometry3D) {
                    try { window.initGeometry3D(); } catch (_) {}
                }
            }

        } catch (err) {
            console.error('SPA Navigation Error:', err);
            if (!isPopState) {
                window.location.href = targetUrl.href;
            }
        } finally {
            ProgressBar.finish();
        }
    }

    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (!link) return;

        if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
        if (link.target && link.target !== '_self') return;
        if (link.hasAttribute('download')) return;

        const href = link.getAttribute('href');
        if (!href) return;
        if (href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:') || href.startsWith('tel:')) return;

        try {
            const targetUrl = new URL(href, window.location.origin);
            if (targetUrl.origin !== window.location.origin) return;
            if (targetUrl.pathname.startsWith('/api/') || targetUrl.pathname === '/health' || targetUrl.pathname === '/healthz') return;

            e.preventDefault();
            navigateTo(targetUrl.href);
        } catch (_) {}
    });

    window.addEventListener('popstate', function() {
        if (window.location.pathname !== '/hinh-hoc-3d' && window.cleanupGeometry3D) {
            try { window.cleanupGeometry3D(); } catch (_) {}
        }
        navigateTo(window.location.href, true);
    });
}

// ==========================================================================
// 11. Application Lifecycle Initialization
// ==========================================================================
document.addEventListener("DOMContentLoaded", function() {
    initTheme();
    renderSidebar();
    initSidebarEventDelegation();
    initSidebarScrollTracking();
    initProgress();
    initContinueLearning();
    initSearch();
    initQuiz();
    initKeyboardShortcuts();
    initSpaRouter();
    renderMath();
});
