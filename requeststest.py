import requests
from pprint import pprint

url = 'https://arstechnica.com'

with requests.Session() as s:
    r = s.get(url)
    pprint(r.request.headers)
    print()
    pprint(r.headers)
    print()

r = requests.get(url)
pprint(r.request.headers)
print()
pprint(r.headers)
print()
