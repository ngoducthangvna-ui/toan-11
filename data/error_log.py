# -*- coding: utf-8 -*-
"""
Sổ tay lỗi sai (Error Log) - 10 sai lầm kinh điển của học sinh
Chương 1: Hàm số & Phương trình Lượng giác
Chương 4: Quan hệ song song trong không gian
Bộ sách Kết nối tri thức với cuộc sống
"""

ERROR_LOG_DATA = [
    {
        "id": 1,
        "chapter_id": 1,
        "chapter_title": "Chương 1: Lượng giác",
        "category": "Điều kiện xác định",
        "title": "Quên đặt điều kiện xác định của hàm số tan(x) và cot(x)",
        "scenario": r"Khi giải phương trình $\tan(2x - \frac{\pi}{4}) = \sqrt{3}$ hoặc $\cot x = 1$, học sinh thường vội vã dùng công thức nghiệm $2x - \frac{\pi}{4} = \frac{\pi}{3} + k\pi$ mà quên mất điều kiện $\cos(2x - \frac{\pi}{4}) \neq 0$. Dẫn đến khi gặp các bài toán chứa đồng thời mẫu số hoặc phương trình tương đương, các nghiệm ngoại lai không bị loại bỏ, gây mất điểm trọn bài.",
        "warning_ui": {
            "type": "danger",
            "badge": "BẪY TỬ THỦY 01",
            "title": "CẢNH BÁO: ĐIỀU KIỆN ẨN CỦA TAN VÀ COT!",
            "message": r"Cứ nhìn thấy biểu thức có chứa $\tan u$ hoặc $\cot u$, phản xạ số 1 trước khi viết bất kỳ chữ nào là: ĐIỀU KIỆN ĐÂU? $\tan u \implies u \neq \frac{\pi}{2} + k\pi$; $\cot u \implies u \neq k\pi$."
        },
        "mnemonic": "TAN sợ NỬA PI (π/2 + kπ) - COT sợ NGUYÊN PI (kπ). Thấy Tan/Cot là Mở Vòng Tròn Phanh Lại Đặt Điều Kiện Ngay!"
    },
    {
        "id": 2,
        "chapter_id": 1,
        "chapter_title": "Chương 1: Lượng giác",
        "category": "Phương trình cơ bản",
        "title": "Rơi rụng họ nghiệm bù khi giải phương trình sin(x) = m",
        "scenario": r"Khi giải phương trình $\sin x = \frac{1}{2}$, rất nhiều bạn chỉ viết $x = \frac{\pi}{6} + k2\pi$ và dừng lại, quên hẳn họ nghiệm bù $x = \pi - \frac{\pi}{6} + k2\pi = \frac{5\pi}{6} + k2\pi$. Lỗi này làm mất 50% số điểm của câu giải phương trình lượng giác.",
        "warning_ui": {
            "type": "warning",
            "badge": "BẪY THIẾU NGHIỆM 02",
            "title": "CẢNH BÁO: SIN PHẢI CÓ 2 NHÁNH ĐỐI XỨNG!",
            "message": r"Trục $\sin$ là trục đứng. Một đường cắt ngang luôn cắt đường tròn tại 2 điểm đối xứng qua trục tung: Góc $\alpha$ và góc bù $(\pi - \alpha)$. Thiếu nhánh bù là rơi rụng nửa số điểm!"
        },
        "mnemonic": "SIN BÙ - COS ĐỐI: Sin lấy (Alpha) và (Pi trừ Alpha); Cos lấy (Cộng trừ Alpha)."
    },
    {
        "id": 3,
        "chapter_id": 1,
        "chapter_title": "Chương 1: Lượng giác",
        "category": "Biến đổi đại số",
        "title": "Quên dấu cộng trừ (±) khi khai căn hoặc hạ bậc",
        "scenario": r"Từ hệ thức $\cos^2 x = \frac{3}{4}$, học sinh vội vàng suy ra $\cos x = \frac{\sqrt{3}}{2}$ mà bỏ qua trường hợp $\cos x = -\frac{\sqrt{3}}{2}$. Hoặc khi biết $\sin x = \frac{3}{5}$ trên khoảng $(\frac{\pi}{2}; \pi)$, tính $\cos x = \sqrt{1 - \sin^2 x} = \frac{4}{5}$ (quên xét dấu âm của góc phần tư thứ II).",
        "warning_ui": {
            "type": "danger",
            "badge": "BẪY DẤU CĂN 03",
            "title": "CẢNH BÁO: KHAI CĂN BẬC HAI BẮT BUỘC CÓ DẤU TRỪ!",
            "message": r"$X^2 = A \implies X = \pm\sqrt{A}$. Luôn xác định vị trí góc phần tư trên đường tròn lượng giác trước khi chốt dấu của $\cos, \sin, \tan$."
        },
        "mnemonic": "Khai căn nhớ có CỘNG TRỪ. Góc phần tư quyết định DẤU: Nhất cả (I: all +), Nhì sin (II: sin +), Tam tan (III: tan/cot +), Tứ cos (IV: cos +)."
    },
    {
        "id": 4,
        "chapter_id": 1,
        "chapter_title": "Chương 1: Lượng giác",
        "category": "Chu kỳ tuần hoàn",
        "title": "Râu ông nọ cắm cằm bà kia: Lộn xộn chu kỳ k2π và kπ",
        "scenario": r"Nhiều bạn giải phương trình $\tan x = 1$ lại ghi kết quả là $x = \frac{\pi}{4} + k2\pi$, hoặc giải $\cos x = 0$ lại ghi đuôi $k2\pi$. Sai sót đuôi chu kỳ khiến toàn bộ bài toán đếm số nghiệm trên một khoảng bị sai hoàn toàn.",
        "warning_ui": {
            "type": "info",
            "badge": "BẪY CHU KỲ 04",
            "title": "CẢNH BÁO: PHÂN BIỆT ĐUÔI kπ VÀ k2π",
            "message": r"Phương trình $\sin x = m, \cos x = m$ (với $m \neq 0, 1, -1$) đuôi là $+ k2\pi$. Phương trình $\tan x = m, \cot x = m$ và trường hợp đặc biệt bằng $0$ ($\sin x = 0, \cos x = 0$) đuôi chỉ là $+ k\pi$!"
        },
        "mnemonic": "Sin, Cos đi TRỌN VÒNG (2π) - Tan, Cot chỉ NỬA VÒNG (π). Bằng 0 xuyên tâm nửa vòng (+ kπ), Bằng 1 chạm đỉnh trọn vòng (+ k2π)."
    },
    {
        "id": 5,
        "chapter_id": 1,
        "chapter_title": "Chương 1: Lượng giác",
        "category": "Đơn vị đo góc",
        "title": "Trộn lẫn đơn vị Độ (°) và Radian trong cùng một biểu thức",
        "scenario": r"Học sinh viết: $x = 30^\circ + k2\pi$ hoặc $\sin(x + 45^\circ) = \cos(x + \frac{\pi}{3})$. Đây là lỗi cấm kỵ trong toán học, bị trừ điểm tuyệt đối vì hai hệ đơn vị khác nhau hoàn toàn.",
        "warning_ui": {
            "type": "warning",
            "badge": "LỖI HỆ ĐƠN VỊ 05",
            "title": "CẢNH BÁO: CHỌN MỘT VÀ CHỈ MỘT HỆ ĐƠN VỊ!",
            "message": r"Nếu đề bài cho độ: nghiệm phải là $x = 30^\circ + k360^\circ$. Nếu đề cho radian: nghiệm phải là $x = \frac{\pi}{6} + k2\pi$. Tuyệt đối không bao giờ trộn lẫn cả hai."
        },
        "mnemonic": "Độ đi với 360° - Radian đi với Pi (2π). Giống như đo chiều dài, không bao giờ viết 1 mét + 5 inch!"
    },
    {
        "id": 6,
        "chapter_id": 4,
        "chapter_title": "Chương 4: Hình học không gian",
        "category": "Vị trí tương đối",
        "title": "Ngộ nhận hai đường thẳng không cắt nhau là song song (Quên chéo nhau)",
        "scenario": r"Trong hình chóp $S.ABCD$, học sinh thấy đoạn $AB$ và $SC$ không cắt nhau liền kết luận ngay $AB // SC$. Trong không gian, hai đường thẳng không có điểm chung có thể chéo nhau nếu chúng không cùng nằm trong một mặt phẳng.",
        "warning_ui": {
            "type": "danger",
            "badge": "BẪY KHÔNG GIAN 06",
            "title": "CẢNH BÁO: HAI ĐƯỜNG THẲNG KHÔNG GIAO NHAU CHƯA CHẮC SONG SONG!",
            "message": r"Chỉ được kết luận song song khi đã chứng minh chúng ĐỒNG PHẲNG. Không cùng nằm trong một mặt phẳng thì chúng CHÉO NHAU!"
        },
        "mnemonic": "Muốn song song: Phải CÙNG MỘT NHÀ (đồng phẳng) và KHÔNG ĐƯỢC CHẠM NHAU. Khác nhà mà không chạm thì là CHÉO NHAU!"
    },
    {
        "id": 7,
        "chapter_id": 4,
        "chapter_title": "Chương 4: Hình học không gian",
        "category": "Giao điểm trong không gian",
        "title": "Tự tiện kẻ hai đường thẳng cắt nhau khi chưa đồng phẳng",
        "scenario": r"Cho hình chóp $S.ABCD$. Học sinh nối $SO$ (với $O$ là tâm đáy) và kéo dài cạnh $AB$ cho chúng cắt nhau tại $K$. Đây là lỗi ngộ nhận hình phẳng: $SO$ nằm trong mặt phẳng đứng $(SAC)$ hoặc $(SBD)$, còn $AB$ nằm ở đáy $(ABCD)$, chúng không đồng phẳng nên trong không gian chúng chéo nhau, không thể cắt nhau!",
        "warning_ui": {
            "type": "danger",
            "badge": "LỖI ĐỒNG PHẲNG 07",
            "title": "CẢNH BÁO: CHỈ ĐƯỢC CẮT NHAU KHI NẰM TRONG CÙNG 1 MẶT PHẲNG!",
            "message": r"Trước khi ghi câu: 'Gọi $I = a \cap b$', luôn tự trả lời câu hỏi: $a$ và $b$ cùng nằm trong mặt phẳng nào? Không chỉ ra được mặt phẳng đó là SAI NGAY LẬP TỨC."
        },
        "mnemonic": "Cùng mẹ sinh ra (Cùng thuộc 1 mp) mới được chạm nhau. Khác mặt phẳng mà kéo dài cho cắt nhau là ảo tưởng hình vẽ!"
    },
    {
        "id": 8,
        "chapter_id": 4,
        "chapter_title": "Chương 4: Hình học không gian",
        "category": "Đường song song mặt phẳng",
        "title": "Chứng minh d // (P) nhưng quên điều kiện d không nằm trong (P)",
        "scenario": r"Học sinh chứng minh được $d // d'$ với $d' \subset (P)$, rồi vội vã kết luận $d // (P)$. Nếu chẳng may $d$ cũng nằm luôn trong mặt phẳng $(P)$ thì định lí không còn đúng ($d \subset (P)$ chứ không phải $d // (P)$).",
        "warning_ui": {
            "type": "warning",
            "badge": "THIẾU ĐIỀU KIỆN 08",
            "title": "CẢNH BÁO: BẮT BUỘC PHẢI CÓ $d \\not\\subset (P)$",
            "message": r"Định lý đầy đủ: Nếu đường thẳng $d$ KHÔNG NẰM TRONG $(P)$ và song song với một đường thẳng $d' \subset (P)$ thì $d // (P)$."
        },
        "mnemonic": "Ba điều kiện vàng: $d$ ở ngoài $(P)$ - $d'$ ở trong $(P)$ - $d$ song song $d'$. Thiếu một trong ba là mất điểm trình bày!"
    },
    {
        "id": 9,
        "chapter_id": 4,
        "chapter_title": "Chương 4: Hình học không gian",
        "category": "Tìm giao tuyến",
        "title": "Tìm giao tuyến chỉ chăm chăm tìm 2 điểm chung mà quên định lý giao tuyến song song",
        "scenario": r"Khi tìm giao tuyến của 2 mặt phẳng chứa 2 đường thẳng song song (như $(SAB)$ và $(SCD)$ có $AB // CD$), học sinh loay hoay cố gắng kéo dài các cạnh để tìm điểm chung thứ hai, dẫn đến kéo dài $AB$ và $CD$ cắt nhau (trong khi chúng song song, không thể cắt nhau).",
        "warning_ui": {
            "type": "info",
            "badge": "CHIẾN THUẬT GIAO TUYẾN 09",
            "title": "CẢNH BÁO: CÓ CẶP CẠNH SONG SONG $\\implies$ GIAO TUYẾN SONG SONG!",
            "message": r"Nếu hai mặt phẳng chứa hai đường thẳng song song thì giao tuyến của chúng (nếu có) phải song song với hai đường thẳng đó (hoặc trùng với một trong hai)."
        },
        "mnemonic": r"Hai mặt phẳng có 1 điểm chung + 2 đường song song $\implies$ Kẻ qua điểm chung đường thẳng song song với 2 đường đó là ra giao tuyến trong 5 giây!"
    },
    {
        "id": 10,
        "chapter_id": 4,
        "chapter_title": "Chương 4: Hình học không gian",
        "category": "Tư duy hình học phẳng sang không gian",
        "title": "Bê nguyên tính chất hình học phẳng áp dụng bừa bãi vào không gian",
        "scenario": r"Học sinh cho rằng: 'Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì song song với nhau'. Điều này ĐÚNG trong hình học phẳng, nhưng SAI HOÀN TOÀN trong hình học không gian (ví dụ 3 cạnh của góc bàn cùng vuông góc với nhau từng đôi một: trục Ox, Oy, Oz cùng vuông góc nhưng không hề song song).",
        "warning_ui": {
            "type": "danger",
            "badge": "TƯ DUY ẢO 10",
            "title": "CẢNH BÁO: ĐỪNG MANG LUẬT PHẲNG VÀO KHÔNG GIAN 3D!",
            "message": r"Trong không gian, có vô số đường thẳng cùng vuông góc hoặc cùng tạo một góc với đường thẳng cho trước (tạo thành một mặt nón hoặc mặt phẳng vuông góc)."
        },
        "mnemonic": "Luật 2D chưa chắc đúng trong 3D. Muốn áp dụng định lý phẳng, phải nhốt tất cả vào CÙNG MỘT MẶT PHẲNG trước!"
    }
]
