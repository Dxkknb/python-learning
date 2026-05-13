import asyncio
import aiohttp
import fetch
import user


async def main():
    username = user.get_username()
    url = f"https://api.github.com/users/{username}/events"

    async with aiohttp.ClientSession() as session:
        data = await fetch.fetch_user_data(session, url)
        item = data[0]

        print(f"""
        - Pushed {len(data)} commit to {item['repo']['name']}
        - Opened a new issue in {item['repo']['name']}
        - Starred {item['repo']['name']}
        - ...
        """)


if __name__ == "__main__":
    asyncio.run(main())
