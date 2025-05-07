from src.repository.contacts import ContactCRUD

class ContactService:

    def __init__(self):
        self.crud = ContactCRUD()
    async def create_contact(self, body):
        return await self.crud.create_contact(body)

