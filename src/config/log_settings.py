from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class LogSettings(BaseSettings):
    """Log settings."""
    
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    LOG_FILE: str = Field(default="app.log")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_log_settings() -> LogSettings:
    """Get cached log settings instance."""
    return LogSettings() 