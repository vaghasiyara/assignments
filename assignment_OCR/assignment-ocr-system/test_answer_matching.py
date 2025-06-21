from backend.machine_learning.answer_matching import calculate_similarity, average_score

student_answers = [
    "The mitochondria is the powerhouse of the cell.",
    "Water is made of hydrogen and oxygen.",
]

faculty_answers = [
    "Mitochondria are known as the powerhouse of cells.",
    "Water consists of two hydrogen atoms and one oxygen atom.",
]

scores = calculate_similarity(student_answers, faculty_answers)
avg = average_score(scores)

print("Individual Scores:", scores)
print("Average Score:", avg)
