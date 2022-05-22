from pathlib import Path
import asyncio
import requests

from fetcher import url_generator, crawl

url_path = "link_list.txt"


def test_url_generator():
    lst = Path(url_path).read_text().splitlines()
    gen = url_generator(url_path)

    for url_g, url_l in zip(gen, lst):
        assert url_g == url_l


def test_crawl():
    gen = url_generator(url_path)
    asyncio.run(crawl(gen, 5, outdir="downloaded"))
    for file, url in zip(Path("downloaded").iterdir(), gen):
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

        assert file.read_bytes() == r.content
