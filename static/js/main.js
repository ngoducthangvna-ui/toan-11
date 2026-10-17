/**
 * Main JavaScript for TOAN 11 MASTER
 * Handles Dark Mode, Learning Progress, Quick Check, Live Search Filter, Interactive Quiz Engine, and SPA Router
 */

// Monkey-patch document.addEventListener for DOMContentLoaded to support dynamic SPA scripts
const _originalAddEventListener = document.addEventListener;
document.addEventListener = function(type, listener, options) {
    if (type === 'DOMContentLoaded' && document.readyState !== 'loading') {
        setTimeout(listener, 1);
        return;
    }
    return _originalAddEventListener.call(this, type, listener, options);
};

/* ==========================================================================
   Global Toast & Ultra-Fast Math Rendering Helpers
   ========================================================================== */
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

function renderMath(container) {
    if (!container) container = document.body;
    // 1. Try KaTeX auto-render first (Fastest, zero FOUC)
    if (window.renderMathInElement) {
        try {
            window.renderMathInElement(container, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '\\[', right: '\\]', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false }
                ],
                throwOnError: false,
                ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"]
            });
            return;
        } catch (_) {}
    }
    // 2. MathJax 3 fallback
    if (window.MathJax && window.MathJax.typesetPromise) {
        try {
            window.MathJax.typesetClear && window.MathJax.typesetClear([container]);
            window.MathJax.typesetPromise([container]).catch(() => {});
        } catch (_) {}
    }
}

document.addEventListener("DOMContentLoaded", function() {
    initTheme();
    initProgress();
    initContinueLearning();
    initSearch();
    initQuiz();
    initSidebarAccordion();
    initSidebarScrollTracking();
    initKeyboardShortcuts();
    initSpaRouter();
    renderMath();
});

/* ==========================================================================
   1. Theme Management (Dark / Light Mode)
   ========================================================================== */
