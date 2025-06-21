from app.services.ocr_service import extract_text_from_path

text = extract_text_from_path("machine_learning/data/raw/sample_assignment.png")
print(text)
