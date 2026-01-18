from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "LLM ML Service"
    env: str = "dev"

settings = Settings()