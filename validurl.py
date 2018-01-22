from urllib.parse import urlparse
import pprint
import requests

urls = ['b', 'boingboing', 'boingboing.net', 'http://boingboing.net',
        'http://www.boingboing.net', 'www.boingboing.net', 'www.boingboing',
        'http://boingboing']

for url in urls:
    print('URL: {0}'.format(url))
    parsed = urlparse(url)
    print(parsed)

    try:
        r = requests.get(url)
        print(r)
    except Exception as e:
        print(e)

    print()
