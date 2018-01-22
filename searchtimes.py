import sys
sys.path.insert(0, '/home/dbeath/code/feedsearch')

from feedsearch import search
from feedfinder2 import find_feeds

import time

# url = 'https://theatlantic.com'
url = 'jsonfeed.org'

start1 = time.perf_counter()

result1 = search(url, info=True)

dur1 = int((time.perf_counter() - start1) * 1000)

start2 = time.perf_counter()

result2 = find_feeds(url)

dur2 = int((time.perf_counter() - start2) * 1000)

print()
print(f'Feedsearch: Time {dur1}ms, Found {result1}')
print(f'Feedfinder2: Time {dur2}ms, Found {result2}')
