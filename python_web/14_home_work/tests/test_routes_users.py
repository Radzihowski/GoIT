"""
Integration tests for src/routes/users.py
Both endpoints are covered. Cloudinary upload is mocked.
"""
from unittest.mock import MagicMock, AsyncMock, patch
from io import BytesIO
from datetime import datetime

from src.database.models import User


def _auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _mock_user(email: str) -> User:
    u = User(id=1, email=email, confirmed=True, avatar="http://old-avatar.com")
    u.created_at = datetime(2024, 1, 1, 0, 0, 0)
    return u


# ---------------------------------------------------------------------------
# GET /api/users/me/   — read_users_me
# ---------------------------------------------------------------------------

def test_read_users_me(client, access_token, user):
    mock_user = _mock_user(user["email"])

    with patch("src.routes.users.auth_service.get_current_user", return_value=mock_user):
        response = client.get(
            "/api/users/me/",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == user["email"]


def test_read_users_me_unauthorized(client):
    response = client.get("/api/users/me/")
    assert response.status_code == 403


# ---------------------------------------------------------------------------
# PATCH /api/users/avatar   — update_avatar_user
# ---------------------------------------------------------------------------

def test_update_avatar_success(client, access_token, user):
    mock_user = _mock_user(user["email"])
    mock_upload_result = {"version": "12345"}
    new_url = "http://cloudinary.com/new-avatar"

    with patch("src.routes.users.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.users.cloudinary.uploader.upload", return_value=mock_upload_result), \
         patch("src.routes.users.cloudinary.CloudinaryImage") as mock_image, \
         patch("src.routes.users.repository_users.update_avatar", new=AsyncMock()):

        mock_image.return_value.build_url.return_value = new_url

        response = client.patch(
            "/api/users/avatar",
            headers=_auth_headers(access_token),
            files={"file": ("avatar.png", BytesIO(b"fake-image-data"), "image/png")},
        )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["url"] == new_url
    assert "detail" in data
