import feedparser
from werkzeug.contrib.atom import AtomFeed, FeedEntry
from datetime import datetime
from pprint import pprint


authors = [
    dict(name='Author 1',
         email='author1@test.com',
         uri='http://test.com/author1'),
    dict(name='Author 2',
         email='author2@test.com',
         uri='http://test.com/author2')
]


author = 'By Scott Bixby in New York and David Crouch (david@crouch.com) in Gothenburg'

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

parsed = feedparser.parse(rss)
pprint(parsed.feed)
print()
pprint(parsed.entries[0])
pprint(parsed.entries[0].author_detail)
print()
