# -*- coding: utf-8 -*-
"""
Đề thi Cuối Học Kì 2 - Đề số 3 (Chuẩn Format 90 phút Hưng Yên / GDPT 2018)
Phạm vi: Trọn bộ Tập 2 (Chương 6 đến Chương 9: Mũ & Logarit, Đạo hàm, Không gian vuông góc, Xác suất)
Tác giả: Antigravity AI
"""

DE_CUOI_KI_2_DE_3 = {
    "id": "de-cuoi-ki-2-de-3",
    "slug": "de-thi-cuoi-ki-2-de-so-3-toan-11",
    "title": "Đề thi Cuối Học Kì 2 - Đề số 3 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Cuối Học Kì 2",
    "subtitle": "Phạm vi: Toàn diện Tập 2 (Chương 6 đến Chương 9 - Đề số 3 Thực chiến & Phân loại điểm cao)",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Hàm số Mũ & Hàm số Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Đạo hàm & Ứng dụng Chuyển động", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Quan hệ vuông góc & Thể tích chóp, hộp", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"},
        {"topic": "Xác suất & Biến cố độc lập", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "matrix_table": [
        {"topic": "Hàm số Mũ & Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Đạo hàm & Chuyển động", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Hình học không gian & Thể tích", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"},
        {"topic": "Quy tắc tính xác suất", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT BỨT PHÁ ĐIỂM 9 - 10 ĐỀ SỐ 3 CUỐI HỌC KÌ 2:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm. Nhận biết nhanh tính chất đối xứng đồ thị mũ/logarit, thể tích hình hộp chữ nhật, đạo hàm lượng giác.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai. Câu chuyển động cực trị vận tốc, hình chóp có mặt bên vuông góc với đáy $SH \perp (ABC)$, trắc nghiệm 4 câu xác suất.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Bấm máy Casio nghiệm logarit $\log_2(x+3) + \log_2(x-3) = 4$, đạo hàm thương số, xác suất tổ hợp 1 nam 1 nữ.</li>
        <li><strong>85 - 90 phút:</strong> Rà soát lại tất cả các câu đã trả lời.</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Với số thực dương $a \neq 1$, giá trị của biểu thức $a^{\log_a 5}$ bằng:",
            "options": ["A. 5", r"B. $\log_a 5$", r"C. $a^5$", "D. 1"],
            "correct": 0,
            "method": "Công thức lũy thừa logarit",
            "explanation": r"Theo định nghĩa và tính chất cơ bản: $a^{\log_a b} = b$, do đó $a^{\log_a 5} = 5$."
        },
        {
            "id": 2,
            "question": r"Tập nghiệm của bất phương trình $2^{x - 1} > 8$ là:",
            "options": [
                r"A. $(4; +\infty)$",
                r"B. $(3; +\infty)$",
                r"C. $[4; +\infty)$",
                r"D. $(-\infty; 4)$"
            ],
            "correct": 0,
            "method": "Bất phương trình mũ cơ bản",
            "explanation": r"$2^{x - 1} > 8 = 2^3 \iff x - 1 > 3 \iff x > 4$. Tập nghiệm là $(4; +\infty)$."
        },
        {
            "id": 3,
            "question": r"Giá trị của logarit thập phân $\log 1000$ bằng:",
            "options": ["A. 3", "B. 10", "C. 100", "D. $\frac{1}{3}$"],
            "correct": 0,
            "method": "Logarit thập phân cơ số 10",
            "explanation": r"$\log 1000 = \log(10^3) = 3$."
        },
        {
            "id": 4,
            "question": r"Đạo hàm của hàm số $y = \frac{1}{x}$ tại điểm $x = 2$ bằng:",
            "options": [
                r"A. $-\frac{1}{4}$",
                r"B. $\frac{1}{4}$",
                r"C. $-\frac{1}{2}$",
                r"D. $\frac{1}{2}$"
            ],
            "correct": 0,
            "method": "Đạo hàm 1/x = -1/x^2",
            "explanation": r"$y' = -\frac{1}{x^2}$. Tại $x = 2 \implies y'(2) = -\frac{1}{4}$."
        },
        {
            "id": 5,
            "question": r"Đạo hàm của hàm số $y = \tan x$ trên tập xác định là:",
            "options": [
                r"A. $y' = 1 + \tan^2 x$",
                r"B. $y' = -\frac{1}{\cos^2 x}$",
                r"C. $y' = \cot x$",
                r"D. $y' = 1 - \tan^2 x$"
            ],
            "correct": 0,
            "method": "Công thức đạo hàm lượng giác tan x",
            "explanation": r"$(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x$."
        },
        {
            "id": 6,
            "question": r"Cho hình chóp tứ giác đều $S.ABCD$ có đáy là hình vuông tâm $O$. Đoạn thẳng nào sau đây là đường cao của hình chóp?",
            "options": ["A. $SO$", "B. $SA$", "C. $SB$", "D. $SC$"],
            "correct": 0,
            "method": "Tính chất chóp đều",
            "explanation": r"Hình chóp tứ giác đều có chân đường cao hạ từ đỉnh trùng với tâm của đáy, tức là đoạn thẳng $SO$."
        },
        {
            "id": 7,
            "question": r"Khoảng cách giữa hai mặt phẳng song song $(\alpha)$ và $(\beta)$ bằng:",
            "options": [
                "A. Khoảng cách từ một điểm bất kì trên $(\alpha)$ đến mặt phẳng $(\beta)$",
                "B. Độ dài đoạn thẳng nối một điểm trên $(\alpha)$ với một điểm trên $(\beta)$",
                "C. Khoảng cách giữa hai đường thẳng bất kì lần lượt nằm trên hai mặt phẳng",
                "D. Bằng 0"
            ],
            "correct": 0,
            "method": "Khoảng cách giữa 2 mặt phẳng song song",
            "explanation": r"Khoảng cách giữa 2 mặt phẳng song song là khoảng cách từ một điểm tùy ý thuộc mặt phẳng này đến mặt phẳng kia."
        },
        {
            "id": 8,
            "question": r"Cho hai biến cố $A$ và $B$ có $P(A) = 0.4, P(B) = 0.5$ và $P(AB) = 0.2$. Xác suất của biến cố hợp $P(A \cup B)$ bằng:",
            "options": ["A. 0.7", "B. 0.9", "C. 0.2", "D. 0.8"],
            "correct": 0,
            "method": "Công thức cộng xác suất tổng quát",
            "explanation": r"$P(A \cup B) = P(A) + P(B) - P(AB) = 0.4 + 0.5 - 0.2 = 0.7$."
        },
        {
            "id": 9,
            "question": r"Một hình hộp chữ nhật có ba kích thước lần lượt là $2\text{ cm}, 3\text{ cm}, 4\text{ cm}$. Thể tích của hình hộp chữ nhật đó là:",
            "options": [r"A. $24\text{ cm}^3$", r"B. $12\text{ cm}^3$", r"C. $8\text{ cm}^3$", r"D. $48\text{ cm}^3$"],
            "correct": 0,
            "method": "Thể tích hình hộp chữ nhật V = abc",
            "explanation": r"$V = a \cdot b \cdot c = 2 \times 3 \times 4 = 24\text{ cm}^3$."
        },
        {
            "id": 10,
            "question": r"Nghiệm của phương trình $\ln x = 0$ là:",
            "options": ["A. $x = 1$", "B. $x = 0$", "C. $x = e$", "D. $x = -1$"],
            "correct": 0,
            "method": "Phương trình logarit tự nhiên",
            "explanation": r"$\ln x = 0 \iff x = e^0 = 1$."
        },
        {
            "id": 11,
            "question": r"Đạo hàm cấp hai của hàm số $y = x^3 - 6x^2$ là:",
            "options": [
                r"A. $y'' = 6x - 12$",
                r"B. $y'' = 3x^2 - 12x$",
                r"C. $y'' = 6x$",
                r"D. $y'' = 6x - 6$"
            ],
            "correct": 0,
            "method": "Đạo hàm cấp hai y'' = (y')'",
            "explanation": r"$y' = 3x^2 - 12x \implies y'' = (3x^2 - 12x)' = 6x - 12$."
        },
        {
            "id": 12,
            "question": r"Cho tứ diện đều $ABCD$ cạnh $a$. Góc giữa hai đường thẳng $AB$ và $CD$ bằng:",
            "options": [r"A. $90^\circ$", r"B. $60^\circ$", r"C. $45^\circ$", r"D. $30^\circ$"],
            "correct": 0,
            "method": "Tính chất tứ diện đều",
            "explanation": r"Trong tứ diện đều, các cặp cạnh đối diện đôi một vuông góc với nhau: $AB \perp CD \implies$ góc bằng $90^\circ$."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Xét hai hàm số $y = f(x) = 2^x$ và $y = g(x) = \log_2 x$.",
            "sub_questions": [
                {"label": "a", "text": r"Hàm số $y = 2^x$ đồng biến trên tập xác định $\mathbb{R}$.", "correct": True, "explanation": r"Đúng. Cơ số $a = 2 > 1$ nên hàm số mũ đồng biến trên $\mathbb{R}$."},
                {"label": "b", "text": r"Tập xác định của hàm số $y = \log_2 x$ là khoảng $(0; +\infty)$.", "correct": True, "explanation": r"Đúng. Biểu thức trong logarit phải dương: $x > 0$."},
                {"label": "c", "text": r"Đồ thị của hai hàm số đối xứng với nhau qua đường thẳng $y = x$.", "correct": True, "explanation": r"Đúng. Hàm số mũ $y = a^x$ và hàm số logarit $y = \log_a x$ là hai hàm ngược nhau, đồ thị đối xứng qua đường phân giác $y = x$."},
                {"label": "d", "text": r"Phương trình $2^x = \log_2 x$ có nghiệm $x = 0$.", "correct": False, "explanation": r"Sai. Tại $x = 0$, hàm số $\log_2 x$ không xác định."}
            ]
        },
        {
            "id": 2,
            "context": r"Một chất điểm chuyển động theo phương trình quãng đường: $s(t) = -t^3 + 6t^2 + 15t$, trong đó $t$ tính bằng giây ($t \ge 0$) và $s$ tính bằng mét.",
            "sub_questions": [
                {"label": "a", "text": r"Phương trình vận tốc tức thời của chất điểm là $v(t) = -3t^2 + 12t + 15$.", "correct": True, "explanation": r"Đúng. $v(t) = s'(t) = -3t^2 + 12t + 15$."},
                {"label": "b", "text": r"Vận tốc ban đầu của chất điểm tại $t = 0$ là $15\text{ m/s}$.", "correct": True, "explanation": r"Đúng. $v(0) = -3(0)^2 + 12(0) + 15 = 15\text{ m/s}$."},
                {"label": "c", "text": r"Thời điểm chất điểm dừng lại ($v = 0$) là lúc $t = 5$ giây.", "correct": True, "explanation": r"Đúng. $-3t^2 + 12t + 15 = 0 \iff t^2 - 4t - 5 = 0 \iff t = 5$ (giây) vì $t \ge 0$."},
                {"label": "d", "text": r"Vận tốc lớn nhất mà chất điểm đạt được là $25\text{ m/s}$.", "correct": False, "explanation": r"Sai. Parabol $v(t) = -3(t - 2)^2 + 27 \implies v_{\max} = 27\text{ m/s}$ tại thời điểm $t = 2$ giây."}
            ]
        },
        {
            "id": 3,
            "context": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $A$ với $AB = a, AC = a\sqrt{3}$. Mặt bên $(SAB)$ là tam giác đều và nằm trong mặt phẳng vuông góc với đáy $(ABC)$. Gọi $H$ là trung điểm của đoạn thẳng $AB$.",
            "sub_questions": [
                {"label": "a", "text": r"Đoạn thẳng $SH$ vuông góc với mặt phẳng đáy $(ABC)$.", "correct": True, "explanation": r"Đúng. Tam giác đều $SAB \implies SH \perp AB$. Mà $(SAB) \perp (ABC)$ theo giao tuyến $AB$ nên $SH \perp (ABC)$."},
                {"label": "b", "text": r"Chiều cao của khối chóp bằng $SH = \frac{a\sqrt{3}}{2}$.", "correct": True, "explanation": r"Đúng. Đường cao tam giác đều cạnh $a$ bằng $\frac{a\sqrt{3}}{2}$."},
                {"label": "c", "text": r"Diện tích tam giác đáy $ABC$ bằng $\frac{a^2\sqrt{3}}{2}$.", "correct": True, "explanation": r"Đúng. $S_{ABC} = \frac{1}{2} AB \cdot AC = \frac{1}{2} \cdot a \cdot a\sqrt{3} = \frac{a^2\sqrt{3}}{2}$."},
                {"label": "d", "text": r"Thể tích của khối chóp $S.ABC$ bằng $\frac{a^3}{4}$.", "correct": True, "explanation": r"Đúng. $V = \frac{1}{3} S_{ABC} \cdot SH = \frac{1}{3} \cdot \frac{a^2\sqrt{3}}{2} \cdot \frac{a\sqrt{3}}{2} = \frac{3a^3}{12} = \frac{a^3}{4}$."}
            ]
        },
        {
            "id": 4,
            "context": r"Một đề kiểm tra trắc nghiệm ngắn gồm 4 câu hỏi. Mỗi câu hỏi có 4 phương án trả lời trong đó chỉ có đúng 1 phương án chính xác. Một học sinh không học bài nên chọn ngẫu nhiên một phương án cho mỗi câu.",
            "sub_questions": [
                {"label": "a", "text": r"Xác suất để học sinh trả lời đúng một câu bất kì là 0.25.", "correct": True, "explanation": r"Đúng. Mỗi câu có 4 phương án, 1 đúng $\implies p = 1/4 = 0.25$."},
                {"label": "b", "text": r"Xác suất để học sinh trả lời đúng cả 4 câu là $\frac{1}{256}$.", "correct": True, "explanation": r"Đúng. Do việc chọn độc lập: $P = (1/4)^4 = \frac{1}{256}$."},
                {"label": "c", "text": r"Xác suất để học sinh trả lời sai cả 4 câu là $\frac{81}{256}$.", "correct": True, "explanation": r"Đúng. Xác suất sai 1 câu là $3/4 \implies P = (3/4)^4 = \frac{81}{256}$."},
                {"label": "d", "text": r"Xác suất để học sinh trả lời đúng ít nhất một câu là $\frac{175}{256}$.", "correct": True, "explanation": r"Đúng. Biến cố đối của 'sai cả 4 câu': $1 - \frac{81}{256} = \frac{175}{256}$."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Cho hàm số $f(x) = \frac{x^2 - 3x}{x + 1}$. Tính giá trị đạo hàm $f'(1)$.",
            "answer": "0",
            "unit": "",
            "method": "Đạo hàm của thương u/v",
            "explanation": r"$f'(x) = \frac{(2x - 3)(x + 1) - (x^2 - 3x)(1)}{(x + 1)^2}$. Tại $x = 1 \implies f'(1) = \frac{(-1)(2) - (-2)(1)}{2^2} = \frac{-2 + 2}{4} = 0$."
        },
        {
            "id": 2,
            "question": r"Tìm nghiệm của phương trình $\log_2(x + 3) + \log_2(x - 3) = 4$.",
            "answer": "5",
            "unit": "",
            "method": "Tổng hai logarit cùng cơ số",
            "explanation": r"Điều kiện $x > 3$. Phương trình $\iff \log_2[(x + 3)(x - 3)] = 4 \iff x^2 - 9 = 2^4 = 16 \iff x^2 = 25 \iff x = 5$ (loại $x = -5$)."
        },
        {
            "id": 3,
            "question": r"Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $6\text{ cm}$. Tính khoảng cách giữa hai mặt phẳng đáy $(ABCD)$ và $(A'B'C'D')$ (đơn vị: $\text{cm}$).",
            "answer": "6",
            "unit": "cm",
            "method": "Khoảng cách giữa hai mặt phẳng đáy lăng trụ",
            "explanation": r"Hai mặt phẳng đáy song song với nhau và có đoạn vuông góc chung là cạnh bên $AA' = 6\text{ cm}$. Do đó khoảng cách bằng $6\text{ cm}$."
        },
        {
            "id": 4,
            "question": r"Cho hình chóp đều $S.ABCD$ có đáy là hình vuông cạnh bằng $2\text{ cm}$, chiều cao $SO = 3\text{ cm}$. Tính thể tích của khối chóp $S.ABCD$ (đơn vị: $\text{cm}^3$).",
            "answer": "4",
            "unit": "cm³",
            "method": "Thể tích chóp V = 1/3 Bh",
            "explanation": r"Diện tích đáy $S_{ABCD} = 2^2 = 4\text{ cm}^2$. Thể tích $V = \frac{1}{3} S_{ABCD} \cdot SO = \frac{1}{3} \times 4 \times 3 = 4\text{ cm}^3$."
        },
        {
            "id": 5,
            "question": r"Cho hàm số $y = \cos x$. Tính giá trị của đạo hàm cấp hai $y''$ tại điểm $x = \pi$.",
            "answer": "1",
            "unit": "",
            "method": "Đạo hàm cấp hai lượng giác",
            "explanation": r"$y' = -\sin x \implies y'' = (-\sin x)' = -\cos x$. Tại $x = \pi \implies y''(\pi) = -\cos(\pi) = -(-1) = 1$."
        },
        {
            "id": 6,
            "question": r"Một đội văn nghệ có 5 học sinh nam và 5 học sinh nữ. Chọn ngẫu nhiên đồng thời 2 học sinh đi biểu diễn. Tính xác suất để chọn được đúng 1 học sinh nam và 1 học sinh nữ (viết kết quả làm tròn đến hai chữ số thập phân).",
            "answer": "0.56",
            "unit": "",
            "method": "Xác suất tổ hợp",
            "explanation": r"Số cách chọn 2 học sinh từ 10 học sinh: $n(\Omega) = C_{10}^2 = \frac{10 \times 9}{2} = 45$. Số cách chọn 1 nam và 1 nữ: $n(A) = C_5^1 \times C_5^1 = 5 \times 5 = 25$. Xác suất $P = \frac{25}{45} = \frac{5}{9} \approx 0.5555... \approx 0.56$."
        }
    ]
}
