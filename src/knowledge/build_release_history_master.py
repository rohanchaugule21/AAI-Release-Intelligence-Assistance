import json
import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_notes.json"

OUTPUT_FILE = (
    ROOT / "data" / "release_history_master.json"
)

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    docs = json.load(fp)

# ==========================================================
# CREATE RELEASE NUMBER MAP FROM FILE NAMES
# ==========================================================

release_catalog = {}

for doc in docs:

    release_number = doc.get(
        "release_number"
    )

    release_catalog[
        release_number
    ] = {

        "release_number":
            release_number,

        "application_version":
            doc.get(
                "release_version"
            ),

        "release_date":
            None,

        "author":
            None,

        "filename":
            doc.get(
                "filename"
            ),

        "validation_status":
            "MISSING_METADATA"
    }

# ==========================================================
# FIND LATEST RELEASE NOTE
# ==========================================================

latest_doc = max(
    docs,
    key=lambda x:
    x["release_number"]
)

print(
    f"Using Release "
    f"{latest_doc['release_number']} "
    f"as release history source"
)

content = latest_doc["content"]

lines = content.split("\n")

# ==========================================================
# PARSE REVISION HISTORY TABLE
# ==========================================================

for line in lines:

    if "|" not in line:
        continue

    parts = [
        p.strip()
        for p in line.split("|")
    ]

    if len(parts) < 4:
        continue

    release_date = parts[0]
    version = parts[1]
    description = parts[2]
    author = parts[3]

    if "/" not in release_date:
        continue

    if not version.startswith("V"):
        continue

    match = re.search(
        r"release\s+(\d+)",
        description,
        re.IGNORECASE
    )

    if not match:
        continue

    release_number = int(
        match.group(1)
    )

    # --------------------------------------------------
    # Fix known documentation mismatch:
    #
    # Description:
    # Release 24
    #
    # Version:
    # V2026.25.0
    #
    # Use version as source when
    # release/version conflict.
    # --------------------------------------------------

    version_match = re.search(
        r"V20\d{2}\.(\d+)\.",
        version,
        re.IGNORECASE
    )

    if version_match:

        version_release = int(
            version_match.group(1)
        )

        if version_release != release_number:

            release_number = (
                version_release
            )

    if (
        release_number
        not in release_catalog
    ):
        continue

    release_catalog[
        release_number
    ][
        "application_version"
    ] = version

    release_catalog[
        release_number
    ][
        "release_date"
    ] = release_date

    release_catalog[
        release_number
    ][
        "author"
    ] = author

    release_catalog[
        release_number
    ][
        "description"
    ] = description

    release_catalog[
        release_number
    ][
        "validation_status"
    ] = "VALID"

# ==========================================================
# SORT
# ==========================================================

history = sorted(
    release_catalog.values(),
    key=lambda x:
    x["release_number"]
)

# ==========================================================
# SAVE
# ==========================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        history,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created "
    f"{len(history)} "
    f"release history records"
)