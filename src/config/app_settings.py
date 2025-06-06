from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class AppSettings(BaseSettings):
    """Application settings."""
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Application"
    
    # Server Settings
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)
    
    # Environment
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_app_settings() -> AppSettings:
    """Get cached app settings instance."""
    return AppSettings() 