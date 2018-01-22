from bs4 import BeautifulSoup
import time
import feedparser

totalstart = time.time()
f = feedparser.parse("http://www.theguardian.com/international/rss")


for entry in f.get('entries'):
    start = time.time()
    soup = BeautifulSoup(entry.get('summary'), 'html.parser')
    text = soup.get_text()
    count = len(text.split(' '))
    end = time.time()
    total = end - start
    print('Count {0} in {1}'.format(count, total))

totalend = time.time()

print('Total time {0}'.format(totalend - totalstart))
