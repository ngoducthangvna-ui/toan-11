/**
 * Main JavaScript for TOAN 11 MASTER
 * Handles Dark Mode, Learning Progress, Live Search, and Interactive Quiz Engine
 */

document.addEventListener("DOMContentLoaded", function() {
    initTheme();
    initProgress();
    initSearch();
    initQuiz();
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
   2. Progress Tracker (Local Storage)
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
                markText.innerText = 'Đã hoàn thành bài này';
            } else {
                markBtn.className = 'btn btn-outline-success btn-sm d-inline-flex align-items-center gap-1';
                markText.innerText = 'Đánh dấu đã học xong';
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
                    document.getElementById('markCompleteText').innerText = 'Đánh dấu đã học xong';
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
   3. Search Functionality
   ========================================================================== */
function initSearch() {
    const searchInput = document.getElementById('globalSearchInput');
    const dropdown = document.getElementById('searchResultsDropdown');

    if (!searchInput || !dropdown) return;

    let debounceTimer;
    searchInput.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        const query = this.value.trim();

        if (query.length < 2) {
            dropdown.style.display = 'none';
            dropdown.innerHTML = '';
            return;
        }

        debounceTimer = setTimeout(async () => {
            try {
                const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
                const data = await res.json();
                renderSearchResults(data.results);
            } catch (err) {
                console.error("Search error:", err);
            }
        }, 250);
    });

    function renderSearchResults(results) {
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
                    <i class="bi ${icon} fs-5"></i>
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
        if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
}

/* ==========================================================================
   4. Interactive Quiz Engine
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
            labels[correctVal].classList.add('correct-choice');

            if (checked) {
                const userVal = parseInt(checked.value);
                if (userVal === correctVal) {
                    correctCount++;
                    statusBox.innerHTML = '<span class="badge bg-success"><i class="bi bi-check-lg"></i> Chính xác!</span>';
                } else {
                    labels[userVal].classList.add('wrong-choice');
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

        // Typeset explanations with MathJax
        if (window.MathJax) {
            MathJax.typesetPromise();
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
