# Бібліотека aioshutil надає асинхронну версію функції модуля Shutil.
#
# Модуль Shutil є синхронним, та його використання в асинхронних застосунках заблокує цикл подій і уповільнить роботу
# застосунку, aioshutil надає асинхронні дружні версії функцій модуля Shutil.
# Для прикладу, давайте ми створимо папку logs та скопіюємо туди наш файл "hello.txt"

import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile

async def main():
    apath = AsyncPath('hello.txt')
    if await apath.exists():
        new_path = AsyncPath('logs')
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)

if __name__ == '__main__':
    asyncio.run(main())