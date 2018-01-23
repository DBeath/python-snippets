import requests
from pprint import pprint
import sys

baseurl = 'https://cloud.feedly.com/v3/'

searchurl = 'search/feeds'

query = sys.argv[1]

full_url = baseurl + searchurl

payload = {'query': query}

r = requests.get(full_url, params=payload)

pprint(r.text)
