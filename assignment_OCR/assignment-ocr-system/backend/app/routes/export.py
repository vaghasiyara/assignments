from fastapi import APIRouter, Response
from app.utils.pdf_exporter import export_results_to_pdf

router = APIRouter()

@router.get("/export-results", response_class=Response)
def export_results():
    output_pdf_path = "backend/app/static/exported_results.pdf"
    export_results_to_pdf(output_pdf_path)

    with open(output_pdf_path, "rb") as f:
        content = f.read()

    return Response(
        content=content,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=exported_results.pdf"}
    )
