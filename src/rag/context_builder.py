def build_context(records):

    context = []

    context.append(
        "RELEVANT RELEASE INTELLIGENCE DATA"
    )

    context.append("=" * 60)

    for record in records:

        source_type = record.get(
            "source_type",
            "unknown"
        )

        release = record.get(
            "release_number",
            "NA"
        )

        content = record["content"]

        # Prevent sending huge records to Qwen

        content = content[:500]

        context.append(
            f"\nSource Type: {source_type}"
        )

        context.append(
            f"Release: {release}"
        )

        context.append(
            content
        )

        context.append(
            "-" * 60
        )

    return "\n".join(
        context
    )