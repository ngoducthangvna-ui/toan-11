# -*- coding: utf-8 -*-
"""
Bộ dữ liệu trung tâm chương trình Toán 11
Tổng hợp 9 chương, đầy đủ lý thuyết các bài học và bài kiểm tra cuối chương.
"""

import unicodedata
from .volume_1 import VOLUME_1_CHAPTERS
from .volume_2 import VOLUME_2_CHAPTERS

ALL_CHAPTERS = VOLUME_1_CHAPTERS + VOLUME_2_CHAPTERS

TOTAL_LESSONS = sum(len(c["lessons"]) for c in ALL_CHAPTERS)
TOTAL_QUESTIONS = sum(len(c["quiz"]["questions"]) for c in ALL_CHAPTERS)

def normalize_text(text):
    """Chuẩn hóa tiếng Việt bỏ dấu để tìm kiếm thông minh"""
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', str(text))
    return "".join(c for c in nfkd if not unicodedata.combining(c)).replace('đ', 'd').replace('Đ', 'D').lower()

def get_chapter(chapter_id):
    """Lấy thông tin chi tiết một chương theo ID (1 đến 9)"""
    for ch in ALL_CHAPTERS:
        if ch["id"] == int(chapter_id):
            return ch
    return None

def get_lesson(chapter_id, lesson_id):
    """Lấy thông tin chi tiết một bài học theo ID"""
    ch = get_chapter(chapter_id)
    if not ch:
        return None, None
    for les in ch["lessons"]:
        if les["id"] == int(lesson_id):
            return ch, les
    return ch, None

def get_chapter_quiz(chapter_id):
    """Lấy bài kiểm tra trắc nghiệm cuối chương"""
    ch = get_chapter(chapter_id)
    if ch and "quiz" in ch:
        return ch, ch["quiz"]
    return None, None

def search_curriculum(query):
    """Tìm kiếm thông minh bài học, chương và công thức theo từ khóa có dấu và không dấu"""
    if not query:
        return []
    raw_query = query.strip().lower()
    norm_query = normalize_text(query)
    results = []

    for ch in ALL_CHAPTERS:
        ch_title_norm = normalize_text(ch["title"])
        ch_sum_norm = normalize_text(ch.get("summary", ""))
        
        # Check chapter match
        if (raw_query in ch["title"].lower() or norm_query in ch_title_norm or 
            raw_query in ch.get("summary", "").lower() or norm_query in ch_sum_norm):
            results.append({
                "type": "chapter",
                "chapter_id": ch["id"],
                "title": ch["title"],
                "subtitle": f"Tập {ch['volume']} • {len(ch['lessons'])} bài học",
                "url": f"/chapter/{ch['id']}"
            })

        # Check lessons match
        for les in ch["lessons"]:
            les_title_norm = normalize_text(les["title"])
            les_content_norm = normalize_text(les.get("content", ""))

            if (raw_query in les["title"].lower() or norm_query in les_title_norm or
                raw_query in les.get("content", "").lower() or norm_query in les_content_norm):
                results.append({
                    "type": "lesson",
                    "chapter_id": ch["id"],
                    "lesson_id": les["id"],
                    "title": les["title"],
                    "subtitle": ch["title"],
                    "url": f"/chapter/{ch['id']}/lesson/{les['id']}"
                })
    return results
