from fastapi import FastAPI
from pydantic import BaseModel

from src.query_engine.query_engine import (
    get_story,
    get_release,
    get_latest_release,
    get_stories_by_release,
    get_releases_by_author,
    count_releases_by_year
)

from src.search.search_engine import (
    global_search
)

from src.comparison.release_compare import (
    compare_releases
)

from src.llm.qwen_formatter import (
    generate_search_answer,
    generate_compare_answer,
    generate_trend_answer,
    generate_rag_answer
)

from src.intents.intent_classifier import (
    classify
)

from src.router.question_router import (
    route_question
)

from src.router.entity_extractor import (
    extract_entities
)

app = FastAPI(
    title="Release Intelligence API",
    version="1.0.0"
)


# ======================================================
# REQUEST MODELS
# ======================================================

class StoryRequest(BaseModel):
    story_id: str


class ReleaseRequest(BaseModel):
    release_number: int


class SearchRequest(BaseModel):
    keyword: str


class CompareRequest(BaseModel):
    release1: int
    release2: int


class AskRequest(BaseModel):
    question: str
    evidence: str


class SmartAskRequest(BaseModel):
    question: str


# ======================================================
# HEALTH
# ======================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ======================================================
# STORY
# ======================================================

@app.post("/story")
def story(request: StoryRequest):

    return get_story(
        request.story_id
    )


# ======================================================
# RELEASE
# ======================================================

@app.post("/release")
def release(request: ReleaseRequest):

    return get_release(
        request.release_number
    )


# ======================================================
# SEARCH
# ======================================================

@app.post("/search")
def search(request: SearchRequest):

    return global_search(
        request.keyword
    )


# ======================================================
# COMPARE
# ======================================================

@app.post("/compare")
def compare(request: CompareRequest):

    return compare_releases(
        request.release1,
        request.release2
    )


# ======================================================
# MANUAL ASK
# ======================================================

@app.post("/ask")
def ask(request: AskRequest):

    answer = generate_answer(
        request.question,
        request.evidence
    )

    return {
        "answer": answer
    }


# ======================================================
# SMART ASK
# ======================================================

@app.post("/ask-smart")
def ask_smart(request: SmartAskRequest):

    question = request.question

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

    if route == "FACT":

        return {
            "route": route,
            "action": action,
            "answer": result
        }

    elif route == "COMPARE":

        answer = generate_compare_answer(
            question,
            str(result)
        )

    elif route == "SEARCH":

        answer = generate_search_answer(
            question,
            str(result)
        )

    elif route == "TREND":

        answer = generate_trend_answer(
            question,
            str(result)
        )

    else:

        answer = generate_rag_answer(
            question,
            str(result)
        )

    return {
        "route": route,
        "action": action,
        "answer": answer
    }

    # ==================================================
    # COMPARE RELEASES
    # ==================================================

    if intent == "COMPARE_RELEASES":

        evidence = compare_releases(
            entities["release1"],
            entities["release2"]
        )

    # ==================================================
    # STORY LOOKUP
    # ==================================================

    elif intent == "STORY_LOOKUP":

        if "story_id" in entities:

            evidence = get_story(
                entities["story_id"]
            )

    # ==================================================
    # RELEASE LOOKUP
    # ==================================================

    elif intent == "RELEASE_LOOKUP":

        if "release_number" in entities:

            evidence = get_release(
                entities["release_number"]
            )

    # ==================================================
    # STORIES BY RELEASE
    # ==================================================

    elif intent == "STORIES_BY_RELEASE":

        if "release_number" in entities:

            evidence = get_stories_by_release(
                entities["release_number"]
            )

    # ==================================================
    # LATEST RELEASE
    # ==================================================

    elif intent == "LATEST_RELEASE":

        evidence = get_latest_release()

    # ==================================================
    # SEARCH
    # ==================================================

    elif intent == "SEARCH":

        keyword = (
            question
            .replace("find", "")
            .replace("Find", "")
            .replace("search", "")
            .replace("Search", "")
            .strip()
        )

        evidence = global_search(
            keyword
        )

    # ==================================================
    # RELEASES BY AUTHOR
    # ==================================================

    elif intent == "RELEASES_BY_AUTHOR":

        q = question.lower()

        if "rohan" in q:

            evidence = get_releases_by_author(
                "Rohan Chaugule"
            )

        elif "kunal" in q:

            evidence = get_releases_by_author(
                "Kunal Panchal"
            )

        elif "rupal" in q:

            evidence = get_releases_by_author(
                "Rupal Koli"
            )

        else:

            evidence = {
                "message":
                "Author not recognized."
            }

    # ==================================================
    # RELEASE COUNT BY YEAR
    # ==================================================

    elif intent == "RELEASE_COUNT_BY_YEAR":

        if "year" in entities:

            evidence = {

                "year": entities["year"],

                "release_count":
                    count_releases_by_year(
                        entities["year"]
                    )
            }

        else:

            evidence = {

                "message":
                "Year not found."
            }

    # ==================================================
    # UNKNOWN
    # ==================================================

    else:

        evidence = {

            "message":
            "Intent currently not supported."
        }

    answer = generate_answer(

        question,

        str(evidence)

    )

    return {

        "question":
            question,

        "intent":
            intent,

        "entities":
            entities,

        "answer":
            answer
    }