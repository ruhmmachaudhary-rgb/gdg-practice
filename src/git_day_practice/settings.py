from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI App"
    API_KEY: str  # required, must be in .env

    class Config:
        env_file = ".env"


settings = Settings()
