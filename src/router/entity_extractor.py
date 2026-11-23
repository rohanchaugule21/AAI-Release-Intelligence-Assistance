import re


def extract_entities(question):

    entities = {}

    q = question.strip()

    # ==================================================
    # RELEASE NUMBERS
    # ==================================================

    releases = re.findall(
        r"release\s+(\d+)",
        q,
        re.IGNORECASE
    )

    if len(releases) == 1:

        entities["release_number"] = int(
            releases[0]
        )

    elif len(releases) >= 2:

        entities["release_1"] = int(
            releases[0]
        )

        entities["release_2"] = int(
            releases[1]
        )

    # ==================================================
    # STORY ID
    # ==================================================

    story_match = re.search(
        r"\b(\d{6,8})\b",
        q
    )

    if story_match:

        entities["story_id"] = (
            story_match.group(1)
        )

    # ==================================================
    # YEAR
    # ==================================================

    year_match = re.search(
        r"\b(20\d{2})\b",
        q
    )

    if year_match:

        entities["year"] = int(
            year_match.group(1)
        )

    # ==================================================
    # LAST N RELEASES
    # ==================================================

    count_match = re.search(
        r"last\s+(\d+)",
        q,
        re.IGNORECASE
    )

    if count_match:

        entities["count"] = int(
            count_match.group(1)
        )

    # ==================================================
    # SEARCH KEYWORD EXTRACTION
    # ==================================================

    lower_q = q.lower()

    # Find X

    if lower_q.startswith("find "):

        entities["keyword"] = (
            q[5:]
            .strip(" .,!?:;")
        )

    # Search X

    elif lower_q.startswith("search "):

        entities["keyword"] = (
            q[7:]
            .strip(" .,!?:;")
        )

    # Show me everything related to X

    elif "related to" in lower_q:

        entities["keyword"] = (
            q.split("related to")[-1]
            .strip(" .,!?:;")
        )

    # Information about X

    elif "information about" in lower_q:

        entities["keyword"] = (
            q.split("information about")[-1]
            .strip(" .,!?:;")
        )

    # What work has been done around X

    elif "work has been done around" in lower_q:

        entities["keyword"] = (
            q.split("around")[-1]
            .strip(" .,!?:;")
        )

    # Which release introduced X

    elif "introduced" in lower_q:

        entities["keyword"] = (
            q.split("introduced")[-1]
            .strip(" .,!?:;")
        )

    # Where was X delivered

    elif lower_q.startswith("where was"):

        keyword = (
            q[9:]
            .replace("delivered", "")
            .strip(" .,!?:;")
        )

        entities["keyword"] = keyword

    # Show me X

    elif lower_q.startswith("show me "):

        entities["keyword"] = (
            q[8:]
            .strip(" .,!?:;")
        )

    return entities