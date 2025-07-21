import json

import requests
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}
# Параметри шляху (Path)
# Path параметр маршруту - це параметр, який визначає частину URL, що повинна збігатися з визначеним значенням під час
# виклику маршруту. Path параметри позначаються за допомогою фігурних дужок {} та можуть використовуватися для
# отримання динамічного контенту, наприклад, під час запиту конкретного користувача або запису в БД. Наприклад,
# маршрут /notes/{note_id} використовує path параметр note_id для ідентифікації конкретного запису в запиті.

@app.get("/notes/new")
async def read_new_notes():
    return {"message": "Return new notes"}


@app.get("/notes/{note_id}")
async def read_note(note_id: int = Path(description="The ID of the note to get", gt=0, le=10)):
    return {"note": note_id}


# Параметри запиту (Query)
# Параметри запиту (Query) - це набір пар "ключ=значення", що йдуть після URL-адреси після знаку ? та розділені
# символом &. Вони використовуються для передачі додаткової інформації у запиті, наприклад, фільтри, пагінація
# та сортування.

@app.get("/notes")
async def read_notes(skip: int = 0, limit: int = Query(default=10, le=100, ge=10)):
    return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}

# For example, in the following case, the q parameter in the route is optional q: str | None = None)
# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = 10, q: str | None = None):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}

# FastAPI дозволяє оголошувати додаткову інформацію та перевірку параметрів. Для цього потрібно імпортувати Query з
# fastapi. Наприклад, встановимо, що значення limit може лежати в межах від 10 до 100.


# Тіло запиту (Body)
#
# Тіло запиту - це дані, які передаються разом з HTTP запитом на сервер. Вони можуть бути у форматі JSON, XML, або
# іншому форматі, та використовуються для передачі додаткової інформації від клієнта до сервера, наприклад, форми даних,
# файли або дані для створення або зміни об'єкта на сервері.

class Note(BaseModel):
    name: str
    description: str
    done: bool

@app.post("/notes")
async def create_note(note: Note):
    return {"name": note.name, "description": note.description, "status": note.done}

# В цьому прикладі ми створюємо клас Note, який визначає три поля: name (рядок str), description ( рядок str) та done
# (булеве значення bool). Потім визначаємо функцію create_note, яка приймає аргумент note типу Note. Функція повертає
# словник {"name": note.name, "description": note.description, "status": note.done}.
# Декоратор @app.post("/notes") реєструє функцію create_note в якості обробника POST-запитів на маршрут /notes.

# Наприклад, в Python за допомогою використання бібліотеки requests можна відправити тіло запиту у форматі JSON
# наступним чином:
data = {"name": "Test note", "description": "Testing", "done": False}
headers = {'Content-type': 'application/json'}

responce = requests.post('http://127.0.0.1:8000/notes', data=json.dumps(data), headers=headers)

print(responce.json())

# На цьому прикладі ми відправляємо POST-запит на URL http://127.0.0.1:8000/notes разом з тілом запиту у форматі JSON
# та заголовком Content-type: application/json. FastAPI автоматично валідує тіло запиту та перетворює його в об'єкт
# типу Note. Потім функція create_note буде викликана разом з аргументом note, що містить в собі об'єкт Note з полями
# name="Test note", "description": "Testing" та "done": False.