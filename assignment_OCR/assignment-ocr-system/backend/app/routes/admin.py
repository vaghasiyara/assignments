from fastapi import APIRouter, UploadFile, File
from app.services.storage_service import save_file
from app.services.ocr_service import extract_text_from_path
import os
from datetime import datetime

router = APIRouter()

@router.post("/upload-answer-sheet")
async def upload_answer_sheet(file: UploadFile = File(...)):
    filename = f"answerkey_{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    file_path = os.path.join("uploads", "admin", "answers", filename)
    save_file(file, file_path)
    extracted_text = extract_text_from_path(file_path)

    # Save extracted text to a .txt file for comparison
    txt_path = file_path + ".txt"
    with open(txt_path, "w") as f:
        f.write(extracted_text)

    return {"message": "Answer sheet uploaded and processed successfully."}
