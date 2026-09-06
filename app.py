import streamlit as st
from google import genai

st.set_page_config(
    page_title="Charans LLM",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Charans LLM")
st.write("Ask anything")

# API key is stored securely in Streamlit Secrets.
API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is Python?",
)

if st.button("Ask", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=question,
                )

            st.subheader("Answer")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
