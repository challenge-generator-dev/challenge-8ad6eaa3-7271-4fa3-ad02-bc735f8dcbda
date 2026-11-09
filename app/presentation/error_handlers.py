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