import asyncio
import platform
import sys
import time
from datetime import datetime, timedelta

import aiohttp

async def get_data(session, day):
    # link = "https://660951750f324a9a28831e25.mockapi.io/test/exchange_rates"
    link = f'https://api.privatbank.ua/p24api/exchange_rates?date={day}'
    async with session.get(link) as response:
        result = await response.json()
        return result

async def main():
    param = sys.argv
    if len(param) < 2:
        print("Enter number of days")
        return
    else:
        day_count = int(param[1])
        if day_count > 10 and day_count < 1:
            print("Parameters should be between 1 and 10")
            return

    dates = []

    for i in range(1, day_count + 1):
        date_stamp = datetime.now() - timedelta(days=i)
        date_stamp_str = date_stamp.strftime('%d.%m.%Y')
        print(date_stamp_str)
        dates.append(date_stamp_str)

    async with aiohttp.ClientSession() as session:
        coroutines = [get_data(session, day) for day in dates]
        result = await asyncio.gather(*coroutines)
        print(result)

if __name__ == "__main__":
    start = time.time()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)
    stop = time.time()
    print(f"Execution time = {stop - start}")
