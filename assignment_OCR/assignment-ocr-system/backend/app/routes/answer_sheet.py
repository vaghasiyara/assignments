from fastapi import APIRouter, UploadFile, File
import os
from app.services.ocr_service import extract_text_from_path

router = APIRouter()
ANSWER_DIR = "faculty_answers"
os.makedirs(ANSWER_DIR, exist_ok=True)

ANSWER_FILE_PATH = os.path.join(ANSWER_DIR, "official_answer.txt")

@router.post("/upload-answer-sheet")
async def upload_answer_sheet(file: UploadFile = File(...)):
    file_location = os.path.join(ANSWER_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_path(file_location)

    with open(ANSWER_FILE_PATH, "w") as f:
        f.write(extracted_text)

    return {
        "message": "Answer sheet uploaded and processed successfully.",
        "extracted_text": extracted_text
    }
