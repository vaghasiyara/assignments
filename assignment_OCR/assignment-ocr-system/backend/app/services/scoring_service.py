import difflib

def evaluate_submission(student_text: str, answer_text: str) -> int:
    student_lines = student_text.strip().splitlines()
    answer_lines = answer_text.strip().splitlines()

    total = len(answer_lines)
    if total == 0:
        return 0

    matched = 0
    for s_line, a_line in zip(student_lines, answer_lines):
        ratio = difflib.SequenceMatcher(None, s_line.strip().lower(), a_line.strip().lower()).ratio()
        if ratio > 0.6:
            matched += 1

    score = int((matched / total) * 100)
    return score
