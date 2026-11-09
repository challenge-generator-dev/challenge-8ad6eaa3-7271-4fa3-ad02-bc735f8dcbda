# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener el proyecto completo y arrancable. Guarda los archivos que te devuelva en la
carpeta del repo, respetando exactamente las rutas.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced

### Brecha de conocimiento
Maneja operaciones de I/O sin bloquear el event loop y modela los errores del dominio de forma explicita

### Misión / candidato
Exponer la consulta de saldos consolidando dos fuentes

### Datos adicionales
Candidato con 3 años en Python

### Reto
- Tema: Servicios asincronicos con FastAPI
- Seniority: advanced-l2
- Tipo: practical
- Título: Implementación de consulta de saldos asincrónica
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Configuración inicial y exposición de la API — objetivo: Configurar el entorno de desarrollo y exponer una API básica para consultar saldos. — entregable (NO resolver): API funcional con una ruta para consultar saldos.
- Fase 2: Integración asincrónica con las fuentes de saldos — objetivo: Integrar la API con las fuentes de saldos de manera asincrónica. — entregable (NO resolver): API que consulta saldos de dos fuentes de manera asincrónica y maneja errores del dominio.
- Fase 3: Consolidación y exposición de los saldos — objetivo: Consolidar los saldos de las dos cuentas y exponerlos a través de la API. — entregable (NO resolver): API que consolida y expone los saldos de dos cuentas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (entrega de archivos).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Entrega de archivos
Entregá cada archivo con su ruta completa, respetando exactamente la estructura de rutas
indicada por los marcadores: un bloque por archivo, precedido por su ruta. No generes ZIPs
ni archivos adjuntos.
La entrega debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: Entregá los archivos completos al finalizar. No preguntes si el usuario
quiere recibirlos. Simplemente entregalos; No debes desplegar en el chat el resumen de lo que arreglaste, solo entregá los archivos.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del último archivo entregado
No preguntes si el usuario quiere los archivos: simplemente entregalos siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "bank-balances-api"
version = "0.1.0"
description = "API para consulta asincrónica de saldos bancarios"
authors = ["Pragma Engineering <engineering@pragma.com.co>"]
license = "MIT"
readme = "README.md"
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.13"
fastapi = "0.115.0"
uvicorn = "0.30.6"
pydantic = "2.9.2"
httpx = "0.27.2"
python-dotenv = "1.0.1"

[tool.poetry.group.dev.dependencies]
pytest = "8.3.2"
pytest-asyncio = "0.24.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
asyncio_mode = "auto"

// === ARCHIVO: app/main.py ===
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

// === ARCHIVO: app/config/settings.py ===
"""
Configuración centralizada de la aplicación.
Lee variables de entorno y proporciona valores por defecto.
"""

from pydantic_settings import BaseSettings
from pydantic import Field, AnyHttpUrl
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Configuración de la API
    app_name: str = Field(default="Bank Balances API", description="Nombre de la aplicación")
    app_version: str = Field(default="1.0.0", description="Versión de la aplicación")
    api_prefix: str = Field(default="/api/v1", description="Prefijo para los endpoints de API")
    
    # Configuración de servicios externos
    current_account_service_url: AnyHttpUrl = Field(
        default="http://localhost:8001/api/current",
        description="URL del servicio de Cuentas Corrientes"
    )
    savings_account_service_url: AnyHttpUrl = Field(
        default="http://localhost:8002/api/savings",
        description="URL del servicio de Cuentas de Ahorro"
    )
    
    # Timeouts para llamadas externas
    external_service_timeout: int = Field(
        default=5,
        description="Timeout en segundos para llamadas a servicios externos"
    )
    
    # Configuración de logging
    log_level: str = Field(default="INFO", description="Nivel de logging")
    
    # Configuración de host y puerto
    host: str = Field(default="0.0.0.0", description="Host donde corre la aplicación")
    port: int = Field(default=8000, description="Puerto donde corre la aplicación")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def __str__(self) -> str:
        return (
            f"Settings(app_name='{self.app_name}', "
            f"app_version='{self.app_version}', "
            f"api_prefix='{self.api_prefix}', "
            f"current_account_service_url='{self.current_account_service_url}', "
            f"savings_account_service_url='{self.savings_account_service_url}', "
            f"external_service_timeout={self.external_service_timeout}, "
            f"log_level='{self.log_level}', "
            f"host='{self.host}', "
            f"port={self.port}')"
        )

    def to_dict(self) -> dict:
        """Convierte la configuración a un diccionario."""
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "api_prefix": self.api_prefix,
            "current_account_service_url": str(self.current_account_service_url),
            "savings_account_service_url": str(self.savings_account_service_url),
            "external_service_timeout": self.external_service_timeout,
            "log_level": self.log_level,
            "host": self.host,
            "port": self.port,
        }


# Instancia global de configuración
_settings_instance: Optional[Settings] = None


def get_settings() -> Settings:
    """Obtiene la instancia singleton de configuración.
    
    Utiliza un patrón singleton para evitar crear múltiples instancias
    de configuración durante el ciclo de vida de la aplicación.
    
    Returns:
        Instancia de Settings configurada.
    """
    global _settings_instance
    
    if _settings_instance is None:
        _settings_instance = Settings()
        
    return _settings_instance


