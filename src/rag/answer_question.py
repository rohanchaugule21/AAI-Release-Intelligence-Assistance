from src.search.semantic_search import (
    semantic_search
)

from src.rag.context_builder import (
    build_context
)

from src.llm.qwen_formatter import (
    generate_rag_answer
)


def answer_question(
    question
):

    records = semantic_search(
        question,
        top_k=5
    )

    context = build_context(
        records
    )

    answer = generate_rag_answer(
        question,
        context
    )

    return answer