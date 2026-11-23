def format_story(story):

    if not story:

        return "Story not found."

    output = []

    output.append(
        f"Release {story['release_number']} "
        f"({story['airport']})"
    )

    output.append("")

    output.append(
        f"Story ID : {story['story_id']}"
    )

    output.append("")

    output.append("Title:")

    output.append(
        story["title"]
    )

    output.append("")

    output.append(
        f"Impact: {story['impact']}"
    )

    output.append("")

    output.append(
        f"Source: "
        f"{story['source_file']}"
    )

    return "\n".join(output)