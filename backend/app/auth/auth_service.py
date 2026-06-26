from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user: UserCreate,
    ):

        existing_user = UserRepository.get_by_email(
            db,
            user.email,
        )

        if existing_user:
            raise ValueError("User already exists.")

        hashed_password = hash_password(user.password)

        return UserRepository.create(
            db=db,
            user=user,
            hashed_password=hashed_password,
        )