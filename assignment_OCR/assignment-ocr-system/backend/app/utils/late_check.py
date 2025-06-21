from datetime import datetime

# Define your submission deadline
DEADLINE = datetime(2025, 6, 20, 23, 59)

def is_late_submission(submit_time: datetime) -> bool:
    return submit_time > DEADLINE
