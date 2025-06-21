from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/download-report/{student_id}")
async def download_report(student_id: str):
    report_path = f"backend/reports/{student_id}_report.txt"
    if os.path.exists(report_path):
        return FileResponse(report_path, media_type="text/plain", filename=f"{student_id}_report.txt")
    return {"error": "Report not found"}
