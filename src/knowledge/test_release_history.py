import json

with open(
    "../../data/release_history_master.json",
    "r",
    encoding="utf-8"
) as fp:

    releases = json.load(fp)

for release in releases:

    print(
        release["release_number"],
        release["application_version"],
        release["author"]
    )