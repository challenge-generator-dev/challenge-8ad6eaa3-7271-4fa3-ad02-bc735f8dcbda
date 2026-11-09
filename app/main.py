"""
Entry point de la aplicación FastAPI.
Configura la instancia de la app, incluye los routers y maneja la inicialización.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import Settings
from app.presentation.api import router as api_router
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    """Crea y configura la instancia de FastAPI."""
    app = FastAPI(
        title="Bank Balances API",
        description="API para consulta asincrónica de saldos bancarios",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    # Configuración CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Incluir routers
    app.include_router(api_router, prefix="/api/v1")

    # Eventos de inicio y apagado
    @app.on_event("startup")
    async def startup_event():
        logger.info("Iniciando aplicación")
        settings = Settings()
        logger.info(f"Configuración cargada: {settings}")

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Apagando aplicación")

    return app

app = create_app()