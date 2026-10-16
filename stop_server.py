# -*- coding: utf-8 -*-
"""
Dừng toàn bộ website Toán 11 và Cloudflare Tunnel đang chạy ngầm
"""

import sys
import os
import json
import subprocess
import ctypes

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
PID_FILE = os.path.join(CURRENT_DIR, "server_pids.json")

def stop():
    killed_any = False
    
    # 1. Kill theo PID lưu trong file
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            c_pid = data.get('cloudflared_pid')
            p_pid = data.get('python_pid')
            if c_pid:
                subprocess.run(f"taskkill /F /PID {c_pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                killed_any = True
            if p_pid:
                subprocess.run(f"taskkill /F /PID {p_pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                killed_any = True
            os.remove(PID_FILE)
        except Exception:
            pass

    # 2. Kill bất kỳ tiến trình cloudflared.exe nào còn sót
    subprocess.run("taskkill /F /IM cloudflared.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Kill tiến trình đang nghe cổng 5000 nếu có
    try:
        cmd = 'powershell -Command "Get-Process -Id (Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue).OwningProcess -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

    # 4. Cập nhật file LINK_TRUY_CAP.txt
    txt_files = [
        os.path.join(CURRENT_DIR, "LINK_TRUY_CAP.txt"),
        os.path.join(ROOT_DIR, "LINK_TRUY_CAP.txt")
    ]
    for tf in txt_files:
        if os.path.exists(tf):
            try:
                with open(tf, 'w', encoding='utf-8') as f:
                    f.write("Máy chủ website Toán 11 Master hiện ĐÃ ĐƯỢC TẮT.\nĐể khởi động lại, hãy nhấp đúp chuột vào file BAT_DAU_CHAY_NGAM.vbs!\n")
            except Exception:
                pass

    # 5. Thông báo hoàn tất
    print("Website Toán 11 Master đã được TẮT thành công!")
    try:
        import threading
        t = threading.Thread(
            target=lambda: ctypes.windll.user32.MessageBoxW(0, "Website Toán 11 Master đã được TẮT thành công!\nTất cả tiến trình chạy ngầm đã được giải phóng.", "Đã Tắt Thành Công", 0x40),
            daemon=True
        )
        t.start()
        t.join(timeout=3)
    except Exception:
        pass

if __name__ == '__main__':
    stop()
