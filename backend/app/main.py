from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Software Engineering Workspace",
)

app.include_router(router, prefix=settings.API_PREFIX)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} API is running."
    }