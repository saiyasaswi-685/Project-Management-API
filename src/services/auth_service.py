from src.core.exceptions import bad_request, unauthorized
from src.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from src.database.repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, email: str, password: str):
        existing_user = self.repository.get_user_by_email(email)

        if existing_user:
            bad_request("Email already registered.")

        hashed_password = hash_password(password)

        return self.repository.create_user(
            email=email,
            hashed_password=hashed_password,
        )

    def login(self, email: str, password: str):
        user = self.repository.get_user_by_email(email)

        if user is None:
            unauthorized("Invalid email or password.")

        if not verify_password(password, user.hashed_password):
            unauthorized("Invalid email or password.")

        access_token = create_access_token(
            data={"sub": str(user.id)}
        )

        return access_token