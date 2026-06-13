
import csv
import os
import uuid
from datetime import datetime

DATA_FILE = "data/responses.csv"

COLUMNS = [
    "session_id", "timestamp",
    *[f"Q{i}" for i in range(1, 26)],
    *[f"{t}{i}" for t in ["EXT","EST","AGR","CSN","OPN"] for i in range(1, 11)],
    "country", "predicted", "confidence",
    "actual", "confirmed", "replayed"
]

def init_csv():
    """Create CSV with headers if it doesn't exist yet."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()

def save_response(answers: dict, country: str, predicted: str, confidence: float) -> str:
    """
    Save a new quiz response. Returns session_id for feedback linking.
    """
    init_csv()
    session_id = str(uuid.uuid4())[:8]

    row = {
        "session_id" : session_id,
        "timestamp"  : datetime.now().isoformat(),
        "country"    : country,
        "predicted"  : predicted,
        "confidence" : confidence,
        "actual"     : "",        # filled in by feedback
        "confirmed"  : "",        # filled in by feedback
        "replayed"   : False,
    }

    # add all question answers
    for key, val in answers.items():
        if key in COLUMNS:
            row[key] = val

    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writerow(row)

    return session_id


def save_feedback(session_id: str, actual: str, confirmed: bool, replayed: bool):
    """
    Update an existing row with user feedback after prediction.
    """
    if not os.path.exists(DATA_FILE):
        return

    rows = []
    with open(DATA_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["session_id"] == session_id:
                row["actual"]    = actual
                row["confirmed"] = confirmed
                row["replayed"]  = replayed
            rows.append(row)

    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def get_stats() -> dict:
    """Basic stats for the optional /stats endpoint."""
    if not os.path.exists(DATA_FILE):
        return {"total": 0, "correct": 0, "accuracy": 0}

    total     = 0
    correct   = 0
    replayed  = 0

    with open(DATA_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row["confirmed"] == "True":
                correct += 1
            if row["replayed"] == "True":
                replayed += 1

    accuracy = round((correct / total * 100), 1) if total > 0 else 0

    return {
        "total"    : total,
        "correct"  : correct,
        "accuracy" : accuracy,
        "replayed" : replayed,
    }