from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException

from src.services.auth_service import AuthService


class TestAuthService:

    @patch("src.services.auth_service.hash_password")
    def test_register_success(self, mock_hash_password):
        repository = MagicMock()

        repository.get_user_by_email.return_value = None
        repository.create_user.return_value = {
            "email": "test@example.com"
        }

        mock_hash_password.return_value = "hashed_password"

        service = AuthService(repository)

        result = service.register(
            email="test@example.com",
            password="Password123",
        )

        assert result["email"] == "test@example.com"

        repository.create_user.assert_called_once_with(
            email="test@example.com",
            hashed_password="hashed_password",
        )

    def test_register_duplicate_email(self):
        repository = MagicMock()

        repository.get_user_by_email.return_value = object()

        service = AuthService(repository)

        with pytest.raises(HTTPException):
            service.register(
                email="test@example.com",
                password="Password123",
            )

    @patch("src.services.auth_service.verify_password")
    @patch("src.services.auth_service.create_access_token")
    def test_login_success(
        self,
        mock_create_token,
        mock_verify_password,
    ):
        repository = MagicMock()

        user = MagicMock()
        user.id = 1
        user.hashed_password = "hashed"

        repository.get_user_by_email.return_value = user

        mock_verify_password.return_value = True
        mock_create_token.return_value = "jwt_token"

        service = AuthService(repository)

        token = service.login(
            email="test@example.com",
            password="Password123",
        )

        assert token == "jwt_token"

    def test_login_invalid_email(self):
        repository = MagicMock()

        repository.get_user_by_email.return_value = None

        service = AuthService(repository)

        with pytest.raises(HTTPException):
            service.login(
                email="wrong@example.com",
                password="Password123",
            )

    @patch("src.services.auth_service.verify_password")
    def test_login_invalid_password(
        self,
        mock_verify_password,
    ):
        repository = MagicMock()

        user = MagicMock()
        user.hashed_password = "hashed"

        repository.get_user_by_email.return_value = user

        mock_verify_password.return_value = False

        service = AuthService(repository)

        with pytest.raises(HTTPException):
            service.login(
                email="test@example.com",
                password="WrongPassword",
            )