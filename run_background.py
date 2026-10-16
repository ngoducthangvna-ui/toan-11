# -*- coding: utf-8 -*-
"""
Khởi động website TOÁN 11 MASTER chạy ngầm 100% trên Windows
Không có bất kỳ cửa sổ dòng lệnh (terminal) nào hiển thị.
Tự động lưu đường dẫn vào LINK_TRUY_CAP.txt và mở lên cho người dùng.
"""

import sys
import os
import re
import time
import json
import socket
import threading
import subprocess
import ctypes
import urllib.request

# Đảm bảo thư mục hiện tại
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
PID_FILE = os.path.join(CURRENT_DIR, "server_pids.json")
CLOUDFLARED_BIN = os.path.join(CURRENT_DIR, "cloudflared.exe")

def kill_previous_instances():
    """Tắt các phiên bản chạy ngầm trước đó nếu có"""
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            c_pid = data.get('cloudflared_pid')
            p_pid = data.get('python_pid')
            if c_pid:
                subprocess.run(f"taskkill /F /PID {c_pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if p_pid and p_pid != os.getpid():
                subprocess.run(f"taskkill /F /PID {p_pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # Giải phóng cổng 5000 nếu đang bị chiếm
    try:
        cmd = 'powershell -Command "Get-Process -Id (Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue).OwningProcess -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

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

def save_qr_code(url, target_paths):
    """Tạo file ảnh qrcode.png để người dùng quét"""
    try:
        import qrcode
        img = qrcode.make(url)
        for p in target_paths:
            img.save(p)
    except Exception:
        pass

def main():
    kill_previous_instances()

    # 1. Khởi chạy Flask Server trong luồng ngầm
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

    # 2. Khởi chạy Cloudflare Tunnel với cờ CREATE_NO_WINDOW (0x08000000)
    CREATE_NO_WINDOW = 0x08000000
    cmd = [CLOUDFLARED_BIN, "tunnel", "--url", "http://127.0.0.1:5000"]
    
    tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace',
        creationflags=CREATE_NO_WINDOW
    )

    # Lưu PIDs
    with open(PID_FILE, 'w', encoding='utf-8') as f:
        json.dump({'python_pid': os.getpid(), 'cloudflared_pid': tunnel_proc.pid}, f)

    public_url = None
    pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    # Đọc output để lấy link https://...
    start_time = time.time()
    while time.time() - start_time < 30:
        line = tunnel_proc.stdout.readline()
        if not line:
            break
        match = pattern.search(line)
        if match:
            public_url = match.group(0)
            break

    if not public_url:
        ctypes.windll.user32.MessageBoxW(0, "Không thể kết nối Internet để tạo link online. Vui lòng kiểm tra lại mạng!", "Lỗi Khởi Động", 0x10)
        tunnel_proc.terminate()
        return

    local_ip = get_local_ip()

    # 3. Tạo file ảnh mã QR qrcode.png
    qr_files = [
        os.path.join(CURRENT_DIR, "qrcode.png"),
        os.path.join(ROOT_DIR, "qrcode.png")
    ]
    save_qr_code(public_url, qr_files)

    # 4. Ghi thông tin kết nối ra file LINK_TRUY_CAP.txt
    info_text = f"""================================================================================
🎓 WEBSITE TOÁN 11 MASTER - ĐANG CHẠY NGẦM THÀNH CÔNG!
(Website vẫn đang chạy bình thường, bạn KHÔNG cần mở bất kỳ cửa sổ nào)
================================================================================

🌍 ĐƯỜNG LINK MỞ TRÊN ĐIỆN THOẠI (BẤT KỲ MẠNG 4G / 5G / WIFI NÀO CŨNG VÀO ĐƯỢC):
👉 {public_url}

📱 CÁCH MỞ:
1. Sao chép đường link trên gửi vào Zalo, Messenger hoặc gõ vào điện thoại.
2. Hoặc mở file ảnh "qrcode.png" trong thư mục này để quét mã bằng Camera/Zalo!

--------------------------------------------------------------------------------
📌 CÁC ĐỊA CHỈ KHÁC:
💻 Mở trên máy tính này : http://localhost:5000 (hoặc http://127.0.0.1:5000)
📶 Mở trên cùng Wi-Fi   : http://{local_ip}:5000
--------------------------------------------------------------------------------
🛑 ĐỂ TẮT TRANG WEB KHI KHÔNG DÙNG NỮA:
Nhấp đúp chuột vào file: "TAT_TRANG_WEB.bat" là xong!
================================================================================
"""

    txt_files = [
        os.path.join(CURRENT_DIR, "LINK_TRUY_CAP.txt"),
        os.path.join(ROOT_DIR, "LINK_TRUY_CAP.txt")
    ]
    for tf in txt_files:
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(info_text)

    # 5. Tự động mở file LINK_TRUY_CAP.txt bằng Notepad lên để người dùng thấy link
    try:
        os.startfile(txt_files[1])
    except Exception:
        pass

    # 6. Hiện thông báo pop-up chúc mừng (chạy luồng riêng để không chặn tiến trình)
    msg_box_text = f"Website Toán 11 Master đang CHẠY NGẦM thành công!\n\nĐường link mở trên điện thoại (4G/5G/Wi-Fi):\n{public_url}\n\n(File LINK_TRUY_CAP.txt đã được mở sẵn cho bạn sao chép)"
    threading.Thread(
        target=lambda: ctypes.windll.user32.MessageBoxW(0, msg_box_text, "Toán 11 Master - Đang Chạy Ngầm", 0x40),
        daemon=True
    ).start()

    # Giữ tiến trình chạy ngầm
    try:
        tunnel_proc.wait()
    except Exception:
        pass

if __name__ == '__main__':
    main()
