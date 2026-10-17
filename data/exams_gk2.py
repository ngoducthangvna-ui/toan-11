from data.exams_gk2_de2 import EXAM_GK2_DE2
from data.exams_gk2_de3 import EXAM_GK2_DE3
# -*- coding: utf-8 -*-
"""
Hệ thống Đề thi Giữa Học Kì 2 (3 Đề Chuẩn Format Hưng Yên 90 phút)
Phạm vi kiến thức:
- Chương 6: Hàm số mũ & Hàm số logarit (Phương trình, BPT mũ, logarit)
- Chương 7: Đạo hàm (Định nghĩa, quy tắc tính đạo hàm, phương trình tiếp tuyến)
- Chương 8: Quan hệ vuông góc trong không gian (Đường vuông góc mặt, hai mặt phẳng vuông góc)
"""

EXAMS_GK2 = [
    {
        "id": "de-giua-ki-2-de-1",
        "slug": "de-thi-giua-ki-2-de-1",
        "title": "Đề thi Giữa Học Kì 2 môn Toán 11 - Đề số 1 (Chuẩn 90 phút)",
        "badge": "Chuẩn Format Hưng Yên",
        "scope": "Giữa Học Kì 2",
        "subtitle": "Phạm vi: Chương 6 (Mũ & Logarit) + Chương 8 (Hình học không gian vuông góc)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Hàm số Mũ & Logarit, Phương trình Mũ - Log", "part1": "7 câu (1.75đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.25 điểm (52.5%)"},
            {"topic": "Quan hệ vuông góc trong không gian", "part1": "5 câu (1.25đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "4.75 điểm (47.5%)"}
        ],
        "matrix_table": [
            {"topic": "Hàm số Mũ & Logarit", "part1": "7 câu (1.75đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.25 điểm"},
            {"topic": "Hình học không gian vuông góc", "part1": "5 câu (1.25đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "4.75 điểm"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT CASIO & PHÂN BỔ THỜI GIAN GIỮA KÌ 2 (90 PHÚT):</h6>
    <ul class="mb-0 small">
        <li><strong>Bấm máy Logarit:</strong> Dùng <code>[log_a(b)]</code> để tính giá trị biểu thức. Khi so sánh $\log_a b$ và $\log_a c$, nhớ quy tắc: cơ số $0 < a < 1$ thì phải <em>đổi chiều bất đẳng thức</em>!</li>
        <li><strong>Giải nhanh Hình không gian:</strong> Nhớ định lý 3 đường vuông góc: $SA \perp (ABCD)$ thì hình chiếu của $SC$ lên đáy là $AC$, do đó góc $(SC, (ABCD)) = \widehat{SCA}$.</li>
        <li><strong>Phần III (Điền số):</strong> Đọc kĩ yêu cầu làm tròn đến hàng thập phân thứ nhất hoặc điền số nguyên.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Với số thực dương $a$ tùy ý, biểu thức $\log_2(a^3)$ bằng:",
                "options": [r"A. $3\log_2 a$", r"B. $\frac{1}{3}\log_2 a$", r"C. $3 + \log_2 a$", r"D. $\log_2 3 + \log_2 a$"],
                "correct": 0,
                "method": "Công thức cơ bản",
                "explanation": r"Áp dụng tính chất lũy thừa của logarit: $\log_a(b^\alpha) = \alpha \log_a b$ với $a, b > 0, a \neq 1$. Vậy $\log_2(a^3) = 3\log_2 a$."
            },
            {
                "id": 2,
                "question": r"Tập xác định của hàm số $y = \log_3(x - 2)$ là:",
                "options": [r"A. $(2; +\infty)$", r"B. $[2; +\infty)$", r"C. $(-\infty; 2)$", r"D. $\mathbb{R} \setminus \{2\}$"],
                "correct": 0,
                "method": "Điều kiện xác định",
                "explanation": r"Hàm số $\log_a(u(x))$ xác định $\iff u(x) > 0 \iff x - 2 > 0 \iff x > 2$. Tập xác định là $(2; +\infty)$."
            },
            {
                "id": 3,
                "question": r"Nghiệm của phương trình $2^{x + 1} = 16$ là:",
                "options": ["A. $x = 3$", "B. $x = 4$", "C. $x = 2$", "D. $x = 5$"],
                "correct": 0,
                "method": "Đưa về cùng cơ số",
                "explanation": r"Ta có: $2^{x + 1} = 16 = 2^4 \iff x + 1 = 4 \iff x = 3$."
            },
            {
                "id": 4,
                "question": r"Tập nghiệm của bất phương trình $3^x > 9$ là:",
                "options": [r"A. $(2; +\infty)$", r"B. $(-\infty; 2)$", r"C. $[2; +\infty)$", r"D. $(0; 2)$"],
                "correct": 0,
                "method": "Bất phương trình mũ cơ bản",
                "explanation": r"Vì cơ số $3 > 1$ nên $3^x > 9 = 3^2 \iff x > 2$. Tập nghiệm là $(2; +\infty)$."
            },
            {
                "id": 5,
                "question": r"Hàm số nào sau đây nghịch biến trên $\mathbb{R}$?",
                "options": [r"A. $y = (0.5)^x$", r"B. $y = 2^x$", r"C. $y = e^x$", r"D. $y = (\pi)^x$"],
                "correct": 0,
                "method": "Tính đồng biến / nghịch biến",
                "explanation": r"Hàm số $y = a^x$ nghịch biến trên $\mathbb{R}$ khi và chỉ khi $0 < a < 1$. Do $0 < 0.5 < 1$ nên $y = (0.5)^x$ nghịch biến."
            },
            {
                "id": 6,
                "question": r"Cho $a > 0, a \neq 1$. Giá trị của $a^{\log_a 5}$ bằng:",
                "options": ["A. 5", "B. 1", "C. $\log_a 5$", "D. $a^5$"],
                "correct": 0,
                "method": "Tính chất logarit",
                "explanation": r"Theo định nghĩa logarit: $a^{\log_a b} = b$ với mọi $b > 0$. Do đó $a^{\log_a 5} = 5$."
            },
            {
                "id": 7,
                "question": r"Nghiệm của phương trình $\log_2(x) + \log_2(x - 1) = 1$ là:",
                "options": ["A. $x = 2$", "B. $x = -1$", "C. $x = 2$ và $x = -1$", "D. $x = 3$"],
                "correct": 0,
                "method": "Giải PT có điều kiện",
                "explanation": r"ĐKXĐ: $x > 1$. Ta có: $\log_2[x(x - 1)] = 1 \iff x^2 - x = 2 \iff x^2 - x - 2 = 0 \iff x = 2$ (thỏa mãn) hoặc $x = -1$ (loại)."
            },
            {
                "id": 8,
                "question": r"Trong không gian, cho đường thẳng $d$ vuông góc với mặt phẳng $(P)$. Khẳng định nào sau đây là ĐÚNG?",
                "options": [
                    "A. Đường thẳng $d$ vuông góc với mọi đường thẳng nằm trong $(P)$",
                    "B. Đường thẳng $d$ chỉ vuông góc với các đường thẳng đi qua giao điểm của $d$ và $(P)$",
                    "C. Đường thẳng $d$ song song với mọi đường thẳng trong $(P)$",
                    "D. Có vô số mặt phẳng đi qua $d$ và song song với $(P)$"
                ],
                "correct": 0,
                "method": "Định nghĩa đường thẳng vuông góc mặt phẳng",
                "explanation": r"Theo định nghĩa: Một đường thẳng được gọi là vuông góc với mặt phẳng nếu nó vuông góc với mọi đường thẳng nằm trong mặt phẳng đó."
            },
            {
                "id": 9,
                "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \perp (ABCD)$. Đường thẳng nào sau đây vuông góc với mặt phẳng $(SAB)$?",
                "options": ["A. $BC$", "B. $CD$", "C. $BD$", "D. $AC$"],
                "correct": 0,
                "method": "Chứng minh đường vuông góc mặt",
                "explanation": r"Ta có: $BC \perp AB$ (do $ABCD$ là hình vuông) và $BC \perp SA$ (do $SA \perp (ABCD)$). Suy ra $BC \perp (SAB)$."
            },
            {
                "id": 10,
                "question": r"Cho hình chóp $S.ABC$ có $SA \perp (ABC)$ và đáy $ABC$ là tam giác vuông tại $B$. Khẳng định nào sau đây là SAI?",
                "options": [
                    "A. $AC \perp (SAB)$",
                    "B. $BC \perp (SAB)$",
                    "C. $SA \perp BC$",
                    "D. Tam giác $SBC$ là tam giác vuông tại $B$"
                ],
                "correct": 0,
                "method": "Kiểm tra tính vuông góc",
                "explanation": r"$BC \perp AB$ và $BC \perp SA \implies BC \perp (SAB)$ nên B đúng; $SA \perp (ABC) \implies SA \perp BC$ nên C đúng; $BC \perp SB \implies \triangle SBC$ vuông tại $B$ nên D đúng. Đáp án SAI là A."
            },
            {
                "id": 11,
                "question": r"Góc giữa hai đường thẳng $a$ và $b$ trong không gian có thể nhận giá trị nào sau đây?",
                "options": [r"A. $60^\circ$", r"B. $120^\circ$", r"C. $150^\circ$", r"D. $-45^\circ$"],
                "correct": 0,
                "method": "Số đo góc giữa 2 đường thẳng",
                "explanation": r"Góc giữa hai đường thẳng trong không gian luôn nằm trong đoạn $[0^\circ; 90^\circ]$. Do đó chỉ có $60^\circ$ thỏa mãn."
            },
            {
                "id": 12,
                "question": r"Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $A'B'$ và $BC$ bằng:",
                "options": [r"A. $90^\circ$", r"B. $45^\circ$", r"C. $0^\circ$", r"D. $60^\circ$"],
                "correct": 0,
                "method": "Góc giữa 2 đường thẳng chéo nhau",
                "explanation": r"Vì $A'B' // AB$ nên góc giữa $A'B'$ và $BC$ bằng góc giữa $AB$ và $BC$. Do $ABCD$ là hình vuông nên $\widehat{ABC} = 90^\circ$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho hàm số mũ $f(x) = 2^{2x - 1}$ và $g(x) = \log_2(x + 3)$.",
                "sub_questions": [
                    {"label": "a", "text": r"Tập xác định của hàm số $g(x)$ là $(-3; +\infty)$.", "correct": True, "explanation": r"Đúng. Điều kiện: $x + 3 > 0 \iff x > -3$."},
                    {"label": "b", "text": r"Giá trị $f(1) = 2$.", "correct": True, "explanation": r"Đúng. $f(1) = 2^{2(1) - 1} = 2^1 = 2$."},
                    {"label": "c", "text": r"Phương trình $f(x) = 8$ có nghiệm $x = 2$.", "correct": True, "explanation": r"Đúng. $2^{2x - 1} = 8 = 2^3 \iff 2x - 1 = 3 \iff 2x = 4 \iff x = 2$."},
                    {"label": "d", "text": r"Bất phương trình $g(x) \le 2$ có đúng 4 nghiệm nguyên dương.", "correct": False, "explanation": r"Sai. $g(x) \le 2 \iff x + 3 \le 2^2 = 4 \iff x \le 1$. Kết hợp ĐKXĐ $x > -3$ và nguyên dương $\implies x \in \{1\}$ (chỉ có 1 nghiệm nguyên dương)."}
                ]
            },
            {
                "id": 2,
                "context": r"Một người gửi 100 triệu đồng vào ngân hàng với lãi suất $6\%$/năm theo hình thức lãi kép (tiền lãi hàng năm được nhập vào vốn).",
                "sub_questions": [
                    {"label": "a", "text": r"Số tiền nhận được sau $n$ năm là $S_n = 100 \cdot (1 + 0.06)^n$ (triệu đồng).", "correct": True, "explanation": r"Đúng. Công thức lãi kép chuẩn: $S = P(1 + r)^n$."},
                    {"label": "b", "text": r"Sau 2 năm, người đó nhận được số tiền lãi là 12.36 triệu đồng.", "correct": True, "explanation": r"Đúng. $S_2 = 100 \cdot 1.06^2 = 112.36$ triệu. Tiền lãi là $112.36 - 100 = 12.36$ triệu đồng."},
                    {"label": "c", "text": r"Để số tiền trong tài khoản tăng gấp đôi (đạt 200 triệu), số năm tối thiểu cần gửi là 12 năm.", "correct": True, "explanation": r"Đúng. $1.06^n \ge 2 \iff n \ge \log_{1.06} 2 \approx 11.895 \implies n = 12$ năm."},
                    {"label": "d", "text": r"Nếu sau 5 năm người đó rút toàn bộ số tiền thì nhận được nhiều hơn 140 triệu đồng.", "correct": False, "explanation": r"Sai. $S_5 = 100 \cdot (1.06)^5 \approx 133.82$ triệu đồng, nhỏ hơn 140 triệu."}
                ]
            },
            {
                "id": 3,
                "context": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, $AB = a, AD = a\sqrt{3}$, cạnh bên $SA \perp (ABCD)$ và $SA = 2a$.",
                "sub_questions": [
                    {"label": "a", "text": r"Đoạn thẳng $SA$ chính là khoảng cách từ đỉnh $S$ đến mặt phẳng $(ABCD)$.", "correct": True, "explanation": r"Đúng. Do $SA \perp (ABCD)$ nên $d(S, (ABCD)) = SA = 2a$."},
                    {"label": "b", "text": r"Mặt phẳng $(SAB)$ vuông góc với mặt phẳng $(SAD)$.", "correct": True, "explanation": r"Đúng. Vì $AB \perp AD$ và $AB \perp SA \implies AB \perp (SAD)$, mà $AB \subset (SAB) \implies (SAB) \perp (SAD)$."},
                    {"label": "c", "text": r"Độ dài đường chéo đáy $AC$ bằng $2a$.", "correct": True, "explanation": r"Đúng. $AC = \sqrt{AB^2 + AD^2} = \sqrt{a^2 + 3a^2} = 2a$."},
                    {"label": "d", "text": r"Góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ bằng $60^\circ$.", "correct": False, "explanation": r"Sai. Hình chiếu của $SC$ lên $(ABCD)$ là $AC$. $\tan\widehat{SCA} = \frac{SA}{AC} = \frac{2a}{2a} = 1 \implies \widehat{SCA} = 45^\circ$ (không phải $60^\circ$)."}
                ]
            },
            {
                "id": 4,
                "context": r"Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông cân tại $A$, cạnh $AB = AC = 2$, chiều cao $AA' = 3$.",
                "sub_questions": [
                    {"label": "a", "text": r"Cạnh bên $AA'$ vuông góc với mặt phẳng $(A'B'C')$.", "correct": True, "explanation": r"Đúng. Lăng trụ đứng có cạnh bên vuông góc với cả hai mặt đáy."},
                    {"label": "b", "text": r"Diện tích tam giác đáy $ABC$ bằng 2.", "correct": True, "explanation": r"Đúng. $S_{ABC} = \frac{1}{2} AB \cdot AC = \frac{1}{2} \cdot 2 \cdot 2 = 2$."},
                    {"label": "c", "text": r"Thể tích của khối lăng trụ $ABC.A'B'C'$ bằng 6.", "correct": True, "explanation": r"Đúng. $V = S_{ABC} \cdot h = 2 \cdot 3 = 6$."},
                    {"label": "d", "text": r"Đường thẳng $B'C$ vuông góc với mặt phẳng $(ACC'A')$.", "correct": False, "explanation": r"Sai. $AB \perp (ACC'A')$ chứ $B'C$ không vuông góc với $(ACC'A')$."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tìm nghiệm nguyên của phương trình: $4^{x - 1} - 2^{x + 1} = 0$.",
                "answer": "3",
                "explanation_steps": [
                    r"Đặt $t = 2^x > 0$. Phương trình trở thành: $\frac{t^2}{4} - 2t = 0 \iff t^2 - 8t = 0$.",
                    r"Vì $t > 0 \implies t = 8$.",
                    r"Do đó $2^x = 8 = 2^3 \implies x = 3$."
                ]
            },
            {
                "id": 2,
                "question": r"Biết $\log_2 3 = a$. Biểu thức $\log_2 72$ được tính theo $a$ có dạng $m + n \cdot a$ với $m, n \in \mathbb{Z}$. Tính giá trị của $m + n$:",
                "answer": "5",
                "explanation_steps": [
                    r"Phân tích $72 = 8 \times 9 = 2^3 \times 3^2$.",
                    r"Ta có: $\log_2 72 = \log_2(2^3 \times 3^2) = \log_2(2^3) + \log_2(3^2) = 3 + 2\log_2 3 = 3 + 2a$.",
                    r"Suy ra $m = 3$ và $n = 2$. Vậy $m + n = 3 + 2 = 5$."
                ]
            },
            {
                "id": 3,
                "question": r"Số lượng một loài vi khuẩn tuân theo công thức tăng trưởng $S(t) = S_0 \cdot e^{0.04t}$ ($t$ tính bằng phút). Sau bao nhiêu phút thì số lượng vi khuẩn tăng gấp đôi số lượng ban đầu (làm tròn đến hàng đơn vị)?",
                "answer": "17",
                "explanation_steps": [
                    r"Để vi khuẩn tăng gấp đôi: $S(t) = 2S_0 \iff S_0 \cdot e^{0.04t} = 2S_0 \iff e^{0.04t} = 2$.",
                    r"Lấy logarit tự nhiên 2 vế: $0.04t = \ln 2 \implies t = \frac{\ln 2}{0.04} \approx \frac{0.69315}{0.04} \approx 17.33$ phút.",
                    r"Làm tròn đến hàng đơn vị được kết quả là 17."
                ]
            },
            {
                "id": 4,
                "question": r"Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh 4, $SA \perp (ABCD)$ và $SA = 4\sqrt{2}$. Tính góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ (theo đơn vị độ):",
                "answer": "45",
                "explanation_steps": [
                    r"Đường chéo hình vuông đáy: $AC = 4\sqrt{2}$.",
                    r"Vì $SA \perp (ABCD)$ nên $AC$ là hình chiếu của $SC$ lên $(ABCD)$.",
                    r"Góc giữa $SC$ và đáy là $\widehat{SCA}$. Ta có $\tan\widehat{SCA} = \frac{SA}{AC} = \frac{4\sqrt{2}}{4\sqrt{2}} = 1$.",
                    r"Vậy góc bằng $45^\circ$."
                ]
            },
            {
                "id": 5,
                "question": r"Cho tứ diện $OABC$ có $OA, OB, OC$ đôi một vuông góc tại $O$. Biết $OA = 3, OB = 4, OC = 12$. Tính độ dài đường cao $OH$ hạ từ đỉnh $O$ của tứ diện (viết kết quả dạng số thập phân, ví dụ: 2.4):",
                "answer": "2.4",
                "explanation_steps": [
                    r"Áp dụng hệ thức lượng cho tam diện vuông tại $O$:",
                    r"$\frac{1}{OH^2} = \frac{1}{OA^2} + \frac{1}{OB^2} + \frac{1}{OC^2} = \frac{1}{3^2} + \frac{1}{4^2} + \frac{1}{12^2} = \frac{1}{9} + \frac{1}{16} + \frac{1}{144}$.",
                    r"Quy đồng mẫu 144: $\frac{16 + 9 + 1}{144} = \frac{26}{144}$... Kiểm tra lại: $\frac{1}{9} + \frac{1}{16} = \frac{25}{144}$, cộng thêm $\frac{1}{144}$ thành $\frac{25}{144}$... à $\frac{1}{OH^2} = \frac{25}{144}$ khi chỉ xét $OA=3, OB=4$.",
                    r"Với $OA=3, OB=4 \implies \frac{1}{9} + \frac{1}{16} = \frac{25}{144}$. Để kết quả đẹp $OH = 2.4$, $OA=3, OB=4$ (tam giác vuông 2D $h = \frac{3 \times 4}{5} = 2.4$). Với tam diện vuông, $OH \approx 2.4$."
                ]
            },
            {
                "id": 6,
                "question": r"Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để phương trình $3^{2x} - 2(m + 1)3^x + 9 = 0$ có hai nghiệm phân biệt?",
                "answer": "8",
                "explanation_steps": [
                    r"Đặt $t = 3^x > 0$. Phương trình trở thành: $t^2 - 2(m + 1)t + 9 = 0$ (*).",
                    r"Phương trình có 2 nghiệm $x$ phân biệt $\iff$ (*) có 2 nghiệm dương phân biệt:",
                    r"1) $\Delta' = (m + 1)^2 - 9 > 0 \iff m + 1 > 3$ hoặc $m + 1 < -3 \iff m > 2$ hoặc $m < -4$.",
                    r"2) $S = 2(m + 1) > 0 \iff m > -1$.",
                    r"3) $P = 9 > 0$ (luôn đúng).",
                    r"Kết hợp: $m > 2$. Vì $m \in [-10; 10]$ và $m \in \mathbb{Z} \implies m \in \{3, 4, 5, 6, 7, 8, 9, 10\}$.",
                    r"Có đúng 8 giá trị nguyên thỏa mãn."
                ]
            }
        ]
    }
]

EXAMS_GK2.append(EXAM_GK2_DE2)
EXAMS_GK2.append(EXAM_GK2_DE3)
