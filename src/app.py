from src.router.entity_extractor import (
    extract_entities
)

from src.router.question_router import (
    route_question
)

from src.llm.qwen_formatter import (
    generate_search_answer,
    generate_compare_answer,
    generate_trend_answer,
    generate_rag_answer
)

from src.executors.release_executor import (
    execute as release_execute
)

from src.executors.story_executor import (
    execute as story_execute
)

from src.query_engine.query_engine import (
    get_all_releases
)

from src.formatter.fact_formatter import (
    format_release_details,
    format_release_count,
    format_story,
    format_release_list
)


def print_result(result):

    print("\n")
    print("=" * 100)

    if isinstance(result, list):

        print(
            f"Records Found: {len(result)}"
        )

        print("=" * 100)

        for item in result:

            print(item)

            print("-" * 100)

    else:

        print(result)

    print("=" * 100)


def build_comparison_evidence(result):

    evidence = []

    stories = result["stories"]

    components = result["components"]

    evidence.append(
        f"Release {stories['release_1']} Deliveries"
    )

    for story in stories["release_1_deliveries"]:

        evidence.append(
            f"Story {story['story_id']} : "
            f"{story['title']}"
        )

    evidence.append("")

    evidence.append(
        f"Release {stories['release_2']} Deliveries"
    )

    for story in stories["release_2_deliveries"]:

        evidence.append(
            f"Story {story['story_id']} : "
            f"{story['title']}"
        )

    evidence.append("")

    evidence.append(
        f"Components in Release "
        f"{components['release_1']}"
    )

    for component in components[
        "present_in_release_1"
    ]:

        evidence.append(
            component["component_name"]
        )

    evidence.append("")

    evidence.append(
        f"Components in Release "
        f"{components['release_2']}"
    )

    for component in components[
        "present_in_release_2"
    ]:

        evidence.append(
            component["component_name"]
        )

    return "\n".join(evidence)


def main():

    print("\n")
    print("=" * 100)
    print("AAI RELEASE INTELLIGENCE BOT")
    print("=" * 100)

    while True:

        question = input(
            "\nAsk Release Intelligence Bot: "
        )

        if question.lower() == "exit":

            break

        entities = extract_entities(
            question
        )

        route_info = route_question(
            question,
            entities
        )

        route = route_info["route"]

        action = route_info.get(
            "action",
            None
        )

        result = route_info["result"]

        print(
            f"\nRoute: {route}"
        )

        print(
            f"Action: {action}"
        )

        print(
            f"Entities: {entities}"
        )

        try:

            # ==================================================
            # FACT ENGINE
            # ==================================================

            if route == "FACT":

                if action == "LATEST_RELEASE":

                    print(
                        format_release_details(
                            result
                        )
                    )

                elif action == "RELEASE_COUNT":

                    print(
                        format_release_count(
                            result[
                                "total_releases"
                            ]
                        )
                    )

                elif action == "LIST_ALL_RELEASES":

                    print(
                        format_release_list(
                            result
                        )
                    )

                elif action == "STORY_LOOKUP":

                    print(
                        format_story(
                            result
                        )
                    )

                else:

                    print_result(result)

                continue

            # ==================================================
            # COMPARE ENGINE
            # ==================================================

            elif route == "COMPARE":

                evidence = (
                    build_comparison_evidence(
                        result
                    )
                )

                answer = generate_compare_answer(
                    question,
                    evidence
                )

                print("\n")
                print("=" * 100)
                print("AI ANSWER")
                print("=" * 100)
                print(answer)
                print("=" * 100)

            # ==================================================
            # SEARCH ENGINE
            # ==================================================

            elif route == "SEARCH":

                answer = generate_search_answer(
                    question,
                    str(result)
                )

                print("\n")
                print("=" * 100)
                print("AI ANSWER")
                print("=" * 100)
                print(answer)
                print("=" * 100)

            # ==================================================
            # TREND ENGINE
            # ==================================================

            elif route == "TREND":


                answer = generate_trend_answer(
                    question,
                    str(result)
                )

                print("\n")
                print("=" * 100)
                print("AI ANSWER")
                print("=" * 100)
                print(answer)
                print("=" * 100)

            # ==================================================
            # RAG ENGINE
            # ==================================================

            elif route == "RAG":

                answer = generate_rag_answer(
                    question,
                    str(result)
                )

                print("\n")
                print("=" * 100)
                print("AI ANSWER")
                print("=" * 100)
                print(answer)
                print("=" * 100)

            # ==================================================
            # FALLBACK
            # ==================================================

            else:

                print(
                    "\nRoute not supported."
                )

        except Exception as ex:

            print("\nERROR")
            print("=" * 100)
            print(ex)
            print("=" * 100)


if __name__ == "__main__":
    main()