import feedparser
import requests
import time
import urllib

start = time.time()
# f = requests.get("http://theguardian.com")
f = urllib.urlopen("http://theguardian.com")

mid = time.time()
print 'mid {0}'.format(mid - start)

# d = feedparser.parse(f.text)

# d = feedparser.parse("http://theguardian.com")

end = time.time()
print 'end {0}'.format(end - start)

# print d.feed.get('title')
# print d.feed.get('subtitle')
# print d.get('bozo')
# print d.version
# print d.get('status')
# print d.feed
