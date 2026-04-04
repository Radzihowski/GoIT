"""
Unit tests for src/services/auth.py  — target: >75% coverage
Missing lines: 27, 30, 42, 53, 66, 71-103, 117-119
"""
import pickle
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from fastapi import HTTPException

from src.services.auth import Auth
from src.database.models import User


class TestAuthService(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.auth = Auth()
        # replace real Redis with a mock so no network call is made
        self.auth.r = MagicMock()

    # ------------------------------------------------------------------ #
    # add_token_to_blacklist  (line 27)
    # ------------------------------------------------------------------ #
    def test_add_token_to_blacklist(self):
        self.auth.add_token_to_blacklist("mytoken")
        self.auth.r.set.assert_called_once()

    # ------------------------------------------------------------------ #
    # is_token_in_blacklist  (line 30)
    # ------------------------------------------------------------------ #
    def test_is_token_in_blacklist_true(self):
        self.auth.r.get.return_value = b"mytoken"
        self.assertTrue(self.auth.is_token_in_blacklist("mytoken"))

    def test_is_token_in_blacklist_false(self):
        self.auth.r.get.return_value = None
        self.assertFalse(self.auth.is_token_in_blacklist("mytoken"))

    # ------------------------------------------------------------------ #
    # verify_password / get_password_hash
    # ------------------------------------------------------------------ #
    def test_verify_password_correct(self):
        hashed = self.auth.get_password_hash("secret")
        self.assertTrue(self.auth.verify_password("secret", hashed))

    def test_verify_password_wrong(self):
        hashed = self.auth.get_password_hash("secret")
        self.assertFalse(self.auth.verify_password("wrong", hashed))

    # ------------------------------------------------------------------ #
    # create_access_token  (line 42 — with expires_delta branch)
    # ------------------------------------------------------------------ #
    async def test_create_access_token_default_expiry(self):
        token = await self.auth.create_access_token(data={"sub": "test@test.com"})
        self.assertIsInstance(token, str)
        self.assertTrue(len(token) > 0)

    async def test_create_access_token_custom_expiry(self):
        # covers line 42 — the expires_delta branch
        token = await self.auth.create_access_token(
            data={"sub": "test@test.com"}, expires_delta=300
        )
        self.assertIsInstance(token, str)

    # ------------------------------------------------------------------ #
    # create_refresh_token  (line 53 — with expires_delta branch)
    # ------------------------------------------------------------------ #
    async def test_create_refresh_token_default_expiry(self):
        token = await self.auth.create_refresh_token(data={"sub": "test@test.com"})
        self.assertIsInstance(token, str)

    async def test_create_refresh_token_custom_expiry(self):
        # covers line 53 — the expires_delta branch
        token = await self.auth.create_refresh_token(
            data={"sub": "test@test.com"}, expires_delta=600
        )
        self.assertIsInstance(token, str)

    # ------------------------------------------------------------------ #
    # decode_refresh_token  (line 66 — wrong scope branch)
    # ------------------------------------------------------------------ #
    async def test_decode_refresh_token_success(self):
        token = await self.auth.create_refresh_token(data={"sub": "test@test.com"})
        email = await self.auth.decode_refresh_token(token)
        self.assertEqual(email, "test@test.com")

    async def test_decode_refresh_token_wrong_scope(self):
        # covers line 66 — token has access_token scope, not refresh_token
        token = await self.auth.create_access_token(data={"sub": "test@test.com"})
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.decode_refresh_token(token)
        self.assertEqual(ctx.exception.status_code, 401)

    async def test_decode_refresh_token_invalid(self):
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.decode_refresh_token("invalid.token")
        self.assertEqual(ctx.exception.status_code, 401)

    # ------------------------------------------------------------------ #
    # get_current_user  (lines 71-103)
    # ------------------------------------------------------------------ #
    async def test_get_current_user_blacklisted_token(self):
        # covers line 77-78 — token in blacklist
        self.auth.r.get.return_value = b"token"
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.get_current_user("sometoken")
        self.assertEqual(ctx.exception.status_code, 401)
        self.assertIn("revoked", ctx.exception.detail)

    async def test_get_current_user_invalid_token(self):
        # covers lines 88-89 — JWTError path
        self.auth.r.get.return_value = None
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.get_current_user("bad.token.value")
        self.assertEqual(ctx.exception.status_code, 401)

    async def test_get_current_user_wrong_scope(self):
        # covers lines 86-87 — token scope is not access_token
        self.auth.r.get.return_value = None
        refresh_token = await self.auth.create_refresh_token(data={"sub": "a@a.com"})
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.get_current_user(refresh_token)
        self.assertEqual(ctx.exception.status_code, 401)

    async def test_get_current_user_from_cache(self):
        # covers lines 100-103 — user found in Redis cache
        user = User(id=1, email="cached@test.com")
        self.auth.r.get.side_effect = [
            None,           # first call: is_token_in_blacklist → not blacklisted
            pickle.dumps(user),  # second call: r.get(f"user:{email}") → cache hit
        ]
        token = await self.auth.create_access_token(data={"sub": "cached@test.com"})

        result = await self.auth.get_current_user(token)
        self.assertEqual(result.email, "cached@test.com")

    async def test_get_current_user_from_db_not_found(self):
        # covers lines 92-96 — user not in cache, not in DB
        self.auth.r.get.return_value = None
        token = await self.auth.create_access_token(data={"sub": "ghost@test.com"})

        with patch(
            "src.services.auth.repository_users.get_user_by_email",
            new=AsyncMock(return_value=None),
        ):
            with self.assertRaises(HTTPException) as ctx:
                await self.auth.get_current_user(token)
        self.assertEqual(ctx.exception.status_code, 401)

    async def test_get_current_user_from_db_found(self):
        # covers lines 92-99 — user not in cache, found in DB, saved to cache
        user = User(id=1, email="db@test.com")
        self.auth.r.get.return_value = None
        token = await self.auth.create_access_token(data={"sub": "db@test.com"})

        with patch(
            "src.services.auth.repository_users.get_user_by_email",
            new=AsyncMock(return_value=user),
        ):
            result = await self.auth.get_current_user(token)

        self.assertEqual(result.email, "db@test.com")
        self.auth.r.set.assert_called_once()
        self.auth.r.expire.assert_called_once()

    # ------------------------------------------------------------------ #
    # create_email_token
    # ------------------------------------------------------------------ #
    def test_create_email_token(self):
        token = self.auth.create_email_token({"sub": "a@a.com"})
        self.assertIsInstance(token, str)

    # ------------------------------------------------------------------ #
    # get_email_from_token  (lines 117-119 — invalid token branch)
    # ------------------------------------------------------------------ #
    async def test_get_email_from_token_success(self):
        token = self.auth.create_email_token({"sub": "verify@test.com"})
        email = await self.auth.get_email_from_token(token)
        self.assertEqual(email, "verify@test.com")

    async def test_get_email_from_token_invalid(self):
        # covers lines 117-119
        with self.assertRaises(HTTPException) as ctx:
            await self.auth.get_email_from_token("bad.token")
        self.assertEqual(ctx.exception.status_code, 422)


if __name__ == "__main__":
    unittest.main()
