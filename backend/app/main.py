import logging

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI Software Engineering Workspace",
)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting Software Engineering Assistant...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Software Engineering Assistant...")


app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "message": "Welcome to the AI Software Engineering Workspace",
    }