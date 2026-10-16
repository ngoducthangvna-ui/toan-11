# -*- coding: utf-8 -*-
"""
Đề thi Cuối Học Kì 2 - Đề số 2 (Chuẩn Format 90 phút Hưng Yên / GDPT 2018)
Phạm vi: Trọn bộ Tập 2 (Chương 6 đến Chương 9: Mũ & Logarit, Đạo hàm, Không gian vuông góc, Xác suất)
Tác giả: Antigravity AI
"""

DE_CUOI_KI_2_DE_2 = {
    "id": "de-cuoi-ki-2-de-2",
    "slug": "de-thi-cuoi-ki-2-de-so-2-toan-11",
    "title": "Đề thi Cuối Học Kì 2 - Đề số 2 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Cuối Học Kì 2",
    "subtitle": "Phạm vi: Toàn diện Tập 2 (Chương 6 đến Chương 9 - Mũ & Logarit, Đạo hàm, Không gian vuông góc & Xác suất)",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Hàm số Mũ & Hàm số Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Đạo hàm & Phương trình Tiếp tuyến", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Quan hệ vuông góc & Thể tích không gian", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"},
        {"topic": "Xác suất cổ điển & Quy tắc nhân", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "matrix_table": [
        {"topic": "Hàm số Mũ & Logarit", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Đạo hàm & Tiếp tuyến", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Hình học không gian & Thể tích", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm"},
        {"topic": "Quy tắc xác suất", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT XỬ LÝ ĐỀ SỐ 2 CUỐI HỌC KÌ 2:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm. Giải nhanh câu công thức thể tích lăng trụ $V = B \cdot h$, thể tích chóp $V = \frac{1}{3}B \cdot h$, tập xác định hàm lũy thừa và logarit.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai. Đọc kĩ bài toán chu kỳ bán rã, hình lập phương $ABCD.A'B'C'D'$, chọn học sinh tổ hợp xác suất.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Tính vận tốc vật rơi tự do $v(t) = s'(t)$, hệ số góc tiếp tuyến, thể tích lăng trụ tam giác đều.</li>
        <li><strong>85 - 90 phút:</strong> Rà soát lại từng con số, đảm bảo làm tròn theo đúng yêu cầu (2 chữ số thập phân).</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Với số thực $a > 0$ và $a \neq 1$, giá trị của biểu thức $\log_a(a^4)$ bằng:",
            "options": ["A. 4", "B. $\frac{1}{4}$", "C. $a^4$", "D. 1"],
            "correct": 0,
            "method": "Tính chất logarit cơ bản",
            "explanation": r"Theo tính chất $\log_a(a^\alpha) = \alpha$, ta có $\log_a(a^4) = 4$."
        },
        {
            "id": 2,
            "question": r"Tập xác định của hàm số $y = (x - 2)^{-3}$ là:",
            "options": [
                r"A. $\mathbb{R} \setminus \{2\}$",
                r"B. $(2; +\infty)$",
                r"C. $[2; +\infty)$",
                r"D. $\mathbb{R}$"
            ],
            "correct": 0,
            "method": "Tập xác định hàm lũy thừa với số mũ nguyên âm",
            "explanation": r"Hàm số lũy thừa $y = u^\alpha$ với $\alpha$ là số nguyên âm xác định khi $u \neq 0 \iff x - 2 \neq 0 \iff x \neq 2$."
        },
        {
            "id": 3,
            "question": r"Nghiệm của phương trình $3^{x + 1} = 27$ là:",
            "options": ["A. $x = 2$", "B. $x = 3$", "C. $x = 1$", "D. $x = 4$"],
            "correct": 0,
            "method": "Phương trình mũ cơ bản",
            "explanation": r"$3^{x + 1} = 27 = 3^3 \iff x + 1 = 3 \iff x = 2$."
        },
        {
            "id": 4,
            "question": r"Đạo hàm của hàm số $y = \cos(2x - 1)$ là:",
            "options": [
                r"A. $y' = -2\sin(2x - 1)$",
                r"B. $y' = 2\sin(2x - 1)$",
                r"C. $y' = -\sin(2x - 1)$",
                r"D. $y' = -2\cos(2x - 1)$"
            ],
            "correct": 0,
            "method": "Đạo hàm hàm hợp cos(u)",
            "explanation": r"$(\cos u)' = -u' \cdot \sin u \implies (\cos(2x-1))' = -(2x-1)' \cdot \sin(2x-1) = -2\sin(2x-1)$."
        },
        {
            "id": 5,
            "question": r"Đạo hàm của hàm số $y = \sqrt{2x + 1}$ là:",
            "options": [
                r"A. $y' = \frac{1}{\sqrt{2x + 1}}$",
                r"B. $y' = \frac{2}{\sqrt{2x + 1}}$",
                r"C. $y' = \frac{1}{2\sqrt{2x + 1}}$",
                r"D. $y' = \sqrt{2x + 1}$"
            ],
            "correct": 0,
            "method": "Đạo hàm sqrt(u)",
            "explanation": r"$(\sqrt{u})' = \frac{u'}{2\sqrt{u}} = \frac{2}{2\sqrt{2x+1}} = \frac{1}{\sqrt{2x+1}}$."
        },
        {
            "id": 6,
            "question": r"Cho hình chóp $S.ABC$ có đáy $ABC$ vuông tại $B$ và $SA \perp (ABC)$. Khẳng định nào sau đây là đúng?",
            "options": [
                r"A. $(SBC) \perp (SAB)$",
                r"B. $(SBC) \perp (SAC)$",
                r"C. $(SAB) \perp (SAC)$",
                r"D. $(ABC) \perp (SBC)$"
            ],
            "correct": 0,
            "method": "Chứng minh hai mặt phẳng vuông góc",
            "explanation": r"Vì $BC \perp AB$ và $BC \perp SA \implies BC \perp (SAB)$. Do $BC \subset (SBC)$ nên $(SBC) \perp (SAB)$."
        },
        {
            "id": 7,
            "question": r"Khoảng cách từ một điểm $M$ đến mặt phẳng $(\alpha)$ là:",
            "options": [
                "A. Độ dài đoạn thẳng vuông góc kẻ từ $M$ đến $(\alpha)$",
                "B. Độ dài đoạn thẳng bất kì nối $M$ với một điểm thuộc $(\alpha)$",
                "C. Khoảng cách từ $M$ đến một đường thẳng bất kì trong $(\alpha)$",
                "D. Bán kính mặt cầu tâm $M$ cắt $(\alpha)$"
            ],
            "correct": 0,
            "method": "Định nghĩa khoảng cách",
            "explanation": r"Khoảng cách từ điểm $M$ đến mặt phẳng $(\alpha)$ là độ dài đoạn thẳng $MH$, với $H$ là hình chiếu vuông góc của $M$ lên $(\alpha)$."
        },
        {
            "id": 8,
            "question": r"Cho $A$ và $B$ là hai biến cố xung khắc. Khẳng định nào sau đây là đúng?",
            "options": [
                r"A. $P(A \cup B) = P(A) + P(B)$",
                r"B. $P(A \cup B) = P(A) \cdot P(B)$",
                r"C. $P(AB) = P(A) \cdot P(B)$",
                r"D. $P(A \cup B) = P(A) + P(B) - P(AB)$"
            ],
            "correct": 0,
            "method": "Quy tắc cộng biến cố xung khắc",
            "explanation": r"Khi $A$ và $B$ xung khắc thì $AB = \emptyset \implies P(AB) = 0$, do đó $P(A \cup B) = P(A) + P(B)$."
        },
        {
            "id": 9,
            "question": r"Cho khối lăng trụ có diện tích đáy $B = 10\text{ cm}^2$ và chiều cao $h = 6\text{ cm}$. Thể tích của khối lăng trụ đó là:",
            "options": [r"A. $60\text{ cm}^3$", r"B. $20\text{ cm}^3$", r"C. $30\text{ cm}^3$", r"D. $180\text{ cm}^3$"],
            "correct": 0,
            "method": "Thể tích khối lăng trụ V = Bh",
            "explanation": r"$V = B \cdot h = 10 \times 6 = 60\text{ cm}^3$."
        },
        {
            "id": 10,
            "question": r"Nghiệm của phương trình $\log_3(2x - 5) = \log_3(x + 1)$ là:",
            "options": ["A. $x = 6$", "B. $x = 4$", "C. $x = 5$", "D. Vô nghiệm"],
            "correct": 0,
            "method": "Giải phương trình logarit cùng cơ số",
            "explanation": r"Phương trình $\iff 2x - 5 = x + 1 \iff x = 6$. Thử lại $6 + 1 = 7 > 0$ (thỏa mãn điều kiện)."
        },
        {
            "id": 11,
            "question": r"Đạo hàm của hàm số $y = x \cdot e^x$ là:",
            "options": [
                r"A. $y' = (x + 1)e^x$",
                r"B. $y' = e^x$",
                r"C. $y' = x e^x$",
                r"D. $y' = (x - 1)e^x$"
            ],
            "correct": 0,
            "method": "Đạo hàm của tích (uv)' = u'v + uv'",
            "explanation": r"$y' = (x)' \cdot e^x + x \cdot (e^x)' = 1 \cdot e^x + x \cdot e^x = (x + 1)e^x$."
        },
        {
            "id": 12,
            "question": r"Thể tích của khối chóp có diện tích đáy $B = 15\text{ cm}^2$ và chiều cao $h = 4\text{ cm}$ bằng:",
            "options": [r"A. $20\text{ cm}^3$", r"B. $60\text{ cm}^3$", r"C. $30\text{ cm}^3$", r"D. $10\text{ cm}^3$"],
            "correct": 0,
            "method": "Thể tích chóp V = 1/3 Bh",
            "explanation": r"$V = \frac{1}{3} B \cdot h = \frac{1}{3} \times 15 \times 4 = 20\text{ cm}^3$."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Cho hàm số $f(x) = x^3 - 3x^2 + 2$ có đồ thị là $(C)$.",
            "sub_questions": [
                {"label": "a", "text": r"Đạo hàm của hàm số là $f'(x) = 3x^2 - 6x$.", "correct": True, "explanation": r"Đúng. $f'(x) = 3x^2 - 6x$."},
                {"label": "b", "text": r"Phương trình $f'(x) = 0$ có hai nghiệm phân biệt là $x = 0$ và $x = 2$.", "correct": True, "explanation": r"Đúng. $3x(x - 2) = 0 \iff x = 0$ hoặc $x = 2$."},
                {"label": "c", "text": r"Hệ số góc của tiếp tuyến của $(C)$ tại điểm có hoành độ $x = -1$ bằng 9.", "correct": True, "explanation": r"Đúng. $k = f'(-1) = 3(-1)^2 - 6(-1) = 3 + 6 = 9$."},
                {"label": "d", "text": r"Phương trình tiếp tuyến của $(C)$ tại giao điểm với trục tung là $y = 2x$.", "correct": False, "explanation": r"Sai. Giao điểm với trục tung $x = 0 \implies y = 2$. Hệ số góc $k = f'(0) = 0$. Phương trình tiếp tuyến là $y = 2$."}
            ]
        },
        {
            "id": 2,
            "context": r"Một chất phóng xạ có khối lượng ban đầu $m_0 = 100\text{ gam}$, sau thời gian $t$ (năm) khối lượng còn lại $m(t)$ tuân theo quy luật phân rã: $m(t) = m_0 \cdot \left(\frac{1}{2}\right)^{t / 24}$, trong đó chu kỳ bán rã là 24 năm.",
            "sub_questions": [
                {"label": "a", "text": r"Sau 24 năm, khối lượng chất phóng xạ còn lại là 50 gam.", "correct": True, "explanation": r"Đúng. $m(24) = 100 \cdot (1/2)^1 = 50\text{ gam}$."},
                {"label": "b", "text": r"Sau 48 năm, khối lượng chất phóng xạ còn lại là 25 gam.", "correct": True, "explanation": r"Đúng. $m(48) = 100 \cdot (1/2)^2 = 100 \times 1/4 = 25\text{ gam}$."},
                {"label": "c", "text": r"Thời gian để khối lượng chất phóng xạ còn lại đúng 12.5 gam là 72 năm.", "correct": True, "explanation": r"Đúng. $100 \cdot (1/2)^{t/24} = 12.5 \iff (1/2)^{t/24} = 1/8 = (1/2)^3 \iff t/24 = 3 \iff t = 72$ năm."},
                {"label": "d", "text": r"Sau 12 năm, khối lượng chất phóng xạ bị phân rã mất một nửa.", "correct": False, "explanation": r"Sai. Cần 24 năm (chu kỳ bán rã) để khối lượng phân rã mất một nửa, sau 12 năm còn lại $100 / \sqrt{2} \approx 70.7\text{ gam}$."}
            ]
        },
        {
            "id": 3,
            "context": r"Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$.",
            "sub_questions": [
                {"label": "a", "text": r"Đường chéo $AC$ vuông góc với đường chéo $BD$ của hình vuông đáy.", "correct": True, "explanation": r"Đúng. Hai đường chéo của hình vuông luôn vuông góc với nhau."},
                {"label": "b", "text": r"Đường thẳng $BD$ vuông góc với mặt phẳng $(ACC'A')$.", "correct": True, "explanation": r"Đúng. Vì $BD \perp AC$ và $BD \perp AA' \implies BD \perp (ACC'A')$."},
                {"label": "c", "text": r"Góc giữa hai đường thẳng $A'B$ và $CD$ bằng $45^\circ$.", "correct": True, "explanation": r"Đúng. Do $CD // AB$ nên góc giữa $A'B$ và $CD$ là góc giữa $A'B$ và $AB$, tức là góc $\widehat{A'BA} = 45^\circ$ trong tam giác vuông cân $A'AB$."},
                {"label": "d", "text": r"Thể tích của khối tứ diện $A.A'B'D'$ bằng $\frac{a^3}{3}$.", "correct": False, "explanation": r"Sai. $V = \frac{1}{3} S_{A'B'D'} \cdot AA' = \frac{1}{3} \cdot \left(\frac{1}{2}a^2\right) \cdot a = \frac{a^3}{6}$."}
            ]
        },
        {
            "id": 4,
            "context": r"Một nhóm học sinh gồm 6 bạn nam và 4 bạn nữ. Chọn ngẫu nhiên đồng thời 3 bạn đi dự đại hội thanh niên tiên tiến.",
            "sub_questions": [
                {"label": "a", "text": r"Số phần tử của không gian mẫu là $n(\Omega) = 120$.", "correct": True, "explanation": r"Đúng. $C_{10}^3 = \frac{10 \times 9 \times 8}{6} = 120$."},
                {"label": "b", "text": r"Xác suất để cả 3 bạn được chọn đều là nữ bằng $\frac{1}{30}$.", "correct": True, "explanation": r"Đúng. Số cách chọn 3 nữ là $C_4^3 = 4$. Xác suất $P = \frac{4}{120} = \frac{1}{30}$."},
                {"label": "c", "text": r"Số cách chọn 3 bạn trong đó có cả nam và nữ là 96 cách.", "correct": True, "explanation": r"Đúng. Chọn 3 nam: $C_6^3 = 20$. Chọn 3 nữ: $C_4^3 = 4$. Số cách có cả nam và nữ: $120 - 20 - 4 = 96$ cách."},
                {"label": "d", "text": r"Xác suất để có ít nhất 1 bạn nữ được chọn là 0.75.", "correct": False, "explanation": r"Sai. Biến cố đối: cả 3 bạn đều nam $\implies P = 1 - \frac{C_6^3}{120} = 1 - \frac{20}{120} = 1 - \frac{1}{6} = \frac{5}{6} \approx 0.83$."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Cho hàm số $y = \frac{x + 2}{x - 1}$ có đồ thị $(C)$. Tìm hệ số góc $k$ của tiếp tuyến với $(C)$ tại điểm có hoành độ $x_0 = 2$.",
            "answer": "-3",
            "unit": "",
            "method": "Hệ số góc k = y'(x0)",
            "explanation": r"$y' = \frac{1(x - 1) - (x + 2)(1)}{(x - 1)^2} = \frac{-3}{(x - 1)^2}$. Tại $x_0 = 2 \implies k = y'(2) = \frac{-3}{(2 - 1)^2} = -3$."
        },
        {
            "id": 2,
            "question": r"Tìm nghiệm của phương trình $\log_5(x^2 - 4x + 9) = 1$.",
            "answer": "2",
            "unit": "",
            "method": "Phương trình logarit đưa về bậc hai",
            "explanation": r"$\log_5(x^2 - 4x + 9) = 1 \iff x^2 - 4x + 9 = 5^1 = 5 \iff x^2 - 4x + 4 = 0 \iff (x - 2)^2 = 0 \iff x = 2$."
        },
        {
            "id": 3,
            "question": r"Một vật rơi tự do không vận tốc đầu từ độ cao xác định theo phương trình chuyển động $s(t) = \frac{1}{2}gt^2$ với gia tốc trọng trường $g = 9.8\text{ m/s}^2$. Tính vận tốc tức thời của vật tại thời điểm $t = 5$ giây kể từ khi bắt đầu rơi (đơn vị: $\text{m/s}$).",
            "answer": "49",
            "unit": "m/s",
            "method": "Vận tốc tức thời v(t) = s'(t)",
            "explanation": r"Vận tốc $v(t) = s'(t) = gt$. Tại $t = 5\text{ s} \implies v(5) = 9.8 \times 5 = 49\text{ m/s}$."
        },
        {
            "id": 4,
            "question": r"Cho hình lăng trụ tam giác đều $ABC.A'B'C'$ có tất cả các cạnh đều bằng $4\text{ cm}$. Tính thể tích của khối lăng trụ đó (đơn vị: $\text{cm}^3$, làm tròn đến hai chữ số thập phân).",
            "answer": "27.71",
            "unit": "cm³",
            "method": "Thể tích lăng trụ tam giác đều V = Bh",
            "explanation": r"Đáy $ABC$ là tam giác đều cạnh 4: $S_{ABC} = \frac{4^2\sqrt{3}}{4} = 4\sqrt{3}\text{ cm}^2$. Chiều cao lăng trụ bằng độ dài cạnh bên $h = AA' = 4\text{ cm}$. Thể tích $V = B \cdot h = 4\sqrt{3} \times 4 = 16\sqrt{3} \approx 27.7128... \approx 27.71\text{ cm}^3$."
        },
        {
            "id": 5,
            "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = 3\text{ cm}, AD = 4\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA = 5\text{ cm}$. Tính thể tích khối chóp $S.ABCD$ (đơn vị: $\text{cm}^3$).",
            "answer": "20",
            "unit": "cm³",
            "method": "Thể tích chóp V = 1/3 Bh",
            "explanation": r"Diện tích đáy hình chữ nhật: $S_{ABCD} = 3 \times 4 = 12\text{ cm}^2$. Chiều cao $h = SA = 5\text{ cm}$. Thể tích: $V = \frac{1}{3} S_{ABCD} \cdot SA = \frac{1}{3} \times 12 \times 5 = 20\text{ cm}^3$."
        },
        {
            "id": 6,
            "question": r"Gieo hai con xúc xắc cân đối và đồng chất. Tính xác suất để tổng số chấm xuất hiện trên hai mặt của hai con xúc xắc bằng 8 (viết kết quả làm tròn đến hai chữ số thập phân).",
            "answer": "0.14",
            "unit": "",
            "method": "Xác suất cổ điển gieo xúc xắc",
            "explanation": r"Không gian mẫu $n(\Omega) = 6 \times 6 = 36$. Các cặp số có tổng bằng 8 là: $(2; 6), (3; 5), (4; 4), (5; 3), (6; 2) \implies$ có 5 cặp thuận lợi. Xác suất $P = \frac{5}{36} \approx 0.1388... \approx 0.14$."
        }
    ]
}
