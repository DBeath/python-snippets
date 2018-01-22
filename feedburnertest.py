import feedparser
from pprint import pprint

url = 'http://feeds.feedburner.com/TheAtlantic'

parsed = feedparser.parse(url)

for item in parsed.get('items'):
    # pprint(item.get('title'))
    # pprint(item.get('feedburner_origlink'))
    # pprint(item.get('link'))
    # print()
    del item['content']
    del item['summary']
    pprint(item)
    print()
