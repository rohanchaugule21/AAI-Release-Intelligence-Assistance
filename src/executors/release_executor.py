from src.query_engine.query_engine import (
    get_latest_release,
    get_release
)


def execute(intent, entities):

    if intent == "LATEST_RELEASE":

        return get_latest_release()

    if intent == "RELEASE_LOOKUP":

        if "release_number" in entities:

            return get_release(
                entities["release_number"]
            )

    return None