"""
Repository functions for user management, including user creation, retrieval, token updates,
email confirmation, and avatar updates.
"""

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from src.database.db import sessionmanager
from src.database.models import User
from src.schemas.users import UserModel


async def get_user_by_email(email: str) -> User:
    """
    Retrieve a user by their email address.

    Args:
        email (str): The email address of the user to retrieve.

    Returns:
        User or None: The user object if found, else None.
    """
    async with sessionmanager.session() as session:
        query = select(User).where(User.email == email)
        print(query)
        result = await session.execute(query)
        print(result)
        return result.scalar()


async def create_user(body: UserModel) -> dict:
    """
    Create a new user in the database.

    Args:
        body (UserModel): The user data for creation.

    Returns:
        dict: A dictionary with the new user's id, email, created_at, and avatar.
    """
    async with sessionmanager.session() as session:
        async with session.begin():
            new_user = User(email=body.email, password=body.password)
            session.add(new_user)
            await session.flush()
            user_id = new_user.id
            user_email = new_user.email
            created_at = new_user.created_at
            avatar = new_user.avatar
        print(f"User {body.email} added successfully!")
        return {"id": user_id, "email": user_email, "created_at": created_at, "avatar": avatar}


async def update_token(user: User, token: str | None) -> None:
    """
    Update the refresh token for a user.

    Args:
        user (User): The user whose token is to be updated.
        token (str | None): The new refresh token value.

    Returns:
        None
    """
    async with sessionmanager.session() as session:
        stmt = (
            update(User)
            .where(User.id == user.id)     # ✅ filter by user!
            .values(refresh_token=token)
        )
        await session.execute(stmt)
        await session.commit()

async def confirmed_email(email: str) -> None:
    """
    Mark a user's email as confirmed.

    Args:
        email (str): The email address of the user to confirm.

    Returns:
        None
    """
    async with sessionmanager.session() as session:
        stmt = (
            update(User)
            .where(User.email == email)     # ✅ filter by user!
            .values(confirmed=True)
        )
        await session.execute(stmt)
        await session.commit()

async def update_avatar(email, url: str) -> None:
    """
    Update the avatar URL for a user and return updated user info.

    Args:
        email (str): The email address of the user whose avatar is to be updated.
        url (str): The new avatar URL.

    Returns:
        dict: A dictionary with the user's id, email, created_at, and updated avatar.
    """
    async with sessionmanager.session() as session:
        stmt = (
            update(User)
            .where(User.email == email)     # ✅ filter by user!
            .values(avatar=url)
        )
        await session.execute(stmt)
        await session.commit()
    user=await get_user_by_email(email)
    user_id = user.id
    user_email = user.email
    created_at = user.created_at
    avatar = user.avatar
    return {"id": user_id, "email": user_email, "created_at": created_at, "avatar": avatar}

