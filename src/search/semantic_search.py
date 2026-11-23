import json
from pathlib import Path

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

KNOWLEDGE_FILE = (
    ROOT / "data" / "unified_knowledge.json"
)

with open(
    KNOWLEDGE_FILE,
    "r",
    encoding="utf-8"
) as fp:

    KNOWLEDGE = json.load(fp)

DOCUMENTS = [

    item["content"]

    for item in KNOWLEDGE
]

VECTORIZER = TfidfVectorizer()

MATRIX = VECTORIZER.fit_transform(
    DOCUMENTS
)


def semantic_search(
    question,
    top_k=10
):

    question_vector = (
        VECTORIZER.transform(
            [question]
        )
    )

    scores = cosine_similarity(
        question_vector,
        MATRIX
    )[0]

    ranked = sorted(

        zip(
            scores,
            KNOWLEDGE
        ),

        key=lambda x: x[0],

        reverse=True

    )

    return [

        item

        for score, item
        in ranked[:top_k]

    ]