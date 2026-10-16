# -*- coding: utf-8 -*-
"""
Đề thi Cuối Học Kì 2 - Đề số 1 (Chuẩn Format 90 phút Hưng Yên / GDPT 2018)
Phạm vi: Trọn bộ Tập 2 (Chương 6 đến Chương 9: Mũ & Logarit, Đạo hàm, Không gian vuông góc, Xác suất)
Tác giả: Antigravity AI
"""

DE_CUOI_KI_2_DE_1 = {
    "id": "de-cuoi-ki-2-de-1",
    "slug": "de-thi-cuoi-ki-2-de-so-1-toan-11",
    "title": "Đề thi Cuối Học Kì 2 - Đề số 1 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Cuối Học Kì 2",
    "subtitle": "Phạm vi: Toàn diện Tập 2 (Chương 6: Mũ & Logarit, Chương 7: Đạo hàm, Chương 8: Quan hệ vuông góc, Chương 9: Xác suất)",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Hàm số Mũ & Hàm số Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Đạo hàm & Tiếp tuyến của đồ thị", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Quan hệ vuông góc trong không gian", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.5 điểm"},
        {"topic": "Quy tắc tính xác suất", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "matrix_table": [
        {"topic": "Hàm số Mũ & Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Đạo hàm & Ứng dụng", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Hình học không gian vuông góc", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.5 điểm"},
        {"topic": "Quy tắc xác suất", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT PHÂN BỔ THỜI GIAN ĐỀ CUỐI HỌC KÌ 2:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm đơn. Bấm máy tính đạo hàm <code>[SHIFT] [d/dx]</code> tại điểm để kiểm tra lại công thức đạo hàm.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai. Phần hình không gian vuông góc nhớ vẽ hình chóp chuẩn (chân đường cao hạ thẳng đứng) để xác định đúng góc và khoảng cách.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Chú ý bài toán thực tế lãi kép, tính gia tốc chuyển động bằng đạo hàm cấp 2 $s''(t)$, khoảng cách không gian.</li>
        <li><strong>85 - 90 phút:</strong> Rà soát đơn vị (năm, cm, mét, xác suất làm tròn).</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Với số thực dương $x$ tùy ý, biểu thức $P = x^{1/3} \cdot \sqrt{x}$ được viết dưới dạng lũy thừa với số mũ hữu tỉ là:",
            "options": [r"A. $x^{5/6}$", r"B. $x^{2/3}$", r"C. $x^{1/6}$", r"D. $x^{4/3}$"],
            "correct": 0,
            "method": "Công thức lũy thừa",
            "explanation": r"$P = x^{1/3} \cdot x^{1/2} = x^{1/3 + 1/2} = x^{5/6}$."
        },
        {
            "id": 2,
            "question": r"Với $a$ là số thực dương tùy ý, $\log_2(8a^3)$ bằng:",
            "options": [
                r"A. $3 + 3\log_2 a$",
                r"B. $3 + \log_2 a$",
                r"C. $8 + 3\log_2 a$",
                r"D. $6\log_2 a$"
            ],
            "correct": 0,
            "method": "Logarit của tích và lũy thừa",
            "explanation": r"$\log_2(8a^3) = \log_2 8 + \log_2(a^3) = 3 + 3\log_2 a$."
        },
        {
            "id": 3,
            "question": r"Tập xác định của hàm số $y = \log_3(x - 4)$ là:",
            "options": [
                r"A. $(4; +\infty)$",
                r"B. $[4; +\infty)$",
                r"C. $(-\infty; 4)$",
                r"D. $\mathbb{R} \setminus \{4\}$"
            ],
            "correct": 0,
            "method": "Điều kiện xác định logarit",
            "explanation": r"Điều kiện biểu thức trong logarit dương: $x - 4 > 0 \iff x > 4$."
        },
        {
            "id": 4,
            "question": r"Đạo hàm của hàm số $y = x^4 - 3x^2 + 2x - 5$ là:",
            "options": [
                r"A. $y' = 4x^3 - 6x + 2$",
                r"B. $y' = 4x^3 - 3x + 2$",
                r"C. $y' = 4x^3 - 6x$",
                r"D. $y' = x^3 - 6x + 2$"
            ],
            "correct": 0,
            "method": "Quy tắc đạo hàm đa thức",
            "explanation": r"$y' = (x^4)' - 3(x^2)' + 2(x)' - (5)' = 4x^3 - 6x + 2$."
        },
        {
            "id": 5,
            "question": r"Đạo hàm của hàm số $y = e^{2x + 1}$ là:",
            "options": [
                r"A. $y' = 2e^{2x + 1}$",
                r"B. $y' = e^{2x + 1}$",
                r"C. $y' = (2x + 1)e^{2x}$",
                r"D. $y' = \frac{1}{2}e^{2x + 1}$"
            ],
            "correct": 0,
            "method": "Đạo hàm hàm hợp mũ e^u",
            "explanation": r"$(e^u)' = u' \cdot e^u \implies (e^{2x+1})' = (2x+1)' \cdot e^{2x+1} = 2e^{2x+1}$."
        },
        {
            "id": 6,
            "question": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$ và $SA \perp (ABC)$. Hình chiếu vuông góc của đoạn thẳng $SC$ lên mặt phẳng $(ABC)$ là:",
            "options": ["A. Đoạn thẳng $AC$", "B. Đoạn thẳng $BC$", "C. Đoạn thẳng $AB$", "D. Điểm $A$"],
            "correct": 0,
            "method": "Hình chiếu vuông góc",
            "explanation": r"Vì $SA \perp (ABC)$ nên hình chiếu của $S$ lên $(ABC)$ là $A$. Điểm $C$ thuộc $(ABC)$ có hình chiếu là chính nó. Vậy hình chiếu của $SC$ lên $(ABC)$ là $AC$."
        },
        {
            "id": 7,
            "question": r"Trong không gian, góc giữa hai đường thẳng vuông góc với nhau bằng:",
            "options": [r"A. $90^\circ$", r"B. $0^\circ$", r"C. $180^\circ$", r"D. $45^\circ$"],
            "correct": 0,
            "method": "Góc giữa hai đường thẳng",
            "explanation": r"Theo định nghĩa, hai đường thẳng vuông góc trong không gian có góc giữa chúng bằng $90^\circ$."
        },
        {
            "id": 8,
            "question": r"Cho $A$ và $B$ là hai biến cố độc lập với $P(A) = 0.6$ và $P(B) = 0.5$. Xác suất của biến cố giao $P(AB)$ bằng:",
            "options": ["A. 0.30", "B. 1.10", "C. 0.10", "D. 0.55"],
            "correct": 0,
            "method": "Quy tắc nhân biến cố độc lập",
            "explanation": r"Vì $A$ và $B$ độc lập nên $P(AB) = P(A) \cdot P(B) = 0.6 \times 0.5 = 0.30$."
        },
        {
            "id": 9,
            "question": r"Cho hai mặt phẳng $(P)$ và $(Q)$ vuông góc với nhau theo giao tuyến $d$. Đường thẳng $a$ nằm trong $(P)$ và vuông góc với giao tuyến $d$. Khẳng định nào sau đây là đúng?",
            "options": [
                r"A. $a \perp (Q)$",
                r"B. $a // (Q)$",
                r"C. $a \subset (Q)$",
                r"D. Góc giữa $a$ và $(Q)$ bằng $45^\circ$"
            ],
            "correct": 0,
            "method": "Định lí vuông góc 2 mặt phẳng",
            "explanation": r"Định lí: Nếu hai mặt phẳng vuông góc với nhau thì bất cứ đường thẳng nào nằm trong mặt phẳng này và vuông góc với giao tuyến đều vuông góc với mặt phẳng kia."
        },
        {
            "id": 10,
            "question": r"Nghiệm của phương trình $\log_2(x - 1) = 3$ là:",
            "options": ["A. $x = 9$", "B. $x = 8$", "C. $x = 7$", "D. $x = 10$"],
            "correct": 0,
            "method": "Phương trình logarit cơ bản",
            "explanation": r"$\log_2(x - 1) = 3 \iff x - 1 = 2^3 = 8 \iff x = 9$ (thỏa mãn $x - 1 > 0$)."
        },
        {
            "id": 11,
            "question": r"Đạo hàm của hàm số $y = \sin(3x)$ là:",
            "options": [
                r"A. $y' = 3\cos(3x)$",
                r"B. $y' = \cos(3x)$",
                r"C. $y' = -3\cos(3x)$",
                r"D. $y' = -3\sin(3x)$"
            ],
            "correct": 0,
            "method": "Đạo hàm sin(u)",
            "explanation": r"$(\sin u)' = u' \cdot \cos u \implies (\sin 3x)' = 3\cos(3x)$."
        },
        {
            "id": 12,
            "question": r"Cho hình lập phương $ABCD.A'B'C'D'$ cạnh bằng $a$. Khoảng cách giữa hai đường thẳng $AB$ và $C'D'$ bằng:",
            "options": [r"A. $a\sqrt{2}$", r"B. $a$", r"C. $a\sqrt{3}$", r"D. $\frac{a}{2}$"],
            "correct": 0,
            "method": "Khoảng cách giữa hai đường chéo nhau",
            "explanation": r"$AB // C'D'$ là sai, $AB // CD$ và $CD // C'D' \implies AB // C'D'$. Khoảng cách giữa hai đường thẳng song song $AB$ và $C'D'$ bằng khoảng cách từ $B$ đến $C'D'$, tức là đường chéo mặt phẳng bên $BC' = a\sqrt{2}$."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Dân số của một tỉnh ở đồng bằng sông Hồng được dự báo theo công thức tăng trưởng liên tục: $S(t) = S_0 \cdot e^{rt}$, trong đó $S_0$ là dân số tại thời điểm ban đầu ($t = 0$), $r$ là tỉ lệ tăng dân số hàng năm, và $t$ là số năm tính từ thời điểm ban đầu.",
            "sub_questions": [
                {"label": "a", "text": r"Nếu $S_0 = 1.2$ triệu người và tỉ lệ tăng hàng năm $r = 1.5\% = 0.015$, công thức dân số là $S(t) = 1.2 \cdot e^{0.015t}$.", "correct": True, "explanation": r"Đúng. Thay các tham số $S_0 = 1.2$ và $r = 0.015$ vào công thức."},
                {"label": "b", "text": r"Sau 10 năm ($t = 10$), dân số của tỉnh ước tính đạt khoảng 1.39 triệu người (lấy $e^{0.15} \approx 1.1618$).", "correct": True, "explanation": r"Đúng. $S(10) = 1.2 \cdot e^{0.15} \approx 1.2 \times 1.1618 \approx 1.394$ triệu người."},
                {"label": "c", "text": r"Để dân số tăng gấp đôi so với ban đầu, cần khoảng thời gian $t = \frac{\ln 2}{r}$ năm.", "correct": True, "explanation": r"Đúng. $2S_0 = S_0 \cdot e^{rt} \iff e^{rt} = 2 \iff rt = \ln 2 \iff t = \frac{\ln 2}{r}$."},
                {"label": "d", "text": r"Với $r = 1.5\%$, sau đúng 30 năm thì dân số sẽ tăng gấp đôi.", "correct": False, "explanation": r"Sai. $t = \frac{\ln 2}{0.015} \approx \frac{0.6931}{0.015} \approx 46.2$ năm, không phải 30 năm."}
            ]
        },
        {
            "id": 2,
            "context": r"Cho hàm số $y = f(x) = \frac{2x - 1}{x + 1}$ có đồ thị $(C)$.",
            "sub_questions": [
                {"label": "a", "text": r"Đạo hàm của hàm số là $f'(x) = \frac{3}{(x + 1)^2}$ với mọi $x \neq -1$.", "correct": True, "explanation": r"Đúng. $f'(x) = \frac{2(x+1) - (2x-1)(1)}{(x+1)^2} = \frac{3}{(x+1)^2}$."},
                {"label": "b", "text": r"Hệ số góc của tiếp tuyến của đồ thị $(C)$ tại điểm có hoành độ $x_0 = 1$ bằng $k = \frac{3}{4}$.", "correct": True, "explanation": r"Đúng. $k = f'(1) = \frac{3}{(1+1)^2} = \frac{3}{4}$."},
                {"label": "c", "text": r"Tọa độ tiếp điểm tại $x_0 = 1$ là $M\left(1; \frac{1}{2}\right)$.", "correct": True, "explanation": r"Đúng. $y_0 = f(1) = \frac{2(1)-1}{1+1} = \frac{1}{2}$."},
                {"label": "d", "text": r"Phương trình tiếp tuyến tại $x_0 = 1$ là $y = \frac{3}{4}x + 1$.", "correct": False, "explanation": r"Sai. Tiếp tuyến: $y - \frac{1}{2} = \frac{3}{4}(x - 1) \iff y = \frac{3}{4}x - \frac{3}{4} + \frac{1}{2} = \frac{3}{4}x - \frac{1}{4}$."}
            ]
        },
        {
            "id": 3,
            "context": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, cạnh bên $SA \perp (ABCD)$ và $SA = a\sqrt{3}$.",
            "sub_questions": [
                {"label": "a", "text": r"Đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$.", "correct": True, "explanation": r"Đúng. Vì $BC \perp AB$ (đáy hình vuông) và $BC \perp SA$ (do $SA \perp$ đáy)."},
                {"label": "b", "text": r"Góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ bằng $60^\circ$.", "correct": False, "explanation": r"Sai. Hình chiếu của $SC$ lên đáy là $AC$. Đáy hình vuông $\implies AC = a\sqrt{2}$. $\tan \alpha = \frac{SA}{AC} = \frac{a\sqrt{3}}{a\sqrt{2}} = \frac{\sqrt{6}}{2} \neq \sqrt{3} \implies \alpha \neq 60^\circ$."},
                {"label": "c", "text": r"Thể tích của khối chóp $S.ABCD$ bằng $V = \frac{a^3\sqrt{3}}{3}$.", "correct": True, "explanation": r"Đúng. $V = \frac{1}{3} S_{ABCD} \cdot SA = \frac{1}{3} \cdot a^2 \cdot a\sqrt{3} = \frac{a^3\sqrt{3}}{3}$."},
                {"label": "d", "text": r"Khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ bằng $\frac{a\sqrt{3}}{2}$.", "correct": True, "explanation": r"Đúng. Kẻ $AH \perp SB$ tại $H$. Do $BC \perp (SAB) \implies BC \perp AH \implies AH \perp (SBC)$. Trong tam giác vuông $SAB$: $\frac{1}{AH^2} = \frac{1}{SA^2} + \frac{1}{AB^2} = \frac{1}{3a^2} + \frac{1}{a^2} = \frac{4}{3a^2} \implies AH = \frac{a\sqrt{3}}{2}$."}
            ]
        },
        {
            "id": 4,
            "context": r"Hai xạ thủ độc lập cùng bắn vào một tấm bia, mỗi người bắn 1 viên. Xác suất bắn trúng bia của người thứ nhất là $P(A) = 0.8$, xác suất bắn trúng của người thứ hai là $P(B) = 0.7$.",
            "sub_questions": [
                {"label": "a", "text": r"Xác suất để cả hai người đều bắn trượt là 0.06.", "correct": True, "explanation": r"Đúng. $P(\overline{A}\overline{B}) = P(\overline{A}) \cdot P(\overline{B}) = (1 - 0.8)(1 - 0.7) = 0.2 \times 0.3 = 0.06$."},
                {"label": "b", "text": r"Xác suất để cả hai người đều bắn trúng là 0.56.", "correct": True, "explanation": r"Đúng. Do độc lập nên $P(AB) = 0.8 \times 0.7 = 0.56$."},
                {"label": "c", "text": r"Xác suất để có ít nhất một người bắn trúng bia là 0.94.", "correct": True, "explanation": r"Đúng. Biến cố đối của 'cả hai bắn trượt': $1 - 0.06 = 0.94$."},
                {"label": "d", "text": r"Xác suất để chỉ có đúng một người bắn trúng bia là 0.40.", "correct": False, "explanation": r"Sai. $P = P(A)\overline{B} + P(\overline{A})B = 0.8 \times 0.3 + 0.2 \times 0.7 = 0.24 + 0.14 = 0.38$."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Cho hàm số $f(x) = \ln(x^2 + 1)$. Tính giá trị của đạo hàm $f'(1)$.",
            "answer": "1",
            "unit": "",
            "method": "Đạo hàm ln(u) = u'/u",
            "explanation": r"$f'(x) = \frac{(x^2 + 1)'}{x^2 + 1} = \frac{2x}{x^2 + 1}$. Thay $x = 1 \implies f'(1) = \frac{2(1)}{1^2 + 1} = \frac{2}{2} = 1$."
        },
        {
            "id": 2,
            "question": r"Tìm nghiệm của phương trình $2^{2x - 1} = 32$.",
            "answer": "3",
            "unit": "",
            "method": "Đưa về cùng cơ số",
            "explanation": r"$2^{2x - 1} = 32 = 2^5 \iff 2x - 1 = 5 \iff 2x = 6 \iff x = 3$."
        },
        {
            "id": 3,
            "question": r"Một chất điểm chuyển động thẳng xác định bởi phương trình $s(t) = t^3 - 3t^2 + 9t + 2$, trong đó $t$ tính bằng giây và $s$ tính bằng mét. Tính gia tốc của chất điểm tại thời điểm $t = 3$ giây (đơn vị: $\text{m/s}^2$).",
            "answer": "12",
            "unit": "m/s²",
            "method": "Gia tốc là đạo hàm cấp 2: a(t) = s''(t)",
            "explanation": r"Vận tốc $v(t) = s'(t) = 3t^2 - 6t + 9$. Gia tốc $a(t) = v'(t) = s''(t) = 6t - 6$. Tại $t = 3 \implies a(3) = 6(3) - 6 = 18 - 6 = 12\text{ m/s}^2$."
        },
        {
            "id": 4,
            "question": r"Một người gửi tiết kiệm số tiền 100 triệu đồng vào ngân hàng với lãi suất $6\%$/năm theo hình thức lãi kép hàng năm. Hỏi sau ít nhất bao nhiêu năm người đó sẽ thu được số tiền cả gốc lẫn lãi từ 200 triệu đồng trở lên?",
            "answer": "12",
            "unit": "năm",
            "method": "Bài toán lãi kép mũ",
            "explanation": r"Số tiền nhận được sau $n$ năm là $A = 100(1 + 0.06)^n = 100(1.06)^n$. Để $A \ge 200 \iff 1.06^n \ge 2 \iff n \ge \log_{1.06} 2 \approx \frac{0.69315}{0.05827} \approx 11.895$. Do $n$ là số nguyên năm nên cần ít nhất 12 năm."
        },
        {
            "id": 5,
            "question": r"Cho hình chóp tam giác $S.ABC$ có đáy là tam giác vuông cân tại $B$, $BA = BC = 2\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA = 2\text{ cm}$. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ (đơn vị: $\text{cm}$, làm tròn đến hai chữ số thập phân).",
            "answer": "1.41",
            "unit": "cm",
            "method": "Khoảng cách từ chân đường cao đến mặt bên",
            "explanation": r"Do $BC \perp AB$ và $BC \perp SA \implies BC \perp (SAB)$. Kẻ $AH \perp SB$ tại $H \implies AH \perp (SBC)$. Khoảng cách là $d(A, (SBC)) = AH$. Trong tam giác vuông cân $SAB$ có $SA = AB = 2 \implies AH = \frac{SA \cdot AB}{\sqrt{SA^2 + AB^2}} = \frac{2 \times 2}{\sqrt{4 + 4}} = \frac{4}{2\sqrt{2}} = \sqrt{2} \approx 1.41\text{ cm}$."
        },
        {
            "id": 6,
            "question": r"Một hộp đựng 5 viên bi màu xanh và 7 viên bi màu đỏ có cùng kích thước. Lấy ngẫu nhiên lần lượt 2 viên bi không hoàn lại. Tính xác suất để cả 2 viên bi lấy ra đều có màu xanh (viết kết quả làm tròn đến hai chữ số thập phân).",
            "answer": "0.15",
            "unit": "",
            "method": "Xác suất lấy lần lượt không hoàn lại",
            "explanation": r"Xác suất lấy viên 1 màu xanh là $\frac{5}{12}$. Sau đó trong hộp còn 4 viên xanh và 7 viên đỏ (tổng 11 viên). Xác suất lấy viên 2 màu xanh là $\frac{4}{11}$. Xác suất cả 2 viên xanh là $P = \frac{5}{12} \times \frac{4}{11} = \frac{20}{132} = \frac{5}{33} \approx 0.1515... \approx 0.15$."
        }
    ]
}
