/**
 * Main JavaScript for TOAN 11 MASTER
 * Handles Dark Mode, Learning Progress, Continue Learning, Live Search Filter, and Interactive Quiz Engine
 */

document.addEventListener("DOMContentLoaded", function() {
    initTheme();
    initProgress();
    initContinueLearning();
    initSearch();
    initQuiz();
    initWorkout();
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

        markBtn.addEventListener('click', function() {
            const idx = completedLessons.indexOf(lessonId);
            if (idx === -1) {
                completedLessons.push(lessonId);
                setBtnCompleted(true);
            } else {
                completedLessons.splice(idx, 1);
                setBtnCompleted(false);
            }
            localStorage.setItem(STORAGE_KEY, JSON.stringify(completedLessons));
            updateProgressUI();
        });

        function setBtnCompleted(isDone) {
            if (isDone) {
                markBtn.className = 'btn btn-success btn-sm d-inline-flex align-items-center gap-1';
                if (markText) markText.innerText = 'Đã hoàn thành bài này';
            } else {
                markBtn.className = 'btn btn-outline-success btn-sm d-inline-flex align-items-center gap-1';
                if (markText) markText.innerText = 'Đánh dấu đã học xong';
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

        // Sync progress on Homepage Chapter Cards
        document.querySelectorAll('.chapter-card-col').forEach(col => {
            const chId = col.dataset.chapterId;
            const lessonIcons = col.querySelectorAll('.lesson-card-icon');
            let chDoneCount = 0;
            const chTotal = lessonIcons.length;

            lessonIcons.forEach(icon => {
                const lesId = icon.dataset.lessonId;
                if (lesId && completedLessons.includes(lesId)) {
                    chDoneCount++;
                    icon.className = 'bi bi-check-circle-fill text-success lesson-card-icon flex-shrink-0';
                } else {
                    icon.className = 'bi bi-circle text-muted lesson-card-icon flex-shrink-0';
                }
            });

            // Update Chapter badge and progress bar
            const badge = col.querySelector('.chapter-progress-badge');
            if (badge) {
                badge.innerText = `${chDoneCount}/${chTotal} bài`;
                if (chDoneCount === chTotal && chTotal > 0) {
                    badge.className = 'badge bg-success text-white border border-success chapter-progress-badge';
                }
            }

            const chBar = col.querySelector('.chapter-progress-bar');
            if (chBar) {
                const chPercent = chTotal > 0 ? Math.round((chDoneCount / chTotal) * 100) : 0;
                chBar.style.width = chPercent + '%';
            }
        });

        // Update Chapter Quiz Best Scores from localStorage
        try {
            const chapterScores = JSON.parse(localStorage.getItem('toan11_chapter_scores') || '{}');
            document.querySelectorAll('.chapter-best-score').forEach(badge => {
                const chId = badge.dataset.chapterId;
                if (chId && chapterScores[chId] !== undefined) {
                    badge.classList.remove('d-none');
                    const scoreVal = badge.querySelector('.score-val');
                    if (scoreVal) {
                        scoreVal.innerText = `Điểm cao nhất: ${chapterScores[chId]}/10`;
                    }
                } else {
                    badge.classList.add('d-none');
                }
            });
        } catch (e) {
            console.error('Error rendering chapter scores:', e);
        }
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

/* ==========================================================================
   6. Workout Luyện Phản Xạ 15 Phút (10 Câu Nhanh)
   ========================================================================== */
function initWorkout() {
    const startBtn = document.getElementById('startWorkoutBtn');
    const container = document.getElementById('workoutContainer');
    const timerEl = document.getElementById('workoutTimer');
    const scoreEl = document.getElementById('workoutScore');
    if (!startBtn || !container) return;

    const WORKOUT_QUESTIONS = [
        { q: "Giá trị của $\\sin\\left(\\frac{\\pi}{2}\\right)$ bằng:", opts: ["0", "1", "-1", "1/2"], ans: 1 },
        { q: "Cấp số cộng có $u_1 = 3, d = 4$. Số hạng $u_2$ bằng:", opts: ["7", "12", "1", "9"], ans: 0 },
        { q: "Giá trị của $\\log_2 8$ bằng:", opts: ["2", "3", "4", "1"], ans: 1 },
        { q: "Đạo hàm của hàm số $y = x^3$ tại $x = 2$ bằng:", opts: ["6", "12", "8", "4"], ans: 1 },
        { q: "Công bội $q$ của cấp số nhân $2, 6, 18, 54$ là:", opts: ["2", "3", "4", "6"], ans: 1 },
        { q: "Giới hạn $\\lim_{n \\to \\infty} \\frac{1}{n}$ bằng:", opts: ["0", "1", "+\\infty", "Không tồn tại"], ans: 0 },
        { q: "Giá trị của $\\cos(0)$ bằng:", opts: ["0", "1", "-1", "undefined"], ans: 1 },
        { q: "Tập xác định của hàm số $y = \\sqrt{x - 3}$ là:", opts: ["$[3; +\\infty)$", "$(3; +\\infty)$", "$(-\\infty; 3]$", "$\\mathbb{R}$"], ans: 0 },
        { q: "Đạo hàm của $y = \\ln x$ (với $x > 0$) là:", opts: ["$1/x$", "$-1/x^2$", "$x$", "$e^x$"], ans: 0 },
        { q: "Góc giữa 2 đường thẳng vuông góc trong không gian bằng:", opts: ["$0^\\circ$", "$45^\\circ$", "$90^\\circ$", "$180^\\circ$"], ans: 2 }
    ];

    let currentIdx = 0;
    let score = 0;
    let timerInterval = null;

    startBtn.addEventListener('click', function() {
        currentIdx = 0;
        score = 0;
        if (scoreEl) scoreEl.innerText = "0 / 10";

        // Drift-free countdown using Date.now()
        const durationSeconds = 15 * 60;
        const endTime = Date.now() + durationSeconds * 1000;
        clearInterval(timerInterval);

        function updateWorkoutTimer() {
            const remaining = Math.max(0, Math.round((endTime - Date.now()) / 1000));
            if (remaining <= 0) {
                clearInterval(timerInterval);
                finishWorkout();
                return;
            }
            const mins = Math.floor(remaining / 60);
            const secs = remaining % 60;
            if (timerEl) {
                timerEl.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
            }
        }

        timerInterval = setInterval(updateWorkoutTimer, 1000);
        updateWorkoutTimer();

        renderQuestion();
    });

    function renderQuestion() {
        if (currentIdx >= WORKOUT_QUESTIONS.length) {
            finishWorkout();
            return;
        }

        const item = WORKOUT_QUESTIONS[currentIdx];
        let optsHtml = '';
        item.opts.forEach((opt, idx) => {
            optsHtml += `
                <button type="button" class="btn btn-outline-secondary text-start p-3 w-100 workout-opt-btn rounded-3 fw-semibold" data-idx="${idx}">
                    ${String.fromCharCode(65 + idx)}. ${opt}
                </button>
            `;
        });

        container.innerHTML = `
            <div class="workout-question-card">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge bg-primary-subtle text-primary border fw-bold">Câu ${currentIdx + 1} / 10</span>
                </div>
                <h5 class="fw-bold mb-3 text-body">${item.q}</h5>
                <div class="d-grid gap-2 mb-3">
                    ${optsHtml}
                </div>
            </div>
        `;

        if (window.MathJax && MathJax.typesetPromise) {
            MathJax.typesetPromise([container]).catch(() => {});
        }

        // Bind clicks
        container.querySelectorAll('.workout-opt-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const chosen = parseInt(this.dataset.idx);
                const allBtns = container.querySelectorAll('.workout-opt-btn');
                allBtns.forEach(b => b.disabled = true);

                if (chosen === item.ans) {
                    this.className = 'btn btn-success text-start p-3 w-100 rounded-3 fw-bold';
                    score++;
                    if (scoreEl) scoreEl.innerText = `${score} / 10`;
                } else {
                    this.className = 'btn btn-danger text-start p-3 w-100 rounded-3 fw-bold';
                    allBtns[item.ans].className = 'btn btn-success text-start p-3 w-100 rounded-3 fw-bold';
                }

                setTimeout(() => {
                    currentIdx++;
                    renderQuestion();
                }, 650);
            });
        });
    }

    function finishWorkout() {
        clearInterval(timerInterval);
        const percent = Math.round((score / 10) * 100);
        let feedback = "Hãy ôn tập thêm lý thuyết để đạt kết quả tốt hơn nhé!";
        let badgeColor = "bg-warning";
        if (percent >= 80) {
            feedback = "🎉 Quá xuất sắc! Phản xạ kiến thức 11 đỉnh cao!";
            badgeColor = "bg-success";
            if (typeof confetti === 'function') {
                confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
            }
        } else if (percent >= 50) {
            feedback = "👍 Khá tốt! Cần luyện thêm để tăng tốc độ.";
            badgeColor = "bg-primary";
        }

        container.innerHTML = `
            <div class="text-center py-4">
                <span class="badge ${badgeColor} fs-5 px-3 py-2 mb-3 rounded-pill">${score} / 10 Điểm</span>
                <h4 class="fw-bold mb-2 text-body">Hoàn thành bài luyện phản xạ!</h4>
                <p class="text-muted mb-4">${feedback}</p>
                <button type="button" id="restartWorkoutBtn" class="btn btn-warning text-dark fw-bold px-4 rounded-pill">
                    <i class="bi bi-arrow-counterclockwise me-1"></i> Luyện tập lại
                </button>
            </div>
        `;

        document.getElementById('restartWorkoutBtn')?.addEventListener('click', function() {
            startBtn.click();
        });
    }
}

