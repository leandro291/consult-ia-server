from fastapi import APIRouter
from app.schemas.prompt_schema import Prompt
from app.services.prompt_service import transcribir_consulta

router = APIRouter(prefix="/consulta")

@router.post("/prompt")
def obtener_consulta(data: Prompt):
    return transcribir_consulta(data.texto)
