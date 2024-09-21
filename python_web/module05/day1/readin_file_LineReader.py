# LineReader — помічник, який дуже ефективний, коли ви хочете прочитати файл лінійно та рядково. Він містить буфер і
# зчитуватиме фрагменти файлу частинами в буфер, де намагатиметься знайти рядки. Розмір фрагмента за замовчуванням
# складає 4 КБ.

import asyncio
from aiofile import AIOFile, LineReader

async def main():
    async with AIOFile("hello.txt", 'r') as afp:
        async for line in LineReader(afp):
            print(line)

if __name__ == "__main__":
    asyncio.run(main())