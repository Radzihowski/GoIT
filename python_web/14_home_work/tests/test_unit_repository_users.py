"""
Unit tests for src/repository/users.py
Missing lines before: 27, 45-50, 71, 83-90, 103-116
Target: 100% coverage
"""
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

from src.database.models import User
from src.schemas.users import UserModel
import src.repository.users as repository_users


def _make_session_mock(scalar_return=None):
    """Build a fully wired async session context-manager mock."""
    mock_result = MagicMock()
    mock_result.scalar.return_value = scalar_return

    # Use spec=None so AsyncMock does not auto-wire begin() as a coroutine
    mock_session = AsyncMock()
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()
    mock_session.flush = AsyncMock()
    mock_session.add = MagicMock()

    # nested transaction context manager: `async with session.begin()`
    # begin() must be a plain callable (not async) that returns an async CM
    mock_begin_ctx = MagicMock()
    mock_begin_ctx.__aenter__ = AsyncMock(return_value=None)
    mock_begin_ctx.__aexit__ = AsyncMock(return_value=None)
    # override the AsyncMock-generated begin with a plain MagicMock
    mock_session.begin = MagicMock(return_value=mock_begin_ctx)

    # outer context manager: `async with sessionmanager.session() as session`
    mock_ctx = MagicMock()
    mock_ctx.__aenter__ = AsyncMock(return_value=mock_session)
    mock_ctx.__aexit__ = AsyncMock(return_value=None)

    return mock_session, mock_ctx


class TestGetUserByEmail(unittest.IsolatedAsyncioTestCase):

    @patch("src.repository.users.sessionmanager")
    async def test_returns_user_when_found(self, mock_sm):
        user = User(id=1, email="found@test.com")
        _, mock_ctx = _make_session_mock(scalar_return=user)
        mock_sm.session.return_value = mock_ctx

        result = await repository_users.get_user_by_email("found@test.com")

        self.assertEqual(result, user)

    @patch("src.repository.users.sessionmanager")
    async def test_returns_none_when_not_found(self, mock_sm):  # covers line 27
        _, mock_ctx = _make_session_mock(scalar_return=None)
        mock_sm.session.return_value = mock_ctx

        result = await repository_users.get_user_by_email("ghost@test.com")

        self.assertIsNone(result)


class TestCreateUser(unittest.IsolatedAsyncioTestCase):

    @patch("src.repository.users.sessionmanager")
    async def test_creates_user_and_returns_dict(self, mock_sm):  # covers lines 45-50
        mock_session, mock_ctx = _make_session_mock()
        mock_sm.session.return_value = mock_ctx

        # Simulate flush setting id/created_at on the new User object
        created_at = datetime(2024, 1, 1)

        async def fake_flush():
            # set attributes that are normally set by DB on flush
            pass

        mock_session.flush.side_effect = fake_flush

        # Patch User so we control what gets created
        mock_user_instance = MagicMock()
        mock_user_instance.id = 99
        mock_user_instance.email = "new@test.com"
        mock_user_instance.created_at = created_at
        mock_user_instance.avatar = None

        body = UserModel(email="new@test.com", password="hashed_pw")

        with patch("src.repository.users.User", return_value=mock_user_instance):
            result = await repository_users.create_user(body)

        self.assertEqual(result["id"], 99)
        self.assertEqual(result["email"], "new@test.com")
        self.assertEqual(result["created_at"], created_at)
        self.assertIsNone(result["avatar"])
        mock_session.add.assert_called_once_with(mock_user_instance)
        mock_session.flush.assert_called_once()


class TestUpdateToken(unittest.IsolatedAsyncioTestCase):

    @patch("src.repository.users.sessionmanager")
    async def test_update_token(self, mock_sm):  # covers line 71
        mock_session, mock_ctx = _make_session_mock()
        mock_sm.session.return_value = mock_ctx

        user = User(id=1, email="tok@test.com")
        await repository_users.update_token(user, "new-refresh-token")

        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()

    @patch("src.repository.users.sessionmanager")
    async def test_update_token_to_none(self, mock_sm):
        mock_session, mock_ctx = _make_session_mock()
        mock_sm.session.return_value = mock_ctx

        user = User(id=2, email="tok2@test.com")
        await repository_users.update_token(user, None)

        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()


class TestConfirmedEmail(unittest.IsolatedAsyncioTestCase):

    @patch("src.repository.users.sessionmanager")
    async def test_confirmed_email(self, mock_sm):  # covers lines 83-90
        mock_session, mock_ctx = _make_session_mock()
        mock_sm.session.return_value = mock_ctx

        await repository_users.confirmed_email("verify@test.com")

        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()


class TestUpdateAvatar(unittest.IsolatedAsyncioTestCase):

    @patch("src.repository.users.sessionmanager")
    async def test_update_avatar(self, mock_sm):  # covers lines 103-116
        user = User(
            id=1,
            email="avatar@test.com",
            created_at=datetime(2024, 1, 1),
            avatar="http://new-avatar.com",
        )

        # update_avatar calls sessionmanager once for UPDATE,
        # then calls get_user_by_email which uses sessionmanager a second time.
        # We provide the same ctx both times via side_effect.
        mock_session_update, mock_ctx_update = _make_session_mock()
        mock_session_get, mock_ctx_get = _make_session_mock(scalar_return=user)

        mock_sm.session.side_effect = [mock_ctx_update, mock_ctx_get]

        result = await repository_users.update_avatar("avatar@test.com", "http://new-avatar.com")

        self.assertEqual(result["email"], "avatar@test.com")
        self.assertEqual(result["avatar"], "http://new-avatar.com")
        self.assertEqual(result["id"], 1)
        mock_session_update.execute.assert_called_once()
        mock_session_update.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
