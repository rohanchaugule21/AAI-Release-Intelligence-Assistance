import json
import re
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

KNOWLEDGE_FILE = ROOT / "data" / "knowledge_base.json"


with open(
    KNOWLEDGE_FILE,
    "r",
    encoding="utf-8"
) as fp:

    knowledge = json.load(fp)


question = input(
    "\nAsk Question: "
)


release_match = re.search(
    r"release\s+(\d+)",
    question,
    re.IGNORECASE
)

release_number = None

if release_match:
    release_number = int(
        release_match.group(1)
    )


results = []

for record in knowledge:

    if release_number:

        if (
            record["release_number"]
            != release_number
        ):
            continue

    results.append(record)


print("\n")
print("=" * 80)

print(
    f"Records Found: {len(results)}"
)

print("=" * 80)


for record in results[:20]:

    print("\n")

    print(
        f"Release : {record['release_number']}"
    )

    print(
        f"Airport : {record['airport']}"
    )

    print(
        f"Section : {record['section']}"
    )

    print("-" * 80)

    print(
        record["content"][:500]
    )
