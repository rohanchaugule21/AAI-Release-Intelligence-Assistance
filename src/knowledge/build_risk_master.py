import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

INPUT_FILE = ROOT / "data" / "knowledge_base.json"

OUTPUT_FILE = ROOT / "data" / "risk_master.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    records = json.load(fp)

risks = []

for record in records:

    if "5. Risks" not in record["section"]:
        continue

    content = record["content"]

    if "Risk Category" not in content:
        continue

    lines = content.split("\n")

    for line in lines:

        if "|" not in line:
            continue

        parts = [
            p.strip()
            for p in line.split("|")
        ]

        if len(parts) < 4:
            continue

        if parts[0] == "Risk Category":
            continue

        risks.append({

            "release_number":
                record["release_number"],

            "release_version":
                record["release_version"],

            "airport":
                record["airport"],

            "risk_category":
                parts[0],

            "risk_description":
                parts[1],

            "risk_impact":
                parts[2],

            "mitigation_plan":
                parts[3]
        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        risks,
        fp,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(risks)} risks"
)