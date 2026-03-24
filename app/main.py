from app.rag_engine import responder

if __name__ == "__main__":
    while True:
        pregunta = input("Pregunta: ")
        respuesta = responder(pregunta)
        print(respuesta)