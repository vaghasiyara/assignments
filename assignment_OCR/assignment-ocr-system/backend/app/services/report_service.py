import os
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "../../reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def generate_report(student_id: str, score: float, total_questions: int, answered_questions: int, submission_time: datetime, is_late: bool):
    status = "Late" if is_late else "On Time"
    report = (
        f"Student ID: {student_id}\n"
        f"Score: {score:.2f}\n"
        f"Answered Questions: {answered_questions}/{total_questions}\n"
        f"Submission Time: {submission_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Submission Status: {status}\n"
    )
    filename = f"{student_id}_report.txt"
    report_path = os.path.join(REPORTS_DIR, filename)

    with open(report_path, "w") as f:
        f.write(report)

    return report_path
