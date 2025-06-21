import os
from difflib import SequenceMatcher
from datetime import datetime

ANSWER_KEY_PATH = "uploaded_answer_keys/latest_answer_key.txt"

def evaluate_assignment(text: str, submission_date: str, deadline_date: str) -> dict:
    score = 0
    max_score = 100

    # ✅ Check if all questions are attempted (simplified logic)
    question_keywords = ["Q1", "Q2", "Q3"]
    answered = all(q.lower() in text.lower() for q in question_keywords)
    if answered:
        score += 30

    # ✅ Compare with faculty answer key
    if os.path.exists(ANSWER_KEY_PATH):
        with open(ANSWER_KEY_PATH, "r") as f:
            answer_key = f.read()

        match_ratio = SequenceMatcher(None, text, answer_key).ratio()
        score += int(match_ratio * 60)  # up to 60 points for content match

    # ✅ Check for late submission
    submission_dt = datetime.strptime(submission_date, "%Y-%m-%d")
    deadline_dt = datetime.strptime(deadline_date, "%Y-%m-%d")

    if submission_dt <= deadline_dt:
        score += 10
    else:
        score -= 10  # Penalty for late submission

    # Final cleanup
    score = max(0, min(score, max_score))

    return {
        "score": score,
        "all_questions_answered": answered,
        "submitted_on_time": submission_dt <= deadline_dt
    }
