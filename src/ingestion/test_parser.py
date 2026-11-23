import json

from section_parser import split_into_sections

with open(
    "../../data/release_notes.json",
    "r",
    encoding="utf-8"
) as fp:
    docs = json.load(fp)

# Look for release 24
for d in docs:

    if d["release_number"] == 24:

        sections = split_into_sections(
            d["content"]
        )

        for section in sections:

            print("\n")
            print("=" * 80)

            print(
                section["section"]
            )

            print("=" * 80)

            print(
                section["content"][:1000]
            )