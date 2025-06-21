import os
from difflib import SequenceMatcher
from .ocr_service import extract_text_from_path

# Get the latest uploaded answer key
def get_latest_answer_key_text(answer_key_dir):
    files = sorted(
        [f for f in os.listdir(answer_key_dir) if f.endswith((".png", ".jpg", ".jpeg", ".pdf"))],
        key=lambda x: os.path.getmtime(os.path.join(answer_key_dir, x)),
        reverse=True
    )
    if not files:
        return None
    latest_file_path = os.path.join(answer_key_dir, files[0])
    return extract_text_from_path(latest_file_path)

# Compare OCR text from student vs faculty
def calculate_match_score(student_text, answer_key_text):
    matcher = SequenceMatcher(None, student_text.lower(), answer_key_text.lower())
    return round(matcher.ratio() * 100, 2)
