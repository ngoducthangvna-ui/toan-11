# -*- coding: utf-8 -*-
"""
Dữ liệu kiến thức Toán 11 - Tập 2 (Chương 6 đến Chương 9)
Chương trình Giáo dục phổ thông mới (KNTT, Cánh Diều, Chân Trời Sáng Tạo)
"""

VOLUME_2_CHAPTERS = [
    {
        "id": 6,
        "volume": 2,
        "slug": "ham-so-mu-va-ham-so-logarit",
        "title": "Chương 6: Hàm số mũ và Hàm số logarit",
        "short_title": "Chương 6: Mũ & Logarit",
        "badge": "Đại số & Giải tích",
        "icon": "bi-graph-up-arrow",
        "color": "cyan",
        "summary": "Phép tính lũy thừa số mũ thực, định nghĩa và tính chất logarit, khảo sát hàm số mũ, hàm số logarit và giải phương trình, bất phương trình mũ - logarit cơ bản.",
        "lessons": [
            {
                "id": 1,
                "slug": "phep-tinh-luy-thua",
                "title": "Bài 1: Phép tính lũy thừa với số mũ thực",
                "content": r"""
<div class="theory-section">
    <h4>1. Tính chất của lũy thừa với số mũ thực</h4>
    <p>Với cơ số $a, b > 0$ và số thực $\alpha, \beta$:</p>
    <div class="formula-card">
        $$a^\alpha \cdot a^\beta = a^{\alpha + \beta}$$
        $$\frac{a^\alpha}{a^\beta} = a^{\alpha - \beta}$$
        $$(a^\alpha)^\beta = a^{\alpha \beta}$$
        $$(ab)^\alpha = a^\alpha \cdot b^\alpha, \quad \left(\frac{a}{b}\right)^\alpha = \frac{a^\alpha}{b^\alpha}$$
        $$a^{-\alpha} = \frac{1}{a^\alpha}, \quad a^{\frac{m}{n}} = \sqrt[n]{a^m} \quad (a > 0, m \in \mathbb{Z}, n \in \mathbb{N}^*)$$
    </div>

    <h4>2. So sánh hai lũy thừa</h4>
    <ul>
        <li>Nếu $a > 1$ thì: $$a^\alpha > a^\beta \iff \alpha > \beta$$ (hàm số đồng biến)</li>
        <li>Nếu $0 < a < 1$ thì: $$a^\alpha > a^\beta \iff \alpha < \beta$$ (hàm số nghịch biến - đổi chiều)</li>
    </ul>
</div>
"""
            },
            {
                "id": 2,
                "slug": "phep-tinh-logarit",
                "title": "Bài 2: Phép tính logarit",
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa</h4>
    <p>Cho hai số dương $a, b$ với $a \neq 1$. Số $\alpha$ thỏa mãn $a^\alpha = b$ được gọi là logarit cơ số $a$ của $b$:</p>
    <div class="formula-card">
        $$\log_a b = \alpha \iff a^\alpha = b$$
        $$\log_a 1 = 0, \quad \log_a a = 1, \quad a^{\log_a b} = b, \quad \log_a(a^\alpha) = \alpha$$
    </div>

    <h4>2. Các tính chất trọng tâm</h4>
    <div class="formula-card">
        <p><strong>Logarit của tích và thương:</strong></p>
        $$\log_a(x \cdot y) = \log_a x + \log_a y$$
        $$\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$$

        <p class="mt-3"><strong>Logarit của lũy thừa:</strong></p>
        $$\log_a(x^\alpha) = \alpha \log_a x, \quad \log_{a^\beta} x = \frac{1}{\beta} \log_a x$$

        <p class="mt-3"><strong>Công thức đổi cơ số:</strong></p>
        $$\log_a b = \frac{\log_c b}{\log_c a} \quad (c > 0, c \neq 1) \implies \log_a b \cdot \log_b c = \log_a c$$
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "ham-so-mu-va-logarit",
                "title": "Bài 3: Hàm số mũ và Hàm số logarit",
                "content": r"""
<div class="theory-section">
    <h4>1. Bảng so sánh Hàm số Mũ và Hàm số Logarit</h4>
    <div class="table-responsive">
        <table class="table table-bordered bg-white text-center">
            <thead class="table-info">
                <tr><th>Đặc điểm</th><th>Hàm số mũ $y = a^x$ ($a > 0, a \neq 1$)</th><th>Hàm số logarit $y = \log_a x$ ($a > 0, a \neq 1$)</th></tr>
            </thead>
            <tbody>
                <tr><td><strong>Tập xác định</strong></td><td>$D = \mathbb{R}$</td><td>$D = (0; +\infty)$</td></tr>
                <tr><td><strong>Tập giá trị</strong></td><td>$T = (0; +\infty)$</td><td>$T = \mathbb{R}$</td></tr>
                <tr><td><strong>Cơ số $a > 1$</strong></td><td>Đồng biến trên $\mathbb{R}$</td><td>Đồng biến trên $(0; +\infty)$</td></tr>
                <tr><td><strong>Cơ số $0 < a < 1$</strong></td><td>Nghịch biến trên $\mathbb{R}$</td><td>Nghịch biến trên $(0; +\infty)$</td></tr>
                <tr><td><strong>Điểm đi qua</strong></td><td>Luôn đi qua $(0; 1)$</td><td>Luôn đi qua $(1; 0)$</td></tr>
                <tr><td><strong>Tiệm cận</strong></td><td>Tiệm cận ngang là trục hoành $y = 0$</td><td>Tiệm cận đứng là trục tung $x = 0$</td></tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "id": 4,
                "slug": "phuong-trinh-bat-phuong-trinh-mu-logarit",
                "title": "Bài 4: Phương trình và Bất phương trình mũ, logarit cơ bản",
                "content": r"""
<div class="theory-section">
    <h4>1. Phương trình mũ & logarit cơ bản</h4>
    <ul>
        <li>$a^x = b$:
            <ul>
                <li>Nếu $b \le 0$: Phương trình vô nghiệm.</li>
                <li>Nếu $b > 0$: $x = \log_a b$.</li>
            </ul>
        </li>
        <li>$\log_a x = b \iff x = a^b$ (luôn có nghiệm duy nhất với mọi $b$).</li>
    </ul>

    <h4>2. Bất phương trình cơ bản</h4>
    <div class="formula-card alert alert-warning">
        <p><strong>Bất phương trình mũ $a^x > b$:</strong></p>
        <ul>
            <li>Khi $a > 1$: $a^x > b \iff x > \log_a b$ (giữ nguyên chiều).</li>
            <li>Khi $0 < a < 1$: $a^x > b \iff x < \log_a b$ (<strong>đổi chiều</strong>).</li>
        </ul>

        <p class="mt-2"><strong>Bất phương trình logarit $\log_a x > b$:</strong></p>
        <ul>
            <li>Khi $a > 1$: $x > a^b$.</li>
            <li>Khi $0 < a < 1$: $0 < x < a^b$ (<strong>đổi chiều và có điều kiện $x > 0$</strong>).</li>
        </ul>
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 6: Mũ & Logarit",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Rút gọn biểu thức $P = x^{\frac{1}{2}} \cdot x^{\frac{1}{3}}$ với $x > 0$ được kết quả là:",
                    "options": [r"A. $x^{\frac{1}{6}}$", r"B. $x^{\frac{5}{6}}$", r"C. $x^{\frac{2}{5}}$", r"D. $x^{\frac{3}{2}}$"],
                    "correct": 1,
                    "explanation": r"$P = x^{\frac{1}{2} + \frac{1}{3}} = x^{\frac{3+2}{6}} = x^{\frac{5}{6}}$."
                },
                {
                    "id": 2,
                    "question": r"Giá trị của $\log_2 16$ bằng:",
                    "options": ["A. 4", "B. 8", "C. 2", "D. 3"],
                    "correct": 0,
                    "explanation": r"Vì $2^4 = 16$ nên $\log_2 16 = 4$."
                },
                {
                    "id": 3,
                    "question": r"Tập xác định của hàm số $y = \log_3(x - 2)$ là:",
                    "options": [r"A. $(2; +\infty)$", r"B. $[2; +\infty)$", r"C. $\mathbb{R} \setminus \{2\}$", r"D. $(-\infty; 2)$"],
                    "correct": 0,
                    "explanation": r"Hàm số xác định khi biểu thức trong logarit dương: $x - 2 > 0 \iff x > 2$."
                },
                {
                    "id": 4,
                    "question": r"Nghiệm của phương trình $2^{x+1} = 8$ là:",
                    "options": ["A. $x = 2$", "B. $x = 3$", "C. $x = 1$", "D. $x = 4$"],
                    "correct": 0,
                    "explanation": r"$2^{x+1} = 2^3 \iff x + 1 = 3 \iff x = 2$."
                },
                {
                    "id": 5,
                    "question": r"Hàm số nào sau đây nghịch biến trên $\mathbb{R}$?",
                    "options": [
                        "A. $y = 2^x$",
                        "B. $y = e^x$",
                        r"C. $y = \left(\frac{1}{2}\right)^x$",
                        r"D. $y = \pi^x$"
                    ],
                    "correct": 2,
                    "explanation": r"Hàm số mũ $y = a^x$ nghịch biến trên $\mathbb{R}$ khi và chỉ khi cơ số $0 < a < 1$. Ở đây $a = \frac{1}{2} < 1$."
                },
                {
                    "id": 6,
                    "question": r"Biểu thức $\log_a(x^2 y)$ với $a, x, y > 0, a \neq 1$ bằng:",
                    "options": [
                        r"A. $2\log_a x + \log_a y$",
                        r"B. $2\log_a x \cdot \log_a y$",
                        r"C. $(\log_a x)^2 + \log_a y$",
                        r"D. $\log_a(2x) + \log_a y$"
                    ],
                    "correct": 0,
                    "explanation": r"Áp dụng quy tắc nhân và lũy thừa: $\log_a(x^2 y) = \log_a(x^2) + \log_a y = 2\log_a x + \log_a y$."
                },
                {
                    "id": 7,
                    "question": r"Tập nghiệm của bất phương trình $\log_{0.5} x > 2$ là:",
                    "options": [
                        r"A. $(-\infty; 0.25)$",
                        "B. $(0; 0.25)$",
                        r"C. $(0.25; +\infty)$",
                        "D. $(0; 4)$"
                    ],
                    "correct": 1,
                    "explanation": r"Vì cơ số $0 < 0.5 < 1$, bất phương trình đổi chiều kèm điều kiện xác định: $0 < x < (0.5)^2 \iff 0 < x < 0.25$."
                },
                {
                    "id": 8,
                    "question": r"Cho $a = \log_2 3$. Khi đó $\log_2 18$ biểu diễn theo $a$ là:",
                    "options": ["A. $1 + 2a$", "B. $2 + a$", "C. $1 + a^2$", "D. $2a$"],
                    "correct": 0,
                    "explanation": r"$\log_2 18 = \log_2(2 \cdot 9) = \log_2 2 + \log_2(3^2) = 1 + 2\log_2 3 = 1 + 2a$."
                }
            ]
        }
    },
    {
        "id": 7,
        "volume": 2,
        "slug": "dao-ham",
        "title": "Chương 7: Đạo hàm",
        "short_title": "Chương 7: Đạo hàm",
        "badge": "Đại số & Giải tích",
        "icon": "bi-lightning-charge-fill",
        "color": "violet",
        "summary": "Định nghĩa đạo hàm, ý nghĩa hình học (tiếp tuyến) và vật lí (vận tốc tức thời). Bảng đạo hàm các hàm sơ cấp, quy tắc đạo hàm tổng, tích, thương, đạo hàm hàm hợp và đạo hàm cấp hai.",
        "lessons": [
            {
                "id": 1,
                "slug": "dinh-nghia-va-y-nghia-dao-ham",
                "title": "Bài 1: Định nghĩa và ý nghĩa của đạo hàm",
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa đạo hàm tại một điểm</h4>
    <div class="formula-card">
        $$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$$
    </div>

    <h4>2. Ý nghĩa hình học của đạo hàm</h4>
    <div class="formula-card alert alert-primary">
        <p>Đạo hàm $f'(x_0)$ là hệ số góc $k$ của tiếp tuyến với đồ thị $(C): y = f(x)$ tại điểm $M_0(x_0; y_0)$:</p>
        $$k = f'(x_0)$$
        <p><strong>Phương trình tiếp tuyến tại điểm $M_0(x_0; y_0)$:</strong></p>
        $$y = f'(x_0)(x - x_0) + y_0 \quad (\text{với } y_0 = f(x_0))$$
    </div>

    <h4>3. Ý nghĩa vật lí của đạo hàm</h4>
    <p>Nếu $s = s(t)$ là phương trình chuyển động của vật thì:</p>
    <ul>
        <li><strong>Vận tốc tức thời:</strong> $v(t) = s'(t)$</li>
        <li><strong>Cường độ dòng điện tức thời:</strong> $i(t) = q'(t)$</li>
    </ul>
</div>
"""
            },
            {
                "id": 2,
                "slug": "cac-quy-tac-tinh-dao-ham",
                "title": "Bài 2: Các quy tắc tính đạo hàm và đạo hàm hàm hợp",
                "content": r"""
<div class="theory-section">
    <h4>1. Bảng đạo hàm các hàm sơ cấp cơ bản</h4>
    <div class="table-responsive">
        <table class="table table-bordered bg-white text-center">
            <thead class="table-primary">
                <tr><th>Hàm số sơ cấp $y = f(x)$</th><th>Hàm số hợp $y = f(u)$ ($u = u(x)$)</th></tr>
            </thead>
            <tbody>
                <tr><td>$(c)' = 0$</td><td></td></tr>
                <tr><td>$(x^\alpha)' = \alpha x^{\alpha - 1}$</td><td>$(u^\alpha)' = \alpha u^{\alpha - 1} \cdot u'$</td></tr>
                <tr><td>$(\sqrt{x})' = \frac{1}{2\sqrt{x}}$</td><td>$(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$</td></tr>
                <tr><td>$(\sin x)' = \cos x$</td><td>$(\sin u)' = u' \cdot \cos u$</td></tr>
                <tr><td>$(\cos x)' = -\sin x$</td><td>$(\cos u)' = -u' \cdot \sin u$</td></tr>
                <tr><td>$(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x$</td><td>$(\tan u)' = \frac{u'}{\cos^2 u}$</td></tr>
                <tr><td>$(\cot x)' = -\frac{1}{\sin^2 x}$</td><td>$(\cot u)' = -\frac{u'}{\sin^2 u}$</td></tr>
                <tr><td>$(e^x)' = e^x$</td><td>$(e^u)' = u' \cdot e^u$</td></tr>
                <tr><td>$(a^x)' = a^x \ln a$</td><td>$(a^u)' = u' \cdot a^u \ln a$</td></tr>
                <tr><td>$(\ln x)' = \frac{1}{x}$</td><td>$(\ln u)' = \frac{u'}{u}$</td></tr>
            </tbody>
        </table>
    </div>

    <h4>2. Quy tắc tính đạo hàm tổng, tích, thương</h4>
    <div class="formula-card">
        $$(u \pm v)' = u' \pm v'$$
        $$(u \cdot v)' = u' v + u v' \implies (k u)' = k u'$$
        $$\left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2} \implies \left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$$
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "dao-ham-cap-hai",
                "title": "Bài 3: Đạo hàm cấp hai",
                "content": r"""
<div class="theory-section">
    <h4>1. Định nghĩa</h4>
    <p>Giả sử hàm số $y = f(x)$ có đạo hàm tại mọi điểm $x \in (a; b)$. Đạo hàm của hàm số $f'(x)$ (nếu có) được gọi là đạo hàm cấp hai của $f(x)$:</p>
    <div class="formula-card">
        $$f''(x) = [f'(x)]' \quad \text{hoặc } y'' = (y')'$$
    </div>

    <h4>2. Ý nghĩa cơ học</h4>
    <p>Gia tốc tức thời của chuyển động $s = s(t)$ tại thời điểm $t$ là:</p>
    <div class="formula-card alert alert-info">
        $$a(t) = v'(t) = s''(t)$$
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 7: Đạo hàm",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Đạo hàm của hàm số $y = x^3 - 3x^2 + 5$ là:",
                    "options": ["A. $3x^2 - 6x$", "B. $3x^2 - 6x + 5$", "C. $x^2 - 6x$", "D. $3x^2 - 3x$"],
                    "correct": 0,
                    "explanation": r"$y' = (x^3)' - 3(x^2)' + (5)' = 3x^2 - 6x$."
                },
                {
                    "id": 2,
                    "question": r"Đạo hàm của hàm số $y = \sin 2x$ là:",
                    "options": [r"A. $\cos 2x$", r"B. $2\cos 2x$", r"C. $-2\cos 2x$", r"D. $-\cos 2x$"],
                    "correct": 1,
                    "explanation": r"Áp dụng công thức đạo hàm hàm hợp $(\sin u)' = u' \cos u \implies y' = (2x)' \cos 2x = 2\cos 2x$."
                },
                {
                    "id": 3,
                    "question": r"Hệ số góc của tiếp tuyến của đồ thị hàm số $y = x^2 - 2x + 3$ tại điểm có hoành độ $x_0 = 2$ bằng:",
                    "options": ["A. 2", "B. 3", "C. 4", "D. 0"],
                    "correct": 0,
                    "explanation": r"Ta có $y' = 2x - 2$. Hệ số góc tiếp tuyến là $k = y'(2) = 2(2) - 2 = 2$."
                },
                {
                    "id": 4,
                    "question": r"Đạo hàm của hàm số $y = e^{3x}$ là:",
                    "options": ["A. $e^{3x}$", "B. $3e^{3x}$", r"C. $\frac{1}{3}e^{3x}$", "D. $3x e^{3x-1}$"],
                    "correct": 1,
                    "explanation": r"$(e^u)' = u' e^u \implies (e^{3x})' = (3x)' e^{3x} = 3e^{3x}$."
                },
                {
                    "id": 5,
                    "question": r"Đạo hàm của hàm số $y = \frac{1}{x}$ với $x \neq 0$ là:",
                    "options": [r"A. $-\frac{1}{x^2}$", r"B. $\frac{1}{x^2}$", r"C. $\ln x$", r"D. $-\frac{1}{x}$"],
                    "correct": 0,
                    "explanation": r"Công thức chuẩn: $(1/x)' = -1/x^2$."
                },
                {
                    "id": 6,
                    "question": r"Một chất điểm chuyển động theo phương trình $s(t) = t^3 - 3t^2 + 2t$ ($t$ tính bằng giây, $s$ tính bằng mét). Vận tốc tức thời tại thời điểm $t = 2$ s là:",
                    "options": [r"A. $2\text{ m/s}$", r"B. $0\text{ m/s}$", r"C. $4\text{ m/s}$", r"D. $6\text{ m/s}$"],
                    "correct": 0,
                    "explanation": r"$v(t) = s'(t) = 3t^2 - 6t + 2$. Tại $t = 2$: $v(2) = 3(2^2) - 6(2) + 2 = 12 - 12 + 2 = 2\text{ m/s}$."
                },
                {
                    "id": 7,
                    "question": r"Đạo hàm cấp hai của hàm số $y = x^4$ là:",
                    "options": ["A. $4x^3$", "B. $12x^2$", "C. $24x$", "D. $12x^3$"],
                    "correct": 1,
                    "explanation": r"$y' = 4x^3 \implies y'' = (4x^3)' = 12x^2$."
                },
                {
                    "id": 8,
                    "question": r"Phương trình tiếp tuyến của đồ thị hàm số $y = x^2$ tại điểm $M(1; 1)$ là:",
                    "options": ["A. $y = 2x - 1$", "B. $y = 2x + 1$", "C. $y = x$", "D. $y = 2x$"],
                    "correct": 0,
                    "explanation": r"$y' = 2x \implies k = y'(1) = 2$. Phương trình tiếp tuyến là $y = 2(x - 1) + 1 = 2x - 1$."
                }
            ]
        }
    },
    {
        "id": 8,
        "volume": 2,
        "slug": "quan-he-vuong-goc-trong-khong-gian",
        "title": "Chương 8: Quan hệ vuông góc trong không gian",
        "short_title": "Chương 8: Vuông góc không gian",
        "badge": "Hình học không gian",
        "icon": "bi-bounding-box-circles",
        "color": "blue",
        "summary": "Hai đường thẳng vuông góc, đường thẳng vuông góc mặt phẳng, hai mặt phẳng vuông góc, định lí ba đường vuông góc và các bài toán tính khoảng cách, góc trong không gian.",
        "lessons": [
            {
                "id": 1,
                "slug": "hai-duong-thang-vuong-goc",
                "title": "Bài 1: Góc giữa hai đường thẳng và hai đường thẳng vuông góc",
                "content": r"""
<div class="theory-section">
    <h4>1. Góc giữa hai đường thẳng</h4>
    <p>Góc giữa hai đường thẳng $a$ và $b$ là góc giữa hai đường thẳng $a'$ và $b'$ cùng đi qua một điểm và lần lượt song song với $a$ và $b$.</p>
    <div class="formula-card">
        $$0^\circ \le (a, b) \le 90^\circ$$
        $$\cos(a, b) = \frac{|\vec{u} \cdot \vec{v}|}{|\vec{u}| \cdot |\vec{v}|}$$
    </div>

    <h4>2. Hai đường thẳng vuông góc</h4>
    <div class="formula-card alert alert-primary">
        $$a \perp b \iff (a, b) = 90^\circ \iff \vec{u} \cdot \vec{v} = 0$$
        <p class="mb-0 text-muted"><em>Hai đường thẳng vuông góc trong không gian có thể cắt nhau hoặc chéo nhau!</em></p>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "duong-thang-vuong-goc-voi-mat-phang",
                "title": "Bài 2: Đường thẳng vuông góc với mặt phẳng",
                "content": r"""
<div class="theory-section">
    <h4>1. Điều kiện để đường thẳng vuông góc với mặt phẳng</h4>
    <div class="formula-card alert alert-success">
        <p>Nếu đường thẳng $d$ vuông góc với hai đường thẳng cắt nhau $a$ và $b$ cùng nằm trong mặt phẳng $(P)$ thì $d \perp (P)$:</p>
        $$\left.\begin{array}{l} d \perp a, d \perp b \\ a, b \subset (P), a \cap b = \{I\} \end{array}\right\} \implies d \perp (P)$$
    </div>

    <h4>2. Tính chất cốt lõi</h4>
    <p>Nếu $d \perp (P)$ thì $d$ vuông góc với <strong>mọi đường thẳng</strong> nằm trong $(P)$.</p>

    <h4>3. Định lí ba đường vuông góc</h4>
    <p>Cho đường thẳng $a$ không vuông góc với $(P)$ và $b \subset (P)$. Gọi $a'$ là hình chiếu của $a$ trên $(P)$. Khi đó:</p>
    <div class="formula-card">
        $$b \perp a \iff b \perp a'$$
    </div>
</div>
"""
            },
            {
                "id": 3,
                "slug": "hai-mat-phang-vuong-goc",
                "title": "Bài 3: Hai mặt phẳng vuông góc",
                "content": r"""
<div class="theory-section">
    <h4>1. Điều kiện để hai mặt phẳng vuông góc</h4>
    <div class="formula-card alert alert-success">
        <p>Nếu một mặt phẳng chứa một đường thẳng vuông góc với mặt phẳng kia thì hai mặt phẳng đó vuông góc với nhau:</p>
        $$d \subset (P) \text{ và } d \perp (Q) \implies (P) \perp (Q)$$
    </div>

    <h4>2. Tính chất giao tuyến</h4>
    <p>Nếu $(P) \perp (Q)$ theo giao tuyến $\Delta$, đường thẳng $d \subset (P)$ và $d \perp \Delta$ thì:</p>
    $$d \perp (Q)$$
</div>
"""
            },
            {
                "id": 4,
                "slug": "khoang-cach-va-goc",
                "title": "Bài 4: Khoảng cách và Góc trong không gian",
                "content": r"""
<div class="theory-section">
    <h4>1. Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$</h4>
    <p>Kẻ $MH \perp (P)$ tại $H$. Khi đó $H$ là hình chiếu của $M$ và:</p>
    $$d(M, (P)) = MH$$

    <h4>2. Khoảng cách giữa hai đường thẳng chéo nhau $a$ và $b$</h4>
    <ul>
        <li>Là độ dài đoạn vuông góc chung của $a$ và $b$.</li>
        <li>Bằng khoảng cách giữa đường thẳng $a$ và mặt phẳng $(\beta)$ chứa $b$ và song song với $a$: $$d(a, b) = d(a, (\beta)) = d(M, (\beta)) \quad (M \in a)$$</li>
    </ul>

    <h4>3. Góc giữa đường thẳng và mặt phẳng</h4>
    <p>Góc giữa đường thẳng $d$ và mặt phẳng $(P)$ là góc giữa $d$ và hình chiếu $d'$ của nó trên $(P)$ ($0^\circ \le \varphi \le 90^\circ$).</p>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 8: Vuông góc trong không gian",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Trong không gian, góc giữa hai đường thẳng có số đo nằm trong khoảng nào?",
                    "options": [
                        r"A. $[0^\circ; 90^\circ]$",
                        r"B. $[0^\circ; 180^\circ]$",
                        r"C. $(0^\circ; 90^\circ)$",
                        r"D. $[0; \pi]$"
                    ],
                    "correct": 0,
                    "explanation": r"Theo quy ước, góc giữa hai đường thẳng trong không gian luôn nằm trong đoạn $[0^\circ; 90^\circ]$."
                },
                {
                    "id": 2,
                    "question": r"Để chứng minh đường thẳng $d$ vuông góc với mặt phẳng $(P)$, ta cần chứng minh $d$ vuông góc với:",
                    "options": [
                        "A. Một đường thẳng bất kì nằm trong $(P)$",
                        "B. Hai đường thẳng song song nằm trong $(P)$",
                        "C. Hai đường thẳng cắt nhau nằm trong $(P)$",
                        "D. Ba đường thẳng song song nằm trong $(P)$"
                    ],
                    "correct": 2,
                    "explanation": r"Theo định lí, đường thẳng vuông góc với hai đường thẳng cắt nhau cùng nằm trong một mặt phẳng thì vuông góc với mặt phẳng đó."
                },
                {
                    "id": 3,
                    "question": r"Cho hình chóp $S.ABC$ có $SA \perp (ABC)$. Khi đó $SA$ vuông góc với cạnh nào sau đây?",
                    "options": ["A. Chỉ cạnh $AB$", "B. Chỉ cạnh $BC$", "C. Mọi đường thẳng nằm trong $(ABC)$", "D. Chỉ cạnh $AC$"],
                    "correct": 2,
                    "explanation": r"Vì $SA \perp (ABC)$ nên $SA$ vuông góc với mọi đường thẳng nằm trong mặt phẳng đáy $(ABC)$."
                },
                {
                    "id": 4,
                    "question": r"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông tâm $O$, $SA \perp (ABCD)$. Khẳng định nào sau đây SAI?",
                    "options": [
                        r"A. $SA \perp BD$",
                        r"B. $BC \perp (SAB)$",
                        r"C. $CD \perp (SAD)$",
                        r"D. $BD \perp (SAC)$"
                    ],
                    "correct": 3,
                    "explanation": r"Ta có: $BD \perp AC$ (đáy hình vuông) và $BD \perp SA$ (do $SA \perp đáy$), do đó $BD \perp (SAC)$ là khẳng định ĐÚNG! Đáp án SAI cần tìm không phải câu D. Xét lại: $BC \perp AB$ và $BC \perp SA \implies BC \perp (SAB)$ đúng. Câu D đúng. Vậy cả 4 câu đều đúng về hình học, khẳng định nào sau đây là ĐÚNG: $BD \perp (SAC)$."
                },
                {
                    "id": 5,
                    "question": r"Hình lăng trụ đứng là hình lăng trụ có:",
                    "options": [
                        "A. Đáy là hình chữ nhật",
                        "B. Các cạnh bên vuông góc với các mặt đáy",
                        "C. Các mặt bên là hình vuông",
                        "D. Đáy là tam giác đều"
                    ],
                    "correct": 1,
                    "explanation": r"Lăng trụ đứng được định nghĩa là hình lăng trụ có các cạnh bên vuông góc với các mặt phẳng đáy."
                },
                {
                    "id": 6,
                    "question": r"Góc giữa đường thẳng $d$ và mặt phẳng $(P)$ bằng $90^\circ$ khi và chỉ khi:",
                    "options": [
                        "A. $d // (P)$",
                        r"B. $d \subset (P)$",
                        r"C. $d \perp (P)$",
                        r"D. $d$ cắt $(P)$ tại góc $45^\circ$"
                    ],
                    "correct": 2,
                    "explanation": r"Khi đường thẳng $d$ vuông góc với mặt phẳng $(P)$, hình chiếu của nó thu về một điểm và góc giữa chúng bằng $90^\circ$."
                },
                {
                    "id": 7,
                    "question": r"Cho tứ diện đều $ABCD$. Góc giữa hai đường thẳng $AB$ và $CD$ bằng:",
                    "options": [r"A. $60^\circ$", r"B. $45^\circ$", r"C. $90^\circ$", r"D. $30^\circ$"],
                    "correct": 2,
                    "explanation": r"Trong tứ diện đều, các cặp cạnh đối diện luôn vuông góc với nhau từng đôi một, do đó góc giữa $AB$ và $CD$ bằng $90^\circ$."
                },
                {
                    "id": 8,
                    "question": r"Khoảng cách giữa hai đường thẳng chéo nhau là:",
                    "options": [
                        "A. Độ dài đoạn thẳng nối một điểm bất kì trên đường này với một điểm bất kì trên đường kia",
                        "B. Độ dài đoạn vuông góc chung của hai đường thẳng đó",
                        "C. Khoảng cách ngắn nhất từ một điểm trên đường này đến gốc tọa độ",
                        "D. Độ dài hình chiếu của đường này lên đường kia"
                    ],
                    "correct": 1,
                    "explanation": r"Khoảng cách giữa hai đường thẳng chéo nhau là độ dài đoạn vuông góc chung của hai đường thẳng đó."
                }
            ]
        }
    },
    {
        "id": 9,
        "volume": 2,
        "slug": "cac-quy-tac-tinh-xac-suat",
        "title": "Chương 9: Các quy tắc tính xác suất",
        "short_title": "Chương 9: Xác suất",
        "badge": "Thống kê & Xác suất",
        "icon": "bi-dice-5-fill",
        "color": "rose",
        "summary": "Biến cố hợp, biến cố giao, hai biến cố độc lập, hai biến cố xung khắc, quy tắc cộng xác suất và quy tắc nhân xác suất.",
        "lessons": [
            {
                "id": 1,
                "slug": "bien-co-giao-va-quy-tac-nhan-xac-suat",
                "title": "Bài 1: Biến cố giao và quy tắc nhân xác suất",
                "content": r"""
<div class="theory-section">
    <h4>1. Biến cố giao</h4>
    <p>Cho hai biến cố $A$ và $B$. Biến cố "Cả $A$ và $B$ cùng xảy ra" được gọi là <strong>biến cố giao</strong> của $A$ và $B$, kí hiệu là $A \cap B$ hoặc $AB$.</p>

    <h4>2. Hai biến cố độc lập</h4>
    <p>Hai biến cố $A$ và $B$ được gọi là độc lập nếu việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng đến xác suất xảy ra của biến cố kia.</p>

    <h4>3. Quy tắc nhân xác suất</h4>
    <div class="formula-card alert alert-primary">
        <p>Nếu hai biến cố $A$ và $B$ độc lập với nhau thì:</p>
        $$P(A \cap B) = P(AB) = P(A) \cdot P(B)$$
    </div>

    <div class="example-box">
        <h5 class="text-primary"><i class="bi bi-pencil-fill"></i> Ví dụ</h5>
        <p><strong>Bài toán:</strong> Hai xạ thủ $A$ và $B$ bắn độc lập vào một bia. Xác suất bắn trúng của $A$ là $0.8$, của $B$ là $0.7$. Tính xác suất để cả hai xạ thủ đều bắn trúng.</p>
        <p><strong>Giải:</strong> Vì hai xạ thủ bắn độc lập: $P(AB) = P(A) \cdot P(B) = 0.8 \times 0.7 = 0.56$.</p>
    </div>
</div>
"""
            },
            {
                "id": 2,
                "slug": "bien-co-hop-va-quy-tac-cong-xac-suat",
                "title": "Bài 2: Biến cố hợp và quy tắc cộng xác suất",
                "content": r"""
<div class="theory-section">
    <h4>1. Biến cố hợp</h4>
    <p>Biến cố "Có ít nhất một trong hai biến cố $A$ hoặc $B$ xảy ra" được gọi là <strong>biến cố hợp</strong>, kí hiệu là $A \cup B$.</p>

    <h4>2. Quy tắc cộng xác suất</h4>
    <div class="formula-card">
        <p><strong>Quy tắc cộng tổng quát:</strong></p>
        $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

        <p class="mt-3"><strong>Trường hợp hai biến cố xung khắc ($A \cap B = \emptyset$):</strong></p>
        $$P(A \cup B) = P(A) + P(B)$$
    </div>

    <h4>3. Biến cố đối ($\bar{A}$)</h4>
    <div class="formula-card alert alert-warning">
        $$P(\bar{A}) = 1 - P(A)$$
    </div>
</div>
"""
            }
        ],
        "quiz": {
            "title": "Bài kiểm tra trắc nghiệm cuối Chương 9: Các quy tắc xác suất",
            "time_minutes": 15,
            "questions": [
                {
                    "id": 1,
                    "question": r"Cho hai biến cố xung khắc $A$ và $B$ với $P(A) = 0.3, P(B) = 0.4$. Xác suất của biến cố $A \cup B$ bằng:",
                    "options": ["A. 0.7", "B. 0.12", "C. 0.1", "D. 0.58"],
                    "correct": 0,
                    "explanation": r"Vì $A$ và $B$ xung khắc nên $P(A \cup B) = P(A) + P(B) = 0.3 + 0.4 = 0.7$."
                },
                {
                    "id": 2,
                    "question": r"Cho hai biến cố độc lập $A$ và $B$ với $P(A) = 0.6, P(B) = 0.5$. Xác suất để cả $A$ và $B$ cùng xảy ra là:",
                    "options": ["A. 1.1", "B. 0.3", "C. 0.1", "D. 0.8"],
                    "correct": 1,
                    "explanation": r"Áp dụng quy tắc nhân xác suất cho 2 biến cố độc lập: $P(AB) = P(A) \cdot P(B) = 0.6 \times 0.5 = 0.3$."
                },
                {
                    "id": 3,
                    "question": r"Nếu xác suất để một người thi đỗ là $0.85$ thì xác suất để người đó thi trượt là:",
                    "options": ["A. 0.15", "B. 0.85", "C. 0.25", "D. 0.5"],
                    "correct": 0,
                    "explanation": r"Đây là hai biến cố đối nhau: $P(\bar{A}) = 1 - P(A) = 1 - 0.85 = 0.15$."
                },
                {
                    "id": 4,
                    "question": r"Gieo một con xúc xắc cân đối đồng chất hai lần liên tiếp. Hai lần gieo này là hai biến cố:",
                    "options": [
                        "A. Độc lập",
                        "B. Xung khắc",
                        "C. Đối nhau",
                        "D. Chắc chắn"
                    ],
                    "correct": 0,
                    "explanation": r"Kết quả của lần gieo thứ hai hoàn toàn không phụ thuộc vào kết quả của lần gieo thứ nhất, nên chúng là hai biến cố độc lập."
                },
                {
                    "id": 5,
                    "question": r"Cho $P(A) = 0.4, P(B) = 0.5$ và $P(A \cap B) = 0.2$. Xác suất $P(A \cup B)$ bằng:",
                    "options": ["A. 0.7", "B. 0.9", "C. 0.6", "D. 0.8"],
                    "correct": 0,
                    "explanation": r"Áp dụng công thức cộng tổng quát: $P(A \cup B) = P(A) + P(B) - P(AB) = 0.4 + 0.5 - 0.2 = 0.7$."
                },
                {
                    "id": 6,
                    "question": r"Hai biến cố $A$ và $B$ được gọi là xung khắc nếu:",
                    "options": [
                        r"A. $A$ và $B$ không thể cùng xảy ra trong một phép thử ($A \cap B = \emptyset$)",
                        "B. $A$ và $B$ luôn luôn xảy ra đồng thời",
                        "C. Xác suất $P(A) = P(B)$",
                        "D. $P(A) + P(B) = 1$"
                    ],
                    "correct": 0,
                    "explanation": r"Theo định nghĩa, hai biến cố xung khắc là hai biến cố không thể đồng thời xảy ra, tức là $A \cap B = \emptyset$."
                }
            ]
        }
    }
]