def reset_settings() -> None:
    """Reinicia la instancia de configuración.
    
    Útil para testing y para permitir recargar configuración.
    """
    global _settings_instance
    _settings_instance = None

// === ARCHIVO: app/domain/models.py ===
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class AccountType(str, Enum):
    """Tipos de cuentas soportados por el dominio."""
    CURRENT = "current_account"
    SAVINGS = "savings_account"

class AccountBalance(BaseModel):
    """Modelo de dominio que representa el saldo de una cuenta."""
    account_id: str = Field(..., description="Identificador único de la cuenta")
    account_type: AccountType = Field(..., description="Tipo de cuenta")
    balance: float = Field(..., description="Saldo actual de la cuenta")
    last_updated: datetime = Field(default_factory=datetime.now, description="Fecha de última actualización del saldo")
    is_available: bool = Field(default=True, description="Indica si el saldo está disponible para consulta")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "account_id": "12345678",
                "account_type": "current_account",
                "balance": 1500.75,
                "last_updated": "2024-05-20T10:00:00",
                "is_available": True
            }
        }

class ConsolidatedBalanceResponse(BaseModel):
    """Modelo de respuesta para la consulta consolidada de saldos."""
    account_id: str = Field(..., description="Identificador único de la cuenta")
    current_account_balance: Optional[float] = Field(None, description="Saldo de la cuenta corriente")
    savings_account_balance: Optional[float] = Field(None, description="Saldo de la cuenta de ahorro")
    consolidated_balance: float = Field(..., description="Saldo consolidado de ambas cuentas")
    status: str = Field(..., description="Estado de la consulta")
    details: Optional[dict] = Field(None, description="Detalles adicionales de la consulta")

    class Config:
        json_schema_extra = {
            "example": {
                "account_id": "12345678",
                "current_account_balance": 1500.75,
                "savings_account_balance": 3200.50,
                "consolidated_balance": 4701.25,
                "status": "success",
                "details": {"last_updated": "2024-05-20T10:00:00"}
            }
        }

class AccountBalanceUnavailableError(Exception):
    """Excepción lanzada cuando el saldo de una cuenta no está disponible."""
    def __init__(self, account_id: str, account_type: AccountType, message: Optional[str] = None):
        self.account_id = account_id
        self.account_type = account_type
        self.message = message or f"Saldo no disponible para la cuenta {account_id} de tipo {account_type.value}"
        super().__init__(self.message)

class ExternalServiceError(Exception):
    """Excepción lanzada cuando ocurre un error en la comunicación con un servicio externo."""
    def __init__(self, service_name: str, message: Optional[str] = None):
        self.service_name = service_name
        self.message = message or f"Error en el servicio externo {service_name}"
        super().__init__(self.message)

// === ARCHIVO: app/__init__.py ===
"""Paquete principal de la aplicación de consulta de saldos bancarios.

Este paquete contiene la estructura de la aplicación siguiendo
una arquitectura hexagonal con separación clara de capas.
"""

__version__ = "0.1.0"
__author__ = "Pragma Engineering <engineering@pragma.com.co>"

from app.domain.models import (
    AccountType,
    AccountBalance,
    ConsolidatedBalanceResponse,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)

__all__ = [
    "AccountType",
    "AccountBalance",
    "ConsolidatedBalanceResponse",
    "AccountBalanceUnavailableError",
    "ExternalServiceError",
]

// === ARCHIVO: app/application/services.py ===
"""Servicios de aplicación que orquestan los casos de uso del dominio.

Contiene la lógica de negocio que coordina la consulta de saldos
desde múltiples fuentes externas de manera asincrónica.
"""

import logging
from typing import Optional

from app.domain.models import (
    AccountType,
    AccountBalance,
    ConsolidatedBalanceResponse,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)
from app.infrastructure.repositories import AccountRepository
from app.infrastructure.external_services import (
    CurrentAccountService,
    SavingsAccountService,
    ServiceUnavailableError,
)

logger = logging.getLogger(__name__)


