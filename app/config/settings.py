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