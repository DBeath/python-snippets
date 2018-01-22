import feedparser
# from urlparse import urlparse

# f = feedparser.parse("http://davidbrin.blogspot.com/feeds/posts/default")
f = feedparser.parse('blah blah')

print(f.get('status'))
print(f.get('bozo'))
print(f.get('bozo_exception'))
feed = f.get('feed')
print(feed.get('title'))
print(feed.get('info'))
print(feed.get('link'))
print(feed.get('description'))
print(feed.get('subtitle'))
print(feed.get('icon'))
print(feed.get('links'))

for e in f.get('entries'):
    print(e.get('title'))
    print(e.get('author'))

# parsed_uri = urlparse(feed.get('link'))
# domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
# print(domain)
