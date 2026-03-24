import sqlite3
from app.config import NO_MATCH_DB


def guardar_no_match(pregunta, similitud):

    conn = sqlite3.connect(NO_MATCH_DB)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS preguntas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        similitud REAL
    )
    """)

    cur.execute(
        "INSERT INTO preguntas (pregunta, similitud) VALUES (?, ?)",
        (pregunta, similitud)
    )

    conn.commit()

    conn.close()