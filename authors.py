import feedparser
import requests

# feed = requests.get("http://pushtester.feedrsub.com/feeds/4/rss")

# f = open('testfeed.xml', 'w+')
# f.write(feed.text)
# f.close()

d = None

with open('testfeed.xml', 'r+') as f:
    d = f.read()

p = feedparser.parse(d)

for i in p.entries:
    print i.author
    print i.author_detail
    print
