from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    page_title: str = "Weather Chatbot"
    page_icon: str = "⛅"
    layout: str = "centered"

    flowise_base_url: str = "https://reinaldoviedo94-flowise.hf.space/"
    flowise_chatflow_id: str = "267ea9e5-45f4-479c-8261-39ba8cc9c019"
    flowise_username: str = "c42ed0ed18dc07cad699a742a4a7cc7c"
    flowise_password: str = "ad1602569190bef23d448b7c2453239d"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()