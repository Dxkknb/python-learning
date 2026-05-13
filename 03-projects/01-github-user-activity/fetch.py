import aiohttp


async def fetch_user_data(session: aiohttp.ClientSession, url: str) -> list[dict]:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()
