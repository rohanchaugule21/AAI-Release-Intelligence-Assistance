import json
from pathlib import Path

from src.ingestion.section_parser import split_into_sections

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

OUTPUT_FILE = ROOT / "data" / "knowledge_base.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    release_notes = json.load(fp)

knowledge_base = []

for release in release_notes:

    sections = split_into_sections(
        release["content"]
    )

    for section in sections:

        knowledge_base.append({

            "release_number":
                release["release_number"],

            "release_version":
                release["release_version"],

            "airport":
                release["airport"],

            "filename":
                release["filename"],

            "section":
                section["section"],

            "content":
                section["content"]

        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        knowledge_base,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(knowledge_base)} knowledge records"
)

print(
    f"Saved to {OUTPUT_FILE}"
)