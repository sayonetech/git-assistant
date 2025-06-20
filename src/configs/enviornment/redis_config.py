from pydantic import Field, NonNegativeInt, PositiveFloat, PositiveInt
from pydantic_settings import BaseSettings


class RedisConfig(BaseSettings):
    """
    Configuration settings for Redis connection
    """

    REDIS_HOST: str = Field(
        description="Hostname or IP address of the Redis server",
        default="localhost",
    )

    REDIS_PORT: PositiveInt = Field(
        description="Port number on which the Redis server is listening",
        default=6379,
    )

    REDIS_USERNAME: str | None = Field(
        description="Username for Redis authentication (if required)",
        default=None,
    )

    REDIS_PASSWORD: str | None = Field(
        description="Password for Redis authentication (if required)",
        default=None,
    )

    REDIS_DB: NonNegativeInt = Field(
        description="Redis database number to use (0-15)",
        default=0,
    )

    REDIS_USE_SSL: bool = Field(
        description="Enable SSL/TLS for the Redis connection",
        default=False,
    )

    REDIS_USE_SENTINEL: bool | None = Field(
        description="Enable Redis Sentinel mode for high availability",
        default=False,
    )

    REDIS_SENTINELS: str | None = Field(
        description="Comma-separated list of Redis Sentinel nodes (host:port)",
        default=None,
    )

    REDIS_SENTINEL_SERVICE_NAME: str | None = Field(
        description="Name of the Redis Sentinel service to monitor",
        default=None,
    )

    REDIS_SENTINEL_USERNAME: str | None = Field(
        description="Username for Redis Sentinel authentication (if required)",
        default=None,
    )

    REDIS_SENTINEL_PASSWORD: str | None = Field(
        description="Password for Redis Sentinel authentication (if required)",
        default=None,
    )

    REDIS_SENTINEL_SOCKET_TIMEOUT: PositiveFloat | None = Field(
        description="Socket timeout in seconds for Redis Sentinel connections",
        default=0.1,
    )

    REDIS_USE_CLUSTERS: bool = Field(
        description="Enable Redis Clusters mode for high availability",
        default=False,
    )

    REDIS_CLUSTERS: str | None = Field(
        description="Comma-separated list of Redis Clusters nodes (host:port)",
        default=None,
    )

    REDIS_CLUSTERS_PASSWORD: str | None = Field(
        description="Password for Redis Clusters authentication (if required)",
        default=None,
    )
