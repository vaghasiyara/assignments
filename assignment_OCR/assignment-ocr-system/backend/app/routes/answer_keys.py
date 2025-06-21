from fastapi import APIRouter, UploadFile, File
import os
from app.services.ocr_service import extract_text_from_path

router = APIRouter()

ANSWER_KEY_DIR = "uploaded_answer_keys"
os.makedirs(ANSWER_KEY_DIR, exist_ok=True)

@router.post("/upload-answer-key")
async def upload_answer_key(file: UploadFile = File(...)):
    file_location = os.path.join(ANSWER_KEY_DIR, file.filename)
    with open(file_location, "wb+") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_path(file_location)

    # Save extracted answer key text
    with open(os.path.join(ANSWER_KEY_DIR, "latest_answer_key.txt"), "w") as f:
        f.write(extracted_text)

    return {"message": "Answer key uploaded and processed successfully."}
