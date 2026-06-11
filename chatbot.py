import streamlit as st
import ollama

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="Cafe AI Assistant")

st.title("☕ AI Cafe Assistant")

# Load Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS
db = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

question = st.text_input("Ask about the menu")

if question:

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    st.subheader("Retrieved Context")
    st.code(context)

    prompt = f"""
You are an AI Cafe Assistant.

Use ONLY the information below.

If the answer is not found, reply exactly:

I could not find that information in the menu.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = ollama.chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("AI Answer")
        st.success(
            response["message"]["content"]
        )

    except Exception as e:
        st.error(f"Ollama Error: {e}")