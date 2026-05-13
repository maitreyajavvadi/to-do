from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/todo_db"
    SECRET_KEY: str = "changeme-use-openssl-rand-hex-32"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_REDIRECT_URI: str = "http://localhost:3000/auth/callback/google"

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://*.vercel.app",
    ]

    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAIL_FROM: str = "noreply@taskflow.app"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
