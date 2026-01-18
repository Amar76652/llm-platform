from fastapi import FastAPI
from app.api import health, prompt
from app.core.config import settings
app = FastAPI(title=settings.app_name)

app.include_router(health.router)
app.include_router(prompt.router)

@app.get("/")
def root():
    return {"message": "ML service is running"}