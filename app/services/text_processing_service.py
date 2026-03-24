import re


def reemplazar_entidades_por_bd(pregunta, analisis, entidades_originales):

    pregunta_norm = pregunta

    if analisis["agencia"] not in ["ninguno",""]:
        original = entidades_originales.get("agencia")
        if original:
            patron = re.compile(re.escape(original), re.IGNORECASE)
            pregunta_norm = patron.sub(analisis["agencia"], pregunta_norm)

    if analisis["agente"] not in ["ninguno",""]:
        original = entidades_originales.get("agente")
        if original:
            patron = re.compile(re.escape(original), re.IGNORECASE)
            pregunta_norm = patron.sub(analisis["agente"], pregunta_norm)

    if analisis["representante"] not in ["ninguno",""]:
        original = entidades_originales.get("representante")
        if original:
            patron = re.compile(re.escape(original), re.IGNORECASE)
            pregunta_norm = patron.sub(analisis["representante"], pregunta_norm)

    if analisis["cliente"] not in ["ninguno",""]:
        original = entidades_originales.get("cliente")
        if original:
            patron = re.compile(re.escape(original), re.IGNORECASE)
            pregunta_norm = patron.sub(analisis["cliente"], pregunta_norm)

    return pregunta_norm