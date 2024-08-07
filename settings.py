from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    page_title: str = "Weather Chatbot"
    page_icon: str = "⛅"
    layout: str = "centered"

    flowise_base_url: str = "http://localhost:3000/"
    flowise_chatflow_id: str = "68405b17-c5b2-4300-ac99-a91df8bbce21"
    flowise_username: str = "c42ed0ed18dc07cad699a742a4a7cc7c"
    flowise_password: str = "ad1602569190bef23d448b7c2453239d"
    openai_api_key: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
