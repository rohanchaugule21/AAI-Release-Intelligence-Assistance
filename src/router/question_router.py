import re

from src.planner.query_planner import (
    plan
)

from src.query_engine.query_engine import (
    get_latest_release,
    get_release,
    get_story,
    get_releases_by_author,
    count_releases_by_year,
    get_last_n_releases,
    get_all_releases,
    get_author_names,
    build_trend_evidence
)

from src.search.search_engine import (
    global_search
)

from src.comparison.release_compare import (
    compare_releases
)

from src.rag.answer_question import (
    answer_question
)


def route_question(
    question,
    entities
):

    planner_result = plan(
        question
    )

    route = planner_result["route"]

    action = planner_result.get(
        "action",
        None
    )

    q = question.lower()

    # ==================================================
    # FACT ENGINE
    # ==================================================

    if route == "FACT":

        if action == "LATEST_RELEASE":

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": get_latest_release()
            }

        elif action == "RELEASE_COUNT":

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": {
                    "total_releases":
                        len(
                            get_all_releases()
                        )
                }
            }

        elif action == "LIST_ALL_RELEASES":

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": get_all_releases()
            }

        elif action == "STORY_LOOKUP":

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": get_story(
                    entities["story_id"]
                )
            }

        elif action == "AUTHOR_LOOKUP":

            matched_author = None

            authors = get_author_names()

            normalized_question = re.sub(
                r"[^a-z0-9 ]",
                "",
                q.lower()
            )

            for author in authors:

                normalized_author = re.sub(
                    r"[^a-z0-9 ]",
                    "",
                    author.lower()
                )

                if (
                    normalized_author
                    in normalized_question
                ):

                    matched_author = author
                    break

            if matched_author:

                result = get_releases_by_author(
                    matched_author
                )

            else:

                release_number = entities.get(
                    "release_number"
                )

                result = get_release(
                    release_number
                )

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": result
            }

        elif action == "RELEASE_DETAILS":

            return {
                "route": "FACT",
                "action": action,
                "use_llm": False,
                "result": get_release(
                    entities["release_number"]
                )
            }

    # ==================================================
    # COMPARE ENGINE
    # ==================================================

    if route == "COMPARE":

        return {
            "route": "COMPARE",
            "action": None,
            "use_llm": True,
            "result": compare_releases(
                entities["release_1"],
                entities["release_2"]
            )
        }

    # ==================================================
    # SEARCH ENGINE
    # ==================================================

    if route == "SEARCH":

        keyword = entities.get(
            "keyword",
            question
        )

        return {
            "route": "SEARCH",
            "action": None,
            "use_llm": True,
            "result": global_search(
                keyword
            )
        }

    # ==================================================
    # TREND ENGINE
    # ==================================================

    if route == "TREND":

        count = entities.get(
            "count",
            5
        )

        return {
            "route": "TREND",
            "action": None,
            "use_llm": True,
            "result": build_trend_evidence(
                count
            )
        }

    # ==================================================
    # FALLBACK TO RAG
    # ==================================================

    return {
        "route": "RAG",
        "action": None,
        "use_llm": True,
        "result": answer_question(
            question
        )
    }