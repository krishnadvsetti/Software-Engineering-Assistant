from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Software Engineering Assistant"
    APP_VERSION: str = "0.1.0"

    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()