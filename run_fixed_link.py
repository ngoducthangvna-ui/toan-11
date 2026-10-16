# -*- coding: utf-8 -*-
"""
Chạy website TOÁN 11 MASTER với ĐỊA CHỈ CỐ ĐỊNH KHÔNG ĐỔI
Sử dụng Localtunnel với subdomain cố định: toan11-thang.loca.lt
"""

import sys
import os
import re
import time
import socket
import threading
import subprocess
import urllib.request

# Thiết lập UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
SUBDOMAIN = "toan11-thang"

def get_public_ip():
    """Lấy IP công khai dùng làm mật khẩu mở trang lần đầu trên điện thoại"""
    try:
        req = urllib.request.Request("https://api.ipify.org", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as res:
            return res.read().decode().strip()
    except Exception:
        return "Xem tại https://loca.lt/mytunnelpassword"

def print_qr_code(url):
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        print("\n📱 QUÉT MÃ QR NÀY ĐỂ MỞ TRÊN ĐIỆN THOẠI:")
        qr.print_ascii(invert=True)
    except Exception:
        pass

def main():
    print("🚀 Đang khởi động website Toán 11...")
    from app import app
    import logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    flask_thread = threading.Thread(
        target=lambda: app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False),
        daemon=True
    )
    flask_thread.start()
    time.sleep(1.5)

    print(f"🌐 Đang kết nối địa chỉ cố định: https://{SUBDOMAIN}.loca.lt ...")
    cmd = f'cmd.exe /c "npx --yes localtunnel --port 5000 --subdomain {SUBDOMAIN}"'
    
    tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )

    fixed_url = None
    pattern = re.compile(rf'https://{SUBDOMAIN}\.loca\.lt')

    start = time.time()
    while time.time() - start < 20:
        line = tunnel_proc.stdout.readline()
        if not line:
            break
        if "your url is:" in line:
            m = re.search(r'https://[a-zA-Z0-9-]+\.loca\.lt', line)
            if m:
                fixed_url = m.group(0)
                break

    if not fixed_url:
        fixed_url = f"https://{SUBDOMAIN}.loca.lt"

    pub_ip = get_public_ip()

    # Tạo ảnh QR
    try:
        import qrcode
        img = qrcode.make(fixed_url)
        img.save(os.path.join(CURRENT_DIR, "qrcode_co_dinh.png"))
        img.save(os.path.join(ROOT_DIR, "qrcode_co_dinh.png"))
    except Exception:
        pass

    # Ghi ra file text
    info = f"""================================================================================
🎓 WEBSITE TOÁN 11 MASTER - ĐỊA CHỈ CỐ ĐỊNH DUY NHẤT VĨNH VIỄN
================================================================================

🌍 ĐƯỜNG LINK CỐ ĐỊNH CỦA BẠN (KHÔNG BAO GIỜ THAY ĐỔI):
👉 {fixed_url}

🔑 MẬT KHẨU XÁC NHẬN (chỉ cần nhập 1 lần duy nhất trên mỗi điện thoại):
   {pub_ip}
   (Khi điện thoại mở link lần đầu, trang web sẽ hỏi "Tunnel Password",
    bạn chỉ cần dán dãy số {pub_ip} này vào ô rồi bấm "Click to Submit" là xong!)

📱 MÃ QR: Xem file "qrcode_co_dinh.png"
💻 Mở trên máy tính này: http://localhost:5000
================================================================================
"""
    for p in [os.path.join(CURRENT_DIR, "LINK_CO_DINH.txt"), os.path.join(ROOT_DIR, "LINK_CO_DINH.txt")]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(info)

    print("\n" + "=" * 76)
    print("🎉 ĐÃ KÍCH HOẠT ĐỊA CHỈ CỐ ĐỊNH DUY NHẤT THÀNH CÔNG!")
    print("=" * 76)
    print(f"\n🌍 ĐƯỜNG LINK DUY NHẤT CỦA BẠN (CỐ ĐỊNH VĨNH VIỄN):")
    print(f"👉 \033[92m\033[1m{fixed_url}\033[0m")
    print(f"\n🔑 Mật khẩu xác nhận lần đầu mở trên điện thoại (Tunnel Password): \033[93m{pub_ip}\033[0m")
    print("   (Chỉ cần nhập dãy số trên 1 lần duy nhất, các lần sau bấm link là vào thẳng)")

    print_qr_code(fixed_url)

    print("-" * 76)
    print("💡 Giữ cửa sổ này mở để website hoạt động.")
    print("🛑 Bấm Ctrl + C để dừng.")
    print("=" * 76 + "\n")

    try:
        tunnel_proc.wait()
    except KeyboardInterrupt:
        tunnel_proc.terminate()
        print("Đã tắt máy chủ!")

if __name__ == '__main__':
    main()
