import asyncio
from feedfinder2 import find_feeds

url = "xkcd.com"

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(find_feeds(url))
feeds = loop.run_until_complete(task)

print(feeds)
