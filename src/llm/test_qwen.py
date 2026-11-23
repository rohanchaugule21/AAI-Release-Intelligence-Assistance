from src.query_engine.query_engine import (
    get_story
)

from src.llm.qwen_formatter import (
    generate_answer
)

story = get_story(
    "1702007"
)

question = (
    "Explain story 1702007"
)

answer = generate_answer(
    question,
    story
)

print("\n")
print(answer)
