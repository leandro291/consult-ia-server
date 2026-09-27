from fastapi import APIRouter
from app.schemas.prompt_schema import Prompt
from app.services.prompt_service import transcribir_consulta

router = APIRouter(prefix="/consulta")

@router.post("/prompt")
async def obtener_consulta(data: Prompt):
    return await transcribir_consulta(data.texto)
