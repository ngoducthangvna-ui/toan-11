# -*- coding: utf-8 -*-
"""
Đề thi Cuối Học Kì 1 - Đề số 2 (Chuẩn Format 90 phút Hưng Yên / GDPT 2018)
Phạm vi: Trọn bộ Tập 1 (Chương 1 đến Chương 5)
Tác giả: Antigravity AI
"""

DE_CUOI_KI_1_DE_2 = {
    "id": "de-cuoi-ki-1-de-2",
    "slug": "de-thi-cuoi-ki-1-de-so-2-toan-11",
    "title": "Đề thi Cuối Học Kì 1 - Đề số 2 (Chuẩn 90 phút)",
    "badge": "Chuẩn Format Hưng Yên",
    "scope": "Cuối Học Kì 1",
    "subtitle": "Phạm vi: Toàn diện Tập 1 (Chương 1 đến Chương 5 - Lượng giác, Cấp số, Thống kê, Không gian & Giới hạn)",
    "time_minutes": 90,
    "total_points": 10.0,
    "matrix_analysis": [
        {"topic": "Hàm số & Phương trình Lượng giác", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Dãy số, Cấp số cộng & Cấp số nhân", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Các số đặc trưng đo xu thế trung tâm", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"},
        {"topic": "Quan hệ song song trong không gian", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"},
        {"topic": "Giới hạn dãy số & hàm số liên tục", "part1": "2 câu (0.5đ)", "part2": "0 câu", "part3": "1 câu (0.5đ)", "total": "1.0 điểm"}
    ],
    "matrix_table": [
        {"topic": "Hàm số & Phương trình Lượng giác", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
        {"topic": "Dãy số, Cấp số cộng & Cấp số nhân", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
        {"topic": "Các số đặc trưng đo xu thế trung tâm", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"},
        {"topic": "Quan hệ song song trong không gian", "part1": "2 câu (0.5đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.0 điểm"},
        {"topic": "Giới hạn & Hàm số liên tục", "part1": "2 câu (0.5đ)", "part2": "0 câu", "part3": "1 câu (0.5đ)", "total": "1.0 điểm"}
    ],
    "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT PHÂN BỔ THỜI GIAN ĐỀ CUỐI HỌC KÌ 1:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm đơn. Giải nhanh câu công thức lượng giác, tính chất giới hạn cơ bản, lý thuyết song song không gian.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai (Bài toán thực tế nhiệt độ/dao động, Cấp số cộng, Bảng thống kê ghép nhóm, Hình lăng trụ song song). Nhớ đọc kĩ từng mệnh đề.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Chú ý tính toán chính xác tổng lương cấp số cộng, số nghiệm phương trình lượng giác, trung vị mẫu ghép nhóm.</li>
        <li><strong>85 - 90 phút:</strong> Kiểm tra lại đáp án số nguyên / số thập phân để không bị mất điểm đáng tiếc.</li>
    </ul>
</div>
""",
    "part1": [
        {
            "id": 1,
            "question": r"Khẳng định nào sau đây là <strong>sai</strong> về công thức lượng giác?",
            "options": [
                r"A. $\cos 2a = 1 - 2\sin^2 a$",
                r"B. $\sin 2a = 2\sin a \cos a$",
                r"C. $\cos 2a = 2\cos^2 a - 1$",
                r"D. $\cos 2a = \sin^2 a - \cos^2 a$"
            ],
            "correct": 3,
            "method": "Công thức nhân đôi",
            "explanation": r"Công thức đúng là $\cos 2a = \cos^2 a - \sin^2 a$, do đó phương án D là sai."
        },
        {
            "id": 2,
            "question": r"Tập xác định của hàm số $y = \tan\left(x - \frac{\pi}{4}\right)$ là:",
            "options": [
                r"A. $D = \mathbb{R} \setminus \left\{\frac{3\pi}{4} + k\pi, k \in \mathbb{Z}\right\}$",
                r"B. $D = \mathbb{R} \setminus \left\{\frac{\pi}{4} + k\pi, k \in \mathbb{Z}\right\}$",
                r"C. $D = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right\}$",
                r"D. $D = \mathbb{R}$"
            ],
            "correct": 0,
            "method": "Điều kiện hàm tan",
            "explanation": r"Hàm số xác định $\iff x - \frac{\pi}{4} \neq \frac{\pi}{2} + k\pi \iff x \neq \frac{3\pi}{4} + k\pi$ ($k \in \mathbb{Z}$)."
        },
        {
            "id": 3,
            "question": r"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = -2$ và công sai $d = 3$. Số hạng thứ 10 bằng:",
            "options": ["A. 25", "B. 28", "C. -29", "D. 31"],
            "correct": 0,
            "method": "Số hạng tổng quát CSC",
            "explanation": r"$u_{10} = u_1 + 9d = -2 + 9 \times 3 = 25$."
        },
        {
            "id": 4,
            "question": r"Tổng của cấp số nhân lùi vô hạn có số hạng đầu $u_1 = 4$ và công bội $q = \frac{1}{3}$ là:",
            "options": ["A. 6", "B. 12", "C. 8", "D. $\frac{16}{3}$"],
            "correct": 0,
            "method": "Tổng CSN lùi vô hạn",
            "explanation": r"$S = \frac{u_1}{1 - q} = \frac{4}{1 - 1/3} = \frac{4}{2/3} = 6$."
        },
        {
            "id": 5,
            "question": r"Giới hạn $\lim_{n \to \infty} \frac{3n^2 - 2n + 1}{2n^2 + 5}$ bằng:",
            "options": [r"A. $\frac{3}{2}$", "B. 0", r"C. $+\infty$", "D. 1"],
            "correct": 0,
            "method": "Chia bậc cao nhất của n",
            "explanation": r"Chia cả tử và mẫu cho $n^2$: $\lim \frac{3 - 2/n + 1/n^2}{2 + 5/n^2} = \frac{3}{2}$."
        },
        {
            "id": 6,
            "question": r"Giới hạn $\lim_{x \to 2} \frac{\sqrt{x + 2} - 2}{x - 2}$ bằng:",
            "options": [r"A. $\frac{1}{4}$", r"B. $\frac{1}{2}$", "C. 0", "D. 1"],
            "correct": 0,
            "method": "Nhân lượng liên hợp",
            "explanation": r"Nhân liên hợp tử: $\frac{(x + 2) - 4}{(x - 2)(\sqrt{x + 2} + 2)} = \frac{1}{\sqrt{x + 2} + 2}$. Thay $x = 2 \implies \frac{1}{2 + 2} = \frac{1}{4}$."
        },
        {
            "id": 7,
            "question": r"Trong không gian, hai đường thẳng phân biệt không có điểm chung thì:",
            "options": [
                "A. Song song hoặc chéo nhau",
                "B. Chéo nhau",
                "C. Song song",
                "D. Cắt nhau"
            ],
            "correct": 0,
            "method": "Vị trí tương đối 2 đường thẳng",
            "explanation": r"Hai đường thẳng phân biệt không có điểm chung có thể cùng thuộc 1 mặt phẳng (song song) hoặc không cùng thuộc mặt phẳng nào (chéo nhau)."
        },
        {
            "id": 8,
            "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang $(AB // CD, AB > CD)$. Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là:",
            "options": [
                "A. Đường thẳng qua $S$ và song song với $AB$",
                "B. Đường thẳng $SO$ với $O$ là giao điểm $AC$ và $BD$",
                "C. Đoạn thẳng $SD$",
                "D. Không có giao tuyến"
            ],
            "correct": 0,
            "method": "Giao tuyến song song",
            "explanation": r"$(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AB // CD$ nên giao tuyến là đường thẳng qua $S$ song song với $AB$ và $CD$."
        },
        {
            "id": 9,
            "question": r"Khảo sát thời gian tự học (giờ/tuần) của 40 học sinh được bảng: $[0; 5): 6, [5; 10): 14, [10; 15): 15, [15; 20): 5$. Nhóm chứa mốt là:",
            "options": ["A. $[10; 15)$", "B. $[5; 10)$", "C. $[0; 5)$", "D. $[15; 20)$"],
            "correct": 0,
            "method": "Nhóm chứa mốt",
            "explanation": r"Nhóm có tần số lớn nhất là nhóm $[10; 15)$ với tần số 15 học sinh."
        },
        {
            "id": 10,
            "question": r"Phương trình lượng giác cơ bản $\sin x = \frac{\sqrt{3}}{2}$ có họ nghiệm là:",
            "options": [
                r"A. $x = \frac{\pi}{3} + k2\pi$ và $x = \frac{2\pi}{3} + k2\pi, k \in \mathbb{Z}$",
                r"B. $x = \pm \frac{\pi}{3} + k2\pi, k \in \mathbb{Z}$",
                r"C. $x = \frac{\pi}{6} + k2\pi$ và $x = \frac{5\pi}{6} + k2\pi, k \in \mathbb{Z}$",
                r"D. $x = \frac{\pi}{3} + k\pi, k \in \mathbb{Z}$"
            ],
            "correct": 0,
            "method": "Nghiệm sin cơ bản",
            "explanation": r"$\sin x = \sin\left(\frac{\pi}{3}\right) \iff x = \frac{\pi}{3} + k2\pi$ hoặc $x = \pi - \frac{\pi}{3} + k2\pi = \frac{2\pi}{3} + k2\pi$ ($k \in \mathbb{Z}$)."
        },
        {
            "id": 11,
            "question": r"Hàm số $f(x) = \frac{2x - 1}{x + 1}$ liên tục trên khoảng nào sau đây?",
            "options": [
                r"A. $(0; +\infty)$",
                r"B. $(-\infty; 1)$",
                r"C. $(-2; 0)$",
                r"D. $\mathbb{R}$"
            ],
            "correct": 0,
            "method": "Khoảng liên tục",
            "explanation": r"Hàm phân thức xác định và liên tục trên từng khoảng $(-\infty; -1)$ và $(-1; +\infty)$. Do $(0; +\infty) \subset (-1; +\infty)$ nên hàm số liên tục trên $(0; +\infty)$."
        },
        {
            "id": 12,
            "question": r"Cho hình lăng trụ $ABC.A'B'C'$. Khẳng định nào sau đây là <strong>sai</strong>?",
            "options": [
                r"A. Các mặt bên là các tam giác",
                r"B. Các cạnh bên đôi một song song và bằng nhau",
                r"C. Hai mặt phẳng đáy $(ABC)$ và $(A'B'C')$ song song với nhau",
                r"D. Các mặt bên là hình bình hành"
            ],
            "correct": 0,
            "method": "Định nghĩa lăng trụ",
            "explanation": r"Các mặt bên của hình lăng trụ là hình bình hành, không phải hình tam giác."
        }
    ],
    "part2": [
        {
            "id": 1,
            "context": r"Nhiệt độ ngoài trời $T$ ($^\circ\text{C}$) tại một trạm quan trắc ở Hưng Yên trong một ngày được mô hình hóa bởi hàm số: $T(t) = 25 + 6\sin\left(\frac{\pi}{12}(t - 8)\right)$, trong đó $t$ là số giờ tính từ nửa đêm ($0 \le t \le 24$).",
            "sub_questions": [
                {"label": "a", "text": r"Chu kỳ biến thiên nhiệt độ của mô hình là 24 giờ.", "correct": True, "explanation": r"Đúng. Chu kỳ $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi/12} = 24$ giờ."},
                {"label": "b", "text": r"Nhiệt độ cao nhất trong ngày đo được là $31^\circ\text{C}$.", "correct": True, "explanation": r"Đúng. Do $-1 \le \sin \le 1$ nên $T_{\max} = 25 + 6(1) = 31^\circ\text{C}$."},
                {"label": "c", "text": r"Vào thời điểm 8 giờ sáng ($t = 8$), nhiệt độ là $25^\circ\text{C}$.", "correct": True, "explanation": r"Đúng. Khi $t = 8$, $\sin(0) = 0 \implies T(8) = 25^\circ\text{C}$."},
                {"label": "d", "text": r"Nhiệt độ đạt $28^\circ\text{C}$ lần đầu tiên trong ngày vào lúc 12 giờ trưa.", "correct": False, "explanation": r"Sai. $25 + 6\sin = 28 \iff \sin = 0.5 \iff \frac{\pi}{12}(t-8) = \frac{\pi}{6} \iff t - 8 = 2 \iff t = 10$ (10 giờ sáng)."}
            ]
        },
        {
            "id": 2,
            "context": r"Cho cấp số cộng $(u_n)$ có số hạng $u_3 = 11$ và $u_8 = 31$.",
            "sub_questions": [
                {"label": "a", "text": r"Công sai của cấp số cộng bằng $d = 4$.", "correct": True, "explanation": r"Đúng. $u_8 - u_3 = 5d \implies 31 - 11 = 5d \implies 5d = 20 \implies d = 4$."},
                {"label": "b", "text": r"Số hạng đầu của cấp số cộng là $u_1 = 3$.", "correct": True, "explanation": r"Đúng. $u_1 = u_3 - 2d = 11 - 2(4) = 3$."},
                {"label": "c", "text": r"Số 203 là số hạng thứ 50 của cấp số cộng.", "correct": False, "explanation": r"Sai. $u_n = 3 + (n-1)4 = 203 \iff 4(n-1) = 200 \iff n - 1 = 50 \iff n = 51$ (số hạng thứ 51)."},
                {"label": "d", "text": r"Tổng của 20 số hạng đầu tiên $S_{20} = 820$.", "correct": True, "explanation": r"Đúng. $S_{20} = \frac{20}{2}[2(3) + 19(4)] = 10[6 + 76] = 10 \times 82 = 820$."}
            ]
        },
        {
            "id": 3,
            "context": r"Khảo sát cân nặng (kg) của 40 học sinh lớp 11A được ghi lại trong bảng tần số ghép nhóm sau: $[40; 45): 4$, $[45; 50): 12$, $[50; 55): 16$, $[55; 60): 6$, $[60; 65): 2$.",
            "sub_questions": [
                {"label": "a", "text": r"Cỡ mẫu của cuộc khảo sát là $n = 40$ học sinh.", "correct": True, "explanation": r"Đúng. $4 + 12 + 16 + 6 + 2 = 40$."},
                {"label": "b", "text": r"Nhóm chứa trung vị là nhóm $[50; 55)$.", "correct": True, "explanation": r"Đúng. $n/2 = 20$. Tần số tích lũy: $cf_1 = 4, cf_2 = 16, cf_3 = 32$. Nhóm thứ 3 chứa vị trí thứ 20 và 21."},
                {"label": "c", "text": r"Trung vị của mẫu số liệu ghép nhóm bằng $51.25\text{ kg}$.", "correct": True, "explanation": r"Đúng. $M_e = 50 + \frac{20 - 16}{16} \times 5 = 50 + \frac{4}{16} \times 5 = 50 + 1.25 = 51.25$."},
                {"label": "d", "text": r"Nhóm chứa mốt là nhóm $[45; 50)$.", "correct": False, "explanation": r"Sai. Nhóm có tần số lớn nhất là $[50; 55)$ với 16 học sinh."}
            ]
        },
        {
            "id": 4,
            "context": r"Cho hình lăng trụ $ABC.A'B'C'$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $A'C'$.",
            "sub_questions": [
                {"label": "a", "text": r"Hai mặt phẳng $(ABC)$ và $(A'B'C')$ song song với nhau.", "correct": True, "explanation": r"Đúng. Hai đáy của hình lăng trụ luôn song song với nhau."},
                {"label": "b", "text": r"Giao tuyến của $(AA'B'B)$ và $(BCC'B')$ là đường thẳng $BB'$.", "correct": True, "explanation": r"Đúng. Cạnh bên $BB'$ là cạnh chung của hai mặt bên này."},
                {"label": "c", "text": r"Đường thẳng $MN$ song song với mặt phẳng $(BCC'B')$.", "correct": False, "explanation": r"Sai. $MN$ không song song với $(BCC'B')$, kéo dài sẽ cắt mặt phẳng."},
                {"label": "d", "text": r"Thiết diện của hình lăng trụ cắt bởi mặt phẳng đi qua $M$ và song song với $(BCC'B')$ là một hình bình hành.", "correct": True, "explanation": r"Đúng. Mặt phẳng song song cắt $(ABC)$ theo đường thẳng qua $M$ song song $BC$, cắt các mặt bên theo các đoạn thẳng song song với các cạnh bên, tạo thành hình bình hành."}
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": r"Tìm số nghiệm của phương trình $\cos 2x - 3\cos x + 2 = 0$ thuộc đoạn $[0; 2\pi]$.",
            "answer": "3",
            "unit": "nghiệm",
            "method": "Đặt ẩn phụ t = cos x",
            "explanation": r"Phương trình $\iff 2\cos^2 x - 3\cos x + 1 = 0 \iff \cos x = 1$ hoặc $\cos x = 1/2$. Trên $[0; 2\pi]$: $\cos x = 1 \implies x = 0, 2\pi$ (2 nghiệm). $\cos x = 1/2 \implies x = \pi/3, 5\pi/3$ (2 nghiệm). Tổng cộng có 4 nghiệm? Khoan: $\cos 2x - 3\cos x + 2 = 0 \iff (2\cos^2 x - 1) - 3\cos x + 2 = 0 \iff 2\cos^2 x - 3\cos x + 1 = 0 \iff \cos x = 1$ (tại $0, 2\pi$) hoặc $\cos x = 1/2$ (tại $\pi/3, 5\pi/3$). Tổng cộng có 4 nghiệm."
        },
        {
            "id": 2,
            "question": r"Một người đi làm được một công ty chào mời mức lương năm đầu tiên là 120 triệu đồng, kể từ năm thứ hai mỗi năm được tăng thêm 15 triệu đồng. Sau 10 năm công tác tại công ty này, tổng số tiền lương người đó nhận được là bao nhiêu triệu đồng?",
            "answer": "1875",
            "unit": "triệu đồng",
            "method": "Tổng cấp số cộng S_10",
            "explanation": r"Dãy số tiền lương là cấp số cộng với $u_1 = 120, d = 15, n = 10$. Tổng số tiền: $S_{10} = \frac{10}{2}[2(120) + (10 - 1) \times 15] = 5[240 + 135] = 5 \times 375 = 1875$ triệu đồng."
        },
        {
            "id": 3,
            "question": r"Tính giới hạn: $\lim_{x \to 3} \frac{x^2 - 5x + 6}{x - 3}$.",
            "answer": "1",
            "unit": "",
            "method": "Phân tích nhân tử khử dạng 0/0",
            "explanation": r"Ta có $x^2 - 5x + 6 = (x - 3)(x - 2)$. Do đó $\lim_{x \to 3} \frac{(x-3)(x-2)}{x-3} = \lim_{x \to 3} (x - 2) = 3 - 2 = 1$."
        },
        {
            "id": 4,
            "question": r"Cho cấp số nhân lùi vô hạn $(u_n)$ có số hạng đầu $u_1 = 12$ và tổng của cấp số nhân bằng $S = 18$. Giá trị của công bội $q$ (viết dưới dạng phân số tối giản tử/mẫu ví dụ 1/3) có mẫu số bằng bao nhiêu?",
            "answer": "3",
            "unit": "",
            "method": "Công thức tổng CSN lùi vô hạn",
            "explanation": r"$S = \frac{u_1}{1 - q} \implies 18 = \frac{12}{1 - q} \implies 1 - q = \frac{12}{18} = \frac{2}{3} \implies q = 1 - \frac{2}{3} = \frac{1}{3}$. Mẫu số bằng 3."
        },
        {
            "id": 5,
            "question": r"Cho hình chóp $S.ABCD$ có đáy là hình bình hành diện tích $60\text{ cm}^2$. Trên cạnh $SA$ lấy điểm $M$ sao cho $SM = \frac{1}{2}SA$. Mặt phẳng $(\alpha)$ đi qua $M$ và song song với mặt phẳng đáy $(ABCD)$ cắt các cạnh $SB, SC, SD$ lần lượt tại $N, P, Q$. Tính diện tích thiết diện $MNPQ$ (đơn vị: $\text{cm}^2$).",
            "answer": "15",
            "unit": "cm²",
            "method": "Tỉ số diện tích thiết diện song song",
            "explanation": r"Vì $(\alpha) // (ABCD)$ nên thiết diện $MNPQ$ là hình bình hành đồng dạng với đáy $ABCD$ theo tỉ số đồng dạng $k = \frac{SM}{SA} = \frac{1}{2}$. Tỉ số diện tích bằng $k^2 = (1/2)^2 = 1/4$. Vậy $S_{MNPQ} = \frac{1}{4} \times S_{ABCD} = \frac{60}{4} = 15\text{ cm}^2$."
        },
        {
            "id": 6,
            "question": r"Từ bảng tần số ghép nhóm cân nặng: $[40; 45): 4, [45; 50): 12, [50; 55): 16, [55; 60): 6, [60; 65): 2$. Tính trung vị của mẫu số liệu ghép nhóm (làm tròn đến hai chữ số thập phân).",
            "answer": "51.25",
            "unit": "kg",
            "method": "Công thức trung vị mẫu ghép nhóm",
            "explanation": r"Cỡ mẫu $n = 40 \implies n/2 = 20$. Nhóm chứa trung vị là $[50; 55)$ có $r = 50, d = 5, n_3 = 16, cf_2 = 16$. $M_e = 50 + \frac{20 - 16}{16} \times 5 = 50 + 1.25 = 51.25$."
        }
    ]
}

# Fix part3 question 1 answer to 4
DE_CUOI_KI_1_DE_2["part3"][0]["answer"] = "4"

EXAMS_CK1 = [DE_CUOI_KI_1_DE_2]
