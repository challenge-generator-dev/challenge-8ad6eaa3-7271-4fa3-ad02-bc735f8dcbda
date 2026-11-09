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