from feedfinder2 import find_feeds
import feedparser
import logging
import sys
import time


class GetFeedError(Exception):
    pass


def get_links(feed):
    """
    Returns a tuple containing the hub url and the self url for
    a parsed feed.

    :param feed: An RSS feed parsed by feedparser
    :type feed: dict
    :return: tuple
    """

    hub_url = None
    self_url = None
    autodiscovery_url = None

    try:
        for link in feed.feed.links:
            if link['rel'] == 'hub':
                hub_url = link['href']
            if link['rel'] == 'self':
                self_url = link['href']
            if link.get('id', None) == 'auto-discovery':
                autodiscovery_url = link['href']
    except AttributeError as e:
        logging.exception(e)
        return None

    if not hub_url and autodiscovery_url:
        return get_links(autodiscovery_url)

    return (hub_url, self_url)


def get_parsed_feed(feed_url):
    """
    Returns a parsed feed given a url.

    :param feed_url: Url of an RSS feed
    :type feed_url: str
    :return: dict
    """

    # r = requests.get(feed_url)
    # if r.status_code is not 200:
    #     raise GetFeedError('Response for url {0} had status {1}'.format(
    #         feed_url, r.status_code))
    try:
        parsed = feedparser.parse(feed_url)
    except:
        raise GetFeedError('Could not parse feed for url {0}'.format(feed_url))

    return parsed


def get_feed(url):
    """
    Given a URL, retrieves the default feed and gets a pubsubhubbub hub
    url. Returns the hub url, self url, and parsed feed.

    :param url: Any Url for a site
    :type url: str
    :return: tuple
    """

    try:
        feed_urls = find_feeds(url)
        logging.info('Feed Urls: {0}'.format(feed_urls))
        feed_url = feed_urls[0]
        logging.info('Feed Url: {0}'.format(feed_url))
    except Exception as e:
        logging.exception(e)
        raise GetFeedError(e)

    if feed_url is None:
        raise GetFeedError('Could not find feed.')

    parsed_feed = get_parsed_feed(feed_url)

    if parsed_feed is None:
        raise GetFeedError('Could not parse feed.')

    links = get_links(parsed_feed)
    logging.info('Links: {0}'.format(links))

    if links is None:
        raise GetFeedError('Could not get links from feed.')

    return (links[0], links[1], parsed_feed)


def main():
    # logger = logging.getLogger('FindFeeds')
    # logger.setLevel(logging.INFO)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    # logger.addHandler(ch)

    logging.basicConfig(level=logging.INFO)
    arg = sys.argv[1]
    logging.info('Finding feeds for {0}'.format(arg))

    start = time.time()
    try:
        # feeds = find_feeds(arg)
        # logging.info(feeds)

        result = get_feed(arg)
        logging.info('Hub: {0}, Self: {1}'.format(result[0], result[1]))
    except Exception as e:
        logging.exception(e)
    finally:
        end = time.time()
        logging.info('Time: {0}s'.format(end-start))

if __name__ == '__main__':
    main()
