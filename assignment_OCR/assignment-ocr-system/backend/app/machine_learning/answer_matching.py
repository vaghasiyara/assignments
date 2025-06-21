from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(student_answers, faculty_answers):
    scores = []
    for student_answer, correct_answer in zip(student_answers, faculty_answers):
        vectorizer = TfidfVectorizer().fit_transform([student_answer, correct_answer])
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
        score = round(similarity * 10, 2)  # Assume each answer has max score 10
        scores.append(score)
    return scores

def average_score(scores):
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)
