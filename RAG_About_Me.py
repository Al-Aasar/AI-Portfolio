import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
CORS(app)


api_key = os.getenv("GOOGLE_API_KEY")


persist_directory = "./chroma_db"
embedding_model = FastEmbedEmbeddings()

if os.path.exists(persist_directory):
    vector_store = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embedding_model
    )
    print("✅ Database linked successfully from chroma_db folder.")
else:
    print("⚠️ Warning: chroma_db not found. Make sure to upload the folder.")

retriever = vector_store.as_retriever(search_kwargs={"k": 15})

model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.3
)

system_prompt = (
    "You are an expert technical interviewer and AI Assistant. "
    "Your task is to provide detailed information about Muhammad Al-Aasar's professional experience and technical implementation. "
    "You have access to two types of data: "
    "1. Muhammad's CV (for general experience and roles). "
    "2. Muhammad's actual Jupyter Notebooks and Python code (for technical logic and implementation). "
    "-------------------------------------------------------"
    "When asked about a project, look into the code chunks to explain HOW he built it, "
    "mentioning specific libraries like YOLO, Tesseract, Streamlit, or Scikit-learn if found in the context. "
    "If the answer is not in the context, say you don't know. "
    "---------------------------------------------------"
    "You are an expert technical interviewer... Respond in the same language as the user's question."
    "You are an expert technical interviewer. Answer based ONLY on Muhammad's CV and code. "
    "If the user asks in Arabic, respond in Arabic using the technical details found in the code. "
    "Muhammad Al-Aasar is equal 'محمد الأعصر' in Arabic. "
    "Context: {context}"
)


prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])


question_answer_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()
    user_input = data.get('text') 

    if not user_input:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = retrieval_chain.invoke({"input": user_input})
        return jsonify({
            "result": response["answer"],
            "message": "Success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


