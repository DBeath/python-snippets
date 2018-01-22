import requests
import urllib2
import time
import feedparser

url = "http://theguardian.com"

rstart = time.time()
r = requests.get(url, verify=False)
rend = time.time()

print 'Requests: {0}'.format(rend - rstart)

fstart = time.time()
f = feedparser.parse(url)
fend = time.time()

print 'Feedparser: {0}'.format(fend - fstart)

ustart = time.time()
u = urllib2.urlopen(url)
uend = time.time()

print 'Urllib: {0}'.format(uend - ustart)
