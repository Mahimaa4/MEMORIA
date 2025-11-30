from dotenv import load_dotenv
import os
load_dotenv(override=True)

print("Loaded API key from .env 👉", os.environ.get("GEMINI_API_KEY")[:10] if os.environ.get("GEMINI_API_KEY") else None)

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# your modules
from modules.pdf_utils import process_pdf
from rag_engine import get_answer_from_pdf   # this will work after I fix rag_engine
from modules.qdrant_utils import setup_collection  # search_vectors removed here

app = Flask(__name__)
CORS(app)

# Embedding model dimension
EMBEDDING_DIM = 768  
setup_collection(vector_size=EMBEDDING_DIM)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process_pdf", methods=["POST"])
def upload_pdf():
    file = request.files.get("file")
    if not file:
        return jsonify({"status": "error", "msg": "No file uploaded"}), 400

    total = process_pdf(file.read(), chunk_size=500)
    return jsonify({"status": "success", "chunks_stored": total})


@app.route("/chat", methods=["POST"])
def chat():
    query = (request.json or {}).get("query", "").strip()
    if not query:
        return jsonify({"answer": "Enter a valid question"})

    response = get_answer_from_pdf(query, top_k=5)
    return jsonify({
    "answer": response["answer"],
    "sources": response["sources"]
})


if __name__ == "__main__":
    print("🚀 EDU-BOT running on http://127.0.0.1:5000")
    app.run(debug=True)
