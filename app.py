# -*- coding: utf-8 -*-
"""
Web ứng dụng Tổng hợp kiến thức và Trắc nghiệm Toán 11
Tác giả: Antigravity AI
Chạy trên nền tảng Python Flask
"""

import os
import sys
# Đảm bảo Python luôn tìm thấy thư mục gốc của dự án trên Linux / Render
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gzip
from flask import Flask, render_template, request, jsonify, redirect, url_for
from data.curriculum import (
    ALL_CHAPTERS,
    TOTAL_LESSONS,
    TOTAL_QUESTIONS,
    get_chapter,
    get_lesson,
    get_chapter_quiz,
    search_curriculum
)
from data.formulas import FORMULA_CATEGORIES
from data.error_log import ERROR_LOG_DATA
from data.exams import EXAM_LIST, get_exam

app = Flask(__name__)
app.config['SECRET_KEY'] = 'toan-11-antigravity-secret-key-2026'

# In-memory caching for ultra-fast rendering & zero latency
VOL1_CHAPTERS = [c for c in ALL_CHAPTERS if c['volume'] == 1]
VOL2_CHAPTERS = [c for c in ALL_CHAPTERS if c['volume'] == 2]
TOTAL_EXAMS = len(EXAM_LIST)
TOTAL_ERROR_LOGS = len(ERROR_LOG_DATA)
TOTAL_EXAM_QUESTIONS = sum(
    len(e.get('part1', [])) + len(e.get('part2', [])) + len(e.get('part3', []))
    for e in EXAM_LIST
)
TOTAL_ALL_QUESTIONS = TOTAL_QUESTIONS + TOTAL_EXAM_QUESTIONS

@app.context_processor
def inject_global_data():
    """Truyền danh sách chương và thông số vào mọi template (Cached)"""
    return {
        'all_chapters': ALL_CHAPTERS,
        'total_lessons': TOTAL_LESSONS,
        'total_questions': TOTAL_QUESTIONS,
        'total_all_questions': TOTAL_ALL_QUESTIONS,
        'vol1_chapters': VOL1_CHAPTERS,
        'vol2_chapters': VOL2_CHAPTERS,
        'total_exams': TOTAL_EXAMS,
        'total_error_logs': TOTAL_ERROR_LOGS
    }

@app.after_request
def add_performance_headers(response):
    """Tối ưu Cache-Control cho Static assets và nén Gzip"""
    if request.path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=604800'
    
    # Gzip response nếu client hỗ trợ và response là text/json/html > 500 bytes
    accept_encoding = request.headers.get('Accept-Encoding', '')
    if (
        'gzip' in accept_encoding.lower()
        and response.status_code == 200
        and not response.direct_passthrough
        and 'Content-Encoding' not in response.headers
        and any(ct in (response.content_type or '') for ct in ['text/', 'application/json', 'application/javascript'])
    ):
        content = response.get_data()
        if len(content) > 500:
            compressed = gzip.compress(content, compresslevel=6)
            response.set_data(compressed)
            response.headers['Content-Encoding'] = 'gzip'
            response.headers['Content-Length'] = len(compressed)
            
    return response

@app.route('/health')
@app.route('/healthz')
def healthz():
    """Healthcheck endpoint cho Render / Uptime Robot / PaaS"""
    return "OK", 200

@app.route('/')
def index():
    """Trang chủ: Tổng quan chương trình và lộ trình học"""
    return render_template('index.html')

@app.route('/chapter/<int:chapter_id>')
def chapter_detail(chapter_id):
    """Trang chi tiết một chương và danh sách bài học"""
    chapter = get_chapter(chapter_id)
    if not chapter:
        return redirect(url_for('index'))
    return render_template('chapter.html', chapter=chapter)

@app.route('/chapter/<int:chapter_id>/lesson/<int:lesson_id>')
def lesson_detail(chapter_id, lesson_id):
    """Trang nội dung bài học chi tiết"""
    chapter, lesson = get_lesson(chapter_id, lesson_id)
    if not chapter or not lesson:
        return redirect(url_for('index'))
    
    # Xác định bài trước và bài tiếp theo
    lesson_ids = [l['id'] for l in chapter['lessons']]
    curr_idx = lesson_ids.index(lesson['id'])
    
    prev_lesson = chapter['lessons'][curr_idx - 1] if curr_idx > 0 else None
    next_lesson = chapter['lessons'][curr_idx + 1] if curr_idx < len(chapter['lessons']) - 1 else None
    
    return render_template(
        'lesson.html',
        chapter=chapter,
        lesson=lesson,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson
    )

