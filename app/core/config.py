from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, loaded once from environment variables / .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # don't crash on other keys present in .env
    )

    # Required: no default, so a missing value stops the app at startup
    db_user: str
    db_password: SecretStr
    db_name: str

    # Safe defaults
    db_host: str = "localhost"
    db_port: int = 5432


@lru_cache
def get_settings() -> Settings:
    """Create the Settings object once and reuse it everywhere."""
    return Settings()