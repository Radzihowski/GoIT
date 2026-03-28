from typing import List
from src.utils.py_logger import get_logger

from fastapi import APIRouter, status, Query, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_limiter.depends import RateLimiter
from src.repository import users as repository_users
from src.services.auth import auth_service

from src.schemas.contacts import ContactInfo, ContactUpdateRequest
# from sqlalchemy.orm import Session
from src.schemas.contacts import ContactRequest, ContactResponse
from src.services.contacts import ContactService

logger = get_logger(__name__)
router = APIRouter(prefix='/contacts', tags=["contacts"])
security = HTTPBearer()
@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(RateLimiter(times=2, seconds=60))])
async def create_contact(body: ContactRequest, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Create a new contact for the authenticated user.

    Creates a new contact with the provided information and associates it with the current user.
    Rate limited to 2 requests per 60 seconds.

    Args:
        body (ContactRequest): The contact data to create including first name, last name,
            email, phone, date of birth, and additional info.
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.

    Returns:
        ContactResponse: The created contact information with ID and creation timestamp.

    Raises:
        HTTPException: 401 if authentication fails, 422 if contact data is invalid.

    Example:
        POST /contacts/
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "date_of_birth": "1990-01-01",
            "info": "Additional information"
        }
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.create_contact(body, user_id=user.id)
    print(response)
    return response


@router.get("/", response_model=List[ContactInfo],
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def read_contacts(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100):
    """
    Retrieve a paginated list of contacts for the authenticated user.

    Fetches contacts owned by the current user with pagination support.
    Rate limited to 5 requests per 60 seconds.

    Args:
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.
        skip (int, optional): Number of contacts to skip for pagination. Defaults to 0.
        limit (int, optional): Maximum number of contacts to return. Defaults to 100.

    Returns:
        List[ContactInfo]: List of contact information objects containing contact details.

    Raises:
        HTTPException: 401 if authentication fails.

    Example:
        GET /contacts/?skip=0&limit=10
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    logger.info(f"User ID: {user.id}")
    service = ContactService()
    response = await service.read_contacts(skip, limit, user_id=user.id)
    print(response)
    return response

@router.get("/search", response_model=List[ContactInfo],
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def search_contacts(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100,
                          first_name: str | None =Query(default=None),
                          last_name: str | None =Query(default=None),
                          email: str | None =Query(default=None)):
    """
    Search contacts by first name, last name, or email for the authenticated user.

    Performs a filtered search across the user's contacts using one or more criteria.
    At least one search parameter should be provided. Rate limited to 5 requests per 60 seconds.

    Args:
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.
        skip (int, optional): Number of contacts to skip for pagination. Defaults to 0.
        limit (int, optional): Maximum number of contacts to return. Defaults to 100.
        first_name (str | None, optional): Filter by first name (partial match). Defaults to None.
        last_name (str | None, optional): Filter by last name (partial match). Defaults to None.
        email (str | None, optional): Filter by email address (partial match). Defaults to None.

    Returns:
        List[ContactInfo]: List of contacts matching the search criteria.

    Raises:
        HTTPException: 401 if authentication fails.

    Example:
        GET /contacts/search?first_name=John&email=@example.com
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.search_contacts(skip, limit, first_name, last_name, email, user_id=user.id)
    print(response)
    return response

@router.get("/upcoming_dob", response_model=List[ContactInfo],
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def upcoming_dob(credentials: HTTPAuthorizationCredentials = Security(security), skip: int = 0, limit: int = 100,
                          days_range: int=Query(default=7, gt=1)):
    """
    Retrieve contacts with upcoming birthdays within a specified date range.

    Finds contacts whose birthdays fall within the next specified number of days.
    Useful for birthday reminders and planning. Rate limited to 5 requests per 60 seconds.

    Args:
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.
        skip (int, optional): Number of contacts to skip for pagination. Defaults to 0.
        limit (int, optional): Maximum number of contacts to return. Defaults to 100.
        days_range (int, optional): Number of days from today to search for birthdays.
            Must be greater than 1. Defaults to 7.

    Returns:
        List[ContactInfo]: List of contacts with birthdays in the specified range,
            ordered by upcoming birthday date.

    Raises:
        HTTPException: 401 if authentication fails, 422 if days_range <= 1.

    Example:
        GET /contacts/upcoming_dob?days_range=30
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.upcoming_dob(skip, limit, days_range, user_id=user.id)
    print(response)
    return response

@router.get("/{contact_id}", response_model=ContactInfo,
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def read_contact(contact_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Retrieve a specific contact by its ID for the authenticated user.

    Fetches detailed information for a single contact owned by the current user.
    Rate limited to 5 requests per 60 seconds.

    Args:
        contact_id (int): The unique identifier of the contact to retrieve.
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.

    Returns:
        ContactInfo: Detailed contact information including all fields.

    Raises:
        HTTPException: 401 if authentication fails, 404 if contact not found or
            not owned by the current user.

    Example:
        GET /contacts/123
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.read_contact(contact_id, user_id=user.id)
    print(response)
    return response


@router.put("/{contact_id}", response_model=ContactInfo,
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def update_contact(contact_id: int, body: ContactUpdateRequest, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Update an existing contact's information for the authenticated user.

    Updates the specified contact with new information. Only provided fields will be updated,
    empty or null fields will be ignored. Rate limited to 5 requests per 60 seconds.

    Args:
        contact_id (int): The unique identifier of the contact to update.
        body (ContactUpdateRequest): The contact data to update. Only non-empty fields
            will be applied to the contact.
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.

    Returns:
        ContactInfo: The updated contact information with all current values.

    Raises:
        HTTPException: 401 if authentication fails, 404 if contact not found or
            not owned by the current user, 422 if update data is invalid.

    Example:
        PUT /contacts/123
        {
            "first_name": "Jane",
            "email": "jane.doe@example.com"
        }
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    response = await service.update_contact(contact_id, body, user_id=user.id)
    print(response)
    return response


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def delete_contact(contact_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Delete a specific contact for the authenticated user.

    Permanently removes the specified contact from the user's contact list.
    This operation cannot be undone. Rate limited to 5 requests per 60 seconds.

    Args:
        contact_id (int): The unique identifier of the contact to delete.
        credentials (HTTPAuthorizationCredentials): JWT token for user authentication.

    Returns:
        None: Returns 204 No Content status on successful deletion.

    Raises:
        HTTPException: 401 if authentication fails, 404 if contact not found or
            not owned by the current user.

    Example:
        DELETE /contacts/123
    """
    token = credentials.credentials
    user = await auth_service.get_current_user(token)
    service = ContactService()
    await service.delete_contact(contact_id, user_id=user.id)


