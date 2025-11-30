import google.generativeai as genai
import os
from typing import List, Dict, Any

# ================= INIT GEMINI ===================
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ ERROR: GEMINI_API_KEY not set in .env")
else:
    genai.configure(api_key=API_KEY)
    print("✅ Gemini API connected")

MODEL_NAME = "gemini-1.5-flash"   # stable + fast model

model = genai.GenerativeModel(model_name=MODEL_NAME)

# =================================================

def ask_ai(prompt: str, history: List[Dict[str, Any]] = None) -> str:
    """Generate response from Gemini with optional conversation history."""

    if history is None:
        history = []

    try:
        chat = model.start_chat(history=history)
        response = chat.send_message(prompt)

        return response.text.strip()

    except Exception as e:
        print("❌ Gemini chat error:", e)
        return "AI generation failed. Please try again."
