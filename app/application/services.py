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