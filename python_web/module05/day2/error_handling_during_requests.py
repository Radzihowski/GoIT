import aiohttp
import asyncio
import platform

urls = ['https://www.google.com', 'https://www.python.org/asdf', 'https://duckduckgo.com', 'http://test']

async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(f'Starting {url}')
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        html = await resp.text()
                        print(url, html[:150])
                    else:
                        print(f"Error status: {resp.status}) for {url}")
            except aiohttp.ClientConnectorError as err:
                print(f"Connection error: {url}", str(err))

if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

# Виведення:
# Starting https://www.google.com
# https://www.google.com <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="uk"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Ty
# Starting https://www.python.org/asdf
# Error status: 404 for https://www.python.org/asdf
# Starting https://duckduckgo.com
# https://duckduckgo.com <!DOCTYPE html>
# <!--[if IEMobile 7 ]> <html lang="en-US" class="no-js iem7"> <![endif]-->
# <!--[if lt IE 7]> <html class="ie6 lt-ie10 lt-ie9 lt-ie8 lt-
# Starting http://test
# Connection error: http://test Cannot connect to host test:80 ssl:default [getaddrinfo failed]