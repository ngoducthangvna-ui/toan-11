# -*- coding: utf-8 -*-
"""
Sổ tay công thức Toán 11 toàn tập - Bảng tra cứu nhanh
"""

FORMULA_CATEGORIES = [
    {
        "id": "luong-giac",
        "title": "1. Công thức Lượng giác",
        "icon": "bi-symmetry-horizontal",
        "formulas": [
            {
                "name": "Hệ thức cơ bản",
                "latex": r"\sin^2 x + \cos^2 x = 1, \quad 1 + \tan^2 x = \frac{1}{\cos^2 x}, \quad 1 + \cot^2 x = \frac{1}{\sin^2 x}, \quad \tan x \cdot \cot x = 1"
            },
            {
                "name": "Công thức cộng",
                "latex": r"\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b, \quad \sin(a \pm b) = \sin a \cos b \pm \cos a \sin b"
            },
            {
                "name": "Công thức nhân đôi & hạ bậc",
                "latex": r"\sin 2a = 2\sin a \cos a, \quad \cos 2a = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a"
            },
            {
                "name": "Công thức biến đổi tích thành tổng",
                "latex": r"\cos a \cos b = \frac{1}{2}[\cos(a-b) + \cos(a+b)], \quad \sin a \sin b = \frac{1}{2}[\cos(a-b) - \cos(a+b)], \quad \sin a \cos b = \frac{1}{2}[\sin(a+b) + \sin(a-b)]"
            },
            {
                "name": "Phương trình lượng giác cơ bản",
                "latex": r"\sin x = \sin \alpha \iff x = \alpha + k2\pi \lor x = \pi - \alpha + k2\pi; \quad \cos x = \cos \alpha \iff x = \pm \alpha + k2\pi"
            }
        ]
    },
    {
        "id": "csc-csn",
        "title": "2. Cấp số cộng & Cấp số nhân",
        "icon": "bi-sort-numeric-up",
        "formulas": [
            {
                "name": "Cấp số cộng (CSC)",
                "latex": r"u_n = u_1 + (n-1)d, \quad S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n-1)d]}{2}, \quad u_k = \frac{u_{k-1} + u_{k+1}}{2}"
            },
            {
                "name": "Cấp số nhân (CSN)",
                "latex": r"u_n = u_1 \cdot q^{n-1}, \quad S_n = \frac{u_1(1-q^n)}{1-q} \quad (q \neq 1), \quad u_k^2 = u_{k-1} \cdot u_{k+1}"
            },
            {
                "name": "Cấp số nhân lùi vô hạn",
                "latex": r"S = \frac{u_1}{1 - q} \quad (|q| < 1)"
            }
        ]
    },
    {
        "id": "gioi-han",
        "title": "3. Giới hạn & Hàm số liên tục",
        "icon": "bi-infinity",
        "formulas": [
            {
                "name": "Giới hạn cơ bản",
                "latex": r"\lim_{n \to \infty} \frac{1}{n^k} = 0 \ (k>0), \quad \lim_{n \to \infty} q^n = 0 \ (|q|<1)"
            },
            {
                "name": "Hàm số liên tục tại điểm $x_0$",
                "latex": r"\lim_{x \to x_0} f(x) = f(x_0)"
            },
            {
                "name": "Định lí giá trị trung gian",
                "latex": r"f(x) \text{ liên tục trên } [a; b] \text{ và } f(a)f(b) < 0 \implies \exists c \in (a; b): f(c) = 0"
            }
        ]
    },
    {
        "id": "mu-logarit",
        "title": "4. Lũy thừa, Mũ & Logarit",
        "icon": "bi-graph-up-arrow",
        "formulas": [
            {
                "name": "Tính chất logarit",
                "latex": r"\log_a(xy) = \log_a x + \log_a y, \quad \log_a(x/y) = \log_a x - \log_a y, \quad \log_a(x^\alpha) = \alpha \log_a x"
            },
            {
                "name": "Đổi cơ số",
                "latex": r"\log_a b = \frac{\log_c b}{\log_c a}, \quad \log_a b \cdot \log_b c = \log_a c, \quad \log_{a^\beta} b = \frac{1}{\beta}\log_a b"
            },
            {
                "name": "Phương trình mũ & logarit",
                "latex": r"a^x = b \iff x = \log_a b \ (b > 0); \quad \log_a x = b \iff x = a^b"
            }
        ]
    },
    {
        "id": "dao-ham",
        "title": "5. Bảng đạo hàm và quy tắc",
        "icon": "bi-lightning-charge-fill",
        "formulas": [
            {
                "name": "Đạo hàm hàm đa thức & căn thức",
                "latex": r"(x^n)' = n x^{n-1}, \quad (\sqrt{x})' = \frac{1}{2\sqrt{x}}, \quad (u^n)' = n u^{n-1} u', \quad (\sqrt{u})' = \frac{u'}{2\sqrt{u}}"
            },
            {
                "name": "Đạo hàm hàm lượng giác",
                "latex": r"(\sin u)' = u'\cos u, \quad (\cos u)' = -u'\sin u, \quad (\tan u)' = \frac{u'}{\cos^2 u}, \quad (\cot u)' = -\frac{u'}{\sin^2 u}"
            },
            {
                "name": "Đạo hàm hàm mũ & logarit",
                "latex": r"(e^u)' = u' e^u, \quad (a^u)' = u' a^u \ln a, \quad (\ln |u|)' = \frac{u'}{u}, \quad (\log_a |u|)' = \frac{u'}{u \ln a}"
            },
            {
                "name": "Tiếp tuyến của đồ thị hàm số",
                "latex": r"y = f'(x_0)(x - x_0) + f(x_0)"
            }
        ]
    },
    {
        "id": "xac-suat",
        "title": "6. Các quy tắc tính Xác suất",
        "icon": "bi-dice-5-fill",
        "formulas": [
            {
                "name": "Quy tắc cộng xác suất",
                "latex": r"P(A \cup B) = P(A) + P(B) - P(AB); \quad A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B)"
            },
            {
                "name": "Quy tắc nhân xác suất (biến cố độc lập)",
                "latex": r"P(A \cap B) = P(A) \cdot P(B)"
            },
            {
                "name": "Biến cố đối",
                "latex": r"P(\bar{A}) = 1 - P(A)"
            }
        ]
    }
]
