import json
import re
from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def construir_prompt(pregunta):
    prompt = f"""
Eres un analizador semántico para una base de datos comercial.

Debes identificar:

1. categoria (siempre)
2. sub_categoria
3. 1 entidade específica mencionada (si aplica)

IMPORTANTE:

La categoria se refiere al tipo de información solicitada, incluso si
no se menciona una entidad específica.

Ejemplos:

Pregunta: ¿Cuáles agencias existen?
categoria: agencia
agencia: ninguno

Pregunta: ¿Cuánto vendió la Agencia Central?
categoria: agencia
agencia: agencia central

Pregunta: ¿Cuánto vendió la Oficina Central? 
categoria: agencia
agencia: agencia central

Pregunta: ¿Qué agentes pertenecen al representante Carlos Rodriguez?
categoria: agente
representante: carlos rodriguez

Si no se menciona una entidad específica usa "ninguno".
Cuando el usuario use sinónimos como "oficina", "sucursal" o "local" 
para referirse a una agencia, debes devolver el nombre completo 
con "agencia" en lugar del sinónimo.

CATEGORIAS:
agencia
agente
representante
cliente

SUB_CATEGORIAS:
ventas
master

Responde SOLO JSON.

FORMATO:

{{
"categoria":"",
"sub_categoria":"",
"agencia":"",
"agente":"",
"representante":"",
"cliente":""
}}

PREGUNTA:
{pregunta}
"""


def limpiar_json_llm(texto):

    if texto is None:
        return None

    texto = texto.strip()

    texto = texto.replace("```json", "")
    texto = texto.replace("```", "")

    match = re.search(r"\{.*\}", texto, re.DOTALL)

    if match:
        texto = match.group()

    try:
        return json.loads(texto)
    except:
        return None


def limpiar_entidades_llm(analisis):

    for k in ["agencia","agente","representante","cliente"]:

        if analisis.get(k) in ["", None]:
            analisis[k] = "ninguno"

    return analisis


def analizar_pregunta(pregunta):
    prompt = construir_prompt(pregunta)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200
    )

    salida = response.choices[0].message.content
    resultado = limpiar_json_llm(salida)

    if resultado is None:
        return None

    resultado = limpiar_entidades_llm(resultado)
    return resultado