# Набір параметрів сесії
#
# Кожен об'єкт ClientSession може бути індивідуально налаштований, щоб усі запити у цій сесії використовували загальний
# набір параметрів. Для цього ви можете передати в сесію набір параметрів запиту і всі вони будуть автоматично додані у
# кожен запит цієї сесії:

import platform
import aiohttp
import asyncio
from uuid import uuid4

async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(
        headers={"Request-Id": str(uuid4())},
        timeout=timeout,
    ) as session:
        async with session.get('https://python.org') as response:
            print("Status:", response.status)
            print("Content-style:", response.headers['content-type'])
            html = await response.text()
            return f"Body: {html[:15]}..."

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

# У цьому прикладі всім запитам у цій сесії встановили в заголовок поле Request-Id та таймаут на читання 1 секунди.