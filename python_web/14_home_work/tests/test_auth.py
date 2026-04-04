from unittest.mock import MagicMock, AsyncMock, patch
from datetime import datetime
from src.database.models import User


# ---------------------------------------------------------------------------
# POST /api/auth/signup  (lines 31-37)
# ---------------------------------------------------------------------------

def test_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)

    response = client.post(
        "/api/auth/signup",
        json=user,
    )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data["user"]["email"] == user.get("email")
    assert "id" in data["user"]


def test_repeat_create_user(client, user):
    response = client.post(
        "/api/auth/signup",
        json=user,
    )
    assert response.status_code == 409, response.text
    assert response.json()["detail"] == "Account already exists"


def test_signup_mocked_success(client, user):                      # lines 34-37
    new_user_dict = {
        "id": 99, "email": user["email"],
        "created_at": datetime(2024, 1, 1).isoformat(), "avatar": None,
    }
    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=None)), \
         patch("src.routes.auth.repository_users.create_user", new=AsyncMock(return_value=new_user_dict)), \
         patch("src.routes.auth.auth_service.get_password_hash", return_value="hashed"), \
         patch("src.routes.auth.send_email", MagicMock()):

        response = client.post("/api/auth/signup", json=user)

    assert response.status_code == 201, response.text
    assert response.json()["user"]["id"] == 99


def test_signup_mocked_conflict(client, user):                     # line 33
    existing = User(id=1, email=user["email"])
    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=existing)):
        response = client.post("/api/auth/signup", json=user)

    assert response.status_code == 409, response.text
    assert response.json()["detail"] == "Account already exists"


# ---------------------------------------------------------------------------
# POST /api/auth/login  (lines 53-64)
# ---------------------------------------------------------------------------

def test_login_mocked_invalid_email(client, user):                 # line 55
    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=None)):
        response = client.post("/api/auth/login", json={"email": "ghost@test.com", "password": "pass1234"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email"


def test_login_mocked_invalid_password(client, user):              # line 57
    mock_user = User(id=1, email=user["email"], confirmed=True, password="hashed")
    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.auth_service.verify_password", return_value=False):
        response = client.post("/api/auth/login", json={"email": user["email"], "password": "badpass1"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid password"


def test_login_mocked_not_confirmed(client, user):                 # line 59
    mock_user = User(id=1, email=user["email"], confirmed=False, password="hashed")
    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.auth_service.verify_password", return_value=True):
        response = client.post("/api/auth/login", json=user)
    assert response.status_code == 401
    assert response.json()["detail"] == "Email not confirmed"



    response = client.post("/api/auth/login", json=user)
    assert response.status_code == 401, response.text
    assert response.json()["detail"] == "Email not confirmed"


def test_login_user(client, session, user):                        # lines 60-64
    current_user: User = session.query(User).filter(
        User.email == user.get("email")
    ).first()
    current_user.confirmed = True
    session.commit()

    response = client.post("/api/auth/login", json=user)
    assert response.status_code == 200, response.text
    assert response.json()["token_type"] == "bearer"


def test_login_wrong_password(client, user):                       # line 55-56
    response = client.post(
        "/api/auth/login",
        json={"email": user.get("email"), "password": "password"},
    )
    assert response.status_code == 401, response.text
    assert response.json()["detail"] == "Invalid password"


def test_login_wrong_email(client, user):                          # line 53-54
    response = client.post(
        "/api/auth/login",
        json={"email": "noone@nowhere.com", "password": user.get("password")},
    )
    assert response.status_code == 401, response.text
    assert response.json()["detail"] == "Invalid email"


def test_login_mocked_success(client, user):                       # lines 60-64 via mock
    mock_user = User(id=1, email=user["email"], confirmed=True, password="hashed")

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.auth_service.verify_password", return_value=True), \
         patch("src.routes.auth.repository_users.update_token", new=AsyncMock()):

        response = client.post("/api/auth/login", json=user)

    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


# ---------------------------------------------------------------------------
# GET /api/auth/refresh_token
# ---------------------------------------------------------------------------

def test_refresh_token_success(client, user):
    from src.services.auth import auth_service
    import asyncio
    mock_user = User(id=1, email=user["email"], confirmed=True)
    refresh_tok = asyncio.run(auth_service.create_refresh_token(data={"sub": user["email"]}))
    mock_user.refresh_token = refresh_tok

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.repository_users.update_token", new=AsyncMock()):

        response = client.get(
            "/api/auth/refresh_token",
            headers={"Authorization": f"Bearer {refresh_tok}"},
        )

    assert response.status_code == 200, response.text
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_refresh_token_mismatch(client, user):                     # lines 84-85
    from src.services.auth import auth_service
    import asyncio
    refresh_tok = asyncio.run(auth_service.create_refresh_token(data={"sub": user["email"]}))
    mock_user = User(id=1, email=user["email"], confirmed=True)
    mock_user.refresh_token = "different-stored-token"             # mismatch → 401

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.repository_users.update_token", new=AsyncMock()):

        response = client.get(
            "/api/auth/refresh_token",
            headers={"Authorization": f"Bearer {refresh_tok}"},
        )

    assert response.status_code == 401, response.text
    assert response.json()["detail"] == "Invalid refresh token"


def test_refresh_token_invalid(client):
    response = client.get(
        "/api/auth/refresh_token",
        headers={"Authorization": "Bearer invalid.token.here"},
    )
    assert response.status_code == 401


# ---------------------------------------------------------------------------
# GET /api/auth/confirmed_email/{token}
# ---------------------------------------------------------------------------

def test_confirmed_email_success(client, user):
    from src.services.auth import auth_service
    email_token = auth_service.create_email_token({"sub": user["email"]})
    mock_user = User(id=1, email=user["email"], confirmed=False)

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)), \
         patch("src.routes.auth.repository_users.confirmed_email", new=AsyncMock()):
        response = client.get(f"/api/auth/confirmed_email/{email_token}")

    assert response.status_code == 200, response.text
    assert response.json()["message"] == "Email confirmed"


def test_confirmed_email_already_confirmed(client, user):
    from src.services.auth import auth_service
    email_token = auth_service.create_email_token({"sub": user["email"]})
    mock_user = User(id=1, email=user["email"], confirmed=True)

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=mock_user)):
        response = client.get(f"/api/auth/confirmed_email/{email_token}")

    assert response.status_code == 200, response.text
    assert response.json()["message"] == "Your email is already confirmed"


def test_confirmed_email_user_not_found(client, user):
    from src.services.auth import auth_service
    email_token = auth_service.create_email_token({"sub": user["email"]})

    with patch("src.routes.auth.repository_users.get_user_by_email", new=AsyncMock(return_value=None)):
        response = client.get(f"/api/auth/confirmed_email/{email_token}")

    assert response.status_code == 400


# ---------------------------------------------------------------------------
# GET /api/auth/logout
# ---------------------------------------------------------------------------

def test_logout_success(client, access_token):
    with patch.object(
        __import__("src.services.auth", fromlist=["auth_service"]).auth_service,
        "add_token_to_blacklist",
        return_value=None,
    ):
        response = client.get(
            "/api/auth/logout",
            headers={"Authorization": f"Bearer {access_token}"},
        )
    assert response.status_code == 200, response.text
    assert response.json()["message"] == "Successfully logged out"

