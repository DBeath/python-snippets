import asyncio
from feedfinder2 import find_feeds
import time

start = time.time()
urls = [
    "davidbeath.com",
    "theatlantic.com",
    "arstechnica.com"]

tasks = [find_feeds(url) for url in urls]

loop = asyncio.get_event_loop()

feeds = loop.run_until_complete(asyncio.gather(*tasks))

end = time.time()

print(feeds)
print('Time: {0}s'.format(end - start))