class BalanceQueryService:
    """Servicio que orquesta la consulta de saldos consolidados.
    
    Coordina la obtención de saldos de múltiples fuentes externas
    de manera asincrónica y maneja los errores del dominio.
    """
    
    def __init__(
        self,
        current_account_service: CurrentAccountService,
        savings_account_service: SavingsAccountService,
        account_repository: AccountRepository,
    ) -> None:
        self._current_account_service = current_account_service
        self._savings_account_service = savings_account_service
        self._account_repository = account_repository
        logger.info(
            "BalanceQueryService inicializado con servicios externos"
        )
    
    async def get_consolidated_balance(
        self,
        account_id: str,
        include_details: bool = False,
    ) -> ConsolidatedBalanceResponse:
        """Obtiene el saldo consolidado de una cuenta.
        
        Consulta simultáneamente los saldos de cuenta corriente y cuenta de ahorro,
        luego los consolida en un solo resultado.
        
        Args:
            account_id: Identificador único de la cuenta principal.
            include_details: Indica si se deben incluir detalles adicionales.
        
        Returns:
            ConsolidatedBalanceResponse con los saldos consolidados.
        
        Raises:
            ValueError: Si el account_id es inválido o está vacío.
            AccountBalanceUnavailableError: Si no se puede obtener el saldo de alguna cuenta.
            ExternalServiceError: Si hay un error de comunicación con los servicios externos.
        """
        if not account_id or not account_id.strip():
            logger.error(f"account_id inválido proporcionado: {account_id}")
            raise ValueError("El identificador de cuenta no puede estar vacío")
        
        account_id = account_id.strip()
        logger.info(
            f"Iniciando consulta de saldo consolidado para cuenta: {account_id}"
        )
        
        # Validar que la cuenta existe en nuestro sistema
        account_exists = await self._account_repository.account_exists(account_id)
        if not account_exists:
            logger.warning(f"Cuenta no encontrada: {account_id}")
            raise AccountBalanceUnavailableError(
                account_id=account_id,
                account_type=AccountType.CURRENT,
                message="La cuenta no existe en el sistema"
            )
        
        # Consultar saldos de ambas fuentes de manera concurrente
        try:
            current_balance, savings_balance = await self._fetch_both_balances(
                account_id
            )
        except ServiceUnavailableError as e:
            logger.error(
                f"Error de servicio externo al consultar saldos: {e.message}"
            )
            raise ExternalServiceError(
                service_name=e.service_name,
                message=e.message
            ) from e
        
        # Calcular saldo consolidado
        consolidated = current_balance.amount + savings_balance.amount
        
        # Determinar estado general
        status = self._determine_status(current_balance, savings_balance)
        
        logger.info(
            f"Saldos consolidados para {account_id}: "
            f"corriente={current_balance.amount}, "
            f"ahorro={savings_balance.amount}, total={consolidated}"
        )
        
        return ConsolidatedBalanceResponse(
            account_id=account_id,
            current_account_balance=current_balance.amount,
            savings_account_balance=savings_balance.amount,
            consolidated_balance=consolidated,
            status=status,
        )
    
    async def _fetch_both_balances(
        self,
        account_id: str,
    ) -> tuple[AccountBalance, AccountBalance]:
        """Consulta ambos saldos de manera concurrente.
        
        Utiliza asyncio.gather para ejecutar ambas consultas en paralelo,
        maximizando el rendimiento del sistema.
        
        Args:
            account_id: Identificador de la cuenta.
        
        Returns:
            Tupla con (saldo_cuenta_corriente, saldo_cuenta_ahorro).
        
        Raises:
            AccountBalanceUnavailableError: Si alguna consulta falla.
        """
        import asyncio
        
        try:
            current_task = self._current_account_service.get_balance(account_id)
            savings_task = self._savings_account_service.get_balance(account_id)
            
            results = await asyncio.gather(
                current_task,
                savings_task,
                return_exceptions=True,
            )
            
            current_result = results[0]
            savings_result = results[1]
            
            # Verificar si alguna consulta lanzó excepción
            if isinstance(current_result, Exception):
                logger.error(
                    f"Error al obtener saldo de cuenta corriente: {current_result}"
                )
                raise AccountBalanceUnavailableError(
                    account_id=account_id,
                    account_type=AccountType.CURRENT,
                    message=str(current_result)
                )
            
            if isinstance(savings_result, Exception):
                logger.error(
                    f"Error al obtener saldo de cuenta de ahorro: {savings_result}"
                )
                raise AccountBalanceUnavailableError(
                    account_id=account_id,
                    account_type=AccountType.SAVINGS,
                    message=str(savings_result)
                )
            
            return current_result, savings_result
            
        except asyncio.CancelledError:
            logger.warning("Consulta de saldos cancelada")
            raise AccountBalanceUnavailableError(
                account_id=account_id,
                account_type=AccountType.CURRENT,
                message="La consulta fue cancelada"
            )
    
    def _determine_status(
        self,
        current_balance: AccountBalance,
        savings_balance: AccountBalance,
    ) -> str:
        """Determina el estado general de los saldos.
        
        Analiza el estado de ambas cuentas y retorna un status consolidado.
        
        Args:
            current_balance: Saldo de cuenta corriente.
            savings_balance: Saldo de cuenta de ahorro.
        
        Returns:
            Estado strings: 'healthy', 'warning', 'unavailable'.
        """
        # Ambos saldos disponibles y positivos
        if (
            current_balance.available
            and savings_balance.available
            and current_balance.amount >= 0
            and savings_balance.amount >= 0
        ):
            return "healthy"
        
        # Al menos un saldo no disponible
        if not current_balance.available or not savings_balance.available:
            return "unavailable"
        
        # Alguno con valor negativo (sobregiro)
        return "warning"


async def get_balance_service() -> BalanceQueryService:
    """Factory para obtener una instancia del servicio de consulta de saldos.
    
    Utiliza inyección de dependencias de FastAPI para obtener los
    colaboradores necesarios.
    
    Returns:
        Instancia configurada de BalanceQueryService.
    """
    from app.config.settings import get_settings
    from app.infrastructure.repositories import get_account_repository
    from app.infrastructure.external_services import (
        get_current_account_service,
        get_savings_account_service,
    )
    
    settings = get_settings()
    
    current_service = await get_current_account_service()
    savings_service = await get_savings_account_service()
    repository = await get_account_repository()
    
    return BalanceQueryService(
        current_account_service=current_service,
        savings_account_service=savings_service,
        account_repository=repository,
    )

