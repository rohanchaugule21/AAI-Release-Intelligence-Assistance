from src.router.question_router import (
    route_question
)

from src.router.entity_extractor import (
    extract_entities
)


while True:

    question = input(
        "\nAsk Anything: "
    )

    if question.lower() == "exit":

        break

    entities = extract_entities(
        question
    )

    result = route_question(
        question,
        entities
    )

    print("\n")
    print("=" * 100)
    print("ROUTE")
    print("=" * 100)

    print(
        result["route"]
    )

    print("\n")
    print("=" * 100)
    print("RESULT")
    print("=" * 100)

    print(
        result["result"]
    )