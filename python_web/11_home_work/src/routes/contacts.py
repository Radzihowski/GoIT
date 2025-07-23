from typing import List

from fastapi import APIRouter, status

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