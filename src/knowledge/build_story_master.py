import json
import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "knowledge_base.json"

OUTPUT_FILE = ROOT / "data" / "story_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    records = json.load(fp)

story_master = []

for record in records:

    content = record["content"]

    if "User Story" not in content:
        continue

    lines = content.split("\n")

    for line in lines:

        line = line.strip()

        if "|" not in line:
            continue

        parts = [
            x.strip()
            for x in line.split("|")
        ]

        if len(parts) < 3:
            continue

        if (
            parts[0].lower()
            == "user story"
        ):

            story_id = parts[1]

            title = parts[2]

            impact = None

            affected_version = None

            if len(parts) >= 5:
                impact = parts[4]

            if len(parts) >= 6:
                affected_version = parts[5]

            story_master.append(

                {
                    "release_number":
                        record["release_number"],

                    "release_version":
                        record["release_version"],

                    "airport":
                        record["airport"],

                    "story_type":
                        "User Story",

                    "story_id":
                        story_id,

                    "title":
                        title,

                    "impact":
                        impact,

                    "affected_version":
                        affected_version,

                    "source_file":
                        record["filename"]
                }
            )

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        story_master,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(story_master)} stories"
)

print(
    f"Saved to {OUTPUT_FILE}"
)