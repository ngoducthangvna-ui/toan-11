# -*- coding: utf-8 -*-
"""Test suite for Math 11 Flask Web App"""
import unittest
from app import app
from data.curriculum import ALL_CHAPTERS

class Math11AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('TOÁN 11 MASTER'.encode('utf-8'), response.data)

    def test_all_chapters(self):
        import html
        for ch in ALL_CHAPTERS:
            res = self.app.get(f'/chapter/{ch["id"]}')
            self.assertEqual(res.status_code, 200, f"Chapter {ch['id']} failed")
            expected_title = html.escape(ch['short_title'])
            self.assertIn(expected_title.encode('utf-8'), res.data)

    def test_all_first_lessons(self):
        for ch in ALL_CHAPTERS:
            first_les = ch['lessons'][0]
            res = self.app.get(f'/chapter/{ch["id"]}/lesson/{first_les["id"]}')
            self.assertEqual(res.status_code, 200, f"Lesson ch{ch['id']}_les{first_les['id']} failed")

    def test_all_quizzes(self):
        import html
        for ch in ALL_CHAPTERS:
            res = self.app.get(f'/chapter/{ch["id"]}/quiz')
            self.assertEqual(res.status_code, 200, f"Quiz for Chapter {ch['id']} failed")
            expected_title = html.escape(ch['quiz']['title'])
            self.assertIn(expected_title.encode('utf-8'), res.data)

    def test_formulas_page(self):
        res = self.app.get('/formulas')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Sổ Tay Công Thức'.encode('utf-8'), res.data)

    def test_calculator_page(self):
        res = self.app.get('/calculator')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Máy Tính Hỗ Trợ Kiểm Tra Kết Quả'.encode('utf-8'), res.data)

    def test_search_api(self):
        res = self.app.get('/api/search?q=lượng giác')
        self.assertEqual(res.status_code, 200)
        json_data = res.get_json()
        self.assertTrue(len(json_data['results']) > 0)

    def test_calculator_api_derivative(self):
        res = self.app.post('/api/calc', json={
            'type': 'derivative',
            'expression': 'x**3 - 3*x**2 + 5'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('3*x**2 - 6*x', data['result_text'])

    def test_calculator_api_limit(self):
        res = self.app.post('/api/calc', json={
            'type': 'limit',
            'expression': '(x**2 - 1)/(x - 1)',
            'target': '1'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
    def test_error_log_page(self):
        res = self.app.get('/error-log')
        self.assertEqual(res.status_code, 200)
        self.assertIn('SỔ TAY LỖI SAI (ERROR LOG)'.encode('utf-8'), res.data)
        self.assertIn('BẪY TỬ THỦY'.encode('utf-8'), res.data)

    def test_exams_page(self):
        res = self.app.get('/exams')
        self.assertEqual(res.status_code, 200)
        self.assertIn('PHÒNG THI THỬ TRỰC TUYẾN 90 PHÚT'.encode('utf-8'), res.data)

    def test_exam_detail_midterm(self):
        res = self.app.get('/exam/de-giua-ki-1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Giữa Học Kì 1'.encode('utf-8'), res.data)

    def test_exam_detail_final(self):
        res = self.app.get('/exam/de-cuoi-ki-1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Cuối Học Kì 1'.encode('utf-8'), res.data)

    def test_lesson_3_engineer_content(self):
        res = self.app.get('/chapter/1/lesson/3')
        self.assertEqual(res.status_code, 200)
        self.assertIn('GÓC NHÌN TỪ KỸ SƯ'.encode('utf-8'), res.data)
        self.assertIn('Checklist'.encode('utf-8'), res.data)

    def test_hinh_hoc_3d_page(self):
        res = self.app.get('/hinh-hoc-3d')
        self.assertEqual(res.status_code, 200)
        self.assertIn('MÔ HÌNH HÌNH HỌC KHÔNG GIAN 3D'.encode('utf-8'), res.data)

    def test_healthz(self):
        res = self.app.get('/healthz')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode('utf-8'), "OK")

    def test_all_11_exams(self):
        from data.exams import EXAM_LIST
        self.assertEqual(len(EXAM_LIST), 11)
        for ex in EXAM_LIST:
            eid = ex['id']
            res = self.app.get(f'/exam/{eid}')
            self.assertEqual(res.status_code, 200, f"Exam {eid} failed")
            self.assertEqual(len(ex['part1']), 12, f"Exam {eid} Part 1 must have 12 questions")
            self.assertEqual(len(ex['part2']), 4, f"Exam {eid} Part 2 must have 4 questions")
            self.assertEqual(len(ex['part3']), 6, f"Exam {eid} Part 3 must have 6 questions")

if __name__ == '__main__':
    unittest.main()
