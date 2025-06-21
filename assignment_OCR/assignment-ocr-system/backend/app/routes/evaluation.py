from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import ocr_service
from machine_learning.answer_matching import calculate_similarity, average_score
from app.services.result_service import save_result  # ✅ Add this

router = APIRouter()

class EvaluationRequest(BaseModel):
    student_id: str
    student_answers: list[str]
    faculty_answers: list[str]

@router.post("/evaluate")
def evaluate_answers(request: EvaluationRequest):
    if len(request.student_answers) != len(request.faculty_answers):
        raise HTTPException(status_code=400, detail="Mismatched number of answers")
    
    scores = calculate_similarity(request.student_answers, request.faculty_answers)
    avg = average_score(scores)

    # ✅ Save to CSV
    save_result(request.student_id, scores, avg)

    return {
        "student_id": request.student_id,
        "individual_scores": scores,
        "average_score": avg
    }
