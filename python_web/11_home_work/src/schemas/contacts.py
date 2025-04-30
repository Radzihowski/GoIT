from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, PastDate


class ContactRequest(BaseModel):
    first_name: str = Field(max_length=56, min_length=2)
    last_name: str = Field(max_length=56, min_length=2)
    email: str = EmailStr()
    phone: str = Field()
    date_of_birth: date = PastDate()
    info: str | None = Field(max_length=1024)


class ContactResponse(ContactRequest):
    id: int

    class Config:
        orm_mode = True
