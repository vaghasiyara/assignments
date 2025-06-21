from PIL import Image
import pytesseract

def extract_text_from_path(file_path):
    return pytesseract.image_to_string(Image.open(file_path)).strip()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity_score(student_ans: str, faculty_ans: str) -> float:
    vectorizer = TfidfVectorizer().fit_transform([student_ans, faculty_ans])
    vectors = vectorizer.toarray()
    return round(cosine_similarity([vectors[0]], [vectors[1]])[0][0] * 100, 2)

def evaluate_similarity(student_text, faculty_file_path="backend/app/uploads/faculty_answers.txt"):
    try:
        with open(faculty_file_path, "r") as f:
            faculty_text = f.read()

        # Convert to lowercase, remove newlines for cleaner comparison
        student_text_clean = student_text.lower().replace("\n", " ")
        faculty_text_clean = faculty_text.lower().replace("\n", " ")

        ratio = SequenceMatcher(None, student_text_clean, faculty_text_clean).ratio()
        score = round(ratio * 100, 2)

        return score
    except FileNotFoundError:
        return None  # Faculty answer sheet not uploaded yet
    except Exception as e:
        print("Error in evaluating similarity:", e)
        return None
