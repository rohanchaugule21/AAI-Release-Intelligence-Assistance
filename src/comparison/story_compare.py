import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

STORY_FILE = ROOT / "data" / "story_master.json"

with open(
    STORY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    STORIES = json.load(fp)


def compare_stories(
    release1,
    release2
):

    release1_stories = [

        story

        for story in STORIES

        if story["release_number"]
        == release1

    ]

    release2_stories = [

        story

        for story in STORIES

        if story["release_number"]
        == release2

    ]

    common = []

    release1_ids = {
        s["story_id"]
        for s in release1_stories
    }

    release2_ids = {
        s["story_id"]
        for s in release2_stories
    }

    for story in release1_stories:

        if story["story_id"] in release2_ids:

            common.append(story)

    return {

        "comparison_type":
            "release_scope_comparison",

        "release_1":
            release1,

        "release_1_deliveries":
            release1_stories,

        "release_2":
            release2,

        "release_2_deliveries":
            release2_stories,

        "common_deliveries":
            common

    }