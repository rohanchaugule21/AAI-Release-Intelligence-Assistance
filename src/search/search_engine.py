import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

STORY_FILE = ROOT / "data" / "story_master.json"

COMPONENT_FILE = ROOT / "data" / "component_master.json"

DEPENDENCY_FILE = ROOT / "data" / "dependency_master.json"

RELEASE_HISTORY_FILE = (
    ROOT / "data" / "release_history_master.json"
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

with open(
    RELEASE_HISTORY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    RELEASE_HISTORY = json.load(fp)


def search_stories(keyword):

    keyword = keyword.lower()

    results = []

    for story in STORIES:

        searchable_text = (
            f"{story.get('title', '')} "
            f"{story.get('story_id', '')}"
        ).lower()

        if keyword in searchable_text:

            results.append(story)

    return results


def search_components(keyword):

    keyword = keyword.lower()

    results = []

    for component in COMPONENTS:

        searchable_text = (
            f"{component.get('component_name', '')}"
        ).lower()

        if keyword in searchable_text:

            results.append(component)

    return results


def search_dependencies(keyword):

    keyword = keyword.lower()

    results = []

    for dependency in DEPENDENCIES:

        searchable_text = (

            f"{dependency.get('name', '')} "
            f"{dependency.get('description', '')}"

        ).lower()

        if keyword in searchable_text:

            results.append(dependency)

    return results


def get_release_details(
    release_numbers
):

    return [

        release

        for release in RELEASE_HISTORY

        if release["release_number"]
        in release_numbers

    ]


def global_search(keyword):

    stories = search_stories(
        keyword
    )

    components = search_components(
        keyword
    )

    dependencies = search_dependencies(
        keyword
    )

    # ==================================================
    # COLLECT RELEASE NUMBERS
    # ==================================================

    release_numbers = set()

    for item in stories:

        release_numbers.add(
            item["release_number"]
        )

    for item in components:

        release_numbers.add(
            item["release_number"]
        )

    for item in dependencies:

        release_numbers.add(
            item["release_number"]
        )

    releases = get_release_details(
        release_numbers
    )

    # ==================================================
    # DEDUP STORIES
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
    # DEDUP COMPONENTS
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
    # DEDUP DEPENDENCIES
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
    # DEBUG
    # ==================================================

    print(
        f"\nKeyword: {keyword}"
    )

    print(
        f"Releases Found: {len(releases)}"
    )

    print(
        f"Stories Found: {len(stories)}"
    )

    print(
        f"Components Found: {len(components)}"
    )

    print(
        f"Dependencies Found: {len(dependencies)}"
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