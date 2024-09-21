# Пакет aiopath​
#
# Якщо ви пишете асинхронний код Python і хочете скористатися перевагами pathlib, але не хочете змішувати блокуюче та
# неблокуюче введення-виведення, ви можете звернутися до aiopath . API aiopath прямо збігається з API pathlib, але всі
# необхідні методи асинхронні.
#
# Наприклад, перевіримо, чи існує файл "hello.txt" у поточній папці:

import asyncio
from aiopath import AsyncPath

async def main():
    apath = AsyncPath("hello.txt")
    print(await apath.exists())
    print(await apath.is_file())
    print(await apath.is_dir())

if __name__ == "__main__":
    asyncio.run(main())

# Якщо файл є, виведення буде наступним:
# True
# True
# False