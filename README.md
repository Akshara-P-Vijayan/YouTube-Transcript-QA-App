# 🎥 YouTube Transcript QA Chatbot

Chat with any YouTube video by simply pasting the link! This app fetches the video transcript and lets you ask questions using a Retrieval-Augmented Generation (RAG) pipeline powered by LangChain + Hugging Face.

👉 **[Live Demo](https://youtube-transcript-app-u.streamlit.app/)

---

## 🚀 Features
- 🔗 Input any YouTube video link
- 📜 Auto-fetch and chunk transcript
- 🧠 Ask questions about the video content
- 🗂️ Vector search with FAISS
- 🤖 LLM-based answers (Falcon-7B-Instruct)

---

## 🧰 Tech Stack
- [Streamlit](https://streamlit.io/) – for frontend
- [LangChain](https://www.langchain.com/) – for RAG pipeline
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) – to get video captions
- [sentence-transformers](https://www.sbert.net/) – for embeddings
- [FAISS](https://github.com/facebookresearch/faiss) – vector DB
- [Transformers](https://huggingface.co/transformers/) – Falcon-7B-Instruct LLM

---

## 📦 Installation

```bash
# 1. Clone the repo
https://github.com/Akshara-P-Vijayan/youtube-transcript-rag.git
cd youtube-transcript-rag

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run locally
streamlit run app.py
```

---

## 📁 Folder Structure

```
youtube-transcript-rag/
├── app.py                # Streamlit app logic
├── requirements.txt      # All dependencies
└── README.md             # You're reading it!
```

---

## 🧠 How It Works
1. Extracts transcript using `youtube-transcript-api`
2. Splits into chunks via `RecursiveCharacterTextSplitter`
3. Embeds chunks with `sentence-transformers`
4. Stores in FAISS vector DB
5. On query → retrieves top relevant chunks → answers via Falcon-7B-Instruct

---

## 📤 Deploy on Streamlit Cloud
1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and deploy `app.py`

---

## 🙋‍♀️ Author
**Akshara P** – [GitHub](https://github.com/Akshara-P-Vijayan) | [LinkedIn](https://linkedin.com/in/akshara-p-b89414244)

---



## 💡 Future Ideas
- Summarize the video content
- Save and export chat history
- Multi-video transcript search
