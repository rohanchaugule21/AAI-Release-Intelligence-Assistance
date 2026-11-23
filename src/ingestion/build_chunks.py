import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"
OUTPUT_FILE = ROOT / "data" / "chunks.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    docs = json.load(fp)

chunks = []

for doc in docs:

    chunks.append({

        "release_number":
            doc["release_number"],

        "airport":
            doc["airport"],

        "filename":
            doc["filename"],

        "content":
            doc["content"]

    })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        chunks,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(chunks)} chunks"
)