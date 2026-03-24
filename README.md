# Sistema RAG con SQLite, FAISS y Groq

Sistema de **Recuperación Aumentada por Generación (RAG)** que combina:

- **SQLite** para almacenamiento estructurado  
- **Embeddings** para representación vectorial  
- **FAISS** para búsqueda de similitud  
- **Groq** para generación de respuestas en lenguaje natural  

Permite realizar consultas en lenguaje natural sobre una base de datos comercial.

---

##  Instalación

1. Clona el repositorio y accede a la carpeta del proyecto:
   ```bash
   cd rag_database
2. Crea y activa un entorno virtual:
  python -m venv venv
  venv\Scripts\activate
3. Instala las dependencias:
  pip install -r requirements.txt
4.  Configuración
 Crea un archivo .env en la raíz del proyecto con las siguientes variables
5. Ejecución
  python -m app.main

##  Estructura del proyecto

```bash
rag_database/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── embeddings.py
│   ├── retrieval.py
│   └── ...
├── data/             
├── requirements.txt
├── .env
└── README.md
