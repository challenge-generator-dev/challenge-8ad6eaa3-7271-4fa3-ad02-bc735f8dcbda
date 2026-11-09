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