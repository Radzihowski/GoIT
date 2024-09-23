# Використання однієї сесії при запитах
#
# Типовий підхід використовувати одну сесію для з'єднання з одним сервісом — це значно прискорює виконання кількох
# запитів на один і той самий сервіс. У у такому разі ви можете передавати створену сесію як аргумент у функцію:

import asyncio
import platform

import aiohttp


async def index(session):
    url = 'https://python.org'
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        return f"Body: {html[:15]}..."


async def doc(session):
    url = "https://www.python.org/doc/"
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        return f"Body: {html[:15]}..."


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(index(session), doc(session))
        return result


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

# Виведдення буде наступним:
# Status: 200
# Content-type: text/html; charset=utf-8
# Status: 200
# Content-type: text/html; charset=utf-8
# ['Body: <!doctype html>...', 'Body: <!doctype html>...']
