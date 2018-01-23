from pprint import pprint
import logging

# import sys
# sys.path.insert(0, '/home/dbeath/code/feedsearch')

# from feedsearch import search
# from feedfinder2 import find_feeds
import Feedsearch

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('feedsearch')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

feeds = search('xkcd.com')

pprint(feeds)
