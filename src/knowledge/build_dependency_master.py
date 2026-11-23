import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

OUTPUT_FILE = ROOT / "data" / "dependency_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    documents = json.load(fp)

dependencies = []

for doc in documents:

    release_number = doc["release_number"]
    release_version = doc["release_version"]
    airport = doc["airport"]

    lines = doc["content"].split("\n")

    for line in lines:

        if "|" not in line:
            continue

        parts = [
            p.strip()
            for p in line.split("|")
        ]

        # Skip headers

        if len(parts) < 4:
            continue

        # Database dependency table

        if parts[0] == "SQL Database":

            dependency = {

                "release_number":
                    release_number,

                "release_version":
                    release_version,

                "airport":
                    airport,

                "dependency_type":
                    "Database",

                "name":
                    parts[1],

                "version":
                    parts[2],

                "description":
                    parts[3]
            }

            dependencies.append(
                dependency
            )

# ==================================================
# Deduplicate
# ==================================================

unique_dependencies = []

seen = set()

for dep in dependencies:

    key = (
        dep["release_number"],
        dep["name"]
    )

    if key in seen:
        continue

    seen.add(key)

    unique_dependencies.append(dep)

# ==================================================
# Save
# ==================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        unique_dependencies,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(unique_dependencies)} dependencies"
)