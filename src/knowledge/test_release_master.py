import json

with open(
    "../../data/story_master.json",
    "r",
    encoding="utf-8"
) as fp:

    stories = json.load(fp)

print(
    f"Stories Found: {len(stories)}"
)

print("\n")

for story in stories[:10]:

    print(
        f"Release: {story['release_number']}"
    )

    print(
        f"Story  : {story['story_id']}"
    )

    print(
        f"Title  : {story['title']}"
    )

    print(
        f"Impact : {story['impact']}"
    )

    print("-" * 80)