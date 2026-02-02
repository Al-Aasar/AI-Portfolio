# 🤖 AI-Powered Professional Portfolio (RAG System)

This project is an **End-to-End RAG (Retrieval-Augmented Generation)** application designed to act as an AI Assistant for **Muhammad Al-Aasar**. It combines a Flask-based backend with a modern Chat UI to provide detailed insights into Muhammad's professional experience and technical code implementation.

## 🚀 Features
* **Semantic Search**: Uses `FastEmbed` and `ChromaDB` to retrieve relevant technical logic from 12+ Jupyter Notebooks and CV.
* **Context-Aware Responses**: Powered by `Gemini 2.5 Flash` to answer questions based strictly on the provided technical context.
* **Modern Chat UI**: A responsive web interface featuring a clean design and integrated profile visuals.
* **Bilingual Support**: Capable of understanding and responding in both Arabic and English while maintaining technical accuracy.

## 🛠️ Tech Stack
* **LLM**: Google Gemini 1.5 Flash.
* **Frameworks**: LangChain, Flask.
* **Vector Database**: ChromaDB.
* **Embeddings**: FastEmbed (Lightweight & Fast).
* **Frontend**: HTML5, CSS3, JavaScript.

## 📂 Project Structure
* `RAG_About_Me.py`: The core Flask API managing retrieval and generation.
* `chroma_db/`: Pre-built vector store containing embeddings of Muhammad's projects.
* `front.html`: Interactive Chat Interface.
* `requirements.txt`: Python dependencies for cloud deployment.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your Google API Key: `os.environ["GOOGLE_API_KEY"] = "your_key"`.
4. Run the server: `python RAG_About_Me.py`.
5. Open `front.html` in your browser.

## 🌐 Deployment
This system is optimized for deployment on **Render** (Backend) and static hosting for the Frontend.
