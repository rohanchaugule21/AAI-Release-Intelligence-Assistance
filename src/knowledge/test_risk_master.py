import json

with open(
    "../../data/risk_master.json",
    "r",
    encoding="utf-8"
) as fp:

    risks = json.load(fp)

print(
    f"Risks Found: {len(risks)}"
)

print()

for risk in risks[:20]:

    print(risk)

    print("-" * 100)