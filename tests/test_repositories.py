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