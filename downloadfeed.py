import requests


feed = requests.get('http://davidbrin.blogspot.com/feeds/posts/default?alt=rss')

with open('davidbrin.html', 'w+') as f:
    f.write(feed.text.encode('utf-8'))
