from src.rag.answer_question import (
    answer_question
)


while True:

    question = input(
        "\nAsk Anything: "
    )

    if question.lower() == "exit":

        break

    answer = answer_question(
        question
    )

    print("\n")
    print("=" * 100)
    print("ANSWER")
    print("=" * 100)

    print(answer)

    print("=" * 100)