from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str
    USER: str
    PASSWORD: str
    DATABASE: str

    class Config:
        env_file = ".env"


settings = Settings()
