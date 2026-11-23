import re


def classify(question):

    q = question.lower()

    # =====================================
    # LAST N RELEASES
    # =====================================

    if (
        "last" in q
        and "release" in q
    ):

        return "LAST_N_RELEASES"

    if (
        "recent releases" in q
    ):

        return "LAST_N_RELEASES"

    # =====================================
    # COMPARE RELEASES
    # =====================================

    if (
        "compare" in q
        and len(
            re.findall(
                r"release\s+\d+",
                q
            )
        ) >= 2
    ):

        return "COMPARE_RELEASES"

    if (
        "what changed between"
        in q
        and len(
            re.findall(
                r"release\s+\d+",
                q
            )
        ) >= 2
    ):

        return "COMPARE_RELEASES"

    # =====================================
    # SEARCH
    # =====================================

    if q.startswith("find "):

        return "SEARCH"

    if q.startswith("search "):

        return "SEARCH"

    # =====================================
    # STORIES BY RELEASE
    # =====================================

    if (
        (
            "story" in q
            or "stories" in q
            or "user story" in q
        )
        and "release" in q
    ):

        return "STORIES_BY_RELEASE"

    # =====================================
    # STORY LOOKUP
    # =====================================

    if re.search(
        r"\d{6,8}",
        q
    ):

        return "STORY_LOOKUP"

    # =====================================
    # LATEST RELEASE
    # =====================================

    if (
        "latest release" in q
        or "most recent release" in q
    ):

        return "LATEST_RELEASE"

    # =====================================
    # AUTHOR LOOKUP
    # =====================================

    if (
        "prepared by" in q
        or "authored by" in q
    ):

        return "RELEASES_BY_AUTHOR"

    # =====================================
    # RELEASE COUNT BY YEAR
    # =====================================

    if (
        "how many releases" in q
        and re.search(
            r"20\d{2}",
            q
        )
    ):

        return "RELEASE_COUNT_BY_YEAR"

    # =====================================
    # RELEASE LOOKUP
    # =====================================

    if (
        "release" in q
        and re.search(
            r"\d+",
            q
        )
    ):

        return "RELEASE_LOOKUP"

    return "UNKNOWN"