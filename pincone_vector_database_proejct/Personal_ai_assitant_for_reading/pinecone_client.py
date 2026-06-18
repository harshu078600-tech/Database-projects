

import os
from pinecone import Pinecone

ASSISTANT_NAME = "mr-x"


def get_api_key():

    try:
        import streamlit as st
        if "PINECONE_API_KEY" in st.secrets:
            return st.secrets["PINECONE_API_KEY"]
    except Exception:
        pass
    return os.getenv("PINECONE_API_KEY")


def get_assistant():
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "PINECONE_API_KEY not found. Set it in a .env file locally, "
            "or in Streamlit Cloud Settings > Secrets when deployed."
        )
    pc = Pinecone(api_key=api_key)
    return pc.assistant.describe_assistant(assistant_name=ASSISTANT_NAME)


def upload_file(assistant, file_path, metadata=None):
    """Upload a single file to the assistant's knowledge base."""
    return assistant.upload_file(
        file_path=file_path,
        metadata=metadata or {},
        timeout=None,
    )


def list_files(assistant):

    return assistant.list_files()


def ask_question(assistant, query, chat_history=None):
    """
    Ask the assistant a question, optionally including prior turns for context.
    Returns (answer_text, list_of_source_filenames).
    """
    messages = (chat_history or []) + [{"role": "user", "content": query}]
    resp = assistant.chat(messages=messages)

    sources = []
    if resp.citations:
        for citation in resp.citations:
            for ref in citation.references:
                name = ref["file"]["name"]
                if name not in sources:
                    sources.append(name)

    return resp.message.content, sources


if __name__ == "__main__":
    api_key = get_api_key()

    pc = Pinecone(api_key=api_key)

    print("Assistants:")
    print(pc.assistant.list_assistants())

    print("\nDetails:")
    print(pc.assistant.describe_assistant("mr-x"))





