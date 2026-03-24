import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "db", "ventas.db")
EMBEDDINGS_PATH = os.path.join(BASE_DIR, "data", "embeddings", "datos_busqueda.pkl")
EXAMPLES_PATH = os.path.join(BASE_DIR, "data", "examples", "examples.json")
NO_MATCH_DB = os.path.join(BASE_DIR, "data", "db", "preguntas_no_match.db")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")