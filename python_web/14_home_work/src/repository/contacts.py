from datetime import datetime, timedelta

from sqlalchemy import select, exists, delete, or_, func

from src.database.db import sessionmanager
from src.database.models import Contact
from src.schemas.contacts import ContactUpdateRequest


class ContactCRUD:
    """
    CRUD operations for Contact model, including creation, reading, updating, deleting,
    searching, and finding upcoming birthdays for contacts.
    """

    @staticmethod
    async def create_contact(body, user_id: int):
        """
        Create a new contact for a user.

        Args:
            body: Contact creation request data.
            user_id (int): The ID of the user to associate the contact with.

        Returns:
            int: The ID of the newly created contact.
        """
        async with sessionmanager.session() as session:
            async with session.begin():
                new_user = Contact(first_name=body.first_name, last_name=body.last_name,
                                   email=body.email, phone=body.phone, date_of_birth=body.date_of_birth,
                                   info=body.info, user_id=user_id)
                await session.add(new_user)
                await session.flush()
                user_id = new_user.id
            print(f"User {body.first_name} added successfully!")
            return user_id

    @staticmethod
    async def read_contact(contact_id: int, user_id: int):
        """
        Retrieve a contact by its ID and user ID.

        Args:
            contact_id (int): The ID of the contact to retrieve.
            user_id (int): The ID of the user who owns the contact.

        Returns:
            Contact or None: The contact object if found, else None.
        """
        async  with sessionmanager.session() as session:
            query = select(Contact).where(Contact.id == contact_id, Contact.user_id==user_id)
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()

    @staticmethod
    async def read_contacts(skip: int, limit: int, user_id: int):
        """
        Retrieve a list of contacts for a user with pagination.

        Args:
            skip (int): Number of records to skip.
            limit (int): Maximum number of records to return.
            user_id (int): The ID of the user whose contacts to retrieve.

        Returns:
            Sequence[Contact]: List of contact objects.
        """
        async with sessionmanager.session() as session:
            query = select(Contact).where(Contact.user_id==user_id).offset(skip).limit(limit)
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalars()

    @staticmethod
    async def delete_contact(contact_id: int, user_id: int):
        """
        Delete a contact by its ID and user ID.

        Args:
            contact_id (int): The ID of the contact to delete.
            user_id (int): The ID of the user who owns the contact.

        Returns:
            int: Number of rows deleted (0 or 1).
        """
        async with sessionmanager.session() as session:
            query = delete(Contact).where(Contact.id == contact_id, Contact.user_id==user_id)
            print(query)
            result = await session.execute(query)
            print(result)
            await session.commit()
            return result.rowcount

    @staticmethod
    async def check_email(email):
        """
        Check if a contact with the given email exists.

        Args:
            email (str): The email address to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """
        async with sessionmanager.session() as session:
            query = select(exists().where(Contact.email==email))
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()

    @staticmethod
    async def update_contact(contact_id, body: ContactUpdateRequest, user_id: int):
        """
        Update an existing contact's information.

        Args:
            contact_id (int): The ID of the contact to update.
            body (ContactUpdateRequest): The updated contact data.
            user_id (int): The ID of the user who owns the contact.

        Returns:
            Contact or None: The updated contact object if found, else None.
        """
        async with sessionmanager.session() as session:
            query = select(Contact).where(Contact.id == contact_id, Contact.user_id==user_id)
            result = await session.execute(query)
            print(result)
            contact = result.scalar()
            print(f"{contact=}")
            if contact is None:
                return None
            if body.first_name != "":
                contact.first_name = body.first_name
            if body.last_name != "":
                contact.last_name = body.last_name
            if body.email != "":
                contact.email = body.email
            if body.date_of_birth != datetime.today().date():
                contact.date_of_birth = body.date_of_birth
            print(datetime.today().date())
            if body.info != "":
                contact.info = body.info
            await session.commit()
            result = await session.execute(query)
            print(result)
            print(contact)
            return result.scalar()

    @staticmethod
    async def search_contacts(skip: int, limit: int, first_name: str, last_name: str, email: str, user_id: int):
        """
        Search for contacts by first name, last name, or email for a user with pagination.

        Args:
            skip (int): Number of records to skip.
            limit (int): Maximum number of records to return.
            first_name (str): First name filter (partial match).
            last_name (str): Last name filter (partial match).
            email (str): Email filter (partial match).
            user_id (int): The ID of the user whose contacts to search.

        Returns:
            List[Contact]: List of matching contact objects.
        """
        async  with (sessionmanager.session() as session):
            filters = [Contact.user_id==user_id]
            if first_name:
                filters.append(Contact.first_name.ilike(f"%{first_name}%"))
            if last_name:
                filters.append(Contact.last_name.ilike(f"%{last_name}%"))
            if email:
                filters.append(Contact.email.ilike(f"%{email}%"))

            query = select(Contact)
            if filters:
                query = query.where(or_(*filters))

            query = query.offset(skip).limit(limit).order_by(Contact.id)

            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def upcoming_dob(skip: int, limit: int, days_range: int, user_id: int):
        """
        Retrieve contacts with upcoming birthdays within a given range of days for a user.

        Args:
            skip (int): Number of records to skip.
            limit (int): Maximum number of records to return.
            days_range (int): Number of days ahead to look for birthdays.
            user_id (int): The ID of the user whose contacts to check.

        Returns:
            List[Contact]: List of contacts with upcoming birthdays.
        """
        async with sessionmanager.session() as session:
            today = datetime.today().date()
            target = today + timedelta(days=days_range)

            today_str = today.strftime('%m-%d')
            target_str = target.strftime('%m-%d')
            print(today_str)
            print(target_str)
            dob_md = func.to_char(Contact.date_of_birth, 'MM-DD')
            print(dob_md)
            if today_str < target_str:
                # Range within same year
                query = select(Contact).where(
                    Contact.user_id==user_id, dob_md.between(today_str, target_str)
                )
            else:
                # Wraps over end of year (e.g., Dec 30 to Jan 5)
                query = select(Contact).where(
                    Contact.user_id==user_id, (dob_md >= today_str) | (dob_md <= target_str)
                )

            query = query.offset(skip).limit(limit).order_by(Contact.id)

            result = await session.execute(query)
            return result.scalars().all()
