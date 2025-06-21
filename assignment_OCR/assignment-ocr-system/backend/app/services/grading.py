from datetime import datetime
from app.utils.similarity import compute_similarity

def check_late(submission_time: str, due_time: str) -> bool:
    fmt = "%Y-%m-%d %H:%M:%S"
    sub_time = datetime.strptime(submission_time, fmt)
    due = datetime.strptime(due_time, fmt)
    return sub_time > due

def count_answered_questions(text: str, total_questions: int = 5) -> int:
    count = 0
    for i in range(1, total_questions + 1):
        if f"Q{i}" in text or f"{i}." in text:
            count += 1
    return count

def extract_student_answers(text: str, total_questions: int = 5) -> dict:
    import re
    answers = {}
    for i in range(1, total_questions + 1):
        pattern = rf"(Q{i}|{i}\.)(.*?)(?=(Q{i+1}|{i+1}\.|$))"
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            answers[f"Q{i}"] = match.group(2).strip()
    return answers

def grade_submission(student_text: str, faculty_answers: dict, total_questions: int = 5) -> dict:
    student_answers = extract_student_answers(student_text, total_questions)
    results = {}
    total_score = 0

    for i in range(1, total_questions + 1):
        key = f"Q{i}"
        student_ans = student_answers.get(key, "")
        faculty_ans = faculty_answers.get(key, "")
        if student_ans and faculty_ans:
            sim = compute_similarity(student_ans, faculty_ans)
            results[key] = sim
            total_score += sim
        else:
            results[key] = 0.0

    avg_score = round(total_score / total_questions, 2)
    return {
        "per_question_similarity": results,
        "total_score": avg_score
    }
