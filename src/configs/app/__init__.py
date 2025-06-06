
from configs.app.celery_config import CeleryBeatConfig, CeleryConfig
from configs.app.llm_config import LlmConfig


class AppConfig(
    # place the configs in alphabet order
    CeleryConfig,
    CeleryBeatConfig,
    LlmConfig,
):
    pass
