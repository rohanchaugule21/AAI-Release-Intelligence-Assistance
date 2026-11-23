from query_engine import (
    get_latest_release,
    get_release,
    get_stories_by_release,
    get_story
)

print("\nLATEST RELEASE")
print(get_latest_release())

print("\nRELEASE 24")
print(get_release(24))

print("\nRELEASE 24 STORIES")

stories = get_stories_by_release(24)

for story in stories:

    print(
        story["story_id"],
        story["title"]
    )

print("\nSTORY 1702007")

print(
    get_story("1702007")
)
