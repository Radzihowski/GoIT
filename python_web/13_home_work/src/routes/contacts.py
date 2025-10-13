from typing import List

from fastapi import APIRouter, status, Query, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.repository import users as repository_users
from src.services.auth import auth_service

from src.schemas.contacts import ContactInfo, ContactUpdateRequest
# from sqlalchemy.orm import Session
from src.schemas.contacts import ContactRequest, ContactResponse
from src.services.contacts import ContactService

router = APIRouter(prefix='/contacts', tags=["contacts"])
security = HTTPBearer()
@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactRequest, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.create_contact(body, user_id=user.id)
    print(response)
    return response


@router.get("/", response_model=List[ContactInfo])
async def read_contacts(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.read_contacts(skip, limit, user_id=user.id)
    print(response)
    return response

@router.get("/search", response_model=List[ContactInfo])
async def search_contacts(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100,
                          first_name: str | None =Query(default=None),
                          last_name: str | None =Query(default=None),
                          email: str | None =Query(default=None)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.search_contacts(skip, limit, first_name, last_name, email, user_id=user.id)
    print(response)
    return response

@router.get("/upcoming_dob", response_model=List[ContactInfo])
async def upcoming_dob(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100,
                          days_range: int=Query(default=7, gt=1)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.upcoming_dob(skip, limit, days_range, user_id=user.id)
    print(response)
    return response

@router.get("/{contact_id}", response_model=ContactInfo)
async def read_contact(contact_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.read_contact(contact_id, user_id=user.id)
    print(response)
    return response


@router.put("/{contact_id}", response_model=ContactInfo)
async def update_contact(contact_id: int, body: ContactUpdateRequest, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.update_contact(contact_id, body, user_id=user.id)
    print(response)
    return response


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    await service.delete_contact(contact_id, user_id=user.id)


