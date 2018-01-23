import requests
from pprint import pprint

search_url = 'davidbeath.com'
feedsearch_url = 'https://feedsearch.auctorial.com/search'

payload = {'url': search_url}
r = requests.get(feedsearch_url, params=payload)

print(r.status_code)
pprint(r.headers)
print()
pprint(r.text)
print()
pprint(r.json())
