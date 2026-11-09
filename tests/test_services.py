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