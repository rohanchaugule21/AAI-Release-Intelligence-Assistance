from src.search.semantic_search import (
    semantic_search
)

question = (
    "What changed recently "
    "for availability reporting?"
)

results = semantic_search(
    question
)

for item in results:

    print("\n")

    print("=" * 80)

    print(
        item["source_type"]
    )

    print(
        item["release_number"]
    )

    print(
        item["content"][:500]
    )