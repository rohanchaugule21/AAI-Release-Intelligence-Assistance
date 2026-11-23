from src.comparison.story_compare import (
    compare_stories
)

from src.comparison.component_compare import (
    compare_components
)

def compare_releases(
    release1,
    release2
):

    story_results = compare_stories(
        release1,
        release2
    )

    component_results = compare_components(
        release1,
        release2
    )

    return {

        "stories":
            story_results,

        "components":
            component_results
    }