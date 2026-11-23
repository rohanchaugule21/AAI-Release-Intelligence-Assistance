import json
import re
from pathlib import Path


ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

KNOWLEDGE_FILE = ROOT / "data" / "knowledge_base.json"


with open(
    KNOWLEDGE_FILE,
    "r",
    encoding="utf-8"
) as fp:
    KNOWLEDGE = json.load(fp)


def extract_release(question):

    match = re.search(
        r"release\s+(\d+)",
        question,
        re.IGNORECASE
    )

    if match:
        return int(
            match.group(1)
        )

    return None


def extract_story(question):

    match = re.search(
        r"(\d{6,8})",
        question
    )

    if match:
        return match.group(1)

    return None


def search(question):

    release_number = extract_release(
        question
    )

    story_number = extract_story(
        question
    )

    results = []

    for record in KNOWLEDGE:

        # Release filter

        if release_number:

            if (
                record["release_number"]
                != release_number
            ):
                continue

        # Story filter

        if story_number:

            if (
                story_number
                not in record["content"]
            ):
                continue

        keyword_score = 0

        for word in question.lower().split():

            if (
                word
                in record["content"].lower()
            ):
                keyword_score += 1

        if keyword_score > 0:

            results.append(
                (
                    keyword_score,
                    record
                )
            )

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        r[1]
        for r in results
    ]