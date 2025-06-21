from difflib import SequenceMatcher

def calculate_similarity(student_answer: str, reference_answer: str) -> float:
    """
    Compares student answer with reference answer using SequenceMatcher.
    Returns a percentage similarity score.
    """
    if not student_answer.strip() or not reference_answer.strip():
        return 0.0
    matcher = SequenceMatcher(None, student_answer.lower(), reference_answer.lower())
    return matcher.ratio() * 100
