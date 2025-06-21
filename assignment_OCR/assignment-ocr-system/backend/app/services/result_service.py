import csv
from pathlib import Path

RESULTS_PATH = Path(__file__).resolve().parent.parent.parent / "results.csv"

def save_result(student_id, individual_scores, average_score):
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Write headers if file doesn't exist
    write_header = not RESULTS_PATH.exists()

    with open(RESULTS_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["student_id", "individual_scores", "average_score"])

        writer.writerow([
            student_id,
            "; ".join([str(score) for score in individual_scores]),
            average_score
        ])
