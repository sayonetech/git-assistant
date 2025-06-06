from configs.enviornment.db_config import DatabaseConfig
from configs.enviornment.http_config import HttpConfig
from configs.enviornment.logging_config import LoggingConfig
from configs.enviornment.redis_config import RedisConfig
from configs.enviornment.security_config import SecurityConfig
from configs.enviornment.qdrant_config import QdrantConfig


class EnviornmentConfig(
    # place the configs in alphabet order
    DatabaseConfig,
    HttpConfig,
    LoggingConfig,
    QdrantConfig,
    RedisConfig,
    SecurityConfig,
):
    pass
