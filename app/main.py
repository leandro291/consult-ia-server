from fastapi import FastAPI
from app.routes.prompt_routes import router

app = FastAPI(title="consult-ia-server")
app.include_router(router)