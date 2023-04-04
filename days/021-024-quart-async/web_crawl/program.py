import asyncio
import bs4
from colorama import Fore
import aiohttp

# Time stats to beat:
# real    0m5.004s
# user    0m1.460s
# sys     0m0.049s

# Time Beat
# real    0m0.809s
# user    0m0.521s
# sys     0m0.033s


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            html = await resp.text()
            print(Fore.RED + f"HTML received for episode {episode_number}", flush=True)
            return html


async def get_title(episode_number: int) -> str:
    """This function uses the Chaining Coroutines Design from
    https://realpython.com/async-io-python/#chaining-coroutines
    """
    html = await get_html(episode_number)
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        raise Exception("MISSING")

    title = header.text.strip()
    print(Fore.WHITE + f"Title found: {title}", flush=True)


def main():
    asyncio.run(get_title_range())
    print("Done.")


async def get_title_range():
    # Please keep this range pretty small to not DDoS my site. ;)
    await asyncio.gather(*(get_title(n) for n in range(150, 170)))


if __name__ == '__main__':
    main()
