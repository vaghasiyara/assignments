import os
from datetime import datetime

# This base folder should be at: backend/app/uploads
BASE_UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../uploads")

def get_assignment_upload_path(filename: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return os.path.join(BASE_UPLOAD_DIR, "assignments", f"assignment_{timestamp}_{filename}")

def get_answer_upload_path(filename: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return os.path.join(BASE_UPLOAD_DIR, "answers", f"answer_{timestamp}_{filename}")

def get_result_download_path(filename: str) -> str:
    return os.path.join(BASE_UPLOAD_DIR, "results", filename)
