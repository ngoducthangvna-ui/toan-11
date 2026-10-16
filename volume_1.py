# -*- coding: utf-8 -*-
"""
Dữ liệu kiến thức Toán 11 - Tập 1 (Chương 1 đến Chương 5)
Chương trình Giáo dục phổ thông mới (KNTT, Cánh Diều, Chân Trời Sáng Tạo)
"""

VOLUME_1_CHAPTERS = [
    {
        "id": 1,
        "volume": 1,
        "slug": "ham-so-luong-giac-va-phuong-trinh-luong-giac",
        "title": "Chương 1: Hàm số lượng giác và Phương trình lượng giác",
        "short_title": "Chương 1: Lượng giác",
        "badge": "Đại số & Giải tích",
        "icon": "bi-symmetry-horizontal",
        "color": "indigo",
        "summary": "Nắm vững góc lượng giác, các công thức biến đổi lượng giác cốt lõi, khảo sát 4 hàm số lượng giác và phương pháp giải phương trình lượng giác cơ bản.",
        "lessons": [
            {
                "id": 1,
                "slug": "gia-tri-luong-giac-cua-goc-luong-giac",
                "title": "Bài 1: Giá trị lượng giác của góc lượng giác",
                "objectives": [
                    "Hiểu khái niệm góc lượng giác, đơn vị radian và liên hệ với độ.",
                    "Xác định giá trị lượng giác của góc trên đường tròn lượng giác.",
                    "Vận dụng các hệ thức lượng giác cơ bản và công thức cung liên kết."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Góc lượng giác và đơn vị Radian</h4>
    <p>Quy ước liên hệ giữa đơn vị độ và đơn vị radian:</p>
    <div class="math-box alert alert-primary">
        $$180^\circ = \pi \text{ rad} \implies 1^\circ = \frac{\pi}{180}\text{ rad}, \quad 1\text{ rad} = \left(\frac{180}{\pi}\right)^\circ \approx 57^\circ 17'45''$$
    </div>
    <p>Độ dài cung tròn bán kính $R$ có số đo $\alpha$ radian là: $$l = R\alpha$$</p>

    <h4>2. Đường tròn lượng giác & Các giá trị lượng giác</h4>
    <p>Đường tròn lượng giác là đường tròn định hướng tâm $O(0;0)$, bán kính $R=1$, chọn $A(1;0)$ làm điểm gốc.</p>
    <ul>
        <li>Trục hoành là <strong>trục Côsin</strong> ($\cos$).</li>
        <li>Trục tung là <strong>trục Sin</strong> ($\sin$).</li>
        <li>Trục tiếp tuyến tại $A(1;0)$ song song với trục tung là <strong>trục Tang</strong> ($\tan$).</li>
        <li>Trục tiếp tuyến tại $B(0;1)$ song song với trục hoành là <strong>trục Côtang</strong> ($\cot$).</li>
    </ul>

    <div class="math-box alert alert-secondary">
        <p><strong>Dấu của các giá trị lượng giác theo từng góc phần tư:</strong></p>
        <table class="table table-bordered table-sm text-center bg-white">
            <thead class="table-light">
                <tr><th>Góc phần tư</th><th>I $(0 < \alpha < \frac{\pi}{2})$</th><th>II $(\frac{\pi}{2} < \alpha < \pi)$</th><th>III $(\pi < \alpha < \frac{3\pi}{2})$</th><th>IV $(\frac{3\pi}{2} < \alpha < 2\pi)$</th></tr>
            </thead>
            <tbody>
                <tr><td>$\sin \alpha$</td><td class="text-success font-weight-bold">+</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td><td class="text-danger font-weight-bold">-</td></tr>
                <tr><td>$\cos \alpha$</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td><td class="text-danger font-weight-bold">-</td><td class="text-success font-weight-bold">+</td></tr>
                <tr><td>$\tan \alpha$</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td></tr>
                <tr><td>$\cot \alpha$</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td><td class="text-success font-weight-bold">+</td><td class="text-danger font-weight-bold">-</td></tr>
            </tbody>
        </table>
    </div>

    <h4>3. Các hệ thức lượng giác cơ bản</h4>
    <div class="formula-card">
        $$\sin^2 \alpha + \cos^2 \alpha = 1$$
        $$1 + \tan^2 \alpha = \frac{1}{\cos^2 \alpha} \quad \left(\alpha \neq \frac{\pi}{2} + k\pi\right)$$
        $$1 + \cot^2 \alpha = \frac{1}{\sin^2 \alpha} \quad (\alpha \neq k\pi)$$
        $$\tan \alpha \cdot \cot \alpha = 1 \quad \left(\alpha \neq k\frac{\pi}{2}\right)$$
    </div>

    <h4>4. Giá trị lượng giác của các cung có liên quan đặc biệt</h4>
    <p><em>(Thần chú ghi nhớ: Cos đối - Sin bù - Phụ chéo - Khác pi tan)</em></p>
    <ul>
        <li><strong>Cung đối nhau ($\alpha$ và $-\alpha$):</strong> $\cos(-\alpha) = \cos \alpha$, $\sin(-\alpha) = -\sin \alpha$, $\tan(-\alpha) = -\tan \alpha$.</li>
        <li><strong>Cung bù nhau ($\alpha$ và $\pi - \alpha$):</strong> $\sin(\pi - \alpha) = \sin \alpha$, $\cos(\pi - \alpha) = -\cos \alpha$.</li>
        <li><strong>Cung phụ nhau ($\alpha$ và $\frac{\pi}{2} - \alpha$):</strong> $\sin\left(\frac{\pi}{2} - \alpha\right) = \cos \alpha$, $\cos\left(\frac{\pi}{2} - \alpha\right) = \sin \alpha$.</li>
        <li><strong>Hơn kém nhau $\pi$ ($\alpha$ và $\alpha + \pi$):</strong> $\tan(\alpha + \pi) = \tan \alpha$, $\sin(\alpha + \pi) = -\sin \alpha$.</li>
    </ul>

    <div class="example-box">
        <h5 class="text-primary"><i class="bi bi-pencil-fill"></i> Ví dụ minh họa</h5>
        <p><strong>Bài toán:</strong> Cho $\sin \alpha = \frac{3}{5}$ với $\frac{\pi}{2} < \alpha < \pi$. Tính $\cos \alpha, \tan \alpha$.</p>
        <p><strong>Lời giải:</strong></p>
        <p>Áp dụng $\sin^2 \alpha + \cos^2 \alpha = 1 \implies \cos^2 \alpha = 1 - \sin^2 \alpha = 1 - \left(\frac{3}{5}\right)^2 = \frac{16}{25}$.</p>
        <p>Vì $\frac{\pi}{2} < \alpha < \pi$ (thuộc góc phần tư thứ II) nên $\cos \alpha < 0 \implies \cos \alpha = -\sqrt{\frac{16}{25}} = -\frac{4}{5}$.</p>
        <p>Khi đó: $\tan \alpha = \frac{\sin \alpha}{\cos \alpha} = \frac{3/5}{-4/5} = -\frac{3}{4}$.</p>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "cong-thuc-luong-giac",
                "title": "Bài 2: Các công thức lượng giác trọng tâm",
                "objectives": [
                    "Thành thạo công thức cộng, công thức nhân đôi, nhân ba.",
                    "Áp dụng công thức hạ bậc trong tính toán tích phân và lượng giác.",
                    "Sử dụng công thức biến đổi tích thành tổng và tổng thành tích."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Công thức cộng</h4>
    <div class="formula-card">
        $$\cos(a - b) = \cos a \cos b + \sin a \sin b$$
        $$\cos(a + b) = \cos a \cos b - \sin a \sin b$$
        $$\sin(a + b) = \sin a \cos b + \cos a \sin b$$
        $$\sin(a - b) = \sin a \cos b - \cos a \sin b$$
        $$\tan(a + b) = \frac{\tan a + \tan b}{1 - \tan a \tan b}, \quad \tan(a - b) = \frac{\tan a - \tan b}{1 + \tan a \tan b}$$
    </div>

    <h4>2. Công thức nhân đôi và công thức hạ bậc</h4>
    <div class="formula-card">
        <p><strong>Công thức nhân đôi:</strong></p>
        $$\sin 2a = 2\sin a \cos a$$
        $$\cos 2a = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a$$
        $$\tan 2a = \frac{2\tan a}{1 - \tan^2 a}$$

        <p class="mt-3"><strong>Công thức hạ bậc:</strong></p>
        $$\cos^2 a = \frac{1 + \cos 2a}{2}, \quad \sin^2 a = \frac{1 - \cos 2a}{2}$$
    </div>

    <h4>3. Công thức biến đổi tích thành tổng & tổng thành tích</h4>
    <div class="formula-card">
        <p><strong>Biến đổi tích thành tổng:</strong></p>
        $$\cos a \cos b = \frac{1}{2}[\cos(a - b) + \cos(a + b)]$$
        $$\sin a \sin b = \frac{1}{2}[\cos(a - b) - \cos(a + b)]$$
        $$\sin a \cos b = \frac{1}{2}[\sin(a + b) + \sin(a - b)]$$

        <p class="mt-3"><strong>Biến đổi tổng thành tích:</strong></p>
        $$\cos u + \cos v = 2\cos\frac{u+v}{2}\cos\frac{u-v}{2}$$
        $$\cos u - \cos v = -2\sin\frac{u+v}{2}\sin\frac{u-v}{2}$$
        $$\sin u + \sin v = 2\sin\frac{u+v}{2}\cos\frac{u-v}{2}$$
        $$\sin u - \sin v = 2\cos\frac{u+v}{2}\sin\frac{u-v}{2}$$
    </div>

    <div class="example-box">
        <h5 class="text-primary"><i class="bi bi-pencil-fill"></i> Ví dụ tính toán</h5>
        <p><strong>Bài toán:</strong> Rút gọn biểu thức $P = \sin\left(x + \frac{\pi}{6}\right) - \sin\left(x - \frac{\pi}{6}\right)$.</p>
        <p><strong>Lời giải:</strong></p>
        <p>Áp dụng công thức biến đổi tổng thành tích $\sin u - \sin v = 2\cos\frac{u+v}{2}\sin\frac{u-v}{2}$:</p>
        <p>Ta có: $\frac{u+v}{2} = \frac{(x + \pi/6) + (x - \pi/6)}{2} = x$</p>
        <p>$\frac{u-v}{2} = \frac{(x + \pi/6) - (x - \pi/6)}{2} = \frac{\pi}{6}$</p>
        <p>Do đó: $P = 2 \cos x \cdot \sin\frac{\pi}{6} = 2 \cos x \cdot \frac{1}{2} = \cos x$.</p>
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "ham-so-luong-giac",
                "title": "Bài 3: Hàm số lượng giác và đồ thị",
                "objectives": [
                    "Nắm vững tính chẵn lẻ, chu kì tuần hoàn của 4 hàm số lượng giác.",
                    "Xác định tập xác định và tập giá trị.",
                    "Nhận diện đồ thị hình sin và các phép tịnh tiến đồ thị."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Bảng tổng hợp tính chất 4 hàm số lượng giác</h4>
    <div class="table-responsive">
        <table class="table table-bordered table-hover bg-white text-center">
            <thead class="table-primary">
                <tr>
                    <th>Hàm số</th>
                    <th>Tập xác định ($D$)</th>
                    <th>Tập giá trị ($T$)</th>
                    <th>Tính chẵn / lẻ</th>
                    <th>Chu kì tuần hoàn</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>$y = \sin x$</strong></td>
                    <td>$\mathbb{R}$</td>
                    <td>$[-1; 1]$</td>
                    <td>Hàm số lẻ ($\sin(-x) = -\sin x$)</td>
                    <td>$T = 2\pi$</td>
                </tr>
                <tr>
                    <td><strong>$y = \cos x$</strong></td>
                    <td>$\mathbb{R}$</td>
                    <td>$[-1; 1]$</td>
                    <td>Hàm số chẵn ($\cos(-x) = \cos x$)</td>
                    <td>$T = 2\pi$</td>
                </tr>
                <tr>
                    <td><strong>$y = \tan x$</strong></td>
                    <td>$D = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right\}$</td>
                    <td>$\mathbb{R}$</td>
                    <td>Hàm số lẻ</td>
                    <td>$T = \pi$</td>
                </tr>
                <tr>
                    <td><strong>$y = \cot x$</strong></td>
                    <td>$D = \mathbb{R} \setminus \left\{k\pi, k \in \mathbb{Z}\right\}$</td>
                    <td>$\mathbb{R}$</td>
                    <td>Hàm số lẻ</td>
                    <td>$T = \pi$</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h4>2. Chu kì hàm hợp dạng $y = \sin(\omega x + \varphi)$ và $y = \tan(\omega x + \varphi)$</h4>
    <div class="math-box alert alert-info">
        <ul>
            <li>Hàm $y = A\sin(\omega x + \varphi)$ và $y = A\cos(\omega x + \varphi)$ có chu kì: $$T = \frac{2\pi}{|\omega|}$$</li>
            <li>Hàm $y = A\tan(\omega x + \varphi)$ và $y = A\cot(\omega x + \varphi)$ có chu kì: $$T = \frac{\pi}{|\omega|}$$</li>
        </ul>
    </div>
</div>
"""
            },
            {
                "id": 4,
                "slug": "phuong-trinh-luong-giac-co-ban",
                "title": "Bài 4: Phương trình lượng giác cơ bản",
                "objectives": [
                    "Nắm vững công thức nghiệm của phương trình lượng giác cơ bản.",
                    r"Hiểu điều kiện có nghiệm của $\sin x = m$ và $\cos x = m$.",
                    r"Sử dụng thành thạo đơn vị radian và chu kì $k2\pi, k\pi$ ($k \in \mathbb{Z}$)."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Phương trình $\sin x = m$</h4>
    <ul>
        <li>Nếu $|m| > 1$: Phương trình vô nghiệm.</li>
        <li>Nếu $|m| \le 1$: Gọi $\alpha$ sao cho $\sin \alpha = m$, nghiệm là:
            $$\left[\begin{array}{l} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{array}\right. \quad (k \in \mathbb{Z})$$
        </li>
    </ul>

    <h4>2. Phương trình $\cos x = m$</h4>
    <ul>
        <li>Nếu $|m| > 1$: Phương trình vô nghiệm.</li>
        <li>Nếu $|m| \le 1$: Gọi $\alpha$ sao cho $\cos \alpha = m$, nghiệm là:
            $$x = \pm \alpha + k2\pi \quad (k \in \mathbb{Z})$$
        </li>
    </ul>

    <h4>3. Phương trình $\tan x = m$ và $\cot x = m$</h4>
    <p>Phương trình luôn có nghiệm với mọi $m \in \mathbb{R}$:</p>
    $$\tan x = \tan \alpha \iff x = \alpha + k\pi \quad (k \in \mathbb{Z})$$
    $$\cot x = \cot \alpha \iff x = \alpha + k\pi \quad (k \in \mathbb{Z})$$

    <h4>4. Các trường hợp đặc biệt thường gặp</h4>
    <div class="math-box alert alert-warning">
        $$\sin x = 0 \iff x = k\pi; \quad \sin x = 1 \iff x = \frac{\pi}{2} + k2\pi; \quad \sin x = -1 \iff x = -\frac{\pi}{2} + k2\pi$$
        $$\cos x = 0 \iff x = \frac{\pi}{2} + k\pi; \quad \cos x = 1 \iff x = k2\pi; \quad \cos x = -1 \iff x = \pi + k2\pi$$
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 1: Lượng giác",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Góc lượng giác có số đo $\frac{5\pi}{6}\text{ rad}$ khi đổi sang đơn vị độ bằng:",
                    "options": [r"A. $120^\circ$", r"B. $150^\circ$", r"C. $135^\circ$", r"D. $210^\circ$"],
                    "correct": 1,
                    "explanation": r"Ta có công thức: $\alpha^\circ = \alpha\text{ rad} \cdot \frac{180^\circ}{\pi} = \frac{5\pi}{6} \cdot \frac{180}{\pi} = 150^\circ$."
                },
                {
                    "id": 2,
                    "question": r"Cho góc $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$. Khẳng định nào sau đây là ĐÚNG?",
                    "options": [
                        r"A. $\sin \alpha < 0, \cos \alpha < 0$",
                        r"B. $\sin \alpha > 0, \cos \alpha > 0$",
                        r"C. $\sin \alpha > 0, \cos \alpha < 0$",
                        r"D. $\sin \alpha < 0, \cos \alpha > 0$"
                    ],
                    "correct": 2,
                    "explanation": r"Góc $\alpha$ thuộc góc phần tư thứ II nên $\sin \alpha > 0$ và $\cos \alpha < 0$."
                },
                {
                    "id": 3,
                    "question": r"Khẳng định nào sau đây là ĐÚNG với mọi $a, b$?",
                    "options": [
                        r"A. $\cos(a+b) = \cos a \cos b + \sin a \sin b$",
                        r"B. $\cos(a+b) = \cos a \cos b - \sin a \sin b$",
                        r"C. $\sin(a+b) = \sin a \cos b - \cos a \sin b$",
                        r"D. $\cos 2a = 1 - \sin^2 a$"
                    ],
                    "correct": 1,
                    "explanation": r"Công thức cộng đúng là $\cos(a+b) = \cos a \cos b - \sin a \sin b$."
                },
                {
                    "id": 4,
                    "question": r"Tập xác định của hàm số $y = \tan x$ là:",
                    "options": [
                        r"A. $D = \mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$",
                        r"B. $D = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right\}$",
                        r"C. $D = \mathbb{R}$",
                        "D. $D = [-1; 1]$"
                    ],
                    "correct": 1,
                    "explanation": r"Hàm số $y = \tan x = \frac{\sin x}{\cos x}$ xác định khi $\cos x \neq 0 \iff x \neq \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$)."
                },
                {
                    "id": 5,
                    "question": r"Nghiệm của phương trình $\sin x = \frac{1}{2}$ là:",
                    "options": [
                        r"A. $x = \pm \frac{\pi}{6} + k2\pi$",
                        r"B. $x = \frac{\pi}{6} + k2\pi$ hoặc $x = \frac{5\pi}{6} + k2\pi$",
                        r"C. $x = \frac{\pi}{3} + k2\pi$ hoặc $x = \frac{2\pi}{3} + k2\pi$",
                        r"D. $x = \frac{\pi}{6} + k\pi$"
                    ],
                    "correct": 1,
                    "explanation": r"Vì $\sin \frac{\pi}{6} = \frac{1}{2}$, nghiệm là $x = \frac{\pi}{6} + k2\pi$ hoặc $x = \pi - \frac{\pi}{6} + k2\pi = \frac{5\pi}{6} + k2\pi$ ($k \in \mathbb{Z}$)."
                },
                {
                    "id": 6,
                    "question": r"Chu kì tuần hoàn của hàm số $y = \cos 2x$ là:",
                    "options": [r"A. $2\pi$", r"B. $\pi$", r"C. $4\pi$", r"D. $\frac{\pi}{2}$"],
                    "correct": 1,
                    "explanation": r"Hàm số $y = \cos(\omega x)$ có chu kì $T = \frac{2\pi}{|\omega|} = \frac{2\pi}{2} = \pi$."
                },
                {
                    "id": 7,
                    "question": r"Số nghiệm của phương trình $\cos x = 0$ thuộc đoạn $[0; 2\pi]$ là:",
                    "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
                    "correct": 1,
                    "explanation": r"$\cos x = 0 \iff x = \frac{\pi}{2} + k\pi$. Trên đoạn $[0; 2\pi]$, các nghiệm là $x = \frac{\pi}{2}$ ($k=0$) và $x = \frac{3\pi}{2}$ ($k=1$). Vậy có đúng 2 nghiệm."
                },
                {
                    "id": 8,
                    "question": r"Giá trị của biểu thức $M = \sin^2 15^\circ + \sin^2 75^\circ$ bằng:",
                    "options": ["A. 0", "B. 1", r"C. $\frac{1}{2}$", "D. 2"],
                    "correct": 1,
                    "explanation": r"Vì $15^\circ + 75^\circ = 90^\circ$ nên $\sin 75^\circ = \cos 15^\circ$. Do đó $M = \sin^2 15^\circ + \cos^2 15^\circ = 1$."
                }
            ]
        }
    },
    {
        "id": 2,
        "volume": 1,
        "slug": "day-so-cap-so-cong-va-cap-so-nhan",
        "title": "Chương 2: Dãy số. Cấp số cộng và Cấp số nhân",
        "short_title": "Chương 2: Dãy số, CSC & CSN",
        "badge": "Đại số & Giải tích",
        "icon": "bi-sort-numeric-up",
        "color": "teal",
        "summary": "Khái niệm dãy số, dãy tăng giảm, bị chặn. Nắm vững tính chất, công thức số hạng tổng quát và công thức tính tổng $n$ số hạng đầu của Cấp số cộng và Cấp số nhân.",
        "lessons": [
            {
                "id": 1,
                "slug": "day-so",
                "title": "Bài 1: Dãy số và các tính chất",
                "objectives": [
                    "Hiểu định nghĩa dãy số hữu hạn và vô hạn.",
                    "Xét tính tăng, giảm của dãy số ($u_{n+1} - u_n$ hoặc so sánh với 1).",
                    "Xét tính bị chặn trên, bị chặn dưới và bị chặn của dãy số."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa dãy số</h4>
    <p>Mỗi hàm số $u: \mathbb{N}^* \to \mathbb{R}, n \mapsto u(n)$ được gọi là một dãy số vô hạn, kí hiệu là $(u_n)$. Dạng khai triển: $u_1, u_2, u_3, \dots, u_n, \dots$</p>

    <h4>2. Dãy số tăng, dãy số giảm</h4>
    <ul>
        <li>Dãy số $(u_n)$ là <strong>dãy số tăng</strong> nếu với mọi $n \in \mathbb{N}^*$: $$u_{n+1} > u_n \iff u_{n+1} - u_n > 0$$</li>
        <li>Dãy số $(u_n)$ là <strong>dãy số giảm</strong> nếu với mọi $n \in \mathbb{N}^*$: $$u_{n+1} < u_n \iff u_{n+1} - u_n < 0$$</li>
        <li><em>Nếu $u_n > 0$ với mọi $n$:</em> so sánh tỉ số $\frac{u_{n+1}}{u_n}$ với $1$. Tỉ số $> 1 \implies$ dãy tăng, $< 1 \implies$ dãy giảm.</li>
    </ul>

    <h4>3. Dãy số bị chặn</h4>
    <ul>
        <li>Bị chặn trên: tồn tại $M$ sao cho $u_n \le M, \forall n \in \mathbb{N}^*$.</li>
        <li>Bị chặn dưới: tồn tại $m$ sao cho $u_n \ge m, \forall n \in \mathbb{N}^*$.</li>
        <li><strong>Bị chặn:</strong> vừa bị chặn trên vừa bị chặn dưới ($m \le u_n \le M, \forall n \in \mathbb{N}^*$).</li>
    </ul>
</div>
"""
            },
            {
                "id": 2,
                "slug": "cap-so-cong",
                "title": "Bài 2: Cấp số cộng (CSC)",
                "objectives": [
                    "Định nghĩa cấp số cộng và công sai $d$.",
                    "Số hạng tổng quát: $u_n = u_1 + (n-1)d$.",
                    "Công thức tính tổng $n$ số hạng đầu $S_n$."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa</h4>
    <p>Dãy số $(u_n)$ là cấp số cộng nếu tồn tại hằng số $d$ (gọi là công sai) sao cho:</p>
    <div class="formula-card">
        $$u_{n+1} = u_n + d \quad (\forall n \in \mathbb{N}^*)$$
    </div>

    <h4>2. Số hạng tổng quát</h4>
    <div class="formula-card">
        $$u_n = u_1 + (n-1)d \quad (n \ge 2)$$
    </div>

    <h4>3. Tính chất các số hạng</h4>
    $$u_k = \frac{u_{k-1} + u_{k+1}}{2} \quad (k \ge 2)$$
    <p>Ba số $a, b, c$ theo thứ tự lập thành CSC $\iff a + c = 2b$.</p>

    <h4>4. Tổng $n$ số hạng đầu tiên ($S_n$)</h4>
    <div class="formula-card">
        $$S_n = u_1 + u_2 + \dots + u_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n-1)d]}{2}$$
    </div>

    <div class="example-box">
        <h5 class="text-primary"><i class="bi bi-pencil-fill"></i> Ví dụ</h5>
        <p><strong>Bài toán:</strong> Cho CSC $(u_n)$ có $u_1 = 3$, công sai $d = 5$. Tìm số hạng thứ 10 và tổng 20 số hạng đầu.</p>
        <p><strong>Lời giải:</strong></p>
        <p>$u_{10} = u_1 + 9d = 3 + 9 \times 5 = 48$.</p>
        <p>$S_{20} = \frac{20 \cdot [2 \times 3 + (20-1) \times 5]}{2} = 10 \cdot [6 + 95] = 10 \cdot 101 = 1010$.</p>
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "cap-so-nhan",
                "title": "Bài 3: Cấp số nhân (CSN)",
                "objectives": [
                    "Định nghĩa cấp số nhân và công bội $q$.",
                    r"Số hạng tổng quát: $u_n = u_1 \cdot q^{n-1}$.",
                    "Tổng $n$ số hạng đầu tiên và tính chất của CSN."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa</h4>
    <p>Dãy số $(u_n)$ là cấp số nhân nếu tồn tại hằng số $q$ (công bội) sao cho:</p>
    <div class="formula-card">
        $$u_{n+1} = u_n \cdot q \quad (\forall n \in \mathbb{N}^*)$$
    </div>

    <h4>2. Số hạng tổng quát</h4>
    <div class="formula-card">
        $$u_n = u_1 \cdot q^{n-1} \quad (n \ge 2)$$
    </div>

    <h4>3. Tính chất các số hạng</h4>
    $$u_k^2 = u_{k-1} \cdot u_{k+1} \implies |u_k| = \sqrt{u_{k-1} \cdot u_{k+1}} \quad (k \ge 2)$$
    <p>Ba số $a, b, c$ theo thứ tự lập thành CSN $\iff ac = b^2$.</p>

    <h4>4. Tổng $n$ số hạng đầu tiên ($S_n$)</h4>
    <div class="formula-card">
        <p>Với $q \neq 1$:</p>
        $$S_n = \frac{u_1(1 - q^n)}{1 - q} = \frac{u_1(q^n - 1)}{q - 1}$$
        <p>Nếu $q = 1$ thì $S_n = n \cdot u_1$.</p>
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 2: Dãy số, CSC & CSN",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = 3n - 1$. Ba số hạng đầu tiên của dãy là:",
                    "options": ["A. $2, 5, 8$", "B. $1, 4, 7$", "C. $3, 6, 9$", "D. $2, 4, 6$"],
                    "correct": 0,
                    "explanation": r"$u_1 = 3(1)-1 = 2$, $u_2 = 3(2)-1 = 5$, $u_3 = 3(3)-1 = 8$."
                },
                {
                    "id": 2,
                    "question": r"Cho cấp số cộng $(u_n)$ có $u_1 = 2$ và công sai $d = 3$. Số hạng thứ 5 của cấp số cộng là:",
                    "options": ["A. 14", "B. 17", "C. 11", "D. 15"],
                    "correct": 0,
                    "explanation": r"$u_5 = u_1 + 4d = 2 + 4 \times 3 = 14$."
                },
                {
                    "id": 3,
                    "question": r"Cho cấp số nhân $(u_n)$ có $u_1 = 3$ và công bội $q = 2$. Giá trị của $u_4$ bằng:",
                    "options": ["A. 24", "B. 48", "C. 18", "D. 12"],
                    "correct": 0,
                    "explanation": r"$u_4 = u_1 \cdot q^3 = 3 \cdot 2^3 = 3 \cdot 8 = 24$."
                },
                {
                    "id": 4,
                    "question": r"Cho cấp số cộng có $u_1 = 1$, công sai $d = 2$. Tổng 10 số hạng đầu $S_{10}$ là:",
                    "options": ["A. 100", "B. 90", "C. 110", "D. 80"],
                    "correct": 0,
                    "explanation": r"$S_{10} = \frac{10[2(1) + (10-1)2]}{2} = 5[2 + 18] = 100$."
                },
                {
                    "id": 5,
                    "question": r"Dãy số nào sau đây là dãy số giảm?",
                    "options": [
                        "A. $u_n = n^2$",
                        r"B. $u_n = \frac{1}{n}$",
                        "C. $u_n = 2^n$",
                        "D. $u_n = 3n + 1$"
                    ],
                    "correct": 1,
                    "explanation": r"Với $u_n = \frac{1}{n}$, khi $n$ tăng thì $\frac{1}{n}$ giảm dần (1, 1/2, 1/3, ...), do đó đây là dãy số giảm."
                },
                {
                    "id": 6,
                    "question": r"Cho ba số $x, 5, 25$ theo thứ tự lập thành một cấp số nhân. Giá trị của $x$ là:",
                    "options": ["A. 1", "B. 5", "C. 0", "D. 2"],
                    "correct": 0,
                    "explanation": r"Theo tính chất cấp số nhân: $5^2 = x \cdot 25 \iff 25 = 25x \iff x = 1$."
                },
                {
                    "id": 7,
                    "question": r"Cho cấp số cộng có $u_4 = 10$ và $u_7 = 19$. Công sai $d$ của cấp số cộng bằng:",
                    "options": ["A. 2", "B. 3", "C. 4", "D. 5"],
                    "correct": 1,
                    "explanation": r"Ta có $u_7 - u_4 = (7-4)d = 3d \iff 19 - 10 = 3d \iff 9 = 3d \iff d = 3$."
                },
                {
                    "id": 8,
                    "question": r"Dãy số $(u_n)$ với $u_n = \sin n$ là một dãy số:",
                    "options": [
                        "A. Tăng",
                        "B. Giảm",
                        "C. Bị chặn",
                        "D. Không bị chặn"
                    ],
                    "correct": 2,
                    "explanation": r"Vì $-1 \le \sin n \le 1$ với mọi $n \in \mathbb{N}^*$, nên dãy số bị chặn trên bởi 1 và bị chặn dưới bởi -1, tức là bị chặn."
                }
            ]
        }
    },
    {
        "id": 3,
        "volume": 1,
        "slug": "cac-so-dac-trung-do-xu-the-trung-tam-mau-so-lieu-ghep-nhom",
        "title": "Chương 3: Số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm",
        "short_title": "Chương 3: Thống kê mẫu ghép nhóm",
        "badge": "Thống kê & Xác suất",
        "icon": "bi-bar-chart-line-fill",
        "color": "emerald",
        "summary": "Nắm vững phương pháp ghép nhóm dữ liệu, tính số trung bình, trung vị, các tứ phân vị ($Q_1, Q_2, Q_3$) và mốt của mẫu số liệu ghép nhóm.",
        "lessons": [
            {
                "id": 1,
                "slug": "mau-so-lieu-ghep-nhom",
                "title": "Bài 1: Thu thập và ghép nhóm số liệu",
                "objectives": [
                    "Hiểu cấu trúc mẫu số liệu ghép nhóm $[a_i; a_{i+1})$.",
                    "Xác định độ dài nhóm và giá trị đại diện của từng nhóm.",
                    "Lập bảng phân bố tần số ghép nhóm."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Khái niệm mẫu số liệu ghép nhóm</h4>
    <p>Mẫu số liệu ghép nhóm là mẫu số liệu được cho dưới dạng các khoảng nửa mở $[a_i; a_{i+1})$ với tần số tương ứng $m_i$.</p>
    <div class="formula-card">
        <p>Với mỗi nhóm $[a_i; a_{i+1})$:</p>
        <ul>
            <li><strong>Độ dài nhóm:</strong> $h = a_{i+1} - a_i$</li>
            <li><strong>Giá trị đại diện:</strong> $$c_i = \frac{a_i + a_{i+1}}{2}$$</li>
            <li><strong>Kích thước mẫu:</strong> $n = m_1 + m_2 + \dots + m_k$</li>
        </ul>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "cac-so-dac-trung",
                "title": "Bài 2: Các số đặc trưng đo xu thế trung tâm",
                "objectives": [
                    "Tính số trung bình của mẫu số liệu ghép nhóm.",
                    "Xác định trung vị ($M_e$), tứ phân vị ($Q_1, Q_2, Q_3$).",
                    "Xác định nhóm chứa mốt và tính giá trị mốt ($M_o$)."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Số trung bình ($\bar{x}$)</h4>
    <div class="formula-card">
        $$\bar{x} = \frac{m_1 c_1 + m_2 c_2 + \dots + m_k c_k}{n} = \frac{1}{n} \sum_{i=1}^k m_i c_i$$
    </div>

    <h4>2. Trung vị ($M_e$)</h4>
    <p>Bước 1: Xác định nhóm chứa trung vị: Nhóm đầu tiên $[a_p; a_{p+1})$ có tần số tích lũy $cf_p \ge \frac{n}{2}$.</p>
    <div class="formula-card">
        $$M_e = a_p + \frac{\frac{n}{2} - cf_{p-1}}{m_p} \cdot (a_{p+1} - a_p)$$
        <p class="small text-muted mb-0">Trong đó $cf_{p-1}$ là tần số tích lũy của nhóm đứng trước nhóm $p$; $m_p$ là tần số của nhóm $p$.</p>
    </div>

    <h4>3. Tứ phân vị ($Q_1, Q_2, Q_3$)</h4>
    <ul>
        <li>$Q_2 = M_e$.</li>
        <li>$Q_1$: thay $\frac{n}{2}$ bởi $\frac{n}{4}$ vào nhóm chứa tứ phân vị thứ nhất.
            $$Q_1 = a_p + \frac{\frac{n}{4} - cf_{p-1}}{m_p} \cdot h$$
        </li>
        <li>$Q_3$: thay $\frac{n}{2}$ bởi $\frac{3n}{4}$ vào nhóm chứa tứ phân vị thứ ba.
            $$Q_3 = a_r + \frac{\frac{3n}{4} - cf_{r-1}}{m_r} \cdot h$$
        </li>
    </ul>

    <h4>4. Mốt ($M_o$)</h4>
    <p>Nhóm chứa mốt là nhóm có tần số $m_j$ lớn nhất. Công thức mốt:</p>
    <div class="formula-card">
        $$M_o = a_j + \frac{m_j - m_{j-1}}{(m_j - m_{j-1}) + (m_j - m_{j+1})} \cdot (a_{j+1} - a_j)$$
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 3: Thống kê mẫu ghép nhóm",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Giá trị đại diện của nhóm số liệu $[20; 30)$ là:",
                    "options": ["A. 20", "B. 25", "C. 30", "D. 10"],
                    "correct": 1,
                    "explanation": r"Giá trị đại diện $c_i = \frac{20 + 30}{2} = 25$."
                },
                {
                    "id": 2,
                    "question": r"Độ dài của nhóm số liệu $[15; 25)$ là:",
                    "options": ["A. 10", "B. 20", "C. 5", "D. 40"],
                    "correct": 0,
                    "explanation": r"Độ dài nhóm $h = 25 - 15 = 10$."
                },
                {
                    "id": 3,
                    "question": r"Tứ phân vị thứ hai $Q_2$ của mẫu số liệu chính là:",
                    "options": ["A. Số trung bình", "B. Trung vị", "C. Mốt", "D. Độ lệch chuẩn"],
                    "correct": 1,
                    "explanation": r"Theo định nghĩa, tứ phân vị thứ hai $Q_2$ trùng với số trung vị $M_e$."
                },
                {
                    "id": 4,
                    "question": r"Nhóm chứa mốt của một mẫu số liệu ghép nhóm là nhóm có:",
                    "options": [
                        "A. Độ dài lớn nhất",
                        "B. Giá trị đại diện lớn nhất",
                        "C. Tần số lớn nhất",
                        "D. Tần số tích lũy lớn nhất"
                    ],
                    "correct": 2,
                    "explanation": r"Nhóm chứa mốt được định nghĩa là nhóm có tần số xuất hiện $m_i$ lớn nhất trong bảng phân bố."
                },
                {
                    "id": 5,
                    "question": r"Một lớp có 40 học sinh. Để tìm nhóm chứa trung vị, ta tìm nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng:",
                    "options": ["A. 10", "B. 20", "C. 30", "D. 40"],
                    "correct": 1,
                    "explanation": r"Vị trí trung vị tương ứng với $\frac{n}{2} = \frac{40}{2} = 20$."
                },
                {
                    "id": 6,
                    "question": r"Để tìm nhóm chứa tứ phân vị thứ nhất $Q_1$ của mẫu số liệu có kích thước $n = 60$, ta tìm nhóm có tần số tích lũy đầu tiên đạt ít nhất:",
                    "options": ["A. 15", "B. 30", "C. 45", "D. 20"],
                    "correct": 0,
                    "explanation": r"Vị trí $Q_1$ tính theo $\frac{n}{4} = \frac{60}{4} = 15$."
                }
            ]
        }
    },
    {
        "id": 4,
        "volume": 1,
        "slug": "quan-he-song-song-trong-khong-gian",
        "title": "Chương 4: Quan hệ song song trong không gian",
        "short_title": "Chương 4: Song song không gian",
        "badge": "Hình học không gian",
        "icon": "bi-box",
        "color": "amber",
        "summary": "Đại cương đường thẳng và mặt phẳng, các tiên đề hình học không gian, vị trí tương đối, định lí về đường thẳng và hai mặt phẳng song song, hình lăng trụ và hình chóp cụt.",
        "lessons": [
            {
                "id": 1,
                "slug": "dai-cuong-duong-thang-va-mat-phang",
                "title": "Bài 1: Điểm, đường thẳng và mặt phẳng trong không gian",
                "objectives": [
                    "Các cách xác định một mặt phẳng trong không gian.",
                    "Các tiên đề hình học không gian.",
                    "Vị trí tương đối của hai đường thẳng (cắt nhau, song song, trùng nhau, chéo nhau)."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Các cách xác định mặt phẳng</h4>
    <p>Một mặt phẳng được xác định duy nhất khi biết:</p>
    <ul>
        <li>Ba điểm không thẳng hàng. Kí hiệu $(ABC)$.</li>
        <li>Một đường thẳng và một điểm nằm ngoài đường thẳng đó. Kí hiệu $(M, d)$.</li>
        <li>Hai đường thẳng cắt nhau. Kí hiệu $(a, b)$.</li>
        <li>Hai đường thẳng song song. Kí hiệu $(a, b)$.</li>
    </ul>

    <h4>2. Vị trí tương đối của hai đường thẳng trong không gian</h4>
    <div class="table-responsive">
        <table class="table table-bordered bg-white text-center">
            <thead class="table-warning">
                <tr><th>Trường hợp</th><th>Số điểm chung</th><th>Cùng thuộc một mp?</th></tr>
            </thead>
            <tbody>
                <tr><td>Cắt nhau ($a \cap b = \{M\}$)</td><td>1 điểm chung</td><td>Có</td></tr>
                <tr><td>Song song ($a // b$)</td><td>0 điểm chung</td><td>Có</td></tr>
                <tr><td>Trùng nhau ($a \equiv b$)</td><td>Vô số điểm chung</td><td>Có</td></tr>
                <tr><td><strong>Chéo nhau</strong></td><td>0 điểm chung</td><td><strong>Không</strong></td></tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "hai-duong-thang-song-song",
                "title": "Bài 2: Hai đường thẳng song song",
                "objectives": [
                    "Định nghĩa và tính chất của hai đường thẳng song song.",
                    "Định lí giao tuyến của 3 mặt phẳng.",
                    "Định lí về hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Định lí 1 (Tính chất bắc cầu)</h4>
    <p>Trong không gian, hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau:</p>
    <div class="formula-card">
        $$\left.\begin{array}{l} a // c \\ b // c \\ a \not\equiv b \end{array}\right\} \implies a // b$$
    </div>

    <h4>2. Định lí giao tuyến (Định lí 3 đường thẳng)</h4>
    <p>Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến đó hoặc <strong>đồng quy</strong> hoặc <strong>đôi một song song</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "slug": "duong-thang-va-mat-phang-song-song",
                "title": "Bài 3: Đường thẳng song song với mặt phẳng",
                "objectives": [
                    "Dấu hiệu nhận biết đường thẳng song song với mặt phẳng.",
                    "Tính chất và định lí giao tuyến liên quan."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Dấu hiệu nhận biết đường thẳng song song mặt phẳng</h4>
    <div class="formula-card alert alert-success">
        $$\left.\begin{array}{l} d \not\subset (\alpha) \\ d' \subset (\alpha) \\ d // d' \end{array}\right\} \implies d // (\alpha)$$
    </div>
    <p><em>Quy tắc vàng: Để chứng minh một đường thẳng song song với một mặt phẳng, ta chỉ cần chứng minh nó song song với một đường thẳng nằm trong mặt phẳng đó!</em></p>

    <h4>2. Tính chất giao tuyến</h4>
    <p>Nếu đường thẳng $d // (\alpha)$, mặt phẳng $(\beta)$ chứa $d$ cắt $(\alpha)$ theo giao tuyến $d'$ thì:</p>
    $$d // d'$$
</div>
"""
            },
            {
                "id": 4,
                "slug": "hai-mat-phang-song-song",
                "title": "Bài 4: Hai mặt phẳng song song",
                "objectives": [
                    "Dấu hiệu nhận biết hai mặt phẳng song song.",
                    "Định lí Thales trong không gian.",
                    "Khái niệm hình lăng trụ, hình hộp."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Dấu hiệu nhận biết hai mặt phẳng song song</h4>
    <div class="formula-card alert alert-success">
        $$\left.\begin{array}{l} a, b \subset (\alpha), a \cap b = \{I\} \\ a // (\beta) \\ b // (\beta) \end{array}\right\} \implies (\alpha) // (\beta)$$
    </div>
    <p><em>Nếu mặt phẳng $(\alpha)$ chứa hai đường thẳng cắt nhau cùng song song với mặt phẳng $(\beta)$ thì $(\alpha) // (\beta)$.</em></p>

    <h4>2. Hình lăng trụ và hình hộp</h4>
    <ul>
        <li><strong>Hình lăng trụ:</strong> có 2 đáy là 2 đa giác bằng nhau nằm trên 2 mp song song, các mặt bên là các hình bình hành, các cạnh bên song song và bằng nhau.</li>
        <li><strong>Hình hộp:</strong> là hình lăng trụ có đáy là hình bình hành (tất cả 6 mặt đều là hình bình hành).</li>
    </ul>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 4: Song song trong không gian",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Trong không gian, qua 3 điểm phân biệt không thẳng hàng ta xác định được bao nhiêu mặt phẳng?",
                    "options": ["A. Vô số", "B. 2", "C. Duy nhất 1", "D. 3"],
                    "correct": 2,
                    "explanation": r"Theo tiên đề hình học không gian, có một và chỉ một mặt phẳng đi qua 3 điểm phân biệt không thẳng hàng."
                },
                {
                    "id": 2,
                    "question": r"Hai đường thẳng không có điểm chung và không cùng nằm trên bất kì mặt phẳng nào được gọi là:",
                    "options": [
                        "A. Hai đường thẳng song song",
                        "B. Hai đường thẳng cắt nhau",
                        "C. Hai đường thẳng chéo nhau",
                        "D. Hai đường thẳng trùng nhau"
                    ],
                    "correct": 2,
                    "explanation": r"Theo định nghĩa, hai đường thẳng chéo nhau là hai đường thẳng không đồng phẳng (không cùng nằm trong một mặt phẳng)."
                },
                {
                    "id": 3,
                    "question": r"Để chứng minh đường thẳng $d$ song song với mặt phẳng $(P)$, ta cần chỉ ra:",
                    "options": [
                        "A. $d$ song song với mọi đường thẳng nằm trong $(P)$",
                        "B. $d$ không nằm trong $(P)$ và song song với một đường thẳng $d'$ nằm trong $(P)$",
                        "C. $d$ cắt một đường thẳng nằm trong $(P)$",
                        "D. $d$ có một điểm chung với $(P)$"
                    ],
                    "correct": 1,
                    "explanation": r"Định lí: Nếu đường thẳng $d$ không nằm trong $(P)$ và song song với đường thẳng $d'$ nằm trong $(P)$ thì $d // (P)$."
                },
                {
                    "id": 4,
                    "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là:",
                    "options": [
                        "A. Đường thẳng qua $S$ và song song với $AB, CD$",
                        "B. Đường thẳng $SO$ với $O$ là tâm hình bình hành",
                        "C. Đường thẳng $SA$",
                        "D. Đường thẳng $SC$"
                    ],
                    "correct": 0,
                    "explanation": r"Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AB // CD$, nên giao tuyến của chúng là đường thẳng đi qua $S$ và song song với $AB, CD$."
                },
                {
                    "id": 5,
                    "question": r"Nếu mặt phẳng $(\alpha)$ song song với mặt phẳng $(\beta)$ thì mọi đường thẳng nằm trong $(\alpha)$ sẽ:",
                    "options": [
                        r"A. Cắt $(\beta)$",
                        r"B. Song song với $(\beta)$",
                        r"C. Trùng với $(\beta)$",
                        r"D. Chéo với $(\beta)$"
                    ],
                    "correct": 1,
                    "explanation": r"Vì $(\alpha) // (\beta)$ nên $(\alpha)$ và $(\beta)$ không có điểm chung. Do đó mọi đường thẳng $d \subset (\alpha)$ không có điểm chung với $(\beta)$, suy ra $d // (\beta)$."
                },
                {
                    "id": 6,
                    "question": r"Hình chóp tứ giác $S.ABCD$ có bao nhiêu mặt bên?",
                    "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
                    "correct": 1,
                    "explanation": r"Hình chóp tứ giác có 1 mặt đáy và 4 mặt bên là $(SAB), (SBC), (SCD), (SDA)$."
                },
                {
                    "id": 7,
                    "question": r"Tất cả các mặt bên của một hình lăng trụ đều là:",
                    "options": [
                        "A. Hình tam giác",
                        "B. Hình chữ nhật",
                        "C. Hình bình hành",
                        "D. Hình vuông"
                    ],
                    "correct": 2,
                    "explanation": r"Theo định nghĩa hình lăng trụ, các mặt bên của hình lăng trụ luôn là các hình bình hành."
                },
                {
                    "id": 8,
                    "question": r"Cho hình hộp $ABCD.A'B'C'D'$. Mặt phẳng $(ABCD)$ song song với mặt phẳng nào sau đây?",
                    "options": ["A. $(ABB'A')$", "B. $(A'B'C'D')$", "C. $(BCC'B')$", "D. $(ACC'A')$"],
                    "correct": 1,
                    "explanation": r"Trong hình hộp, hai mặt đáy $(ABCD)$ và $(A'B'C'D')$ song song với nhau."
                }
            ]
        }
    },
    {
        "id": 5,
        "volume": 1,
        "slug": "gioi-han-ham-so-lien-tuc",
        "title": "Chương 5: Giới hạn. Hàm số liên tục",
        "short_title": "Chương 5: Giới hạn & Liên tục",
        "badge": "Đại số & Giải tích",
        "icon": "bi-infinity",
        "color": "rose",
        "summary": r"Giới hạn của dãy số, tổng cấp số nhân lùi vô hạn. Giới hạn của hàm số tại một điểm, tại vô cực, các dạng vô định $\\frac{0}{0}, \\frac{\\infty}{\\infty}, \\infty-\\infty$ và tính liên tục của hàm số.",
        "lessons": [
            {
                "id": 1,
                "slug": "gioi-han-day-so",
                "title": "Bài 1: Giới hạn của dãy số",
                "objectives": [
                    r"Các giới hạn cơ bản: $\\lim \\frac{1}{n^k} = 0$, $\\lim q^n = 0$ ($|q| < 1$).",
                    "Các phép toán giới hạn tổng, hiệu, tích, thương.",
                    r"Tổng cấp số nhân lùi vô hạn $S = \\frac{u_1}{1 - q}$."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Các giới hạn cơ bản</h4>
    <div class="formula-card">
        $$\lim_{n \to \infty} \frac{1}{n^k} = 0 \quad (k > 0)$$
        $$\lim_{n \to \infty} q^n = 0 \quad (|q| < 1)$$
        $$\lim_{n \to \infty} c = c \quad (c \text{ là hằng số})$$
    </div>

    <h4>2. Tổng cấp số nhân lùi vô hạn</h4>
    <p>Cấp số nhân $(u_n)$ có công bội $q$ thỏa mãn $|q| < 1$ được gọi là cấp số nhân lùi vô hạn. Tổng của nó:</p>
    <div class="formula-card alert alert-primary">
        $$S = u_1 + u_2 + \dots + u_n + \dots = \frac{u_1}{1 - q}$$
    </div>

    <div class="example-box">
        <h5 class="text-primary"><i class="bi bi-pencil-fill"></i> Ví dụ</h5>
        <p><strong>Tính:</strong> $S = 1 + \frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2^n} + \dots$</p>
        <p><strong>Giải:</strong> Đây là CSN lùi vô hạn với $u_1 = 1$, $q = \frac{1}{2}$. Tổng $S = \frac{1}{1 - 1/2} = 2$.</p>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "gioi-han-ham-so",
                "title": "Bài 2: Giới hạn của hàm số và các dạng vô định",
                "objectives": [
                    "Giới hạn hữu hạn tại một điểm và giới hạn tại vô cực.",
                    r"Giới hạn một bên: bên trái ($x \to x_0^-$) và bên phải ($x \to x_0^+$).",
                    r"Phương pháp khử các dạng vô định $\\frac{0}{0}, \\frac{\\infty}{\\infty}, \\infty - \\infty$."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Giới hạn một bên</h4>
    <div class="formula-card">
        $$\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L$$
    </div>

    <h4>2. Các phương pháp khử dạng vô định</h4>
    <div class="table-responsive">
        <table class="table table-bordered bg-white">
            <thead class="table-danger">
                <tr><th>Dạng vô định</th><th>Phương pháp giải đặc trưng</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>$\frac{0}{0}$</strong></td>
                    <td>
                        <ul>
                            <li>Phân tích đa thức thành nhân tử để triệt tiêu $(x - x_0)$.</li>
                            <li>Nhân liên hợp nếu chứa căn thức: $(\sqrt{A} - \sqrt{B})(\sqrt{A} + \sqrt{B}) = A - B$.</li>
                        </ul>
                    </td>
                </tr>
                <tr>
                    <td><strong>$\frac{\infty}{\infty}$</strong></td>
                    <td>Đặt lũy thừa bậc cao nhất của tử và mẫu ra ngoài rồi rút gọn.</td>
                </tr>
                <tr>
                    <td><strong>$\infty - \infty$</strong></td>
                    <td>Nhân lượng liên hợp để chuyển về dạng $\frac{\infty}{\infty}$ hoặc $\frac{C}{\infty} = 0$.</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "ham-so-lien-tuc",
                "title": "Bài 3: Hàm số liên tục",
                "objectives": [
                    r"Khái niệm hàm số liên tục tại điểm $x_0$: $\\lim_{x \\to x_0} f(x) = f(x_0)$.",
                    "Hàm số liên tục trên khoảng, đoạn.",
                    "Định lí Bolzano (giá trị trung gian) chứng minh phương trình có nghiệm."
                ],
                "content": r"""
<div class="theory-section">
    <h4>1. Hàm số liên tục tại một điểm</h4>
    <div class="formula-card">
        <p>Hàm số $y = f(x)$ liên tục tại $x_0 \in (a; b) \iff$</p>
        $$\lim_{x \to x_0} f(x) = f(x_0)$$
    </div>

    <h4>2. Tính liên tục của các hàm sơ cấp</h4>
    <p>Các hàm đa thức, phân thức hữu tỉ, lượng giác liên tục trên từng khoảng xác định của chúng.</p>

    <h4>3. Định lí giá trị trung gian (Định lí Bolzano)</h4>
    <div class="formula-card alert alert-success">
        <p>Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \cdot f(b) < 0$ thì tồn tại ít nhất một điểm $c \in (a; b)$ sao cho:</p>
        $$f(c) = 0$$
        <p class="mb-0 text-muted"><em>Ứng dụng: Chứng minh phương trình có ít nhất một nghiệm trên khoảng $(a; b)$.</em></p>
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 5: Giới hạn & Hàm số liên tục",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Giá trị của $\lim_{n \to \infty} \frac{2n + 1}{n + 3}$ bằng:",
                    "options": ["A. 2", r"B. $\frac{1}{3}$", r"C. $+\infty$", "D. 0"],
                    "correct": 0,
                    "explanation": r"Chia cả tử và mẫu cho $n$: $\lim \frac{2 + 1/n}{1 + 3/n} = \frac{2 + 0}{1 + 0} = 2$."
                },
                {
                    "id": 2,
                    "question": r"Tổng của cấp số nhân lùi vô hạn $1 + \frac{1}{3} + \frac{1}{9} + \dots + \frac{1}{3^n} + \dots$ bằng:",
                    "options": [r"A. $\frac{3}{2}$", "B. 2", r"C. $\frac{2}{3}$", r"D. $\frac{4}{3}$"],
                    "correct": 0,
                    "explanation": r"Ta có $u_1 = 1$, công bội $q = \frac{1}{3}$. Tổng $S = \frac{u_1}{1 - q} = \frac{1}{1 - 1/3} = \frac{3}{2}$."
                },
                {
                    "id": 3,
                    "question": r"Giá trị của $\lim_{x \to 2} (x^2 - 3x + 5)$ bằng:",
                    "options": ["A. 3", "B. 5", "C. 7", "D. 1"],
                    "correct": 0,
                    "explanation": r"Thay trực tiếp $x = 2$: $2^2 - 3(2) + 5 = 4 - 6 + 5 = 3$."
                },
                {
                    "id": 4,
                    "question": r"Giá trị của giới hạn dạng vô định $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$ bằng:",
                    "options": ["A. 0", "B. 1", "C. 2", "D. Không tồn tại"],
                    "correct": 2,
                    "explanation": r"$\lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = \lim_{x \to 1} (x+1) = 1 + 1 = 2$."
                },
                {
                    "id": 5,
                    "question": r"Cho $\lim_{x \to 1^+} f(x) = 3$ và $\lim_{x \to 1^-} f(x) = 3$. Khi đó $\lim_{x \to 1} f(x)$ bằng:",
                    "options": ["A. 6", "B. 3", "C. 0", "D. Không tồn tại"],
                    "correct": 1,
                    "explanation": r"Vì giới hạn bên trái bằng giới hạn bên phải và bằng 3 nên giới hạn tại điểm đó bằng 3."
                },
                {
                    "id": 6,
                    "question": r"Hàm số $y = \frac{1}{x - 2}$ gián đoạn tại điểm nào?",
                    "options": ["A. $x = 0$", "B. $x = 2$", "C. $x = -2$", "D. $x = 1$"],
                    "correct": 1,
                    "explanation": r"Hàm số không xác định tại $x = 2$, do đó hàm số gián đoạn tại điểm $x = 2$."
                },
                {
                    "id": 7,
                    "question": r"Nếu hàm số $f(x)$ liên tục trên $[0; 2]$ và $f(0) = -3, f(2) = 5$, phương trình $f(x) = 0$ có ít nhất bao nhiêu nghiệm trong khoảng $(0; 2)$?",
                    "options": ["A. 0 nghiệm", "B. 1 nghiệm", "C. 2 nghiệm", "D. 3 nghiệm"],
                    "correct": 1,
                    "explanation": r"Vì $f(0) \cdot f(2) = (-3) \cdot 5 = -15 < 0$, theo định lí Bolzano, phương trình $f(x) = 0$ có ít nhất 1 nghiệm trong khoảng $(0; 2)$."
                },
                {
                    "id": 8,
                    "question": r"Giá trị của $\lim_{x \to +\infty} \frac{3x^2 - x + 1}{x^2 + 4}$ bằng:",
                    "options": ["A. 0", "B. 3", r"C. $+\infty$", r"D. $\frac{1}{4}$"],
                    "correct": 1,
                    "explanation": r"Bậc cao nhất ở tử và mẫu cùng là $x^2$, hệ số tương ứng là 3 và 1. Giới hạn bằng $\frac{3}{1} = 3$."
                }
            ]
        }
    }
]
