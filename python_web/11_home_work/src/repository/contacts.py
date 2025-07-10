from src.database.db import sessionmanager
from src.database.models import Contact
from sqlalchemy import select, exists
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
    async def read_contact(self, body) # TODO add this next
        ...

    async def update_contact(self, body):
        ...

    async def delete_contact(self, body):
        ...

    async def check_email(self, email):
        async with sessionmanager.session() as session:
            query = select(exists().where(Contact.email==email))
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()
