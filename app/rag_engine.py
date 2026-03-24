from app.services.llm_service import analizar_pregunta
from app.services.embedding_service import cargar_datos_busqueda
from app.services.similarity_service import buscar_similitud, validar_entidad_por_similitud
from app.services.sql_service import construir_sql, ejecutar_sql, cargar_entidades
from app.services.memory_service import guardar_no_match
from app.services.text_processing_service import reemplazar_entidades_por_bd


def responder(pregunta_usuario):
    print("\nAnalizando intención...\n")

    analisis = analizar_pregunta(pregunta_usuario)

    entidades_db = cargar_entidades()

    entidades_originales = analisis.copy()

    match_agencia, _, conf_agencia = validar_entidad_por_similitud(analisis["agencia"], "agencias", entidades_db)
    analisis["agencia"] = match_agencia

    match_agente, _, conf_agente = validar_entidad_por_similitud(analisis["agente"], "agentes", entidades_db)
    analisis["agente"] = match_agente

    match_representante, _, conf_representante = validar_entidad_por_similitud(analisis["representante"], "representantes", entidades_db)
    analisis["representante"] = match_representante

    match_cliente, _, conf_cliente = validar_entidad_por_similitud(analisis["cliente"], "clientes", entidades_db)
    analisis["cliente"] = match_cliente

    if analisis is None:
        return {"error": "fallo analisis llm"}

    pregunta_normalizada = reemplazar_entidades_por_bd(
        pregunta_usuario,
        analisis,
        entidades_originales
    )

    datos_busqueda = cargar_datos_busqueda()

    requiere_filtro = (
        analisis["agencia"] != "ninguno"
        or analisis["agente"] != "ninguno"
        or analisis["representante"] != "ninguno"
        or analisis["cliente"] != "ninguno"
    )

    MAP_CATEGORIAS = {
        "agencia": "Agencia",
        "agente": "Agente",
        "representante": "Representante Comercial",
