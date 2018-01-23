from werkzeug.http import parse_options_header
import requests


def parse_content_type(content_type):
    if isinstance(content_type, (tuple, list)):
        content_type = content_type[0].lower()
    return content_type

url = 'https://boingboing.net/feed'
# url = 'http://qz.com/feed/atom/'


r = requests.get(url)


headers = r.headers.get('content-type')

print(headers)

parsed = parse_options_header(headers)
print(parsed)

print(type(parsed))

ct = parse_content_type(parsed)
print(ct)
print(type(ct))
