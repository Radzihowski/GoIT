# Створюємо репозиторій користувача
from datetime import datetime, timedelta
from sqlalchemy import select, exists, delete, or_, func

from src.database.db import sessionmanager
from src.database.models import User
from src.schemas.users import UserModel


async def get_user_by_email(email: str) -> User:
    async with sessionmanager.session() as session:
        query = select(User).where(User.email == email)
        print(query)
        result = await session.execute(query)
        print(result)
        return result.scalar()


async def create_user(body: UserModel) -> User:
    async with sessionmanager.session() as session:
        async with session.begin():
            new_user = User(email=body.email, password=body.password)
            session.add(new_user)
            await session.flush()
            user_id = new_user.id
        print(f"User {body.first_name} added successfully!")
        return user


async def update_token(user: User, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()
