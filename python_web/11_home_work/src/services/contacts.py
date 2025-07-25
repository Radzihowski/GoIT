from src.repository.contacts import ContactCRUD
from src.schemas.contacts import ContactUpdateRequest
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


    async def read_contact(self, contact_id:int):
        result = await self.crud.read_contact(contact_id)
        print(result)
        if result is None:
            raise HTTPException(status_code=404, detail="Contact doesn't exists with such ID")
        return result

    async def read_contacts(self, skip:int, limit:int):
        result = await self.crud.read_contacts(skip, limit)
        print(result)
        return result

    async def delete_contact(self, contact_id:int):
        result = await self.crud.delete_contact(contact_id)
        print(result)
        if result == 0:
            raise HTTPException(status_code=404, detail="Contact doesn't exists with such ID")

    async def update_contact(self, contact_id:int, body: ContactUpdateRequest):
        result = await self.crud.update_contact(contact_id, body)
        if result is None:
            raise HTTPException(status_code=404, detail="Contact doesn't exists with such ID")
        return result

    async def search_contacts(self, skip:int, limit:int, first_name:str, last_name:str, email:str):
        result = await self.crud.search_contacts(skip, limit, first_name, last_name, email)
        print(result)
        return result