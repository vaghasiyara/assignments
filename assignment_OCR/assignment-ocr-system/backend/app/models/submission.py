from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Text, JSON
from app.database import Base
from datetime import datetime

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    is_late = Column(Boolean, default=False)
    extracted_text = Column(Text)
    total_score = Column(Float)
    per_question_similarity = Column(JSON)
