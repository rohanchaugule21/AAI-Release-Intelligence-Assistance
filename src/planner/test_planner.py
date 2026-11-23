from src.planner.query_planner import (
    plan
)

while True:

    question = input(
        "\nQuestion: "
    )

    if question.lower() == "exit":

        break

    result = plan(
        question
    )

    print(
        f"\nRoute: {result['route']}"
    )