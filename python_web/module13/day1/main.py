# Код надсилання листа
# розбираємо механізм надсилання листа за допомогою пакета Fastapi-mail

from pathlib import Path

import  uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydetic import EmailStr, BaseModel
from typing import List

class EmailSchema(BaseModel):
    email: EmailStr

    conf = ConnectionConfig(
        MAIL_USERNAME="example@meta.ua",
        MAIL_PASSWORD="secretPassword",
        MAIL_FROM="example@meta.ua",
        MAIL_PORT=465,
        MAIL_SERVER="smtp.meta.ua",
        MAIL_FROM_NAME="Example email",
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=True,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
        TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
    )