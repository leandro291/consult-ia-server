from fastapi import FastAPI
from app.routes.prompt_routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="consult-ia-server")
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:8000"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"]
)
