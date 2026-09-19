from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    NAME_PROJECT: str
    DESCRIPTION: str
    ROOT_PATH: str
    IS_PRODUCTION: bool
    VERSION: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
