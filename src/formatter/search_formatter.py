def format_search_results(
    keyword,
    results
):

    lines = []

    lines.append(
        f"Search Results : {keyword}"
    )

    lines.append(
        "=" * 60
    )

    # Stories

    stories = results["stories"]

    if stories:

        lines.append("")
        lines.append(
            "STORIES"
        )

        lines.append(
            "-" * 60
        )

        for story in stories:

            lines.append(
                f"Release "
                f"{story['release_number']}"
            )

            lines.append(
                f"Story "
                f"{story['story_id']}"
            )

            lines.append(
                story["title"]
            )

            lines.append("")

    # Components

    components = results[
        "components"
    ]

    if components:

        lines.append("")
        lines.append(
            "COMPONENTS"
        )

        lines.append(
            "-" * 60
        )

        for comp in components:

            lines.append(
                f"Release "
                f"{comp['release_number']}"
            )

            lines.append(
                comp[
                    "component_name"
                ]
            )

            lines.append("")

    return "\n".join(lines)