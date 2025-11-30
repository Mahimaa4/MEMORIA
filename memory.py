import sqlite3
import uuid

# =========================
# 🔥 MEMORY DATABASE MODE
# Change ":memory:" → "memory.db" to persist across restarts
# =========================
DB = "memory.db"   # ← if you want RAM only, change back to ":memory:"


# ---------------- INIT DB -----------------
def init_memory_db():
    global conn
    conn = sqlite3.connect(DB, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            session_id TEXT,
            role TEXT,
            content TEXT
        )
    """)
    conn.commit()
    print("🧠 Chat Memory initialized:", DB)


# ---------------- SAVE MESSAGE -----------------
def save_chat_message(session_id: str, role: str, content: str):
    conn.execute("INSERT INTO messages VALUES (?,?,?)", (session_id, role, content))
    conn.commit()


# ---------------- FETCH FULL CHAT HISTORY -----------------
def get_chat_history(session_id: str):
    """
    Returns chat history in proper Gemini conversation format:
    [
      {"role": "user", "parts": ["hi"]},
      {"role": "model", "parts": ["hello"]}
    ]
    """

    cursor = conn.execute(
        "SELECT role, content FROM messages WHERE session_id=? ORDER BY ROWID ASC",
        (session_id,)
    )

    history = [{"role": r, "parts": [c]} for r, c in cursor.fetchall()]

    # 🔥 limit history to avoid long prompt lag
    return history[-20:]   # last 20 messages only (safe)
    

# ---------------- NEW — GENERATE/RETURN SESSION ID -----------------
def new_session() -> str:
    """Create a new unique session id when chat starts."""
    return str(uuid.uuid4())
