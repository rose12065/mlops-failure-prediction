import csv
import os
from pathlib import Path
from datetime import datetime


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "pipeline_runs.csv"

run_id = os.getenv("RUN_ID", "local")
commit_id = os.getenv("COMMIT_ID", "local")
pipeline_status = os.getenv("PIPELINE_STATUS", "UNKNOWN")
changed_files = os.getenv("CHANGED_FILES", "0")

test_outcome = os.getenv("TEST_OUTCOME", "UNKNOWN")
train_outcome = os.getenv("TRAIN_OUTCOME", "UNKNOWN")


if test_outcome == "failure":
    failure_stage = "TESTING"
    failure_type = "TEST_FAILURE"

elif train_outcome == "failure":
    failure_stage = "TRAINING"
    failure_type = "TRAINING_FAILURE"

else:
    failure_stage = "NONE"
    failure_type = "NONE"


file_exists = CSV_FILE.exists()


with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "run_id",
            "commit_id",
            "timestamp",
            "pipeline_status",
            "failure_stage",
            "failure_type",
            "changed_files"
        ])

        writer.writerow([
            run_id,
            commit_id,
            datetime.now().isoformat(),
            pipeline_status,
            failure_stage,
            failure_type,
            changed_files
        ])


print(f"Pipeline run recorded: {run_id}")
print(f"Status: {pipeline_status}")
print(f"Failure stage: {failure_stage}")
print(f"Failure type: {failure_type}")