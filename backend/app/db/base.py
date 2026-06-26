from app.models.base import Base

# Import models here so Alembic can discover them
from app.models.user import User

__all__ = [
    "Base",
]