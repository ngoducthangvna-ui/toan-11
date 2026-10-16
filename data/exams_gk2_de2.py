# -*- coding: utf-8 -*-
"""Đề thi Giữa Học Kì 2 - Đề số 2 (Chuẩn 90 phút Hưng Yên)"""

EXAM_GK2_DE2 = {
    "id": "de-giua-ki-2-de-2",
    "slug": "de-thi-giua-ki-2-de-2",
    "title": "Đề thi Giữa Học Kì 2 - Đề số 2 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Giữa Học Kì 2",
    "subtitle": "Phạm vi: Phương trình Mũ - Logarit + Đạo hàm cơ bản & Phương trình tiếp tuyến",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Mũ & Logarit nâng cao", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm (50%)"},
        {"topic": "Đạo hàm & Tiếp tuyến đồ thị", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm (50%)"}
    ],
    "matrix_table": [
        {"topic": "Mũ & Logarit nâng cao", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm"},
        {"topic": "Đạo hàm & Tiếp tuyến đồ thị", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> BẤM MÁY ĐẠO HÀM & TIẾP TUYẾN CASIO FX-580VN X:</h6>
    <ul class="mb-0 small">
        <li><strong>Tính hệ số góc tiếp tuyến:</strong> Bấm <code>[SHIFT] [d/dx]</code> nhập hàm số $f(x)$ tại $x = x_0$ ra ngay hệ số góc $k = f'(x_0)$.</li>
        <li><strong>Phương trình tiếp tuyến:</strong> $y = f'(x_0)(x - x_0) + y_0$.</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Đạo hàm của hàm số $y = x^4 - 3x^2 + 2$ là:",
            "options": [r"A. $y' = 4x^3 - 6x$", r"B. $y' = 4x^3 - 3x$", r"C. $y' = 4x^3 - 6x + 2$", r"D. $y' = x^3 - 6x$"],
            "correct": 0,
            "method": "Quy tắc lũy thừa",
            "explanation": r"$(x^4)' = 4x^3$, $(-3x^2)' = -6x$, $(2)' = 0$. Vậy $y' = 4x^3 - 6x$."
        },
        {
            "id": 2,
            "question": r"Hệ số góc của tiếp tuyến của đồ thị hàm số $y = x^3 - 2x + 1$ tại điểm có hoành độ $x_0 = 1$ bằng:",
            "options": ["A. 1", "B. 2", "C. 3", "D. 0"],
            "correct": 0,
            "method": "Hệ số góc k = f'(x0)",
            "explanation": r"$y' = 3x^2 - 2$. Hệ số góc $k = y'(1) = 3(1)^2 - 2 = 1$."
        },
        {
            "id": 3,
            "question": r"Tập nghiệm của bất phương trình $\log_{0.5}(x) \ge 1$ là:",
            "options": [r"A. $(0; 0.5]$", r"B. $[0.5; +\infty)$", r"C. $(0; 2]$", r"D. $[2; +\infty)$"],
            "correct": 0,
            "method": "Cơ số nhỏ hơn 1 đổi chiều",
            "explanation": r"ĐKXĐ: $x > 0$. Vì cơ số $0.5 < 1$ nên $\log_{0.5} x \ge 1 \iff x \le (0.5)^1 = 0.5$. Kết hợp: $0 < x \le 0.5$."
        },
        {
            "id": 4,
            "question": r"Đạo hàm của hàm số $y = \sin(2x)$ là:",
            "options": [r"A. $2\cos(2x)$", r"B. $\cos(2x)$", r"C. $-2\cos(2x)$", r"D. $2\sin(2x)$"],
            "correct": 0,
            "method": "Đạo hàm hàm hợp",
            "explanation": r"$(\sin u)' = u' \cos u \implies (\sin 2x)' = 2\cos(2x)$."
        },
        {
            "id": 5,
            "question": r"Phương trình $e^x = 5$ có nghiệm là:",
            "options": [r"A. $x = \ln 5$", r"B. $x = \log_5 e$", r"C. $x = 5^e$", r"D. $x = e^5$"],
            "correct": 0,
            "method": "Định nghĩa logarit tự nhiên",
            "explanation": r"$e^x = 5 \iff x = \ln 5$."
        },
        {
            "id": 6,
            "question": r"Đạo hàm của hàm số $y = \ln x$ với $x > 0$ là:",
            "options": [r"A. $\frac{1}{x}$", r"B. $-\frac{1}{x^2}$", r"C. $\frac{1}{x\ln 10}$", "D. 1"],
            "correct": 0,
            "method": "Đạo hàm cơ bản ln",
            "explanation": r"$(\ln x)' = \frac{1}{x}$."
        },
        {
            "id": 7,
            "question": r"Cho hàm số $y = f(x)$ có $f'(2) = 3$ và $f(2) = 5$. Phương trình tiếp tuyến của đồ thị tại điểm $M(2; 5)$ là:",
            "options": [r"A. $y = 3x - 1$", r"B. $y = 3x + 1$", r"C. $y = 3x + 5$", r"D. $y = 2x + 1$"],
            "correct": 0,
            "method": "Phương trình tiếp tuyến",
            "explanation": r"$y = f'(2)(x - 2) + f(2) = 3(x - 2) + 5 = 3x - 1$."
        },
        {
            "id": 8,
            "question": r"Nghiệm của phương trình $\log_3(2x - 1) = 2$ là:",
            "options": ["A. 5", "B. 4", "C. 9", "D. 10"],
            "correct": 0,
            "method": "Mũ hóa logarit",
            "explanation": r"$2x - 1 = 3^2 = 9 \iff 2x = 10 \iff x = 5$."
        },
        {
            "id": 9,
            "question": r"Đạo hàm của hàm số $y = \sqrt{x}$ (với $x > 0$) là:",
            "options": [r"A. $\frac{1}{2\sqrt{x}}$", r"B. $\frac{1}{\sqrt{x}}$", r"C. $2\sqrt{x}$", r"D. $\frac{2}{\sqrt{x}}$"],
            "correct": 0,
            "method": "Đạo hàm căn",
            "explanation": r"$(\sqrt{x})' = \frac{1}{2\sqrt{x}}$."
        },
        {
            "id": 10,
            "question": r"Đạo hàm cấp hai của hàm số $y = x^3$ là:",
            "options": ["A. $6x$", "B. $3x^2$", "C. 6", "D. $x^2$"],
            "correct": 0,
            "method": "Đạo hàm cấp hai",
            "explanation": r"$y' = 3x^2 \implies y'' = (3x^2)' = 6x$."
        },
        {
            "id": 11,
            "question": r"Cho hai hàm số $u(x), v(x)$ có đạo hàm. Đẳng thức nào sau đây ĐÚNG?",
            "options": [
                r"A. $(u \cdot v)' = u'v + uv'$",
                r"B. $(u \cdot v)' = u'v'$",
                r"C. $(u \cdot v)' = u'v - uv'$",
                r"D. $(u \cdot v)' = u' + v'$"
            ],
            "correct": 0,
            "method": "Quy tắc tích",
            "explanation": r"Đạo hàm của một tích: $(uv)' = u'v + uv'$."
        },
        {
            "id": 12,
            "question": r"Nghiệm của bất phương trình $2^{x - 2} < 8$ là:",
            "options": [r"A. $x < 5$", r"B. $x > 5$", r"C. $x < 3$", r"D. $x > 3$"],
            "correct": 0,
            "method": "Bất phương trình mũ",
            "explanation": r"$2^{x - 2} < 8 = 2^3 \iff x - 2 < 3 \iff x < 5$."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Cho hàm số $y = f(x) = \frac{2x - 1}{x + 1}$ có đồ thị $(C)$.",
            "sub_questions": [
                {"label": "a", "text": r"Tập xác định của hàm số là $D = \mathbb{R} \setminus \{-1\}$.", "correct": True, "explanation": r"Đúng."},
                {"label": "b", "text": r"Đạo hàm của hàm số là $f'(x) = \frac{3}{(x + 1)^2}$.", "correct": True, "explanation": r"Đúng. Áp dụng quy tắc $\frac{ad - bc}{(cx + d)^2} = \frac{2(1) - (-1)(1)}{(x + 1)^2} = \frac{3}{(x + 1)^2}$."},
                {"label": "c", "text": r"Hệ số góc của tiếp tuyến tại điểm có hoành độ $x_0 = 0$ bằng 3.", "correct": True, "explanation": r"Đúng. $f'(0) = \frac{3}{(0 + 1)^2} = 3$."},
                {"label": "d", "text": r"Phương trình tiếp tuyến tại điểm có hoành độ $x_0 = 0$ là $y = 3x + 1$.", "correct": False, "explanation": r"Sai. Điểm tiếp xúc $M(0; -1)$, PTTT: $y = 3(x - 0) - 1 = 3x - 1$."}
            ]
        },
        {
            "id": 2,
            "context": r"Cho hàm số $y = 2^x$ và $y = \log_2 x$.",
            "sub_questions": [
                {"label": "a", "text": r"Đồ thị của hai hàm số đối xứng nhau qua đường thẳng $y = x$.", "correct": True, "explanation": r"Đúng. Đây là tính chất hai hàm số ngược nhau."},
                {"label": "b", "text": r"Hàm số $y = 2^x$ luôn đồng biến trên $\mathbb{R}$.", "correct": True, "explanation": r"Đúng. Do cơ số $2 > 1$."},
                {"label": "c", "text": r"Hàm số $y = \log_2 x$ có tập giá trị là $\mathbb{R}$.", "correct": True, "explanation": r"Đúng. Tập giá trị của logarit là $(-\infty; +\infty)$."},
                {"label": "d", "text": r"Hai đồ thị cắt nhau tại 3 điểm phân biệt.", "correct": False, "explanation": r"Sai. $2^x > x > \log_2 x$ với mọi $x > 0$, hai đồ thị không cắt nhau."}
            ]
        },
        {
            "id": 3,
            "context": r"Một vật chuyển động thẳng xác định bởi phương trình $s(t) = t^3 - 3t^2 + 9t$ ($t$ tính bằng giây, $s$ tính bằng mét).",
            "sub_questions": [
                {"label": "a", "text": r"Vận tốc tức thời của vật là $v(t) = s'(t) = 3t^2 - 6t + 9$.", "correct": True, "explanation": r"Đúng. Ý nghĩa cơ học của đạo hàm: $v(t) = s'(t)$."},
                {"label": "b", "text": r"Vận tốc ban đầu của vật tại thời điểm $t = 0$ là 9 m/s.", "correct": True, "explanation": r"Đúng. $v(0) = 9$ m/s."},
                {"label": "c", "text": r"Gia tốc tức thời của vật tại thời điểm $t = 2$ giây bằng 6 m/s$^2$.", "correct": True, "explanation": r"Đúng. $a(t) = v'(t) = 6t - 6 \implies a(2) = 6(2) - 6 = 6$ m/s$^2$."},
                {"label": "d", "text": r"Vận tốc của vật đạt giá trị nhỏ nhất bằng 0 m/s.", "correct": False, "explanation": r"Sai. $v(t) = 3(t - 1)^2 + 6 \ge 6$ m/s. Vận tốc nhỏ nhất là 6 m/s."}
            ]
        },
        {
            "id": 4,
            "context": r"Cho phương trình logarit: $\log_2^2 x - 4\log_2 x + 3 = 0$.",
            "sub_questions": [
                {"label": "a", "text": r"Điều kiện xác định của phương trình là $x > 0$.", "correct": True, "explanation": r"Đúng."},
                {"label": "b", "text": r"Đặt $t = \log_2 x$, phương trình trở thành $t^2 - 4t + 3 = 0$.", "correct": True, "explanation": r"Đúng."},
                {"label": "c", "text": r"Phương trình có 2 nghiệm phân biệt là $x_1 = 2$ và $x_2 = 8$.", "correct": True, "explanation": r"Đúng. $t = 1 \implies x = 2^1 = 2$; $t = 3 \implies x = 2^3 = 8$."},
                {"label": "d", "text": r"Tích của hai nghiệm phương trình bằng 10.", "correct": False, "explanation": r"Sai. Tích $x_1 \cdot x_2 = 2 \cdot 8 = 16$."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Tính đạo hàm của hàm số $f(x) = x^3 - 3x$ tại điểm $x = 2$:",
            "answer": "9",
            "explanation_steps": [
                r"$f'(x) = 3x^2 - 3$.",
                r"Tại $x = 2$: $f'(2) = 3(2)^2 - 3 = 12 - 3 = 9$."
            ]
        },
        {
            "id": 2,
            "question": r"Tìm hệ số góc của tiếp tuyến của đồ thị hàm số $y = \frac{x + 2}{x - 1}$ tại điểm có tung độ $y_0 = 4$:",
            "answer": "-3",
            "explanation_steps": [
                r"Tìm hoành độ tiếp điểm: $\frac{x_0 + 2}{x_0 - 1} = 4 \iff x_0 + 2 = 4x_0 - 4 \iff 3x_0 = 6 \implies x_0 = 2$.",
                r"Đạo hàm: $y' = \frac{1(-1) - 2(1)}{(x - 1)^2} = \frac{-3}{(x - 1)^2}$.",
                r"Hệ số góc tại $x_0 = 2$: $k = y'(2) = \frac{-3}{(2 - 1)^2} = -3$."
            ]
        },
        {
            "id": 3,
            "question": r"Biết phương trình $2^{2x} - 6 \cdot 2^x + 8 = 0$ có hai nghiệm $x_1, x_2$. Tính tổng $x_1 + x_2$:",
            "answer": "3",
            "explanation_steps": [
                r"Đặt $t = 2^x > 0$. Phương trình thành $t^2 - 6t + 8 = 0 \iff t = 2$ hoặc $t = 4$.",
                r"$2^x = 2 \implies x_1 = 1$.",
                r"$2^x = 4 \implies x_2 = 2$.",
                r"Tổng $x_1 + x_2 = 1 + 2 = 3$."
            ]
        },
        {
            "id": 4,
            "question": r"Cho hàm số $f(x) = \ln(x^2 + 1)$. Tính giá trị của $f'(1)$ (viết kết quả dạng số nguyên):",
            "answer": "1",
            "explanation_steps": [
                r"Áp dụng công thức đạo hàm hàm hợp $(\ln u)' = \frac{u'}{u}$:",
                r"$f'(x) = \frac{(x^2 + 1)'}{x^2 + 1} = \frac{2x}{x^2 + 1}$.",
                r"Tại $x = 1$: $f'(1) = \frac{2(1)}{1^2 + 1} = \frac{2}{2} = 1$."
            ]
        },
        {
            "id": 5,
            "question": r"Một chất điểm chuyển động với phương trình quãng đường $s(t) = -t^3 + 6t^2 + 2t$ ($t \ge 0$, tính bằng giây). Tại thời điểm nào thì vận tốc của chất điểm đạt giá trị lớn nhất (tính bằng giây)?",
            "answer": "2",
            "explanation_steps": [
                r"Vận tốc: $v(t) = s'(t) = -3t^2 + 12t + 2$.",
                r"Đây là tam thức bậc hai có $a = -3 < 0$, đạt giá trị lớn nhất tại đỉnh parabol:",
                r"$t = -\frac{b}{2a} = -\frac{12}{2(-3)} = 2$ giây."
            ]
        },
        {
            "id": 6,
            "question": r"Tìm số nghiệm nguyên của bất phương trình: $\log_3(x - 1) \le 2$:",
            "answer": "9",
            "explanation_steps": [
                r"Điều kiện: $x - 1 > 0 \iff x > 1$.",
                r"Vì cơ số $3 > 1$ nên $x - 1 \le 3^2 = 9 \iff x \le 10$.",
                r"Kết hợp điều kiện: $1 < x \le 10$.",
                r"Các nghiệm nguyên là $x \in \{2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Có đúng 9 nghiệm."
            ]
        }
    ]
}
