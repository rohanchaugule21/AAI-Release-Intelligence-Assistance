import json

with open(
    "../../data/knowledge_base.json",
    "r",
    encoding="utf-8"
) as fp:

    records = json.load(fp)

for record in records:

    if "Known" in record["section"]:

        print("\n")
        print("=" * 100)

        print(
            f"Release: {record['release_number']}"
        )

        print(
            f"Section: {record['section']}"
        )

        print("=" * 100)

        print(
            record["content"]
        )