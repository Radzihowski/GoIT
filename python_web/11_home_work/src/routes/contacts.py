from typing import List

from fastapi import APIRouter, status, Query

from src.schemas.contacts import ContactInfo, ContactUpdateRequest
# from sqlalchemy.orm import Session
from src.schemas.contacts import ContactRequest, ContactResponse
from src.services.contacts import ContactService

router = APIRouter(prefix='/contacts', tags=["contacts"])

@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactRequest):
    service = ContactService()
    response = await service.create_contact(body)
    print(response)
    return response


@router.get("/", response_model=List[ContactInfo])
async def read_contacts(skip: int = 0, limit: int = 100):
    service = ContactService()
    response = await service.read_contacts(skip, limit)
    print(response)
    return response

@router.get("/search", response_model=List[ContactInfo])
async def search_contacts(skip: int = 0, limit: int = 100,
                          first_name: str | None =Query(default=None),
                          last_name: str | None =Query(default=None),
                          email: str | None =Query(default=None)):
    service = ContactService()
    response = await service.search_contacts(skip, limit, first_name, last_name, email)
    print(response)
    return response

@router.get("/{contact_id}", response_model=ContactInfo)
async def read_contact(contact_id: int):
    service = ContactService()
    response = await service.read_contact(contact_id)
    print(response)
    return response


@router.put("/{contact_id}", response_model=ContactInfo)
async def update_contact(contact_id: int, body: ContactUpdateRequest):
    service = ContactService()
    response = await service.update_contact(contact_id, body)
    print(response)
    return response


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int):
    service = ContactService()
    await service.delete_contact(contact_id)


