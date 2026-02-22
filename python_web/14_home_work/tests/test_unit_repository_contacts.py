import unittest
from unittest.mock import MagicMock
from datetime import date

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

    def assert_called_n_times(self, mock_method, expected_count):
        """
        Helper method to assert that a mock method was called exactly n times.

        Args:
            mock_method: The mock method to check
            expected_count: Expected number of calls
        """
        actual_count = mock_method.call_count
        self.assertEqual(
            actual_count,
            expected_count,
            f"Expected {expected_count} calls, but got {actual_count}"
        )

    def setup_async_session_mock(self, mock_sessionmanager, return_data=None):
        """
        Fixture to setup async session mocking for SQLAlchemy 2.0 style operations.

        Args:
            mock_sessionmanager: The mocked sessionmanager object
            return_data: Data to be returned by the mocked query operation

        Returns:
            tuple: (mock_session, mock_result) for additional customization if needed
        """
        # Create mock session and result objects
        mock_session = AsyncMock()
        mock_result = MagicMock()

        # Setup the async context manager properly
        async_context = AsyncMock()
        async_context.__aenter__.return_value = mock_session
        async_context.__aexit__.return_value = None
        mock_sessionmanager.session.return_value = async_context

        # Mock the session.execute() method to return our mock result
        mock_session.execute.return_value = mock_result

        # Mock the begin() transaction context manager properly
        mock_session.begin = MagicMock()
        mock_session.begin.return_value.__aenter__ = AsyncMock(return_value=None)
        mock_session.begin.return_value.__aexit__ = AsyncMock(return_value=None)

        # Set return data if provided
        if return_data is not None:
            mock_result.scalars.return_value = return_data
            mock_result.scalar.return_value = return_data[0] if return_data else None

        return mock_session, mock_result

    @patch('src.repository.contacts.sessionmanager')
    async def test_read_contacts(self, mock_sessionmanager):
        # Create test contacts
        contacts = [Contact(), Contact(), Contact()]

        # Setup mock using fixture
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager, contacts)

        # Call the method under test
        result = await self.crud.read_contacts(skip=0, limit=10, user_id=self.user.id)

        # Assert the result
        self.assertEqual(result, contacts)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_read_contact(self, mock_sessionmanager):
        # Create test contact
        contact = Contact(id=1, first_name="John", last_name="Doe", email="john@test.com")

        # Setup mock using fixture - for single result operations
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager, [contact])

        # Call the method under test
        result = await self.crud.read_contact(contact_id=1, user_id=self.user.id)

        # Assert the result
        self.assertEqual(result, contact)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    @patch('src.repository.contacts.Contact')
    async def test_create_contact(self, mock_contact_class, mock_sessionmanager):
        # Setup mock using fixture - for create operations, we don't need return data
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)

        # Mock the flush operation
        mock_session.flush.return_value = None
        mock_session.add.return_value = None

        # Mock the Contact instance and its ID
        mock_contact_instance = MagicMock()
        mock_contact_instance.id = 123  # Mock the ID that gets set after flush
        mock_contact_class.return_value = mock_contact_instance

        # Create test contact data
        contact_data = ContactRequest(
            first_name="John",
            last_name="Doe",
            email="john@test.com",
            phone="123-456-7890",
            date_of_birth="1990-01-01",
            info="Test contact"
        )

        # Call the method under test
        result = await self.crud.create_contact(body=contact_data, user_id=self.user.id)

        # Assert the result (should return the contact ID)
        self.assertEqual(result, 123)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()

        # Verify the Contact was instantiated with correct data
        mock_contact_class.assert_called_once_with(
            first_name="John",
            last_name="Doe",
            email="john@test.com",
            phone="123-456-7890",
            date_of_birth=date(1990, 1, 1),
            info="Test contact",
            user_id=self.user.id
        )

    @patch('src.repository.contacts.sessionmanager')
    async def test_delete_contact(self, mock_sessionmanager):
        # Setup mock using fixture
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)

        # Mock the rowcount for delete operations
        mock_result.rowcount = 1
        mock_session.commit.return_value = None

        # Call the method under test
        result = await self.crud.delete_contact(contact_id=1, user_id=self.user.id)

        # Assert the result (number of deleted rows)
        self.assertEqual(result, 1)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_check_email(self, mock_sessionmanager):
        bool_result = True  # Assuming the email exists for this test
        # Setup mock using fixture
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager, [bool_result])

        # Call the method under test
        result = await self.crud.check_email(email="test@test.com")

        # Assert the result (number of deleted rows)
        self.assertEqual(result, bool_result)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_update_contact(self, mock_sessionmanager):
        # Create test contact data
        contact_data = ContactUpdateRequest(
            first_name="John",
            last_name="Doe",
            email="john@test.com",
            phone="123-456-7890",
            date_of_birth="1990-01-01",
            info="Test contact"
        )

        # Create test contact
        contact = Contact(id=1, first_name="John", last_name="Doe", email="john@test.com")

        # Setup mock using fixture
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)

        # Mock update operations - need to handle two execute calls
        mock_result1 = MagicMock()
        mock_result2 = MagicMock()

        # First execute (to find contact) returns the contact
        mock_result1.scalar.return_value = contact
        # Second execute (after update) returns the updated contact
        mock_result2.scalar.return_value = contact

        # Set up execute to return different results for each call
        mock_session.execute.side_effect = [mock_result1, mock_result2]
        mock_session.commit.return_value = None

        # Call the method under test
        result = await self.crud.update_contact(contact_id=1, body=contact_data, user_id=self.user.id)

        # Assert the result
        self.assertEqual(result, contact)

        # Verify the session manager was called correctly
        mock_sessionmanager.session.assert_called_once()
        self.assert_called_n_times(mock_session.execute, 2)  # Called twice: select and after update
        mock_session.commit.assert_called_once()
        # Verify scalar was called on both result objects
        mock_result1.scalar.assert_called_once()
        mock_result2.scalar.assert_called_once()

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

