from src.query_engine.query_engine import (
    get_story
)

from src.formatter.story_formatter import (
    format_story
)

story = get_story(
    "1702007"
)

print(
    format_story(story)
)