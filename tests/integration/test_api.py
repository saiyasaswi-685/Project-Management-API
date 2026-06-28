from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestAPI:

    def test_home(self):
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {
            "message": "Project Management API is running"
        }

    def test_register_user(self):
        response = client.post(
            "/api/auth/register",
            json={
                "email": "integration@example.com",
                "password": "Password123"
            },
        )

        # User may already exist if test runs multiple times
        assert response.status_code in [201, 400]

    def test_login_invalid_credentials(self):
        response = client.post(
            "/api/auth/login",
            json={
                "email": "wrong@example.com",
                "password": "wrongpassword"
            },
        )

        assert response.status_code == 401