// === ARCHIVO: app/infrastructure/external_services.py ===
"""Clientes HTTP asincrónicos para sistemas externos de saldos."""
import os
from typing import Optional

import httpx

from app.domain.models import (
    AccountBalance,
    AccountType,
    ExternalServiceError,
)


class CurrentAccountClient:
    """Cliente asincrónico para el Sistema de Cuentas Corrientes."""

    def __init__(self, base_url: Optional[str] = None) -> None:
        self.base_url = base_url or os.getenv(
            "CURRENT_ACCOUNT_SERVICE_URL",
            "http://localhost:8001"
        )
        self.timeout = httpx.Timeout(10.0, connect=5.0)

    async def get_balance(self, account_id: str) -> AccountBalance:
        """Consulta el saldo de una cuenta corriente."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/accounts/{account_id}/balance"
                )
                if response.status_code == 404:
                    raise ExternalServiceError(
                        service_name="current_account",
                        message=f"Cuenta {account_id} no encontrada"
                    )
                if response.status_code >= 500:
                    raise ExternalServiceError(
                        service_name="current_account",
                        message="Error del servicio de cuenta corriente"
                    )
                response.raise_for_status()
                data = response.json()
                return AccountBalance(
                    account_id=account_id,
                    account_type=AccountType.CURRENT,
                    balance=float(data.get("balance", 0.0)),
                    currency=data.get("currency", "USD"),
                    status=data.get("status", "active"),
                )
        except httpx.ConnectError as e:
            raise ExternalServiceError(
                service_name="current_account",
                message=f"Conexión fallida: {str(e)}"
            )
        except httpx.TimeoutException as e:
            raise ExternalServiceError(
                service_name="current_account",
                message=f"Tiempo de espera agotado: {str(e)}"
            )
        except httpx.HTTPStatusError as e:
            raise ExternalServiceError(
                service_name="current_account",
                message=f"Error HTTP {e.response.status_code}: {str(e)}"
            )


class SavingsAccountClient:
    """Cliente asincrónico para el Sistema de Cuentas de Ahorro."""

    def __init__(self, base_url: Optional[str] = None) -> None:
        self.base_url = base_url or os.getenv(
            "SAVINGS_ACCOUNT_SERVICE_URL",
            "http://localhost:8002"
        )
        self.timeout = httpx.Timeout(10.0, connect=5.0)

    async def get_balance(self, account_id: str) -> AccountBalance:
        """Consulta el saldo de una cuenta de ahorro."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/savings/{account_id}/balance"
                )
                if response.status_code == 404:
                    raise ExternalServiceError(
                        service_name="savings_account",
                        message=f"Cuenta de ahorro {account_id} no encontrada"
                    )
                if response.status_code >= 500:
                    raise ExternalServiceError(
                        service_name="savings_account",
                        message="Error del servicio de cuenta de ahorro"
                    )
                response.raise_for_status()
                data = response.json()
                return AccountBalance(
                    account_id=account_id,
                    account_type=AccountType.SAVINGS,
                    balance=float(data.get("balance", 0.0)),
                    currency=data.get("currency", "USD"),
                    status=data.get("status", "active"),
                )
        except httpx.ConnectError as e:
            raise ExternalServiceError(
                service_name="savings_account",
                message=f"Conexión fallida: {str(e)}"
            )
        except httpx.TimeoutException as e:
            raise ExternalServiceError(
                service_name="savings_account",
                message=f"Tiempo de espera agotado: {str(e)}"
            )
        except httpx.HTTPStatusError as e:
            raise ExternalServiceError(
                service_name="savings_account",
                message=f"Error HTTP {e.response.status_code}: {str(e)}"
            )


def get_current_account_client() -> CurrentAccountClient:
    """Factory para obtener instancia del cliente de cuenta corriente."""
    return CurrentAccountClient()


def get_savings_account_client() -> SavingsAccountClient:
    """Factory para obtener instancia del cliente de cuenta de ahorro."""
    return SavingsAccountClient()

// === ARCHIVO: app/infrastructure/repositories.py ===
"""Repositorios asincrónicos para acceso a fuentes de saldos."""
from typing import Protocol, Optional

from app.domain.models import (
    AccountBalance,
    AccountType,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)
from app.infrastructure.external_services import (
    CurrentAccountClient,
    SavingsAccountClient,
)


class AccountBalanceRepository(Protocol):
    """Protocolo para repositorio de saldos de cuenta."""

    async def get_balance(self, account_id: str) -> AccountBalance: ...


class CurrentAccountRepository:
    """Repositorio para consultar saldos de Cuenta Corriente."""

    def __init__(self, client: CurrentAccountClient) -> None:
        self._client = client

    async def get_balance(self, account_id: str) -> AccountBalance:
        """Obtiene el saldo de una cuenta corriente."""
        try:
            balance = await self._client.get_balance(account_id)
            return balance
        except ExternalServiceError as e:
            raise AccountBalanceUnavailableError(
                account_id=account_id,
                account_type=AccountType.CURRENT,
                message=str(e),
            )


