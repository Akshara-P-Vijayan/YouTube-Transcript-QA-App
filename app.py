import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import re

st.set_page_config(page_title="🎥 YouTube Transcript Chatbot", page_icon="🧠")
st.title("🎥 Chat with any YouTube Video")

def extract_video_id(url):
    pattern = r"(?:v=|youtu.be/)([\w-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([chunk['text'] for chunk in transcript])
    return text

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents([text])

def create_vector_db(chunks):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embedder)

def get_llm():
    pipe = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", tokenizer="tiiuae/falcon-7b-instruct", max_new_tokens=200, do_sample=True)
    return HuggingFacePipeline(pipeline=pipe)

def create_qa_chain(db):
    llm = get_llm()
    retriever = db.as_retriever(search_type="similarity", k=3)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

# --- Streamlit UI ---
youtube_url = st.text_input("🔗 Paste YouTube Video URL")
if youtube_url:
    try:
        with st.spinner("Fetching transcript and preparing chatbot..."):
            vid = extract_video_id(youtube_url)
            transcript = fetch_transcript(vid)
            st.success("Transcript fetched successfully!")

            chunks = chunk_text(transcript)
            db = create_vector_db(chunks)
            qa = create_qa_chain(db)

        query = st.text_input("💬 Ask a question about the video")
        if query:
            with st.spinner("Generating answer..."):
                response = qa.invoke(query)
                st.markdown(f"**🤖 Answer:** {response.strip()}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
