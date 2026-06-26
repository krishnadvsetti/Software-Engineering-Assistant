from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health():
    return {
        "status": "healthy",
        "service": "Software Engineering Assistant",
        "timestamp": datetime.now(timezone.utc),
    }