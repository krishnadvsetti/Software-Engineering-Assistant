from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str,
    ):
        return UserRepository.get_by_email(db, email)

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate,
        hashed_password: str,
    ):
        return UserRepository.create(
            db,
            user,
            hashed_password,
        )