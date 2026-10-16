# -*- coding: utf-8 -*-
"""
Bộ dữ liệu trung tâm chương trình Toán 11
Tổng hợp 9 chương, đầy đủ lý thuyết các bài học và bài kiểm tra cuối chương.
"""

from .volume_1 import VOLUME_1_CHAPTERS
from .volume_2 import VOLUME_2_CHAPTERS

ALL_CHAPTERS = VOLUME_1_CHAPTERS + VOLUME_2_CHAPTERS

TOTAL_LESSONS = sum(len(c["lessons"]) for c in ALL_CHAPTERS)
TOTAL_QUESTIONS = sum(len(c["quiz"]["questions"]) for c in ALL_CHAPTERS)

def get_chapter(chapter_id):
    """Lấy thông tin chi tiết một chương theo ID (1 đến 9)"""
    for ch in ALL_CHAPTERS:
        if ch["id"] == int(chapter_id):
            return ch
    return None

def get_lesson(chapter_id, lesson_id):
    """Lấy thông tin chi tiết một bài học theo ID chương và ID bài học"""
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
    """Tìm kiếm bài học và chương theo từ khóa"""
    if not query:
        return []
    query_lower = query.lower().strip()
    results = []
    for ch in ALL_CHAPTERS:
        # Check chapter match
        if query_lower in ch["title"].lower() or query_lower in ch["summary"].lower():
            results.append({
                "type": "chapter",
                "chapter_id": ch["id"],
                "title": ch["title"],
                "subtitle": f"Tập {ch['volume']} • {len(ch['lessons'])} bài học",
                "url": f"/chapter/{ch['id']}"
            })
        # Check lessons match
        for les in ch["lessons"]:
            if query_lower in les["title"].lower() or query_lower in les["content"].lower():
                results.append({
                    "type": "lesson",
                    "chapter_id": ch["id"],
                    "lesson_id": les["id"],
                    "title": les["title"],
                    "subtitle": ch["title"],
                    "url": f"/chapter/{ch['id']}/lesson/{les['id']}"
                })
    return results
