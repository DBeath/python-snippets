import feedparser
from werkzeug.contrib.atom import AtomFeed, FeedEntry
from pprint import pprint
from datetime import datetime


author = [
    dict(name='Test 1',
         email='test1@test.com',
         uri='http://test.com/test1'),
    dict(name='Test 2',
         email='test2@test.com',
         uri='http://test.com/test2')
]

# author = 'Yara Elmjouie for Tehran Bureau and Zoe Williams in Liverpool'

feed = AtomFeed(
    title='Test Feed',
    feed_url='http://testfeed.com'
)

entry = FeedEntry(
    title='Test Entry',
    url='http://testfeed.com/testentry',
    updated=datetime.utcnow(),
    content='Test Entry',
    author=author
)

feed.entries.append(entry)

rss = feed.to_string()

pprint(rss)
print()
print('------------------------------------------------------------')
# parsed = feedparser.parse(rss)
# parsed = feedparser.parse('http://www.vice.com/rss')

with open('vice.xml', 'r+') as f:
    vice = f.read()

parsed = feedparser.parse(vice)

entry = parsed.entries[0]
pprint(entry)


print('------------------------------------------------------------')
author1 = entry.authors[0]
name = author1.name
email = author1.get('email')
url = author1.get('href')
print(name)
print(email)
print(url)

print()
print('------------------------------------------------------------')
for e in parsed.entries:
    pprint(e.authors)
