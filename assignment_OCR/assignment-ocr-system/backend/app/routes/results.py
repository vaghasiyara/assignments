from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

@router.get("/download-results")
def download_results():
    file_path = Path(__file__).resolve().parent.parent.parent / "results.csv"
    if not file_path.exists():
        return {"error": "results.csv not found"}

    return FileResponse(path=file_path, filename="results.csv", media_type='text/csv')
