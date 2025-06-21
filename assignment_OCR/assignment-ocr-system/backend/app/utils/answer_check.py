import re

def check_all_questions_present(text: str, expected_questions: list[str]) -> dict:
    present_questions = []
    for q in expected_questions:
        pattern = rf"\b{re.escape(q)}\b"
        if re.search(pattern, text, re.IGNORECASE):
            present_questions.append(q)
    missing = [q for q in expected_questions if q not in present_questions]
    return {
        "present": present_questions,
        "missing": missing,
        "all_answered": len(missing) == 0
    }
