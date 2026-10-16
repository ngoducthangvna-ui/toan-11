# TOÁN 11 MASTER - CỔNG KIẾN THỨC VÀ BÀI KIỂM TRA TOÁN 11

Trang web tổng hợp toàn bộ kiến thức Toán học lớp 11 theo đúng chương trình GDPT mới nhất (áp dụng cho các bộ sách Kết nối tri thức, Cánh Diều, Chân trời sáng tạo).

---

## 🌟 Tính Năng Nổi Bật

1. **Tổng hợp đầy đủ 9 Chương theo sách giáo khoa**:
   - **TẬP 1 (Học kì I)**:
     - **Chương 1**: Hàm số lượng giác và phương trình lượng giác (4 bài học)
     - **Chương 2**: Dãy số. Cấp số cộng và cấp số nhân (3 bài học)
     - **Chương 3**: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm (2 bài học)
     - **Chương 4**: Quan hệ song song trong không gian (4 bài học)
     - **Chương 5**: Giới hạn. Hàm số liên tục (3 bài học)
   - **TẬP 2 (Học kì II)**:
     - **Chương 6**: Hàm số mũ và hàm số logarit (4 bài học)
     - **Chương 7**: Đạo hàm (3 bài học)
     - **Chương 8**: Quan hệ vuông góc trong không gian (4 bài học)
     - **Chương 9**: Các quy tắc tính xác suất (2 bài học)
2. **Hệ thống Bài kiểm tra trắc nghiệm cuối mỗi chương**:
   - Cuối mỗi chương đều có bài kiểm tra trắc nghiệm bao quát kiến thức.
   - Chấm điểm tự động và tính điểm ngay lập tức (thang điểm 10).
   - Lời giải chi tiết từng bước cho từng câu hỏi kèm hiển thị đáp án đúng/sai trực quan.
   - Chức năng làm lại bài kiểm tra và hiệu ứng chúc mừng điểm cao.
3. **Hiển thị công thức Toán học chuẩn quốc tế**:
   - Sử dụng thư viện **MathJax 3** kết xuất công thức LaTeX sắc nét, mượt mà ($ \sin, \cos, \lim, \int, \frac{a}{b}, \sqrt{x} $).
4. **Sổ tay tra cứu công thức nhanh (Cheat Sheet)**:
   - Tổng hợp tất cả công thức quan trọng có bộ lọc tìm kiếm theo từ khóa.
5. **Máy tính kiểm tra kết quả thông minh (Python SymPy Engine)**:
   - Tích hợp công cụ tính đạo hàm $f'(x)$, tính giới hạn $\lim f(x)$, giải phương trình đại số bằng Python SymPy trực tiếp trên web.
6. **Theo dõi tiến độ học tập & Chế độ Sáng / Tối (Dark Mode)**:
   - Lưu trữ tiến độ bài học vào `localStorage` của trình duyệt.

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Website

### Cách 1: Chạy trực tiếp bằng 1 cú click (Khuyên dùng trên Windows)
Nhấp đúp chuột vào file:
```
run.bat
```

### Cách 2: Chạy bằng dòng lệnh Terminal
1. Cài đặt các thư viện cần thiết (nếu chưa có):
```bash
pip install -r requirements.txt
```

2. Khởi động ứng dụng Flask:
```bash
python app.py
```

3. Mở trình duyệt web và truy cập địa chỉ:
```
http://127.0.0.1:5000
```

---

## 📂 Cấu Trúc Thư Mục Dự Án

```
Antigravity_test/
├── app.py                     # Máy chủ Flask chính & API giải toán
├── requirements.txt           # Danh sách thư viện Python
├── run.bat                    # Script khởi chạy 1-click trên Windows
├── test_app.py                # Bộ unit test tự động cho toàn bộ hệ thống
├── data/
│   ├── __init__.py            # Khởi tạo gói dữ liệu
│   ├── curriculum.py          # Bộ tổng hợp 9 chương, bài học & hàm tìm kiếm
│   ├── volume_1.py            # Dữ liệu Tập 1 (Chương 1 đến 5 + Bài kiểm tra)
│   ├── volume_2.py            # Dữ liệu Tập 2 (Chương 6 đến 9 + Bài kiểm tra)
│   └── formulas.py            # Dữ liệu sổ tay công thức tra cứu nhanh
├── templates/
│   ├── base.html              # Layout khung tổng thể (Navbar, Sidebar, MathJax, Dark Mode)
│   ├── index.html             # Trang chủ tổng quan & lộ trình học
│   ├── chapter.html           # Trang chi tiết một chương
│   ├── lesson.html            # Trang bài học chi tiết + mục tiêu + ví dụ
│   ├── quiz.html              # Trang bài kiểm tra trắc nghiệm tự chấm điểm
│   ├── formulas.html          # Trang sổ tay công thức toàn tập
│   ├── calculator.html        # Trang máy tính đại số giải tích SymPy
│   └── includes/
│       └── sidebar.html       # Sidebar điều hướng & thanh tiến độ học tập
└── static/
    ├── css/
    │   └── custom.css         # CSS tùy biến giao diện EdTech hiện đại
    └── js/
        └── main.js            # Xử lý giao diện, làm bài thi, lưu tiến độ, tìm kiếm
```
