# Setup

Proyecto FastAPI gestionado con [uv](https://docs.astral.sh/uv/). Basado en la documentación oficial de FastAPI (vía Context7).

## Requisitos

- Python >= 3.14
- uv

## Instalación

```bash
uv sync
```

Se creó originalmente con:

```bash
uv init --bare --name consult-ia-server
uv add "fastapi[standard]"   # incluye fastapi CLI, uvicorn, etc.
```

## Estructura

```
.
├── app
│   ├── __init__.py
│   └── main.py      # instancia `app` + /health
├── pyproject.toml
└── setup.md
```

Para crecer: agregar `app/routers/<recurso>.py` con `APIRouter()` y montarlo en `main.py` con `app.include_router(...)` ([Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications)).

## Ejecutar

Desarrollo (auto-reload):

```bash
uv run fastapi dev app/main.py
```

Producción:

```bash
uv run fastapi run app/main.py
```

- API: http://127.0.0.1:8000
- Docs interactivas (Swagger): http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Agregar dependencias

```bash
uv add <paquete>
```

## Variables de entorno

```bash
cp .env.example .env   # y completar DEEPSEEK_API_KEY
```

`.env` está en `.gitignore`: nunca se commitea. Solo `.env.example` (sin valores) va al repo.
