import aiohttp
import asyncio

async def fetch(session, url):
    with aiohttp.Timeout(10, loop=session.loop):
        async with session.get(url) as response:
            return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        a = await fetch(session, 'http://httpbin.org/ip')
        b = await fetch(session, 'http://httpbin.org/ip')
        print(a,b)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))