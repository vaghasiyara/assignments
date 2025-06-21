import os
import difflib
from typing import List

def compare_texts(submitted: str, answers: List[str]) -> float:
    total_score = 0
    for answer in answers:
        match_ratio = difflib.SequenceMatcher(None, submitted, answer).ratio()
        total_score += match_ratio
    if answers:
        return round((total_score / len(answers)) * 100, 2)
    return 0.0

def generate_result(student_text: str, answer_texts: List[str]) -> dict:
    score = compare_texts(student_text, answer_texts)
    result = {
        "score": score,
        "remarks": "Excellent" if score > 80 else ("Average" if score > 50 else "Needs Improvement")
    }
    return result
