import json
import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

OUTPUT_FILE = ROOT / "data" / "release_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    docs = json.load(fp)

release_master = []

for doc in docs:

    release_record = {

        "release_number":
            doc["release_number"],

        "release_version":
            doc["release_version"],

        "airport":
            doc["airport"],

        "filename":
            doc["filename"],

        "author": None,

        "release_date": None,

        "description": None
    }

    content = doc["content"]

    lines = content.split("\n")

    for line in lines:

        if (
            "IRS Release" in line
            and "|" in line
        ):
            release_record[
                "description"
            ] = line

            break

    release_master.append(
        release_record
    )

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        release_master,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(release_master)} releases"
)
