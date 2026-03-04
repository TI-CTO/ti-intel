"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Intel Store configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    supabase_url: str
    supabase_key: str
    tavily_api_key: str = ""
    semantic_scholar_api_key: str = ""
    embedding_model: str = "intfloat/multilingual-e5-large"


settings = Settings()
