import json

with open(
    "../../data/release_notes.json",
    "r",
    encoding="utf-8"
) as fp:

    docs = json.load(fp)

for doc in sorted(
    docs,
    key=lambda x: x["release_number"] or 0
):

    print(
        doc["release_number"],
        doc["release_version"],
        doc["filename"]
    )