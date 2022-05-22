import argparse
import asyncio

import aiofiles
import aiohttp


def url_generator(urls):
    with open(urls, "r") as urls_file:
        for url in urls_file:
            url = url.strip()
            if not url:
                continue
            yield url


async def fetch(name, session, q, outdir):
    while True:
        url = await q.get()
        try:
            async with session.get(url) as resp:
                file_path = f"{outdir}/{name}.html"
                f = await aiofiles.open(file_path, mode="wb")
                await f.write(await resp.read())
                await f.close()
        except Exception as e:
            print(file_path, e)
        finally:
            q.task_done()
            print(f"{name}: {url}")


async def crawl(urls, threads=5, headers=None, outdir="."):
    q = asyncio.Queue()
    for url in urls:
        await q.put(url)

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [
            asyncio.create_task(fetch(f"coro_{i}", session, q, outdir))
            for i in range(threads)
        ]
        await q.join()

    for t in tasks:
        t.cancel()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", type=str, help="urls file")
    parser.add_argument("-c", "--threads", type=int, default=5, help="threads")
    parser.add_argument("--outdir", type=str, default=".", help="output directory")
    return parser.parse_args()


def main():
    args = parse_args()
    urls = url_generator(args.urls)
    asyncio.run(crawl(urls, args.threads, outdir=args.outdir))


if __name__ == "__main__":
    main()
