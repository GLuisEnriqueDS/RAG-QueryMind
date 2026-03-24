import numpy as np
import faiss
from difflib import get_close_matches, SequenceMatcher
from app.services.embedding_service import modelo_embeddings
from app.utils.text_utils import normalizar


def validar_entidad_por_similitud(entidad_llm, tipo_entidad, entidades_db, umbral=0.5):
    if entidad_llm in ["ninguno", ""]:
        return "ninguno", None, 0.0

    lista_lower = [e.lower() for e in entidades_db[tipo_entidad]]
    entidad_lower = entidad_llm.lower()

    matches = get_close_matches(entidad_lower, lista_lower, n=1, cutoff=umbral)

    if matches:
        idx = lista_lower.index(matches[0])
        entidad_valida = entidades_db[tipo_entidad][idx]
        nivel_confianza = SequenceMatcher(None, entidad_lower, matches[0]).ratio()
        return entidad_valida, entidad_valida, nivel_confianza

    if entidad_lower in lista_lower:
        idx = lista_lower.index(entidad_lower)
        entidad_valida = entidades_db[tipo_entidad][idx]
        return entidad_valida, entidad_valida, 1.0

    return "ninguno", None, 0.0


def buscar_similitud(pregunta, datos_busqueda, entidad, requiere_filtro):

    entidad = entidad.title()

    if entidad not in datos_busqueda:
        return 0, None

    bloque = datos_busqueda[entidad]

    embeddings = np.array(bloque["embeddings"]).astype("float32")
    ejemplos = bloque["ejemplos"]

    emb_usuario = modelo_embeddings.encode(
        [normalizar(pregunta)],
        normalize_embeddings=True
    ).astype("float32")

    indices_validos = []

    for i, e in enumerate(ejemplos):

        filtro_ejemplo = str(e["requiere_filtro"]).lower() == "true"

        if filtro_ejemplo != requiere_filtro:
            continue

    return similitud, ejemplo