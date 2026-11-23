def format_comparison(
    result
):

    lines = []

    stories = result[
        "stories"
    ]

    components = result[
        "components"
    ]

    lines.append(
        f"Release "
        f"{stories['release_1']}"
        f" vs "
        f"{stories['release_2']}"
    )

    lines.append("")

    # Added Stories

    lines.append(
        "ADDED STORIES"
    )

    lines.append(
        "-" * 50
    )

    for story in stories["added"]:

        lines.append(
            f"{story['story_id']} - "
            f"{story['title']}"
        )

    lines.append("")

    # Removed Stories

    lines.append(
        "REMOVED STORIES"
    )

    lines.append(
        "-" * 50
    )

    for story in stories["removed"]:

        lines.append(
            f"{story['story_id']} - "
            f"{story['title']}"
        )

    lines.append("")

    # Added Components

    lines.append(
        "ADDED COMPONENTS"
    )

    lines.append(
        "-" * 50
    )

    for component in components["added"]:

        lines.append(
            component
        )

    return "\n".join(lines)