import time
from pprint import pprint

from feedfinder2 import find_feeds

from feedsearch import search

# url = 'http://nymag.com/newyork/rss/'
url = 'http://arstechnica.com'

start1 = time.perf_counter()

result1 = search(url, info=True, check_all=False)

time1 = int((time.perf_counter() - start1) * 1000)

start2 = time.perf_counter()

result2 = find_feeds(url, check_all=False)

time2 = int((time.perf_counter() - start2) * 1000)

print()
print(f'Feedsearch searched url in {time1}ms: Found: {result1}')
print(f'Feedfinder2 searched url in {time2}ms: Found: {result2}')

print()
for r in result1:
    pprint(vars(r))
print()
pprint(result2)
