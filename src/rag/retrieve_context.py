from src.search.semantic_search import (
    semantic_search
)


def retrieve_context(
    question,
    top_k=5
):

    results = semantic_search(
        question,
        top_k=top_k
    )

    evidence = []

    for item in results:

        content = item["content"]

        # Prevent huge prompts

        content = content[:1000]

        evidence.append(
            content
        )

    context = "\n\n".join(
        evidence
    )

    print(
        f"\nRetrieved Records: {len(results)}"
    )

    print(
        f"Context Length: {len(context)} characters"
    )

    return context