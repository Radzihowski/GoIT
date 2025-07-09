import re
from datetime import date, timedelta, datetime
from pprint import pprint

from pydantic import BaseModel, Field, PastDate, field_validator


class ContactRequest(BaseModel):  # визначаємо вхідні дані
    first_name: str = Field(max_length=56, min_length=2)
    last_name: str = Field(max_length=56, min_length=2)
    email: str = Field()
    phone: str = Field()
    date_of_birth: date = Field()
    info: str | None = Field(max_length=1024)

    @field_validator('email', mode='before')
    @classmethod
    def email_checker(cls, value: str) -> str:
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, value):
            return value
        else:
            raise ValueError('Email not valid')

    @field_validator('date_of_birth', mode='before')
    @classmethod
    def date_of_birth_checker(cls, value: str) -> date:
        birth_day = datetime.strptime(value, "%d-%m-%Y").date()
        date_18 = (datetime.now() - timedelta(days=18 * 365)).date()
        if date_18 < birth_day:
            raise ValueError("User must be 18+")
        else:
            return birth_day


class ContactResponse(BaseModel):  # визначаємо вихідні дані повертає айдішнік інт
    id: int

    class Config:
        from_attributes = True
