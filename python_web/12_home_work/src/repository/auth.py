class ContactCRUD:
    # Function to add a user to the database
    async def read_contact(self, contact_id:int):
        async  with sessionmanager.session() as session:
            query = select(Contact).where(Contact.id == contact_id)
            print(query)
            result = await session.execute(query)
            print(result)
            return result.scalar()