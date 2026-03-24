Sistema RAG que combina SQLite + embeddings + FAISS + Groq para responder consultas en lenguaje natural sobre una base de datos comercial.

1.Instalación
cd rag_database
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2.Configuración
Crear archivo .env
3.Ejecución
python -m app.main
4.Uso
Al Ejecutar aparecerá:
Pregunta:
Escribe tu consulta y el sistema responderá automáticamente.
