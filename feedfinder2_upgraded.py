#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

__version__ = "0.0.3"

try:
    __FEEDFINDER2_SETUP__
except NameError:
    __FEEDFINDER2_SETUP__ = False

if not __FEEDFINDER2_SETUP__:
    __all__ = ["find_feeds"]

    import logging
    import requests
    from bs4 import BeautifulSoup
    from six.moves.urllib import parse as urlparse
    import feedparser


def coerce_url(url):
    url = url.strip()
    if url.startswith("feed://"):
        return "http://{0}".format(url[7:])
    for proto in ["http://", "https://"]:
        if url.startswith(proto):
            return url
    return "http://{0}".format(url)


class FeedInfo(object):

    def __init__(self, link, soup=None):
        parsed = feedparser.parse(link)
        self.link = link

        if soup:
            self.icon_link = self.find_icon_link(soup)
            if self.icon_link:
                self.icon = self.get_icon(self.icon_link)
            self.website = self.get_website(soup)

        if parsed:
            self.title = self.find_title(parsed)
            self.description = self.find_description(parsed)

    def find_icon_link(self, soup):
        self.icon_link = soup.find("link", rel="shortcut icon")

    def get_icon(self, link):
        self.icon = requests.get(link)

    def find_title(self, parsed):
        title = parsed.feed.get('title', None)
        if not title:
            return
        self.title = self.clean_title(title)

    def clean_title(self, title):
        try:
            title = BeautifulSoup(title, 'html.parser').get_text()
            if len(title) > 1024:
                title = title[:1020] + u'...'
            return title
        except Exception as e:
            logging.exception(u'Failed to clean title: {0}'.format(e))

    def find_description(self, parsed):
        subtitle = parsed.feed.get('subtitle', None)
        if subtitle:
            self.description = subtitle
        else:
            self.description = parsed.feed.get('description', None)

    def get_website(self, soup):
        self.website = soup.find("link", rel="canonical")


class FeedFinder(object):

    def __init__(self, user_agent=None):
        if user_agent is None:
            user_agent = "feedfinder2/{0}".format(__version__)
        self.user_agent = user_agent

    def get_feed(self, url):
        try:
            r = requests.get(url, headers={"User-Agent": self.user_agent})
        except Exception as e:
            logging.warn("Error while getting '{0}'".format(url))
            logging.warn("{0}".format(e))
            return None
        return r

    def is_feed_data(self, text):
        data = text.lower()
        if data.count("<html"):
            return False
        return data.count("<rss")+data.count("<rdf")+data.count("<feed")

    def is_feed(self, url):
        r = self.get_feed(url)
        if not r:
            return False
        text = r.text
        if not text:
            return False
        return self.is_feed_data(text)

    def is_feed_url(self, url):
        return any(map(url.lower().endswith,
                       [".rss", ".rdf", ".xml", ".atom"]))

    def is_feedlike_url(self, url):
        return any(map(url.lower().count,
                       ["rss", "rdf", "xml", "atom", "feed"]))


def find_feeds(url, check_all=False, user_agent=None):
    finder = FeedFinder(user_agent=user_agent)

    # Format the URL properly.
    url = coerce_url(url)

    # Download the requested URL.
    response = finder.get_feed(url)
    text = response.text
    if text is None:
        return []

    # Check if it is already a feed.
    if finder.is_feed_data(text):
        return [url]

    # Look for <link> tags.
    logging.info("Looking for <link> tags.")
    tree = BeautifulSoup(text, "html.parser")
    links = []
    for link in tree.find_all("link"):
        if link.get("type") in ["application/rss+xml",
                                "text/xml",
                                "application/atom+xml",
                                "application/x.atom+xml",
                                "application/x-atom+xml"]:
            links.append(urlparse.urljoin(url, link.get("href", "")))

    # Check the detected links.
    urls = list(filter(finder.is_feed, links))
    logging.info("Found {0} feed <link> tags.".format(len(urls)))
    if len(urls) and not check_all:
        return sort_urls(urls)

    # Look for <a> tags.
    logging.info("Looking for <a> tags.")
    local, remote = [], []
    for a in tree.find_all("a"):
        href = a.get("href", None)
        if href is None:
            continue
        if "://" not in href and finder.is_feed_url(href):
            local.append(href)
        if finder.is_feedlike_url(href):
            remote.append(href)

    # Check the local URLs.
    local = [urlparse.urljoin(url, l) for l in local]
    urls += list(filter(finder.is_feed, local))
    logging.info("Found {0} local <a> links to feeds.".format(len(urls)))
    if len(urls) and not check_all:
        return sort_urls(urls)

    # Check the remote URLs.
    remote = [urlparse.urljoin(url, l) for l in remote]
    urls += list(filter(finder.is_feed, remote))
    logging.info("Found {0} remote <a> links to feeds.".format(len(urls)))
    if len(urls) and not check_all:
        return sort_urls(urls)

    # Guessing potential URLs.
    fns = ["atom.xml", "index.atom", "index.rdf", "rss.xml", "index.xml",
           "index.rss"]
    urls += list(filter(finder.is_feed, [urlparse.urljoin(url, f)
                                         for f in fns]))
    sorted_urls = sort_urls(urls)

    feedinfos = []
    for url in sorted_urls:
        feedinfos.append(FeedInfo(url, tree))

    print(feedinfos)
    return feedinfos


def url_feed_prob(url):
    if "comments" in url:
        return -2
    if "georss" in url:
        return -1
    kw = ["atom", "rss", "rdf", ".xml", "feed"]
    for p, t in zip(range(len(kw), 0, -1), kw):
        if t in url:
            return p
    return 0


def sort_urls(feeds):
    return sorted(list(set(feeds)), key=url_feed_prob, reverse=True)


if __name__ == "__main__":
    print(find_feeds("www.preposterousuniverse.com/blog/"))
    print(find_feeds("http://xkcd.com"))
    print(find_feeds("dan.iel.fm/atom.xml"))
    print(find_feeds("dan.iel.fm", check_all=True))
    print(find_feeds("kapadia.github.io"))
    print(find_feeds("blog.jonathansick.ca"))
    print(find_feeds("asdasd"))
