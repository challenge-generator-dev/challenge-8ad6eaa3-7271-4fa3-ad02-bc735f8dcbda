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