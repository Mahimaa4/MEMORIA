# 🎓MEMORIA — PDF Knowledge Chat (RAG)

Memoria is an AI learning assistant that lets users upload PDFs and ask questions based on the content inside them using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 📄 **Upload PDF**
* 🔍 **Automatic text chunking + embeddings**
* 🧠 **Semantic search**
* 🤖 **AI-generated answers from PDF context**
* 📚 Powered by **Vector DB + LLM + Embedding model**

---

## 🏗️ Tech Stack

| Purpose              | Tool          |
| -------------------- | ------------- |
| Embeddings           | Google AI     |
| Vector Database      | Qdrant        |
| PDF Reader           | PyMuPDF       |
| Backend API          | Flask         |
| Vector Search Client | Qdrant Client |
| Frontend             | HTML, CSS, JS |

---

## 📁 Project Structure

```
EDU-BOT/
│── app.py
│── rag_engine.py
│── embeddings.py
│── requirements.txt
│── modules/
│    ├── pdf_utils.py
│    ├── qdrant_utils.py
│    └── chat_llm.py
│── templates/
│    └── index.html
│── static/
│    ├── style.css
│    └── script.js
```

---

## ⚙️ Setup & Installation

1️⃣ Clone the repository
2️⃣ Create & activate virtual environment (Python 3.10+)

```
python -m venv venv
venv\Scripts\activate  (Windows)
source venv/bin/activate  (Mac/Linux)
```

3️⃣ Install dependencies

```
pip install -r requirements.txt
```

4️⃣ Add your API key as environment variable or `.env`

```
GEMINI_API_KEY=your_api_key_here
```

5️⃣ Run the app

```
python app.py
```

The bot will start on **localhost**

---

## 💬 API Usage

### Upload PDF

Endpoint:

```
POST /process_pdf
```

### Chat with EDU-BOT

Endpoint:

```
POST /chat
```

Example request:

```json
{
  "message": "What is pollution?"
}
```

---

## 🧠 How It Works (RAG Flow)

1. PDF text is extracted using Google AI embeddings
2. Text is split into chunks
3. Chunks are converted into vector embeddings using Qdrant semantic search
4. User questions are embedded and matched against stored vectors
5. Retrieved chunks are sent as context to Qdrant Client

---

## 🔐 Important Notes

* Do **NOT push your real API key publicly**
* Add a `.gitignore` file including:

  ```
  .env
  venv/
  __pycache__/
  ```

---

## 📌 Requirements

See the auto-generated `requirements.txt` file in the repo.

---

## 🌟 Future Enhancements

* Support for more formats (DOCX, PPTX)
* History-based chat memory
* Improved ranking + hybrid search

---

### ⭐ If you found this helpful, don’t forget to give the repo a star on GitHub! 😍


