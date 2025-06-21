from backend.app.services.matching_service import calculate_similarity

student_answer = "Water boils at 100 degrees Celsius under standard conditions."
reference_answer = "Under normal pressure, water boils at 100°C."

score = calculate_similarity(student_answer, reference_answer)
print(f"Similarity Score: {score:.2f}%")
