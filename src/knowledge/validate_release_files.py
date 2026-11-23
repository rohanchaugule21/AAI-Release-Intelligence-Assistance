import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

DOCS = ROOT / "documents"

print("\n")
print("=" * 120)
print("FILE SYSTEM VALIDATION")
print("=" * 120)

files = list(
    DOCS.rglob("*.docx")
)

for file in sorted(files):

    match = re.search(
        r"ReleaseNoteV(\d+)",
        file.name,
        re.IGNORECASE
    )

    if match:

        release_no = int(
            match.group(1)
        )

        print(
            f"{release_no:02d} | {file.name}"
        )