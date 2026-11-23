import json
import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:7b"


def ask_qwen(
    prompt,
    temperature=0.1,
    timeout=600
):
    """
    Sends a prompt to Ollama/Qwen
    and returns the generated text.
    """

    payload = {

        "model": MODEL,

        "prompt": prompt,

        "stream": False,

        "options": {
            "temperature": temperature
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=timeout
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            ""
        ).strip()

    except Exception as ex:

        return (
            "Qwen/Ollama Error: "
            f"{str(ex)}"
        )
