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

    @patch('src.repository.contacts.sessionmanager')
    async def test_search_contacts_by_first_name(self, mock_sessionmanager):
        # Create test contacts
        contacts = [
            Contact(id=1, first_name="John", last_name="Doe", email="john@test.com"),
            Contact(id=2, first_name="Johnny", last_name="Smith", email="johnny@test.com"),
        ]

        # Setup mock using fixture
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        # Call the method under test — filter by first_name only
        result = await self.crud.search_contacts(
            skip=0, limit=10,
            first_name="John", last_name="", email="",
            user_id=self.user.id
        )

        # Assert the result
        self.assertEqual(result, contacts)

        # Verify session interactions
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()
        mock_result.scalars.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_search_contacts_by_last_name(self, mock_sessionmanager):
        contacts = [
            Contact(id=1, first_name="John", last_name="Doe", email="john@test.com"),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        result = await self.crud.search_contacts(
            skip=0, limit=10,
            first_name="", last_name="Doe", email="",
            user_id=self.user.id
        )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_search_contacts_by_email(self, mock_sessionmanager):
        contacts = [
            Contact(id=1, first_name="John", last_name="Doe", email="john@test.com"),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        result = await self.crud.search_contacts(
            skip=0, limit=10,
            first_name="", last_name="", email="john@test.com",
            user_id=self.user.id
        )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_search_contacts_no_filters_returns_all(self, mock_sessionmanager):
        """When all filters are empty, should return all contacts for the user."""
        contacts = [
            Contact(id=1, first_name="Alice", last_name="Smith", email="alice@test.com"),
            Contact(id=2, first_name="Bob", last_name="Jones", email="bob@test.com"),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        result = await self.crud.search_contacts(
            skip=0, limit=10,
            first_name="", last_name="", email="",
            user_id=self.user.id
        )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_search_contacts_returns_empty_list(self, mock_sessionmanager):
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = []

        result = await self.crud.search_contacts(
            skip=0, limit=10,
            first_name="NonExistent", last_name="", email="",
            user_id=self.user.id
        )

        self.assertEqual(result, [])
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_upcoming_dob_within_same_year(self, mock_sessionmanager):
        """Test upcoming birthdays when range stays within the same year (no year wrap)."""
        contacts = [
            Contact(id=1, first_name="John", last_name="Doe",
                    email="john@test.com", date_of_birth=date(1990, 4, 1)),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        # days_range=7 from today (2026-03-28) stays within the same year: 03-28 to 04-04
        result = await self.crud.upcoming_dob(
            skip=0, limit=10,
            days_range=7,
            user_id=self.user.id
        )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()
        mock_result.scalars.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_upcoming_dob_wraps_over_year_end(self, mock_sessionmanager):
        """Test upcoming birthdays when the range wraps over Dec 31 → Jan 1."""
        contacts = [
            Contact(id=1, first_name="Eve", last_name="Winter",
                    email="eve@test.com", date_of_birth=date(1985, 1, 2)),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        # Patch datetime.today() inside the method so the range wraps over year end
        with patch('src.repository.contacts.datetime') as mock_dt:
            from datetime import date as real_date, datetime as real_datetime
            mock_dt.today.return_value = real_datetime(2025, 12, 28)
            mock_dt.side_effect = lambda *a, **kw: real_datetime(*a, **kw)

            result = await self.crud.upcoming_dob(
                skip=0, limit=10,
                days_range=7,
                user_id=self.user.id
            )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_upcoming_dob_returns_empty_list(self, mock_sessionmanager):
        """Test that an empty list is returned when no birthdays are upcoming."""
        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = []

        result = await self.crud.upcoming_dob(
            skip=0, limit=10,
            days_range=7,
            user_id=self.user.id
        )

        self.assertEqual(result, [])
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()

    @patch('src.repository.contacts.sessionmanager')
    async def test_upcoming_dob_pagination(self, mock_sessionmanager):
        """Test that skip/limit pagination parameters are respected."""
        contacts = [
            Contact(id=2, first_name="Bob", last_name="Doe",
                    email="bob@test.com", date_of_birth=date(1992, 4, 2)),
        ]

        mock_session, mock_result = self.setup_async_session_mock(mock_sessionmanager)
        mock_result.scalars.return_value.all.return_value = contacts

        result = await self.crud.upcoming_dob(
            skip=1, limit=1,
            days_range=14,
            user_id=self.user.id
        )

        self.assertEqual(result, contacts)
        mock_sessionmanager.session.assert_called_once()
        mock_session.execute.assert_called_once()


if __name__ == '__main__':
    unittest.main()

