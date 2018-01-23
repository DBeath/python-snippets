import feedparser
from pprint import pprint

with open('jsonfeed.json', 'r') as feed:
    text = feed.read()

# url = 'http://feeds.feedburner.com/TheAtlantic'
url = "http://feeds.feedburner.com/nymag/vulture"

parsed = feedparser.parse(text)

pprint(parsed)

pprint(parsed.get('namespaces'))
pprint(parsed.entries[0])
