import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:
    docs = json.load(fp)

release_number = int(
    input("Enter Release Number: ")
)

for doc in docs:

    if doc["release_number"] == release_number:

        print("\n")
        print("=" * 100)
        print(doc["filename"])
        print("=" * 100)

        print(doc["content"])

        break