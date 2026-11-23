import json

with open(
    "../../data/component_master.json",
    "r",
    encoding="utf-8"
) as fp:

    components = json.load(fp)

print(
    f"Components Found: {len(components)}"
)

print()

for component in components[:25]:

    print(component)
    print("-" * 80)