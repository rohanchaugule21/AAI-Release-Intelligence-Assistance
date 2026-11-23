import json
import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

OUTPUT_FILE = ROOT / "data" / "component_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    documents = json.load(fp)

components = []

for doc in documents:

    release_number = doc["release_number"]

    release_version = doc["release_version"]

    airport = doc["airport"]

    content = doc["content"]

    lines = content.split("\n")

    # ==========================================
    # SQL DATABASES
    # ==========================================

    for line in lines:

        if "SQL Database" in line and "|" in line:

            parts = [
                p.strip()
                for p in line.split("|")
            ]

            if len(parts) >= 3:

                components.append({

                    "release_number":
                        release_number,

                    "release_version":
                        release_version,

                    "airport":
                        airport,

                    "component_type":
                        "Database",

                    "component_name":
                        parts[1],

                    "version":
                        parts[2]

                })

    # ==========================================
    # STORED PROCEDURES
    # ==========================================

    for i, line in enumerate(lines):

        if (
            "Stored Procedure"
            in line
        ):

            window = "\n".join(
                lines[i:i+20]
            )

            matches = re.findall(
                r"dydmo\.[A-Za-z0-9_]+",
                window,
                re.IGNORECASE
            )

            for proc in matches:

                components.append({

                    "release_number":
                        release_number,

                    "release_version":
                        release_version,

                    "airport":
                        airport,

                    "component_type":
                        "Stored Procedure",

                    "component_name":
                        proc,

                    "version":
                        None

                })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        components,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(components)} components"
)