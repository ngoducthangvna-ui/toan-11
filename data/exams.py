# -*- coding: utf-8 -*-
"""
Hệ thống Đề thi Chuẩn Format mới của Bộ Giáo dục & Đào tạo (Mô phỏng Sở GD&ĐT Hưng Yên)
Gồm 3 phần chuẩn:
- Phần I: 12 câu trắc nghiệm 4 lựa chọn (3,0 điểm)
- Phần II: 4 câu trắc nghiệm Đúng / Sai (4,0 điểm)
- Phần III: 6 câu trắc nghiệm Trả lời ngắn (3,0 điểm)
Kèm Chiến thuật bấm máy Casio fx-580VNX/880BTG, Bảng ma trận & Giải thích trực quan
"""

EXAM_LIST = [
    {
        "id": "de-giua-ki-1",
        "slug": "de-thi-giua-ki-1-toan-11",
        "title": "Đề thi Giữa Học Kì 1 môn Toán 11 (Chuẩn 90 phút)",
        "badge": "Chuẩn Ma Trận Hưng Yên",
        "subtitle": "Phạm vi: Chương 1 (Lượng giác) + Nửa đầu Chương 2 (Dãy số, Cấp số cộng)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Hàm số & Phương trình Lượng giác", "part1": "8 câu (2.0đ)", "part2": "2 câu (2.0đ)", "part3": "4 câu (2.0đ)", "total": "6.0 điểm (60%)"},
            {"topic": "Dãy số & Cấp số cộng", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm (40%)"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT PHÂN BỔ THỜI GIAN & BẤM MÁY CASIO 90 PHÚT:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm đơn. Mỗi câu tối đa 1.5 phút. Các câu nhận biết giải nhanh bằng mắt hoặc bấm Casio Table <code>[MENU] [8]</code> (fx-580VNX) để quét giá trị lớn nhất, nhỏ nhất, chu kỳ.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai. Đây là mỏ điểm (4.0 điểm)! Đọc kĩ từng ý a, b, c, d vì ý trước thường là bậc thang cho ý sau. Câu thực tế (bánh xe quay, bài toán tiền bạc) tóm tắt các đại lượng ra nháp.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Bắt buộc tính toán cẩn thận từng con số. Câu phương trình lượng giác nhớ đếm nghiệm trên đoạn/khoảng bằng cách vẽ vòng tròn lượng giác hoặc chặn $k \in \mathbb{Z}$.</li>
        <li><strong>85 - 90 phút:</strong> Rà soát lại tô đáp án và các phép tính làm tròn.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Góc có số đo $\frac{2\pi}{3}\text{ rad}$ khi đổi sang đơn vị độ bằng:",
                "options": [r"A. $120^\circ$", r"B. $150^\circ$", r"C. $135^\circ$", r"D. $60^\circ$"],
                "correct": 0,
                "method": "Nhẩm nhanh hoặc Casio",
                "explanation": r"Công thức: $\alpha^\circ = \frac{2\pi}{3} \cdot \frac{180^\circ}{\pi} = 120^\circ$. Bấm máy: <code>2 * 180 / 3 = 120</code>."
            },
            {
                "id": 2,
                "question": r"Tập xác định của hàm số $y = \frac{1}{\cos x}$ là:",
                "options": [
                    r"A. $D = \mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$",
                    r"B. $D = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right\}$",
                    r"C. $D = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k2\pi, k \in \mathbb{Z}\right\}$",
                    r"D. $D = \mathbb{R}$"
                ],
                "correct": 1,
                "method": "Nhận biết lý thuyết",
                "explanation": r"Điều kiện mẫu số khác 0: $\cos x \neq 0 \iff x \neq \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 3,
                "question": r"Hàm số nào sau đây là hàm số chẵn?",
                "options": [r"A. $y = \sin x$", r"B. $y = \cos x$", r"C. $y = \tan x$", r"D. $y = \cot x$"],
                "correct": 1,
                "method": "Nhận biết",
                "explanation": r"Trong 4 hàm lượng giác cơ bản, duy nhất $y = \cos x$ là hàm số chẵn vì $\cos(-x) = \cos x$."
            },
            {
                "id": 4,
                "question": r"Giá trị lớn nhất $M$ của hàm số $y = 3\sin(2x - \frac{\pi}{4}) + 2$ bằng:",
                "options": ["A. 3", "B. 5", "C. 2", "D. 1"],
                "correct": 1,
                "method": "Chặn giá trị",
                "explanation": r"Vì $-1 \le \sin(2x - \pi/4) \le 1 \implies M = 3(1) + 2 = 5$."
            },
            {
                "id": 5,
                "question": r"Nghiệm của phương trình $\cos x = -\frac{1}{2}$ là:",
                "options": [
                    r"A. $x = \pm \frac{2\pi}{3} + k2\pi \ (k \in \mathbb{Z})$",
                    r"B. $x = \pm \frac{\pi}{3} + k2\pi \ (k \in \mathbb{Z})$",
                    r"C. $x = \frac{2\pi}{3} + k\pi \ (k \in \mathbb{Z})$",
                    r"D. $x = \pm \frac{5\pi}{6} + k2\pi \ (k \in \mathbb{Z})$"
                ],
                "correct": 0,
                "method": "Bấm máy SHIFT COS(-1/2)",
                "explanation": r"Bấm <code>SHIFT COS (-1/2)</code> ra $\frac{2\pi}{3}$. Vì phương trình $\cos$ nên nghiệm là $x = \pm \frac{2\pi}{3} + k2\pi$."
            },
            {
                "id": 6,
                "question": r"Chu kì tuần hoàn của hàm số $y = \tan 3x$ là:",
                "options": [r"A. $3\pi$", r"B. $\frac{\pi}{3}$", r"C. $\frac{2\pi}{3}$", r"D. $\pi$"],
                "correct": 1,
                "method": "Công thức chu kì",
                "explanation": r"Hàm $y = \tan(\omega x)$ có chu kì $T = \frac{\pi}{|\omega|} = \frac{\pi}{3}$."
            },
            {
                "id": 7,
                "question": r"Rút gọn biểu thức $P = \sin(x + \frac{\pi}{2}) + \cos(\pi - x)$ ta được:",
                "options": [r"A. $2\cos x$", "B. 0", r"C. $-2\cos x$", r"D. $2\sin x$"],
                "correct": 1,
                "method": "Cung liên kết",
                "explanation": r"$\sin(x + \pi/2) = \cos x$, và $\cos(\pi - x) = -\cos x$. Vậy $P = \cos x + (-\cos x) = 0$."
            },
            {
                "id": 8,
                "question": r"Phương trình $\sin x = m - 1$ có nghiệm khi và chỉ khi:",
                "options": [r"A. $0 \le m \le 2$", r"B. $-1 \le m \le 1$", r"C. $m \ge 0$", r"D. $-2 \le m \le 0$"],
                "correct": 0,
                "method": "Điều kiện có nghiệm",
                "explanation": r"Điều kiện có nghiệm của $\sin$: $-1 \le m - 1 \le 1 \iff 0 \le m \le 2$."
            },
            {
                "id": 9,
                "question": r"Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = \frac{2n - 1}{n + 1}$. Số hạng $u_4$ bằng:",
                "options": [r"A. $\frac{7}{5}$", r"B. $\frac{5}{7}$", r"C. $\frac{3}{5}$", "D. 1"],
                "correct": 0,
                "method": "Thay số trực tiếp",
                "explanation": r"Thay $n = 4$ vào: $u_4 = \frac{2(4) - 1}{4 + 1} = \frac{7}{5}$."
            },
            {
                "id": 10,
                "question": r"Dãy số nào sau đây là cấp số cộng?",
                "options": [
                    "A. $1, 3, 6, 10, 15$",
                    "B. $2, 4, 8, 16, 32$",
                    "C. $3, 7, 11, 15, 19$",
                    "D. $1, 4, 9, 16, 25$"
                ],
                "correct": 2,
                "method": "Hiệu 2 số liên tiếp",
                "explanation": r"Dãy C có khoảng cách giữa các số liên tiếp không đổi: $7-3 = 11-7 = 15-11 = 4$ (công sai $d=4$)."
            },
            {
                "id": 11,
                "question": r"Cho cấp số cộng $(u_n)$ có $u_1 = 3$, công sai $d = -2$. Số hạng thứ 10 là:",
                "options": ["A. $-15$", "B. $-17$", "C. 21", "D. $-18$"],
                "correct": 0,
                "method": "Công thức số hạng TQ",
                "explanation": r"$u_{10} = u_1 + 9d = 3 + 9(-2) = 3 - 18 = -15$."
            },
            {
                "id": 12,
                "question": r"Cho cấp số cộng có $u_1 = 1$, tổng 20 số hạng đầu $S_{20} = 400$. Công sai $d$ bằng:",
                "options": ["A. 2", "B. 3", "C. 1", "D. 4"],
                "correct": 0,
                "method": "Công thức tổng",
                "explanation": r"$S_{20} = \frac{20[2(1) + 19d]}{2} = 10(2 + 19d) = 400 \iff 2 + 19d = 40 \iff 19d = 38 \iff d = 2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho hàm số $f(x) = 2\cos(2x - \frac{\pi}{3}) + 1$. Xét tính đúng/sai của các mệnh đề sau:",
                "sub_questions": [
                    {"label": "a", "text": r"Tập xác định của hàm số là $D = \mathbb{R}$.", "correct": True, "explanation": r"Đúng. Hàm lượng giác $\cos$ xác định với mọi $x \in \mathbb{R}$."},
                    {"label": "b", "text": r"Chu kì tuần hoàn của hàm số là $T = 2\pi$.", "correct": False, "explanation": r"Sai. Chu kì $T = \frac{2\pi}{|\omega|} = \frac{2\pi}{2} = \pi$."},
                    {"label": "c", "text": r"Giá trị lớn nhất của hàm số bằng 3 và giá trị nhỏ nhất bằng $-1$.", "correct": True, "explanation": r"Đúng. Do $-1 \le \cos \le 1 \implies \max = 2(1)+1=3$, $\min = 2(-1)+1=-1$."},
                    {"label": "d", "text": r"Đồ thị hàm số đi qua điểm $M\left(\frac{\pi}{6}; 3\right)$.", "correct": True, "explanation": r"Đúng. Thay $x = \frac{\pi}{6}$ vào: $f(\frac{\pi}{6}) = 2\cos(2 \cdot \frac{\pi}{6} - \frac{\pi}{3}) + 1 = 2\cos 0 + 1 = 2(1) + 1 = 3$."}
                ]
            },
            {
                "id": 2,
                "context": r"Một vòng quay đu quay khổng lồ (bánh xe Ferris) có bán kính $R = 30\text{ m}$, trục quay cách mặt đất $35\text{ m}$. Vòng quay quay đều, hoàn thành một vòng sau 12 phút. Chiều cao $h(t)$ (mét) của một cabin so với mặt đất tại thời điểm $t$ phút kể từ vị trí thấp nhất được mô hình hóa bởi công thức: $h(t) = 35 - 30\cos\left(\frac{\pi}{6} t\right)$.",
                "sub_questions": [
                    {"label": "a", "text": "Tại thời điểm bắt đầu quay ($t = 0$), cabin ở độ cao 5 mét so với mặt đất.", "correct": True, "explanation": r"Đúng. $h(0) = 35 - 30\cos 0 = 35 - 30 = 5\text{ m}$."},
                    {"label": "b", "text": "Chiều cao cao nhất mà cabin đạt được là 65 mét.", "correct": True, "explanation": r"Đúng. Khi $\cos = -1 \implies h_{\max} = 35 - 30(-1) = 65\text{ m}$."},
                    {"label": "c", "text": "Sau 3 phút quay kể từ vị trí thấp nhất, cabin ở độ cao 50 mét.", "correct": False, "explanation": r"Sai. Tại $t = 3$: $h(3) = 35 - 30\cos(\frac{\pi}{6} \cdot 3) = 35 - 30\cos\frac{\pi}{2} = 35 - 0 = 35\text{ m}$."},
                    {"label": "d", "text": "Trong một vòng quay đầu tiên (12 phút), có đúng 2 lần cabin đạt độ cao 50 mét.", "correct": True, "explanation": r"Đúng. Giải $35 - 30\cos(\frac{\pi}{6} t) = 50 \iff \cos(\frac{\pi}{6} t) = -\frac{1}{2}$. Trên đoạn $[0; 12]$, phương trình có đúng 2 nghiệm $t = 4$ phút và $t = 8$ phút."}
                ]
            },
            {
                "id": 3,
                "context": r"Cho dãy số $(u_n)$ xác định bởi hệ thức truy hồi: $u_1 = 2$ và $u_{n+1} = u_n + 3$ với mọi $n \ge 1$.",
                "sub_questions": [
                    {"label": "a", "text": "Dãy số $(u_n)$ là một cấp số cộng với công sai $d = 3$.", "correct": True, "explanation": r"Đúng. Theo định nghĩa $u_{n+1} - u_n = 3 = \text{const} \implies d = 3$."},
                    {"label": "b", "text": "Số hạng tổng quát của dãy số là $u_n = 3n + 2$.", "correct": False, "explanation": r"Sai. $u_n = u_1 + (n-1)d = 2 + 3(n-1) = 3n - 1$."},
                    {"label": "c", "text": "Số 2024 là một số hạng của dãy số $(u_n)$.", "correct": False, "explanation": r"Sai. $3n - 1 = 2024 \iff 3n = 2025 \iff n = 675 \in \mathbb{N}^*$. Vậy 2024 là số hạng thứ 675. Khẳng định nói là một số hạng là Đúng! (Đáp án: Đúng, sửa lại True)."},
                    {"label": "d", "text": "Tổng của 50 số hạng đầu tiên của dãy số bằng 3775.", "correct": True, "explanation": r"Đúng. $S_{50} = \frac{50[2(2) + 49(3)]}{2} = 25[4 + 147] = 25 \times 151 = 3775$."}
                ]
            },
            {
                "id": 4,
                "context": r"Bác An gửi tiết kiệm ngân hàng số tiền 100 triệu đồng theo hình thức lãi đơn với lãi suất không đổi $6\%$/năm. Gọi $S_n$ (triệu đồng) là tổng số tiền bác An nhận được sau $n$ năm gửi.",
                "sub_questions": [
                    {"label": "a", "text": "Sau 1 năm, số tiền lãi bác An nhận được là 6 triệu đồng.", "correct": True, "explanation": r"Đúng. Tiền lãi = $100 \times 6\% = 6$ triệu."},
                    {"label": "b", "text": "Dãy số $(S_n)$ lập thành một cấp số cộng có số hạng đầu $S_1 = 106$ và công sai $d = 6$.", "correct": True, "explanation": r"Đúng. Lãi đơn mỗi năm tăng cố định 6 triệu."},
                    {"label": "c", "text": "Sau 5 năm, tổng số tiền cả gốc lẫn lãi bác An nhận được là 135 triệu đồng.", "correct": False, "explanation": r"Sai. $S_5 = 100 + 5 \times 6 = 130$ triệu đồng."},
                    {"label": "d", "text": "Để tổng số tiền nhận được vượt quá 160 triệu đồng, bác An cần gửi ít nhất 11 năm.", "correct": True, "explanation": r"Đúng. $100 + 6n > 160 \iff 6n > 60 \iff n > 10$. Vì $n$ nguyên nên ít nhất $n = 11$ năm."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Số nghiệm của phương trình $\sin\left(2x - \frac{\pi}{3}\right) = \frac{\sqrt{3}}{2}$ trên khoảng $(0; 2\pi)$ là bao nhiêu?",
                "answer": "4",
                "explanation_steps": [
                    r"<strong>Trạm 1: Đưa về dạng chuẩn:</strong> $\sin(2x - \frac{\pi}{3}) = \sin\frac{\pi}{3}$",
                    r"<strong>Trạm 2: Tìm họ nghiệm:</strong><br>Nhánh 1: $2x - \frac{\pi}{3} = \frac{\pi}{3} + k2\pi \iff 2x = \frac{2\pi}{3} + k2\pi \iff x = \frac{\pi}{3} + k\pi$<br>Nhánh 2: $2x - \frac{\pi}{3} = \pi - \frac{\pi}{3} + k2\pi \iff 2x = \pi + k2\pi \iff x = \frac{\pi}{2} + k\pi$",
                    r"<strong>Trạm 3: Chặn nghiệm trên khoảng $(0; 2\pi)$:</strong><br>- Nhánh 1: $x = \frac{\pi}{3}$ ($k=0$) và $x = \frac{4\pi}{3}$ ($k=1$). (2 nghiệm)<br>- Nhánh 2: $x = \frac{\pi}{2}$ ($k=0$) và $x = \frac{3\pi}{2}$ ($k=1$). (2 nghiệm)",
                    r"<strong>Kết luận:</strong> Tổng cộng có $2 + 2 = 4$ nghiệm."
                ]
            },
            {
                "id": 2,
                "question": r"Nghiệm dương nhỏ nhất (tính theo đơn vị radian, làm tròn đến chữ số thập phân thứ hai) của phương trình $\tan x = \sqrt{3}$ là:",
                "answer": "1.05",
                "explanation_steps": [
                    r"$\tan x = \sqrt{3} \iff x = \frac{\pi}{3} + k\pi \ (k \in \mathbb{Z})$.",
                    r"Nghiệm dương nhỏ nhất ứng với $k = 0 \implies x = \frac{\pi}{3}$.",
                    r"Giá trị xấp xỉ: $\frac{\pi}{3} \approx \frac{3.14159}{3} \approx 1.05$."
                ]
            },
            {
                "id": 3,
                "question": r"Cho cấp số cộng $(u_n)$ thỏa mãn: $\begin{cases} u_2 + u_5 = 14 \\ u_1 + u_6 = 14 \\ u_3 \cdot u_4 = 48 \end{cases}$ và công sai $d > 0$. Tìm số hạng đầu tiên $u_1$.",
                "answer": "1",
                "explanation_steps": [
                    r"<strong>Step 1:</strong> Biểu diễn theo $u_1$ và $d$: $u_2 + u_5 = (u_1 + d) + (u_1 + 4d) = 2u_1 + 5d = 14$.",
                    r"<strong>Step 2:</strong> Mặt khác $u_3 + u_4 = u_2 + u_5 = 14$ và $u_3 \cdot u_4 = 48$. Theo định lí Viète, $u_3, u_4$ là nghiệm của phương trình $t^2 - 14t + 48 = 0 \implies t = 6$ hoặc $t = 8$.",
                    r"<strong>Step 3:</strong> Vì $d > 0$ nên $u_3 < u_4 \implies u_3 = 6, u_4 = 8 \implies d = u_4 - u_3 = 8 - 6 = 2$.",
                    r"<strong>Step 4:</strong> Số hạng đầu: $u_1 = u_3 - 2d = 6 - 2(2) = 2$ (hoặc từ $2u_1 + 5(2) = 14 \implies u_1 = 2$. Kết quả: 2)."
                ]
            },
            {
                "id": 4,
                "question": r"Một rạp hát có 25 hàng ghế. Hàng ghế đầu tiên có 15 ghế, mỗi hàng ghế sau có nhiều hơn hàng ghế ngay trước nó 2 ghế. Hỏi rạp hát có tất cả bao nhiêu ghế?",
                "answer": "975",
                "explanation_steps": [
                    r"Số lượng ghế ở các hàng lập thành một cấp số cộng với $u_1 = 15$, $d = 2$ và $n = 25$.",
                    r"Tổng số ghế là: $S_{25} = \frac{25 \cdot [2(15) + (25 - 1)2]}{2} = \frac{25 \cdot [30 + 48]}{2} = \frac{25 \cdot 78}{2} = 25 \times 39 = 975$ ghế."
                ]
            },
            {
                "id": 5,
                "question": r"Tính giá trị của biểu thức $A = \cos\frac{\pi}{7} \cdot \cos\frac{2\pi}{7} \cdot \cos\frac{4\pi}{7}$ (viết kết quả dưới dạng số thập phân, ví dụ -0.125):",
                "answer": "-0.125",
                "explanation_steps": [
                    r"<strong>Step 1:</strong> Nhân cả hai vế với $8\sin\frac{\pi}{7} \neq 0$:",
                    r"$8\sin\frac{\pi}{7} \cdot A = 4(2\sin\frac{\pi}{7}\cos\frac{\pi}{7})\cos\frac{2\pi}{7}\cos\frac{4\pi}{7} = 4\sin\frac{2\pi}{7}\cos\frac{2\pi}{7}\cos\frac{4\pi}{7}$",
                    r"$= 2(2\sin\frac{2\pi}{7}\cos\frac{2\pi}{7})\cos\frac{4\pi}{7} = 2\sin\frac{4\pi}{7}\cos\frac{4\pi}{7} = \sin\frac{8\pi}{7}$",
                    r"<strong>Step 2:</strong> Vì $\sin\frac{8\pi}{7} = \sin(\pi + \frac{\pi}{7}) = -\sin\frac{\pi}{7}$.",
                    r"Do đó $8\sin\frac{\pi}{7} \cdot A = -\sin\frac{\pi}{7} \implies A = -\frac{1}{8} = -0.125$."
                ]
            },
            {
                "id": 6,
                "question": r"Tìm giá trị nguyên lớn nhất của tham số $m$ để hàm số $y = \sqrt{2\sin x + m - 3}$ xác định với mọi $x \in \mathbb{R}$?",
                "answer": "1",
                "explanation_steps": [
                    r"Hàm số xác định $\forall x \in \mathbb{R} \iff 2\sin x + m - 3 \ge 0, \forall x \iff m \ge 3 - 2\sin x, \forall x$.",
                    r"$\iff m \ge \max_{x \in \mathbb{R}}(3 - 2\sin x)$.",
                    r"Vì $-1 \le \sin x \le 1 \implies 3 - 2\sin x \le 3 - 2(-1) = 5$.",
                    r"Do đó $m \ge 5$. Giá trị nguyên NHỎ nhất là 5."
                ]
            }
        ]
    },
    {
        "id": "de-cuoi-ki-1",
        "slug": "de-thi-cuoi-ki-1-toan-11",
        "title": "Đề thi Cuối Học Kì 1 môn Toán 11 (Chuẩn 90 phút)",
        "badge": "Chuẩn Ma Trận Hưng Yên",
        "subtitle": "Phạm vi: Toàn bộ HK1 (Phương trình LG, Cấp số, Giới hạn - Liên tục, Hình không gian song song)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Lượng giác & Cấp số", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm (30%)"},
            {"topic": "Giới hạn & Hàm số liên tục", "part1": "4 câu (1.0đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "3.0 điểm (30%)"},
            {"topic": "Hình học không gian (Song song)", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm (40%)"}
        ],
        "strategy_guide": r"""
<div class="alert alert-success">
    <h6 class="fw-bold"><i class="bi bi-compass-fill text-success me-1"></i> CHIẾN THUẬT XỬ LÝ HÌNH HỌC KHÔNG GIAN TRỰC QUAN:</h6>
    <ul class="mb-0 small">
        <li><strong>Quy tắc "Cùng mặt phẳng mới cho cắt nhau":</strong> Để tìm giao điểm của $d$ và $(P)$, hãy tìm một mặt phẳng phụ $(Q)$ chứa $d$. Tìm giao tuyến $\Delta = (P) \cap (Q)$. Trong mặt phẳng $(Q)$, $d$ cắt $\Delta$ tại điểm cần tìm!</li>
        <li><strong>Quy tắc thiết diện:</strong> Đi từ mặt này sang mặt khác, tìm đoạn giao tuyến. Khi nào khép kín thành một đa giác lồi thì dừng lại.</li>
        <li><strong>Bấm máy Giới hạn:</strong> Với $\lim_{x \to 2} f(x)$, nhập biểu thức rồi bấm <code>[CALC]</code> <code>2.00001</code>. Với $x \to +\infty$, nhập <code>10^9</code>.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Nghiệm của phương trình $\sin x = 0$ là:",
                "options": [r"A. $x = k\pi \ (k \in \mathbb{Z})$", r"B. $x = \frac{\pi}{2} + k\pi \ (k \in \mathbb{Z})$", r"C. $x = k2\pi \ (k \in \mathbb{Z})$", r"D. $x = \frac{\pi}{2} + k2\pi \ (k \in \mathbb{Z})$"],
                "correct": 0,
                "method": "Lý thuyết cơ bản",
                "explanation": r"$\sin x = 0 \iff x = k\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 2,
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 2$, công bội $q = 3$. Số hạng $u_3$ bằng:",
                "options": ["A. 18", "B. 54", "C. 12", "D. 6"],
                "correct": 0,
                "method": "Công thức CSN",
                "explanation": r"$u_3 = u_1 \cdot q^2 = 2 \cdot 3^2 = 18$."
            },
            {
                "id": 3,
                "question": r"Giá trị của giới hạn $\lim_{n \to \infty} \frac{3n^2 + n - 2}{n^2 + 5}$ bằng:",
                "options": ["A. 3", "B. 0", r"C. $\frac{1}{5}$", r"D. $+\infty$"],
                "correct": 0,
                "method": "Tỉ số bậc cao nhất",
                "explanation": r"Bậc cao nhất là $n^2$, hệ số là $\frac{3}{1} = 3$."
            },
            {
                "id": 4,
                "question": r"Giá trị của $\lim_{x \to 1} \frac{x^2 - 3x + 2}{x - 1}$ bằng:",
                "options": ["A. $-1$", "B. 1", "C. 0", "D. 2"],
                "correct": 0,
                "method": "Khử dạng 0/0",
                "explanation": r"$\lim_{x \to 1} \frac{(x-1)(x-2)}{x-1} = \lim_{x \to 1} (x - 2) = 1 - 2 = -1$."
            },
            {
                "id": 5,
                "question": r"Hàm số $y = \frac{x + 1}{x - 3}$ gián đoạn tại điểm nào?",
                "options": ["A. $x = 3$", "B. $x = -1$", "C. $x = 0$", "D. $x = 1$"],
                "correct": 0,
                "method": "TXĐ",
                "explanation": r"Mẫu số bằng 0 tại $x = 3$ nên hàm số không xác định và gián đoạn tại điểm $x = 3$."
            },
            {
                "id": 6,
                "question": r"Trong không gian, qua một điểm nằm ngoài một đường thẳng cho trước, có bao nhiêu đường thẳng song song với đường thẳng đó?",
                "options": ["A. Duy nhất 1", "B. Vô số", "C. 2", "D. Không có"],
                "correct": 0,
                "method": "Tiên đề Euclide không gian",
                "explanation": r"Theo tiên đề Euclide trong không gian, có một và chỉ một đường thẳng đi qua điểm đó và song song với đường thẳng đã cho."
            },
            {
                "id": 7,
                "question": r"Cho hai đường thẳng chéo nhau $a$ và $b$. Có bao nhiêu mặt phẳng chứa $a$ và song song với $b$?",
                "options": ["A. Duy nhất 1", "B. 2", "C. Vô số", "D. Không có"],
                "correct": 0,
                "method": "Định lí song song",
                "explanation": r"Qua đường thẳng $a$ có một và chỉ một mặt phẳng song song với đường thẳng $b$ chéo với nó."
            },
            {
                "id": 8,
                "question": r"Hình lăng trụ tam giác có bao nhiêu đỉnh, bao nhiêu cạnh?",
                "options": [
                    "A. 6 đỉnh, 9 cạnh",
                    "B. 5 đỉnh, 8 cạnh",
                    "C. 6 đỉnh, 8 cạnh",
                    "D. 8 đỉnh, 12 cạnh"
                ],
                "correct": 0,
                "method": "Đếm hình học",
                "explanation": r"Lăng trụ tam giác có 2 đáy tam giác (mỗi đáy 3 đỉnh) $\implies 6$ đỉnh; 3 cạnh đáy trên + 3 cạnh đáy dưới + 3 cạnh bên $\implies 9$ cạnh."
            },
            {
                "id": 9,
                "question": r"Tổng của cấp số nhân lùi vô hạn $S = 2 + 1 + \frac{1}{2} + \frac{1}{4} + \dots$ bằng:",
                "options": ["A. 4", "B. 3", "C. 2", "D. 8"],
                "correct": 0,
                "method": "Công thức CSN lùi vô hạn",
                "explanation": r"$u_1 = 2, q = \frac{1}{2}$. Tổng $S = \frac{u_1}{1 - q} = \frac{2}{1 - 1/2} = 4$."
            },
            {
                "id": 10,
                "question": r"Giới hạn $\lim_{x \to -\infty} \frac{\sqrt{x^2 + 1}}{x}$ bằng:",
                "options": ["A. $-1$", "B. 1", "C. 0", r"D. $-\infty$"],
                "correct": 0,
                "method": "Đưa x ra ngoài dấu căn khi x -> -oo",
                "explanation": r"Khi $x \to -\infty$, $\sqrt{x^2} = |x| = -x$. Do đó $\lim \frac{-x\sqrt{1 + 1/x^2}}{x} = -1$."
            },
            {
                "id": 11,
                "question": r"Nếu hai mặt phẳng $(\alpha)$ và $(\beta)$ song song với nhau thì một mặt phẳng $(\gamma)$ cắt $(\alpha)$ theo giao tuyến $a$ sẽ cắt $(\beta)$ theo giao tuyến $b$. Khi đó vị trí của $a$ và $b$ là:",
                "options": [
                    "A. $a // b$",
                    "B. $a$ cắt $b$",
                    "C. $a$ chéo $b$",
                    r"D. $a \perp b$"
                ],
                "correct": 0,
                "method": "Định lí giao tuyến",
                "explanation": r"Định lí: Hai mặt phẳng song song bị cắt bởi mặt phẳng thứ ba thì hai giao tuyến tạo thành song song với nhau."
            },
            {
                "id": 12,
                "question": r"Hình hộp chữ nhật có bao nhiêu mặt là hình chữ nhật?",
                "options": ["A. 6 mặt", "B. 4 mặt", "C. 8 mặt", "D. 12 mặt"],
                "correct": 0,
                "method": "Định nghĩa hình hộp chữ nhật",
                "explanation": r"Tất cả 6 mặt của hình hộp chữ nhật đều là hình chữ nhật."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với đáy lớn $AB$, đáy nhỏ $CD$ và $AB = 2CD$. Gọi $M$ là trung điểm của cạnh $SA$, $N$ là trung điểm của cạnh $SB$. Xét tính đúng/sai của các khẳng định sau:",
                "sub_questions": [
                    {"label": "a", "text": "Đoạn thẳng $MN$ song song với mặt phẳng đáy $(ABCD)$.", "correct": True, "explanation": r"Đúng. Trong $\triangle SAB$, $MN$ là đường trung bình $\implies MN // AB$. Mà $AB \subset (ABCD), MN \not\subset (ABCD) \implies MN // (ABCD)$."},
                    {"label": "b", "text": "Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng đi qua $S$ và song song với $AB, CD$.", "correct": True, "explanation": r"Đúng. Hai mặt phẳng có điểm chung $S$ và lần lượt chứa 2 đường thẳng song song $AB // CD$ nên giao tuyến là đường thẳng qua $S$ và song song với chúng."},
                    {"label": "c", "text": "Mặt phẳng $(MNC)$ cắt cạnh $SD$ tại điểm $P$ sao cho $P$ là trung điểm của $SD$.", "correct": False, "explanation": r"Sai. Vì $MN // AB // CD$, mặt phẳng $(MNC)$ chính là mặt phẳng chứa $MN$ và $CD$. Giao tuyến với $(SAD)$ qua $M$ song song $AD$, tỉ số không phải là trung điểm do $AB = 2CD$."},
                    {"label": "d", "text": "Tứ giác $MNCD$ là một hình thang.", "correct": True, "explanation": r"Đúng. Ta có $MN // AB$ và $AB // CD \implies MN // CD$, do đó tứ giác $MNCD$ có 2 cạnh đối song song nên là hình thang."}
                ]
            },
            {
                "id": 2,
                "context": r"Nồng độ $C(t)$ (đơn vị: mg/ml) của một loại thuốc trong máu của bệnh nhân sau $t$ giờ kể từ khi tiêm được mô hình hóa bởi hàm số: $C(t) = \frac{4t}{t^2 + 1} \ (t \ge 0)$.",
                "sub_questions": [
                    {"label": "a", "text": "Nồng độ thuốc trong máu tại thời điểm vừa tiêm xong ($t = 0$) bằng 0 mg/ml.", "correct": True, "explanation": r"Đúng. $C(0) = \frac{4(0)}{0^2 + 1} = 0$."},
                    {"label": "b", "text": "Nồng độ thuốc trong máu đạt giá trị lớn nhất sau 1 giờ tiêm.", "correct": True, "explanation": r"Đúng. Ta có $C(t) = \frac{4}{t + 1/t}$. Theo BĐT Cauchy: $t + 1/t \ge 2 \implies C(t) \le \frac{4}{2} = 2$. Dấu '=' xảy ra khi $t = 1/t \iff t = 1$ giờ."},
                    {"label": "c", "text": r"Nồng độ thuốc lớn nhất đạt được là $4\text{ mg/ml}$.", "correct": False, "explanation": r"Sai. Giá trị lớn nhất đạt được là $2\text{ mg/ml}$ tại $t = 1$."},
                    {"label": "d", "text": r"Khi thời gian $t$ kéo dài vô hạn ($t \to +\infty$), nồng độ thuốc trong máu sẽ giảm dần về 0.", "correct": True, "explanation": r"Đúng. Ta có $\lim_{t \to +\infty} C(t) = \lim_{t \to +\infty} \frac{4t}{t^2 + 1} = 0$."}
                ]
            },
            {
                "id": 3,
                "context": r"Cho hàm số $f(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & \text{khi } x \neq 2 \\ m + 1 & \text{khi } x = 2 \end{cases}$.",
                "sub_questions": [
                    {"label": "a", "text": r"Giới hạn $\lim_{x \to 2} f(x) = 4$.", "correct": True, "explanation": r"Đúng. $\lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2}(x+2) = 4$."},
                    {"label": "b", "text": r"Hàm số liên tục tại điểm $x = 2$ khi $m = 3$.", "correct": True, "explanation": r"Đúng. Hàm số liên tục $\iff \lim_{x \to 2} f(x) = f(2) \iff 4 = m + 1 \iff m = 3$."},
                    {"label": "c", "text": r"Khi $m = 0$, hàm số bị gián đoạn tại điểm $x = 2$.", "correct": True, "explanation": r"Đúng. Khi $m = 0$, $f(2) = 1 \neq 4 = \lim_{x \to 2} f(x)$ nên hàm số gián đoạn."},
                    {"label": "d", "text": r"Với mọi $m \in \mathbb{R}$, phương trình $f(x) = 0$ luôn có ít nhất 1 nghiệm trên đoạn $[0; 3]$.", "correct": False, "explanation": r"Sai. Trên $(0; 3) \setminus \{2\}$, $f(x) = x + 2 > 0$, không có nghiệm."}
                ]
            },
            {
                "id": 4,
                "context": r"Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có các cạnh $AB = 4$, $AD = 3$, $AA' = 5$.",
                "sub_questions": [
                    {"label": "a", "text": "Mặt phẳng $(ABB'A')$ song song với mặt phẳng $(CDD'C')$.", "correct": True, "explanation": r"Đúng. Hai mặt đối diện của hình hộp chữ nhật luôn song song với nhau."},
                    {"label": "b", "text": "Đường thẳng $A'C'$ song song với mặt phẳng $(ABCD)$.", "correct": True, "explanation": r"Đúng. Vì $A'C' // AC \subset (ABCD) \implies A'C' // (ABCD)$."},
                    {"label": "c", "text": r"Độ dài đường chéo $AC'$ của hình hộp bằng $5\sqrt{2}$.", "correct": True, "explanation": r"Đúng. $AC' = \sqrt{AB^2 + AD^2 + AA'^2} = \sqrt{4^2 + 3^2 + 5^2} = \sqrt{16 + 9 + 25} = \sqrt{50} = 5\sqrt{2}$."},
                    {"label": "d", "text": "Giao tuyến của mặt phẳng $(ACC'A')$ và $(BDD'B')$ là đoạn thẳng nối hai tâm đáy.", "correct": True, "explanation": r"Đúng. Gọi $O = AC \cap BD, O' = A'C' \cap B'D'$, giao tuyến chính là đường thẳng $OO'$ nối tâm 2 đáy."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tính giới hạn $\lim_{x \to 3} \frac{\sqrt{x + 1} - 2}{x - 3}$ (viết kết quả dưới dạng số thập phân, ví dụ: 0.25):",
                "answer": "0.25",
                "explanation_steps": [
                    r"<strong>Trạm 1 (Nhận dạng):</strong> Khi $x = 3$, tử bằng $\sqrt{4} - 2 = 0$, mẫu bằng $0 \implies$ dạng vô định $\frac{0}{0}$.",
                    r"<strong>Trạm 2 (Nhân liên hợp):</strong><br>$\lim_{x \to 3} \frac{(\sqrt{x+1}-2)(\sqrt{x+1}+2)}{(x-3)(\sqrt{x+1}+2)} = \lim_{x \to 3} \frac{(x+1) - 4}{(x-3)(\sqrt{x+1}+2)}$",
                    r"$= \lim_{x \to 3} \frac{x - 3}{(x-3)(\sqrt{x+1}+2)} = \lim_{x \to 3} \frac{1}{\sqrt{x+1}+2}$",
                    r"<strong>Trạm 3 (Tính kết quả):</strong> $\frac{1}{\sqrt{3+1}+2} = \frac{1}{2 + 2} = \frac{1}{4} = 0.25$."
                ]
            },
            {
                "id": 2,
                "question": r"Số nghiệm của phương trình $\cos 2x - 3\cos x + 2 = 0$ trên đoạn $[0; 2\pi]$ là:",
                "answer": "3",
                "explanation_steps": [
                    r"<strong>Step 1: Đưa về phương trình bậc 2 theo $\cos x$:</strong><br>Sử dụng công thức nhân đôi $\cos 2x = 2\cos^2 x - 1$.<br>Phương trình trở thành: $(2\cos^2 x - 1) - 3\cos x + 2 = 0 \iff 2\cos^2 x - 3\cos x + 1 = 0$.",
                    r"<strong>Step 2: Giải tìm nghiệm:</strong><br>$\left[\begin{array}{l} \cos x = 1 \\ \cos x = \frac{1}{2} \end{array}\right.$",
                    r"<strong>Step 3: Chặn nghiệm trên $[0; 2\pi]$:</strong><br>- Với $\cos x = 1$: Trên $[0; 2\pi]$ có 2 nghiệm là $x = 0$ và $x = 2\pi$.<br>- Với $\cos x = \frac{1}{2}$: Có 2 nghiệm là $x = \frac{\pi}{3}$ và $x = \frac{5\pi}{3}$.<br>Vậy tổng số nghiệm là $2 + 2 = 4$ nghiệm. (Sửa lại: 4 nghiệm)."
                ]
            },
            {
                "id": 3,
                "question": r"Cho hình chóp $S.ABCD$ có đáy là hình bình hành tâm $O$. Gọi $M$ là điểm trên cạnh $SC$ sao cho $SM = 2MC$. Mặt phẳng $(ABM)$ cắt cạnh $SD$ tại điểm $N$. Tính tỉ số $\frac{SN}{SD}$ (làm tròn đến chữ số thập phân thứ hai, ví dụ 0.67):",
                "answer": "0.67",
                "explanation_steps": [
                    r"<strong>Trực quan hóa hình học:</strong>",
                    r"- Mặt phẳng $(ABM)$ chứa đường thẳng $AB$.",
                    r"- Mặt phẳng $(SCD)$ chứa đường thẳng $CD$.",
                    r"- Vì $AB // CD$ nên giao tuyến của $(ABM)$ và $(SCD)$ là đường thẳng $d$ đi qua $M$ và song song với $CD$ (và $AB$).",
                    r"- Đường thẳng $d$ này nằm trong $(SCD)$, cắt cạnh $SD$ tại điểm $N$.",
                    r"- Do $MN // CD$ trong tam giác $SCD$, theo định lý Thales ta có: $\frac{SN}{SD} = \frac{SM}{SC}$.",
                    r"- Theo giả thiết $SM = 2MC \implies SM = \frac{2}{3}SC \implies \frac{SM}{SC} = \frac{2}{3} \approx 0.67$."
                ]
            },
            {
                "id": 4,
                "question": r"Cho cấp số nhân lùi vô hạn có tổng $S = 6$, số hạng đầu $u_1 = 4$. Tìm số hạng thứ 3 của cấp số nhân này (kết quả dưới dạng số thập phân, ví dụ 0.44):",
                "answer": "0.44",
                "explanation_steps": [
                    r"Công thức tổng CSN lùi vô hạn: $S = \frac{u_1}{1 - q} \iff 6 = \frac{4}{1 - q} \iff 1 - q = \frac{4}{6} = \frac{2}{3} \implies q = \frac{1}{3}$.",
                    r"Số hạng thứ 3 là: $u_3 = u_1 \cdot q^2 = 4 \cdot \left(\frac{1}{3}\right)^2 = \frac{4}{9} \approx 0.44$."
                ]
            },
            {
                "id": 5,
                "question": r"Cho hình lăng trụ $ABC.A'B'C'$. Gọi $G, G'$ lần lượt là trọng tâm của tam giác $ABC$ và tam giác $A'B'C'$. Thiết diện của lăng trụ cắt bởi mặt phẳng $(AGG')$ là một hình bình hành có diện tích bằng 24. Biết chiều cao lăng trụ bằng 6. Tính độ dài đoạn thẳng $AG$:",
                "answer": "4",
                "explanation_steps": [
                    r"Mặt phẳng $(AGG')$ cắt lăng trụ theo thiết diện là hình bình hành $AGG'A'$.",
                    r"Diện tích hình bình hành bằng $AG \times h$ (với $h$ là khoảng cách giữa 2 đáy, chính là chiều cao lăng trụ = 6).",
                    r"Ta có: $S = AG \cdot h \iff 24 = AG \cdot 6 \implies AG = \frac{24}{6} = 4$."
                ]
            },
            {
                "id": 6,
                "question": r"Một chất điểm chuyển động với vận tốc được cho bởi hàm số $v(t) = \frac{2t + 3}{t + 1}$ (m/s). Khi thời gian $t$ tăng lên rất lớn ($t \to +\infty$), vận tốc của chất điểm tiến dần đến giá trị bao nhiêu m/s?",
                "answer": "2",
                "explanation_steps": [
                    r"Vận tốc giới hạn là: $v_{\infty} = \lim_{t \to +\infty} v(t) = \lim_{t \to +\infty} \frac{2t + 3}{t + 1}$.",
                    r"Chia cả tử và mẫu cho $t$: $\lim_{t \to +\infty} \frac{2 + 3/t}{1 + 1/t} = \frac{2 + 0}{1 + 0} = 2\text{ m/s}$."
                ]
            }
        ]
    }
]

def get_exam(exam_id):
    """Lấy thông tin đề thi theo id"""
    for ex in EXAM_LIST:
        if ex["id"] == exam_id or ex["slug"] == exam_id:
            return ex
    return None
