def format_release_details(
    release
):

    if not release:

        return "Release not found."

    return f"""
Release {release['release_number']}

Application Version
-------------------
{release['application_version']}

Author
------
{release['author']}

Release Date
------------
{release['release_date']}

Source File
-----------
{release['filename']}
"""


def format_release_count(
    count
):

    return (
        f"Total Releases Available: {count}"
    )


def format_story(
    story
):

    if not story:

        return "Story not found."

    return f"""
Story ID
--------
{story['story_id']}

Title
-----
{story['title']}

Release
-------
{story['release_number']}

Airport
-------
{story['airport']}

Impact
------
{story['impact']}
"""


def format_release_list(
    releases
):

    lines = []

    lines.append(
        "Available Releases"
    )

    lines.append(
        "-" * 30
    )

    for release in releases:

        lines.append(

            f"Release "
            f"{release['release_number']} "
            f"({release['application_version']})"

        )

    return "\n".join(lines)
