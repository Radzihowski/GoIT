import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas.contacts import ContactRequest, ContactResponse, ContactInfo, ContactUpdateRequest
from src.repository.contacts import ContactCRUD
from unittest.mock import patch, AsyncMock
class TestContacts(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1, email="test@test.com", password="password")
        self.crud = ContactCRUD()

    @patch('src.repository.contacts.sessionmanager')
    async def test_read_contacts(self, mock_sessionmanager):
        # Create mock session and result objects
        mock_session = AsyncMock()
        mock_result = MagicMock()

        # Setup the async context manager properly
        async_context = AsyncMock()
        async_context.__aenter__.return_value = mock_session
        async_context.__aexit__.return_value = None
        mock_sessionmanager.session.return_value = async_context

        # Create test contacts
        contacts = [Contact(), Contact(), Contact()]

        # Mock the session.execute() method to return our mock result
        mock_session.execute.return_value = mock_result
        # Mock the result.scalars() method to return our test contacts
        mock_result.scalars.return_value = contacts

        # Call the method under test
        result = await self.crud.read_contacts(skip=0, limit=10, user_id=self.user.id)

        # Assert the result
        self.assertEqual(result, contacts)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    # async def test_get_note_found(self):
    #     note = Note()
    #     self.session.query().filter().first.return_value = note
    #     result = await get_note(note_id=1, user=self.user, db=self.session)
    #     self.assertEqual(result, note)
    #
    # async def test_get_note_not_found(self):
    #     self.session.query().filter().first.return_value = None
    #     result = await get_note(note_id=1, user=self.user, db=self.session)
    #     self.assertIsNone(result)
    #
    # async def test_create_note(self):
    #     body = NoteModel(title="test", description="test note", tags=[1, 2])
    #     tags = [Tag(id=1, user_id=1), Tag(id=2, user_id=1)]
    #     self.session.query().filter().all.return_value = tags
    #     result = await create_note(body=body, user=self.user, db=self.session)
    #     self.assertEqual(result.title, body.title)
    #     self.assertEqual(result.description, body.description)
    #     self.assertEqual(result.tags, tags)
    #     self.assertTrue(hasattr(result, "id"))
    #
    # async def test_remove_note_found(self):
    #     note = Note()
    #     self.session.query().filter().first.return_value = note
    #     result = await remove_note(note_id=1, user=self.user, db=self.session)
    #     self.assertEqual(result, note)
    #
    # async def test_remove_note_not_found(self):
    #     self.session.query().filter().first.return_value = None
    #     result = await remove_note(note_id=1, user=self.user, db=self.session)
    #     self.assertIsNone(result)
    #
    # async def test_update_note_found(self):
    #     body = NoteUpdate(title="test", description="test note", tags=[1, 2], done=True)
    #     tags = [Tag(id=1, user_id=1), Tag(id=2, user_id=1)]
    #     note = Note(tags=tags)
    #     self.session.query().filter().first.return_value = note
    #     self.session.query().filter().all.return_value = tags
    #     self.session.commit.return_value = None
    #     result = await update_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertEqual(result, note)
    #
    # async def test_update_note_not_found(self):
    #     body = NoteUpdate(title="test", description="test note", tags=[1, 2], done=True)
    #     self.session.query().filter().first.return_value = None
    #     self.session.commit.return_value = None
    #     result = await update_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertIsNone(result)
    #
    # async def test_update_status_note_found(self):
    #     body = NoteStatusUpdate(done=True)
    #     note = Note()
    #     self.session.query().filter().first.return_value = note
    #     self.session.commit.return_value = None
    #     result = await update_status_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertEqual(result, note)
    #
    # async def test_update_status_note_not_found(self):
    #     body = NoteStatusUpdate(done=True)
    #     self.session.query().filter().first.return_value = None
    #     self.session.commit.return_value = None
    #     result = await update_status_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

