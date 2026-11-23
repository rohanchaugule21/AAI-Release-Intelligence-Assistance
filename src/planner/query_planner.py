import re


def plan(question):

    q = question.lower().strip()

    # ==================================================
    # FACT QUESTIONS
    # ==================================================

    if (
        "latest release" in q
        or "most recent release" in q
    ):

        return {
            "route": "FACT",
            "action": "LATEST_RELEASE"
        }

    if (
        "how many releases" in q
        or "total releases" in q
        or "number of releases" in q
    ):

        return {
            "route": "FACT",
            "action": "RELEASE_COUNT"
        }

    if (
        "list all releases" in q
        or "list all the releases" in q
        or "show all releases" in q
        or "show all the releases" in q
        or "display all releases" in q
        or "display all the releases" in q
        or "release history" in q
    ):

        return {
            "route": "FACT",
            "action": "LIST_ALL_RELEASES"
        }

    if (
        "who prepared" in q
        or "who authored" in q
        or "prepared by" in q
        or "authored by" in q
    ):

        return {
            "route": "FACT",
            "action": "AUTHOR_LOOKUP"
        }

    if (
        "application version" in q
        or "release version" in q
        or "release date" in q
        or "show details" in q
        or "release details" in q
        or "tell me about release" in q
        or "show release" in q
        or "what is the release" in q
        or "version of release" in q
    ):

        return {
            "route": "FACT",
            "action": "RELEASE_DETAILS"
        }

    if re.search(
        r"\b\d{6,8}\b",
        q
    ):

        return {
            "route": "FACT",
            "action": "STORY_LOOKUP"
        }

    # ==================================================
    # COMPARE
    # ==================================================

    if (
        "compare" in q
        and len(
            re.findall(
                r"release\s+\d+",
                q
            )
        ) >= 2
    ):

        return {
            "route": "COMPARE"
        }

    if (
        "what changed between" in q
    ):

        return {
            "route": "COMPARE"
        }

    # ==================================================
    # SEARCH
    # ==================================================

    search_patterns = [

        "find",
        "search",
        "related to",
        "show me everything related to",
        "which releases involve",
        "which releases contain",
        "which releases modified",
        "where was",
        "introduced",
        "implemented",
        "delivered in",
        "information about"

    ]

    if any(
        pattern in q
        for pattern in search_patterns
    ):

        return {
            "route": "SEARCH"
        }

    # ==================================================
    # TREND
    # ==================================================

    trend_patterns = [

        "what changed recently",
        "recent changes",
        "what's new",
        "whats new",
        "last releases",
        "recent releases",
        "last 5 releases",
        "last 10 releases",
        "summarize releases",
        "summarise releases",
        "major themes",
        "trends",
        "recent work"

    ]

    if any(
        pattern in q
        for pattern in trend_patterns
    ):

        return {
            "route": "TREND"
        }

    # ==================================================
    # DEFAULT
    # ==================================================

    return {
        "route": "RAG"
    }