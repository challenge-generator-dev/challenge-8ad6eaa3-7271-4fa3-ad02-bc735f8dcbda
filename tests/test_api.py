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