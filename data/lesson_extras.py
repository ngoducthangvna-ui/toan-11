# -*- coding: utf-8 -*-
"""
Dữ liệu bổ trợ bài học: Ví dụ vận dụng thực chiến và Câu hỏi trắc nghiệm nhanh (Quick Check)
Được tích hợp vào cấu trúc từng bài học để nâng cao tính tương tác.
"""

LESSON_EXTRAS = {
    # CHƯƠNG 1
    (1, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính giá trị lượng giác theo cung phần tư",
                "problem": r"Cho góc lượng giác $\alpha$ thỏa mãn $\sin \alpha = \frac{3}{5}$ và $\frac{\pi}{2} < \alpha < \pi$. Tính $\cos \alpha$ và $\tan \alpha$.",
                "solution": r"""<p><strong>Bước 1:</strong> Dùng hệ thức $\sin^2 \alpha + \cos^2 \alpha = 1 \implies \cos^2 \alpha = 1 - \left(\frac{3}{5}\right)^2 = \frac{16}{25}$.</p>
<p><strong>Bước 2:</strong> Vì $\frac{\pi}{2} < \alpha < \pi$ (góc phần tư thứ II) nên $\cos \alpha < 0 \implies \cos \alpha = -\frac{4}{5}$.</p>
<p><strong>Bước 3:</strong> Suy ra $\tan \alpha = \frac{\sin \alpha}{\cos \alpha} = \frac{3/5}{-4/5} = -\frac{3}{4}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Đổi góc có số đo $\alpha = \frac{3\pi}{4}$ rad sang độ:",
                "options": [r"A. $120^\circ$", r"B. $135^\circ$", r"C. $150^\circ$", r"D. $225^\circ$"],
                "answer": 1,
                "explanation": r"Công thức đổi đơn vị: $\alpha^\circ = \frac{180^\circ}{\pi} \cdot \alpha = \frac{180^\circ}{\pi} \cdot \frac{3\pi}{4} = 135^\circ$."
            },
            {
                "question": r"Cho $\pi < \alpha < \frac{3\pi}{2}$. Khẳng định nào sau đây là ĐÚNG?",
                "options": [r"A. $\sin \alpha > 0, \cos \alpha > 0$", r"B. $\sin \alpha < 0, \cos \alpha < 0$", r"C. $\sin \alpha > 0, \cos \alpha < 0$", r"D. $\tan \alpha < 0$"],
                "answer": 1,
                "explanation": r"Ở góc phần tư thứ III, cả trục hoành ($\cos$) và trục tung ($\sin$) đều nhận giá trị âm, do đó $\sin \alpha < 0$ và $\cos \alpha < 0$."
            }
        ]
    },
    (1, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Rút gọn biểu thức lượng giác",
                "problem": r"Tính giá trị của biểu thức $A = \sin 75^\circ \cdot \cos 15^\circ - \cos 75^\circ \cdot \sin 15^\circ$.",
                "solution": r"""<p><strong>Bước 1:</strong> Nhận dạng công thức cộng $\sin(a - b) = \sin a \cos b - \cos a \sin b$.</p>
<p><strong>Bước 2:</strong> Áp dụng với $a = 75^\circ, b = 15^\circ$: $A = \sin(75^\circ - 15^\circ) = \sin 60^\circ = \frac{\sqrt{3}}{2}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Công thức nhân đôi nào sau đây là ĐÚNG?",
                "options": [r"A. $\cos 2x = \cos^2 x + \sin^2 x$", r"B. $\sin 2x = 2\sin x \cos x$", r"C. $\cos 2x = 2\sin^2 x - 1$", r"D. $\sin 2x = \sin x \cos x$"],
                "answer": 1,
                "explanation": r"Công thức chuẩn: $\sin 2x = 2\sin x \cos x$, còn $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$."
            }
        ]
    },
    (1, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Tìm tập xác định của hàm số",
                "problem": r"Tìm tập xác định của hàm số $y = \tan\left(2x - \frac{\pi}{4}\right)$.",
                "solution": r"""<p><strong>Điều kiện:</strong> Hàm số $y = \tan u$ xác định khi $u \neq \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$).</p>
<p>Suy ra $2x - \frac{\pi}{4} \neq \frac{\pi}{2} + k\pi \iff 2x \neq \frac{3\pi}{4} + k\pi \iff x \neq \frac{3\pi}{8} + k\frac{\pi}{2}$.</p>
<p>Vậy $D = \mathbb{R} \setminus \left\{\frac{3\pi}{8} + k\frac{\pi}{2}, k \in \mathbb{Z}\right\}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Tập giá trị của hàm số $y = 3\sin 2x - 1$ là:",
                "options": ["A. $[-1; 1]$", "B. $[-4; 2]$", "C. $[-3; 3]$", "D. $[2; 4]$"],
                "answer": 1,
                "explanation": r"Vì $-1 \le \sin 2x \le 1 \implies -3 \le 3\sin 2x \le 3 \implies -4 \le 3\sin 2x - 1 \le 2$."
            }
        ]
    },
    (1, 4): {
        "examples": [
            {
                "title": "Ví dụ 1: Giải phương trình lượng giác cơ bản",
                "problem": r"Giải phương trình: $\sin\left(x + \frac{\pi}{3}\right) = \frac{1}{2}$.",
                "solution": r"""<p>Ta có $\frac{1}{2} = \sin \frac{\pi}{6}$, phương trình tương đương:</p>
<p>$\left[\begin{aligned} x + \frac{\pi}{3} &= \frac{\pi}{6} + k2\pi \\ x + \frac{\pi}{3} &= \pi - \frac{\pi}{6} + k2\pi \end{aligned}\right. \iff \left[\begin{aligned} x &= -\frac{\pi}{6} + k2\pi \\ x &= \frac{\pi}{2} + k2\pi \end{aligned}\right. \quad (k \in \mathbb{Z})$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Phương trình $\cos x = 0$ có nghiệm là:",
                "options": [r"A. $x = k2\pi$", r"B. $x = \frac{\pi}{2} + k\pi$", r"C. $x = \pi + k2\pi$", r"D. $x = k\pi$"],
                "answer": 1,
                "explanation": r"Điểm trên đường tròn lượng giác có hoành độ bằng 0 là hai điểm cực trị của trục tung: $x = \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$)."
            }
        ]
    },

    # CHƯƠNG 2
    (2, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Tìm số hạng và xét tính tăng giảm",
                "problem": r"Cho dãy số $(u_n)$ với $u_n = \frac{2n - 1}{n + 1}$. Tìm $u_5$ và chứng minh $(u_n)$ là dãy số tăng.",
                "solution": r"""<p>Thay $n = 5$: $u_5 = \frac{2(5) - 1}{5 + 1} = \frac{9}{6} = \frac{3}{2}$.</p>
<p>Xét hiệu $u_{n+1} - u_n = \frac{2(n+1) - 1}{(n+1) + 1} - \frac{2n - 1}{n + 1} = \frac{2n + 1}{n + 2} - \frac{2n - 1}{n + 1} = \frac{3}{(n+2)(n+1)} > 0, \forall n \ge 1$.</p>
<p>Vậy dãy $(u_n)$ là dãy số tăng.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Cho dãy số $(u_n)$ xác định bởi $u_n = 3n - 2$. Số hạng thứ 10 bằng:",
                "options": ["A. 26", "B. 28", "C. 30", "D. 32"],
                "answer": 1,
                "explanation": r"$u_{10} = 3(10) - 2 = 28$."
            }
        ]
    },
    (2, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Tìm số hạng đầu và công sai",
                "problem": r"Cho cấp số cộng $(u_n)$ có $u_1 = 3$ và $u_5 = 15$. Tìm công sai $d$ và tổng $S_{20}$.",
                "solution": r"""<p>Ta có $u_5 = u_1 + 4d \implies 15 = 3 + 4d \implies 4d = 12 \implies d = 3$.</p>
<p>Tổng 20 số hạng đầu: $S_{20} = \frac{20}{2}[2u_1 + (20-1)d] = 10[2(3) + 19(3)] = 10[6 + 57] = 630$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Cấp số cộng $(u_n)$ có $u_1 = 2$ và $d = -3$. Số hạng thứ 5 bằng:",
                "options": ["A. -10", "B. -13", "C. 14", "D. -7"],
                "answer": 0,
                "explanation": r"$u_5 = u_1 + 4d = 2 + 4(-3) = 2 - 12 = -10$."
            }
        ]
    },
    (2, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính toán trong cấp số nhân",
                "problem": r"Cho cấp số nhân $(u_n)$ có $u_1 = 2$ và công bội $q = 3$. Hỏi số 486 là số hạng thứ mấy?",
                "solution": r"""<p>Áp dụng $u_n = u_1 \cdot q^{n-1} \implies 486 = 2 \cdot 3^{n-1} \implies 3^{n-1} = 243 = 3^5$.</p>
<p>Suy ra $n - 1 = 5 \implies n = 6$. Vậy 486 là số hạng thứ 6.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 3, q = 2$. Tổng 5 số hạng đầu $S_5$ bằng:",
                "options": ["A. 93", "B. 96", "C. 48", "D. 63"],
                "answer": 0,
                "explanation": r"$S_5 = \frac{u_1(1 - q^5)}{1 - q} = \frac{3(1 - 32)}{1 - 2} = 3 \times 31 = 93$."
            }
        ]
    },

    # CHƯƠNG 3
    (3, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính số trung bình của mẫu ghép nhóm",
                "problem": r"Một nhóm gồm 20 học sinh có thời gian tự học mỗi ngày như sau: $[0; 2)$ có 4 em, $[2; 4)$ có 10 em, $[4; 6)$ có 6 em. Tính thời gian tự học trung bình.",
                "solution": r"""<p>Giá trị đại diện các nhóm lần lượt là: $c_1 = 1, c_2 = 3, c_3 = 5$.</p>
<p>Thời gian trung bình: $\bar{x} = \frac{4 \times 1 + 10 \times 3 + 6 \times 5}{20} = \frac{4 + 30 + 30}{20} = \frac{64}{20} = 3.2$ giờ.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Giá trị đại diện của nhóm số liệu $[40; 60)$ là:",
                "options": ["A. 40", "B. 50", "C. 60", "D. 45"],
                "answer": 1,
                "explanation": r"Giá trị đại diện bằng trung bình cộng hai đầu mút: $\frac{40 + 60}{2} = 50$."
            }
        ]
    },
    (3, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Tìm nhóm chứa mốt",
                "problem": r"Xét mẫu ghép nhóm với các tần số: $[10; 20)$ có 5; $[20; 30)$ có 18; $[30; 40)$ có 12; $[40; 50)$ có 7. Hãy xác định nhóm chứa mốt.",
                "solution": r"""<p>Tần số lớn nhất trong mẫu là 18 (thuộc nhóm $[20; 30)$).</p>
<p>Vậy nhóm chứa mốt của mẫu số liệu là $[20; 30)$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Nhóm chứa mốt của mẫu số liệu ghép nhóm là nhóm có:",
                "options": ["A. Độ dài lớn nhất", "B. Giá trị đại diện lớn nhất", "C. Tần số lớn nhất", "D. Tần số nhỏ nhất"],
                "answer": 2,
                "explanation": r"Theo định nghĩa: Nhóm chứa mốt là nhóm có tần số xuất hiện lớn nhất trong các nhóm số liệu."
            }
        ]
    },

    # CHƯƠNG 4
    (4, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Xác định giao tuyến của hai mặt phẳng",
                "problem": r"Cho tứ diện $ABCD$. Tìm giao tuyến của hai mặt phẳng $(ABC)$ và $(ABD)$.",
                "solution": r"""<p>Hai điểm phân biệt $A$ và $B$ đều thuộc cả hai mặt phẳng $(ABC)$ và $(ABD)$.</p>
<p>Do đó giao tuyến của hai mặt phẳng là đường thẳng đi qua hai điểm chung: $(ABC) \cap (ABD) = AB$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Có bao nhiêu mặt phẳng đi qua ba điểm không thẳng hàng?",
                "options": ["A. 1 và chỉ 1", "B. 2", "C. Vô số", "D. Không có"],
                "answer": 0,
                "explanation": r"Tiên đề cơ bản: Qua ba điểm không thẳng hàng xác định một và chỉ một mặt phẳng."
            }
        ]
    },
    (4, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Tìm giao tuyến song song",
                "problem": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với đáy lớn $AB$ song song với $CD$. Tìm giao tuyến của $(SAB)$ và $(SCD)$.",
                "solution": r"""<p>Ta có $S \in (SAB) \cap (SCD)$ là một điểm chung.</p>
<p>Mặt khác $AB \subset (SAB), CD \subset (SCD)$ và $AB // CD$.</p>
<p>Theo định lý giao tuyến của hai mặt phẳng chứa hai đường song song: Giao tuyến đi qua $S$ và song song với $AB, CD$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Hai đường thẳng phân biệt không có điểm chung và cùng nằm trong một mặt phẳng thì:",
                "options": ["A. Chéo nhau", "B. Trùng nhau", "C. Song song", "D. Cắt nhau"],
                "answer": 2,
                "explanation": r"Định nghĩa: Hai đường thẳng song song là hai đường thẳng đồng phẳng và không có điểm chung."
            }
        ]
    },
    (4, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Chứng minh đường thẳng song song mặt phẳng",
                "problem": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M$ là trung điểm của $SC$. Chứng minh $OM // (SAD)$.",
                "solution": r"""<p>Trong tam giác $SAC$, $O$ là trung điểm của $AC$, $M$ là trung điểm của $SC$. Do đó $OM$ là đường trung bình $\implies OM // SA$.</p>
<p>Vì $OM \not\subset (SAD)$ và $OM // SA$ với $SA \subset (SAD)$ nên $OM // (SAD)$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Điều kiện để đường thẳng $d$ song song với mặt phẳng $(\alpha)$ là:",
                "options": [
                    r"A. $d$ song song với ít nhất một đường thẳng nằm trong $(\alpha)$ và $d \not\subset (\alpha)$",
                    r"B. $d$ vuông góc với $(\alpha)$",
                    r"C. $d$ cắt $(\alpha)$",
                    r"D. $d$ song song với mọi đường thẳng nằm trong $(\alpha)$"
                ],
                "answer": 0,
                "explanation": r"Định lý: Nếu đường thẳng $d$ không nằm trong mặt phẳng $(\alpha)$ và song song với một đường thẳng nằm trong $(\alpha)$ thì $d // (\alpha)$."
            }
        ]
    },
    (4, 4): {
        "examples": [
            {
                "title": "Ví dụ 1: Chứng minh hai mặt phẳng song song",
                "problem": r"Cho hình lăng trụ tam giác $ABC.A'B'C'$. Chứng minh $(ABC) // (A'B'C')$.",
                "solution": r"""<p>Ta có $AB // A'B'$ và $AC // A'C'$ (các mặt bên là hình bình hành).</p>
<p>Vì $AB, AC$ cắt nhau tại $A$ trong $(ABC)$ và lần lượt song song với hai đường cắt nhau $A'B', A'C'$ trong $(A'B'C')$ nên $(ABC) // (A'B'C')$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Nếu hai mặt phẳng song song thì mọi đường thẳng nằm trong mặt phẳng này sẽ:",
                "options": [
                    "A. Cắt mặt phẳng kia",
                    "B. Song song với mặt phẳng kia",
                    "C. Trùng với mặt phẳng kia",
                    "D. Vuông góc với mặt phẳng kia"
                ],
                "answer": 1,
                "explanation": r"Theo tính chất: Nếu $(P) // (Q)$ thì mọi đường thẳng nằm trong $(P)$ đều song song với $(Q)$."
            }
        ]
    },

    # CHƯƠNG 5
    (5, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính giới hạn dạng phân thức vô định",
                "problem": r"Tính giới hạn $L = \lim_{n \to \infty} \frac{3n^2 - 2n + 5}{2n^2 + n - 1}$.",
                "solution": r"""<p>Chia cả tử và mẫu cho $n^2$ (bậc cao nhất):</p>
<p>$L = \lim_{n \to \infty} \frac{3 - \frac{2}{n} + \frac{5}{n^2}}{2 + \frac{1}{n} - \frac{1}{n^2}} = \frac{3 - 0 + 0}{2 + 0 - 0} = \frac{3}{2}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Giới hạn $\lim_{n \to \infty} \left(\frac{1}{3}\right)^n$ bằng:",
                "options": ["A. 1", "B. 0", r"C. $+\infty$", "D. 3"],
                "answer": 1,
                "explanation": r"Định lý giới hạn cấp số nhân: Nếu $|q| < 1$ thì $\lim_{n \to \infty} q^n = 0$. Ở đây $q = 1/3 < 1$ nên giới hạn bằng 0."
            }
        ]
    },
    (5, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Khử dạng vô định 0/0",
                "problem": r"Tính giới hạn $I = \lim_{x \to 2} \frac{x^2 - 4}{x - 2}$.",
                "solution": r"""<p>Khi $x \to 2$, cả tử và mẫu đều tiến về 0 (dạng $\frac{0}{0}$).</p>
<p>Phân tích tử thức thành nhân tử: $x^2 - 4 = (x - 2)(x + 2)$.</p>
<p>Suy ra $I = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x + 2) = 2 + 2 = 4$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Giới hạn $\lim_{x \to 3} (2x - 1)$ bằng:",
                "options": ["A. 5", "B. 6", "C. 7", "D. 4"],
                "answer": 0,
                "explanation": r"Hàm số xác định tại $x = 3$, thay số trực tiếp: $2(3) - 1 = 5$."
            }
        ]
    },
    (5, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Xét tính liên tục tại một điểm",
                "problem": r"Xét tính liên tục của hàm số $f(x) = \begin{cases} \frac{x^2 - 1}{x - 1} & \text{khi } x \neq 1 \\ 2 & \text{khi } x = 1 \end{cases}$ tại điểm $x = 1$.",
                "solution": r"""<p>1. Ta có $f(1) = 2$.</p>
<p>2. $\lim_{x \to 1} f(x) = \lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = \lim_{x \to 1} (x + 1) = 2$.</p>
<p>3. Do $\lim_{x \to 1} f(x) = f(1) = 2$, hàm số liên tục tại điểm $x = 1$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Hàm số $f(x) = \frac{1}{x - 3}$ gián đoạn tại điểm nào?",
                "options": ["A. $x = 0$", "B. $x = 3$", "C. $x = -3$", "D. Không có"],
                "answer": 1,
                "explanation": r"Hàm số không xác định tại $x = 3$, do đó hàm số gián đoạn tại $x = 3$."
            }
        ]
    },

    # CHƯƠNG 6
    (6, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Rút gọn biểu thức chứa lũy thừa",
                "problem": r"Rút gọn biểu thức $P = \frac{a^{4/3} \cdot \sqrt{a}}{a^{1/6}}$ với $a > 0$.",
                "solution": r"""<p>Đổi về cùng lũy thừa cơ số $a$: $\sqrt{a} = a^{1/2}$.</p>
<p>$P = \frac{a^{4/3 + 1/2}}{a^{1/6}} = \frac{a^{11/6}}{a^{1/6}} = a^{11/6 - 1/6} = a^{10/6} = a^{5/3}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Với $a > 0$, biểu thức $\sqrt[3]{a^2}$ viết dưới dạng lũy thừa với số mũ hữu tỉ là:",
                "options": [r"A. $a^{3/2}$", r"B. $a^{2/3}$", r"C. $a^6$", r"D. $a^{1/3}$"],
                "answer": 1,
                "explanation": r"Công thức chuẩn: $\sqrt[n]{a^m} = a^{m/n} \implies \sqrt[3]{a^2} = a^{2/3}$."
            }
        ]
    },
    (6, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính giá trị biểu thức logarit",
                "problem": r"Tính giá trị của biểu thức $A = \log_2 24 - \log_2 3$.",
                "solution": r"""<p>Áp dụng công thức hiệu hai logarit cùng cơ số: $\log_a x - \log_a y = \log_a \left(\frac{x}{y}\right)$.</p>
<p>$A = \log_2\left(\frac{24}{3}\right) = \log_2 8 = \log_2(2^3) = 3$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Với $a > 0, a \neq 1$, giá trị của $\log_a(a^4)$ bằng:",
                "options": ["A. 1", "B. 4", "C. 0", "D. $a$"],
                "answer": 1,
                "explanation": r"Theo định nghĩa logarit: $\log_a(a^k) = k \implies \log_a(a^4) = 4$."
            }
        ]
    },
    (6, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Xét chiều biến thiên của hàm số mũ và logarit",
                "problem": r"Trong các hàm số sau, hàm số nào đồng biến trên $\mathbb{R}$: $y = \left(\frac{1}{2}\right)^x, y = 3^x, y = \left(\frac{2}{3}\right)^x$?",
                "solution": r"""<p>Hàm số mũ $y = a^x$ đồng biến trên $\mathbb{R}$ khi cơ số $a > 1$.</p>
<p>Ta thấy $3 > 1$, trong khi $1/2 < 1$ và $2/3 < 1$. Do đó chỉ có hàm số $y = 3^x$ đồng biến trên $\mathbb{R}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Tập xác định của hàm số $y = \log_3(x - 2)$ là:",
                "options": [r"A. $(2; +\infty)$", r"B. $[2; +\infty)$", r"C. $(-\infty; 2)$", r"D. $\mathbb{R} \setminus \{2\}$"],
                "answer": 0,
                "explanation": r"Điều kiện để biểu thức dưới dấu logarit có nghĩa: $x - 2 > 0 \iff x > 2$."
            }
        ]
    },
    (6, 4): {
        "examples": [
            {
                "title": "Ví dụ 1: Giải phương trình logarit",
                "problem": r"Giải phương trình: $\log_2(x + 1) = 3$.",
                "solution": r"""<p>Điều kiện: $x + 1 > 0 \iff x > -1$.</p>
<p>Phương trình $\log_2(x + 1) = 3 \iff x + 1 = 2^3 = 8 \iff x = 7$ (thỏa mãn).</p>
<p>Vậy nghiệm của phương trình là $x = 7$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Nghiệm của phương trình $3^x = 9$ là:",
                "options": ["A. $x = 1$", "B. $x = 2$", "C. $x = 3$", "D. $x = 0$"],
                "answer": 1,
                "explanation": r"$3^x = 9 = 3^2 \implies x = 2$."
            }
        ]
    },

    # CHƯƠNG 7
    (7, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Viết phương trình tiếp tuyến của đồ thị hàm số",
                "problem": r"Viết phương trình tiếp tuyến của đồ thị hàm số $y = x^2 - 3x + 2$ tại điểm có hoành độ $x_0 = 2$.",
                "solution": r"""<p><strong>Bước 1:</strong> Tính tung độ tiếp điểm $y_0 = 2^2 - 3(2) + 2 = 0$. Tiếp điểm $M(2; 0)$.</p>
<p><strong>Bước 2:</strong> Tính đạo hàm $y' = 2x - 3 \implies y'(2) = 2(2) - 3 = 1$ (hệ số góc $k = 1$).</p>
<p><strong>Bước 3:</strong> Phương trình tiếp tuyến: $y - 0 = 1(x - 2) \iff y = x - 2$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Hệ số góc của tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $x_0$ là:",
                "options": ["A. $f(x_0)$", "B. $f'(x_0)$", r"C. $\frac{f(x_0)}{x_0}$", r"D. $\Delta y$"],
                "answer": 1,
                "explanation": r"Ý nghĩa hình học của đạo hàm: $f'(x_0)$ chính là hệ số góc của tiếp tuyến tại điểm có hoành độ $x_0$."
            }
        ]
    },
    (7, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính đạo hàm của tích và thương",
                "problem": r"Tính đạo hàm của hàm số $y = \frac{2x - 1}{x + 1}$.",
                "solution": r"""<p>Áp dụng quy tắc tính đạo hàm phân thức $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:</p>
<p>$y' = \frac{(2x - 1)'(x + 1) - (2x - 1)(x + 1)'}{(x + 1)^2} = \frac{2(x + 1) - 1(2x - 1)}{(x + 1)^2} = \frac{2x + 2 - 2x + 1}{(x + 1)^2} = \frac{3}{(x + 1)^2}$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Đạo hàm của hàm số $y = \sin(2x)$ là:",
                "options": [r"A. $\cos(2x)$", r"B. $2\cos(2x)$", r"C. $-2\cos(2x)$", r"D. $2\sin(2x)$"],
                "answer": 1,
                "explanation": r"Công thức đạo hàm hàm hợp: $(\sin u)' = u' \cdot \cos u \implies (\sin 2x)' = 2\cos(2x)$."
            }
        ]
    },
    (7, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Bài toán chuyển động tính gia tốc tức thời",
                "problem": r"Một vật chuyển động thẳng với phương trình $s(t) = t^3 - 3t^2 + 2t$ ($t$ tính bằng giây, $s$ tính bằng mét). Tính gia tốc của vật tại thời điểm $t = 3$ s.",
                "solution": r"""<p>Vận tốc tức thời: $v(t) = s'(t) = 3t^2 - 6t + 2$.</p>
<p>Gia tốc tức thời: $a(t) = v'(t) = s''(t) = 6t - 6$.</p>
<p>Tại $t = 3$: $a(3) = 6(3) - 6 = 12 \text{ m/s}^2$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Gia tốc tức thời $a(t)$ của chuyển động thẳng có phương trình quãng đường $s(t)$ là:",
                "options": ["A. $s(t)$", "B. $s'(t)$", "C. $s''(t)$", r"D. $\frac{s(t)}{t}$"],
                "answer": 2,
                "explanation": r"Gia tốc tức thời là đạo hàm cấp hai của quãng đường theo thời gian: $a(t) = s''(t) = v'(t)$."
            }
        ]
    },

    # CHƯƠNG 8
    (8, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính góc giữa hai đường thẳng trong không gian",
                "problem": r"Cho hình lập phương $ABCD.A'B'C'D'$. Tính góc giữa hai đường thẳng $AB$ và $B'C'$.",
                "solution": r"""<p>Vì $B'C' // BC$ nên góc giữa $AB$ và $B'C'$ bằng góc giữa $AB$ và $BC$.</p>
<p>Vì đáy $ABCD$ là hình vuông nên $\widehat{ABC} = 90^\circ$.</p>
<p>Vậy góc giữa $AB$ và $B'C'$ bằng $90^\circ$ (hai đường thẳng vuông góc với nhau).</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Góc giữa hai đường thẳng trong không gian có giá trị nằm trong khoảng nào?",
                "options": [r"A. $[0^\circ; 180^\circ]$", r"B. $[0^\circ; 90^\circ]$", r"C. $(0^\circ; 90^\circ)$", r"D. $[0^\circ; 360^\circ]$"],
                "answer": 1,
                "explanation": r"Theo quy ước: Góc giữa hai đường thẳng trong không gian luôn nằm trong đoạn từ $0^\circ$ đến $90^\circ$."
            }
        ]
    },
    (8, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Chứng minh đường thẳng vuông góc mặt phẳng",
                "problem": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \perp (ABCD)$. Chứng minh $BC \perp (SAB)$.",
                "solution": r"""<p>Ta có $BC \perp AB$ (do $ABCD$ là hình vuông).</p>
<p>Vì $SA \perp (ABCD)$ và $BC \subset (ABCD) \implies SA \perp BC$ hay $BC \perp SA$.</p>
<p>Như vậy $BC$ vuông góc với hai đường thẳng cắt nhau $AB$ và $SA$ trong mặt phẳng $(SAB)$. Do đó $BC \perp (SAB)$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Đường thẳng $d$ vuông góc với mặt phẳng $(\alpha)$ khi và chỉ khi:",
                "options": [
                    r"A. $d$ vuông góc với ít nhất 1 đường thẳng trong $(\alpha)$",
                    r"B. $d$ vuông góc với hai đường thẳng cắt nhau nằm trong $(\alpha)$",
                    r"C. $d$ song song với 1 đường thẳng trong $(\alpha)$",
                    r"D. $d$ vuông góc với hai đường thẳng song song trong $(\alpha)$"
                ],
                "answer": 1,
                "explanation": r"Định lý cơ bản: Nếu một đường thẳng vuông góc với hai đường thẳng cắt nhau cùng nằm trong một mặt phẳng thì nó vuông góc với mặt phẳng đó."
            }
        ]
    },
    (8, 3): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính khoảng cách từ điểm đến mặt phẳng",
                "problem": r"Cho hình chóp $S.ABC$ có $SA \perp (ABC)$ và $SA = a$. Tam giác $ABC$ vuông tại $B$ với $AB = a$. Tính khoảng cách từ $S$ đến $(ABC)$.",
                "solution": r"""<p>Vì $SA \perp (ABC)$ tại $A$ nên hình chiếu của $S$ lên $(ABC)$ là điểm $A$.</p>
<p>Do đó khoảng cách từ $S$ đến mặt phẳng $(ABC)$ chính là độ dài đoạn $SA = a$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Nếu mặt phẳng $(P)$ vuông góc với mặt phẳng $(Q)$ theo giao tuyến $d$, một đường thẳng nằm trong $(P)$ và vuông góc với $d$ thì:",
                "options": [
                    r"A. Song song với $(Q)$",
                    r"B. Vuông góc với $(Q)$",
                    r"C. Trùng với $(Q)$",
                    r"D. Cắt $(Q)$ nhưng không vuông góc"
                ],
                "answer": 1,
                "explanation": r"Định lý: Nếu hai mặt phẳng vuông góc với nhau thì bất kỳ đường thẳng nào nằm trong mặt phẳng này và vuông góc với giao tuyến thì vuông góc với mặt phẳng kia."
            }
        ]
    },
    (8, 4): {
        "examples": [
            {
                "title": "Ví dụ 1: Tính thể tích khối chóp",
                "problem": r"Tính thể tích khối chóp $S.ABC$ có diện tích đáy $S_{\triangle ABC} = 12 \text{ cm}^2$ và chiều cao $h = 5 \text{ cm}$.",
                "solution": r"""<p>Áp dụng công thức thể tích khối chóp: $V = \frac{1}{3} S_{\text{đáy}} \cdot h$.</p>
<p>$V = \frac{1}{3} \times 12 \times 5 = 20 \text{ cm}^3$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Công thức tính thể tích khối lăng trụ có diện tích đáy $B$ và chiều cao $h$ là:",
                "options": [r"A. $V = \frac{1}{3} B h$", r"B. $V = B h$", r"C. $V = \frac{1}{2} B h$", r"D. $V = 3 B h$"],
                "answer": 1,
                "explanation": r"Thể tích lăng trụ: $V = B \cdot h$, còn thể tích chóp mới có hệ số $1/3$."
            }
        ]
    },

    # CHƯƠNG 9
    (9, 1): {
        "examples": [
            {
                "title": "Ví dụ 1: Áp dụng quy tắc nhân xác suất",
                "problem": r"Hai xạ thủ độc lập cùng bắn vào một mục tiêu. Xác suất bắn trúng của xạ thủ thứ nhất là $P(A) = 0.7$, của xạ thủ thứ hai là $P(B) = 0.8$. Tính xác suất để cả hai xạ thủ cùng bắn trúng.",
                "solution": r"""<p>Vì hai xạ thủ bắn độc lập, biến cố "cả hai xạ thủ cùng bắn trúng" là biến cố giao $AB$.</p>
<p>Áp dụng quy tắc nhân: $P(AB) = P(A) \cdot P(B) = 0.7 \times 0.8 = 0.56$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Hai biến cố $A$ và $B$ độc lập khi:",
                "options": [
                    r"A. Việc biến cố này xảy ra hay không không ảnh hưởng đến xác suất xảy ra biến cố kia",
                    r"B. $A$ và $B$ không thể cùng xảy ra",
                    r"C. $A$ và $B$ luôn xảy ra đồng thời",
                    r"D. $P(A) + P(B) = 1$"
                ],
                "answer": 0,
                "explanation": r"Định nghĩa: Hai biến cố $A$ và $B$ được gọi là độc lập nếu việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng tới xác suất xảy ra của biến cố kia."
            }
        ]
    },
    (9, 2): {
        "examples": [
            {
                "title": "Ví dụ 1: Áp dụng quy tắc cộng xác suất",
                "problem": r"Một hộp chứa 5 quả cầu đỏ và 7 quả cầu xanh. Lấy ngẫu nhiên 1 quả cầu. Gọi $A$ là biến cố 'Lấy được quả đỏ' và $B$ là biến cố 'Lấy được quả xanh'. Tính xác suất lấy được quả màu đỏ hoặc màu xanh.",
                "solution": r"""<p>Tổng số quả cầu trong hộp là $5 + 7 = 12$ quả.</p>
<p>$P(A) = \frac{5}{12}, P(B) = \frac{7}{12}$.</p>
<p>Vì quả lấy ra không thể vừa đỏ vừa xanh nên $A$ và $B$ là hai biến cố xung khắc ($A \cap B = \emptyset$).</p>
<p>Áp dụng quy tắc cộng: $P(A \cup B) = P(A) + P(B) = \frac{5}{12} + \frac{7}{12} = 1$.</p>"""
            }
        ],
        "quick_check": [
            {
                "question": r"Cho hai biến cố xung khắc $A$ và $B$ với $P(A) = 0.35$ và $P(B) = 0.45$. Xác suất của biến cố hợp $P(A \cup B)$ bằng:",
                "options": ["A. 0.80", "B. 0.1575", "C. 0.10", "D. 0.70"],
                "answer": 0,
                "explanation": r"Vì $A$ và $B$ xung khắc nên $P(A \cup B) = P(A) + P(B) = 0.35 + 0.45 = 0.80$."
            },
            {
                "question": r"Cho biến cố $A$ có $P(A) = 0.65$. Xác suất của biến cố đối $P(\bar{A})$ bằng:",
                "options": ["A. 0.65", "B. 0.35", "C. 1.35", "D. 0"],
                "answer": 1,
                "explanation": r"Công thức biến cố đối: $P(\bar{A}) = 1 - P(A) = 1 - 0.65 = 0.35$."
            }
        ]
    }
}

def get_lesson_extras(chapter_id, lesson_id):
    """Lấy danh sách ví dụ vận dụng và câu hỏi quick check theo (ch_id, les_id)"""
    return LESSON_EXTRAS.get((int(chapter_id), int(lesson_id)), None)
