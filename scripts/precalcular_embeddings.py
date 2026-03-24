import pickle
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import unicodedata

def normalizar(texto):
    if not texto:
        return ""
    texto = texto.strip()                       # quita espacios al inicio/final
    texto = unicodedata.normalize("NFKC", texto)  # normaliza acentos y caracteres especiales
    texto = texto.replace("\u200b", "")        # quita caracteres invisibles comunes
    texto = texto.replace("\xa0", "")          # quita espacios no-break
    return texto.lower()

# Modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Cargar el nuevo examples.json
with open(r"C:\Users\Enrique Guerra\Documents\Claro Insurance\Proyectos\RAG Database\examplesV2.json", "r", encoding="utf-8") as f:
    ejemplos = json.load(f)

# Agrupar por ENTIDAD (antes categoria)
por_entidad = {}
for i, e in enumerate(ejemplos):
    por_entidad.setdefault(e["entidad"], []).append((i, e))

data = {}

for entidad, items in por_entidad.items():
    # Normalizamos todas las preguntas
    preguntas = [normalizar(e["pregunta"]) for _, e in items]
    embeds = modelo.encode(preguntas, normalize_embeddings=True)

    embeds = np.array(embeds).astype("float32")
    dim = embeds.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(embeds)

    data[entidad] = {
        "indices_globales": [i for i, _ in items],
        "ejemplos": [e for _, e in items],
        "embeddings": embeds,
        "index": index,
        "dimension": dim
    }

# Guardar embeddings para búsquedas rápidas
with open("datos_busquedaV2.pkl", "wb") as f:
    pickle.dump(data, f)

print("Embeddings generados y almacenados en 'datos_busqueda.pkl'.")