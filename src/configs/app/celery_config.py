from pydantic import Field, PositiveFloat, computed_field
from pydantic_settings import BaseSettings

from configs.enviornment.db_config import DatabaseConfig


class CeleryBeatConfig(BaseSettings):
    CELERY_BEAT_SCHEDULER_TIME: int = Field(
        description="Interval in days for Celery Beat scheduler execution, default to 1 day",
        default=1,
    )


class CeleryConfig(DatabaseConfig):
    CELERY_BACKEND: str = Field(
        description="Backend for Celery task results. Options: 'database', 'redis'.",
        default="database",
    )

    CELERY_BROKER_URL: str | None = Field(
        description="URL of the message broker for Celery tasks.",
        default=None,
    )

    CELERY_USE_SENTINEL: bool | None = Field(
        description="Whether to use Redis Sentinel for high availability.",
        default=False,
    )

    CELERY_SENTINEL_MASTER_NAME: str | None = Field(
        description="Name of the Redis Sentinel master.",
        default=None,
    )

    CELERY_SENTINEL_SOCKET_TIMEOUT: PositiveFloat | None = Field(
        description="Timeout for Redis Sentinel socket operations in seconds.",
        default=0.1,
    )

    @computed_field
    @property
    def CELERY_RESULT_BACKEND(self) -> str | None:
        return (
            f"db+{self.SQLALCHEMY_DATABASE_URI}"
            if self.CELERY_BACKEND == "database"
            else self.CELERY_BROKER_URL
        )

    @computed_field
    @property
    def BROKER_USE_SSL(self) -> bool:
        return (
            self.CELERY_BROKER_URL.startswith("rediss://")
            if self.CELERY_BROKER_URL
            else False
        )
