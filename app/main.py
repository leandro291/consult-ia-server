from fastapi import FastAPI

app = FastAPI(title="consult-ia-server")


@app.get("/health")
def health():
    return {"saludo": "Hola esta es la primera etapa de mi proyecto"}
