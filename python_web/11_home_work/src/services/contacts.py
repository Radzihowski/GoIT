from src.repository.contacts import ContactCRUD
from fastapi import HTTPException
class ContactService:

    def __init__(self):
        self.crud = ContactCRUD()
    async def create_contact(self, body):
        email_exists_in_db = await self.crud.check_email(body.email)
        print(email_exists_in_db)
        if email_exists_in_db:
            raise HTTPException(status_code=409, detail="Contact with this email already exists.")

        result = await self.crud.create_contact(body)
        return {"id": result}

