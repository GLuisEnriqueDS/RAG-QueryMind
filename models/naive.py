import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import re

# Datos de entrenamiento
preguntas = [
    "¿Cuáles son los nombres de todas las agencias registradas?",
    "¿Qué agentes trabajan en la Agencia Central?",
    "¿Cuántos agentes tiene cada agencia?",
    "¿Qué representantes comerciales guían a más de 2 agentes?",
    "¿Cuál es el agente que ha realizado más ventas?",
    "¿Cuál es el monto total de ventas por cada agencia?",
    "¿Qué clientes han realizado compras superiores a $2000?",
    "¿Qué productos tienen un precio mayor al promedio?",
    "¿Cuántas ventas ha realizado cada agente en el año 2023?",
    "¿Qué representante comercial tiene los agentes con mayores ventas?",
    "¿Qué agencia tiene la mayor cantidad de ventas?",
    "¿Cuáles son los 5 productos más vendidos?",
    "¿Qué agentes no han realizado ninguna venta?",
    "¿Cuál es el promedio de ventas por agente en cada agencia?",
    "¿Qué cliente ha gastado más dinero en total?",
    "¿Cuántos agentes tiene cada representante comercial?",
    "¿Cuál es el producto más caro de cada categoría?",
    "¿Qué agencia tiene los agentes con mayor antigüedad?",
    "¿Qué representante tiene el agente más joven?",
    "¿Cuál es el mes del año con más ventas?"
]

categorias = [
    "Agencia", "Agente", "Agencia", "Representante Comercial", "Agente",
    "Agencia", "General", "General", "Agente", "Representante Comercial",
    "Agencia", "General", "Agente", "Agencia", "General",
    "Representante Comercial", "General", "Agencia", "Representante Comercial", "General"
]

# Entrenar modelo
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(preguntas, categorias)
joblib.dump(modelo, "clasificador_naive.pkl")

def clasificar_inteligente(pregunta):
    modelo = joblib.load("clasificador_naive.pkl")
    
    pregunta_lower = pregunta.lower()
    
    # Prioridad 1: Palabras clave específicas
    if "representante" in pregunta_lower or "comercial" in pregunta_lower:
        if "agente" not in pregunta_lower or "representante" in pregunta_lower:
            return "Representante Comercial"
    
    if "agencia" in pregunta_lower and "agente" not in pregunta_lower:
        return "Agencia"
    
    if "agente" in pregunta_lower and "agencia" not in pregunta_lower:
        return "Agente"
    
    # Prioridad 2: Si menciona ambos, usar el modelo
    if "agencia" in pregunta_lower and "agente" in pregunta_lower:
        return modelo.predict([pregunta])[0]
    
    # Prioridad 3: Para todo lo demás, usar el modelo
    return modelo.predict([pregunta])[0]

# Prueba
preguntas_prueba = [
    "¿Qué agencia tiene más vendedores?",
    "¿Quiénes son los representantes comerciales?",
    "¿Cuánto vendió el agente Pérez?",
    "¿Qué productos están en oferta?",
    "¿Qué agencia tiene los mejores agentes?"
]

print("🔮 Resultados:")
for p in preguntas_prueba:
    print(f"'{p}' → {clasificar_inteligente(p)}")