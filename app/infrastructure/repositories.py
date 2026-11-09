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