# -*- coding: utf-8 -*-
"""
Sổ tay công thức Toán 11 Toàn Tập - Chuẩn GDPT 2018
Mỗi công thức hiển thị riêng biệt trên 1 dòng rõ ràng, chống tràn màn hình.
Tác giả: Antigravity AI
"""

FORMULA_CATEGORIES = [
    {
        "id": "chuong-1-luong-giac",
        "title": "CHƯƠNG I: HÀM SỐ LƯỢNG GIÁC & PHƯƠNG TRÌNH LƯỢNG GIÁC",
        "icon": "bi-symmetry-horizontal",
        "formulas": [
            {
                "name": "1. Đổi đơn vị góc và Độ dài cung tròn",
                "latex_lines": [
                    r"\alpha^\circ = \frac{\pi}{180} \cdot \alpha \text{ (rad)}",
                    r"\alpha \text{ (rad)} = \left(\frac{180}{\pi} \cdot \alpha\right)^\circ",
                    r"l = R \cdot \alpha \quad (\text{với } \alpha \text{ tính bằng rad})"
                ]
            },
            {
                "name": "2. Các hệ thức lượng giác cơ bản",
                "latex_lines": [
                    r"\tan\alpha = \frac{\sin\alpha}{\cos\alpha} \quad \left(\alpha \neq \frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right)",
                    r"\cot\alpha = \frac{\cos\alpha}{\sin\alpha} \quad (\alpha \neq k\pi, k \in \mathbb{Z})",
                    r"\sin^2\alpha + \cos^2\alpha = 1",
                    r"1 + \tan^2\alpha = \frac{1}{\cos^2\alpha} \quad \left(\alpha \neq \frac{\pi}{2} + k\pi, k \in \mathbb{Z}\right)",
                    r"1 + \cot^2\alpha = \frac{1}{\sin^2\alpha} \quad (\alpha \neq k\pi, k \in \mathbb{Z})",
                    r"\tan\alpha \cdot \cot\alpha = 1 \quad \left(\alpha \neq k\frac{\pi}{2}, k \in \mathbb{Z}\right)"
                ]
            },
            {
                "name": "3. Góc đối nhau (α và -α)",
                "latex_lines": [
                    r"\cos(-\alpha) = \cos\alpha",
                    r"\sin(-\alpha) = -\sin\alpha",
                    r"\tan(-\alpha) = -\tan\alpha",
                    r"\cot(-\alpha) = -\cot\alpha"
                ]
            },
            {
                "name": "3. Góc bù nhau (α và π - α)",
                "latex_lines": [
                    r"\sin(\pi - \alpha) = \sin\alpha",
                    r"\cos(\pi - \alpha) = -\cos\alpha",
                    r"\tan(\pi - \alpha) = -\tan\alpha",
                    r"\cot(\pi - \alpha) = -\cot\alpha"
                ]
            },
            {
                "name": "3. Góc phụ nhau (α và π/2 - α)",
                "latex_lines": [
                    r"\sin\left(\frac{\pi}{2} - \alpha\right) = \cos\alpha",
                    r"\cos\left(\frac{\pi}{2} - \alpha\right) = \sin\alpha",
                    r"\tan\left(\frac{\pi}{2} - \alpha\right) = \cot\alpha",
                    r"\cot\left(\frac{\pi}{2} - \alpha\right) = \tan\alpha"
                ]
            },
            {
                "name": "3. Góc hơn kém π (α và π + α)",
                "latex_lines": [
                    r"\sin(\pi + \alpha) = -\sin\alpha",
                    r"\cos(\pi + \alpha) = -\cos\alpha",
                    r"\tan(\pi + \alpha) = \tan\alpha",
                    r"\cot(\pi + \alpha) = \cot\alpha"
                ]
            },
            {
                "name": "4. Công thức cộng",
                "latex_lines": [
                    r"\cos(a - b) = \cos a \cos b + \sin a \sin b",
                    r"\cos(a + b) = \cos a \cos b - \sin a \sin b",
                    r"\sin(a - b) = \sin a \cos b - \cos a \sin b",
                    r"\sin(a + b) = \sin a \cos b + \cos a \sin b",
                    r"\tan(a - b) = \frac{\tan a - \tan b}{1 + \tan a \tan b}",
                    r"\tan(a + b) = \frac{\tan a + \tan b}{1 - \tan a \tan b}"
                ]
            },
            {
                "name": "5. Công thức nhân đôi",
                "latex_lines": [
                    r"\sin 2a = 2\sin a \cos a",
                    r"\cos 2a = \cos^2 a - \sin^2 a",
                    r"\cos 2a = 2\cos^2 a - 1",
                    r"\cos 2a = 1 - 2\sin^2 a",
                    r"\tan 2a = \frac{2\tan a}{1 - \tan^2 a}"
                ]
            },
            {
                "name": "6. Công thức hạ bậc",
                "latex_lines": [
                    r"\cos^2 a = \frac{1 + \cos 2a}{2}",
                    r"\sin^2 a = \frac{1 - \cos 2a}{2}",
                    r"\tan^2 a = \frac{1 - \cos 2a}{1 + \cos 2a}"
                ]
            },
            {
                "name": "7. Công thức biến đổi tích thành tổng",
                "latex_lines": [
                    r"\cos a \cos b = \frac{1}{2}[\cos(a - b) + \cos(a + b)]",
                    r"\sin a \sin b = \frac{1}{2}[\cos(a - b) - \cos(a + b)]",
                    r"\sin a \cos b = \frac{1}{2}[\sin(a - b) + \sin(a + b)]"
                ]
            },
            {
                "name": "8. Công thức biến đổi tổng thành tích",
                "latex_lines": [
                    r"\cos u + \cos v = 2\cos\frac{u + v}{2}\cos\frac{u - v}{2}",
                    r"\cos u - \cos v = -2\sin\frac{u + v}{2}\sin\frac{u - v}{2}",
                    r"\sin u + \sin v = 2\sin\frac{u + v}{2}\cos\frac{u - v}{2}",
                    r"\sin u - \sin v = 2\cos\frac{u + v}{2}\sin\frac{u - v}{2}"
                ]
            },
            {
                "name": "9. Chu kì của các hàm số lượng giác cơ bản",
                "latex_lines": [
                    r"y = \sin x \text{ có chu kì } T = 2\pi",
                    r"y = \cos x \text{ có chu kì } T = 2\pi",
                    r"y = \tan x \text{ có chu kì } T = \pi",
                    r"y = \cot x \text{ có chu kì } T = \pi"
                ]
            },
            {
                "name": "10. Phương trình lượng giác cơ bản & trường hợp đặc biệt",
                "latex_lines": [
                    r"\sin x = \sin\alpha \iff x = \alpha + k2\pi \lor x = \pi - \alpha + k2\pi \quad (k \in \mathbb{Z})",
                    r"\sin x = 1 \iff x = \frac{\pi}{2} + k2\pi \quad (k \in \mathbb{Z})",
                    r"\sin x = -1 \iff x = -\frac{\pi}{2} + k2\pi \quad (k \in \mathbb{Z})",
                    r"\sin x = 0 \iff x = k\pi \quad (k \in \mathbb{Z})",
                    r"\cos x = \cos\alpha \iff x = \alpha + k2\pi \lor x = -\alpha + k2\pi \quad (k \in \mathbb{Z})",
                    r"\cos x = 1 \iff x = k2\pi \quad (k \in \mathbb{Z})",
                    r"\cos x = -1 \iff x = \pi + k2\pi \quad (k \in \mathbb{Z})",
                    r"\cos x = 0 \iff x = \frac{\pi}{2} + k\pi \quad (k \in \mathbb{Z})",
                    r"\tan x = \tan\alpha \iff x = \alpha + k\pi \quad (k \in \mathbb{Z})",
                    r"\cot x = \cot\alpha \iff x = \alpha + k\pi \quad (k \in \mathbb{Z})"
                ]
            }
        ]
    },
    {
        "id": "chuong-2-csc-csn",
        "title": "CHƯƠNG II: DÃY SỐ. CẤP SỐ CỘNG VÀ CẤP SỐ NHÂN",
        "icon": "bi-sort-numeric-up",
        "formulas": [
            {
                "name": "1. Tính chất của dãy số",
                "latex_lines": [
                    r"u_{n+1} > u_n, \forall n \in \mathbb{N}^* \quad (\text{Dãy số tăng})",
                    r"u_{n+1} < u_n, \forall n \in \mathbb{N}^* \quad (\text{Dãy số giảm})",
                    r"m \le u_n \le M, \forall n \in \mathbb{N}^* \quad (\text{Dãy số bị chặn})"
                ]
            },
            {
                "name": "2. Cấp số cộng (Công sai d)",
                "latex_lines": [
                    r"u_n = u_{n-1} + d \quad (n \ge 2)",
                    r"u_n = u_1 + (n - 1)d \quad (n \ge 2)",
                    r"u_k = \frac{u_{k-1} + u_{k+1}}{2} \quad (k \ge 2)",
                    r"S_n = \frac{n(u_1 + u_n)}{2}",
                    r"S_n = \frac{n[2u_1 + (n - 1)d]}{2}"
                ]
            },
            {
                "name": "3. Cấp số nhân (Công bội q)",
                "latex_lines": [
                    r"u_n = u_{n-1} \cdot q \quad (n \ge 2)",
                    r"u_n = u_1 \cdot q^{n-1} \quad (n \ge 2)",
                    r"u_k^2 = u_{k-1} \cdot u_{k+1} \quad (k \ge 2)",
                    r"S_n = \frac{u_1(1 - q^n)}{1 - q} \quad (q \neq 1)",
                    r"S = \frac{u_1}{1 - q} \quad (|q| < 1, \text{ CSN lùi vô hạn})"
                ]
            }
        ]
    },
    {
        "id": "chuong-3-thong-ke",
        "title": "CHƯƠNG III: CÁC SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM CỦA MẪU SỐ LIỆU GHÉP NHÓM",
        "icon": "bi-bar-chart-line-fill",
        "formulas": [
            {
                "name": "1. Giá trị đại diện và Số trung bình",
                "latex_lines": [
                    r"x_i = \frac{a_i + a_{i+1}}{2} \quad (\text{Giá trị đại diện của nhóm } [a_i; a_{i+1}))",
                    r"n = n_1 + n_2 + \dots + n_k \quad (\text{Cỡ mẫu})",
                    r"\bar{x} = \frac{n_1 x_1 + n_2 x_2 + \dots + n_k x_k}{n} \quad (\text{Số trung bình})"
                ]
            },
            {
                "name": "2. Trung vị (Me) và Tứ phân vị (Q1, Q2, Q3)",
                "latex_lines": [
                    r"M_e = u_m + \frac{\frac{n}{2} - C}{n_m} \cdot (u_{m+1} - u_m)",
                    r"Q_1 = u_j + \frac{\frac{n}{4} - C}{n_j} \cdot (u_{j+1} - u_j)",
                    r"Q_2 = M_e",
                    r"Q_3 = u_p + \frac{\frac{3n}{4} - C}{n_p} \cdot (u_{p+1} - u_p)",
                    r"\text{Trong đó: } [u_m; u_{m+1}) \text{ chứa trung vị; } n_m \text{ là tần số; } C \text{ là tần số tích lũy trước đó.}"
                ]
            },
            {
                "name": "3. Mốt của mẫu số liệu ghép nhóm (Mo)",
                "latex_lines": [
                    r"M_o = u_m + \frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \cdot (u_{m+1} - u_m)"
                ]
            }
        ]
    },
    {
        "id": "chuong-4-khong-gian-song-song",
        "title": "CHƯƠNG IV: QUAN HỆ SONG SONG TRONG KHÔNG GIAN (CÁC HỆ THỨC CỐT LÕI)",
        "icon": "bi-bounding-box-circles",
        "formulas": [
            {
                "name": "1. Điều kiện đường thẳng song song mặt phẳng",
                "latex_lines": [
                    r"\begin{cases} d \not\subset (\alpha) \\ d // d' \\ d' \subset (\alpha) \end{cases} \implies d // (\alpha)"
                ]
            },
            {
                "name": "2. Định lí giao tuyến khi có đường song song mặt",
                "latex_lines": [
                    r"\begin{cases} d // (\alpha) \\ d \subset (\beta) \\ (\alpha) \cap (\beta) = d' \end{cases} \implies d' // d"
                ]
            },
            {
                "name": "3. Điều kiện hai mặt phẳng song song",
                "latex_lines": [
                    r"\begin{cases} a \cap b = I, \ a, b \subset (\alpha) \\ a // (\beta), \ b // (\beta) \end{cases} \implies (\alpha) // (\beta)"
                ]
            },
            {
                "name": "4. Một mặt phẳng cắt hai mặt phẳng song song",
                "latex_lines": [
                    r"\begin{cases} (\alpha) // (\beta) \\ (\gamma) \cap (\alpha) = a \\ (\gamma) \cap (\beta) = b \end{cases} \implies a // b"
                ]
            },
            {
                "name": "5. Định lí Thales trong không gian",
                "latex_lines": [
                    r"\frac{A'B'}{AB} = \frac{B'C'}{BC} = \frac{A'C'}{AC}"
                ]
            }
        ]
    },
    {
        "id": "chuong-5-gioi-han",
        "title": "CHƯƠNG V: GIỚI HẠN. HÀM SỐ LIÊN TỤC",
        "icon": "bi-infinity",
        "formulas": [
            {
                "name": "1. Giới hạn của dãy số và Cấp số nhân lùi vô hạn",
                "latex_lines": [
                    r"\lim_{n \to +\infty} \frac{1}{n^k} = 0 \quad (k \in \mathbb{N}^*)",
                    r"\lim_{n \to +\infty} q^n = 0 \quad (|q| < 1)",
                    r"\lim_{n \to +\infty} c = c \quad (c \text{ là hằng số})",
                    r"S = u_1 + u_1 q + u_1 q^2 + \dots = \frac{u_1}{1 - q} \quad (|q| < 1)",
                    r"\lim_{n \to +\infty} n^k = +\infty \quad (k \in \mathbb{N}^*)",
                    r"\lim_{n \to +\infty} q^n = +\infty \quad (q > 1)"
                ]
            },
            {
                "name": "2. Giới hạn của hàm số",
                "latex_lines": [
                    r"\lim_{x \to x_0} c = c",
                    r"\lim_{x \to x_0} x^n = x_0^n \quad (n \in \mathbb{N}^*)",
                    r"\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = L",
                    r"\lim_{x \to +\infty} \frac{c}{x^k} = 0 \quad (k \in \mathbb{N}^*)",
                    r"\lim_{x \to -\infty} \frac{c}{x^k} = 0 \quad (k \in \mathbb{N}^*)"
                ]
            },
            {
                "name": "3. Hàm số liên tục",
                "latex_lines": [
                    r"\lim_{x \to x_0} f(x) = f(x_0) \quad (\text{Điều kiện hàm số liên tục tại điểm } x_0)",
                    r"f(a) \cdot f(b) < 0 \implies \exists c \in (a; b): f(c) = 0 \quad (\text{Định lí giá trị trung gian})"
                ]
            }
        ]
    },
    {
        "id": "chuong-6-mu-logarit",
        "title": "CHƯƠNG VI: HÀM SỐ MŨ VÀ HÀM SỐ LOGARIT",
        "icon": "bi-graph-up-arrow",
        "formulas": [
            {
                "name": "1. Công thức Lũy thừa",
                "latex_lines": [
                    r"a^m \cdot a^n = a^{m+n}",
                    r"\frac{a^m}{a^n} = a^{m-n}",
                    r"(a^m)^n = a^{m \cdot n}",
                    r"(a \cdot b)^n = a^n \cdot b^n",
                    r"\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}",
                    r"a^{-n} = \frac{1}{a^n}",
                    r"a^{\frac{m}{n}} = \sqrt[n]{a^m}"
                ]
            },
            {
                "name": "2. Tính chất Logarit",
                "latex_lines": [
                    r"\log_a(x \cdot y) = \log_a x + \log_a y",
                    r"\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y",
                    r"\log_a(x^\alpha) = \alpha \log_a x",
                    r"\log_a b = \frac{\log_c b}{\log_c a} \quad (\text{Đổi cơ số})",
                    r"\log_{a^\beta} b = \frac{1}{\beta}\log_a b",
                    r"a^{\log_a b} = b"
                ]
            },
            {
                "name": "3. Phương trình Mũ & Logarit cơ bản",
                "latex_lines": [
                    r"a^x = b \iff x = \log_a b \quad (b > 0)",
                    r"\log_a x = b \iff x = a^b"
                ]
            }
        ]
    },
    {
        "id": "chuong-7-dao-ham",
        "title": "CHƯƠNG VII: ĐẠO HÀM VÀ TIẾP TUYẾN",
        "icon": "bi-lightning-charge-fill",
        "formulas": [
            {
                "name": "1. Đạo hàm đa thức & căn thức",
                "latex_lines": [
                    r"(c)' = 0 \quad (c \text{ là hằng số})",
                    r"(x^n)' = n x^{n-1}",
                    r"(\sqrt{x})' = \frac{1}{2\sqrt{x}}",
                    r"\left(\frac{1}{x}\right)' = -\frac{1}{x^2}",
                    r"(u^n)' = n u^{n-1} u'",
                    r"(\sqrt{u})' = \frac{u'}{2\sqrt{u}}"
                ]
            },
            {
                "name": "2. Đạo hàm hàm lượng giác",
                "latex_lines": [
                    r"(\sin x)' = \cos x",
                    r"(\cos x)' = -\sin x",
                    r"(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x",
                    r"(\cot x)' = -\frac{1}{\sin^2 x} = -(1 + \cot^2 x)",
                    r"(\sin u)' = u' \cos u",
                    r"(\cos u)' = -u' \sin u",
                    r"(\tan u)' = \frac{u'}{\cos^2 u}"
                ]
            },
            {
                "name": "3. Đạo hàm hàm mũ & logarit",
                "latex_lines": [
                    r"(e^x)' = e^x",
                    r"(e^u)' = u' e^u",
                    r"(a^x)' = a^x \ln a",
                    r"(\ln |x|)' = \frac{1}{x}",
                    r"(\ln |u|)' = \frac{u'}{u}",
                    r"(\log_a |u|)' = \frac{u'}{u \ln a}"
                ]
            },
            {
                "name": "4. Phương trình tiếp tuyến của đồ thị hàm số",
                "latex_lines": [
                    r"y = f'(x_0)(x - x_0) + f(x_0)"
                ]
            }
        ]
    },
    {
        "id": "chuong-8-khong-gian-vuong-goc",
        "title": "CHƯƠNG VIII: QUAN HỆ VUÔNG GÓC TRONG KHÔNG GIAN & THỂ TÍCH",
        "icon": "bi-box",
        "formulas": [
            {
                "name": "1. Đường thẳng vuông góc mặt phẳng",
                "latex_lines": [
                    r"\begin{cases} d \perp a, \ d \perp b \\ a \cap b = I, \ a, b \subset (\alpha) \end{cases} \implies d \perp (\alpha)"
                ]
            },
            {
                "name": "2. Hai mặt phẳng vuông góc",
                "latex_lines": [
                    r"\begin{cases} d \subset (\alpha) \\ d \perp (\beta) \end{cases} \implies (\alpha) \perp (\beta)"
                ]
            },
            {
                "name": "3. Công thức Thể tích Khối đa diện",
                "latex_lines": [
                    r"V_{\text{chóp}} = \frac{1}{3} S_{\text{đáy}} \cdot h",
                    r"V_{\text{lăng trụ}} = S_{\text{đáy}} \cdot h",
                    r"V_{\text{hộp chữ nhật}} = a \cdot b \cdot c",
                    r"V_{\text{lập phương}} = a^3"
                ]
            }
        ]
    },
    {
        "id": "chuong-9-xac-suat",
        "title": "CHƯƠNG IX: CÁC QUY TẮC TÍNH XÁC SUẤT",
        "icon": "bi-dice-5-fill",
        "formulas": [
            {
                "name": "1. Quy tắc cộng xác suất",
                "latex_lines": [
                    r"P(A \cup B) = P(A) + P(B) - P(AB)",
                    r"A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B) \quad (\text{Biến cố xung khắc})"
                ]
            },
            {
                "name": "2. Quy tắc nhân xác suất",
                "latex_lines": [
                    r"P(A \cap B) = P(A) \cdot P(B) \quad (\text{Biến cố độc lập})"
                ]
            },
            {
                "name": "3. Biến cố đối",
                "latex_lines": [
                    r"P(\bar{A}) = 1 - P(A)"
                ]
            }
        ]
    }
]
