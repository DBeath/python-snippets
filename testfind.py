# from feedfinder2_upgraded import find_feeds
from feedfinder2 import find_feeds
from pprint import pprint

# url = "http://boingboing.net"
url = "http://localhost:5000/author/1"

feeds = find_feeds(url)
pprint(feeds)
