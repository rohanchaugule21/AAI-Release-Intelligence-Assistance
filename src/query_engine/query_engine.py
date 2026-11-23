import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

# ==========================================================
# FILES
# ==========================================================

RELEASE_FILE = ROOT / "data" / "release_master.json"

STORY_FILE = ROOT / "data" / "story_master.json"

RELEASE_HISTORY_FILE = (
    ROOT / "data" / "release_history_master.json"
)

# ==========================================================
# LOAD DATA
# ==========================================================

with open(
    RELEASE_FILE,
    "r",
    encoding="utf-8"
) as fp:

    RELEASES = json.load(fp)

with open(
    STORY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    STORIES = json.load(fp)

with open(
    RELEASE_HISTORY_FILE,
    "r",
    encoding="utf-8"
) as fp:

    RELEASE_HISTORY = json.load(fp)

# ==========================================================
# RELEASE FUNCTIONS
# ==========================================================

def get_latest_release():

    releases = sorted(
        RELEASE_HISTORY,
        key=lambda x:
        x["release_number"]
    )

    return releases[-1]


def get_release(release_no):

    for release in RELEASE_HISTORY:

        if (
            release["release_number"]
            == release_no
        ):

            return release

    return None


def get_all_releases():

    return sorted(
        RELEASE_HISTORY,
        key=lambda x:
        x["release_number"]
    )


def get_last_n_releases(count):

    releases = sorted(
        RELEASE_HISTORY,
        key=lambda x:
        x["release_number"]
    )

    return releases[-count:]

# ==========================================================
# STORY FUNCTIONS
# ==========================================================

def get_story(story_id):

    for story in STORIES:

        if (
            story["story_id"]
            == str(story_id)
        ):

            return story

    return None


def get_stories_by_release(release_no):

    return [

        story

        for story in STORIES

        if story["release_number"]
        == release_no

    ]

# ==========================================================
# RELEASE HISTORY FUNCTIONS
# ==========================================================

def get_releases_by_year(year):

    results = []

    for release in RELEASE_HISTORY:

        release_date = str(
            release.get(
                "release_date"
            )
        )

        if (
            release_date
            and release_date.endswith(
                str(year)
            )
        ):

            results.append(
                release
            )

    return results


def count_releases_by_year(year):

    return len(
        get_releases_by_year(year)
    )


def get_releases_by_author(author):

    results = []

    for release in RELEASE_HISTORY:

        release_author = str(
            release.get(
                "author"
            )
        )

        if (
            author.lower()
            in release_author.lower()
        ):

            results.append(
                release
            )

    return results


def get_author_names():

    authors = set()

    for release in RELEASE_HISTORY:

        author = release.get(
            "author"
        )

        if author:

            authors.add(
                author
            )

    return sorted(
        list(authors)
    )

def build_trend_evidence(count=5):

    from src.trends.trend_engine import (
        get_recent_release_summary
    )

    return get_recent_release_summary(
        count
    )
    
def get_release_by_version(version):

    for release in RELEASE_HISTORY:

        release_version = str(
            release.get(
                "application_version"
            )
        )

        if (
            release_version.lower()
            ==
            version.lower()
        ):

            return release

    return None