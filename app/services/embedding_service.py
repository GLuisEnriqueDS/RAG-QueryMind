import pickle
from sentence_transformers import SentenceTransformer
from app.config import EMBEDDINGS_PATH

modelo_embeddings = SentenceTransformer("all-MiniLM-L6-v2")

def cargar_datos_busqueda():
    with open(EMBEDDINGS_PATH, "rb") as f:
        datos = pickle.load(f)
    return datos