class SavingsAccountRepository:
    """Repositorio para consultar saldos de Cuenta de Ahorro."""

    def __init__(self, client: SavingsAccountClient) -> None:
        self._client = client

    async def get_balance(self, account_id: str) -> AccountBalance:
        """Obtiene el saldo de una cuenta de ahorro."""
        try:
            balance = await self._client.get_balance(account_id)
            return balance
        except ExternalServiceError as e:
            raise AccountBalanceUnavailableError(
                account_id=account_id,
                account_type=AccountType.SAVINGS,
                message=str(e),
            )


async def get_current_account_repository(
    client: CurrentAccountClient,
) -> CurrentAccountRepository:
    """Inyección de dependencias para repositorio de cuenta corriente."""
    return CurrentAccountRepository(client)


async def get_savings_account_repository(
    client: SavingsAccountClient,
) -> SavingsAccountRepository:
    """Inyección de dependencias para repositorio de cuenta de ahorro."""
    return SavingsAccountRepository(client)

// === ARCHIVO: app/presentation/api.py ===
from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import Optional

from app.domain.models import ConsolidatedBalanceResponse, AccountBalanceUnavailableError
from app.application.services import AccountBalanceService

router = APIRouter(prefix="/api/v1/accounts", tags=["accounts"])


async def get_balance_service() -> AccountBalanceService:
    from app.main import get_balance_service as _get_service
    return await _get_service()


@router.get(
    "/{account_id}/balances",
    response_model=ConsolidatedBalanceResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar saldos consolidados de una cuenta",
    description="""
    Retorna los saldos de Cuenta Corriente y Cuenta de Ahorro de forma asincrónica.
    
    - **account_id**: Identificador único de la cuenta del cliente
    - **include_details** (opcional): Include additional details about each account
    """
)
async def get_consolidated_balances(
    account_id: str,
    include_details: bool = Query(default=False, description="Include detailed breakdown"),
    service: AccountBalanceService = Depends(get_balance_service),
) -> ConsolidatedBalanceResponse:
    """
    Endpoint principal para consultar saldos consolidados.
    
    Este endpoint orquesta la consulta asíncrona de dos fuentes:
    - Sistema de Cuentas Corrientes
    - Sistema de Cuentas de Ahorro
    
    Args:
        account_id: Identificador de la cuenta del cliente
        include_details: Si true, incluye detalles adicionales en la respuesta
        service: Inyección del servicio de saldos
    
    Returns:
        ConsolidatedBalanceResponse con los saldos consolidados
    
    Raises:
        HTTPException: Si ocurre un error al obtener los saldos
    """
    try:
        result = await service.get_consolidated_balance(account_id, include_details)
        return result
    except AccountBalanceUnavailableError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error": "balance_unavailable",
                "message": e.message or "El saldo no está disponible en este momento",
                "account_id": e.account_id,
                "account_type": e.account_type.value if e.account_type else None,
            },
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": "Error interno del servidor al procesar la solicitud",
            },
        )


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["health"],
)
async def health_check() -> dict:
    """Endpoint de verificación de salud del servicio."""
    return {"status": "healthy", "service": "bank-balances-api"}

// === ARCHIVO: app/presentation/error_handlers.py ===
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Union

from app.domain.models import (
    AccountBalanceUnavailableError,
    ExternalServiceError,
    AccountType,
)


async def account_balance_unavailable_handler(
    request: Request,
    exc: AccountBalanceUnavailableError,
) -> JSONResponse:
    """
    Manejador para errores de saldo no disponible.
    
    Este error ocurre cuando una de las fuentes de saldo (Cuenta Corriente
    o Cuenta de Ahorro) no puede proporcionar el saldo solicitado.
    
    Args:
        request: Objeto de solicitud de FastAPI
        exc: Excepción del dominio con información del error
    
    Returns:
        JSONResponse con código 503 y detalles del error
    """
    account_type_str = exc.account_type.value if exc.account_type else "unknown"
    
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "error": "BALANCE_UNAVAILABLE",
            "message": exc.message or f"El saldo de {account_type_str} no está disponible",
            "account_id": exc.account_id,
            "account_type": account_type_str,
            "path": str(request.url.path),
            "timestamp": "",
        },
    )


