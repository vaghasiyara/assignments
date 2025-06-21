import json
import os
from datetime import datetime

LOG_FILE = "evaluation_logs.json"

def log_assignment_result(filename, match_score):
    entry = {
        "filename": filename,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "match_score": match_score
    }

    # Load existing log or start a new list
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    # Append new entry
    data.append(entry)

    # Save back to file
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)