@app.route('/chapter/<int:chapter_id>/quiz')
def chapter_quiz(chapter_id):
    """Vô hiệu hóa an toàn route bài kiểm tra cuối chương - Điều hướng về chi tiết chương"""
    return redirect(url_for('chapter_detail', chapter_id=chapter_id))

@app.route('/formulas')
def formulas():
    """Trang tra cứu sổ tay công thức toàn bộ Toán 11 kèm Flashcard"""
    return render_template('formulas.html', categories=FORMULA_CATEGORIES)

@app.route('/hinh-hoc-3d')
def hinh_hoc_3d():
    """Phòng thí nghiệm hình học không gian 3D tương tác (Chương 4 & 8)"""
    return render_template('hinh_hoc_3d.html')

@app.route('/calculator')
def calculator():
    """Máy tính toán học (Chuyển tiếp hoặc hỗ trợ)"""
    return render_template('calculator.html')

@app.route('/error-log')
def error_log():
    """Trang Sổ tay lỗi sai (Hỗ trợ tương thích)"""
    return render_template('error_log.html', error_logs=ERROR_LOG_DATA)

@app.route('/exams')
def exams():
    """Phòng thi thử trực tuyến: Đề Giữa kì & Cuối kì chuẩn ma trận Hưng Yên 90 phút"""
    return render_template('exams.html', exams=EXAM_LIST)

@app.route('/exam/<exam_id>')
def exam_view(exam_id):
    """Trang làm bài thi thử trực tuyến kèm đồng hồ bấm giờ và chấm điểm tự động"""
    exam = get_exam(exam_id)
    if not exam:
        return redirect(url_for('exams'))
    return render_template('exam_view.html', exam=exam)

@app.route('/api/search')
def api_search():
    """API tìm kiếm bài học nhanh"""
    q = request.args.get('q', '').strip()
    results = search_curriculum(q)
    return jsonify({'results': results})

@app.route('/api/calc', methods=['POST'])
def api_calculate():
    """API giải toán sử dụng SymPy (Đạo hàm, Giới hạn, Giải phương trình)"""
    try:
        import sympy as sp
        data = request.get_json() or {}
        calc_type = data.get('type')
        expr_str = data.get('expression', '').strip()
        var_str = data.get('variable', 'x').strip() or 'x'
        target_str = data.get('target', '0').strip() or '0'
        
        if not expr_str:
            return jsonify({'success': False, 'error': 'Vui lòng nhập biểu thức toán!'})
            
        x = sp.Symbol(var_str)
        # Parse expression safely
        expr = sp.sympify(expr_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'e': sp.E, 'pi': sp.pi, 'ln': sp.log, 'log': sp.log, 'sqrt': sp.sqrt})
        
        result_latex = ""
        result_text = ""
        
        if calc_type == 'derivative':
            # Tính đạo hàm
            deriv = sp.diff(expr, x)
            result_latex = sp.latex(deriv)
            result_text = str(deriv)
        elif calc_type == 'limit':
            # Tính giới hạn
            if target_str in ['oo', '+oo', 'inf']:
                target = sp.oo
            elif target_str in ['-oo', '-inf']:
                target = -sp.oo
            else:
                target = sp.sympify(target_str)
            lim_val = sp.limit(expr, x, target)
            result_latex = sp.latex(lim_val)
            result_text = str(lim_val)
        elif calc_type == 'solve':
            # Giải phương trình expr = 0
            solutions = sp.solve(expr, x)
            result_latex = ", ".join([sp.latex(s) for s in solutions]) if solutions else "\\text{Vô nghiệm hoặc cần mở rộng}"
            result_text = str(solutions)
        else:
            return jsonify({'success': False, 'error': 'Loại phép tính không hợp lệ'})
            
        return jsonify({
            'success': True,
            'result_latex': result_latex,
            'result_text': result_text,
            'original_latex': sp.latex(expr)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': f"Lỗi tính toán: {str(e)}"})

def get_local_ip():
    """Lấy địa chỉ IP nội bộ của máy tính trong mạng Wi-Fi/LAN"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 65)
    print("🎓 WEBSITE TOÁN 11 MASTER ĐANG CHẠY...")
    print(f"💻 Mở trên MÁY TÍNH : http://localhost:5000 (hoặc http://127.0.0.1:5000)")
    print(f"📱 Mở trên ĐIỆN THOẠI: http://{local_ip}:5000")
    print("   👉 Lưu ý: Điện thoại & máy tính phải kết nối CÙNG mạng Wi-Fi!")
    print("=" * 65)
    app.run(host='0.0.0.0', port=5000, debug=True)
