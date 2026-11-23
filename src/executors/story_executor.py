from src.query_engine.query_engine import (
    get_story,
    get_stories_by_release
)


def execute(intent, entities):

    if "story_id" in entities:

        return get_story(
            entities["story_id"]
        )

    if "release_number" in entities:

        return get_stories_by_release(
            entities["release_number"]
        )

    return None