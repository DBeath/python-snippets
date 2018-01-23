import requests
import feedparser
import time
from timeit import default_timer as timer

start = timer()

url = 'http://qz.com/feed/atom'

r = requests.get(url)

parsed = feedparser.parse(r.text)
print(len(parsed.entries))
end = timer()

print("Time: {0}".format(end - start))