async def external_service_error_handler(
    request: Request,
    exc: ExternalServiceError,
) -> JSONResponse:
    """
    Manejador para errores de servicios externos.
    
    Este error ocurre cuando hay un problema de comunicación con los
    sistemas externos (Sistema de Cuentas Corrientes o Sistema de
    Cuentas de Ahorro).
    
    Args:
        request: Objeto de solicitud de FastAPI
        exc: Excepción del dominio con información del servicio fallido
    
    Returns:
        JSONResponse con código 502 y detalles del error
    """
    return JSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content={
            "error": "EXTERNAL_SERVICE_ERROR",
            "message": exc.message or f"Error de comunicación con {exc.service_name}",
            "service_name": exc.service_name,
            "path": str(request.url.path),
            "timestamp": "",
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """
    Manejador para errores de validación de solicitud.
    
    FastAPI valida automáticamente los parámetros de entrada contra
    los modelos Pydantic definidos. Este handler personaliza la respuesta.
    
    Args:
        request: Objeto de solicitud de FastAPI
        exc: Excepción de validación de Pydantic
    
    Returns:
        JSONResponse con código 422 y detalles de validación
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "VALIDATION_ERROR",
            "message": "Error de validación en los parámetros de entrada",
            "details": errors,
            "path": str(request.url.path),
        },
    )


def register_error_handlers(app: FastAPI) -> None:
    """
    Registra todos los manejadores de errores en la aplicación FastAPI.
    
    Este método debe llamarse después de crear la instancia de FastAPI
    para asegurar que todas las excepciones del dominio y técnicas
    tengan manejadores personalizados.
    
    Args:
        app: Instancia de FastAPI donde registrar los manejadores
    
    Note:
        El orden de registro no importa, FastAPI usa el tipo de excepción
        para determinar qué handler usar.
    """
    app.add_exception_handler(AccountBalanceUnavailableError, account_balance_unavailable_handler)
    app.add_exception_handler(ExternalServiceError, external_service_error_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

// === ARCHIVO: tests/test_services.py ===
import pytest
from unittest.mock import AsyncMock, MagicMock
from app.domain.models import (
    AccountType,
    AccountBalance,
    ConsolidatedBalanceResponse,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)
from app.application.services import AccountBalanceService


class TestAccountBalanceService:
    """Pruebas unitarias para el servicio de consulta de saldos."""

    @pytest.fixture
    def mock_current_account_repo(self):
        """Mock del repositorio de cuenta corriente."""
        repo = AsyncMock()
        repo.get_balance.return_value = AccountBalance(
            account_id="ACC001",
            account_type=AccountType.CURRENT,
            balance=1500.50,
            status="active",
        )
        return repo

    @pytest.fixture
    def mock_savings_account_repo(self):
        """Mock del repositorio de cuenta de ahorro."""
        repo = AsyncMock()
        repo.get_balance.return_value = AccountBalance(
            account_id="ACC001",
            account_type=AccountType.SAVINGS,
            balance=2300.75,
            status="active",
        )
        return repo

    @pytest.fixture
    def service(self, mock_current_account_repo, mock_savings_account_repo):
        """Instancia del servicio con repositorios mockeados."""
        return AccountBalanceService(
            current_account_repo=mock_current_account_repo,
            savings_account_repo=mock_savings_account_repo,
        )

    @pytest.mark.asyncio
    async def test_get_consolidated_balance_success(self, service):
        """Verifica que se consolidan correctamente los saldos de ambas cuentas."""
        result = await service.get_consolidated_balance("ACC001")

        assert isinstance(result, ConsolidatedBalanceResponse)
        assert result.account_id == "ACC001"
        assert result.current_account_balance == 1500.50
        assert result.savings_account_balance == 2300.75
        assert result.consolidated_balance == 3801.25
        assert result.status == "active"

    @pytest.mark.asyncio
    async def test_get_consolidated_balance_current_unavailable(self, service, mock_current_account_repo):
        """Maneja el caso cuando la cuenta corriente no está disponible."""
        mock_current_account_repo.get_balance.side_effect = AccountBalanceUnavailableError(
            account_id="ACC001",
            account_type=AccountType.CURRENT,
            message="Sistema de cuentas corrientes no disponible",
        )

        result = await service.get_consolidated_balance("ACC001")

        assert result.account_id == "ACC001"
        assert result.current_account_balance == 0.0
        assert result.savings_account_balance == 2300.75
        assert result.consolidated_balance == 2300.75
        assert result.status == "partial"

    @pytest.mark.asyncio
    async def test_get_consolidated_balance_savings_unavailable(self, service, mock_savings_account_repo):
        """Maneja el caso cuando la cuenta de ahorro no está disponible."""
        mock_savings_account_repo.get_balance.side_effect = AccountBalanceUnavailableError(
            account_id="ACC001",
            account_type=AccountType.SAVINGS,
            message="Sistema de cuentas de ahorro no disponible",
        )

        result = await service.get_consolidated_balance("ACC001")

        assert result.account_id == "ACC001"
        assert result.current_account_balance == 1500.50
        assert result.savings_account_balance == 0.0
        assert result.consolidated_balance == 1500.50
        assert result.status == "partial"

    @pytest.mark.asyncio
    async def test_get_consolidated_balance_both_unavailable(self, service, mock_current_account_repo, mock_savings_account_repo):
        """Maneja el caso cuando ambas cuentas no están disponibles."""
        mock_current_account_repo.get_balance.side_effect = AccountBalanceUnavailableError(
            account_id="ACC001",
            account_type=AccountType.CURRENT,
        )
        mock_savings_account_repo.get_balance.side_effect = AccountBalanceUnavailableError(
            account_id="ACC001",
            account_type=AccountType.SAVINGS,
        )

        result = await service.get_consolidated_balance("ACC001")

        assert result.account_id == "ACC001"
        assert result.current_account_balance == 0.0
        assert result.savings_account_balance == 0.0
        assert result.consolidated_balance == 0.0
        assert result.status == "unavailable"

    @pytest.mark.asyncio
    async def test_get_consolidated_balance_external_service_error(self, service, mock_current_account_repo):
        """Maneja errores externos del servicio."""
        mock_current_account_repo.get_balance.side_effect = ExternalServiceError(
            service_name="current_account_system",
            message="Connection timeout",
        )

        with pytest.raises(ExternalServiceError) as exc_info:
            await service.get_consolidated_balance("ACC001")

        assert exc_info.value.service_name == "current_account_system"

    @pytest.mark.asyncio
    async def test_get_balance_by_type_current(self, service, mock_current_account_repo):
        """Verifica la consulta de saldo por tipo de cuenta - corriente."""
        result = await service.get_balance_by_type("ACC001", AccountType.CURRENT)

        assert isinstance(result, AccountBalance)
        assert result.account_type == AccountType.CURRENT
        mock_current_account_repo.get_balance.assert_called_once_with("ACC001")

    @pytest.mark.asyncio
    async def test_get_balance_by_type_savings(self, service, mock_savings_account_repo):
        """Verifica la consulta de saldo por tipo de cuenta - ahorro."""
        result = await service.get_balance_by_type("ACC001", AccountType.SAVINGS)

        assert isinstance(result, AccountBalance)
        assert result.account_type == AccountType.SAVINGS
        mock_savings_account_repo.get_balance.assert_called_once_with("ACC001")

// === ARCHIVO: tests/test_repositories.py ===
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from httpx import Response, HTTPStatusError
from app.domain.models import (
    AccountType,
    AccountBalance,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)
from app.infrastructure.repositories import CurrentAccountRepository, SavingsAccountRepository


class TestCurrentAccountRepository:
    """Pruebas unitarias para el repositorio de cuenta corriente."""

    @pytest.fixture
    def mock_settings(self):
        """Mock de configuración."""
        settings = MagicMock()
        settings.current_account_service_url = "http://localhost:8001"
        settings.current_account_service_timeout = 5.0
        return settings

    @pytest.mark.asyncio
    async def test_get_balance_success(self, mock_settings):
        """Verifica la obtención exitosa del saldo de cuenta corriente."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "account_id": "ACC001",
                "balance": 1500.50,
                "status": "active",
            }
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = CurrentAccountRepository(settings=mock_settings)
            result = await repo.get_balance("ACC001")

            assert isinstance(result, AccountBalance)
            assert result.account_id == "ACC001"
            assert result.account_type == AccountType.CURRENT
            assert result.balance == 1500.50
            assert result.status == "active"

    @pytest.mark.asyncio
    async def test_get_balance_not_found(self, mock_settings):
        """Maneja el caso de cuenta no encontrada."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_response.json.return_value = {"detail": "Account not found"}
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = CurrentAccountRepository(settings=mock_settings)

            with pytest.raises(AccountBalanceUnavailableError) as exc_info:
                await repo.get_balance("ACC999")

            assert exc_info.value.account_id == "ACC999"
            assert exc_info.value.account_type == AccountType.CURRENT

    @pytest.mark.asyncio
    async def test_get_balance_http_error(self, mock_settings):
        """Maneja errores HTTP del servicio externo."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 500
            mock_response.json.return_value = {"detail": "Internal server error"}
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = CurrentAccountRepository(settings=mock_settings)

            with pytest.raises(AccountBalanceUnavailableError) as exc_info:
                await repo.get_balance("ACC001")

            assert exc_info.value.account_type == AccountType.CURRENT

    @pytest.mark.asyncio
    async def test_get_balance_connection_error(self, mock_settings):
        """Maneja errores de conexión con el servicio externo."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = (
                ExternalServiceError(
                    service_name="current_account_service",
                    message="Connection failed",
                )
            )

            repo = CurrentAccountRepository(settings=mock_settings)

            with pytest.raises(ExternalServiceError) as exc_info:
                await repo.get_balance("ACC001")

            assert exc_info.value.service_name == "current_account_service"


class TestSavingsAccountRepository:
    """Pruebas unitarias para el repositorio de cuenta de ahorro."""

    @pytest.fixture
    def mock_settings(self):
        """Mock de configuración."""
        settings = MagicMock()
        settings.savings_account_service_url = "http://localhost:8002"
        settings.savings_account_service_timeout = 5.0
        return settings

    @pytest.mark.asyncio
    async def test_get_balance_success(self, mock_settings):
        """Verifica la obtención exitosa del saldo de cuenta de ahorro."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "account_id": "ACC001",
                "balance": 2300.75,
                "status": "active",
            }
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = SavingsAccountRepository(settings=mock_settings)
            result = await repo.get_balance("ACC001")

            assert isinstance(result, AccountBalance)
            assert result.account_id == "ACC001"
            assert result.account_type == AccountType.SAVINGS
            assert result.balance == 2300.75
            assert result.status == "active"

    @pytest.mark.asyncio
    async def test_get_balance_not_found(self, mock_settings):
        """Maneja el caso de cuenta no encontrada."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_response.json.return_value = {"detail": "Account not found"}
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = SavingsAccountRepository(settings=mock_settings)

            with pytest.raises(AccountBalanceUnavailableError) as exc_info:
                await repo.get_balance("ACC999")

            assert exc_info.value.account_id == "ACC999"
            assert exc_info.value.account_type == AccountType.SAVINGS

    @pytest.mark.asyncio
    async def test_get_balance_service_unavailable(self, mock_settings):
        """Maneja el caso de servicio no disponible."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 503
            mock_response.json.return_value = {"detail": "Service unavailable"}
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            repo = SavingsAccountRepository(settings=mock_settings)

            with pytest.raises(AccountBalanceUnavailableError) as exc_info:
                await repo.get_balance("ACC001")

            assert exc_info.value.account_type == AccountType.SAVINGS

    @pytest.mark.asyncio
    async def test_get_balance_timeout(self, mock_settings):
        """Maneja errores de timeout."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = (
                ExternalServiceError(
                    service_name="savings_account_service",
                    message="Request timeout",
                )
            )

            repo = SavingsAccountRepository(settings=mock_settings)

            with pytest.raises(ExternalServiceError) as exc_info:
                await repo.get_balance("ACC001")

            assert exc_info.value.service_name == "savings_account_service"

// === ARCHIVO: tests/test_api.py ===
import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock, MagicMock
from app.main import create_app
from app.domain.models import (
    AccountType,
    AccountBalance,
    ConsolidatedBalanceResponse,
    AccountBalanceUnavailableError,
    ExternalServiceError,
)


@pytest.fixture
async def client():
    """Cliente HTTP asíncrono para pruebas de integración."""
    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestAccountBalancesEndpoint:
    """Pruebas de integración para el endpoint de consulta de saldos."""

    @pytest.mark.asyncio
    async def test_get_balances_success(self, client):
        """Verifica la respuesta exitosa del endpoint de saldos."""
        mock_balance_current = AccountBalance(
            account_id="ACC001",
            account_type=AccountType.CURRENT,
            balance=1500.50,
            status="active",
        )
        mock_balance_savings = AccountBalance(
            account_id="ACC001",
            account_type=AccountType.SAVINGS,
            balance=2300.75,
            status="active",
        )
        mock_response = ConsolidatedBalanceResponse(
            account_id="ACC001",
            current_account_balance=1500.50,
            savings_account_balance=2300.75,
            consolidated_balance=3801.25,
            status="active",
        )

        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            response = await client.get("/api/v1/accounts/ACC001/balances")

        assert response.status_code == 200
        data = response.json()
        assert data["account_id"] == "ACC001"
        assert data["current_account_balance"] == 1500.50
        assert data["savings_account_balance"] == 2300.75
        assert data["consolidated_balance"] == 3801.25
        assert data["status"] == "active"

    @pytest.mark.asyncio
    async def test_get_balances_with_details_param(self, client):
        """Verifica que el parámetro query include_details se procesa correctamente."""
        mock_response = ConsolidatedBalanceResponse(
            account_id="ACC001",
            current_account_balance=1500.50,
            savings_account_balance=2300.75,
            consolidated_balance=3801.25,
            status="active",
        )

        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            response = await client.get("/api/v1/accounts/ACC001/balances?include_details=true")

        assert response.status_code == 200
        data = response.json()
        assert "account_id" in data

    @pytest.mark.asyncio
    async def test_get_balances_account_not_found(self, client):
        """Verifica el manejo de cuenta no encontrada."""
        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            side_effect=AccountBalanceUnavailableError(
                account_id="ACC999",
                account_type=AccountType.CURRENT,
                message="Account not found",
            ),
        ):
            response = await client.get("/api/v1/accounts/ACC999/balances")

        assert response.status_code == 404
        data = response.json()
        assert "detail" in data

    @pytest.mark.asyncio
    async def test_get_balances_service_unavailable(self, client):
        """Verifica el manejo de servicio externo no disponible."""
        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            side_effect=ExternalServiceError(
                service_name="current_account_service",
                message="Service unavailable",
            ),
        ):
            response = await client.get("/api/v1/accounts/ACC001/balances")

        assert response.status_code == 503
        data = response.json()
        assert "detail" in data

    @pytest.mark.asyncio
    async def test_get_balances_partial_response(self, client):
        """Verifica el manejo de respuesta parcial cuando una cuenta no está disponible."""
        mock_response = ConsolidatedBalanceResponse(
            account_id="ACC001",
            current_account_balance=0.0,
            savings_account_balance=2300.75,
            consolidated_balance=2300.75,
            status="partial",
        )

        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            response = await client.get("/api/v1/accounts/ACC001/balances")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "partial"
        assert data["current_account_balance"] == 0.0
        assert data["savings_account_balance"] == 2300.75

    @pytest.mark.asyncio
    async def test_get_balances_invalid_account_id(self, client):
        """Verifica el manejo de ID de cuenta inválido."""
        response = await client.get("/api/v1/accounts//balances")
        assert response.status_code in [404, 422]

    @pytest.mark.asyncio
    async def test_get_balances_unavailable_status(self, client):
        """Verifica el manejo cuando ambas cuentas no están disponibles."""
        mock_response = ConsolidatedBalanceResponse(
            account_id="ACC001",
            current_account_balance=0.0,
            savings_account_balance=0.0,
            consolidated_balance=0.0,
            status="unavailable",
        )

        with patch(
            "app.application.services.AccountBalanceService.get_consolidated_balance",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            response = await client.get("/api/v1/accounts/ACC001/balances")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "unavailable"
        assert data["consolidated_balance"] == 0.0

    @pytest.mark.asyncio
    async def test_health_endpoint(self, client):
        """Verifica que el endpoint de healthcheck responde correctamente."""
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data

// === ARCHIVO: requirements.txt ===
fastapi==0.115.0
uvicorn==0.30.6
pydantic==2.9.2
pydantic-settings==2.5.2
httpx==0.27.2
python-dotenv==1.0.1
pytest==8.3.2
pytest-asyncio==0.24.0
```
