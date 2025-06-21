from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

router = APIRouter()

ASSIGNMENTS_DIR = Path("machine_learning/data/answers")
ASSIGNMENTS_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/assignments/upload")
async def upload_assignment_sheet(file: UploadFile = File(...)):
    if not file.filename.endswith((".png", ".jpg", ".jpeg", ".pdf")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    save_path = ASSIGNMENTS_DIR / file.filename
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Assignment sheet '{file.filename}' uploaded successfully."}
