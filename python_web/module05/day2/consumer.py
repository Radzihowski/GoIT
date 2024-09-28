import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)

async def consumer(hostname: str, port: int):
    ws_resource_url = f"ws://{hostname}:{port}"
    try:
        async with websockets.connect(ws_resource_url) as ws:
            async for message in ws:
                logging.info(f"Message: {message}")
    except websockets.ConnectionClosedError as e:
        logging.error(f"Connection closed with error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(consumer('localhost', 4000))
