import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/ask-smart"

st.set_page_config(
    page_title="Release Intelligence Assistant",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AAI Release Intelligence Assistant")

question = st.text_input(
    "Ask a question",
    placeholder="e.g. What changed recently?"
)

if st.button("Ask"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            response = requests.post(
                API_URL,
                json={
                    "question": question
                },
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            st.markdown(
                f"**Route:** {data.get('route')}"
            )

            action = data.get(
                "action"
            )

            if action:

                st.markdown(
                    f"**Action:** {action}"
                )

            st.markdown(
                "---"
            )

            answer = data.get(
                "answer"
            )

            if isinstance(
                answer,
                dict
            ):

                st.json(answer)

            else:

                st.markdown(answer)

        except Exception as ex:

            st.error(
                str(ex)
            )