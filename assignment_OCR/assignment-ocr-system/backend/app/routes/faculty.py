from fastapi import APIRouter, UploadFile, File
from app.services.storage_service import save_file
import os
from datetime import datetime

router = APIRouter()

@router.post("/upload-answer-sheet")
async def upload_answer_sheet(file: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"answerkey_{timestamp}_{file.filename}"
    file_path = os.path.join("uploads", "faculty", filename)
    save_file(file, file_path)
    return {"message": "Answer key uploaded", "filename": filename}
