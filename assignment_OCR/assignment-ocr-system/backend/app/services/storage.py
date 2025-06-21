import os
from fastapi import UploadFile
from uuid import uuid4

UPLOAD_DIR = "uploaded_assignments"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file: UploadFile) -> str:
    file_extension = os.path.splitext(file.filename)[1]
    file_path = os.path.join(UPLOAD_DIR, f"{uuid4()}{file_extension}")
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
