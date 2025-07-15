from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl

class User(BaseModel):
    name: str
    email: EmailStr
    website: HttpUrl
    age: Optional[int] = Field(None, ge=13, le=90)
    friends: Optional[int] = 0

user = User(name="John", email="john@examle.com", website="https://john.com", age=45, friends=10)
print(user)

user = User(name="Jane", email="jone@examle.com", website="https://jane.com", age=12, friends=25)
print(user)

user = User(name="Bob", email="bob@examle.com", website="hhtp://bob", age=40)
print(user)

