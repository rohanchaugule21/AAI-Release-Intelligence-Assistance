import json

with open(
    "../../data/story_master.json",
    "r",
    encoding="utf-8"
) as fp:

    stories = json.load(fp)

print(
    f"\nStories Found: {len(stories)}\n"
)

for story in stories[:20]:

    print(
        f"Release Number : {story['release_number']}"
    )

    print(
        f"Release Version: {story['release_version']}"
    )

    print(
        f"Airport        : {story['airport']}"
    )

    print(
        f"Story ID       : {story['story_id']}"
    )

    print(
        f"Title          : {story['title']}"
    )

    print(
        f"Impact         : {story['impact']}"
    )

    print(
        f"Affected Ver   : {story['affected_version']}"
    )

    print(
        f"Source File    : {story['source_file']}"
    )

    print("-" * 100)