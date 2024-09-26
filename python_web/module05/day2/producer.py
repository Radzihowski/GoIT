# Відправлятимемо повідомлення за допомогою producer. Ми підключаємося до веб-сокету так само, як робили це раніше з
# consumer. А далі відправляємо асинхронне повідомлення на сервер await ws.send(message) та відключаємося.

import asyncio
import websockets
import sys

async def producer(message: str, host: str, port: int):
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)

if __name__ == '__main__':
    asyncio.run(producer(message=sys.argv[1], host='localhost', port=4000))
