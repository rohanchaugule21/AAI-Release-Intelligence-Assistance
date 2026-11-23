import json

with open(
    "../../data/dependency_master.json",
    "r",
    encoding="utf-8"
) as fp:

    deps = json.load(fp)

print(
    f"\nDependencies Found: {len(deps)}\n"
)

for dep in deps[:20]:

    print(dep)

    print("-" * 100)