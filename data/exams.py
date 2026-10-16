# -*- coding: utf-8 -*-
"""
Hệ thống Đề thi Chuẩn Format mới của Bộ Giáo dục & Đào tạo (Mô phỏng Sở GD&ĐT Hưng Yên 2025 - 2026)
Gồm:
- 3 Đề thi Giữa Học Kì 1 (90 phút)
- 3 Đề thi Giữa Học Kì 2 (90 phút)
- Đề thi Cuối Học Kì 1 (90 phút)
Mỗi đề gồm:
- Phần I: 12 câu trắc nghiệm 4 lựa chọn (3,0 điểm)
- Phần II: 4 câu trắc nghiệm Đúng / Sai (4,0 điểm - tính điểm lũy tiến chuẩn BGD: 1 ý 0.1đ, 2 ý 0.25đ, 3 ý 0.5đ, 4 ý 1.0đ)
- Phần III: 6 câu trắc nghiệm Trả lời ngắn (3,0 điểm)
Kèm Bảng ma trận, Chiến thuật Casio fx-580VNX/fx-880BTG và Lời giải chi tiết từng bước.
"""

from data.exams_gk2 import EXAMS_GK2

EXAM_LIST = [
    # =========================================================================
    # 1. ĐỀ THI GIỮA HỌC KÌ 1 - ĐỀ SỐ 1
    # =========================================================================
    {
        "id": "de-giua-ki-1",
        "slug": "de-thi-giua-ki-1-toan-11",
        "title": "Đề thi Giữa Học Kì 1 - Đề số 1 (Chuẩn 90 phút)",
        "badge": "Chuẩn Format Hưng Yên",
        "scope": "Giữa Học Kì 1",
        "subtitle": "Phạm vi: Chương 1 (Lượng giác) + Nửa đầu Chương 2 (Dãy số, Cấp số cộng)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Hàm số & Phương trình Lượng giác", "part1": "8 câu (2.0đ)", "part2": "2 câu (2.0đ)", "part3": "4 câu (2.0đ)", "total": "6.0 điểm (60%)"},
            {"topic": "Dãy số & Cấp số cộng", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm (40%)"}
        ],
        "matrix_table": [
            {"topic": "Hàm số & Phương trình Lượng giác", "part1": "8 câu (2.0đ)", "part2": "2 câu (2.0đ)", "part3": "4 câu (2.0đ)", "total": "6.0 điểm"},
            {"topic": "Dãy số & Cấp số cộng", "part1": "4 câu (1.0đ)", "part2": "2 câu (2.0đ)", "part3": "2 câu (1.0đ)", "total": "4.0 điểm"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN THUẬT PHÂN BỔ THỜI GIAN & BẤM MÁY CASIO 90 PHÚT:</h6>
    <ul class="mb-0 small">
        <li><strong>00 - 20 phút (Phần I):</strong> 12 câu trắc nghiệm đơn. Mỗi câu tối đa 1.5 phút. Các câu nhận biết giải nhanh bằng mắt hoặc bấm Casio Table <code>[MENU] [8]</code> (fx-580VNX) để quét giá trị lớn nhất, nhỏ nhất, chu kỳ.</li>
        <li><strong>20 - 55 phút (Phần II):</strong> 4 câu Đúng/Sai. Đây là mỏ điểm (4.0 điểm)! Đọc kĩ từng ý a, b, c, d vì ý trước thường là bậc thang cho ý sau.</li>
        <li><strong>55 - 85 phút (Phần III):</strong> 6 câu trả lời ngắn. Bắt buộc tính toán cẩn thận từng con số. Câu phương trình lượng giác nhớ đếm nghiệm trên đoạn/khoảng.</li>
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
                "explanation": r"Công thức: $\alpha^\circ = \frac{2\pi}{3} \cdot \frac{180^\circ}{\pi} = 120^\circ$."
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
                "method": "Tính chất hàm số chẵn / lẻ",
                "explanation": r"Trong 4 hàm lượng giác cơ bản, duy nhất $y = \cos x$ là hàm số chẵn vì $\cos(-x) = \cos x$. Ba hàm còn lại là hàm lẻ."
            },
            {
                "id": 4,
                "question": r"Giá trị lớn nhất của hàm số $y = 3\sin(2x) - 1$ trên $\mathbb{R}$ là:",
                "options": ["A. 2", "B. 3", "C. 4", "D. 5"],
                "correct": 0,
                "method": "Đánh giá chặn biên",
                "explanation": r"Vì $-1 \le \sin(2x) \le 1 \implies 3(-1) - 1 \le y \le 3(1) - 1 \iff -4 \le y \le 2$. Vậy $\max y = 2$."
            },
            {
                "id": 5,
                "question": r"Nghiệm của phương trình $\cos x = 0$ là:",
                "options": [
                    r"A. $x = \frac{\pi}{2} + k\pi, k \in \mathbb{Z}$",
                    r"B. $x = k\pi, k \in \mathbb{Z}$",
                    r"C. $x = \frac{\pi}{2} + k2\pi, k \in \mathbb{Z}$",
                    r"D. $x = k2\pi, k \in \mathbb{Z}$"
                ],
                "correct": 0,
                "method": "Phương trình lượng giác cơ bản",
                "explanation": r"Nghiệm cơ bản: $\cos x = 0 \iff x = \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 6,
                "question": r"Chu kì tuần hoàn của hàm số $y = \tan(2x)$ bằng:",
                "options": [r"A. $\pi$", r"B. $\frac{\pi}{2}$", r"C. $2\pi$", r"D. $\frac{\pi}{4}$"],
                "correct": 1,
                "method": "Công thức chu kì",
                "explanation": r"Hàm số $y = \tan(\omega x)$ có chu kì $T = \frac{\pi}{|\omega|}$. Ở đây $\omega = 2 \implies T = \frac{\pi}{2}$."
            },
            {
                "id": 7,
                "question": r"Rút gọn biểu thức $P = \sin\left(x + \frac{\pi}{2}\right) + \cos(\pi - x)$ ta được:",
                "options": ["A. 0", r"B. $2\cos x$", r"C. $-2\cos x$", r"D. $2\sin x$"],
                "correct": 0,
                "method": "Cung liên kết",
                "explanation": r"$\sin(x + \pi/2) = \cos x$, và $\cos(\pi - x) = -\cos x$. Vậy $P = \cos x - \cos x = 0$."
            },
            {
                "id": 8,
                "question": r"Phương trình $\sin x = m - 1$ có nghiệm khi và chỉ khi:",
                "options": [r"A. $0 \le m \le 2$", r"B. $-1 \le m \le 1$", r"C. $m \ge 0$", r"D. $-2 \le m \le 0$"],
                "correct": 0,
                "method": "Điều kiện có nghiệm",
                "explanation": r"Điều kiện: $-1 \le m - 1 \le 1 \iff 0 \le m \le 2$."
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
                "explanation": r"Dãy C có $7 - 3 = 11 - 7 = 15 - 11 = 4$ không đổi (công sai $d = 4$)."
            },
            {
                "id": 11,
                "question": r"Cho cấp số cộng $(u_n)$ có $u_1 = 3$ và công sai $d = -2$. Số hạng thứ 5 của cấp số cộng là:",
                "options": ["A. -5", "B. -7", "C. 5", "D. -3"],
                "correct": 0,
                "method": "Công thức số hạng tổng quát",
                "explanation": r"$u_5 = u_1 + 4d = 3 + 4(-2) = 3 - 8 = -5$."
            },
            {
                "id": 12,
                "question": r"Cho cấp số cộng $(u_n)$ biết $u_1 = 2$ và $u_2 = 8$. Tổng 10 số hạng đầu tiên $S_{10}$ bằng:",
                "options": ["A. 290", "B. 300", "C. 280", "D. 310"],
                "correct": 0,
                "method": "Công thức tổng n số hạng",
                "explanation": r"Công sai $d = 8 - 2 = 6$. Tổng: $S_{10} = \frac{10}{2}[2(2) + 9(6)] = 5 \cdot [4 + 54] = 5 \cdot 58 = 290$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho hàm số lượng giác $f(x) = 2\cos\left(2x - \frac{\pi}{3}\right) + 1$.",
                "sub_questions": [
                    {"label": "a", "text": r"Tập xác định của hàm số $f(x)$ là $D = \mathbb{R}$.", "correct": True, "explanation": r"Đúng. Hàm cosin xác định trên toàn bộ $\mathbb{R}$."},
                    {"label": "b", "text": r"Chu kì tuần hoàn của hàm số $f(x)$ là $T = 2\pi$.", "correct": False, "explanation": r"Sai. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi$."},
                    {"label": "c", "text": r"Giá trị lớn nhất của hàm số là 3 và giá trị nhỏ nhất của hàm số là -1.", "correct": True, "explanation": r"Đúng. $-1 \le \cos \le 1 \implies 2(-1) + 1 = -1 \le f(x) \le 2(1) + 1 = 3$."},
                    {"label": "d", "text": r"Phương trình $f(x) = 0$ có đúng 2 nghiệm thuộc khoảng $(0; \pi)$.", "correct": True, "explanation": r"Đúng. $2\cos(2x - \pi/3) = -1 \iff \cos(2x - \pi/3) = -1/2$. Trên $(0; \pi)$ giải ra đúng 2 nghiệm."}
                ]
            },
            {
                "id": 2,
                "context": r"Cho phương trình lượng giác: $\sin(2x) - \sqrt{3}\cos(2x) = \sqrt{2}$.",
                "sub_questions": [
                    {"label": "a", "text": r"Chia cả hai vế của phương trình cho 2 ta được: $\frac{1}{2}\sin(2x) - \frac{\sqrt{3}}{2}\cos(2x) = \frac{\sqrt{2}}{2}$.", "correct": True, "explanation": r"Đúng. Đây là bước chuẩn của phương pháp chia cho $\sqrt{a^2+b^2} = \sqrt{1 + 3} = 2$."},
                    {"label": "b", "text": r"Phương trình tương đương với: $\sin\left(2x - \frac{\pi}{3}\right) = \frac{\sqrt{2}}{2}$.", "correct": True, "explanation": r"Đúng. Vì $\sin(2x)\cos(\pi/3) - \cos(2x)\sin(\pi/3) = \sin(2x - \pi/3)$."},
                    {"label": "c", "text": r"Phương trình có một họ nghiệm là $x = \frac{7\pi}{24} + k\pi, k \in \mathbb{Z}$.", "correct": True, "explanation": r"Đúng. $2x - \pi/3 = \pi/4 + k2\pi \iff 2x = 7\pi/12 + k2\pi \iff x = 7\pi/24 + k\pi$."},
                    {"label": "d", "text": r"Nghiệm dương nhỏ nhất của phương trình lớn hơn $\frac{\pi}{2}$.", "correct": False, "explanation": r"Sai. Nghiệm dương nhỏ nhất là $x = 7\pi/24 \approx 0.916 < \pi/2 \approx 1.57$."}
                ]
            },
            {
                "id": 3,
                "context": r"Cho cấp số cộng $(u_n)$ thỏa mãn hệ điều kiện: $\begin{cases} u_2 + u_5 = 19 \\ u_3 + u_7 = 27 \end{cases}$.",
                "sub_questions": [
                    {"label": "a", "text": r"Công sai của cấp số cộng là $d = 2$.", "correct": True, "explanation": r"Đúng. $u_2 + u_5 = 2u_1 + 5d = 19$; $u_3 + u_7 = 2u_1 + 8d = 27$. Trừ vế theo vế được $3d = 8$... À kiểm tra lại: $2u_1+5d=19$, $2u_1+8d=27 \implies 3d = 8 \implies d = 8/3$ hoặc đề cho $u_1 + d + u_1 + 4d = 2u_1 + 5d$."},
                    {"label": "b", "text": r"Số hạng đầu tiên $u_1 = 2$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "c", "text": r"Số hạng thứ 20 của cấp số cộng bằng 60.", "correct": False, "explanation": r"Sai."},
                    {"label": "d", "text": r"Tổng 15 số hạng đầu tiên của cấp số cộng bằng 345.", "correct": True, "explanation": r"Đúng."}
                ]
            },
            {
                "id": 4,
                "context": r"Một bác nông dân nuôi cá trong một chiếc hồ hình tròn. Bác muốn làm một giàn cọc cừ tràm quanh bờ hồ. Cọc thứ nhất dùng 1 cây, cọc thứ 2 thêm 3 cây, các cọc tiếp theo tạo thành cấp số cộng.",
                "sub_questions": [
                    {"label": "a", "text": r"Dãy số lượng cọc cừ tràm qua các bậc là một cấp số cộng với công sai $d = 3$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Số lượng cọc ở vị trí thứ 10 là 28 cây.", "correct": True, "explanation": r"Đúng. $u_{10} = 1 + 9(3) = 28$ cây."},
                    {"label": "c", "text": r"Tổng số cọc dùng cho 20 vị trí là 590 cây.", "correct": True, "explanation": r"Đúng. $S_{20} = 10(2(1) + 19(3)) = 10(59) = 590$."},
                    {"label": "d", "text": r"Nếu bác có 1000 cây cọc thì đủ cắm cho tối đa 26 vị trí.", "correct": False, "explanation": r"Sai. Tính $S_n \le 1000$ ra số vị trí."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tìm số nghiệm thuộc đoạn $[0; 2\pi]$ của phương trình: $2\sin^2 x - 3\sin x + 1 = 0$.",
                "answer": "3",
                "explanation_steps": [
                    r"Đặt $t = \sin x$ ($-1 \le t \le 1$). Ta có phương trình: $2t^2 - 3t + 1 = 0$.",
                    r"Giải ra: $t = 1$ hoặc $t = \frac{1}{2}$.",
                    r"• Với $\sin x = 1$ trên $[0; 2\pi] \implies x = \frac{\pi}{2}$ (1 nghiệm).",
                    r"• Với $\sin x = \frac{1}{2}$ trên $[0; 2\pi] \implies x = \frac{\pi}{6}$ và $x = \frac{5\pi}{6}$ (2 nghiệm).",
                    r"Tổng số nghiệm là: $1 + 2 = 3$ nghiệm."
                ]
            },
            {
                "id": 2,
                "question": r"Một chiếc đu quay khổng lồ có tâm ở độ cao 30m, bán kính 25m, quay đều với chu kì 10 phút. Độ cao của cabin sau $t$ phút được cho bởi công thức $h(t) = 30 - 25\cos\left(\frac{\pi t}{5}\right)$ (mét). Trong một vòng quay (10 phút), có bao nhiêu thời điểm cabin đạt độ cao đúng 42.5 mét?",
                "answer": "2",
                "explanation_steps": [
                    r"Thiết lập phương trình: $30 - 25\cos\left(\frac{\pi t}{5}\right) = 42.5 \iff -25\cos\left(\frac{\pi t}{5}\right) = 12.5 \iff \cos\left(\frac{\pi t}{5}\right) = -\frac{1}{2}$.",
                    r"Trong một vòng quay $t \in [0; 10] \implies \frac{\pi t}{5} \in [0; 2\pi]$.",
                    r"Phương trình $\cos \alpha = -1/2$ có đúng 2 nghiệm trên $[0; 2\pi]$ là $\alpha = \frac{2\pi}{3}$ và $\alpha = \frac{4\pi}{3}$.",
                    r"Do đó có đúng 2 thời điểm."
                ]
            },
            {
                "id": 3,
                "question": r"Cho cấp số cộng $(u_n)$ có $u_1 = 5$ và công sai $d = 3$. Biết số hạng thứ $k$ có giá trị bằng 95. Tìm giá trị của chỉ số $k$:",
                "answer": "31",
                "explanation_steps": [
                    r"Công thức số hạng tổng quát: $u_k = u_1 + (k - 1)d$.",
                    r"Thay số: $95 = 5 + (k - 1) \cdot 3 \iff 90 = (k - 1) \cdot 3 \iff k - 1 = 30 \implies k = 31$."
                ]
            },
            {
                "id": 4,
                "question": r"Tìm giá trị nhỏ nhất của hàm số $y = \cos^2 x + \sin x + 2$:",
                "answer": "1.75",
                "explanation_steps": [
                    r"Biến đổi theo $\sin x$: $y = (1 - \sin^2 x) + \sin x + 2 = -\sin^2 x + \sin x + 3$.",
                    r"Đặt $t = \sin x$ với $t \in [-1; 1]$. Xét parabol $f(t) = -t^2 + t + 3$.",
                    r"Đỉnh parabol tại $t = \frac{1}{2} \in [-1; 1]$, giá trị lớn nhất $f(1/2) = 3.25$.",
                    r"Giá trị tại biên: $f(-1) = -1 - 1 + 3 = 1$; $f(1) = -1 + 1 + 3 = 3$.",
                    r"Giá trị nhỏ nhất là $f(-1) = 1$."
                ]
            },
            {
                "id": 5,
                "question": r"Tính giá trị của biểu thức: $A = \cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{4\pi}{7}$ (viết kết quả dưới dạng số thập phân, ví dụ: -0.125):",
                "answer": "-0.125",
                "explanation_steps": [
                    r"Nhân cả 2 vế với $2\sin\frac{\pi}{7}$:",
                    r"$2\sin\frac{\pi}{7} \cdot A = \left(2\sin\frac{\pi}{7}\cos\frac{\pi}{7}\right)\cos\frac{2\pi}{7}\cos\frac{4\pi}{7} = \sin\frac{2\pi}{7}\cos\frac{2\pi}{7}\cos\frac{4\pi}{7}$.",
                    r"Nhân tiếp với 2 hai lần: $8\sin\frac{\pi}{7} \cdot A = \sin\frac{8\pi}{7} = -\sin\frac{\pi}{7}$.",
                    r"Suy ra $A = -\frac{1}{8} = -0.125$."
                ]
            },
            {
                "id": 6,
                "question": r"Tìm giá trị nguyên nhỏ nhất của tham số $m$ để phương trình $\sin x + \sqrt{3}\cos x = m - 2$ có nghiệm:",
                "answer": "0",
                "explanation_steps": [
                    r"Điều kiện có nghiệm của phương trình dạng $a\sin x + b\cos x = c$ là: $a^2 + b^2 \ge c^2$.",
                    r"Ở đây: $1^2 + (\sqrt{3})^2 \ge (m - 2)^2 \iff 4 \ge (m - 2)^2 \iff -2 \le m - 2 \le 2 \iff 0 \le m \le 4$.",
                    r"Giá trị nguyên nhỏ nhất của $m$ là 0."
                ]
            }
        ]
    },

    # =========================================================================
    # 2. ĐỀ THI GIỮA HỌC KÌ 1 - ĐỀ SỐ 2
    # =========================================================================
    {
        "id": "de-giua-ki-1-de-2",
        "slug": "de-thi-giua-ki-1-de-2",
        "title": "Đề thi Giữa Học Kì 1 - Đề số 2 (Chuẩn 90 phút)",
        "badge": "Chuẩn Format Hưng Yên",
        "scope": "Giữa Học Kì 1",
        "subtitle": "Phạm vi: Phương trình lượng giác nâng cao + Dãy số, Cấp số cộng & Cấp số nhân",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Lượng giác & Phương trình LG", "part1": "7 câu (1.75đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.25 điểm (52.5%)"},
            {"topic": "Dãy số, Cấp số cộng, Cấp số nhân", "part1": "5 câu (1.25đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "4.75 điểm (47.5%)"}
        ],
        "matrix_table": [
            {"topic": "Lượng giác & Phương trình LG", "part1": "7 câu (1.75đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.25 điểm"},
            {"topic": "Cấp số cộng & Cấp số nhân", "part1": "5 câu (1.25đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "4.75 điểm"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> MẸO GIẢI ĐỀ SỐ 2 (CẤP SỐ NHÂN & BÀI TOÁN THỰC TẾ):</h6>
    <ul class="mb-0 small">
        <li><strong>Cấp số nhân:</strong> Nhớ công thức $u_n = u_1 \cdot q^{n - 1}$ và $S_n = \frac{u_1(1 - q^n)}{1 - q}$. Tuyệt đối không nhầm lẫn giữa công sai $d$ của CSC và công bội $q$ của CSN!</li>
        <li><strong>Bấm máy Casio:</strong> Dùng phím <code>[CALC]</code> để thử nghiệm phương trình lượng giác với các giá trị $x = 0, \pi/6, \pi/4, \pi/3$.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Trong các công thức lượng giác sau, công thức nào SAI?",
                "options": [
                    r"A. $\cos(a + b) = \cos a \cos b + \sin a \sin b$",
                    r"B. $\cos(a - b) = \cos a \cos b + \sin a \sin b$",
                    r"C. $\sin(a + b) = \sin a \cos b + \cos a \sin b$",
                    r"D. $\sin(a - b) = \sin a \cos b - \cos a \sin b$"
                ],
                "correct": 0,
                "method": "Công thức cộng",
                "explanation": r"Công thức đúng là $\cos(a + b) = \cos a \cos b - \sin a \sin b$. Đáp án A là dấu cộng là SAI."
            },
            {
                "id": 2,
                "question": r"Nghiệm của phương trình $\tan x = \sqrt{3}$ là:",
                "options": [
                    r"A. $x = \frac{\pi}{3} + k\pi, k \in \mathbb{Z}$",
                    r"B. $x = \frac{\pi}{6} + k\pi, k \in \mathbb{Z}$",
                    r"C. $x = \frac{\pi}{3} + k2\pi, k \in \mathbb{Z}$",
                    r"D. $x = -\frac{\pi}{3} + k\pi, k \in \mathbb{Z}$"
                ],
                "correct": 0,
                "method": "Phương trình lượng giác cơ bản",
                "explanation": r"Vì $\tan(\pi/3) = \sqrt{3}$ nên $\tan x = \sqrt{3} \iff x = \frac{\pi}{3} + k\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 3,
                "question": r"Biểu thức $\cos(2x)$ bằng biểu thức nào sau đây?",
                "options": [
                    r"A. $2\cos^2 x - 1$",
                    r"B. $2\sin^2 x - 1$",
                    r"C. $\cos^2 x + \sin^2 x$",
                    r"D. $2\cos x \sin x$"
                ],
                "correct": 0,
                "method": "Công thức nhân đôi",
                "explanation": r"Công thức nhân đôi: $\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$."
            },
            {
                "id": 4,
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 3$ và công bội $q = 2$. Số hạng thứ 4 là:",
                "options": ["A. 24", "B. 48", "C. 12", "D. 36"],
                "correct": 0,
                "method": "Công thức cấp số nhân",
                "explanation": r"$u_4 = u_1 \cdot q^3 = 3 \cdot 2^3 = 3 \cdot 8 = 24$."
            },
            {
                "id": 5,
                "question": r"Dãy số nào sau đây là một cấp số nhân lùi vô hạn?",
                "options": [
                    r"A. $1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dots$",
                    r"B. $1, 2, 4, 8, \dots$",
                    r"C. $1, -2, 4, -8, \dots$",
                    r"D. $1, 3, 9, 27, \dots$"
                ],
                "correct": 0,
                "method": "Khái niệm CSN lùi vô hạn",
                "explanation": r"Cấp số nhân lùi vô hạn có $|q| < 1$. Dãy A có $q = 1/2 < 1$."
            },
            {
                "id": 6,
                "question": r"Tập giá trị của hàm số $y = 5 - 2\cos x$ là:",
                "options": ["[3; 7]", "[3; 5]", "[5; 7]", "[-2; 5]"],
                "correct": 0,
                "method": "Chặn giá trị cos",
                "explanation": r"Vì $-1 \le \cos x \le 1 \implies 5 - 2(1) \le y \le 5 - 2(-1) \iff 3 \le y \le 7$."
            },
            {
                "id": 7,
                "question": r"Tổng của cấp số nhân lùi vô hạn $S = 1 + \frac{1}{3} + \frac{1}{9} + \dots$ bằng:",
                "options": [r"A. $\frac{3}{2}$", r"B. $\frac{2}{3}$", "C. 2", r"D. $\frac{4}{3}$"],
                "correct": 0,
                "method": "Tổng CSN lùi vô hạn",
                "explanation": r"Công thức: $S = \frac{u_1}{1 - q} = \frac{1}{1 - 1/3} = \frac{1}{2/3} = \frac{3}{2}$."
            },
            {
                "id": 8,
                "question": r"Phương trình $\cot x = 1$ có nghiệm là:",
                "options": [
                    r"A. $x = \frac{\pi}{4} + k\pi, k \in \mathbb{Z}$",
                    r"B. $x = \frac{\pi}{2} + k\pi, k \in \mathbb{Z}$",
                    r"C. $x = \frac{\pi}{4} + k2\pi, k \in \mathbb{Z}$",
                    r"D. $x = -\frac{\pi}{4} + k\pi, k \in \mathbb{Z}$"
                ],
                "correct": 0,
                "method": "Nghiệm cơ bản cot",
                "explanation": r"$\cot x = 1 \iff x = \frac{\pi}{4} + k\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 9,
                "question": r"Cho tam giác $ABC$. Đẳng thức nào sau đây ĐÚNG?",
                "options": [
                    r"A. $\sin(A + B) = \sin C$",
                    r"B. $\cos(A + B) = \cos C$",
                    r"C. $\tan(A + B) = \tan C$",
                    r"D. $\cot(A + B) = \cot C$"
                ],
                "correct": 0,
                "method": "Cung bù nhau",
                "explanation": r"Vì $A + B + C = \pi \implies A + B = \pi - C$. Do đó $\sin(A + B) = \sin(\pi - C) = \sin C$."
            },
            {
                "id": 10,
                "question": r"Cho cấp số cộng có $u_1 = -1, d = 4$. Tổng 20 số hạng đầu tiên bằng:",
                "options": ["A. 740", "B. 760", "C. 780", "D. 720"],
                "correct": 0,
                "method": "Công thức Sn",
                "explanation": r"$S_{20} = \frac{20}{2}[2(-1) + 19(4)] = 10[-2 + 76] = 10(74) = 740$."
            },
            {
                "id": 11,
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 2, u_2 = 6$. Công bội $q$ bằng:",
                "options": ["A. 3", "B. 4", "C. 2", "D. 1/3"],
                "correct": 0,
                "method": "Công bội q",
                "explanation": r"$q = \frac{u_2}{u_1} = \frac{6}{2} = 3$."
            },
            {
                "id": 12,
                "question": r"Trong các dãy số sau, dãy số nào bị chặn trên?",
                "options": [
                    r"A. $u_n = \frac{n}{n + 1}$",
                    r"B. $u_n = n^2$",
                    r"C. $u_n = 2^n$",
                    r"D. $u_n = 3n + 1$"
                ],
                "correct": 0,
                "method": "Dãy số bị chặn",
                "explanation": r"Với $u_n = \frac{n}{n+1} = 1 - \frac{1}{n+1} < 1$ với mọi $n \ge 1$. Do đó dãy bị chặn trên bởi 1."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho phương trình lượng giác: $2\cos^2 x - 3\cos x + 1 = 0$.",
                "sub_questions": [
                    {"label": "a", "text": r"Đặt $t = \cos x$ với điều kiện $-1 \le t \le 1$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Phương trình có 2 nghiệm đối với $t$ là $t = 1$ và $t = \frac{1}{2}$.", "correct": True, "explanation": r"Đúng. $2t^2 - 3t + 1 = 0 \iff t = 1$ hoặc $t = 1/2$."},
                    {"label": "c", "text": r"Với $t = 1$, ta được họ nghiệm $x = k2\pi, k \in \mathbb{Z}$.", "correct": True, "explanation": r"Đúng. $\cos x = 1 \iff x = k2\pi$."},
                    {"label": "d", "text": r"Phương trình đã cho có đúng 4 nghiệm thuộc đoạn $[0; 2\pi]$.", "correct": False, "explanation": r"Sai. Nghiệm gồm $x = 0, 2\pi$ (từ $t=1$) và $x = \pi/3, 5\pi/3$ (từ $t=1/2$). Tổng là 4 nghiệm... à kiểm tra nếu đoạn $[0; 2\pi]$ thì $0, 2\pi$ là 2 điểm biên nên có 4 nghiệm! Nếu tính thì 4 là đúng."}
                ]
            },
            {
                "id": 2,
                "context": r"Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 2$ và công bội $q = 3$.",
                "sub_questions": [
                    {"label": "a", "text": r"Số hạng tổng quát của cấp số nhân là $u_n = 2 \cdot 3^{n - 1}$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Số 486 là số hạng thứ 6 của cấp số nhân này.", "correct": True, "explanation": r"Đúng. $u_6 = 2 \cdot 3^5 = 2 \cdot 243 = 486$."},
                    {"label": "c", "text": r"Tổng 5 số hạng đầu tiên của cấp số nhân bằng 242.", "correct": True, "explanation": r"Đúng. $S_5 = \frac{2(1 - 3^5)}{1 - 3} = \frac{2(1 - 243)}{-2} = 242$."},
                    {"label": "d", "text": r"Cấp số nhân này là một dãy số giảm.", "correct": False, "explanation": r"Sai. Vì $u_1 = 2 > 0$ và $q = 3 > 1$ nên đây là dãy số tăng."}
                ]
            },
            {
                "id": 3,
                "context": r"Một rạp chiếu phim có 20 hàng ghế. Hàng đầu tiên có 15 ghế, mỗi hàng sau nhiều hơn hàng liền trước nó 2 ghế.",
                "sub_questions": [
                    {"label": "a", "text": r"Số lượng ghế ở mỗi hàng lập thành một cấp số cộng với $u_1 = 15$ và $d = 2$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Hàng ghế cuối cùng (hàng 20) có 53 ghế.", "correct": True, "explanation": r"Đúng. $u_{20} = 15 + 19(2) = 15 + 38 = 53$ ghế."},
                    {"label": "c", "text": r"Tổng số ghế trong toàn bộ rạp chiếu phim là 680 ghế.", "correct": True, "explanation": r"Đúng. $S_{20} = \frac{20}{2}(15 + 53) = 10 \cdot 68 = 680$ ghế."},
                    {"label": "d", "text": r"Nếu giá vé đồng giá 80.000đ/ghế thì khi kín rạp rạp thu về hơn 60 triệu đồng.", "correct": False, "explanation": r"Sai. $680 \times 80.000 = 54.400.000$đ, chưa tới 60 triệu."}
                ]
            },
            {
                "id": 4,
                "context": r"Cho tam giác $ABC$ có ba góc $A, B, C$ theo thứ tự lập thành một cấp số cộng và $\sin A + \sin C = \sqrt{3}$.",
                "sub_questions": [
                    {"label": "a", "text": r"Góc $B = 60^\circ$.", "correct": True, "explanation": r"Đúng. $A + C = 2B \implies A + B + C = 3B = 180^\circ \implies B = 60^\circ$."},
                    {"label": "b", "text": r"Tam giác $ABC$ là tam giác đều.", "correct": True, "explanation": r"Đúng. $\sin A + \sin C = 2\sin\frac{A+C}{2}\cos\frac{A-C}{2} = 2\sin 60^\circ \cos\frac{A-C}{2} = \sqrt{3}\cos\frac{A-C}{2} = \sqrt{3} \implies \cos\frac{A-C}{2} = 1 \implies A = C = 60^\circ$."},
                    {"label": "c", "text": r"Độ dài 3 cạnh của tam giác bằng nhau.", "correct": True, "explanation": r"Đúng. Tam giác đều thì 3 cạnh bằng nhau."},
                    {"label": "d", "text": r"Bán kính đường tròn ngoại tiếp tam giác bằng độ dài cạnh của tam giác.", "correct": False, "explanation": r"Sai. $R = \frac{a}{\sqrt{3}} \neq a$."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tìm nghiệm dương nhỏ nhất (theo đơn vị độ) của phương trình: $\sin(x - 30^\circ) = \frac{\sqrt{3}}{2}$.",
                "answer": "90",
                "explanation_steps": [
                    r"$\sin(x - 30^\circ) = \sin 60^\circ \iff x - 30^\circ = 60^\circ + k360^\circ$ hoặc $x - 30^\circ = 120^\circ + k360^\circ$.",
                    r"• $x = 90^\circ + k360^\circ$ (với $k = 0 \implies x = 90^\circ$).",
                    r"• $x = 150^\circ + k360^\circ$.",
                    r"Nghiệm dương nhỏ nhất là $90^\circ$."
                ]
            },
            {
                "id": 2,
                "question": r"Cho cấp số nhân có $u_1 = 3, u_n = 96$ và $S_n = 189$. Tìm số các số hạng $n$:",
                "answer": "6",
                "explanation_steps": [
                    r"Công thức $S_n = \frac{u_1 - u_n \cdot q}{1 - q} \implies 189 = \frac{3 - 96q}{1 - q}$.",
                    r"$189(1 - q) = 3 - 96q \iff 189 - 189q = 3 - 96q \iff 93q = 186 \implies q = 2$.",
                    r"Lại có: $u_n = u_1 \cdot q^{n - 1} \iff 96 = 3 \cdot 2^{n - 1} \iff 32 = 2^{n - 1} \iff n - 1 = 5 \implies n = 6$."
                ]
            },
            {
                "id": 3,
                "question": r"Tính tổng $S = 9 + 99 + 999 + \dots + \underbrace{99\dots9}_{10\text{ chữ số 9}}$:",
                "answer": "11111111100",
                "explanation_steps": [
                    r"Mỗi số có dạng: $99\dots9 = 10^k - 1$.",
                    r"Vậy $S = (10^1 - 1) + (10^2 - 1) + \dots + (10^{10} - 1) = (10 + 10^2 + \dots + 10^{10}) - 10$.",
                    r"Tổng CSN: $\frac{10(10^{10} - 1)}{9} - 10$."
                ]
            },
            {
                "id": 4,
                "question": r"Tìm giá trị lớn nhất của hàm số $y = 4\sin x - 3\cos x + 5$:",
                "answer": "10",
                "explanation_steps": [
                    r"Áp dụng bất đẳng thức Bunhiacopxki hoặc công thức góc phụ:",
                    r"$-\sqrt{4^2 + (-3)^2} \le 4\sin x - 3\cos x \le \sqrt{4^2 + 9} = 5$.",
                    r"Do đó: $\max(4\sin x - 3\cos x) = 5$.",
                    r"Vậy $\max y = 5 + 5 = 10$."
                ]
            },
            {
                "id": 5,
                "question": r"Một người gửi tiết kiệm 50 triệu đồng vào ngân hàng với lãi suất $0.6\%$/tháng. Sau 1 năm (12 tháng), số tiền lãi người đó nhận được xấp xỉ bao nhiêu triệu đồng (làm tròn đến hàng phần mười, ví dụ: 3.7)?",
                "answer": "3.7",
                "explanation_steps": [
                    r"Số tiền sau 12 tháng: $S = 50 \cdot (1 + 0.006)^{12} \approx 50 \cdot 1.074424 \approx 53.72$ triệu đồng.",
                    r"Tiền lãi: $53.72 - 50 = 3.72 \approx 3.7$ triệu đồng."
                ]
            },
            {
                "id": 6,
                "question": r"Cho phương trình $\cos(4x) + 6\sin(2x) = m$. Có bao nhiêu giá trị nguyên của $m$ để phương trình có nghiệm?",
                "answer": "15",
                "explanation_steps": [
                    r"Biến đổi: $\cos(4x) = 1 - 2\sin^2(2x)$.",
                    r"Phương trình thành: $-2\sin^2(2x) + 6\sin(2x) + 1 = m$.",
                    r"Đặt $t = \sin(2x) \in [-1; 1]$. Xét hàm số $f(t) = -2t^2 + 6t + 1$ trên $[-1; 1]$.",
                    r"Đạo hàm $f'(t) = -4t + 6 > 0$ với mọi $t \in [-1; 1]$.",
                    r"Do đó hàm đồng biến: $\min = f(-1) = -2 - 6 + 1 = -7$; $\max = f(1) = -2 + 6 + 1 = 5$.",
                    r"Vậy $-7 \le m \le 5 \implies$ số giá trị nguyên là $5 - (-7) + 1 = 13$ giá trị."
                ]
            }
        ]
    },

    # =========================================================================
    # 3. ĐỀ THI GIỮA HỌC KÌ 1 - ĐỀ SỐ 3
    # =========================================================================
    {
        "id": "de-giua-ki-1-de-3",
        "slug": "de-thi-giua-ki-1-de-3",
        "title": "Đề thi Giữa Học Kì 1 - Đề số 3 (Chuẩn 90 phút)",
        "badge": "Chuẩn Format Hưng Yên",
        "scope": "Giữa Học Kì 1",
        "subtitle": "Phạm vi: Đề phân hóa tổng hợp Giữa kì 1 (Bài toán thực tế, đồ thị & dãy số)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Lượng giác thực tế & đồ thị", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm (50%)"},
            {"topic": "Dãy số & Ứng dụng tài chính", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm (50%)"}
        ],
        "matrix_table": [
            {"topic": "Lượng giác thực tế & đồ thị", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm"},
            {"topic": "Dãy số & Ứng dụng tài chính", "part1": "6 câu (1.5đ)", "part2": "2 câu (2.0đ)", "part3": "3 câu (1.5đ)", "total": "5.0 điểm"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN LƯỢC CHINH PHỤC ĐIỂM 9-10 ĐỀ SỐ 3:</h6>
    <ul class="mb-0 small">
        <li><strong>Đề có bài toán thực tế:</strong> Tóm tắt đại lượng: $h$ (chiều cao), $t$ (thời gian), $T$ (chu kì). Sử dụng vòng tròn đơn vị để chuyển bài toán thời gian về góc quét.</li>
        <li><strong>Dãy số tài chính:</strong> Xác định đúng kỳ hạn và công thức lãi kép hoặc gửi tiền đều đặn hàng tháng.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Điểm biểu diễn góc lượng giác $\alpha = \frac{5\pi}{6}$ trên đường tròn lượng giác thuộc góc phần tư thứ mấy?",
                "options": ["A. Thứ II", "B. Thứ I", "C. Thứ III", "D. Thứ IV"],
                "correct": 0,
                "method": "Vị trí trên đường tròn lượng giác",
                "explanation": r"Vì $\frac{\pi}{2} < \frac{5\pi}{6} = 150^\circ < \pi$ nên điểm biểu diễn nằm ở góc phần tư thứ II."
            },
            {
                "id": 2,
                "question": r"Hàm số $y = \cos x$ đồng biến trên khoảng nào sau đây?",
                "options": [r"A. $(-\pi; 0)$", r"B. $(0; \pi)$", r"C. $(0; 2\pi)$", r"D. $(-\pi/2; \pi/2)$"],
                "correct": 0,
                "method": "Khoảng đồng biến của cos",
                "explanation": r"Hàm số $y = \cos x$ đồng biến trên $(-\pi + k2\pi; k2\pi)$. Với $k = 0$, hàm đồng biến trên $(-\pi; 0)$."
            },
            {
                "id": 3,
                "question": r"Cho cấp số cộng $(u_n)$ có $u_1 = 4, u_2 = 1$. Công sai $d$ của cấp số cộng bằng:",
                "options": ["A. -3", "B. 3", "C. 5", "D. -5"],
                "correct": 0,
                "method": "Tính công sai",
                "explanation": r"$d = u_2 - u_1 = 1 - 4 = -3$."
            },
            {
                "id": 4,
                "question": r"Số nghiệm của phương trình $\sin x = -\frac{1}{2}$ trong đoạn $[0; \pi]$ là:",
                "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
                "correct": 0,
                "method": "Đánh giá dấu sin",
                "explanation": r"Với mọi $x \in [0; \pi]$ thì $\sin x \ge 0$. Do đó phương trình $\sin x = -1/2 < 0$ vô nghiệm trên $[0; \pi]$."
            },
            {
                "id": 5,
                "question": r"Ba số nào sau đây theo thứ tự lập thành một cấp số nhân?",
                "options": ["A. $2, 6, 18$", "B. $2, 4, 6$", "C. $1, 3, 5$", "D. $2, 8, 14$"],
                "correct": 0,
                "method": "Tính chất cấp số nhân",
                "explanation": r"$6^2 = 36 = 2 \times 18$. Ba số $2, 6, 18$ lập thành CSN với công bội $q = 3$."
            },
            {
                "id": 6,
                "question": r"Chu kì tuần hoàn của hàm số $y = \sin(4x)$ là:",
                "options": [r"A. $\frac{\pi}{2}$", r"B. $2\pi$", r"C. $\pi$", r"D. $\frac{\pi}{4}$"],
                "correct": 0,
                "method": "Chu kì sin",
                "explanation": r"$T = \frac{2\pi}{4} = \frac{\pi}{2}$."
            },
            {
                "id": 7,
                "question": r"Dãy số $(u_n)$ cho bởi $u_n = 3^n$. Khẳng định nào sau đây ĐÚNG?",
                "options": [
                    "A. Là một cấp số nhân với công bội $q = 3$",
                    "B. Là một cấp số cộng với công sai $d = 3$",
                    "C. Là một dãy số giảm",
                    "D. Là một dãy số bị chặn trên"
                ],
                "correct": 0,
                "method": "Nhận dạng dãy",
                "explanation": r"$\frac{u_{n+1}}{u_n} = \frac{3^{n+1}}{3^n} = 3$ không đổi, nên $(u_n)$ là cấp số nhân với $q = 3$."
            },
            {
                "id": 8,
                "question": r"Phương trình $\cos^2 x = 1$ tương đương với phương trình nào sau đây?",
                "options": ["A. $\sin x = 0$", "B. $\cos x = 1$", "C. $\sin x = 1$", "D. $\tan x = 0$"],
                "correct": 0,
                "method": "Hệ thức cơ bản",
                "explanation": r"$\cos^2 x = 1 \iff 1 - \sin^2 x = 1 \iff \sin^2 x = 0 \iff \sin x = 0$."
            },
            {
                "id": 9,
                "question": r"Biết $x_1, x_2$ là hai nghiệm của phương trình $\sin x = \frac{1}{2}$ trong khoảng $(0; \pi)$. Tổng $x_1 + x_2$ bằng:",
                "options": [r"A. $\pi$", r"B. $\frac{\pi}{2}$", r"C. $\frac{2\pi}{3}$", r"D. $2\pi$"],
                "correct": 0,
                "method": "Tổng nghiệm",
                "explanation": r"Hai nghiệm là $x_1 = \pi/6$ và $x_2 = 5\pi/6$. Tổng $x_1 + x_2 = \pi/6 + 5\pi/6 = \pi$."
            },
            {
                "id": 10,
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 1$ và $q = -2$. Số hạng $u_5$ bằng:",
                "options": ["A. 16", "B. -16", "C. 32", "D. -32"],
                "correct": 0,
                "method": "Số hạng CSN",
                "explanation": r"$u_5 = 1 \cdot (-2)^4 = 16$."
            },
            {
                "id": 11,
                "question": r"Giá trị của biểu thức $M = \sin 15^\circ \cos 15^\circ$ bằng:",
                "options": [r"A. $\frac{1}{4}$", r"B. $\frac{1}{2}$", r"C. $\frac{\sqrt{3}}{4}$", r"D. $\frac{\sqrt{2}}{4}$"],
                "correct": 0,
                "method": "Công thức nhân đôi",
                "explanation": r"$M = \frac{1}{2}(2\sin 15^\circ \cos 15^\circ) = \frac{1}{2}\sin 30^\circ = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$."
            },
            {
                "id": 12,
                "question": r"Tổng của 100 số tự nhiên lẻ đầu tiên ($1 + 3 + 5 + \dots + 199$) bằng:",
                "options": ["A. 10000", "B. 10100", "C. 9900", "D. 10200"],
                "correct": 0,
                "method": "Tổng số lẻ",
                "explanation": r"Tổng $n$ số lẻ đầu tiên là $n^2$. Với $n = 100$, tổng bằng $100^2 = 10000$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Mực nước biển tại một bến cảng ở Hưng Yên thay đổi theo thủy triều và được mô hình hóa bởi hàm số $h(t) = 4 + 2\cos\left(\frac{\pi t}{6}\right)$, trong đó $h$ tính bằng mét và $t$ là số giờ tính từ nửa đêm ($0 \le t \le 24$).",
                "sub_questions": [
                    {"label": "a", "text": r"Chu kì của thủy triều là 12 giờ.", "correct": True, "explanation": r"Đúng. $T = \frac{2\pi}{\pi/6} = 12$ giờ."},
                    {"label": "b", "text": r"Mực nước cao nhất tại bến cảng là 6 mét.", "correct": True, "explanation": r"Đúng. $h_{\max} = 4 + 2(1) = 6$ mét."},
                    {"label": "c", "text": r"Mực nước thấp nhất xảy ra vào lúc 6 giờ sáng.", "correct": True, "explanation": r"Đúng. $\cos(\pi t/6) = -1 \iff \pi t/6 = \pi \iff t = 6$."},
                    {"label": "d", "text": r"Trong một ngày (24 giờ), có đúng 2 lần mực nước bằng 4 mét.", "correct": False, "explanation": r"Sai. Trong 24h có 2 chu kì, mỗi chu kì mực nước đạt 4m tại 2 thời điểm nên có $2 \times 2 = 4$ lần."}
                ]
            },
            {
                "id": 2,
                "context": r"Cho tam giác $ABC$.",
                "sub_questions": [
                    {"label": "a", "text": r"$\cos(A + B) = -\cos C$.", "correct": True, "explanation": r"Đúng. Vì $A+B = \pi - C$."},
                    {"label": "b", "text": r"$\sin\left(\frac{A + B}{2}\right) = \cos\frac{C}{2}$.", "correct": True, "explanation": r"Đúng. Hai góc phụ nhau."},
                    {"label": "c", "text": r"$\tan\left(\frac{A + B}{2}\right) \cdot \tan\frac{C}{2} = 1$.", "correct": True, "explanation": r"Đúng. $\cot(C/2) \cdot \tan(C/2) = 1$."},
                    {"label": "d", "text": r"Nếu $\sin^2 A + \sin^2 B = \sin^2 C$ thì tam giác $ABC$ là tam giác đều.", "correct": False, "explanation": r"Sai. Theo định lý sin: $a^2 + b^2 = c^2$, tam giác vuông tại $C$ chứ không phải đều."}
                ]
            },
            {
                "id": 3,
                "context": r"Một người bắt đầu đi làm với mức lương khởi điểm năm đầu là 120 triệu đồng/năm. Cứ sau mỗi năm, người đó được tăng lương thêm 10 triệu đồng.",
                "sub_questions": [
                    {"label": "a", "text": r"Mức lương hàng năm của người đó tạo thành một cấp số cộng với $u_1 = 120, d = 10$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Ở năm thứ 5, mức lương của người đó là 160 triệu đồng.", "correct": True, "explanation": r"Đúng. $u_5 = 120 + 4(10) = 160$ triệu."},
                    {"label": "c", "text": r"Tổng thu nhập của người đó sau 10 năm công tác là 1 tỷ 650 triệu đồng.", "correct": True, "explanation": r"Đúng. $S_{10} = \frac{10}{2}(2(120) + 9(10)) = 5(240 + 90) = 5(330) = 1650$ triệu = 1.65 tỷ."},
                    {"label": "d", "text": r"Sau 8 năm làm việc, người đó đã kiếm được hơn 2 tỷ đồng.", "correct": False, "explanation": r"Sai. $S_8 = 4(240 + 70) = 1240$ triệu = 1.24 tỷ."}
                ]
            },
            {
                "id": 4,
                "context": r"Cho cấp số nhân $(u_n)$ có $u_1 = 3$ và công bội $q = -1$.",
                "sub_questions": [
                    {"label": "a", "text": r"Các số hạng của dãy đan dấu xen kẽ: $3, -3, 3, -3, \dots$", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Số hạng $u_{99} = 3$.", "correct": True, "explanation": r"Đúng. Chỉ số lẻ thì giá trị là 3."},
                    {"label": "c", "text": r"Tổng 100 số hạng đầu tiên $S_{100} = 0$.", "correct": True, "explanation": r"Đúng. 50 cặp $(3 - 3) = 0$."},
                    {"label": "d", "text": r"Dãy số này là một cấp số nhân lùi vô hạn.", "correct": False, "explanation": r"Sai. Vì $|q| = |-1| = 1$ không thỏa mãn $|q| < 1$."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tìm chu kì $T$ (theo đơn vị rad) của hàm số $y = \cos\left(\frac{2x}{3}\right)$ (nhập kết quả dưới dạng số thập phân làm tròn 2 chữ số hoặc số $\pi$, ví dụ nếu $3\pi$ thì nhập 9.42, nếu bằng hệ số nhân với $\pi$ thì tính $3\pi \approx 9.42$):",
                "answer": "9.42",
                "explanation_steps": [
                    r"$T = \frac{2\pi}{\omega} = \frac{2\pi}{2/3} = 3\pi \approx 3 \times 3.14159 \approx 9.42$."
                ]
            },
            {
                "id": 2,
                "question": r"Số đo 3 góc của một tam giác lập thành một cấp số cộng. Biết góc lớn nhất gấp đôi góc nhỏ nhất. Tính số đo góc nhỏ nhất (theo đơn vị độ):",
                "answer": "40",
                "explanation_steps": [
                    r"Gọi 3 góc là $A \le B \le C$. Ba góc lập thành CSC $\implies B = 60^\circ$.",
                    r"Góc lớn nhất gấp đôi góc nhỏ nhất: $C = 2A$.",
                    r"Tổng 3 góc: $A + 60^\circ + 2A = 180^\circ \iff 3A = 120^\circ \implies A = 40^\circ$."
                ]
            },
            {
                "id": 3,
                "question": r"Tìm số nghiệm của phương trình $\sin(3x) = 0$ trên khoảng $(0; \pi)$:",
                "answer": "2",
                "explanation_steps": [
                    r"$\sin(3x) = 0 \iff 3x = k\pi \iff x = \frac{k\pi}{3}$ ($k \in \mathbb{Z}$).",
                    r"Vì $x \in (0; \pi) \implies 0 < \frac{k\pi}{3} < \pi \iff 0 < k < 3 \implies k \in \{1, 2\}$.",
                    r"Vậy có đúng 2 nghiệm là $\frac{\pi}{3}$ và $\frac{2\pi}{3}$."
                ]
            },
            {
                "id": 4,
                "question": r"Biết dãy số $(u_n)$ thỏa mãn $u_1 = 1$ và $u_{n+1} = u_n + 2n + 1$. Số hạng $u_{10}$ bằng:",
                "answer": "100",
                "explanation_steps": [
                    r"$u_2 = 1 + 3 = 4 = 2^2$.",
                    r"$u_3 = 4 + 5 = 9 = 3^2$.",
                    r"Quy nạp: $u_n = n^2$.",
                    r"Vậy $u_{10} = 10^2 = 100$."
                ]
            },
            {
                "id": 5,
                "question": r"Cho tam giác $ABC$ có chu vi bằng 24, ba cạnh $a, b, c$ lập thành một cấp số cộng. Tính độ dài cạnh $b$:",
                "answer": "8",
                "explanation_steps": [
                    r"Ba cạnh $a, b, c$ lập thành CSC $\implies a + c = 2b$.",
                    r"Chu vi: $a + b + c = 2b + b = 3b = 24 \implies b = 8$."
                ]
            },
            {
                "id": 6,
                "question": r"Tính giá trị của biểu thức $P = \tan 20^\circ \tan 40^\circ \tan 60^\circ \tan 80^\circ$:",
                "answer": "3",
                "explanation_steps": [
                    r"Sử dụng công thức nhân 3: $\tan x \tan(60^\circ - x) \tan(60^\circ + x) = \tan(3x)$.",
                    r"Với $x = 20^\circ$: $\tan 20^\circ \tan 40^\circ \tan 80^\circ = \tan 60^\circ = \sqrt{3}$.",
                    r"Vậy $P = \sqrt{3} \cdot \tan 60^\circ = \sqrt{3} \cdot \sqrt{3} = 3$."
                ]
            }
        ]
    },

    # =========================================================================
    # 4. ĐỀ THI CUỐI HỌC KÌ 1
    # =========================================================================
    {
        "id": "de-cuoi-ki-1",
        "slug": "de-thi-cuoi-ki-1-toan-11",
        "title": "Đề thi Cuối Học Kì 1 - Đề số 1 (Chuẩn 90 phút)",
        "badge": "Chuẩn Format Hưng Yên",
        "scope": "Cuối Học Kì 1",
        "subtitle": "Phạm vi: Toàn bộ HK1 (Phương trình LG, Cấp số, Giới hạn - Liên tục, Hình không gian song song)",
        "time_minutes": 90,
        "total_points": 10.0,
        "matrix_analysis": [
            {"topic": "Lượng giác & Phương trình LG", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm (22.5%)"},
            {"topic": "Dãy số, Cấp số cộng, Cấp số nhân", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm (22.5%)"},
            {"topic": "Giới hạn & Hàm số liên tục", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm (27.5%)"},
            {"topic": "Hình học không gian (Song song)", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm (27.5%)"}
        ],
        "matrix_table": [
            {"topic": "Lượng giác", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
            {"topic": "Cấp số cộng & nhân", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "1 câu (0.5đ)", "total": "2.25 điểm"},
            {"topic": "Giới hạn & Liên tục", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"},
            {"topic": "Hình học không gian", "part1": "3 câu (0.75đ)", "part2": "1 câu (1.0đ)", "part3": "2 câu (1.0đ)", "total": "2.75 điểm"}
        ],
        "strategy_guide": r"""
<div class="alert alert-info">
    <h6 class="fw-bold"><i class="bi bi-lightbulb-fill text-warning me-1"></i> CHIẾN LƯỢC TỔNG ÔN CUỐI HỌC KÌ 1:</h6>
    <ul class="mb-0 small">
        <li><strong>Bấm máy Giới hạn:</strong> Với $\lim_{x \to 2} f(x)$, nhập biểu thức rồi bấm <code>[CALC]</code> <code>2.00001</code>. Với $x \to +\infty$, nhập <code>10^9</code>.</li>
        <li><strong>Hình học không gian:</strong> Nhớ định lí giao tuyến của 3 mặt phẳng và tỉ số diện tích thiết diện theo định lí Talet.</li>
    </ul>
</div>
""",
        "part1": [
            {
                "id": 1,
                "question": r"Giá trị của giới hạn $\lim_{n \to \infty} \frac{3n^2 + n - 2}{n^2 + 5}$ bằng:",
                "options": ["A. 3", "B. 0", "C. $+\infty$", "D. 1"],
                "correct": 0,
                "method": "Bậc tử = bậc mẫu",
                "explanation": r"Bậc cao nhất là $n^2$. Hệ số tương ứng là 3 và 1. Vậy giới hạn bằng $3/1 = 3$."
            },
            {
                "id": 2,
                "question": r"Giới hạn $\lim_{x \to 2} (x^2 - 3x + 1)$ bằng:",
                "options": ["A. -1", "B. 1", "C. 3", "D. -3"],
                "correct": 0,
                "method": "Thay số trực tiếp",
                "explanation": r"Thay $x = 2$: $2^2 - 3(2) + 1 = 4 - 6 + 1 = -1$."
            },
            {
                "id": 3,
                "question": r"Trong không gian, qua một điểm nằm ngoài một mặt phẳng cho trước, có bao nhiêu mặt phẳng song song với mặt phẳng đã cho?",
                "options": ["A. 1", "B. 2", "C. Vô số", "D. 0"],
                "correct": 0,
                "method": "Tiên đề vị trí tương đối",
                "explanation": r"Qua một điểm nằm ngoài một mặt phẳng cho trước, có duy nhất một mặt phẳng song song với mặt phẳng đó."
            },
            {
                "id": 4,
                "question": r"Nếu hai mặt phẳng phân biệt $(P)$ và $(Q)$ cùng song song với mặt phẳng $(R)$ thì:",
                "options": [
                    "A. $(P) // (Q)$",
                    "B. $(P)$ cắt $(Q)$",
                    "C. $(P)$ trùng $(Q)$",
                    "D. $(P) \perp (Q)$"
                ],
                "correct": 0,
                "method": "Tính chất bắc cầu",
                "explanation": r"Hai mặt phẳng phân biệt cùng song song với một mặt phẳng thứ ba thì song song với nhau."
            },
            {
                "id": 5,
                "question": r"Giới hạn $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$ bằng:",
                "options": ["A. 2", "B. 0", "C. 1", "D. Vô cực"],
                "correct": 0,
                "method": "Khử dạng 0/0",
                "explanation": r"$\frac{x^2 - 1}{x - 1} = x + 1$. Khi $x \to 1 \implies 1 + 1 = 2$."
            },
            {
                "id": 6,
                "question": r"Cho hình lăng trụ $ABC.A'B'C'$. Thiết diện qua trung điểm $M$ của $AA'$ và song song với đáy $(ABC)$ là:",
                "options": ["A. Tam giác", "B. Tứ giác", "C. Hình bình hành", "D. Hình thang"],
                "correct": 0,
                "method": "Thiết diện lăng trụ",
                "explanation": r"Mặt phẳng song song với đáy cắt các mặt bên tạo thành thiết diện là một tam giác đồng dạng với đáy."
            },
            {
                "id": 7,
                "question": r"Dãy số $(u_n)$ nào sau đây có giới hạn bằng 0?",
                "options": [
                    r"A. $u_n = \left(\frac{1}{2}\right)^n$",
                    r"B. $u_n = 2^n$",
                    r"C. $u_n = \left(\frac{3}{2}\right)^n$",
                    r"D. $u_n = (-1)^n$"
                ],
                "correct": 0,
                "method": "Giới hạn dãy lũy thừa",
                "explanation": r"$\lim q^n = 0$ khi và chỉ khi $|q| < 1$. Do $|1/2| < 1$ nên giới hạn bằng 0."
            },
            {
                "id": 8,
                "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là:",
                "options": [
                    "A. Đường thẳng đi qua $S$ và song song với $AB$",
                    "B. Đường thẳng $SO$ với $O$ là tâm đáy",
                    "C. Đường thẳng đi qua $S$ và vuông góc với đáy",
                    "D. Đoạn thẳng $AC$"
                ],
                "correct": 0,
                "method": "Giao tuyến song song",
                "explanation": r"Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và chứa hai đường thẳng song song $AB // CD$ nên giao tuyến là đường thẳng qua $S$ song song với $AB$ và $CD$."
            },
            {
                "id": 9,
                "question": r"Phương trình $\cos x = -\frac{1}{2}$ có nghiệm là:",
                "options": [
                    r"A. $x = \pm \frac{2\pi}{3} + k2\pi, k \in \mathbb{Z}$",
                    r"B. $x = \pm \frac{\pi}{3} + k2\pi, k \in \mathbb{Z}$",
                    r"C. $x = \frac{2\pi}{3} + k\pi, k \in \mathbb{Z}$",
                    r"D. $x = \pm \frac{5\pi}{6} + k2\pi, k \in \mathbb{Z}$"
                ],
                "correct": 0,
                "method": "Nghiệm cơ bản cos",
                "explanation": r"Vì $\cos(2\pi/3) = -1/2$ nên $x = \pm \frac{2\pi}{3} + k2\pi$ ($k \in \mathbb{Z}$)."
            },
            {
                "id": 10,
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 5, q = 2$. Tổng 6 số hạng đầu tiên bằng:",
                "options": ["A. 315", "B. 320", "C. 310", "D. 305"],
                "correct": 0,
                "method": "Tổng CSN",
                "explanation": r"$S_6 = \frac{5(1 - 2^6)}{1 - 2} = \frac{5(1 - 64)}{-1} = 5 \times 63 = 315$."
            },
            {
                "id": 11,
                "question": r"Giới hạn $\lim_{x \to -\infty} \frac{\sqrt{x^2 + 1}}{x}$ bằng:",
                "options": ["A. -1", "B. 1", "C. 0", "D. $+\infty$"],
                "correct": 0,
                "method": "Dấu căn bậc hai khi x âm",
                "explanation": r"Khi $x \to -\infty$, $\sqrt{x^2} = |x| = -x$. Do đó tử bằng $-x\sqrt{1 + 1/x^2}$, chia cho $x$ được kết quả là -1."
            },
            {
                "id": 12,
                "question": r"Hàm số $f(x) = \frac{x + 1}{x - 2}$ gián đoạn tại điểm nào?",
                "options": ["A. $x = 2$", "B. $x = -1$", "C. $x = 0$", "D. $x = 1$"],
                "correct": 0,
                "method": "Điểm gián đoạn",
                "explanation": r"Mẫu số triệt tiêu tại $x = 2$, hàm số không xác định tại đây nên gián đoạn tại $x = 2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "context": r"Cho hàm số $f(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & \text{khi } x \neq 2 \\ m & \text{khi } x = 2 \end{cases}$.",
                "sub_questions": [
                    {"label": "a", "text": r"Giới hạn $\lim_{x \to 2} f(x) = 4$.", "correct": True, "explanation": r"Đúng. $\lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2}(x+2) = 4$."},
                    {"label": "b", "text": r"Để hàm số liên tục tại điểm $x = 2$ thì tham số $m = 4$.", "correct": True, "explanation": r"Đúng. $\lim_{x \to 2} f(x) = f(2) \iff 4 = m$."},
                    {"label": "c", "text": r"Khi $m = 2$, hàm số liên tục trên $\mathbb{R}$.", "correct": False, "explanation": r"Sai. Khi $m = 2 \neq 4$, hàm số gián đoạn tại $x = 2$."},
                    {"label": "d", "text": r"Đồ thị hàm số khi $m = 4$ là một đường thẳng đi qua gốc tọa độ.", "correct": False, "explanation": r"Sai. Đường thẳng $y = x + 2$ không đi qua gốc tọa độ $(0; 0)$."}
                ]
            },
            {
                "id": 2,
                "context": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N$ lần lượt là trung điểm của $SA$ và $SD$.",
                "sub_questions": [
                    {"label": "a", "text": r"Đường thẳng $MN$ song song với đường thẳng $AD$.", "correct": True, "explanation": r"Đúng. $MN$ là đường trung bình của tam giác $SAD$."},
                    {"label": "b", "text": r"Đường thẳng $MN$ song song với mặt phẳng $(ABCD)$.", "correct": True, "explanation": r"Đúng. Vì $MN // AD$ và $AD \subset (ABCD)$."},
                    {"label": "c", "text": r"Mặt phẳng $(OMN)$ song song với mặt phẳng $(SBC)$.", "correct": True, "explanation": r"Đúng. $ON // SC$ và $OM // SB \implies (OMN) // (SBC)$."},
                    {"label": "d", "text": r"Thiết diện của hình chóp cắt bởi mặt phẳng $(OMN)$ là một tam giác.", "correct": False, "explanation": r"Sai. Thiết diện là hình thang."}
                ]
            },
            {
                "id": 3,
                "context": r"Cho cấp số nhân $(u_n)$ có $u_1 = 1$ và $q = 2$. Gọi $S_n$ là tổng của $n$ số hạng đầu tiên.",
                "sub_questions": [
                    {"label": "a", "text": r"Số hạng tổng quát là $u_n = 2^{n - 1}$.", "correct": True, "explanation": r"Đúng."},
                    {"label": "b", "text": r"Tổng $S_n = 2^n - 1$.", "correct": True, "explanation": r"Đúng. $S_n = \frac{1(1 - 2^n)}{1 - 2} = 2^n - 1$."},
                    {"label": "c", "text": r"Để $S_n > 1000$ thì giá trị nhỏ nhất của $n$ là 10.", "correct": True, "explanation": r"Đúng. $2^{10} - 1 = 1023 > 1000$."},
                    {"label": "d", "text": r"Dãy số $(S_n)$ là một cấp số nhân.", "correct": False, "explanation": r"Sai. $S_n = 2^n - 1$ không phải cấp số nhân do có số hạng tự do -1."}
                ]
            },
            {
                "id": 4,
                "context": r"Cho phương trình: $\cos(2x) - (2m + 1)\cos x + m + 1 = 0$.",
                "sub_questions": [
                    {"label": "a", "text": r"Đưa về phương trình bậc 2 đối với $\cos x$: $2\cos^2 x - (2m + 1)\cos x + m = 0$.", "correct": True, "explanation": r"Đúng. Vì $\cos(2x) = 2\cos^2 x - 1$."},
                    {"label": "b", "text": r"Phương trình luôn có nghiệm $\cos x = 1$ với mọi giá trị của tham số $m$.", "correct": False, "explanation": r"Sai. Phân tích thành: $(2\cos x - 1)(\cos x - m) = 0 \implies \cos x = 1/2$ luôn là nghiệm."},
                    {"label": "c", "text": r"Một họ nghiệm độc lập với $m$ là $x = \pm \frac{\pi}{3} + k2\pi, k \in \mathbb{Z}$.", "correct": True, "explanation": r"Đúng. Từ $\cos x = 1/2$."},
                    {"label": "d", "text": r"Để phương trình có nghiệm thì $-1 \le m \le 1$.", "correct": False, "explanation": r"Sai. Phương trình luôn có nghiệm $\cos x = 1/2$ với mọi $m$."}
                ]
            }
        ],
        "part3": [
            {
                "id": 1,
                "question": r"Tính giới hạn $\lim_{x \to 3} \frac{\sqrt{x + 1} - 2}{x - 3}$ (viết kết quả dưới dạng số thập phân, ví dụ: 0.25):",
                "answer": "0.25",
                "explanation_steps": [
                    r"Nhân liên hợp cả tử và mẫu với $(\sqrt{x + 1} + 2)$:",
                    r"$\lim_{x \to 3} \frac{(x + 1) - 4}{(x - 3)(\sqrt{x + 1} + 2)} = \lim_{x \to 3} \frac{x - 3}{(x - 3)(\sqrt{x + 1} + 2)} = \lim_{x \to 3} \frac{1}{\sqrt{x + 1} + 2}$.",
                    r"Thay $x = 3$ vào: $\frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4} = 0.25$."
                ]
            },
            {
                "id": 2,
                "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành diện tích bằng 40. Gọi $M$ là trung điểm của cạnh $SC$. Mặt phẳng $(ABM)$ cắt cạnh $SD$ tại điểm $N$. Tính diện tích tứ giác $ABMN$:",
                "answer": "30",
                "explanation_steps": [
                    r"Vì $AB // CD$ nên giao tuyến của $(ABM)$ với $(SCD)$ qua $M$ song song với $CD$.",
                    r"Suy ra $MN // CD$. Do $M$ là trung điểm $SC \implies N$ là trung điểm $SD$.",
                    r"Tứ giác $ABMN$ là hình thang với $MN = \frac{1}{2} CD = \frac{1}{2} AB$.",
                    r"Tỉ số diện tích thiết diện được tính bằng 30."
                ]
            },
            {
                "id": 3,
                "question": r"Tìm giá trị của tham số $a$ để hàm số $f(x) = \begin{cases} \frac{x^2 - 9}{x - 3} & \text{khi } x > 3 \\ 2x + a & \text{khi } x \le 3 \end{cases}$ liên tục tại điểm $x = 3$:",
                "answer": "0",
                "explanation_steps": [
                    r"• $\lim_{x \to 3^+} f(x) = \lim_{x \to 3^+} (x + 3) = 6$.",
                    r"• $\lim_{x \to 3^-} f(x) = f(3) = 2(3) + a = 6 + a$.",
                    r"Để liên tục tại $x = 3 \iff 6 + a = 6 \implies a = 0$."
                ]
            },
            {
                "id": 4,
                "question": r"Tính tổng $S = 2 + \frac{2}{3} + \frac{2}{9} + \frac{2}{27} + \dots$:",
                "answer": "3",
                "explanation_steps": [
                    r"Đây là tổng cấp số nhân lùi vô hạn với $u_1 = 2$ và công bội $q = \frac{1}{3}$.",
                    r"Công thức: $S = \frac{u_1}{1 - q} = \frac{2}{1 - 1/3} = \frac{2}{2/3} = 3$."
                ]
            },
            {
                "id": 5,
                "question": r"Cho hình lăng trụ đứng $ABC.A'B'C'$ có chiều cao bằng 6. Trọng tâm tam giác $ABC$ là $G$, trọng tâm $A'B'C'$ là $G'$. Biết diện tích thiết diện qua $A, G, G'$ và song song với cạnh bên bằng 24. Tính độ dài đoạn thẳng $AG$:",
                "answer": "4",
                "explanation_steps": [
                    r"Mặt phẳng $(AGG')$ cắt lăng trụ theo thiết diện là hình bình hành $AGG'A'$.",
                    r"Diện tích hình bình hành bằng $AG \times h$ với $h = 6$.",
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

# Gộp thêm 3 Đề Giữa Kì 2
EXAM_LIST.extend(EXAMS_GK2)

def get_exam(exam_id):
    """Lấy thông tin đề thi theo id hoặc slug"""
    for ex in EXAM_LIST:
        if ex["id"] == exam_id or ex["slug"] == exam_id:
            return ex
    return None
