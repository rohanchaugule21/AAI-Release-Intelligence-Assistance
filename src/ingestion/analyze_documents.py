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

    documents = json.load(fp)

print("\n")
print("=" * 100)
print("DOCUMENT ANALYSIS")
print("=" * 100)

for doc in documents[:3]:

    print("\n")
    print(f"File       : {doc['filename']}")
    print(f"Airport    : {doc['airport']}")
    print(f"Release No : {doc['release_number']}")

    print("\nFirst 1500 characters:")
    print("-" * 60)

    print(doc["content"][:1500])

    print("\n")
    print("=" * 100)