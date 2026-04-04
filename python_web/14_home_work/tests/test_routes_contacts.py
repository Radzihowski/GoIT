"""
Integration tests for src/routes/contacts.py
Every endpoint is covered. The service and auth layers are mocked
so tests run without a real database or Redis.
"""
from unittest.mock import MagicMock, AsyncMock, patch

from src.database.models import Contact, User


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _mock_user(user_fixture) -> User:
    return User(id=1, email=user_fixture["email"], confirmed=True)


def _contact(**kwargs) -> Contact:
    defaults = dict(
        id=1,
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone="123456789",
        date_of_birth="1990-01-01",
        info="test",
        user_id=1,
    )
    defaults.update(kwargs)
    c = Contact()
    for k, v in defaults.items():
        setattr(c, k, v)
    return c


# ---------------------------------------------------------------------------
# POST /api/contacts/   — create_contact
# ---------------------------------------------------------------------------

def test_create_contact_success(client, access_token, user):
    mock_user = _mock_user(user)
    mock_service = AsyncMock(return_value={"id": 1})

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.create_contact", mock_service):

        response = client.post(
            "/api/contacts/",
            headers=_auth_headers(access_token),
            json={
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "123456789",
                "date_of_birth": "1990-01-01",
                "info": "test",
            },
        )

    assert response.status_code == 201, response.text
    assert response.json()["id"] == 1


def test_create_contact_unauthorized(client):
    response = client.post("/api/contacts/", json={})
    assert response.status_code == 403


# ---------------------------------------------------------------------------
# GET /api/contacts/   — read_contacts
# ---------------------------------------------------------------------------

def test_read_contacts_success(client, access_token, user):
    mock_user = _mock_user(user)
    contacts = [_contact(id=1), _contact(id=2)]
    mock_service = AsyncMock(return_value=contacts)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.read_contacts", mock_service):

        response = client.get(
            "/api/contacts/",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2


# ---------------------------------------------------------------------------
# GET /api/contacts/search   — search_contacts
# ---------------------------------------------------------------------------

def test_search_contacts_by_name(client, access_token, user):
    mock_user = _mock_user(user)
    contacts = [_contact(first_name="John")]
    mock_service = AsyncMock(return_value=contacts)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.search_contacts", mock_service):

        response = client.get(
            "/api/contacts/search?first_name=John",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text
    assert response.json()[0]["first_name"] == "John"


def test_search_contacts_empty_result(client, access_token, user):
    mock_user = _mock_user(user)
    mock_service = AsyncMock(return_value=[])

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.search_contacts", mock_service):

        response = client.get(
            "/api/contacts/search?first_name=Nobody",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text
    assert response.json() == []


# ---------------------------------------------------------------------------
# GET /api/contacts/upcoming_dob   — upcoming_dob
# ---------------------------------------------------------------------------

def test_upcoming_dob(client, access_token, user):
    mock_user = _mock_user(user)
    contacts = [_contact()]
    mock_service = AsyncMock(return_value=contacts)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.upcoming_dob", mock_service):

        response = client.get(
            "/api/contacts/upcoming_dob?days_range=7",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text


# ---------------------------------------------------------------------------
# GET /api/contacts/{id}   — read_contact
# ---------------------------------------------------------------------------

def test_read_contact_found(client, access_token, user):
    mock_user = _mock_user(user)
    contact = _contact(id=1)
    mock_service = AsyncMock(return_value=contact)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.read_contact", mock_service):

        response = client.get(
            "/api/contacts/1",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 200, response.text
    assert response.json()["id"] == 1


def test_read_contact_not_found(client, access_token, user):
    from fastapi import HTTPException
    mock_user = _mock_user(user)
    mock_service = AsyncMock(side_effect=HTTPException(status_code=404, detail="Not found"))

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.read_contact", mock_service):

        response = client.get(
            "/api/contacts/999",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# PUT /api/contacts/{id}   — update_contact
# ---------------------------------------------------------------------------

def test_update_contact_success(client, access_token, user):
    mock_user = _mock_user(user)
    updated = _contact(first_name="Jane")
    mock_service = AsyncMock(return_value=updated)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.update_contact", mock_service):

        response = client.put(
            "/api/contacts/1",
            headers=_auth_headers(access_token),
            json={"first_name": "Jane"},
        )

    assert response.status_code == 200, response.text
    assert response.json()["first_name"] == "Jane"


def test_update_contact_not_found(client, access_token, user):
    from fastapi import HTTPException
    mock_user = _mock_user(user)
    mock_service = AsyncMock(side_effect=HTTPException(status_code=404, detail="Not found"))

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.update_contact", mock_service):

        response = client.put(
            "/api/contacts/999",
            headers=_auth_headers(access_token),
            json={"first_name": "Jane"},
        )

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# DELETE /api/contacts/{id}   — delete_contact
# ---------------------------------------------------------------------------

def test_delete_contact_success(client, access_token, user):
    mock_user = _mock_user(user)
    mock_service = AsyncMock(return_value=None)

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.delete_contact", mock_service):

        response = client.delete(
            "/api/contacts/1",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 204


def test_delete_contact_not_found(client, access_token, user):
    from fastapi import HTTPException
    mock_user = _mock_user(user)
    mock_service = AsyncMock(side_effect=HTTPException(status_code=404, detail="Not found"))

    with patch("src.routes.contacts.auth_service.get_current_user", return_value=mock_user), \
         patch("src.routes.contacts.ContactService.delete_contact", mock_service):

        response = client.delete(
            "/api/contacts/999",
            headers=_auth_headers(access_token),
        )

    assert response.status_code == 404