function initTheme() {
    const themeBtn = document.getElementById('themeToggleBtn');
    const themeIcon = document.getElementById('themeIcon');
    const savedTheme = localStorage.getItem('toan11_theme') || 'light';

    document.documentElement.setAttribute('data-bs-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeBtn) {
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

/* ==========================================================================
   2. Progress Tracker & Chapter Card Sync (Local Storage)
   ========================================================================== */
function initProgress() {
    const STORAGE_KEY = 'toan11_completed_lessons';
    let completedLessons = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    updateProgressUI();

    // Mark complete button on lesson page
    const markBtn = document.getElementById('markCompleteBtn');
    if (markBtn) {
        const lessonId = markBtn.dataset.lessonId;
        const markText = document.getElementById('markCompleteText');

        if (completedLessons.includes(lessonId)) {
            setBtnCompleted(true);
        }

        if (!markBtn.dataset.bound) {
            markBtn.dataset.bound = 'true';
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
        }

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

    // Reset progress button
    const resetBtn = document.getElementById('resetProgressBtn');
    if (resetBtn) {
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
        const totalLessons = 29; // Total across all 9 chapters
        const count = completedLessons.length;
        const percent = Math.min(100, Math.round((count / totalLessons) * 100));

        const bar = document.getElementById('overallProgressBar');
        const text = document.getElementById('overallProgressText');
        const counter = document.getElementById('completedLessonsCount');

        if (bar) bar.style.width = percent + '%';
        if (text) text.innerText = percent + '%';
        if (counter) counter.innerText = `${count}/${totalLessons} bài`;

        // Update checkmarks in sidebar
        document.querySelectorAll('.lesson-check-icon').forEach(icon => {
            const link = icon.closest('a');
            if (link && link.dataset.lessonId) {
                if (completedLessons.includes(link.dataset.lessonId)) {
                    icon.classList.remove('d-none');
                } else {
                    icon.classList.add('d-none');
                }
            }
        });
    }
}

/* ==========================================================================
   3. Continue Learning Feature (localStorage: toan11_last_lesson & lastVisitedLesson)
   ========================================================================== */
function initContinueLearning() {
    const LAST_LESSON_KEY = 'toan11_last_lesson';
    const COMPLETED_KEY = 'toan11_completed_lessons';
    let completedLessons = [];
    try {
        completedLessons = JSON.parse(localStorage.getItem(COMPLETED_KEY) || '[]');
    } catch (_) {
        completedLessons = [];
    }
    let savedLast = null;
    try {
        savedLast = localStorage.getItem(LAST_LESSON_KEY) || localStorage.getItem('lastVisitedLesson');
    } catch (_) {
        savedLast = null;
    }

    // 1. If currently on a lesson page, save it as the latest lesson
    if (window.location.pathname.includes('/lesson/')) {
        const titleEl = document.querySelector('h1.display-6, .lesson-header h1, h1');
        const lessonTitle = titleEl ? titleEl.innerText.trim() : 'Bài học gần nhất';
        const currentData = {
            title: lessonTitle,
            url: window.location.pathname
        };
        try {
            localStorage.setItem(LAST_LESSON_KEY, JSON.stringify(currentData));
            localStorage.setItem('lastVisitedLesson', JSON.stringify(currentData));
        } catch (_) {}
    }

    // 2. Global listener: when user clicks on any lesson link, remember it
    document.addEventListener('click', function(e) {
        const lessonLink = e.target.closest('[data-lesson-id]');
        if (lessonLink && lessonLink.getAttribute('href')) {
            const title = lessonLink.dataset.lessonTitle || lessonLink.innerText.trim();
            const url = lessonLink.getAttribute('href');
            if (url && url !== '#') {
                const data = { title: title, url: url };
                try {
                    localStorage.setItem(LAST_LESSON_KEY, JSON.stringify(data));
                    localStorage.setItem('lastVisitedLesson', JSON.stringify(data));
                } catch (_) {}
            }
        }
    });

    // 3. On Homepage: Smart CTA logic
    const heroPrimaryBtn = document.getElementById('heroPrimaryBtn');
    const heroBtnText = document.getElementById('heroPrimaryBtnText');
    if (heroPrimaryBtn && heroBtnText) {
        // New user condition: no completed lessons AND no visited lesson yet
        if (completedLessons.length === 0 && !savedLast) {
            heroPrimaryBtn.href = '/chapter/1/lesson/1';
            heroBtnText.innerText = 'Bắt đầu học ngay: Chương 1 - Bài 1';
            heroPrimaryBtn.className = 'btn hero-btn-primary btn-lg px-4 fw-bold d-inline-flex align-items-center justify-content-center gap-2 shadow-sm';
        } else if (savedLast) {
            try {
                const lastLesson = JSON.parse(savedLast);
                if (lastLesson && lastLesson.url && lastLesson.title) {
                    heroPrimaryBtn.href = lastLesson.url;
                    let displayTitle = lastLesson.title;
                    if (displayTitle.length > 36) {
                        displayTitle = displayTitle.substring(0, 34) + '...';
                    }
                    heroBtnText.innerText = `Học tiếp: ${displayTitle}`;
                    heroPrimaryBtn.className = 'btn hero-btn-primary btn-lg px-4 fw-bold d-inline-flex align-items-center justify-content-center gap-2 shadow-sm';
                    heroPrimaryBtn.title = `Học tiếp: ${lastLesson.title}`;
                }
            } catch (err) {
                heroPrimaryBtn.href = '/chapter/1/lesson/1';
                heroBtnText.innerText = 'Bắt đầu học ngay: Chương 1 - Bài 1';
                heroPrimaryBtn.className = 'btn hero-btn-primary btn-lg px-4 fw-bold d-inline-flex align-items-center justify-content-center gap-2 shadow-sm';
            }
        }
    }
}

/* ==========================================================================
   4. Live Search & Filter (with Ctrl+K Shortcut)
   ========================================================================== */
function initSearch() {
    const searchInput = document.getElementById('globalSearchInput');
    const dropdown = document.getElementById('searchResultsDropdown');
    const homeAlert = document.getElementById('homeSearchAlert');
    const homeKeyword = document.getElementById('homeSearchKeyword');
    const clearHomeBtn = document.getElementById('clearHomeSearchBtn');
    const isHomepage = document.querySelector('.homepage-container') !== null;

    if (!searchInput) return;

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

    // Keyboard shortcut: Ctrl + K or Cmd + K
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
            e.preventDefault();
            searchInput.focus();
            searchInput.select();
        }
        if (e.key === 'Escape' && dropdown) {
            dropdown.style.display = 'none';
        }
    });

    // Keyboard navigation within search input
    searchInput.addEventListener('keydown', function(e) {
        if (!dropdown || dropdown.style.display !== 'block') return;
        const items = dropdown.querySelectorAll('.dropdown-item');
        if (!items.length) return;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            const nextIdx = (selectedSearchIdx + 1) % items.length;
            highlightSearchItem(nextIdx);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            const prevIdx = (selectedSearchIdx - 1 + items.length) % items.length;
            highlightSearchItem(prevIdx);
        } else if (e.key === 'Enter') {
            if (selectedSearchIdx >= 0 && items[selectedSearchIdx]) {
                e.preventDefault();
                items[selectedSearchIdx].click();
                dropdown.style.display = 'none';
                searchInput.blur();
            }
        }
    });

    let debounceTimer;
    searchInput.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        const query = this.value.trim();

        debounceTimer = setTimeout(async () => {
            // 1. Live Filter on Homepage Cards
            if (isHomepage) {
                filterHomepageCards(query);
            }

            // 2. Dropdown search suggestion via API
            if (query.length < 2) {
                if (dropdown) {
                    dropdown.style.display = 'none';
                    dropdown.innerHTML = '';
                    selectedSearchIdx = -1;
                }
                return;
            }

            try {
                const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
                const data = await res.json();
                renderSearchResults(data.results);
            } catch (err) {
                console.error("Search error:", err);
            }
        }, 180);
    });

    // Helper: Vietnamese search normalization (remove accents)
    function removeAccents(str) {
        if (!str) return '';
        return str.normalize('NFD')
                  .replace(/[\u0300-\u036f]/g, '')
                  .replace(/đ/g, 'd')
                  .replace(/Đ/g, 'D')
                  .toLowerCase();
    }

    // Filter Homepage Chapter Cards
    function filterHomepageCards(rawQuery) {
        const query = removeAccents(rawQuery.trim());
        const chapterCols = document.querySelectorAll('.chapter-card-col');

        if (!query) {
            chapterCols.forEach(col => {
                col.classList.remove('d-none', 'search-matched');
            });
            if (homeAlert) homeAlert.classList.add('d-none');
            return;
        }

        let matchCount = 0;
        chapterCols.forEach(col => {
            const content = removeAccents(col.getAttribute('data-search-content') || col.innerText);
            if (content.includes(query)) {
                col.classList.remove('d-none');
                col.classList.add('search-matched');
                matchCount++;
            } else {
                col.classList.add('d-none');
                col.classList.remove('search-matched');
            }
        });

        if (homeAlert && homeKeyword) {
            homeKeyword.innerText = rawQuery;
            homeAlert.classList.remove('d-none');
        }
    }

    if (clearHomeBtn) {
        clearHomeBtn.addEventListener('click', function() {
            searchInput.value = '';
            filterHomepageCards('');
            if (dropdown) dropdown.style.display = 'none';
            searchInput.focus();
        });
    }

    function renderSearchResults(results) {
        if (!dropdown) return;
        selectedSearchIdx = -1;

        if (!results || results.length === 0) {
            dropdown.innerHTML = '<div class="p-3 text-center text-muted small"><i class="bi bi-emoji-neutral me-1"></i> Không tìm thấy bài học phù hợp</div>';
            dropdown.style.display = 'block';
            return;
        }

        let html = '<div class="py-1">';
        results.forEach(item => {
            const icon = item.type === 'chapter' ? 'bi-journal-richtext text-primary' : 'bi-file-earmark-text text-success';
            html += `
                <a href="${item.url}" class="dropdown-item py-2 px-3 d-flex align-items-center gap-2 rounded-2">
                    <i class="bi ${icon} fs-5 flex-shrink-0"></i>
                    <div class="text-truncate">
                        <div class="fw-semibold small text-truncate text-body">${item.title}</div>
                        <div class="text-muted small text-truncate" style="font-size: 0.75rem;">${item.subtitle}</div>
                    </div>
                </a>
            `;
        });
        html += '</div>';
        dropdown.innerHTML = html;
        dropdown.style.display = 'block';

        dropdown.querySelectorAll('.dropdown-item').forEach((item, i) => {
            item.addEventListener('mouseenter', () => highlightSearchItem(i));
        });
    }

    // Close on outside click
    document.addEventListener('click', function(e) {
        if (dropdown && !searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
}

/* ==========================================================================
   5. Interactive Quiz Engine
   ========================================================================== */
function initQuiz() {
    const quizForm = document.getElementById('quizForm');
    if (!quizForm) return;

    const questionCards = document.querySelectorAll('.question-card');
    const submitBtn = document.getElementById('submitQuizBtn');
    const resultCard = document.getElementById('quizResultCard');
    const retryBtn = document.getElementById('retryQuizBtn');

    // Radio option selection highlighting
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

    // Submit and Grade
    if (submitBtn) {
        submitBtn.addEventListener('click', function() {
        let correctCount = 0;
        const total = questionCards.length;
        let unanswered = 0;

        // Check for unanswered
        questionCards.forEach(card => {
            const checked = card.querySelector('input[type="radio"]:checked');
            if (!checked) unanswered++;
        });

        if (unanswered > 0) {
            const confirmSubmit = confirm(`Bạn còn ${unanswered} câu chưa làm. Bạn có chắc chắn muốn nộp bài luôn không?`);
            if (!confirmSubmit) return;
        }

        // Process answers
        questionCards.forEach((card, idx) => {
            const correctVal = parseInt(card.dataset.correct);
            const qId = card.dataset.questionId;
            const checked = card.querySelector('input[type="radio"]:checked');
            const explanationBox = document.getElementById(`explanation-${qId}`);
            const statusBox = explanationBox.querySelector('.explanation-status');
            const labels = card.querySelectorAll('.option-label');

            // Disable all radios
            card.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);

            // Highlight the truly correct answer
            if (labels[correctVal]) {
                labels[correctVal].classList.add('correct-choice');
            }

            if (checked) {
                const userVal = parseInt(checked.value);
                if (userVal === correctVal) {
                    correctCount++;
                    statusBox.innerHTML = '<span class="badge bg-success"><i class="bi bi-check-lg"></i> Chính xác!</span>';
                } else {
                    if (labels[userVal]) labels[userVal].classList.add('wrong-choice');
                    statusBox.innerHTML = '<span class="badge bg-danger"><i class="bi bi-x-lg"></i> Chưa chính xác</span>';
                }
            } else {
                statusBox.innerHTML = '<span class="badge bg-secondary"><i class="bi bi-dash-circle"></i> Chưa trả lời</span>';
            }

            // Reveal explanation
            explanationBox.classList.remove('d-none');
        });

        // Calculate score on 10-point scale
        const score = ((correctCount / total) * 10).toFixed(1);
        const percent = Math.round((correctCount / total) * 100);

        // Save best score to localStorage
        try {
            const quizPage = document.querySelector('.quiz-page');
            const chapterId = quizPage?.dataset?.chapterId || (window.location.pathname.match(/\/chapter\/(\d+)\/quiz/)?.[1]);
            if (chapterId) {
                const scores = JSON.parse(localStorage.getItem('toan11_chapter_scores') || '{}');
                const numScore = parseFloat(score);
                const prevBest = parseFloat(scores[chapterId] || 0);
                if (numScore > prevBest) {
                    scores[chapterId] = numScore;
                    localStorage.setItem('toan11_chapter_scores', JSON.stringify(scores));
                }
            }
        } catch (e) {
            console.error('Error saving chapter score:', e);
        }

        // Update Result Banner
        document.getElementById('resultScore').innerText = `${score} / 10 điểm`;
        document.getElementById('resultProgressBar').style.width = percent + '%';

        const resultTitle = document.getElementById('resultTitle');
        const resultFeedback = document.getElementById('resultFeedback');
        const resultIcon = document.getElementById('resultIcon');

        if (percent >= 80) {
            resultTitle.innerText = "🎉 Xuất sắc! Nắm vững kiến thức";
            resultFeedback.innerText = `Bạn đã trả lời đúng ${correctCount}/${total} câu hỏi. Hãy tiếp tục phát huy ở các chương tiếp theo!`;
            resultIcon.innerHTML = '<i class="bi bi-trophy-fill text-warning fs-1"></i>';
            document.getElementById('resultProgressBar').className = 'progress-bar progress-bar-striped bg-success';
            // Trigger confetti!
            if (typeof confetti === 'function') {
                confetti({
                    particleCount: 120,
                    spread: 80,
                    origin: { y: 0.6 }
                });
            }
        } else if (percent >= 50) {
            resultTitle.innerText = "👍 Khá tốt! Đạt yêu cầu cơ bản";
            resultFeedback.innerText = `Bạn đã trả lời đúng ${correctCount}/${total} câu hỏi. Hãy xem lại lời giải chi tiết cho các câu sai bên dưới nhé.`;
            resultIcon.innerHTML = '<i class="bi bi-award-fill text-primary fs-1"></i>';
            document.getElementById('resultProgressBar').className = 'progress-bar progress-bar-striped bg-primary';
        } else {
            resultTitle.innerText = "💪 Cố gắng thêm nhé!";
            resultFeedback.innerText = `Bạn đạt ${correctCount}/${total} câu. Hãy đọc lại lý thuyết của chương và bấm "Làm lại bài kiểm tra" để cải thiện điểm số.`;
            resultIcon.innerHTML = '<i class="bi bi-patch-exclamation-fill text-danger fs-1"></i>';
            document.getElementById('resultProgressBar').className = 'progress-bar progress-bar-striped bg-warning';
        }

        resultCard.classList.remove('d-none');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="bi bi-check-all"></i> Đã nộp bài';

        // Smooth scroll up to result card
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

        // Typeset explanations with MathJax (scoped)
        if (window.MathJax && MathJax.typesetPromise) {
            const quizContainer = document.getElementById('quizForm') || document.querySelector('.quiz-page');
            MathJax.typesetPromise(quizContainer ? [quizContainer] : []).catch(() => {});
        }
        });
    }

    // Retry Quiz
    if (retryBtn) {
        retryBtn.addEventListener('click', function() {
            questionCards.forEach(card => {
                const qId = card.dataset.questionId;
                const explanationBox = document.getElementById(`explanation-${qId}`);
                explanationBox.classList.add('d-none');

                card.querySelectorAll('input[type="radio"]').forEach(r => {
                    r.disabled = false;
                    r.checked = false;
                });

                card.querySelectorAll('.option-label').forEach(l => {
                    l.className = 'option-label p-3 rounded-3 border d-flex align-items-center gap-3 cursor-pointer transition-all';
                });
            });

            resultCard.classList.add('d-none');
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<i class="bi bi-send-check-fill"></i> Nộp bài & Chấm điểm';

            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
}

function initKeyboardShortcuts() {
    if (window._keyboardShortcutsInitialized) return;
    window._keyboardShortcutsInitialized = true;

    document.addEventListener('keydown', function(e) {
        // Alt + Left Arrow: Previous lesson
        if (e.altKey && (e.key === 'ArrowLeft' || e.key === 'Left')) {
            const prevBtn = document.getElementById('prevLessonBtn');
            if (prevBtn) {
                e.preventDefault();
                prevBtn.click();
            }
        }
        // Alt + Right Arrow: Next lesson
        else if (e.altKey && (e.key === 'ArrowRight' || e.key === 'Right')) {
            const nextBtn = document.getElementById('nextLessonBtn');
            if (nextBtn) {
                e.preventDefault();
                nextBtn.click();
            }
        }
    });
}

/* ==========================================================================
   7. Sidebar 60fps Accordion & Smart LocalStorage Persistence
   ========================================================================== */
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

function initSidebarAccordion() {
    // 1. Restore state from localStorage & auto-expand active chapter
    try {
        let openIds = [];
        const saved = localStorage.getItem('toan11_open_chapters') || sessionStorage.getItem('toan11_open_chapters');
        if (saved) {
            try { openIds = JSON.parse(saved); } catch (_) { openIds = []; }
        }

        // Detect active chapter from URL e.g. /chapter/2 or /chapter/2/lesson/1
        const pathMatch = window.location.pathname.match(/\/chapter\/(\d+)/);
        if (pathMatch && pathMatch[1]) {
            const activeChId = String(pathMatch[1]);
            if (!openIds.includes(activeChId)) {
                openIds.push(activeChId);
            }
        } else if (!saved) {
            // First time visit on homepage: open Chapter 1 by default
            openIds = ['1'];
        }

        // Apply state across both desktop & offcanvas mobile sidebars
        document.querySelectorAll('.sidebar-accordion-collapse').forEach(collapseEl => {
            const chId = collapseEl.getAttribute('data-chapter-id');
            const targetId = collapseEl.id;
            const buttons = document.querySelectorAll(
                `.sidebar-ch-btn[data-chapter-target="${targetId}"], .sidebar-ch-btn[data-chapter-id="${chId}"]`
            );
            const isOpen = openIds.includes(String(chId)) || openIds.includes(Number(chId));

            if (isOpen) {
                collapseEl.classList.add('show');
                buttons.forEach(btn => {
                    btn.classList.remove('collapsed');
                    btn.setAttribute('aria-expanded', 'true');
                });
            } else {
                collapseEl.classList.remove('show');
                buttons.forEach(btn => {
                    btn.classList.add('collapsed');
                    btn.setAttribute('aria-expanded', 'false');
                });
            }
        });

        saveSidebarState();
    } catch (e) {
        console.warn('Sidebar state initialization error:', e);
    }

    // 2. Delegate click handler on entire chapter header (including native chevron & icons)
    if (window._sidebarAccordionBound) return;
    window._sidebarAccordionBound = true;

    document.addEventListener('click', function(e) {
        const header = e.target.closest('.accordion-header') || e.target.closest('.sidebar-ch-btn');
        if (!header) return;

        const btn = header.classList.contains('sidebar-ch-btn') ? header : header.querySelector('.sidebar-ch-btn');
        if (!btn) return;

        e.preventDefault();
        e.stopPropagation();

        const chapterId = btn.getAttribute('data-chapter-id') || 
                          btn.closest('.accordion-item')?.getAttribute('data-chapter-id');
        const targetId = btn.getAttribute('data-chapter-target') || (chapterId ? `collapse-ch-${chapterId}` : null);
        if (!targetId && !chapterId) return;

        // Locate target collapse container in the current accordion-item
        const accordionItem = btn.closest('.accordion-item');
        const targetCollapse = accordionItem ? 
            accordionItem.querySelector('.sidebar-accordion-collapse') : 
            (targetId ? document.getElementById(targetId) : null);
            
        if (!targetCollapse) return;

        const isCurrentlyOpen = targetCollapse.classList.contains('show');
        const nextState = !isCurrentlyOpen;

        // Toggle state across both desktop & offcanvas mobile instances of this chapter
        const collSelector = chapterId ? 
            `.sidebar-accordion-collapse[data-chapter-id="${chapterId}"]` : 
            `#${targetId}`;
        const btnSelector = chapterId ? 
            `.sidebar-ch-btn[data-chapter-id="${chapterId}"]` : 
            `[data-chapter-target="${targetId}"]`;

        document.querySelectorAll(collSelector).forEach(c => {
            if (nextState) {
                c.classList.add('show');
            } else {
                c.classList.remove('show');
            }
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
    });
}

function initSidebarScrollTracking() {
    const desktop = document.getElementById('desktopSidebar');
    if (!desktop) return;
    const scroller = desktop;

    let scrollTimeout = null;
    scroller.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            try {
                localStorage.setItem('toan11_sidebar_scroll', scroller.scrollTop);
                sessionStorage.setItem('toan11_sidebar_scroll', scroller.scrollTop);
            } catch (_) {}
        }, 60);
    }, { passive: true });
}

/* ==========================================================================
   8. SPA Smooth Navigation Engine (Fetch API + History API + View Transitions)
   ========================================================================== */
function initSpaRouter() {
    // 1. In-memory Cache: url -> { title, viewHtml, scriptsHtml, timestamp }
    const pageCache = new Map();

    // Cache initial page on load
    const initialView = document.getElementById('spaViewContainer');
    const initialScripts = document.getElementById('spaScriptsContainer');
    if (initialView) {
        pageCache.set(window.location.pathname + window.location.search, {
            title: document.title,
            viewHtml: initialView.innerHTML,
            scriptsHtml: initialScripts ? initialScripts.innerHTML : '',
            timestamp: Date.now()
        });
    }

    // 2. Top Progress Bar Controller (Only appears if network takes > 120ms)
    const ProgressBar = {
        timer: null,
        bar: document.getElementById('spaProgressBar'),
        start() {
            if (!this.bar) this.bar = document.getElementById('spaProgressBar');
            if (!this.bar) return;
            clearTimeout(this.timer);
            this.bar.classList.remove('done');
            this.bar.style.width = '0%';
            this.timer = setTimeout(() => {
                this.bar.classList.add('active');
                this.bar.style.width = '35%';
                setTimeout(() => {
                    if (this.bar.classList.contains('active')) {
                        this.bar.style.width = '75%';
                    }
                }, 200);
            }, 120);
        },
        finish() {
            clearTimeout(this.timer);
            if (!this.bar) return;
            if (this.bar.classList.contains('active')) {
                this.bar.style.width = '100%';
                this.bar.classList.add('done');
                setTimeout(() => {
                    this.bar.classList.remove('active', 'done');
                    this.bar.style.width = '0%';
                }, 300);
            }
        }
    };

    // 3. Instant Sidebar Active State Updater
    function updateSidebarActive(targetPath, shouldScroll = true) {
        const cleanPath = targetPath.split('?')[0].split('#')[0];
        const sidebarLinks = document.querySelectorAll('.sidebar-column a, #sidebarOffcanvas a');
        let activeLink = null;

        sidebarLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href) return;
            const linkPath = href.split('?')[0].split('#')[0];

            if (linkPath === cleanPath) {
                link.classList.add('active');
                activeLink = link;
                if (link.href.includes('/quiz')) {
                    link.classList.add('text-white', 'bg-danger');
                    link.classList.remove('bg-danger-subtle');
                }
            } else {
                link.classList.remove('active');
                if (link.href.includes('/quiz')) {
                    link.classList.remove('text-white', 'bg-danger');
                    link.classList.add('bg-danger-subtle');
                }
            }
        });

        // Smart Chapter Accordion Sync: Open active chapter, collapse other chapters
        if (activeLink) {
            const collapseEl = activeLink.closest('.sidebar-accordion-collapse');
            if (collapseEl) {
                const activeChId = collapseEl.getAttribute('data-chapter-id');
                if (activeChId) {
                    // Open active chapter across desktop & mobile
                    document.querySelectorAll(`.sidebar-accordion-collapse[data-chapter-id="${activeChId}"]`).forEach(c => c.classList.add('show'));
                    document.querySelectorAll(`.sidebar-ch-btn[data-chapter-id="${activeChId}"], .sidebar-ch-btn[data-chapter-target="collapse-ch-${activeChId}"]`).forEach(btn => {
                        btn.classList.remove('collapsed');
                        btn.setAttribute('aria-expanded', 'true');
                    });

                    saveSidebarState();
                }
            }

            // Smooth scroll into view inside desktop sidebar
            if (shouldScroll) {
                setTimeout(() => {
                    const desktopActive = document.querySelector('#desktopSidebar a.active');
                    if (desktopActive) {
                        desktopActive.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }, 120);
            }
        }

        // Close mobile offcanvas if open
        const offcanvasEl = document.getElementById('sidebarOffcanvas');
        if (offcanvasEl && offcanvasEl.classList.contains('show')) {
            try {
                const offcanvasInstance = bootstrap.Offcanvas.getInstance(offcanvasEl);
                if (offcanvasInstance) offcanvasInstance.hide();
            } catch (_) {}
        }

        // Close search dropdown if open
        const dropdown = document.getElementById('searchResultsDropdown');
        if (dropdown) dropdown.style.display = 'none';
    }

    // 4. Background Prefetcher (Low-priority fetch with 60ms hover debounce)
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
            if (targetUrl.pathname.startsWith('/api/')) return;

            prefetchTimer = setTimeout(() => {
                prefetchPage(targetUrl.href);
            }, 60);
        } catch (_) {}
    });

    document.addEventListener('mouseout', function(e) {
        const link = e.target.closest('a[href]');
        if (link && prefetchTimer) {
            clearTimeout(prefetchTimer);
            prefetchTimer = null;
        }
    });

    // 5. Script Re-Execution Helper
    async function executeScriptsFromContainer(scriptsContainer) {
        if (!scriptsContainer) return;
        const scripts = Array.from(scriptsContainer.querySelectorAll('script'));

        for (const oldScript of scripts) {
            if (oldScript.src) {
                // Skip re-downloading large external libs if already in window
                if (oldScript.src.includes('three.min.js') && window.THREE) continue;
                if (oldScript.src.includes('OrbitControls.js') && window.THREE && window.THREE.OrbitControls) continue;
                if (oldScript.src.includes('geometry3d.js')) {
                    if (window.initGeometry3D) {
                        window.initGeometry3D();
                        continue;
                    }
                }

                // Sequential load for new external scripts
                await new Promise((resolve) => {
                    const newScript = document.createElement('script');
                    Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
                    newScript.onload = resolve;
                    newScript.onerror = resolve;
                    document.head.appendChild(newScript);
                });
            } else {
                // Inline script execution
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

    // 6. Navigation Logic with View Transitions
    let isNavigating = false;
    async function navigateTo(url, isPopState = false) {
        const targetUrl = new URL(url, window.location.origin);
        const cacheKey = targetUrl.pathname + targetUrl.search;

        // If clicking on current URL without hash difference, no-op
        if (!isPopState && targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) {
            if (targetUrl.hash) {
                const targetEl = document.querySelector(targetUrl.hash);
                if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth' });
            }
            return;
        }

        // 1. Instant active feedback on sidebar with smooth auto-scroll
        updateSidebarActive(targetUrl.pathname, true);

        // 2. Cleanup 3D scene if leaving 3D page
        if (window.location.pathname === '/hinh-hoc-3d' && targetUrl.pathname !== '/hinh-hoc-3d') {
            if (window.cleanupGeometry3D) {
                try { window.cleanupGeometry3D(); } catch (_) {}
            }
        }

        // 3. Start top progress bar
        ProgressBar.start();
        isNavigating = true;

        try {
            let pageData = pageCache.get(cacheKey);

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
                pageCache.set(cacheKey, pageData);
            }

            // 4. Update History
            if (!isPopState) {
                history.pushState({ url: targetUrl.href }, '', targetUrl.href);
            }

            // 5. DOM Swap with View Transitions API or Fallback
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

            // 6. Execute scripts from the new page
            try {
                await executeScriptsFromContainer(scriptsContainer);
            } catch (scriptErr) {
                console.warn('SPA Script Execution Warning:', scriptErr);
            }

            // 7. Ultra-fast Math rendering (KaTeX auto-render prioritized + MathJax fallback)
            renderMath(viewContainer);

            // 8. Re-initialize global components on new DOM
            try { initProgress(); } catch (_) {}
            try { initContinueLearning(); } catch (_) {}
            try { initQuiz(); } catch (_) {}

            // 9. If navigated to 3D page, ensure 3D scene starts
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
            isNavigating = false;
            ProgressBar.finish();
        }
    }

    // 7. Global Link Interception
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

    // 8. History PopState Handler (Back / Forward buttons)
    window.addEventListener('popstate', function() {
        navigateTo(window.location.href, true);
    });
}


