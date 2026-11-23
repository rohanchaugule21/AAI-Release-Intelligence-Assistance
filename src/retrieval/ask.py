from retriever import search


while True:

    question = input(
        "\nAsk Question: "
    )

    if question.lower() == "exit":
        break

    results = search(
        question
    )

    print("\n")
    print("=" * 100)
    print(
        f"Found {len(results)} matches"
    )
    print("=" * 100)

    for result in results[:5]:

        print("\n")

        print(
            f"Release : {result['release_number']}"
        )

        print(
            f"Version : {result['release_version']}"
        )

        print(
            f"Airport : {result['airport']}"
        )

        print(
            f"Section : {result['section']}"
        )

        print("-" * 80)

        print(
            result["content"][:1000]
        )