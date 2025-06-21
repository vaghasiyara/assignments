import datetime

def check_all_questions_answered(text: str) -> bool:
    # Dummy check — you can improve this by pattern recognition
    required_keywords = ["Q1", "Q2", "Q3"]
    return all(q in text for q in required_keywords)

def is_late_submission(student_id: str) -> bool:
    # Dummy rule: if student_id ends with odd number, it's late
    try:
        return int(student_id[-1]) % 2 == 1
    except:
        return True  # If invalid, assume late

def load_faculty_answers(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return [""]  # Return empty default answer if missing
