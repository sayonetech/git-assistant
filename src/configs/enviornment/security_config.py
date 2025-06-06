from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings


class SecurityConfig(BaseSettings):
    """
    Security-related configurations for the application
    """

    SECRET_KEY: str = Field(
        description="Secret key for secure session cookie signing."
        "Make sure you are changing this key for your deployment with a strong key."
        "Generate a strong key using `openssl rand -base64 42` or set via the `SECRET_KEY` environment variable.",
        default="",
    )

    ADMIN_API_KEY_ENABLE: bool = Field(
        description="Whether to enable admin api key for authentication",
        default=False,
    )

    ADMIN_API_KEY: str | None = Field(
        description="admin api key for authentication",
        default=None,
    )
