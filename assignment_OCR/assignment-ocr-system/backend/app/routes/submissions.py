from fastapi import APIRouter, UploadFile, File, Form
from app.services.storage_service import save_file
from app.services.ocr_service import extract_text_from_path
from app.services.scoring_service import evaluate_submission
from app.utils.late_check import is_late_submission
import os
import json
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = "uploads/backend/app/assignments"
ANSWER_SHEET_PATH = "uploads/backend/app/answers/answer_sheet.txt"
LOG_FILE = "evaluation_logs.json"

@router.post("/upload-assignment")
async def upload_assignment(file: UploadFile = File(...), student: str = Form(default="")):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filename = f"assignment_{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    file_location = os.path.join(UPLOAD_DIR, filename)

    # Save file
    save_file(file, file_location)

    # Extract and evaluate
    extracted_text = extract_text_from_path(file_location)
    score = evaluate_submission(extracted_text, ANSWER_SHEET_PATH)
    late = is_late_submission(file.filename)

    # Log result
    log_entry = {
        "student": student,
        "filename": filename,
        "score": score,
        "late": late,
        "timestamp": timestamp
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    return {
        "message": "Assignment uploaded and evaluated successfully",
        "score": score,
        "late": late
    }

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/download-results")
def download_results():
    result_file = "outputs/results.csv"
    if os.path.exists(result_file):
        return FileResponse(result_file, filename="results.csv", media_type="text/csv")
    else:
        return {"detail": "Result file not found"}
