import requests


OLLAMA_URL = (
    "http://localhost:11434/api/generate"
)


def generate_answer(
    question,
    evidence
):

    prompt = f"""
You are an AAI Release Intelligence Assistant.

Answer only using the provided evidence.

Question:
{question}

Evidence:
{evidence}

Requirements:
- Be concise.
- Use business friendly language.
- Do not invent information.
- Mention release number if available.
"""

    response = requests.post(

        OLLAMA_URL,

        json={

            "model":
                "qwen2.5:7b",

            "prompt":
                prompt,

            "stream":
                False
        }
    )

    return response.json()[
        "response"
    ]