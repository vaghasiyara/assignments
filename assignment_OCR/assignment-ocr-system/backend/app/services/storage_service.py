import os
from fastapi import UploadFile
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../uploads"))

def save_file(file: UploadFile, filename: str = None, subfolder: str = "assignments") -> str:
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"assignment_{timestamp}_{file.filename}"
    target_folder = os.path.join(BASE_DIR, subfolder)
    os.makedirs(target_folder, exist_ok=True)

    file_path = os.path.join(target_folder, filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
