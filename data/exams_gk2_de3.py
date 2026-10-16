# -*- coding: utf-8 -*-
"""Đề thi Giữa Học Kì 2 - Đề số 3 (Chuẩn 90 phút Hưng Yên)"""

EXAM_GK2_DE3 = {
    "id": "de-giua-ki-2-de-3",
    "slug": "de-thi-giua-ki-2-de-3",
    "title": "Đề thi Giữa Học Kì 2 - Đề số 3 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Giữa Học Kì 2",
    "subtitle": "Phạm vi: Đề phân hóa toàn diện Giữa kì 2 (Mũ, Logarit, Đạo hàm & Hình không gian)",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Mũ, Logarit & Ứng dụng thực tế", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm (40%)"},
        {"topic": "Đạo hàm & Ứng dụng vận tốc", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm (30%)"},
        {"topic": "Hình học không gian (Góc & Khoảng cách)", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm (30%)"}
    ],
    "matrix_table": [
        {"topic": "Mũ, Logarit & Ứng dụng", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm"},
        {"topic": "Đạo hàm & Vận tốc", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"},
        {"topic": "Hình không gian vuông góc", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> ĐỀ PHÂN HÓA HƯNG YÊN - CHIẾN LƯỢC ĐẠT ĐIỂM TỐI ĐA:</h6>
    <ul class="mb-0 small">
        <li><strong>Hình học không gian:</strong> Sử dụng mô hình 3D trong đầu hoặc vẽ hình chuẩn: nhớ góc giữa đường thẳng và mặt phẳng bằng góc giữa đường thẳng đó và hình chiếu của nó lên mặt phẳng.</li>
        <li><strong>Phương trình tiếp tuyến song song đường thẳng:</strong> $f'(x_0) = k_{song\_song}$. Giải tìm $x_0$ rồi viết PTTT, nhớ kiểm tra điều kiện trùng!</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Cho hình lập phương $ABCD.A'B'C'D'$. Đường thẳng nào sau đây vuông góc với mặt phẳng $(ABCD)$?",
            "options": ["A. $AA'$", "B. $AC$", "C. $A'B'$", "D. $B'D'$"],
            "correct": 0,
            "method": "Đặc điểm hình lập phương",
            "explanation": r"Trong hình lập phương, các cạnh bên $AA', BB', CC', DD'$ vuông góc với hai mặt phẳng đáy."
        },
        {
            "id": 2,
            "question": r"Đạo hàm của hàm số $y = 3^x$ là:",
            "options": [r"A. $3^x \ln 3$", r"B. $\frac{3^x}{\ln 3}$", r"C. $x \cdot 3^{x - 1}$", r"D. $3^x$"],
            "correct": 0,
            "method": "Đạo hàm hàm mũ",
            "explanation": r"Công thức chuẩn: $(a^x)' = a^x \ln a$. Do đó $(3^x)' = 3^x \ln 3$."
        },
        {
            "id": 3,
            "question": r"Biểu thức $\log_a\left(\frac{x}{y}\right)$ (với $a, x, y > 0, a \neq 1$) bằng:",
            "options": [
                r"A. $\log_a x - \log_a y$",
                r"B. $\frac{\log_a x}{\log_a y}$",
                r"C. $\log_a x + \log_a y$",
                r"D. $\log_a(x - y)$"
            ],
            "correct": 0,
            "method": "Tính chất logarit",
            "explanation": r"Logarit của một thương bằng hiệu các logarit: $\log_a(x/y) = \log_a x - \log_a y$."
        },
        {
            "id": 4,
            "question": r"Cho hình chóp đều $S.ABCD$. Góc giữa đường thẳng $SO$ và mặt đáy $(ABCD)$ bằng:",
            "options": [r"A. $90^\circ$", r"B. $60^\circ$", r"C. $45^\circ$", r"D. $30^\circ$"],
            "correct": 0,
            "method": "Chóp đều",
            "explanation": r"Trong hình chóp đều, $SO$ vuông góc với mặt đáy nên góc giữa $SO$ và đáy là $90^\circ$."
        },
        {
            "id": 5,
            "question": r"Đạo hàm của hàm số $y = \cos x$ là:",
            "options": [r"A. $-\sin x$", r"B. $\sin x$", r"C. $-\cos x$", r"D. $\frac{1}{\cos^2 x}$"],
            "correct": 0,
            "method": "Đạo hàm lượng giác",
            "explanation": r"$(\cos x)' = -\sin x$."
        },
        {
            "id": 6,
            "question": r"Cho số thực dương $a$. Biểu thức $\sqrt{a \sqrt{a}}$ viết dưới dạng lũy thừa với số mũ hữu tỉ là:",
            "options": [r"A. $a^{3/4}$", r"B. $a^{1/4}$", r"C. $a^{1/2}$", r"D. $a^{3/2}$"],
            "correct": 0,
            "method": "Lũy thừa hữu tỉ",
            "explanation": r"$\sqrt{a \cdot a^{1/2}} = \sqrt{a^{3/2}} = (a^{3/2})^{1/2} = a^{3/4}$."
        },
        {
            "id": 7,
            "question": r"Cho hình chóp $S.ABC$ có $SA \perp (ABC)$. Hình chiếu vuông góc của đường thẳng $SB$ lên mặt phẳng $(ABC)$ là:",
            "options": ["A. Đoạn thẳng $AB$", "B. Đoạn thẳng $BC$", "C. Đoạn thẳng $AC$", "D. Điểm $A$"],
            "correct": 0,
            "method": "Hình chiếu vuông góc",
            "explanation": r"Hình chiếu của $S$ lên $(ABC)$ là $A$, hình chiếu của $B$ là chính nó. Vậy hình chiếu của $SB$ là $AB$."
        },
        {
            "id": 8,
            "question": r"Đạo hàm của hàm số $y = \frac{1}{x}$ (với $x \neq 0$) là:",
            "options": [r"A. $-\frac{1}{x^2}$", r"B. $\frac{1}{x^2}$", r"C. $\ln x$", r"D. $-\frac{1}{x}$"],
            "correct": 0,
            "method": "Công thức cơ bản",
            "explanation": r"$(1/x)' = -1/x^2$."
        },
        {
            "id": 9,
            "question": r"Bất phương trình $e^x > 1$ có tập nghiệm là:",
            "options": [r"A. $(0; +\infty)$", r"B. $[0; +\infty)$", r"C. $(-\infty; 0)$", r"D. $(1; +\infty)$"],
            "correct": 0,
            "method": "Bất phương trình e^x",
            "explanation": r"$e^x > 1 = e^0 \iff x > 0$."
        },
        {
            "id": 10,
            "question": r"Nếu đường thẳng $a$ vuông góc với hai đường thẳng cắt nhau cùng nằm trong mặt phẳng $(P)$ thì:",
            "options": [
                r"A. $a \perp (P)$",
                "B. $a // (P)$",
                r"C. $a \subset (P)$",
                r"D. $a$ tạo với $(P)$ góc $45^\circ$"
            ],
            "correct": 0,
            "method": "Định lí đường vuông góc mặt",
            "explanation": r"Định lí cơ bản: Một đường thẳng vuông góc với hai đường thẳng cắt nhau trong mặt phẳng thì vuông góc với mặt phẳng đó."
        },
        {
            "id": 11,
            "question": r"Đạo hàm của hàm số $y = x^2 \sin x$ là:",
            "options": [
                r"A. $2x\sin x + x^2\cos x$",
                r"B. $2x\cos x$",
                r"C. $x^2\cos x$",
                r"D. $2x\sin x - x^2\cos x$"
            ],
            "correct": 0,
            "method": "Đạo hàm tích",
            "explanation": r"$y' = (x^2)'\sin x + x^2(\sin x)' = 2x\sin x + x^2\cos x$."
        },
        {
            "id": 12,
            "question": r"Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ là:",
            "options": [
                "A. Độ dài đoạn vuông góc kẻ từ $M$ đến $(P)$",
                "B. Độ dài đoạn thẳng bất kì nối $M$ với một điểm trên $(P)$",
                "C. Độ lớn góc giữa $M$ và $(P)$",
                "D. Khoảng cách ngắn nhất từ $M$ đến gốc tọa độ"
            ],
            "correct": 0,
            "method": "Khái niệm khoảng cách",
            "explanation": r"Khoảng cách từ điểm đến mặt phẳng là độ dài đoạn thẳng vuông góc hạ từ điểm đó xuống mặt phẳng."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Cho hàm số $f(x) = x^3 - 3x^2 + 2$.",
            "sub_questions": [
                {"label": "a", "text": r"Đạo hàm của hàm số là $f'(x) = 3x^2 - 6x$.", "correct": True, "explanation": r"Đúng."},
                {"label": "b", "text": r"Phương trình $f'(x) = 0$ có hai nghiệm là $x = 0$ và $x = 2$.", "correct": True, "explanation": r"Đúng. $3x(x - 2) = 0 \iff x = 0$ hoặc $x = 2$."},
                {"label": "c", "text": r"Tiếp tuyến của đồ thị tại điểm uốn $I(1; 0)$ có hệ số góc bằng -3.", "correct": True, "explanation": r"Đúng. $f'(1) = 3(1)^2 - 6(1) = -3$."},
                {"label": "d", "text": r"Có 2 tiếp tuyến của đồ thị song song với trục hoành.", "correct": True, "explanation": r"Đúng. Trục hoành có hệ số góc $k = 0$. $f'(x) = 0$ có 2 nghiệm $x = 0$ và $x = 2$ cho ra 2 tiếp tuyến $y = 2$ và $y = -2$."}
            ]
        },
        {
            "id": 2,
            "context": r"Nồng độ thuốc trong máu của một bệnh nhân sau $t$ giờ kể từ khi uống được mô hình hóa bởi hàm số $C(t) = 4t \cdot e^{-0.5t}$ (mg/L).",
            "sub_questions": [
                {"label": "a", "text": r"Tại thời điểm ban đầu $t = 0$, nồng độ thuốc trong máu bằng 0.", "correct": True, "explanation": r"Đúng. $C(0) = 0$."},
                {"label": "b", "text": r"Đạo hàm của hàm số là $C'(t) = 4e^{-0.5t}(1 - 0.5t)$.", "correct": True, "explanation": r"Đúng. Áp dụng quy tắc đạo hàm của tích: $4e^{-0.5t} + 4t(-0.5e^{-0.5t}) = 4e^{-0.5t}(1 - 0.5t)$."},
                {"label": "c", "text": r"Nồng độ thuốc trong máu đạt cực đại sau đúng 2 giờ kể từ khi uống.", "correct": True, "explanation": r"Đúng. $C'(t) = 0 \iff 1 - 0.5t = 0 \iff t = 2$ giờ."},
                {"label": "d", "text": r"Nồng độ thuốc cao nhất trong máu vượt quá 3.5 mg/L.", "correct": False, "explanation": r"Sai. $C(2) = 4(2)e^{-1} = \frac{8}{e} \approx \frac{8}{2.718} \approx 2.94$ mg/L $< 3.5$ mg/L."}
            ]
        },
        {
            "id": 3,
            "context": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$, $SA \perp (ABC)$ và $SA = a$.",
            "sub_questions": [
                {"label": "a", "text": r"Đường thẳng $SA$ vuông góc với cạnh $BC$.", "correct": True, "explanation": r"Đúng. Do $SA \perp (ABC)$ mà $BC \subset (ABC)$."},
                {"label": "b", "text": r"Gọi $M$ là trung điểm $BC$, khi đó $BC \perp (SAM)$.", "correct": True, "explanation": r"Đúng. $BC \perp AM$ (đường cao tam giác đều) và $BC \perp SA \implies BC \perp (SAM)$."},
                {"label": "c", "text": r"Góc giữa mặt phẳng $(SBC)$ và mặt phẳng đáy $(ABC)$ là góc $\widehat{SMA}$.", "correct": True, "explanation": r"Đúng. Do $AM \perp BC$ và $SM \perp BC$."},
                {"label": "d", "text": r"Số đo góc $\widehat{SMA}$ bằng $45^\circ$.", "correct": False, "explanation": r"Sai. $AM = \frac{a\sqrt{3}}{2}$, $\tan\widehat{SMA} = \frac{SA}{AM} = \frac{a}{a\sqrt{3}/2} = \frac{2}{\sqrt{3}} \neq 1$."}
            ]
        },
        {
            "id": 4,
            "context": r"Cho phương trình $2^{x^2 - 4} = 1$.",
            "sub_questions": [
                {"label": "a", "text": r"Phương trình tương đương với $x^2 - 4 = 0$.", "correct": True, "explanation": r"Đúng. $1 = 2^0 \implies x^2 - 4 = 0$."},
                {"label": "b", "text": r"Phương trình có 2 nghiệm đối xứng nhau qua gốc tọa độ.", "correct": True, "explanation": r"Đúng. $x = \pm 2$."},
                {"label": "c", "text": r"Tích của hai nghiệm bằng -4.", "correct": True, "explanation": r"Đúng. $2 \cdot (-2) = -4$."},
                {"label": "d", "text": r"Tổng bình phương các nghiệm bằng 16.", "correct": False, "explanation": r"Sai. $2^2 + (-2)^2 = 4 + 4 = 8$."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Cho hàm số $y = x^3 - 3x^2 + 1$. Viết phương trình tiếp tuyến của đồ thị hàm số tại điểm có hoành độ $x_0 = 3$. Hệ số tự do của phương trình tiếp tuyến (dạng $y = kx + b$) bằng:",
            "answer": "-26",
            "explanation_steps": [
                r"Tọa độ tiếp điểm: $x_0 = 3 \implies y_0 = 3^3 - 3(3^2) + 1 = 1$.",
                r"Đạo hàm: $y' = 3x^2 - 6x \implies k = y'(3) = 3(9) - 18 = 9$.",
                r"PTTT: $y = 9(x - 3) + 1 = 9x - 27 + 1 = 9x - 26$.",
                r"Hệ số tự do $b = -26$."
            ]
        },
        {
            "id": 2,
            "question": r"Biết đồ thị hàm số $y = a^x$ đi qua điểm $A(2; 9)$. Tìm giá trị của $\log_a 27$:",
            "answer": "3",
            "explanation_steps": [
                r"Thay $A(2; 9)$: $a^2 = 9 \implies a = 3$ (do $a > 0$).",
                r"Vậy $\log_3 27 = \log_3(3^3) = 3$."
            ]
        },
        {
            "id": 3,
            "question": r"Một vật rơi tự do theo phương trình $s(t) = \frac{1}{2}gt^2$ với $g = 9.8\text{ m/s}^2$. Vận tốc tức thời của vật tại thời điểm $t = 5$ giây bằng bao nhiêu m/s?",
            "answer": "49",
            "explanation_steps": [
                r"Vận tốc tức thời: $v(t) = s'(t) = gt$.",
                r"Tại $t = 5$: $v(5) = 9.8 \times 5 = 49$ m/s."
            ]
        },
        {
            "id": 4,
            "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh 3. Cạnh bên $SA \perp (ABCD)$ và $SA = 3\sqrt{3}$. Tính số đo góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ (theo đơn vị độ, làm tròn số nguyên):",
            "answer": "51",
            "explanation_steps": [
                r"Đường chéo hình vuông đáy: $AC = 3\sqrt{2}$.",
                r"Hình chiếu của $SC$ lên $(ABCD)$ là $AC \implies$ góc là $\widehat{SCA}$.",
                r"$\tan\widehat{SCA} = \frac{SA}{AC} = \frac{3\sqrt{3}}{3\sqrt{2}} = \sqrt{\frac{3}{2}} \approx 1.2247$.",
                r"$\widehat{SCA} \approx 50.77^\circ \approx 51^\circ$."
            ]
        },
        {
            "id": 5,
            "question": r"Tìm giá trị của $x$ thỏa mãn: $2\log_3(x - 2) + \log_3(x - 4)^2 = 0$:",
            "answer": "3",
            "explanation_steps": [
                r"ĐKXĐ: $x > 2, x \neq 4$.",
                r"Biến đổi: $\log_3(x - 2)^2 + \log_3(x - 4)^2 = 0 \iff [(x - 2)(x - 4)]^2 = 3^0 = 1$.",
                r"$\iff (x - 2)(x - 4) = 1$ hoặc $(x - 2)(x - 4) = -1$.",
                r"Với $(x - 2)(x - 4) = -1 \iff x^2 - 6x + 8 = -1 \iff x^2 - 6x + 9 = 0 \iff (x - 3)^2 = 0 \implies x = 3$ (thỏa mãn ĐK)."
            ]
        },
        {
            "id": 6,
            "question": r"Cho hàm số $y = \frac{x^2 + 2x - 1}{x - 1}$. Đạo hàm của hàm số tại điểm $x = 2$ có giá trị bằng:",
            "answer": "-1",
            "explanation_steps": [
                r"$y' = \frac{(2x + 2)(x - 1) - (x^2 + 2x - 1)(1)}{(x - 1)^2}$.",
                r"Tại $x = 2$: tử bằng $(4 + 2)(1) - (4 + 4 - 1)(1) = 6 - 7 = -1$. Mẫu bằng $1^2 = 1$. Kết quả là -1."
            ]
        }
    ]
}
