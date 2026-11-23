import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

DATA = ROOT / "data"

OUTPUT_FILE = DATA / "unified_knowledge.json"

FILES = [

    ("release_history",
     DATA / "release_history_master.json"),

    ("story",
     DATA / "story_master.json"),

    ("component",
     DATA / "component_master.json"),

    ("dependency",
     DATA / "dependency_master.json")
]

knowledge = []

for source_type, file_path in FILES:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as fp:

        records = json.load(fp)

    for record in records:

        knowledge.append({

            "source_type":
                source_type,

            "release_number":
                record.get(
                    "release_number"
                ),

            "content":
                str(record)

        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        knowledge,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(knowledge)} knowledge records"
)