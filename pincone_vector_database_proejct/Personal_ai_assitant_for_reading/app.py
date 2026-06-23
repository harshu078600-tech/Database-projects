import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Ab API key access karo
api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("PINECONE_API_KEY not found. Check your .env file.")



import streamlit as st
from pinecone_client import get_assistant, upload_file, list_files, ask_question

st.set_page_config(
    page_title="MR. X",
    page_icon="🧠",
    layout="wide"
)


st.markdown("""
<style>

/* ---------- IMPORT FONT ---------- */

@import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ---------- BACKGROUND ---------- */

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at top left, rgba(255,255,255,0.18), transparent 35%),
        radial-gradient(circle at bottom right, rgba(255,255,255,0.12), transparent 30%),
        linear-gradient(135deg,
            #0f172a 0%,
            #1e293b 35%,
            #312e81 70%,
            #4c1d95 100%);
    background-attachment: fixed;
    overflow: hidden;
}

/* Floating light effects */

[data-testid="stAppViewContainer"]::before,
[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    width: 420px;
    height: 420px;
    border-radius: 50%;
    filter: blur(90px);
    z-index: -1;
}

[data-testid="stAppViewContainer"]::before {
    background: rgba(99, 102, 241, 0.28);
    top: -120px;
    left: -120px;
}

[data-testid="stAppViewContainer"]::after {
    background: rgba(236, 72, 153, 0.22);
    bottom: -120px;
    right: -120px;
}

/* ---------- MAIN CONTAINER ---------- */

.main .block-container {
    padding-top: 2rem;
    max-width: 850px;
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(30px) saturate(180%);
    -webkit-backdrop-filter: blur(30px) saturate(180%);

    border-right: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        8px 0 32px rgba(0,0,0,0.15),
        inset -1px 0 0 rgba(255,255,255,0.08);
}

/* ---------- TITLES ---------- */

h1, h2, h3, p, label, .stMarkdown {
    color: rgba(255,255,255,0.95) !important;
}

h1 {
    font-weight: 700;
    letter-spacing: -0.04em;
    font-size: 3rem !important;
}

[data-testid="stCaptionContainer"] {
    color: rgba(255,255,255,0.72);
}

/* ---------- CHAT MESSAGES ---------- */

div[data-testid="stChatMessage"] {
    background: transparent;
    border: none;
}

div[data-testid="stChatMessageContent"] {
    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);

    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 28px;

    box-shadow:
        0 12px 40px rgba(0,0,0,0.18),
        inset 0 1px 1px rgba(255,255,255,0.18);

    padding: 1rem 1.25rem;

    color: rgba(255,255,255,0.96);

    transition: all 0.25s ease;
}

div[data-testid="stChatMessageContent"]:hover {
    transform: translateY(-2px);

    background: rgba(255,255,255,0.14);

    box-shadow:
        0 18px 50px rgba(0,0,0,0.22),
        inset 0 1px 1px rgba(255,255,255,0.25);
}

/* ---------- CHAT INPUT ---------- */

div[data-testid="stChatInput"] {
    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(30px) saturate(180%);
    -webkit-backdrop-filter: blur(30px) saturate(180%);

    border: 1px solid rgba(255,255,255,0.20);

    border-radius: 24px;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.16),
        inset 0 1px 1px rgba(255,255,255,0.15);

    padding: 8px 14px;
}

div[data-testid="stChatInput"]:focus-within {
    border: 1px solid rgba(255,255,255,0.35);

    box-shadow:
        0 0 0 4px rgba(255,255,255,0.08),
        0 16px 40px rgba(0,0,0,0.20);
}

div[data-testid="stChatInput"] textarea {
    color: white !important;
    background: transparent !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(255,255,255,0.55) !important;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    width: 100%;

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.18);

    color: white;

    border-radius: 18px;

    padding: 0.65rem 1rem;

    transition: all 0.25s ease;

    box-shadow:
        0 8px 24px rgba(0,0,0,0.12),
        inset 0 1px 1px rgba(255,255,255,0.12);
}

.stButton > button:hover {
    transform: translateY(-2px);

    background: rgba(255,255,255,0.18);

    box-shadow:
        0 12px 32px rgba(0,0,0,0.18),
        inset 0 1px 1px rgba(255,255,255,0.2);
}

/* ---------- FILE UPLOADER ---------- */

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);

    border: 1px dashed rgba(255,255,255,0.25);

    border-radius: 22px;

    backdrop-filter: blur(20px);

    padding: 1rem;
}

/* ---------- EXPANDERS ---------- */

details {
    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.14);

    border-radius: 18px;

    backdrop-filter: blur(20px);

    overflow: hidden;
}

/* ---------- SCROLLBAR ---------- */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.15);
    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255,255,255,0.28);
}

/* ---------- REMOVE STREAMLIT HEADER ---------- */

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu,
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;'>MR. X</h1>
<p style='text-align:center;color:rgba(255,255,255,0.7);margin-top:-10px;'>
Your private knowledge assistant
</p>
""", unsafe_allow_html=True)



@st.cache_resource
def load_assistant():
    return get_assistant()


try:
    assistant = load_assistant()
except Exception as e:
    st.error(f"Could not connect to Pinecone Assistant: {e}")
    st.stop()


# ---- Sidebar: upload + knowledge base view ----
with st.sidebar:
    st.subheader("Documents")
    uploaded_file = st.file_uploader("Add a note or PDF", type=["txt", "pdf", "md", "docx"])

    if uploaded_file is not None and st.button("Upload to Knowledge Base"):
        with st.spinner("Uploading..."):
            temp_path = f"./{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            try:
                upload_file(assistant, temp_path, metadata={"source": uploaded_file.name})
                st.success(f"'{uploaded_file.name}' uploaded! It may take a minute to finish processing.")
            except Exception as e:
                st.error(f"Upload failed: {e}")

    st.divider()
    st.header("📄 Files in Knowledge Base")
    try:
        files = list_files(assistant)

        if files:
            for f in files:

                st.text(f"• {f.name} ({f.status})")
        else:
            st.text("No files uploaded yet.")
    except Exception as e:
        st.warning(f"Could not load file list: {e}")

    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# ---- Chat history ----
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg.get("sources"):
            with st.expander("Sources"):
                for s in msg["sources"]:
                    st.text(f"📄 {s}")


# ---- Chat input ----
if prompt := st.chat_input("Ask something about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages[:-1]
                ]
                answer, sources = ask_question(assistant, prompt, chat_history=history)
                st.write(answer)
                if sources:
                    with st.expander("Sources"):
                        for s in sources:
                            st.text(f"📄 {s}")
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer, "sources": sources}
                )
            except Exception as e:
                error_msg = f"Something went wrong: {e}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})


                  
