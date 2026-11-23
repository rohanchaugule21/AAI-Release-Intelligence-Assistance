from src.query_engine.query_engine import (
    get_last_n_releases
)

import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

DATA = ROOT / "data"

STORY_FILE = (
    DATA / "story_master.json"
)

COMPONENT_FILE = (
    DATA / "component_master.json"
)

DEPENDENCY_FILE = (
    DATA / "dependency_master.json"
)

with open(
    STORY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    STORIES = json.load(fp)

with open(
    COMPONENT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    COMPONENTS = json.load(fp)

with open(
    DEPENDENCY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    DEPENDENCIES = json.load(fp)


def get_recent_release_summary(
    count=5
):

    releases = get_last_n_releases(
        count
    )

    release_numbers = {

        release["release_number"]

        for release in releases

    }

    # ==================================================
    # STORIES
    # ==================================================

    stories = [

        story

        for story in STORIES

        if story["release_number"]
        in release_numbers

    ]

    # ==================================================
    # COMPONENTS
    # ==================================================

    components = [

        component

        for component in COMPONENTS

        if component["release_number"]
        in release_numbers

    ]

    # ==================================================
    # DEPENDENCIES
    # ==================================================

    dependencies = [

        dependency

        for dependency in DEPENDENCIES

        if dependency["release_number"]
        in release_numbers

    ]

    # ==================================================
    # DEDUPLICATE STORIES
    # ==================================================

    unique_stories = {}

    for story in stories:

        story_id = story.get(
            "story_id"
        )

        if story_id not in unique_stories:

            unique_stories[
                story_id
            ] = story

    stories = list(
        unique_stories.values()
    )

    # ==================================================
    # DEDUPLICATE COMPONENTS
    # ==================================================

    unique_components = {}

    for component in components:

        key = (

            component.get(
                "release_number"
            ),

            component.get(
                "component_name"
            )

        )

        if key not in unique_components:

            unique_components[
                key
            ] = component

    components = list(
        unique_components.values()
    )

    # ==================================================
    # DEDUPLICATE DEPENDENCIES
    # ==================================================

    unique_dependencies = {}

    for dependency in dependencies:

        key = (

            dependency.get(
                "release_number"
            ),

            dependency.get(
                "name"
            )

        )

        if key not in unique_dependencies:

            unique_dependencies[
                key
            ] = dependency

    dependencies = list(
        unique_dependencies.values()
    )



    # ==================================================
    # RETURN
    # ==================================================

    return {

        "releases":
            releases,

        "stories":
            stories,

        "components":
            components,

        "dependencies":
            dependencies

    }