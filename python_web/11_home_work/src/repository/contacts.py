from sqlalchemy import select, exists, delete, or_

from src.database.db import sessionmanager
from src.database.models import Contact
from src.schemas.contacts import ContactUpdateRequest
from datetime import datetime

class ContactCRUD:
    # Function to add a user to the database
    async def create_contact(self, body):
        async with sessionmanager.session() as session:
            async with session.begin():
                new_user = Contact(first_name=body.first_name, last_name=body.last_name,
                                   email=body.email, phone=body.phone, date_of_birth=body.date_of_birth,
                                   info=body.info)
                session.add(new_user)
                await session.flush()
                user_id = new_user.id
            print(f"User {body.first_name} added successfully!")
            return user_id
    async def read_contact(self, contact_id:int):
        async  with sessionmanager.session() as session:
            query = select(Contact).where(Contact.id == contact_id)
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()
    async def read_contacts(self, skip:int, limit:int):
        async  with sessionmanager.session() as session:
            query = select(Contact).offset(skip).limit(limit)
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalars()

    async def delete_contact(self, contact_id:int):
        async  with sessionmanager.session() as session:
            query = delete(Contact).where(Contact.id == contact_id)
            print(query)
            result = await session.execute(query)
            print(result)
            await session.commit()
            return result.rowcount

    async def check_email(self, email):
        async with sessionmanager.session() as session:
            query = select(exists().where(Contact.email==email))
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()

    async def update_contact(self, contact_id, body: ContactUpdateRequest):
        async with sessionmanager.session() as session:
            query = select(Contact).where(Contact.id == contact_id)
            print(query)
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

    async def search_contacts(self, skip:int, limit:int, first_name:str, last_name:str, email:str):
        async  with (sessionmanager.session() as session):
            filters = []
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
