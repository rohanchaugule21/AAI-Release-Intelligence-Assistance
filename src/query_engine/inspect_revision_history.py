import json

with open(
    "../../data/release_notes.json",
    "r",
    encoding="utf-8"
) as fp:

    docs = json.load(fp)

for doc in docs:

    if doc["release_number"] == 24:

        print(doc["content"])

        break