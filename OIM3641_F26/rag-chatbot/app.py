import os
from pathlib import Path

from dotenv import load_dotenv
from google.genai import errors as genai_errors
import httpx
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI
import streamlit as st

load_dotenv()

DATA_DIR = Path(__file__).parent / "data"


def get_api_key():
    """Return GEMINI_API_KEY, or show an error and stop the app if it is missing."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error(
            "GEMINI_API_KEY not found. Add a line `GEMINI_API_KEY=your-key` "
            "to the .env file next to app.py, then restart the app."
        )
        st.stop()
    return api_key


def validate_data_dir():
    """Stop the app with a clear message unless DATA_DIR is a folder with visible files."""
    if not DATA_DIR.is_dir():
        st.error(
            f"Data folder not found: `{DATA_DIR}`. "
            "Create it and put the handbook PDF inside, then restart the app."
        )
        st.stop()
    # Ignore hidden files such as .DS_Store so they don't count as documents
    if not any(p.is_file() and not p.name.startswith(".") for p in DATA_DIR.iterdir()):
        st.error(
            f"Data folder `{DATA_DIR}` is empty. "
            "Add the handbook PDF to it, then restart the app."
        )
        st.stop()


@st.cache_resource(show_spinner="Indexing the handbook...")
def get_query_engine(api_key):
    """Load the documents, build the vector index, and return a cached query engine."""
    Settings.llm = GoogleGenAI(model="gemini-3.5-flash-lite", api_key=api_key)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    documents = SimpleDirectoryReader(str(DATA_DIR)).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()


st.title("Babson Handbook Chatbot")

api_key = get_api_key()
validate_data_dir()

try:
    query_engine = get_query_engine(api_key)
except Exception as e:
    st.error(
        f"Could not build the search index: {e}. Check that the PDFs in "
        f"`{DATA_DIR}` are valid and that you are online (the embedding model "
        "may need to download), then restart the app."
    )
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Ask a question about the student handbook"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                answer = query_engine.query(question).response
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except httpx.TransportError:
            st.error("Could not reach the Gemini API. Check your internet connection and ask again.")
        except genai_errors.APIError as e:
            st.error(f"The Gemini API returned an error ({e.code}): it may be a rate limit or a bad key. Wait a moment and ask again.")
        except Exception as e:
            st.error(f"Something went wrong answering that question: {e}. Please try again.")
