# -*- coding: utf-8 -*-
"""
Chạy website TOÁN 11 MASTER ở chế độ Trực Tuyến Toàn Cầu
Sử dụng Cloudflare Tunnel bảo mật cao (HTTPS)
Bất kỳ điện thoại nào ở bất kỳ đâu (4G, 5G, Wi-Fi khác mạng) đều truy cập được ngay lập tức!
"""

import sys
import os
import re
import time
import subprocess
import threading
import urllib.request
import socket

# Thiết lập bảng mã UTF-8 cho console Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CLOUDFLARED_URL = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
CLOUDFLARED_BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cloudflared.exe")

def ensure_cloudflared():
    """Kiểm tra và tự động tải cloudflared.exe nếu chưa có"""
    if not os.path.exists(CLOUDFLARED_BIN):
        print("⏳ Đang tải công cụ kết nối đám mây Cloudflare (chỉ tải 1 lần duy nhất)...")
        urllib.request.urlretrieve(CLOUDFLARED_URL, CLOUDFLARED_BIN)
        print("✅ Đã sẵn sàng!")

def get_local_ip():
    """Lấy IP mạng nội bộ"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def print_qr_code(url):
    """In mã QR trực tiếp ra màn hình Terminal để quét bằng camera điện thoại"""
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        print("\n📱 QUÉT MÃ QR NÀY BẰNG CAMERA ĐIỆN THOẠI HOẶC ZALO ĐỂ MỞ NGAY:")
        qr.print_ascii(invert=True)
    except Exception as e:
        pass

def main():
    ensure_cloudflared()

    # 1. Khởi chạy Flask Server trong luồng ngầm
    print("🚀 Đang khởi động máy chủ Flask...")
    from app import app
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    flask_thread = threading.Thread(
        target=lambda: app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False),
        daemon=True
    )
    flask_thread.start()
    time.sleep(1.5)

    # 2. Khởi chạy Cloudflare Tunnel để tạo link công khai toàn cầu
    print("🌐 Đang tạo đường dẫn phát trực tuyến toàn cầu (Cloudflare Tunnel)...")
    cmd = [CLOUDFLARED_BIN, "tunnel", "--url", "http://127.0.0.1:5000"]
    
    tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )

    public_url = None
    pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    # Đọc output để trích xuất link https://...
    while tunnel_proc.poll() is None:
        line = tunnel_proc.stdout.readline()
        if not line:
            break
        match = pattern.search(line)
        if match:
            public_url = match.group(0)
            break

    if not public_url:
        print("❌ Không thể tạo đường dẫn công khai. Vui lòng kiểm tra lại kết nối Internet.")
        tunnel_proc.terminate()
        return

    local_ip = get_local_ip()

    # 3. Hiển thị thông tin kết nối
    print("\n" + "=" * 76)
    print("🎉 CHÚC MỪNG! WEBSITE TOÁN 11 MASTER ĐÃ ĐƯỢC PHÁT TRỰC TUYẾN TOÀN CẦU")
    print("=" * 76)
    print(f"\n🌍 ĐƯỜNG LINK CÔNG KHAI (MỞ TỪ BẤT CỨ ĐÂU - 4G, 5G, WIFI BẤT KỲ):")
    print(f"👉 \033[92m\033[1m{public_url}\033[0m")
    print("   (Gửi link trên qua Zalo, Messenger hoặc gõ vào điện thoại để mở)")

    print_qr_code(public_url)

    print("-" * 76)
    print("📌 CÁC ĐỊA CHỈ TRUY CẬP KHÁC:")
    print(f"💻 Trên máy tính này : http://localhost:5000")
    print(f"📶 Trong cùng Wi-Fi  : http://{local_ip}:5000")
    print("-" * 76)
    print("💡 Giữ cửa sổ này mở để website tiếp tục hoạt động.")
    print("🛑 Nhấn tổ hợp phím [Ctrl + C] khi bạn muốn dừng máy chủ.")
    print("=" * 76 + "\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nĐang tắt máy chủ...")
        tunnel_proc.terminate()
        tunnel_proc.wait()
        print("Đã tắt an toàn!")

if __name__ == '__main__':
    main()
