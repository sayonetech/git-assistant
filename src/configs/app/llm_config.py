from pydantic import Field
from pydantic_settings import BaseSettings


class LlmConfig(BaseSettings):
    """
    Configuration for LLM Provider
    """

    PROVIDER_NAME: str = Field(
        description="LLM Provider Name",
        default="vertex_ai",
    )

    RE_RANKING_PROVIDER_NAME: str = Field(
        description="Reranking Provider Name",
        default="cohere",
    )

    MODEL_NAME: str = Field(
        description="LLM model Name",
        default="gemini-1.5-flash-002",
    )

    EMBEDDING_MODEL_NAME: str = Field(
        description="Embedding model Name",
        default="text-multilingual-embedding-002",
    )

    RE_RANKING_MODEL_NAME: str = Field(
        description="Embedding model Name",
        default="rerank-english-v3.0",
    )

    LB_ENABLED: bool = Field(
        description="Enable or disable billing functionality",
        default=False,
    )
