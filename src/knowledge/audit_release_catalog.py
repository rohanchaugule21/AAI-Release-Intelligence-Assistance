import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "release_history_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    releases = json.load(fp)

print("\n")
print("=" * 120)
print("RELEASE HISTORY AUDIT")
print("=" * 120)

for release in releases:

    print(
        f"Release: {release['release_number']} | "
        f"Version: {release['application_version']} | "
        f"Date: {release['release_date']} | "
        f"Author: {release['author']}"
    )
