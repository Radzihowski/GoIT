"""
Unit tests for src/services/contacts.py  — target: 100% coverage
Missing lines: 9-15, 19-23, 26-28, 31-34, 37-40, 43-45, 48-50
"""
import unittest
from unittest.mock import AsyncMock, MagicMock
from fastapi import HTTPException

from src.services.contacts import ContactService
from src.database.models import Contact


class TestContactService(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.service = ContactService()          # covers line 7
        self.service.crud = MagicMock()          # replace real CRUD with mock
        self.user_id = 1

    # ------------------------------------------------------------------ #
    # create_contact  (lines 9-15)
    # ------------------------------------------------------------------ #
    async def test_create_contact_email_already_exists(self):
        self.service.crud.check_email = AsyncMock(return_value=True)

        with self.assertRaises(HTTPException) as ctx:
            await self.service.create_contact(
                MagicMock(email="exists@test.com"), user_id=self.user_id
            )
        self.assertEqual(ctx.exception.status_code, 409)

    async def test_create_contact_success(self):
        self.service.crud.check_email = AsyncMock(return_value=False)
        self.service.crud.create_contact = AsyncMock(return_value=42)

        result = await self.service.create_contact(
            MagicMock(email="new@test.com"), user_id=self.user_id
        )
        self.assertEqual(result, {"id": 42})

    # ------------------------------------------------------------------ #
    # read_contact  (lines 19-23)
    # ------------------------------------------------------------------ #
    async def test_read_contact_not_found(self):
        self.service.crud.read_contact = AsyncMock(return_value=None)

        with self.assertRaises(HTTPException) as ctx:
            await self.service.read_contact(contact_id=99, user_id=self.user_id)
        self.assertEqual(ctx.exception.status_code, 404)

    async def test_read_contact_found(self):
        contact = Contact(id=1, first_name="John")
        self.service.crud.read_contact = AsyncMock(return_value=contact)

        result = await self.service.read_contact(contact_id=1, user_id=self.user_id)
        self.assertEqual(result, contact)

    # ------------------------------------------------------------------ #
    # read_contacts  (lines 26-28)
    # ------------------------------------------------------------------ #
    async def test_read_contacts(self):
        contacts = [Contact(id=1), Contact(id=2)]
        self.service.crud.read_contacts = AsyncMock(return_value=contacts)

        result = await self.service.read_contacts(skip=0, limit=10, user_id=self.user_id)
        self.assertEqual(result, contacts)

    # ------------------------------------------------------------------ #
    # delete_contact  (lines 31-34)
    # ------------------------------------------------------------------ #
    async def test_delete_contact_not_found(self):
        self.service.crud.delete_contact = AsyncMock(return_value=0)

        with self.assertRaises(HTTPException) as ctx:
            await self.service.delete_contact(contact_id=99, user_id=self.user_id)
        self.assertEqual(ctx.exception.status_code, 404)

    async def test_delete_contact_success(self):
        self.service.crud.delete_contact = AsyncMock(return_value=1)
        await self.service.delete_contact(contact_id=1, user_id=self.user_id)

    # ------------------------------------------------------------------ #
    # update_contact  (lines 37-40)
    # ------------------------------------------------------------------ #
    async def test_update_contact_not_found(self):
        self.service.crud.update_contact = AsyncMock(return_value=None)

        with self.assertRaises(HTTPException) as ctx:
            await self.service.update_contact(
                contact_id=99, body=MagicMock(), user_id=self.user_id
            )
        self.assertEqual(ctx.exception.status_code, 404)

    async def test_update_contact_success(self):
        contact = Contact(id=1, first_name="Updated")
        self.service.crud.update_contact = AsyncMock(return_value=contact)

        result = await self.service.update_contact(
            contact_id=1, body=MagicMock(), user_id=self.user_id
        )
        self.assertEqual(result, contact)

    # ------------------------------------------------------------------ #
    # search_contacts  (lines 43-45)
    # ------------------------------------------------------------------ #
    async def test_search_contacts(self):
        contacts = [Contact(id=1, first_name="John")]
        self.service.crud.search_contacts = AsyncMock(return_value=contacts)

        result = await self.service.search_contacts(
            skip=0, limit=10,
            first_name="John", last_name="", email="",
            user_id=self.user_id
        )
        self.assertEqual(result, contacts)

    async def test_search_contacts_empty(self):
        self.service.crud.search_contacts = AsyncMock(return_value=[])

        result = await self.service.search_contacts(
            skip=0, limit=10,
            first_name="Nobody", last_name="", email="",
            user_id=self.user_id
        )
        self.assertEqual(result, [])

    # ------------------------------------------------------------------ #
    # upcoming_dob  (lines 48-50)
    # ------------------------------------------------------------------ #
    async def test_upcoming_dob(self):
        contacts = [Contact(id=1, first_name="Birthday Person")]
        self.service.crud.upcoming_dob = AsyncMock(return_value=contacts)

        result = await self.service.upcoming_dob(
            skip=0, limit=10, days_range=7, user_id=self.user_id
        )
        self.assertEqual(result, contacts)

    async def test_upcoming_dob_empty(self):
        self.service.crud.upcoming_dob = AsyncMock(return_value=[])

        result = await self.service.upcoming_dob(
            skip=0, limit=10, days_range=7, user_id=self.user_id
        )
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
